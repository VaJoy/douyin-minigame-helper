---
title: "tt.setStorageSync"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/data-caching/tt-set-storage-sync
update_time: 2024-08-19
---

## 语法

```js
tt.setStorageSync(key, rawData)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
以「键值对」的形式设置本地缓存数据。这是一个同步接口，是[tt.setStorage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/data-caching/tt-set-storage)的同步版本。

## 示例代码
```js
try {
  tt.setStorageSync("didShownAd", false);
} catch (error) {
  console.log(`setStorageSync调用失败`);
}
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| key | string | 是 |  | 1.0.0 | 键名 |
| rawData | string \| number \| boolean \| object \| null \| undefined | 否 |  | 1.0.0 | [本地缓存数据类型](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/other/local-data-caching)，键值 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21101 | exceed storage item max length |  |  |
| 21102 | exceed storage max size %sMb |  |  |
| 21103 | set storage fail |  |  |
| 20000 | internal error |  |  |
| 20001 | invalid param |  |  |
| -1 | promise not call |  |  |
| 20000 | key is illegal |  |  |
| 10102 | Methord %@ not implement |  |  |
| 20000 | dataType is illegal |  |  |
| 21000 | exceed storage item max length |  |  |
| 21000 | exceed storage max size 10Mb |  |  |
| 21000 | localStorage setObject failed, data: %@; key: %@ |  |  |

## 注意事项
- 将数据存储在本地缓存中指定的 key 中。如果之前存在同名 key，会覆盖掉原来该 key 对应的内容。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/data-caching/tt-set-storage-sync) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-set-storage-sync%22%7D)
