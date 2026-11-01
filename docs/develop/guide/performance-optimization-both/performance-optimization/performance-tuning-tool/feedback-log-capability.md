---
title: "反馈日志能力"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/performance-optimization/performance-tuning-tool/feedback-log-capability
update_time: 2025-01-06
---

## 简介
小游戏上线后，用户可能会反馈一些测试时没有覆盖到的问题，这些问题可能会在特定的客户端或者基础库版本出现，或者在特殊的游戏场景下出现，为了能更好地处理用户反馈，平台提供了反馈日志的能力。
  开发者可以调用 tt.getLogManager 的相关 api 打印反馈日志，反馈日志存储在用户的客户端缓存中，仅在用户反馈提交成功时上传，开发者可以在 「管理 -> 用户反馈 」的反馈记录中点击下载日志（如果有上报的话）查看。
  普通小游戏该 api 的具体使用方法可以参考 [tt.getLogManager](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/debugging/tt-get-log-manager) 文档，unity 小游戏可以参考 [LogManager](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/basics/debugging/log-manager/log-manager) 文档。
## 使用方式
仅在抖音、抖音极速版、抖音火山版支持，基础库 3.55.0 以上版本可用，确保在调用日志 api 之前已经调用 tt.login 登录。之后在需要调用的位置打印日志，示例如下：

```typescript
const feedbackLogManager = tt.getLogManager();
feedbackLogManager.debug('debug 日志')
feedbackLogManager.info('info 日志')
feedbackLogManager.log('log 日志')
feedbackLogManager.warn('warn 日志')
feedbackLogManager.error('error 日志')
```

当用户通过抖音系宿主的 「小游戏右上角的胶囊按钮 -> 反馈与帮助 -> 向开发者反馈」中提交反馈，且本地存在反馈日志的时候就会尝试上传反馈日志到后台，后台的日志下载入口如下：

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/9b074d6249764fdd9bd20b7ca1b06166)

## 使用限制
1. 最多保存 **5M **的日志内容，超过 5M 后，旧的日志内容会被删除。同时，平台也会删除长期未使用的小游戏的反馈日志。
1. 每次调用最多 1000 个字符，超出后截断。
1. 谨慎打日志，避免在无限循环里面调用打日志接口，避免直接重写 console.log 的方式打日志，平台会做基本的频控，调用频率过高时会抛错。
1. 日志 api 的函数类型和 console 的接口类似，都能接受不定长的参数，但是内部实现是将每个参数分别做 JSON.stringify 后再以空格拼接，因此无法处理存在自循环的数据结构。
