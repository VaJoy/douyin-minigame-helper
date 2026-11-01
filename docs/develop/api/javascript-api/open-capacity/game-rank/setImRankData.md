---
title: "tt.setImRankData"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/game-rank/setImRankData
update_time: 2024-07-24
---

## 语法

```js
tt.setImRankData(extra, priority, zoneId, value, dataType)
```
基础库 2.70.0 开始支持本方法，这是一个**异步**方法。
在关键的游戏场景，设置写入用户的排行榜数据（游戏成绩信息），该数据会上传到服务端。

## 示例代码

【代码示例1】一个跑酷游戏，想要对用户的跑酷分数做排序

```js
tt.setImRankData({
  dataType: 0, //成绩为数字类型
  value: "999999", //该用户得了999999分
  priority: 0, //dataType为数字类型，不需要权重，直接传0
  extra: "extra",
  zoneId: 'test',
  success(res) {
    console.log(`setImRankData success res: ${res}`);
  },
  fail(res) {
    console.log(`setImRankData fail res: ${res.errMsg}`);
  },
});
```

【代码示例2】一个moba游戏，想要对用户的段位进行排序

```js
tt.setImRankData({
  dataType: 1, //成绩为枚举类型，因为段位不是一个数字
  value: "秩序白银", //该用户段位为白银
  priority: 2, //dataType为 1，需要权重，该游戏排序为 青铜（1）、白银（2）、黄金（3）、王者（4），因此此处传2
  extra: "extra",
  zoneId: "default",
  success(res) {
    console.log(`setImRankData success res: ${res}`);
  },
  fail(res) {
    console.log(`setImRankData fail res: ${res.errMsg}`);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| extra | string | 否 |  | 2.70.0 | 补充字段。字节数要求不超过 128 |
| priority | number | 否 | 0 | 2.70.0 | 用于判断权重 ，仅当  dataType 为 1 时需要，不传则使用默认值 0。如传入 value 为'白银'，priority 为 2，则白银的权重为 2，传入value 为 '黄金'，priority 为 3，则黄金的权重为3，高于白银，届时生成的榜单，黄金段位会排在白银前面 |
| zoneId | string | 否 | default | 3.5.0 | 排行榜分区标识，取值可以是 'default' 或 'test' 或其他开发者自定义的分区标识，'default' 表示为默认的线上分区，'test' 表示测试分区。不同分区的排行榜数据存在数据隔离，如 zoneId='test' 设置的数据不会影响通过  zoneId='default' 的排行榜，可用于测试环境。目前每个小游戏除了 default 和 test， 最多可支持 10 个分区 |
| value | string | 是 |  | 2.70.0 | 展示出来的数值，dataType 为 0 时只能传正数的**字符串**（如'103', '105'）,且取值范围为 **[0, int32_MAX)**，否则会报错。  dataType 为 1 时，则可传入任意字符串（eg：'青铜'、'白银'） |
| dataType | number | 是 |  | 2.70.0 | 可选值: 0 或 1  0 表示数据为数字类型，往往适用于游戏的通关分数（如 103分、105分）； 1 表示数据为字符串类型，适用于段位信息（如 '青铜'、'白银'） |

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
| 20001 | invalid param |  |  |
| 20000 | 暂不支持该能力 |  |  |
| 21104 | zone num exceeds limit |  |  |
| 21101 | user not login |  |  |
| 21102 | /s |  |  |
| 21103 | internal error |  |  |
| 20000 | internal error |  |  |
| 10301 | feature is not supported in app setRankData |  |  |
| 10601 | not login |  |  |

## 注意事项
**字段解释**

![](https://p9-developer-sign.bytemaimg.com/obj/developer-inner/open_admin/1719233633131/blob?x-expires=4872833633&x-signature=5z5ZLzZbKcnQM63AtSep0tLAoRw%3D)

## 版本说明
抖音&抖 lite 23.2.0 版本后支持。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/tt-set-im-rank-data) / [本地体验路径](tt-set-im-rank-data)