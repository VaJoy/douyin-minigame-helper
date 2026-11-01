---
title: "运行环境"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/runtime/env
update_time: 2025-09-22
---

抖音小游戏在以下平台采用不同的JavaScript执行引擎：

| 平台 | 执行引擎 | 技术说明 |
| --- | --- | --- |
| iOS客户端 | JavaScriptCore | Apple提供的JavaScript引擎 |
| Android客户端 | [V8引擎](https://v8.dev/) | Google开发的高性能JavaScript引擎 |
| 开发者工具 | [Electron](https://www.electronjs.org/) | 基于Chromium的桌面应用框架 |

## 平台差异说明
#### 主要差异点
  **语法支持差异**：
  - 各平台对ECMAScript新特性的支持程度不同
  - 建议通过[setting设置](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/code-edit/project-config#afdc577e)进行ES6到ES5的转换

  **API支持差异**：
  - 基础库内置了必要的Polyfill补丁
  - 详细支持情况参考[运行环境支持文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/runtime-performance/performance-optimization#365822b6)

### 重要注意事项
**开发者工具限制说明**：
- 开发者工具仅用于开发调试阶段
- 最终功能表现请以真机客户端为准
- 建议在发布前进行多平台真机测试
