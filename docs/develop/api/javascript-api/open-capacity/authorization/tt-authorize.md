---
title: "tt.authorize"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/authorization/tt-authorize
update_time: 2025-09-29
---

## 语法

```js
tt.authorize(scope)
```
基础库 1.80.0 开始支持本方法，这是一个**异步**方法。
向用户请求单项能力授权（如地理位置、摄像头等）。

## 示例代码
```js
tt.authorize({
  scope: 'scope.camera',
  success: () => {
    console.log('授权成功');
  },
  fail: (err) => {
    console.error('授权失败', err);
  }
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| scope | string | 是 |  | 1.80.0 | 需要授权的能力 scope（如 scope.camera、scope.record 等） |

## 回调：成功回调
授权成功回调
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）：固定为 "authorize:ok" - **data**（Object）：用户授权结果，属性如下 |

## 回调：失败回调
授权失败回调（包括隐私拒绝、scope 拒绝、频控等）
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）：详细失败原因 - **errNo**（number）：错误码 |

## 回调：完成回调
接口调用结束回调
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）：接口调用结束时的状态信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21105 | /s |  |  |
| 21102 | auth deny |  |  |
| 10401 | internal auth error |  |  |
| 21101 | invalid scope |  |  |
| 21103 | batched auth permission deny |  |  |
| 21104 | %s not support batched auth |  |  |
| 20001 | invalid param |  |  |
| 20000 | internal error |  |  |
| 20000 | Scope is NULL. |  |  |
| 10401 | Internal error: platform auth deny |  |  |
| 21106 | not login |  |  |

## 注意事项
新版本中在 scope 授权前会前置校验隐私协议授权。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
