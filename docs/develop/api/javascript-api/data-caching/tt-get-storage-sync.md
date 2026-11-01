---
title: "tt.getStorageSync"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/data-caching/tt-get-storage-sync
update_time: 2024-08-19
---

## 语法

```js
tt.getStorageSync(key)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
获取本地缓存数据。这是一个同步接口，是[tt.getStorage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/data-caching/tt-get-storage/)的同步版本。

## 示例代码
```js
try {
  console.log(tt.getStorageSync("myKey"));
} catch (error) {
  console.log(`getStorageSync调用失败`);
}
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| key | string | 是 |  | 1.0.0 | 键名 |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| StorageData | string \| object \| number \| boolean \| null \| undefined \| array | [本地缓存数据类型](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/other/local-data-caching)  键名对应的数据，如无数据或数据类型不支持会返回空字符串 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/data-caching/tt-get-storage-sync) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-get-storage-sync%22%7D)
