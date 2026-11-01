---
title: "tt.addPhoneCalendar"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/device/calendar/tt-add-phone-calendar
update_time: 2024-08-29
---

## 语法

```js
tt.addPhoneCalendar(location, endTime, alarm, alarmOffset, allDay, title, startTime)
```
基础库 2.52.0 开始支持本方法，这是一个**异步**方法。
向系统日历添加事件。

## 示例代码
```js
tt.addPhoneCalendar({
  title: "测试非重复事件",
  startTime: Date.now() / 1000,
  endTime: Date.now() / 1000 + 3600,
  alarm: false,
  location: "测试location",
  description: "测试description",
  success() {
    console.log("添加桌面成功");
  },
  fail(res) {
    console.log("添加桌面失败", err.errMsg);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| location | string | 否 |  | 2.52.0 | 事件位置 |
| endTime | number | 否 |  | 2.52.0 | 结束时间的 unix 时间戳。默认值为 startTime 的值 |
| alarm | boolean | 否 | true | 2.52.0 | 是否提醒 |
| alarmOffset | number | 否 | 0 | 2.52.0 | 提醒提前量（单位：秒） |
| allDay | boolean | 否 | false | 2.52.0 | 是否全天事件 |
| title | string | 是 |  | 2.52.0 | 日历事件标题 |
| startTime | number | 是 |  | 2.52.0 | 开始时间的 unix 时间戳（1970年1月1日开始所经过的秒数，单位：秒） |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："addPhoneCalendar:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："addPhoneCalendar:fail" + 详细错误信息 |

## 使用限制
该 API 必须要由用户点击触发，也就是只能在 tt.onTouchEnd 的回调里面同步调用该 API。

## 用户授权说明
本 API 需要用户授权方可调用，详细信息可参考[用户授权](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/user-information/authorization/authorization)

## 授权要求
无需开发者授权；需要用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/device/calendar/tt-add-phone-calendar) / [本地体验路径](tt-add-phone-calendar)
