---
title: "tt.createBuffer"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/drawing/inflate/tt-create-buffer
update_time: 2024-08-15
---

基础库 1.98.0 开始支持本方法，这是一个**同步**方法。
创建一个 buffer 对象。该对象提供 buffer 和字符串互相转化的方法，用法上和 Node.js 中的 Buffer 有区别，详见代码示例。

## 示例代码
```js
const Buffer = tt.createBuffer();
const buffer1 = Buffer.from("abc");
const string1 = Buffer.toString(buffer1);
console.log(
  `[API: buffer] default encoding is utf8, "abc" to buffer, then buffer to string is still: ${string1}`
);
// [API: buffer] default encoding is utf8, "abc" to buffer, then buffer to string is still: abc

const buffer2 = Buffer.from("abc", "utf8");
const string2 = Buffer.toString(buffer2, "base64");
console.log(`[API: buffer] "abc" to base64 is: ${string2}`);
// [API: buffer] "abc" to base64 is: YWJj

const buffer3 = Buffer.from("YWJj", "base64");
const string3 = Buffer.toString(buffer3, "utf8");
console.log(`[API: buffer] "YWJj" to utf8 string is: ${string3}`);
// [API: buffer] "YWJj" to utf8 string is: abc
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| （返回值） | Object | object 类型，详细参数描述如下：  **对象字段** - **toString**（Function）：将 buffer 转化为字符串 - **from**（Function）：将字符串转化为 buffer |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[本地体验路径](tt-create-buffer)
