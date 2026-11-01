---
title: "Data CDN功能"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/packaging-release/webgl-data-cdn-tutorial
update_time: 2026-09-01
---

> **警告**
> Data CDN功能会绕过平台内置的data预下载、预解压能力，**导致启动耗时有一定的劣化**，非必要的话，请勿使用该功能，如果包体超过大小，建议优先使用包体压缩功能，或者裁剪优化体积，Data CDN 功能尽量最后再考虑。

> **注意**
> TTSDK <= 6.9.0 的版本（对应 game.json 中版本插件 <= 4.39.0），有包状态下启动耗时会显著偏长（bug）。
> TTSDK >= 6.9.1 的版本修复了这个问题，如果用到了Data CDN功能，**建议开发者尽快升级至 6.9.1（含）及之后的版本。**提醒：只是修复了Data CDN功能的bug，相比不用Data CDN的包体，耗时还是会偏长，请谨慎选择。

## 简介
由于新包体格式设置了 30MB 的包体上限，给小游戏在上传、提审环节带来了不小的控制包体大小的挑战，因此我们在新包体格式中推出了 Data CDN 构建选项，允许开发者将 data 文件从包体剥离，放至开发者指定的 CDN 上，运行时再下载、加载。
> Data CDN 构建选项只支持新包体格式，不支持旧包体格式

## 操作方式
1. 确保打的是新包体格式。取消勾选【是否采用旧格式打包】。
1. 选择【压缩首包资源】或【Brotli压缩】。
1. 在 TTSDK 打包界面将 【首包资源加载方式】设置为 【CDN】。
1. 在【游戏资源CDN】中填入 CDN 前缀。该字段对应产物包 game.js 中的 managerConfig.DATA_CDN。
1. （可选）填写【首包资源加载前缀】字段。该字段一般默认为空即可，适用于开发者想将 data 文件放在 cdn 的指定目录。对应字段为 unity-namespace.js 中的 dataFileSubPrefix 字段。
1. 打包成功后，data 文件一般会在与 tt-minigame 同级的 webgl 目录下。
1. 将 data 文件上传到上面配置的 CDN 上。
1. 运行时会在启动时 拼接 data 文件完整路径进行下载：DATA_CDN + dataFileSubPrefix（一般为空字符串） + datafilename。其中 datafilename 为 game.js 中的 DATA_FILE_MD5 + “**webgl.data.unityweb.bin.br**"。
> 注意一定要在打包时选择 brotli 压缩资源，否则会出现拉不到资源的情况。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/41f0f6aeea0041edb18a082b7ebca64a~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/c79cc6041bce460daf24e10c21bc693f~tplv-9nona0m7ha-image.image)

## Q&A
### 采用 Data CDN 后 FP 耗时增长，正常吗？
分两种情况。
1. 如果是首次进入，会涉及到 data 文件的下载、解压、加载，FP 耗时增长属于正常现象，其中大部分为下载耗时。
1. 如果是有包状态，FP 耗时理论上和 Package 模式持平。如果发现耗时大幅增长，请联系我们排查。

IDE在内网测试中，11MB data数据，首包状态下，FP耗时增加1600ms，其中下载1500ms，br解压100ms。建议开发者关注cdn服务器下载速度。

TTSDK 6.9.0及之前的版本（对应game.json中版本插件4.39.0及之前），data文件下载到本地后，每次启动都会在JS侧进行br解压，导致fp耗时增长。建议开发者尽快升级至6.9.1（含）及之后的版本，fp耗时会有比较大的优化。

警告：Data CDN功能会绕过平台内置的data预下载、预解压能力，**导致启动耗时有一定的劣化**，非必要的话，请勿使用该功能，如果包体超过大小，建议优先包体压缩功能，或者裁剪优化体积，Data CDN 功能尽量最后再考虑。
TTSDK <= 6.9.0 的版本（对应 game.json 中版本插件 <= 4.39.0），有包状态下启动耗时会显著偏长。TTSDK >= 6.9.1 的版本修复了这个问题，**建议开发者尽快升级至 6.9.1（含）及之后的版本**，>= 6.9.1 只是优化了一部分
