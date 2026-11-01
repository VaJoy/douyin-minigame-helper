---
title: "API 类型声明"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/api-type-declaration
update_time: 2025-12-16
---

小游戏 API 的 TypeScript 类型定义文件，包含抖音小游戏 API 的接口定义、参数信息、参数说明、返回值类型等内容。使用 TS 开发的游戏工程可引入使用，提升开发效率和体验。
- npm地址：https://www.npmjs.com/package/@douyin-minigame/api-typings
## 安装

```bash
npm install @douyin-minigame/api-typings
```

## 使用
安装后手动进行导入。
- `import '@douyin-minigame/api-typings';`
也可以直接在项目的 `tsconfig.json` 配置文件中指定。
- `types: ["@douyin-minigame/api-typings"]`。
或者通过 [三斜杠指令](https://www.tslang.cn/docs/handbook/triple-slash-directives.html) 引用。
- `/// <reference path="node_modules/@douyin-minigame/api-typings/index.d.ts" />`
## Q&A
**Q1：最新版本的声明发现有缺失或错误？**
我们会定期更新接口声明。如果需要纠错或快速补充，请发起工单进行反馈
**Q2：接口的类型定义和文档站不一致怎么办？**
以文档接口描述为准。如果需要修复，同样请联系我们处理。
