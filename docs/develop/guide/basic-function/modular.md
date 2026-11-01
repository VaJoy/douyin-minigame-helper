---
title: "模块化"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/basic-function/modular
update_time: 2025-06-16
---

## 模块导出机制
开发者可以将公共代码封装为独立的JS模块文件，通过`module.exports`或`exports`对外暴露接口。需要特别注意：
1. `exports`实质是`module.exports`的引用，修改`exports`指向可能导致异常，建议优先使用`module.exports`
2. 抖音小游戏暂不支持直接引入node_modules，推荐以下解决方案：
- 将所需依赖代码手动拷贝至项目目录
- 使用平台支持的npm管理功能

```js
// common.js
function sayHello(name) { console.log(`Hello ${name} !`) }
function sayGoodbye(name) { console.log(`Goodbye ${name} !`) }

module.exports.sayHello = sayHello
exports.sayGoodbye = sayGoodbye
*
```

## 作用域规则
### 文件作用域
JS文件中声明的变量/函数默认具有文件级作用域，不同文件中的同名变量不会相互影响。

### 全局对象
抖音小游戏提供全局对象`GameGlobal`（类比浏览器的window对象），可用于跨文件数据共享：

```js
// a.js 
GameGlobal.appConfig = { 
 version: '1.0.0' 
} 
 
// b.js 
console.log(GameGlobal.appConfig.version) // 输出"1.0.0"
```

## 注意事项
1. 模块加载采用CommonJS规范
2. 循环引用可能导致未定义行为
3. 全局变量应谨慎使用，避免命名冲突

// a.js

GameGlobal.globalData = 1

// b.js

console.log(GameGlobal.globalData) // 输出 "1"
