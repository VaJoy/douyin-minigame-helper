---
title: "console"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/basic-function/console
update_time: 2024-07-24
---

向调试面板中打印日志。console 是一个全局对象，可以直接访问。在客户端中，向 vConsole 中输出日志。
## 方法

| 调用方法 | 说明 |
| --- | --- |
| `console.log()` | 向调试面板中打印 log 日志 |
| `console.info()` | 向调试面板中打印 info 日志 |
| `console.warn()` | 向调试面板中打印 warn 日志 |
| `console.debug()` | 向调试面板中打印 debug 日志 |
| `console.error()` | 向调试面板中打印 error 日志 |
| `console.group(string label)` | 在调试面板中创建一个新的分组。随后输出的内容都会被添加一个缩进，表示该内容属于当前分组。调用 console.groupEnd 之后分组结束。 |
| `console.groupEnd()` | 结束由 console.group 创建的分组 |

## 注意
- 由于 vConsole 功能有限，以及不同客户端对 console 方法的支持情况有差异，建议开发者在小程序中只使用本文档中提供的方法。
- 部分内容展示的限制请参见[调试](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/developer-instrument/development-assistance/real-machine-adjust/)
- 注意，真机环境时，开始调试模式 vConsole 页面的情况下，高频率的进行日志输出会对小游戏性能产生影响。
