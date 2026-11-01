---
title: "tt.setImRankDataInOpenContext"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/game-rank/set-im-rank-data-in-open-context
update_time: 2024-09-13
---

## 语法

```js
tt.setImRankDataInOpenContext(extra, priority, zoneId, value, dataType)
```
基础库 2.74.0 开始支持本方法，这是一个**异步**方法。
在关键的游戏场景，设置写入用户的排行榜数据（游戏成绩信息）,该数据会上传到服务端，该方法设置的数据与[tt.setImRankData](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/game-rank/setImRankData)同源，区别在于该方法需要在开放数据域中使用，请访问 [开放数据域能力介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/relationship-chain/open-data-base/) 进行通信

## 示例代码

【代码示例1】一个跑酷游戏，想要对用户的跑酷分数做排序

```js
tt.setImRankDataInOpenContext({
  dataType: 0, //成绩为数字类型
  value: "999999", //该用户得了999999分
  priority: 0, //dataType为数字类型，不需要权重，直接传0
  extra: "extra",
  success(res) {
    console.log(`setImRankDataInOpenContext success res: ${res}`);
  },
  fail(res) {
    console.log(`setImRankDataInOpenContext fail res: ${res.errMsg}`);
  },
});
```

【代码示例2】一个 moba 游戏，想要对用户的段位进行排序

```js
tt.setImRankDataInOpenContext({
  dataType: 1, //成绩为枚举类型，因为段位不是一个数字
  value: "秩序白银", //该用户段位为白银
  priority: 2, //dataType为枚举类型，需要权重，该游戏排序为 青铜（1）、白银（2）、黄金（3）、王者（4），因此此处传2
  extra: "extra",
  success(res) {
    console.log(`setImRankDataInOpenContext success res: ${res}`);
  },
  fail(res) {
    console.log(`setImRankDataInOpenContext fail res: ${res.errMsg}`);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| extra | string | 否 |  | 2.74.0 | 补充字段。字节数要求不超过 128 |
| priority | number | 否 | 0 | 2.74.0 | 判断权重，仅当 dataType 为 1 时有效。  当 dataType为1时，需要给每个 value 传对应的权重，如传入 value 为白银，priority为 2，则白银的权重为 2，传入value为黄金，priority为 3，则黄金的权重为3，高于白银，届时生成的榜单，黄金会排在白银前面 |
| zoneId | string | 否 | default | 2.74.0 | 排行榜分区标识，取值可以是 'default' 或 'test' 或其他开发者自定义字符串。'default'表示为默认的线上分区，不同分区的排行榜数据存在数据隔离，如 zoneId='test' 设置的数据不会影响通过  zoneId='default' 的排行榜，可用于测试环境。目前每个小游戏除了 default 和 test， 最多可支持 10 个分区（未包括默认的线上分区） |
| value | string | 是 |  | 2.74.0 | 展示出来的数值，dataType == 0 时只能传正数的字符串，否则会报错  value为具体的值，若dataType为0，请传入数字（eg：103、105）；  若dataType为1，则传入字符串（eg：青铜、白银） |
| dataType | number | 是 |  | 2.74.0 | 0：数字类型 、 1：枚举类型  dataType：数字类型（0）往往适用于游戏的通关分数（103分、105分），枚举类型（1）适用于段位信息（青铜、白银）； |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："setImRankData:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："setImRankData:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21101 | user not login |  |  |
| 21102 | /s |  |  |
| 21103 | internal error |  |  |
| 21104 | zone num exceeds limit |  |  |
| 20000 | internal error |  |  |
| 10301 | feature is not supported in app xxx |  |  |
| 10601 | not login |  |  |

## 使用限制
抖音&抖 lite 23.4.0 版本后支持

## 注意事项
**字段解释**

![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1667309692612)

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/tt-set-im-rank-data-in-open-context) / [本地体验路径](tt-set-im-rank-data-in-open-context)