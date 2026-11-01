---
title: "UnionID 机制说明"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/user-info/unionid-intro
update_time: 2025-08-27
---

当开发者运营多个抖音小游戏时，可通过 UnionID 机制确保用户身份的唯一性。同一用户在使用同一抖音开放平台账号下的不同应用时，其 UnionID 将保持一致。

## UnionID 核心特性
- **跨应用统一标识**：
1. 小程序小游戏不互通
1. 小游戏的抖音app,抖音极速版,抖音火山版不互通
1. 抖音下开发者的所有小游戏 UnionID 互通
- **无需重复授权**：基础 UnionID 获取不强制要求用户授权
### UnionID 获取方式
已绑定开放平台的小游戏可通过以下方式获取：
  - 使用 [tt.login](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/log-in/tt-login) 登录接口配合[code2Session](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/log-in/code-2-session) 即可获取
  - 适用场景：基础用户识别场景
