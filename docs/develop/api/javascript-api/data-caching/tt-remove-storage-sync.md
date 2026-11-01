---
title: "tt.removeStorageSync"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/data-caching/tt-remove-storage-sync
update_time: 2024-07-24
---

## 语法

```js
tt.removeStorageSync(key)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
从本地缓存数据中删除 key 对应的值。

## 示例代码
```js
try {
  tt.removeStorageSync("didShownAd");
  console.log(`removeStorageSync调用成功`);
} catch (error) {
  console.log(`removeStorageSync调用失败`);
}
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| key | string | 是 |  | 1.0.0 | 键名 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21101 | remove storage fail,key == %s |  |  |
| 20001 | invalid param |  |  |
| 20000 | internal error |  |  |
| -1 | promise not call |  |  |
| 20000 | key is illegal |  |  |
| 21000 | localStorage removeObjectForKey failed, key: %@ |  |  |
| 10102 | Methord %@ not implement |  |  |

## 注意事项
删除失败时会报错，建议通过 try/catch 进行兜底。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/data-caching/tt-remove-storage-sync) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-remove-storage-sync%22%7D)
