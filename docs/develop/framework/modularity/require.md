---
title: "require"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/modularity/require
update_time: 2024-07-24
---

## any require(string path)
引入模块。返回模块通过 [module.exports](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/modularity/module) 或 exports 暴露的接口。
## 参数

| 名称 | 数据类型 | 描述 |
| --- | --- | --- |
| `path` | `String` | 需要引入模块文件相对于当前文件的相对路径，不支持绝对路径 |

**具体路径参考图片**
![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1665281908873 "common.js 定义模块")
**使用相对路径** ![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1665282126533)
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
```js
// game.js 中
var common = require("./common/common.js");
common.sayGoodbye("test goodbye");
common.sayHello("test hello");
```
