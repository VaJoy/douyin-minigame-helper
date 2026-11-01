---
title: "tt.bindUnionGroup"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/union-group/tt-bind-group
update_time: 2025-04-07
---

## 语法

```js
tt.bindUnionGroup(unionId)
```
基础库 3.51.0 开始支持本方法，这是一个**异步**方法。
给指定公会绑定公开群

## 示例代码
```js
tt.bindUnionGroup({
  unionId: 'testUnionId',
  success(res) {
    console.log('tt.bindUnionGroup success', res);
  },
  fail(res) {
    console.log('tt.bindUnionGroup failed', res);
  }
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| unionId | string | 是 |  | 3.51.0 | 查询绑定群信息的公会 ID，格式限制为字母数字下划线，长度不超过 30 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："bindUnionGroup:ok" - **bindResult**（boolean）：是否绑定公开群，true 完成绑定，false 未绑定 |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："bindUnionGroup:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 135901 | unknown error |  |  |
| 135902 | server error |  |  |
| 135903 | union has been bound to a group |  |  |
| 135904 | user auth deny |  |  |
| 135905 | user auth expired |  |  |
| 135906 | user auth fail |  |  |
| 135907 | open auth fail |  |  |
| 135908 | open page fail |  |  |
| 999976 | must be invoked by user tap gesture |  |  |
| 999985 | network unavailable |  |  |
| 999986 | invoke too frequently |  |  |
| 999987 | The feature is not supported in app |  |  |
| 999988 | The feature is not available in current operating system |  |  |
| 999996 | not login |  |  |
| 999999 | invalid param |  |  |

## 使用限制
- 目前仅支持抖音，抖 lite，可以使用 [tt.getSystemInfoSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/system-information/tt-get-system-info-sync) 判断宿主
- 该 API 必须要由用户点击触发，也就是只能在 [tt.onTouchEnd](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/click-event/tt-on-touch-end) 的回调里面同步调用该 API

## 前置条件
需要提前调用 [tt.login({force: true})](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/log-in/tt-login) 保证用户已登录宿主

## 相关课程
[公会群能力指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/union-group-guide)

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/union-group)
