---
title: "代码包"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/basic-function/subpackages/introduction
update_time: 2025-04-15
---

> 基础库 1.88.0 及以上版本开始支持，使用小游戏 IDE 进行开发，可[点击下载](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/developer-instrument/developer-instrument-update-and-download)。
随着小游戏的玩法越来越丰富，开发者对于扩大包大小的需求越来越强烈，所以我们推出了小游戏分包加载这一个功能。 所谓的分包加载，即把游戏内容按一定规则拆分为几个包，在首次启动时先下载必要的包，这个必要的包我们称为「主包」，开发者可以在主包内触发其它分包的下载，从而把首次启动的下载耗时分散到游戏运行中。
IDE 对包体积大小有一定限制，分包与非分包小游戏限制也不尽相同。具体请见：[字节跳动小游戏 - 代码包体积限制说明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/mini-game/bytedance-mini-game#%E4%BB%A3%E7%A0%81%E5%8C%85%E9%99%90%E5%88%B6)。
对小游戏进行分包，可以优化小游戏首次启动的下载时间，以及在多团队共同开发时可以更好的解耦协作。具体使用方法请参考：
- [普通分包](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/subpackages/basic)
**普通小游戏包**
未配置分包的场景下，每个小游戏允许上传的代码包总大小上限为 20MB。
**分包后小游戏包**
对于配置了分包的小游戏，默认限制为：
- 小游戏整体包（小游戏包整个目录）大小不超过 20MB，开通虚拟支付后的小游戏不超过30M。
- 单个主包不超过 4MB
- 单个分包大小不超过 20MB，开通虚拟支付后的小游戏不超过30M。
