---
title: "tt.openFeedback"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/feedback/tt-open-feedback
update_time: 2025-06-27
---

基础库 3.76.0 开始支持本方法，这是一个**异步**方法。
打开反馈页

## 示例代码
```js
tt.onTouchEnd(() => {
  tt.openFeedback({
    success() {
      console.log('打开反馈页成功');
    },
    fail(err) {
      console.log('打开反馈页失败');
    }
  })
});
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："openFeedback:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："openFeedback:fail" + 详细错误信息 |

## 使用限制
必须在用户交互后才能使用，即在 [touchEnd](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/system/click-event/tt-on-touch-end) 事件回调内调用该接口

## 注意事项
注意接口的支持版本，未支持的版本可以引导玩家手动打开反馈页进行反馈

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/foundation/tt-open-feedback) / [本地体验路径](tt-open-feedback)
