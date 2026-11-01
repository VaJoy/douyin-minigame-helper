---
title: "exports"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/modularity/exports
update_time: 2024-07-24
---

## Object exports
module.exports 的引用
## 示例代码
```js
// common.js
function sayHello(name) {
console.log(`Hello ${name} !`);
}
function sayGoodbye(name) {
console.log(`Goodbye ${name} !`);
}
module.exports.sayHello = sayHello;
exports.sayGoodbye = sayGoodbye;
```
