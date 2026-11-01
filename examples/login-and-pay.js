/**
 * 登录 + 下单：前端只负责拿 code 与调起支付，openid 与发货都在服务端
 *
 * 用法：
 *   const Account = require('./login-and-pay');
 *   const session = await Account.login();       // { openid, sessionKey? }
 *   await Account.pay({ amount: 6, customId: 'order_001' });
 *
 * 服务端需实现：
 *   POST /api/login   { code } -> { openid }
 *   POST /api/pay     { openid, orderId } -> { ok }
 *   支付回调验签后按 customId 幂等发货
 */
const Account = (() => {
  const API_BASE = 'https://your-server.com';

  function request(url, data) {
    return new Promise((resolve, reject) => {
      tt.request({
        url: API_BASE + url,
        method: 'POST',
        header: { 'content-type': 'application/json' },
        data,
        success(res) {
          if (res.statusCode === 200 && res.data && res.data.ok) resolve(res.data);
          else reject(res.data || res);
        },
        fail: reject,
      });
    });
  }

  /** 静默登录：拿 code 换 openid，前端不接触 session_key */
  function login() {
    return new Promise((resolve, reject) => {
      tt.login({
        force: false, // 不强制弹登录框，先用匿名态
        success(res) {
          const code = res.code || res.anonymousCode;
          if (!code) return reject(new Error('未取到登录凭证'));
          request('/api/login', { code, anonymous: !res.code })
            .then((data) => resolve({ openid: data.openid, isLogin: res.isLogin }))
            .catch(reject);
        },
        fail: reject,
      });
    });
  }

  /** 检查登录态是否还有效（服务端校验 session_key） */
  function checkSession() {
    return request('/api/check-session', {});
  }

  /**
   * 发起内购
   * @param {number} amount 金额（元），必须是平台限定价位
   * @param {string} customId 商户订单号，全局唯一
   */
  async function pay({ amount, customId, extraInfo = '' }) {
    const canDirectBuy = tt.canIUse('requestGamePayment.object.goodType');

    // 让服务端先落单，避免前端自造订单号
    const order = await request('/api/pay', { amount, customId });

    return new Promise((resolve, reject) => {
      tt.requestGamePayment({
        mode: 'game',
        env: 0,
        currencyType: 'CNY',
        platform: 'android',
        zoneId: '1',
        customId: order.orderId,
        extraInfo,
        // 道具直购（3.47.0+）需要这两个字段；否则走游戏币
        ...(canDirectBuy
          ? { goodType: 2, orderAmount: Math.round(amount * 100), goodName: order.goodName }
          : { buyQuantity: order.buyQuantity }),
        success(res) {
          // 只代表支付流程走完，发货以服务端回调为准
          resolve({ ok: true, raw: res, orderId: order.orderId });
        },
        fail(res) {
          reject(new Error(res.errMsg || '支付失败'));
        },
      });
    });
  }

  return { login, checkSession, pay };
})();

module.exports = Account;
