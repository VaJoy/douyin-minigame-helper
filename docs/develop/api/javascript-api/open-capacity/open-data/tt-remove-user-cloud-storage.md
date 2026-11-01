---
title: "tt.removeUserCloudStorage"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/open-data/tt-remove-user-cloud-storage
update_time: 2025-10-10
---

## 语法

```js
tt.removeUserCloudStorage(keyList)
```
基础库 1.11.0 开始支持本方法，这是一个**异步**方法。
删除当前宿主 APP 中有群功能的同玩该游戏的用户托管数据当中对应 key 的数据。

## 示例代码
```js
tt.removeUserCloudStorage({
  keyList: ["xxx"], // 要删除的 key 列表,
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
| keyList | Array<string> | 是 |  | 1.11.0 | 要删除掉的 key 列表 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | "removeUserCloudStorage:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | "removeUserCloudStorage:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21000 | get session id failed. |  |  |
| 20000 | keyList is null |  |  |
| 10301 | feature is not supported in app |  |  |
| 21000 | 网络请求错误 |  |  |
| 21000 | response json has error |  |  |
| 10401 | internal error/网络请求非200 |  |  |
| 10103 | network unavailable |  |  |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/open-capacity/relationship-chain/open-data/tt-remove-user-cloud-storage) / [本地体验路径](tt-remove-user-cloud-storage)
