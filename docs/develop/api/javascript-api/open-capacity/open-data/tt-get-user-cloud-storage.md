---
title: "tt.getUserCloudStorage"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/open-data/tt-get-user-cloud-storage
update_time: 2025-10-10
---

## 语法

```js
tt.getUserCloudStorage(keyList)
```
基础库 1.11.0 开始支持本方法，这是一个**异步**方法。
获取当前用户托管数据当中对应 key 的数据。

## 示例代码
```js
tt.getUserCloudStorage({
  keyList: ["xxx"], // 要获取的 key 列表
  success: (res) => {
    console.log("调用成功");
    console.log(res.KVDataList);
  },
  fail: (res) => {
    console.log("调用失败");
  },
  complete: (res) => {
    console.log("调用完成");
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| keyList | Array<string> | 是 |  | 1.11.0 | 要获取的 key 列表 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| KVDataList​ | Array<Object> | 用户托管的 KV 数据列表​。数据类型为 [KVData](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/relationship-chain/open-data/kv-data) 类型 |
| errMsg | string | "getUserCloudStorage:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | "setUserCloudStorage:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21000 | get session id failed. |  |  |
| 10301 | feature is not supported in app |  |  |
| 20000 | keyList is null |  |  |
| 21000 | * |  |  |
| 21000 | response json doesn't have `data` field |  |  |
| 10401 | internal error/网络请求非200 |  |  |
| 10103 | network unavailable |  |  |
| 20000 | internal error |  |  |

## 使用限制
该接口只可在开放数据域下使用

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/open-capacity/relationship-chain/open-data/tt-get-user-cloud-storage) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-get-user-cloud-storage%22%7D)
