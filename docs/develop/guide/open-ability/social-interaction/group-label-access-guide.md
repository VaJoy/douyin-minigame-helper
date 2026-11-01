---
title: "群标签能力接入指南"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/social-interaction/group-label-access-guide
update_time: 2025-11-28
---

## 能力简介
群标签能力可以满足群粉丝在群内聊天时，在群昵称后自动携带由厂商配置的称号标签，且点击标签即可查询标签规则。
### 示例介绍
群主选择标签

| 进入群聊设置页 | 添加更多标签 | 绑定应用 | 添加标签 |
| --- | --- | --- | --- |

群聊展示标签（粉丝自动携带）

| 群聊展示标签 | 点击标签查看铭牌卡&游戏入口 | 标签规则详情页&游戏入口 |
| --- | --- | --- |

### 接入收益
- 游戏群活跃：单日进入群新增**+150%、**群发言人数**+150%**
- 游戏启动渗透：单日群成员进入游戏**+5%**
## 能力接入
### 能力申请入口

| **示意图** | **描述** |
| --- | --- |
|  | **开始接入：** Step 1：点击「运营」板块-「能力中心」 Step 2：找到「运营能力」模块-点击「抖音群聊能力」即可开始接入 Step 3：进入后选择「群标签能力」tab Step 4：了解相关内容后，点击「开始接入」，即开始接入流程 |

### 接入流程简述

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/179f831469ac4a108a1936daf9da792a~tplv-9nona0m7ha-image.image)

### 接入流程介绍
#### Step1：完成基础配置
> 基础配置指的是配置铭牌卡的背景图，此图应用于该游戏的所有标签卡片。
> 若调整背景图，将同步更新所有标签卡片；
> 最多可上传1张图，图片尺寸**1200*540**，大小不超1M，支持 jpg、jpeg、png 格式
> 图片上传后会进入审核链路，审核结果将通过开放平台站内信同步

| 基础配置入口 | 背景图配置 |
| --- | --- |

#### Step2：新增标签配置
> 新增标签配置指的是配置标签的展示文案，包括名称、获取规则、有效期、标签 ICON、标签颜色
> 注意：这里不涉及任何接口能力，只是用于配置标签的展示样式。
> 成功提交后进入审核流程，审核通过会以站内信&端内通知，**审核通过后可以获得标签 id 用于技术配置！**
> 单游戏最多上架9个标签

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/c8d8ae4a730e4606a95275800f291c4d~tplv-9nona0m7ha-image.image)

#### Step3：通过接口完成标签下发
接入下方任意一种技术类型的 API 即可

| 技术类型 | 技术文档 |
| --- | --- |
| OpenAPI | [设置用户群标签_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/social-interaction/group-label-ability/set-user-tags) [查询用户群标签_小游戏_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/social-interaction/group-label-ability/get-user-group-tag) |
| JSAPI | [tt.setGroupTag_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/social-interaction/group-label-ability/tt-set-group-tag) [tt.getUserGroupTagInfo_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/social-interaction/group-label-ability/tt-getuser-taginfo) |
| C# API | [群标签能力_小游戏_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/open-ability/social-interaction/group-label-ability/group-tag) |

#### 可选接入（优化群标签主动曝光）
目前通过接口给某个用户完成标签下发后，还需要用户在「群聊内」完成授权，才能展示用户标签

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/2e3f4a30768c468aa19d3eb7ba323901~tplv-9nona0m7ha-image.image)

如需更前置的引导用户完成授权，可在「小游戏内」接入 [tt.authorize](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/authorization/tt-authorize) ，传入 scope.groupTag 进行授权弹窗唤起，效果如下：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/69d8df80814d4667a1e14396295b4b32~tplv-9nona0m7ha-image.image)

## FAQ
目前一个用户只能展示一个标签，示例如下：

| 操作 | 结果 |
| --- | --- |
| 下发后删除 给 A 用户佩戴一个标签 123 给 A 用户删除一个标签 123 | 无标签 |
| 连续下发标签 给 A 用户佩戴一个标签 123 给 A 用户佩戴一个标签 456 | 佩戴 456 |
| 删除最早的一个标签 给 A 用户佩戴一个标签 123 给 A 用户佩戴一个标签 456 给 A 用户删除一个标签 123 | 佩戴 456 |
| 删除最后一个标签 给 A 用户佩戴一个标签 123 给 A 用户佩戴一个标签 456 给 A 用户删除一个标签 456 | 无标签 |
