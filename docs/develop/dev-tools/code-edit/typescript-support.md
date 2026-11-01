---
title: "TypeScript 支持"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/code-edit/typescript-support
update_time: 2025-05-27
---

## 环境准备
要构建 TypeScript 项目，您需要：
1. 安装 [Node.js](https://nodejs.org/)（包含 npm 包管理器）
1. 通过项目配置设置预处理命令

## 编译配置
您可以通过以下方式配置 TypeScript 编译：
1. 在项目配置中添加 `tsc` 编译命令作为预处理步骤
1. 使用 `tsconfig.json` 文件自定义编译选项（参考[官方文档](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html)）

## 注意事项
1. 抖音小游戏运行环境仅支持 JavaScript 文件
1. 所有 `.ts` 源文件默认不会包含在最终发布包中
1. 确保编译后的 `.js` 文件路径与原始 `.ts` 文件保持一致

## 推荐实践
1. 在 `package.json` 中配置开发依赖
1. 使用 `--watch` 模式进行持续编译
1. 定期检查编译输出是否符合预期
