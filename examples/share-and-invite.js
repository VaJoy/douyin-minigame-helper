/**
 * 分享与邀请：被动分享内容 + 主动分享 + 邀请参数回传
 *
 * 用法：
 *   const Share = require('./share-and-invite');
 *   Share.setupPassive(() => ({ title: '我在第 12 关等你', query: 'from=passive' }));
 *   Share.invite({ uid: '123', level: 12 });
 *
 * 说明：
 * - 被动分享：用户点右上角「更多 → 分享」时触发，回调里返回内容；
 * - 主动分享：游戏内按钮调用 tt.shareAppMessage；
 * - 被邀请方通过 tt.getLaunchOptionsSync().query 拿到参数。
 */
const Share = (() => {
  /** 注册被动分享，provider 返回 { title, desc, imageUrl, query, templateId } */
  function setupPassive(provider) {
    tt.onShareAppMessage(() => provider());
  }

  function showMenu() {
    tt.showShareMenu({ success() {}, fail() {} });
  }

  function hideMenu() {
    tt.hideShareMenu({ success() {}, fail() {} });
  }

  /** 主动分享；resolve(true) 表示分享成功 */
  function share(param) {
    return new Promise((resolve) => {
      tt.shareAppMessage({
        ...param,
        success(res) { resolve(res); },
        fail(res) {
          console.warn('[share] fail', res.errMsg);
          resolve(null);
        },
      });
    });
  }

  /** 邀请好友：channel=invite，成功回调可能带回被邀请人信息 */
  function invite({ uid, level, channel = 'invite' }) {
    return share({
      channel,
      title: '一起来玩，组队有奖励',
      desc: `好友邀请你挑战第 ${level} 关`,
      query: `from=invite&inviter=${encodeURIComponent(uid)}&level=${level}`,
    });
  }

  /** 冷启动时读取分享/邀请带来的参数 */
  function readLaunchQuery() {
    const { query = {}, scene } = tt.getLaunchOptionsSync();
    return { query, scene, fromInvite: query.from === 'invite' };
  }

  return { setupPassive, showMenu, hideMenu, share, invite, readLaunchQuery };
})();

module.exports = Share;
