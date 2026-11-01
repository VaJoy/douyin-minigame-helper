---
title: "UpdateManager.onUpdateFailed"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/update/update-manager/update-manager-on-update-failed
update_time: 2024-09-25
---

## 语法

```js
UpdateManager.onUpdateFailed(callback)
```
基础库 1.9.0 开始支持本方法，这是一个**同步**方法。
当新版本下载失败，会进行回调。

## 示例代码
```js
const updateManager = tt.getUpdateManager();
updateManager.onUpdateFailed(function (err) {
  // 请求完新版本信息的回调
  console.log("版本更新失败原因", err);
  tt.showToast({
    title: "版本更新失败，请重试",
    icon: "none",
  });
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.9.0 | 当新版本下载失败时回调的函数  **对象字段** - **err**（string）：版本更新失败原因 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
