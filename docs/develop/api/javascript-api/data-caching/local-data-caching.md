---
title: "本地数据缓存"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/data-caching/local-data-caching
update_time: 2024-07-29
---

小游戏可以通过下面列出的 API 读取、写入、删除、清理本地缓存数据。与[`LocalStorage`](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/localStorage)类似。
本地缓存数据以**用户+小游戏**维度隔离，同一台设备上，不同用户之间、不同小游戏之间，本地缓存数据不可互访。
> ⚠️ 注意
> 本地缓存数据的上限约为**10MB**，同时也受到用户设备存储空间、缓存清理等机制的限制，可能会导致信息丢失。因此请不要将重要数据存放在本地数据缓存
## API Checklist
- `getStorage`
- `getStorageSync`
- `setStorage`
- `setStorageSync`
## 本地缓存数据类型
小游戏默认支持以下数据类型，存储和获取时无需类型转换。其它数据类型可根据需要在处理时转换为字符串存储，**强行操作会导致数据丢失**。
- `String`
- `Object`
- `Array`
- `Number`
- `Date`
- `Boolean`
- `Undefined`
- `Null`
