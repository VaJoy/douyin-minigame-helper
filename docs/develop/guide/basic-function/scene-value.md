---
title: "场景值"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/basic-function/scene-value
update_time: 2025-08-20
---

> ⚠️ 注意，基础库 1.12.0 开始支持此功能
## 场景值概述
场景值用于追踪用户进入小游戏的来源路径。完整场景值定义请参考[**场景值列表**](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/scene-value)

### 系统限制说明
由于Android系统限制，以下情况无法获取准确场景值：
> 热启动时，拿到的场景值是首次冷启动的值
- 用户通过 Home 键退出游戏后，再次从桌面图标进入时，无法获取准确场景值
- 系统将保留上一次的场景值记录

### **获取场景值**
> 建议同时使用两种方式以确保场景值获取的准确性

开发者可通过以下API获取场景值信息：
#### 同步获取方式
通过 [tt.getLaunchOptionsSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/system/lifecycle/tt-get-launch-options-sync) 获取游戏启动时的初始场景值

#### 事件监听方式
监听游戏显示事件，通过  [tt.onShow](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/system/lifecycle/tt-on-show) 获取当前场景值

**
