---
title: "tt.env"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/update/tt-env
update_time: 2026-07-16
---

> 从基础库 1.0.0 开始支持
环境变量。
## 属性说明
| 属性名 | 类型 | 默认值 | 说明 | 最低支持版本 |
| -------------- | ------ | ------------- | ------------------ | ------------ |
| USER_DATA_PATH | string | ttfile://user | 用户数据存储的路径 | 1.0.0 |
## 代码示例
```js
console.log(tt.env.USER_DATA_PATH); // ttfile://user
```
## Bug & Tip
- Tip：访问本地目录或者本地文件时，需要以 `tt.env.USER_DATA_PATH` 开头，否则容易出现访问受限的情况。
