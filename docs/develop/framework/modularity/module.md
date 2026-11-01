---
title: "module"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/modularity/module
update_time: 2024-07-24
---

## Object module
当前模块对象
## 属性
| 名称 | 数据类型 | 描述 |
| --------- | -------- | ----------------------------------------------------- |
| `exports` | `Object` | 模块向外暴露的对象，使用`require`引用该模块时可以获取 |
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
