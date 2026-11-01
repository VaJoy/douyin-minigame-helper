---
title: "tt.getStorageInfo"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/data-caching/tt-get-storage-info
update_time: 2024-07-24
---

基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
异步获取本地缓存数据的相关信息。

## 示例代码
```js
tt.getStorageInfo({
  success(res) {
    console.log(res.keys);
    console.log(res.currentSize);
    console.log(res.limitSize);
  },
  fail(res) {
    console.log(`getStorageInfo调用失败`);
  },
});
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **keys**（Array<string>）：本地数据缓存中的所有键名列表，如本地数据则返回空数组 - **currentSize**（number）：当前占用的空间大小，以 KB 为单位 - **limitSize**（number）：存储空间上限，以 KB 为单位，一般来说会返回 10240 - **errMsg**（string）："getStorageInfo:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："getStorageInfo:fail " + 详细错误信息 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/data-caching/tt-get-storage-info) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-get-storage-info%22%7D)
