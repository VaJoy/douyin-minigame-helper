---
title: "进阶指南"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/dev-guide/study-guide
update_time: 2025-12-01
---

如果你已具备小游戏开发基础知识并想深入学习，可依代码习惯选择合适方式。
## 使用JavaScript/TypeScript开发
### **小游戏与Web游戏的区别**
若你是前端开发工程师，或乐意学习JavaScript（[点击学习](https://web.dev/learn/javascript)），上手小游戏不难。可将小游戏视为仅有全屏Canvas的页面，无DOM与CSS，仅能执行JS，代码从game.js入口启动，基于Canvas渲染结合抖音小游戏API实现。
### **学习开发途径**
对游戏渲染感兴趣，可阅读[WebGL文档](https://webglfundamentals.org/webgl/lessons/zh_cn/)了解底层知识。
不过更推荐阅读游戏引擎文档，其提供可视化编辑器，便于上手且适配不同小游戏平台。开发者利用游戏引擎封装的组件，并调用抖音小游戏API，就能完成抖音小游戏的开发。如[Cocos Creator官方文档](https://docs.cocos.com/) 、[LayaAir官方文档](https://layaair.layabox.com/#/doc) 。
另外，像[PixiJS](https://pixijs.com/)和[ThreeJS](https://threejs.org/)等引擎，引入[tt-adapter](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/runtime/adapter)并做适配调整也能发布到小游戏，但不建议无经验开发者使用。
## 使用C#开发
### **已熟练掌握Unity游戏**
我们推荐您直接查阅[Unity引擎适配](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/install-connect/sc_access_guide)和[C# API](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/api-overview)，可以快速的把已有的Unity游戏转换为抖音小游戏。
### **学习开发Unity游戏**
可参考[Unity官方文档](https://docs.unity.cn/cn/current/Manual/UnityManual.html) 、[团结引擎官方文档](https://docs.unity.cn/cn/tuanjiemanual/Manual/) 、[Unity中文课堂](https://learn.u3d.cn/) 。
