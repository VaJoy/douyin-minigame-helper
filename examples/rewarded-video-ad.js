/**
 * 激励视频广告：单例管理 + 预加载 + 发奖判定
 *
 * 用法：
 *   const AdManager = require('./rewarded-video-ad');
 *   AdManager.init('YOUR_AD_UNIT_ID');
 *   AdManager.show().then(() => grantReward()).catch(() => toast('暂无广告'));
 *
 * 说明：
 * - 广告实例全局只创建一次，重复 create 会累积资源；
 * - 必须在 onClose 里判断 res.isEnded，show() 成功不代表看完了；
 * - 首次 show 失败通常是没预加载，load 后再试一次。
 */
const AdManager = (() => {
  let ad = null;
  let loaded = false;
  let pendingResolve = null;
  let pendingReject = null;

  function init(adUnitId) {
    if (ad) return ad;
    ad = tt.createRewardedVideoAd({ adUnitId });

    ad.onLoad(() => {
      loaded = true;
    });

    ad.onError((err) => {
      loaded = false;
      console.warn('[ad] error', err.errCode, err.errMsg);
      if (pendingReject) {
        pendingReject(err);
        pendingResolve = pendingReject = null;
      }
    });

    ad.onClose((res) => {
      loaded = false;
      if (pendingResolve) {
        // isEnded 为 true 才算完整观看
        pendingResolve(res && res.isEnded === true);
        pendingResolve = pendingReject = null;
      }
      // 看完立刻预加载下一条
      ad.load();
    });

    ad.load();
    return ad;
  }

  /** 展示广告，resolve(true) 表示看完，resolve(false) 表示中途关闭 */
  function show() {
    if (!ad) return Promise.reject(new Error('AdManager 未初始化'));

    return new Promise((resolve, reject) => {
      pendingResolve = resolve;
      pendingReject = reject;

      const tryShow = () => ad.show().catch(() => ad.load().then(() => ad.show()));

      if (loaded) {
        tryShow().catch((e) => {
          pendingResolve = pendingReject = null;
          reject(e);
        });
      } else {
        ad.load()
          .then(() => tryShow())
          .catch((e) => {
            pendingResolve = pendingReject = null;
            reject(e);
          });
      }
    });
  }

  /** 是否值得显示「看广告」按钮 */
  function isReady() {
    return loaded;
  }

  function destroy() {
    if (ad) {
      ad.destroy();
      ad = null;
      loaded = false;
    }
  }

  return { init, show, isReady, destroy };
})();

module.exports = AdManager;
