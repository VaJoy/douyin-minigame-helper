---
title: "tt.getLaunchOptionsSync"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/system/lifecycle/tt-get-launch-options-sync
update_time: 2025-06-12
---

> 基础库 1.12.0 开始支持本方法，低版本需做[兼容处理](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/basic-library/compatibility-description/)，这是一个同步方法
返回小游戏启动参数。
## 语法

```js
var options = tt.getLaunchOptionsSync()
```

## 参数说明
无
## 返回值
#### Object

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| query | Object | 启动参数。开发者在部分场景下往query中添加自定义字段时，应避免与某些特殊字段同名，具体可见下表。 |
| scene | string | 启动场景值, 所有 scene 值可以在 [场景值](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/scene-value/) 中查看。以及 IDE 中：普通编译-> 增加编译模式->进入场景，查看所有场景值 |
| extra | Object | 小游戏基本信息，包括宿主 Id，gameId 等参数。 |

**query 特殊字段：**
以下字段均为特定场景所使用，开发者应避免在query中使用同名字段。

| 特殊字段 | 含义&使用说明 |
| --- | --- |
| ad_params | 平台的广告场景字段。 如果需要消费该字段，需要对其进行一次 decode 操作。 由于 ad_params 参数较长，不建议直接把 query 全部透传给服务端接口。 |
| feed_game_scene | 推荐流直出场景字段。 |
| feed_game_channel | 推荐流直出场景字段。 |
| feed_game_content_id | 推荐流直出场景字段。 |
| feed_game_extra | 推荐流直出场景字段。 |

**extra 部分返回如下：**

| 属性名 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| aid | number | 宿主 id | 2.31.0 |
| appId | string | 小游戏 appId。 | 2.31.0 |
| mpVersion | string | 小游戏的版本信息。 | 2.31.0 |
| launch_from | string | 启动场景的补充信息，仅当`scene=021020`时返回，可用于区分微端和桌面快捷方式场景 `miniapk`表示微端场景，`desktop`表示桌面快捷方式进入 | 2.56.0 |

## 扫码体验

