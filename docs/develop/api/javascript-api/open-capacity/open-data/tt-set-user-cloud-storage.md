---
title: "tt.setUserCloudStorage"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/open-data/tt-set-user-cloud-storage
update_time: 2025-10-10
---

## 语法

```js
tt.setUserCloudStorage(KVDataList)
```
基础库 1.11.0 开始支持本方法，这是一个**异步**方法。
对用户存储的数据进行写入操作, 允许同时写多组 KV 数据。

## 示例代码
```js
tt.setUserCloudStorage({
  KVDataList: [
    {
      key: "xxx",
      value: JSON.stringify({
        ttgame: {
          score: 100,
          update_time: 1557813466,
        },
        progress: 10,
      }),
    },
  ],
  success: (res) => {
    console.log("调用成功");
    console.log(res.errMsg);
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
| KVDataList | Array<Object> | 是 |  | 1.11.0 | 要修改的 KV 数据列表。数据类型为 [KVData](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/relationship-chain/open-data/kv-data) |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | "setUserCloudStorage:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | "setUserCloudStorage:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21000 | get session id failed. |  |  |
| 20000 | KVDataList |  |  |
| 10301 | feature is not supported in app |  |  |
| 21000 | * |  |  |
| 21000 | response json has error |  |  |
| 10401 | internal error/网络请求非200 |  |  |
| 10103 | network unavailable |  |  |
| 20000 | internal error |  |  |

## 使用限制
- 上报的 value 值必须是 string，开发者可以针对 value 使用 JSON.stringify 进行处理。
- 每个 openid 所标识的用户在每个游戏上托管的数据不能超过 128 个 key-value 对。
- 上报的 key-value 列表当中每一项的 key+value 长度都不能超过 1K(1024)字节。
- 上报的 key-value 列表当中每一个 key 长度都不能超过 128 字节。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/open-capacity/open-data/tt-set-user-cloud-storage) / [本地体验路径](tt-set-user-cloud-storage)
