---
title: "KVData"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/open-data/kv-data
update_time: 2024-07-24
---

托管的 KV 数据，类型为 object。
## 属性说明

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| key | string | 数据的 key |
| value | string | 数据的 value |

## 设置排行榜
平台提供了挑战排行榜功能，部分宿主 APP 会在其特有的功能页展示游戏排行数据。开发者若想利用，则需要把排行榜数据存储到对应的 key/value 中，一个排行榜数据对应一个 key，多个排行榜则多个 key。同时在小游戏管理后台“运营-运营能力-游戏排行榜”下配置对应的 key 以及相关排行榜属性。且 value 的内容必须是 JSON Object 格式序列化的字符串，该 JSON Object 顶层必须包含 ttgame 字段，定义如下：

| 属性 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| score | Int32 | 是 | 游戏成绩，用该字段排序 |
| update_time | Int64 | 是 | 最后更新时间，Unix 时间戳 |

注意：
1. 使用 setUserCloudStorage 接口设置 KVData 时，当 key 为排行榜 key，则 value 结构必须符合以上要求，否则会设置失败
1. ttgame 下开发者不可自定义其他字段，score 为平台固定使用的排序字段，若开发者想要以某个游戏数据排序，需要将该数据存储在 score 字段上。 ttgame 同级开发者可自由定义，比如定义一个 progress 字段，用于游戏关卡进度。
## 示例
比如某小游戏有一个分数排行榜，分数排行榜需要记录分数以及关卡进度（游戏内的排行榜需要展示耗时），可以在 ttgame 同级别定义一个不和已定义的托管数据的 key 相冲突的 key 作为分数排行榜的 key，如 progress 字段，用于存储玩家的关卡进度。
在玩家游戏结束后，闯过第 10 关，获得本周最高分 100 分，则需要更新排行榜数据，假设当前时间戳为 1557813466， 则完整 value 在序列化之前的内容如下：

```js
{
  "ttgame": {
    "score": 100,
    "update_time": 1557813466
  },
  "progress": 10
}
```

最终序列化为 string 后，value 为 "{"ttgame":{"score":100,"update_time": 1557813466},"progress":10}"
