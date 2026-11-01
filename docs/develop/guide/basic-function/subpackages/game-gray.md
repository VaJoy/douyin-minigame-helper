---
title: "游戏灰度"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/basic-function/subpackages/game-gray
update_time: 2025-08-25
---

## 灰度版操作流程
### 入口

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/e70ea5ab99114b05a28533d562495bbe~tplv-9nona0m7ha-image.image)

### 提审

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/514fbd73a9e045c09ea6ac788ff22efe~tplv-9nona0m7ha-image.image)

### 灰度版本

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/c2891b73c92a413fb62069cffe679bd8~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/a3fd353840414d43a5ae73a0fde4e7b8~tplv-9nona0m7ha-image.image)

### 灰度比例

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/ed37a64d852144ca81f8e81e9866e521~tplv-9nona0m7ha-image.image)

### 灰度撤销与覆盖

> 可以在前一个版本的基础上覆盖之前的灰度进程，不需要额外发布

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/95e60290c7ac405c9e35af2834c7b988~tplv-9nona0m7ha-image.image)

## 注意事项
1. 灰度比例只可递增，不可减少,灰度满 15 天后将自动全量到线上。
1. 可以发布灰度之后撤销灰度，此时撤销灰度，会直接撤掉线上灰度版本，需要重新提交测试版本
