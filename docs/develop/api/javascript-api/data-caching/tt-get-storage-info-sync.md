---
title: "tt.getStorageInfoSync"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/data-caching/tt-get-storage-info-sync
update_time: 2024-08-19
---

基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
同步获取当前本地缓存数据的相关信息。

## 示例代码
```js
try {
  var res = tt.getStorageInfoSync();
  console.log(res.keys);
  console.log(res.currentSize);
  console.log(res.limitSize);
} catch (error) {
  console.log(`getStorageInfoSync调用失败`);
}
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object类型  **对象字段** - **currentSize**（number）：占用空间大小，以 KB 为单位 - **limitSize**（number）：存储空间上限，以 KB 为单位，一般来说会返回 10240 - **keys**（Array<string>）：string数组，本地数据缓存中的所有键名列表，如无本地数据则返回空数组 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/data-caching/tt-get-storage-info-sync) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-get-storage-info-sync%22%7D)
