---
title: "实时日志"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/runtime/debug/real-time-log
update_time: 2025-04-30
---

## 简介
为了补齐小游戏开发环节中的线上排查能力，帮助开发者自助解决问题，我们推出了实时日志功能。开发者可通过 tt.getRealtimeLogManager 打印实时日志，日志将实时上报到开发者平台的控制台。开发者可从平台的「控制台 -> 数据 -> 性能分析 -> 日志查询」进入日志查询页面，查看开发者打印的日志信息。
普通小游戏该 api 的具体使用方法可以参考 [tt.getRealtimeLogManager](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/debugging/tt-get-realtimelog-manager) 文档，unity 小游戏可以参考 [RealtimeLogManager](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/basics/debugging/realtime-log-manager/realtime-log-manager) 文档。
### 如何使用
在基础库 3.55.0 版本以上可用，在小游戏代码中调用 tt.getRealtimeLogManager 来打日志，示例如下：

```js
const logger = tt.getRealtimeLogManager();
logger.setFilterMsg('mainScene');
logger.debug('调试 debug')
logger.info('调试 info')
logger.log('调试 log')
logger.warn('调试 warn')
logger.error('调试 error')
```

当小游戏执行了打印日志的代码后，将能在后台查询页面看到对应的输出（实际情况可能有几分钟的延迟）。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/23110c2f611a4f4d8767f46896add07b)

由于后台资源限制，“实时日志”使用规则如下：
1. **每个小游戏账号**每天限制 2000 条日志，日志会保留 7 天，建议遇到问题及时定位。
1. 一条日志的限制长度** 256** 个字符，超出会被截断，避免在循环里面调用打日志接口，避免直接重写 console.log 的方式打日志，建议不要直接打印堆栈。
1. 打印的每一个参数会通过 JSON.stringify 序列化，请避免打印自循环引用的结构。
1. setFilterMsg 和 addFilterMsg 可设置类似日志 tag 的过滤字段。如需添加多个关键字，建议使用 addFilterMsg。例如 addFilterMsg('scene1'), addFilterMsg('scene2'),addFilterMsg('scene3')
1. addFilterMsg 和 setFilterMsg 的参数不能有空格。
1. 实时日志目前只支持在**手机端**测试。工具端的接口可以调用，但不会上报到后台。
1. **非线上版本**的日志只能通过 vconsole 来查看日志上报情况， 不会上报到后台。
