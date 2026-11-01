---
title: "RankResItem"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/game-rank/rank-res-item
update_time: 2024-07-24
---

RankResItem 属性如下：
> 数字类型则按照传入的 value 从大到小排序，若数字大小相同，按照写入时间从早到晚排序
> 字符串类型按照权重从高到低排序，若权重相同，按照写入事件从早到晚排序

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| data_type | number | 可选值：0 或 1。0 代表 value 为数字类型 ，1 代表 value 为枚举名称 |
| value | string | 分数值或枚举名称，代表分数值时只能传正数 |
| priority | number | `data_type === 1`时有意义，返回值为正整数，表示枚举名称对应的权重 |
| extra | string | 传入的附加字段，小游戏只负责透传 |
| openid | string | 用户的 openid |
| sec_uid | string | 加密后的 uid |
| user_img | string | 用户头像 |
| nick_name | string | 用户昵称 |
| utime | number | unix秒级时间戳 |
