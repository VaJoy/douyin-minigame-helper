---
title: "tt.removeStorage"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/data-caching/tt-remove-storage
update_time: 2024-07-24
---

## 语法

```js
tt.removeStorage(key)
```
基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
从本地缓存数据中异步删除 key 对应的值。

## 示例代码
```js
tt.removeStorage({
  key: "didShownAd",
  success(res) {
    console.log(`removeStorage调用成功`);
  },
  fail(res) {
    console.log(`removeStorage调用失败`);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| key | string | 是 |  | 1.0.0 | 键名 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："removeStorage:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："removeStorage:fail " + 错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21101 | remove storage fail,key == %s |  |  |
| 20000 | internal error |  |  |
| 20001 | invalid param |  |  |
| 20000 | key is illegal |  |  |
| 21000 | localStorage removeObjectForKey failed, key: |  |  |
| -1 | promise not call |  |  |
| 10102 | Methord %@ not implement |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/data-caching/tt-remove-storage) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-remove-storage%22%7D)
