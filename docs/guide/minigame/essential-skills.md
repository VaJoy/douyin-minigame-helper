---
title: "必接能力"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/minigame/essential-skills
update_time: 2025-12-08
---

开发前，建议您先阅读 [《小游戏开发准备》](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/minigame/sign)、[《开发规范》](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/mini-game-configuration)、[《运营规范》](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/agreement-and-norms/norms/introduction)和 [《设计规范》](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/advertise/norms)文档，以便更好地进行小游戏开发。
## 必接能力一览

| 必接能力 | 能力描述 | 能力详情 |
| --- | --- | --- |
| 侧边栏复访能力 | 所有小游戏必须接入【侧边栏复访能力】 | [「必接」侧边栏复访能力](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/-retention/sidebar) |
| 客服能力 | 内购游戏必须接入【客服能力】 | [抖音 IM 客服](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/user-service/douyinIM)：仅适用于抖音 App [抖音平台客服](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/user-ops/user-service/bytehi-im)：全 APP 通用且支持第三方消息推送 |
| 敏感词 | 游戏内存在用户可自定义输入时必须接入【敏感词】 | [tt.onKeyboardInput](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/interface/keyboard/tt-on-keyboard-input) [tt.offKeyboardComplete](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/interface/keyboard/tt-off-keyboard-complete) [tt.offKeyboardConfirm](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/interface/keyboard/tt-off-keyboard-confirm) |