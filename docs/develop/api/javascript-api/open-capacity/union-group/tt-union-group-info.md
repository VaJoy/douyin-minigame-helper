---
title: "tt.getUnionGroupInfo"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/union-group/tt-union-group-info
update_time: 2025-04-07
---

## 语法

```js
tt.getUnionGroupInfo(unionId)
```
基础库 3.51.0 开始支持本方法，这是一个**异步**方法。
获取公会绑定群信息

## 示例代码
```js
tt.getUnionGroupInfo({
  unionId: 'testUnionId',
  success(res) {
    console.log('tt.getUnionGroupInfo success', res);
  },
  fail(res) {
    console.log('tt.getUnionGroupInfo failed', res);
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
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："getUnionGroupInfo:ok" - **bindStatus**（boolean）：目前公会的绑定状态，true 则公会已绑定，false 则公会未绑定 |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："getUnionGroupInfo:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 135801 | unknown error |  |  |
| 135802 | server error |  |  |
| 999985 | network unavailable |  |  |
| 999986 | invoke too frequently |  |  |
| 999987 | The feature is not supported in app |  |  |
| 999988 | The feature is not available in current operating system |  |  |
| 999996 | not login |  |  |
| 999999 | invalid param |  |  |

## 使用限制
目前仅支持抖音，抖音极速版，可以使用 [tt.getSystemInfoSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/system-information/tt-get-system-info-sync) 判断宿主

## 注意事项
IDE 上该接口返回模拟结果，请使用真机预览调试

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
