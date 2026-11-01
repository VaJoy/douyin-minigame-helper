/**
 * 侧边栏复访（必接能力）：检查宿主是否支持 + 引导跳转
 *
 * 用法：
 *   const Sidebar = require('./sidebar-return');
 *   const ok = await Sidebar.canUse();
 *   if (ok) Sidebar.enter();     // 用户点击「去侧边栏领奖」时调用
 *
 * 说明：
 * - 所有小游戏都必须接入，影响推荐权重；
 * - scene 目前只支持 'sidebar'；
 * - 必须在用户点击事件里调用，冷启动直接跳会被拒。
 */
const Sidebar = (() => {
  let supported = null;

  /** 是否支持侧边栏场景（带缓存，避免重复请求） */
  function canUse() {
    if (supported !== null) return Promise.resolve(supported);

    return new Promise((resolve) => {
      tt.checkScene({
        scene: 'sidebar',
        success(res) {
          supported = !!res.isExist;
          resolve(supported);
        },
        fail() {
          supported = false;
          resolve(false);
        },
      });
    });
  }

  /** 跳转到侧边栏；resolve(true) 表示跳转成功 */
  function enter() {
    return new Promise((resolve) => {
      tt.navigateToScene({
        scene: 'sidebar',
        success() { resolve(true); },
        fail(res) {
          console.warn('[sidebar] 跳转失败', res.errMsg || res);
          resolve(false);
        },
      });
    });
  }

  /**
   * 渲染入口按钮时调用：支持才展示，避免点了没反应
   * @param {Function} onClick 用户点击后的业务回执
   */
  async function bindButton(el, onClick) {
    const ok = await canUse();
    if (!ok) {
      if (el) el.style.display = 'none';
      return false;
    }
    if (el) {
      tt.onTouchEnd((e) => {
        const { clientX, clientY } = e.changedTouches[0];
        const r = el.getBoundingClientRect && el.getBoundingClientRect();
        if (r && clientX >= r.left && clientX <= r.right && clientY >= r.top && clientY <= r.bottom) {
          enter().then((done) => done && onClick && onClick());
        }
      });
    }
    return true;
  }

  return { canUse, enter, bindButton };
})();

module.exports = Sidebar;
