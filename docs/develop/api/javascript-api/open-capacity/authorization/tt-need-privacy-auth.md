---
title: "tt.onNeedPrivacyAuthorization"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/authorization/tt-need-privacy-auth
update_time: 2026-07-07
---

## 语法

```js
tt.onNeedPrivacyAuthorization(callback)
```
基础库 4.17.0 开始支持本方法，这是一个**同步**方法。
注册隐私授权需要用户确认时的回调。开发者可通过自定义 UI 呈现隐私授权弹窗，并在用户操作后通过回调提供的 resolve 函数反馈结果。

## 示例代码
```js
tt.onNeedPrivacyAuthorization((resolve, eventInfo) => {
  console.log('触发隐私授权的接口：', eventInfo.referrer);
  // 开发者展示自定义隐私弹窗 UI
  this.showPrivacyPopup({
    onAgree: () => {
      resolve({ event: 'agree' });
    },
    onDisagree: () => {
      resolve({ event: 'disagree' });
    }
  });
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 4.17.0 | 监听隐私授权需求的回调函数。回调入参为 (resolve, eventInfo)。  **对象字段** - **resolve**（Function）：隐私授权结果反馈接口。调用 resolve({ event: 'agree' }) 表示同意，resolve({ event: 'disagree' }) 表示拒绝。 - **eventInfo**（Object）：包含触发本次回调的关联信息。 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
