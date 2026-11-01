---
title: "tt.reportAnalytics"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/data-analysis/tt-report-analytics
update_time: 2024-07-24
---

## 语法

```js
tt.reportAnalytics(event, data)
```
基础库 1.8.0 开始支持本方法，这是一个**同步**方法。
自定义分析数据上报接口，调用后，会将数据上报到[抖音开放平台](https://developer.open-douyin.com/)，开发者可以进入[抖音开放平台](https://developer.open-douyin.com/)「数据」-「自定义分析」-「事件分析/漏斗分析」模块查看上报数据。

## 示例代码
```js
tt.reportAnalytics("clickBanner", {
  time: 1547533711355,
  uid: 123456,
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| event | string | 是 |  | 1.8.0 | 事件名，注意不能超过 110 字符 |
| data | Object | 是 |  | 1.8.0 | 上报的数据  data 中传入自定义属性，属性名为配置的字段名，属性值为上报的数据  \|  \|  \|  \|  \|  \| \| --- \| --- \| --- \| --- \| --- \| \| 属性 \| 类型 \| 必填 \| 说明 \| 最低支持版本 \| \| key \| string \| 是 \| 配置中的字段名 \| 1.8.0 \| \| value \| number \| string \| boolean \| 是 \| 上报的数据 \| 1.8.0 \| |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | param $paramName is exceed maximum length limit $maximumLength |  |  |
| 20000 | internal error |  |  |
| 20001 | eventName exceeded the maximum length: 110. |  |  |
| 20001 | invalid param |  |  |
| 20001 | data exceeded the maximum number of fields: 256. |  |  |
| 20001 | ${key} exceeded the maximum number of bytes: 128. |  |  |
| 21000 | invalid type param |  |  |
| 20001 | the value of data[${key}] exceeded the maximum number of bytes: 1024. |  |  |
| 20001 | the key first char can not be _. |  |  |
| 20001 | the key can not be mp_name or mp_id. |  |  |

## 注意事项
使用埋点验证 能力对已有埋点进行上报时，需要使用上传到开发者平台的测试版本、审核版本、线上版本。目前 IDE 预览版本不支持埋点验证。

## 前置条件
使用前，需要前往抖音开放平台「数据 - 自定义分析 - 事件管理」中新建事件，配置好事件名与字段。

## 相关课程
[事件管理](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/about-data/advanced-analysis/events)

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/open-capacity/data-analysis/tt-report-analytics) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-report-analytics%22%7D)
