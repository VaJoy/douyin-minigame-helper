---
title: "tt.setStorage"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/data-caching/tt-set-storage
update_time: 2024-08-19
---

## 语法

```js
tt.setStorage(key, data)
```
基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
以「键值对」的形式设置本地缓存数据。

## 示例代码
```js
tt.setStorage({
  key: "didShownAd",
  data: true,
  success(res) {
    console.log(`set seen ad flag`);
  },
  fail(res) {
    console.log(`setStorage调用失败`);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| key | string | 是 |  | 1.0.0 | 键名 |
| data | string \| object \| number \| boolean \| null \| undefined \| array | 否 |  | 1.0.0 | [本地缓存数据类型](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/other/local-data-caching)，键名对应的数据 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："setStorage:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："setStorage:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21101 | exceed storage item max length |  |  |
| 21102 | exceed storage max size %sMb |  |  |
| 21103 | set storage fail |  |  |
| 20001 | invalid param |  |  |
| 20000 | internal error |  |  |
| 20000 | key is illegal |  |  |
| 20000 | dataType is illegal |  |  |
| 21000 | exceed storage item max length |  |  |
| 21000 | exceed storage max size 10Mb |  |  |
| 21000 | localStorage setObject failed, data: %@; key: %@ |  |  |
| -1 | promise not call |  |  |
| 10102 | Methord %@ not implement |  |  |

## 注意事项
- 将数据存储在本地缓存中指定的 key 中，会覆盖掉原来该 key 对应的内容。
- 用户在平台 app（头条或抖音）内退出登录，或者在系统中清除 app 的缓存可清除数据。
- 单个 key 数据最大 1M，总体容量最大 10M，超出后会回调失败。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/data-caching/tt-set-storage) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-set-storage%22%7D)
