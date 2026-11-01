---
title: "tt.getImRankList"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/game-rank/getImRankList
update_time: 2025-09-29
---

## 语法

```js
tt.getImRankList(zoneId, suffix, rankTitle, dataType, relationType, rankType)
```
基础库 2.70.0 开始支持本方法，这是一个**异步**方法。
获取排行榜列表，调用 API 后， 根据参数自动绘制游戏好友排行榜（ native UI ）。

## 示例代码
```js
//moba游戏自动生成段位榜
tt.getImRankList({
  relationType: "all", // 总榜 
  dataType: 1, //只圈选type为枚举类型的数据进行排序
  rankType: "day", //每天凌晨0点更新，只对当天0点到现在写入的数据进行排序
  suffix: "", //为空或不填，一般枚举类型不需要填后缀
  rankTitle: "rankTitle", //标题
  zoneId: 'default',
  success(res) {
    console.log(`getImRankData success res: ${res}`);
  },
  fail(res) {
    console.log(`getImRankData fail res: ${res.errMsg}`);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| zoneId | string | 否 | default | 3.5.0 | 排行榜分区标识，取值可以是 'default' 或 'test' 或其他开发者自定义字符串，'default' 表示为默认的线上分区，不同分区的排行榜数据存在数据隔离，如 zoneId='test' 设置的数据不会影响通过 zoneId='default' 的排行榜，可用于测试环境。目前每个小游戏除了 default 和 test， 最多可支持 10 个分区 |
| suffix | string | 否 |  | 2.70.0 | 分数后缀补充文案 |
| rankTitle | string | 否 |  | 2.70.0 | 排行榜标题 |
| dataType | number | 是 |  | 2.70.0 | 可选值有 0 或 1。 0 表示数据被解析为数值。1 表示数据被解析为字符串 |
| relationType | number | 否 | friend | 2.70.0 | 排行榜类型  **可选值：** default=

同时获取好友榜和总榜

；all=

总榜

；friend=

当前登录用户的好友的游戏数据排行

 |
| rankType | string | 是 |  | 2.70.0 | 可选值有：day、week、month、all |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："getImRankList:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："getImRankList:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | 暂不支持该能力 |  |  |
| 20001 | invalid param |  |  |
| 21105 | rank list is showing |  |  |
| 21101 | user not login |  |  |
| 21102 | /s |  |  |
| 21103 | internal error |  |  |
| 20000 | internal error |  |  |
| 10601 | not login |  |  |
| 10301 | feature is not supported in app xxx |  |  |
| 21104 | zone num exceeds limit |  |  |

## 注意事项
**排序规则：**

数字类型则按照传入的 value 从大到小排序，若数字大小相同，按照写入时间从早到晚排序

枚举类型按照权重从高到低排序，若权重相同，按照写入时间从早到晚排序

![](https://p3-developer-sign.bytemaimg.com/obj/developer-inner/open_admin/1719233166339/blob?x-expires=4872833166&x-signature=R9Btdxl7abN7rrFZkOrtDP1kQWs%3D)

**参数字段对应解释：**

![](https://p9-developer-sign.bytemaimg.com/obj/developer-inner/open_admin/1719233525757/blob?x-expires=4872833525&x-signature=VtJfEchilbEoiT7hvPixr%2BKKDmo%3D)

## 前置条件
在拉起排行榜前，需要调用 [tt.login](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/api/open-interface/log-in/tt-login/) 接口进行用户登录，否则可能会出现榜单无法拉起或闪退的问题

## 版本说明
抖音&抖 lite 23.2.0 版本后支持

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/tt-get-im-rank-list) / [本地体验路径](tt-get-im-rank-list)