---
title: "tt.inflate"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/drawing/inflate/tt-inflate
update_time: 2024-08-15
---

## 语法

```js
tt.inflate(buffer, raw)
```
基础库 1.3.0 开始支持本方法，这是一个**同步**方法。
提供解压缩的能力，支持由 [zlib.deflateSync](https://nodejs.org/api/zlib.html#zlib_zlib_inflatesync_buffer_options) 和 [zlib.deflateRawSync](https://nodejs.org/api/zlib.html#zlib_zlib_deflaterawsync_buffer_options) 得到的压缩数据。与 node 提供的异步解压缩方法不同，这是一个同步方法。

## 示例代码
```js
const Buffer = tt.createBuffer();
const content1 = "eJxzT03NLgYABXQB8A==";
const buffer1 = Buffer.from(content1, "base64");
const result1 = tt.inflate(buffer1); // 默认为false
console.log(
  `[API: ZLIB] the result of inflate is: ${Buffer.toString(result1)}`
);
// [API: ZLIB] the result of inflate is: Geeks
const content2 = "c09NzS4GAA==";
const buffer2 = Buffer.from(content2, "base64");
const result2 = tt.inflate(buffer2, true);
console.log(
  `[API: ZLIB] the result of inflate raw is: ${Buffer.toString(result2)}`
);
// [API: ZLIB] the result of inflate raw is: Geeks
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 |  | 1.3.0 | 可以通过 [tt.createBuffer()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/drawing/inflate/tt-create-buffer) 提供的 from 方法得到 |
| raw | boolean | 否 | false | 1.98.0 | 当参数 raw 为 false 时，对应的压缩方法为 [zlib.deflateSync](https://nodejs.org/api/zlib.html#zlib_zlib_inflatesync_buffer_options)，对应的解压缩方法为 [zlib.inflateSync](https://nodejs.org/api/zlib.html#zlib_zlib_inflatesync_buffer_options)，与 zlib 提供的异步解压缩方法不同，小游戏中提供的 tt.inflate 是同步的。   当参数 raw 为 true 时，对应的压缩方法为 [zlib.deflateRawSync](https://nodejs.org/api/zlib.html#zlib_zlib_deflaterawsync_buffer_options)，对应的解压缩方法为 [zlib.inflateRawSync](https://nodejs.org/api/zlib.html#zlib_zlib_inflaterawsync_buffer_options) ，与 zlib 提供的异步解压缩方法不同，小游戏中提供的 tt.inflate 是同步的 |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| （返回值） | ArrayBuffer | Uint8Array。可以通过 [tt.createBuffer()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/drawing/inflate/tt-create-buffer) 提供的 toString 方法将结果转化为字符串 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/drawing/inflate/tt-inflate) / [本地体验路径](tt-inflate)
