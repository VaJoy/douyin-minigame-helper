---
title: "tt.getOpenDataContext"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/open-data-area/tt-get-open-data-context
update_time: 2025-10-10
---

基础库 1.11.0 开始支持本方法，这是一个**同步**方法。
获取开放数据域。

## 示例代码
```js
const openCtx = tt.getOpenDataContext();
openCtx.postMessage({
  company: "bytedance",
});
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| （返回值） | Object | object 类型，属性如下：  **对象字段** - **canvas**（Object）：开放数据域和主域共享的 canvas，与 [tt.createCanvas](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/drawing/picture/tt-create-canvas) 获取的 canvas 类型一致 - **postMessage**（Function）：主域向开放数据域发送消息。该方法只能在主域中使用 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 注意事项
在开放数据域中，只能加载和 [tt.getUserInfo](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/user-information/info/tt-get-user-info) 返回的 avatarUrl 相同域名的图像。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/open-capacity/relationship-chain/open-data-area/tt-get-open-data-context) / [本地体验路径](tt-get-open-data-context)
