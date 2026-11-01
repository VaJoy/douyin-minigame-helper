---
title: "官方群能力接入指南"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/social-interaction/official-group-capability-guide
update_time: 2026-04-10
---

## 能力简介
官方群能力是小游戏平台侧提供的创建游戏官方粉丝群的能力，小游戏无需下载、即点即玩的特点，非常适合抖音的好友进行互动，群聊能力能够有效帮助提升用户的长线留存，也方便开发者与用户形成良好互动。
### 示例介绍

| **用户官方群入口** | **用户加入群聊** | **群内固定复访入口** |
| --- | --- | --- |
| 游戏内放置官方群入口，引导用户进入官方群 | 用户点击官方群入口，唤起加群页面，加入群聊 | 通过在后台绑定的官方账号，账号下所有的群聊都会展示游戏固定复访入口 |

### 接入收益

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/a51b6dd39b90435e914c75f45faeec36~tplv-9nona0m7ha-image.image)

## 能力接入
### 能力申请入口
首先，登录开发者平台，找到 「运营 - 运营能力 - 官方群能力」进行能力的开通

| **示意图** | **描述** |
| --- | --- |
|  | **开始接入：** Step 1：点击「能力」板块 -「能力中心」 Step 2：找到「社交能力」模块-点击「抖音群聊能力」即可开始接入 Step 3：进入后选择「官方群能力」tab Step 4：了解相关内容后，点击「开始接入」，即开始接入流程 |

### 接入流程简述

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/6d5e81ec82924048be52837bd43062ed~tplv-9nona0m7ha-image.image)

### 接入流程详情
#### Step 1：创建群聊并获取群ID

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/80337a109c904564825ac8a5e9c42dff~tplv-9nona0m7ha-image.image)

在开放平台创建群聊后，平台会生成群ID（这个 ID 在后续的 API 调用中至关重要）。
在开放平台上创建群聊前，需要先绑定抖音号（群主将默认为当前绑定的抖音号）

> **注意：绑定操作不可逆！**
> 请谨慎选择用于绑定的抖音号，一旦创建群聊，**群主账号将无法解绑**

绑定完成后，按照下面路径将群展示在个人主页，（路径：个人主页-设置-抖音创作者中心-主播中心-直播服务-更多-公开群），将群聊设置为展示。视频教程如下：

视频链接：[https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/f7b9a165dd7a4b29bbe52f9b50f57935~tplv-9nona0m7ha-image.image](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/f7b9a165dd7a4b29bbe52f9b50f57935~tplv-9nona0m7ha-image.image)

#### Step 2：游戏添加加群入口
创建群聊后，在游戏内设计加入群聊的入口，引导用户加入群聊。如：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/2fde76d799884410a87c000b796ff6aa~tplv-9nona0m7ha-image.image)

#### Step 3：玩家加群
游戏加群入口添加完成后，玩家点击加入后，通过调用 tt.joingroup 方法，传入 groupid（创建群聊后，在控制台获取） 后，玩家即可快捷地在游戏内加入官方群中。

```js
tt.joinGroup({
  groupid: "998877", //加入的群id，可在平台创建群聊后获得
  sessionFrom: "sessionFrom",
  extraInfo: "extraInfo",
  success(res) {
    console.log(res);
  },
  fail(res) {
    console.log(res);
  },
});
```
