---
title: "群标签能力接入方案"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/user-ops/-retention/group-label-access
update_time: 2025-08-11
---

## 一、能力介绍

群标签能力是抖音小游戏继粉丝群、官方群后提供的第三大群聊能力。接入此能力后，可以满足群粉丝在群内聊天时，在群昵称后自动携带由厂商配置的称号标签，且点击标签即可查询获得方式以及启动游戏。

接入收益：

1.丰富群聊话题，增加粉丝聊天积极性，提高群的整体活跃度

2.增加群内复访游戏入口，提高用户留存

## 二、业务路径

![](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/15c144995d204eec81eeae484a564d3e~tplv-9nona0m7ha-image.image)

## 三、能力示意

### 1.群主选择标签

官方群管理员&游戏公会粉丝群群主默认可见对应游戏的标签选项，其他游戏铭牌需厂商申请挂载

![](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/b9245cdcdcb24bf481ce3d22c6206172~tplv-9nona0m7ha-image.image)

群聊设置页

![](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/afc629873f6047478ad7bda32b2da3bd~tplv-9nona0m7ha-image.image)

标签选择页

![](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/d477822859154b3f92c5c026ef40aea2~tplv-9nona0m7ha-image.image)

选择小游戏标签

### 2.群聊展示标签（粉丝自动携带）

![](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/877cc25790f34192865e843758115c1d~tplv-9nona0m7ha-image.image)

群聊发现铭牌

![](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/c47920704f3f4082aab94e803a933bc1~tplv-9nona0m7ha-image.image)

点击铭牌查看铭牌卡&游戏入口

![](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/f7e245bc25c542d6b2aed07c49ce0f27~tplv-9nona0m7ha-image.image)

铭牌规则详情页&游戏入口

## 四、标签配置流程

### 1.找到能力入口

> 登录开放平台，找到「运营能力」-「用户留存」-「游戏群标签能力」

![](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/3e11341dffec4a9d8b134af7543ee509~tplv-9nona0m7ha-image.image)

### 2.完成基础配置

> 基础配置指的是配置铭牌卡的背景图，此图应用于该游戏的所有标签卡片。
>
> 若调整背景图，将同步更新所有标签卡片；
>
> 最多可上传1张图，图片尺寸400\*180，大小不超1M，支持 jpg、jpeg、png 格式
>
> 图片上传后会进入审核链路，审核结果将通过开放平台站内信同步

![](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/821f654a28c544b1821192ab2a9b5ef0~tplv-9nona0m7ha-image.image)

基础配置入口

![](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/cab7a2684f75433f8b6b2d363076deae~tplv-9nona0m7ha-image.image)

上传背景图

### 3.新增标签配置

> 新增标签配置指的是配置标签的展示文案，包括名称、获取规则、有效期、标签 ICON、标签颜色
>
> 注意：这里不涉及任何接口能力，只是用于配置标签的展示样式。
>
> 成功提交后进入审核流程，审核通过会以站内信&端内通知，**审核通过后可以获得标签 id 用于技术配置！**单游戏最多上架9个标签

![](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/5e8e84c26bfd4c52abf46b6167f01d78~tplv-9nona0m7ha-image.image)

新增标签入口

![](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/41c88b79f8df41099d77430b7b0ced17~tplv-9nona0m7ha-image.image)

配置标签文案&图片素材

### 4.通过接口完成标签下发

下发方式详见下方技术接入指引

## 五、技术接入指引

### open api

[设置用户群标签\_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/game-group-tag/set-group-tag)

[查询用户群标签\_小游戏\_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/game-group-tag/get-user-group-tag)

#### js api

[tt.setGroupTag\_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/im-group/tt-set-group-tag)

[tt.getUserGroupTagInfo\_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/im-group/tt-getusergrouptaginfo)

### c# api

[群标签能力\_小游戏\_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/open-ability/group-tag)

## 六、示例

本期一个用户只能展示一个标签，后续才会支持多个标签且能够顺延标签(比如第4个场景，二期才会支持顺延为123)

目前新的下发标签会替换掉上一个标签，平台不存上一个标签是什么

|  |  |
| --- | --- |
| 下发和删除操作 | 结果 |
| 1.下发后删除  a.给 A 用户佩戴一个标签 123  b.给 A 用户删除一个标签 123 | 无标签 |
| 2.连续下发标签  a.给 A 用户佩戴一个标签 123  b.给 A 用户佩戴一个标签 456 | 佩戴 456 |
| 3.删除最早的一个标签  a.给 A 用户佩戴一个标签 123  b.给 A 用户佩戴一个标签 456  c.给 A 用户删除一个标签 123 | 佩戴 456 |
| 4.删除最后一个标签  a.给 A 用户佩戴一个标签 123  b.给 A 用户佩戴一个标签 456  c.给 A 用户删除一个标签 456 | 无标签   |
