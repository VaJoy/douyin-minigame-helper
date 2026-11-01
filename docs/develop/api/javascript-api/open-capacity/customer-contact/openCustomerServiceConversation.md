---
title: "tt.openCustomerServiceConversation"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/customer-contact/openCustomerServiceConversation
update_time: 2025-10-10
---

## 语法

```js
tt.openCustomerServiceConversation(type, sessionFrom)
```
基础库 2.66.1 开始支持本方法，这是一个**异步**方法。
平台提供的小游戏客服能力，按钮界面由开发者绘制后，点击调用该 api 可拉起客服界面

## 示例代码
```js
tt.openCustomerServiceConversation({
  type: 3, // 抖音客服平台
  success(res) {
    console.log(res);
  },
  fail(res) {
    console.log(res);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| type | number | 否 | 1 | 2.66.1 | 1 ：小 6 客服  2 :  抖音IM 客服（仅支持抖音）  3：抖音客服平台（基础库 3.41.0 开始支持） |
| sessionFrom | string | 否 |  | 2.66.1 | 保留字段，暂时可以不填 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："openCustomerServiceConversation:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："openCustomerServiceConversation:fail" + 详细错误信息 |

## 注意事项
- 用户必须在登录状态下才能调起IM客服，否则会出现返回成功，但是前端无响应的问题
- **该 API 必须要由用户点击触发，只能在 tt.onTouchEnd 的回调里面同步调用该 API**
- 若当前登录的用户与被绑定的抖音号相同，无法拉起 im 客服

## 前置条件
**使用抖音IM客服需要先绑定抖音号，详情请查看：****[抖音客服能力介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/user-service/douyinIM)**

## 相关课程
[抖音客服平台-客服能力](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/user-service/bytehi-im)

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
