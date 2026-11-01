---
title: "tt.requestSubscribeMessage"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/subscribe-message/tt-request-subscribe-message
update_time: 2025-11-24
---

## 错误码

| errCode | errNo | errMsg | 说明 |
| --- | --- | --- | --- |
| 1001 | 暂时未加 | no permission | 没有权限(白名单配置，暂无需关注) |
| 1002 | 20000 | invalid params | 参数不合法 |
| 1003 | 20000 | template counts out of max bounds | 模板消息个数超过限制（最多 3 个） |
| 1004 | 21101 | template not exist or invalid | 模板消息不存在或不合法 |
| 1005 | 21102 | template type not the same | 模板消息类型不一致，或者订阅消息是多个并包含了版本更新提醒。在 tmplIds 数组中，多个模板 id 代表的模板类型（一次性或者永久）和消息类型（分为普通消息和版本更新消息两类）都应该分别保持一致。例如：tmplIds 中的所有模板 id 代表的模板类型统一为一次性，消息类型全部为普通消息。 |
| 2001 | 21103 | network error | 网络问题 |
| 2002 | 21104 | service error | 服务错误 |
| 3001 | 21105 | auth deny | 拒绝授权 |
| 3002 | 21106 | login deny | 拒绝登录 |
| 4001 | 21107 | request count out of limit | 请求次数超过限制 (二期弹窗频控取消，不会再出现) |
| 4002 | 21108 | main switch off | 总开关关闭 |
| 4003 | 21109 | templates switches all off | 请求模板消息开关均关闭 |
| 4004 | 21110 | forbidden | 后台封禁 |
| 暂时未加 | 暂时未加 | not supported by current application | 宿主不支持 |
| 5001 | 10401 | Internal error: \${附加信息} | 内部错误 |

## 语法

```js
tt.requestSubscribeMessage(tmplIds)
```
基础库 1.73.0 开始支持本方法，这是一个**异步**方法。
调起客户端订阅消息界面，返回用户订阅消息的操作结果。当用户勾选了订阅面板中的 “总是保持以上选择，不再询问” 时，或是点击了订阅面板中 “拒绝，不再询问” 时，模板消息会被添加到用户的小程序设置页，用户可以在设置页面进行管理。

## 示例代码
```js
// index.js
const tmplIds = ["MSGxx", "MSGxx"];
tt.requestSubscribeMessage({
  tmplIds: tmplIds,
  complete: (res) => {
    tt.showModal({
      title: "订阅完成",
      content: JSON.stringify(res),
    });
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| tmplIds | Array<string> | 是 |  | 1.73.0 | 需要订阅的消息模板的 id 的集合，最多支持传入三个 tmplId。  消息 id 获取请参考[教程](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/subscribe-message/introduce)中的【获取消息 ID】步骤 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **TEMPLATE_ID**（string）：[TEMPLATE_ID]为模板 id - **errMsg**（string）："requestSubscribeMessage:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："requestSubscribeMessage:fail" + 详细错误信息 |

## 使用限制
当前仅支持抖音宿主

## 注意事项
- 只允许在以下时机中调用：点击事件、[支付](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/tt-request-game-payment)回调函数。
- 模版分为一次性模版和长期性模版，一次性模版 ID 和长期性模版 ID 不可同时使用。
- 版本更新提醒需要单独订阅。与其他混合的情况下会产生 1005 错误。

## 相关课程
订阅功能介绍及使用方式见文档：[订阅消息功能](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/subscribe-message/introduce)。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
