---
title: "JS 支持情况"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/runtime/js-support
update_time: 2025-08-20
---

## 安全限制
基于平台安全策略，抖音小游戏运行环境禁止以下动态代码执行行为：
- 禁止使用 `eval()` 函数执行代码
- 禁止通过 `new Function()` 构造函数动态创建函数

## ECMAScript 标准支持
### 运行环境差异
抖音小游戏在不同终端设备上的 [JavaScript 执行环境](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/runtime-performance/performance-optimization) 存在平台差异性，导致 ECMAScript 标准支持程度不同。

### Polyfill 解决方案
平台基础库集成了 [core-js](https://github.com/zloirock/core-js) 补丁库，可自动填充缺失的标准 API。但需注意：
1. 语法差异无法通过 Polyfill 解决
1. 使用高级语法（如 [async/await](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/async_function)）时，需配合 [代码编译工具](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/code-compile/native-language-compile) 进行转译

## 兼容性注意事项
### 受限 API
以下特性在低版本运行环境中不可用：
- `Proxy` 对象（全版本不可用）

### Promise 执行时序
由于 iOS 15 及以下系统使用 `setTimeout` 模拟 Promise 实现：
1. 导致 Promise 回调变为宏任务（非标准微任务）
1. 执行时序与标准规范存在差异
1. iOS 16+ 版本已修复此问题

```js
// 时序验证示例 
const stack = []; 
setTimeout(() => stack.push(6), 0); 
stack.push(1); 
new Promise(resolve => { 
    stack.push(2); 
    resolve(); 
}).then(() => stack.push(5)); 
stack.push(3); 
setTimeout(() => { 
    // 标准环境输出：[1,2,3,5,6] 
    // iOS15 环境输出：[1,2,3,6,5] 
    console.log(stack);  
}, 1000);
```

var arr = []
setTimeout(() => arr.push(6), 0)
arr.push(1)
const p = newPromise(resolve => {
arr.push(2)
resolve()
})
arr.push(3)
p.then(() => arr.push(5))
arr.push(4)
setTimeout(() => arr.push(7), 0)
setTimeout(() => {
// 应该输出 [1,2,3,4,5,6,7]
// 在 iOS15 小游戏环境，这里会输出 [1,2,3,4,6,5,7]
console.log(arr)
}, 1000)