![screenshot](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMQAAADECAYAAADApo5rAAAAAklEQVR4AewaftIAAAjQSURBVO3BQY4kyZEAQdVA/f/Lug0eHHZyIJBZPUOuidgfrLX+42GtdTystY6HtdbxsNY6HtZax8Na63hYax0Pa63jYa11PKy1joe11vGw1joe1lrHw1rreFhrHT98SOVvqrhRmSreULmpmFSmihuVb6qYVG4qPqFyUzGp/E0Vn3hYax0Pa63jYa11/PBlFd+k8k0qU8UbKm+oTBWTyk3FjcpUMalMKjcVNxWfqPgmlW96WGsdD2ut42Gtdfzwy1TeqHhD5Y2KSWWqmFT+TVT+JpWbik+ovFHxmx7WWsfDWut4WGsdP/yPqXijYlL5J1XcVEwqk8onVKaK/08e1lrHw1rreFhrHT/8j1G5qZhUpopJ5aZiUrlRuVH5RMWkMlXcqEwqb1T8N3tYax0Pa63jYa11/PDLKv6mijcqJpU3VG4q3lC5qbhRmSomlTcqflPFv8nDWut4WGsdD2ut44cvU/k3UZkqJpWpYlKZKiaVqWJSmSomlaliUrlRmSomlaliUpkqJpWpYlKZKm5U/s0e1lrHw1rreFhrHT98qOLfrGJS+YTKVHFTMalMFZPKN1XcVNxUfKLiv8nDWut4WGsdD2utw/7gAypTxaTyTRVvqEwVNyo3FZPKTcWNylTxhsrfVPGGyjdV/KaHtdbxsNY6HtZah/3BB1TeqPiEyk3FpHJT8U0qNxWTyicqJpWp4kZlqphUbipuVN6oeENlqvjEw1rreFhrHQ9rrcP+4AMqU8UbKlPFpHJTMal8U8WNylQxqUwVb6hMFZ9Q+UTFjcpNxY3KTcVvelhrHQ9rreNhrXXYH3xA5aZiUpkqvknlpuJG5Y2Kb1KZKj6hMlW8oXJTMalMFTcqNxV/08Na63hYax0Pa63D/uCLVG4qJpWpYlKZKiaVqWJSmSpuVKaKN1RuKt5Q+UTFpDJVTCpTxaTyRsWkMlVMKm9UfNPDWut4WGsdD2ut44cPqdxUvKEyVUwqU8WkMlVMKlPFGyo3FTcqU8Wk8omKSWWqeEPlEypTxaRyUzGp/KaHtdbxsNY6HtZah/3BL1L5popJ5abiEyo3FZ9QeaPiRmWqmFRuKiaVqeJGZar4b/Kw1joe1lrHw1rr+OFDKm9UTCo3FZPKTcUbKm9UvKEyVbxRMancVEwqU8UbFW9UTCpTxaRyU3GjMlV84mGtdTystY6HtdZhf/AXqUwVk8obFZ9QmSo+oXJT8YbKVPGGyk3FpHJTMalMFZ9Quan4TQ9rreNhrXU8rLUO+4MPqNxU3KhMFTcqU8Wk8v9ZxSdU/kkVb6hMFZ94WGsdD2ut42GtdfzwL6NyU/FNFZPKGxWTylRxozJVTCpTxaQyqUwVk8pUMVVMKlPFpHJTMalMFTcqU8VU8U0Pa63jYa11PKy1jh++rGJSmSreqHijYlL5popJ5UblExWTyk3FpDJVvFHxT6r4mx7WWsfDWut4WGsd9gdfpDJVvKHyRsWkMlVMKlPFP0llqnhD5TdV3KjcVHxCZaqYVKaKTzystY6HtdbxsNY6fviQylQxqUwVb1S8UTGpTBVvqEwVNyrfpHJTMancVNyoTCo3FTcqn6j4mx7WWsfDWut4WGsdP3yo4hMqNyrfpDJVTCqfqJhUpopJ5Y2KT6hMFTcVb6hMFZPKVDGpvFHxTQ9rreNhrXU8rLUO+4MvUvmmihuVqWJSuamYVKaKSeWm4g2VT1TcqLxRcaMyVXxC5aZiUrmp+MTDWut4WGsdD2ut44d/WMWkMql8ouJGZaqYVKaKG5Wp4o2KSWWqmFQ+UTGpTBVTxaQyVdyoTBU3KjcV3/Sw1joe1lrHw1rrsD/4gMpU8YbKTcUnVG4q3lCZKiaVb6qYVKaKSWWquFGZKiaVm4oblaliUpkqblRuKj7xsNY6HtZax8Na67A/+IDKTcUbKjcVb6hMFW+oTBW/SWWq+CaVm4pvUpkqblRuKn7Tw1rreFhrHQ9rrcP+4AMqv6niDZU3Kt5QmSq+SeWmYlKZKm5UpopPqEwVb6jcVEwqU8U3Pay1joe11vGw1jp++GUVn1C5qZgqJpWpYlKZKm4qJpU3Km4qJpU3VKaKqWJS+ZtUpooblaliUpkqPvGw1joe1lrHw1rr+OGXqdxU3FTcqEwVU8WkcqPyT1K5UZkqblSmipuKG5UblZuKSeWm4m96WGsdD2ut42GtdfzwZRU3KpPKVDGpTBWfqJhUpopJ5abib6qYVKaKqWJSmSreqJhUbiomlaniDZWp4pse1lrHw1rreFhrHT/8MpVPVEwqU8UnKiaVN1Smim+qmFSmihuVqWJSmSpuVG4qbiomlZuKqeI3Pay1joe11vGw1jp++GUVn1CZKt5QmSomlaniRmWqmFSmijcqPqEyVbyh8gmVT1RMKlPFb3pYax0Pa63jYa112B/8F1OZKm5UPlHxhsonKiaVNyreUJkqblSmijdUbipuVKaKTzystY6HtdbxsNY6fviQyt9UMVVMKjcV/6SKSeWNik+oTBVvqLyhMlV8QmWq+KaHtdbxsNY6HtZaxw9fVvFNKjcqU8WkMqncVNyo3FRMFf8klanipuKbKt6o+Cc9rLWOh7XW8bDWOn74ZSpvVHxCZaq4UZlUpoqbihuVm4pJ5RMqNypTxaQyVUwVk8qk8gmVm4rf9LDWOh7WWsfDWuv44X+cylQxVdyo3KhMFVPFpDKp3Ki8UfGGyo3KTcU3qdyo3FR84mGtdTystY6Htdbxw/+YihuVf1LFpHJTcaMyqXyi4kblRuUTFZPKVPGbHtZax8Na63hYax0//LKK31QxqUwVU8WkclNxozKp3FS8oXJTcaPyTRWTyk3FjcqkMlVMKlPFNz2stY6HtdbxsNY6fvgylb9JZar4RMUbFZPKJyomlaliUvlExaQyVUwqU8WNyk3FjcpU8Zse1lrHw1rreFhrHfYHa63/eFhrHQ9rreNhrXU8rLWOh7XW8bDWOh7WWsfDWut4WGsdD2ut42GtdTystY6HtdbxsNY6HtZax/8B5p3NdVFj8WsAAAAASUVORK5CYII=)

## 代码示例
[开发者工具中预览](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/system/lifecycle/tt-get-launch-options-sync)

```js
var options = tt.getLaunchOptionsSync();
console.log(options);
```
