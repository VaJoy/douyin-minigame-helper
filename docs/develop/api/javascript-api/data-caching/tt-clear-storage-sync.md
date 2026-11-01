---
title: "tt.clearStorageSync"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/data-caching/tt-clear-storage-sync
update_time: 2024-07-24
---

基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
清理 **全部** 本地数据缓存的同步接口。

## 示例代码
```js
try {
  tt.clearStorageSync();
  console.log(`clearStorageSync调用成功`);
} catch (error) {
  console.log(`clearStorageSync调用失败`);
}
```

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21101 | clear storage fail |  |  |
| 20000 | internal error |  |  |
| -1 | promise not call |  |  |
| 21000 | localStorage removeAllObjects failed |  |  |
| 20000 | key is illegal |  |  |

## 注意事项
该方法无参数，也没有返回值，所以无法判断接口是否调用失败。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/data-caching/tt-clear-storage-sync) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-clear-storage-sync%22%7D)
