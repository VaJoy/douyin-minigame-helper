---
title: "tt.getStorage"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/data-caching/tt-get-storage
update_time: 2024-08-19
---

## 语法

```js
tt.getStorage(key)
```
基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
获取本地缓存数据。

## 示例代码
```js
tt.getStorage({
  key: "didShownAd",
  success(res) {
    console.log(res);
  },
  fail(res) {
    console.log("getStorage调用失败");
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
| res | Object | object 类型，属性如下：  **对象字段** - **data**（string \| object \| number \| boolean \| null \| undefined \| array）：[本地缓存数据类型](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/other/local-data-caching)  键名对应的数据，如无数据或数据类型不支持会返回空字符串 - **errMsg**（string）："getStorage:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："getStorage:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21101 | data not found, key == %s |  |  |
| 20000 | internal error |  |  |
| 20001 | invalid param |  |  |
| 20000 | key is illegal |  |  |
| 21000 | data not found, key == %@ |  |  |
| -1 | promise not call |  |  |
| 10102 | Methord %@ not implement |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/data-caching/tt-get-storage) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-get-storage%22%7D)
