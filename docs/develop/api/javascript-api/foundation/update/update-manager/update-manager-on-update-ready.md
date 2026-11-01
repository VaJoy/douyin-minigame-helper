---
title: "UpdateManager.onUpdateReady"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/update/update-manager/update-manager-on-update-ready
update_time: 2024-09-25
---

## 语法

```js
UpdateManager.onUpdateReady(callback)
```
基础库 1.9.0 开始支持本方法，这是一个**同步**方法。
当新版本下载完成，会进行回调。

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
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.9.0 | 当新版本下载完成后进行回调的函数 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
