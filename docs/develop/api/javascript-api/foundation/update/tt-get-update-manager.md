---
title: "tt.getUpdateManager"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/update/tt-get-update-manager
update_time: 2024-07-24
---

基础库 1.9.0 开始支持本方法，这是一个**同步**方法。
获取全局唯一的版本更新管理器，用于管理小游戏更新。小游戏发布新版本后不是立即生效，在个别情况会比较慢。如果想做到立即更新，可以接入该主动更新的能力。

## 示例代码
```js
const updateManager = tt.getUpdateManager();
updateManager.onUpdateReady((res) => {
  tt.showModal({
    title: "更新提示",
    content: "新版本已经准备好，是否重启小游戏？",
    success: (res) => {
      if (res.confirm) {
        // 新的版本已经下载好，调用 applyUpdate 应用新版本并重启
        updateManager.applyUpdate();
      }
    },
  });
});

updateManager.onUpdateFailed((err) => {
  // 新的版本下载失败
  console.log("版本下载失败原因", err);
  tt.showToast({
    title: "新版本下载失败，请稍后再试",
    icon: "none",
  });
});
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| UpdateManager | Object | 全局唯一的[UpdateManager](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/update/update-manager/update-manager)对象。 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 注意事项
在有新版本的情况下，小游戏运行中任意时候单独使用 applyUpdate 即可立即重启游戏。但建议在 onUpdateReady 中给用户提示确认后进行重启。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/foundation/update/tt-get-update-manager/) / [本地体验路径](tt-get-update-manager)
