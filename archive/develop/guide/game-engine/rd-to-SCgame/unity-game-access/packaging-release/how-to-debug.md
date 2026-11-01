---
title: "错误堆栈与异常排查"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/packaging-release/how-to-debug
update_time: 2025-10-11
---

本文将介绍抖音小游戏在开发者工具或真机上出现异常时，开发者该如何排查并解决问题。

## 未启用分包时
默认构建参数下（DebugSymbols 选项为 External 时），错误堆栈可能显示如下：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/d32fadb136ac436d98da959eb8a0777d~tplv-9nona0m7ha-image.image)

其中 wasm 函数显示为不可读的 “func + 函数 ID” ，在未启用 wasm 代码分包时，有两种方式获取原始堆栈信息：

1. 借助符号表还原函数名称。符号表文件通常位于小游戏包同级目录下的 wasm_symbols目录下：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/bd263be120344933b8b4b0a7aea4926c~tplv-9nona0m7ha-image.image)

解压后为一个 json 文件，保存了函数 ID 到函数名的映射，例如上面的报错前三个函数可查表还原为：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/6fa1f61c06fd4b16968d9a9a518e0ef2~tplv-9nona0m7ha-image.image)

1. 修改构建参数，将函数名打入 wasm 包体内：
在 TTSDK 构建工具面板中，将 DebugSymbols 选项调整为 Embedded，此时 wasm 包体内将包含有函数名称

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/8010aa5316d84914bdb6ca686d5c7277~tplv-9nona0m7ha-image.image)

此时错误堆栈如下：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/8f4b2f2c48164c14bdede979716c7158~tplv-9nona0m7ha-image.image)

**注意：使用 Embedded 选项后，wasm 包体体积将大幅上升，请勿在线上版本中使用。且此时由于没有符号表文件，无法开启分包。**

## 启用分包时
启用 wasm 分包后，由于原来的函数分散到了两个 wasm 文件内，堆栈中显示的函数 ID 会发生变化，无法使用原始的符号表文件还原堆栈。
如图，左侧为分包前，右侧为分包后，可以看到函数 ID 发生变化：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/6f52f2e0b5e34902bcb9af4a16b5000e~tplv-9nona0m7ha-image.image)

此时需要在分包时修改分包类型为 debug（需要抖音开发者工具版本号>=4.4.6）：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/e7832ff5dc23480aadced8a76285b14b~tplv-9nona0m7ha-image.image)

相比于 release 包，debug 包会将原始函数 ID 作为函数名打入分包后的 wasm 文件中。如图，左侧为分包前堆栈，右侧为分包后堆栈，可以看到分包后堆栈中显示为 “f + 函数 ID”，其中函数 ID 与原始函数 ID 相同，可查询符号表还原堆栈。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/03d17cb22ba74a99917b38fac44401eb~tplv-9nona0m7ha-image.image)

**注意：由于 debug 包中包含了“f + ID” 形式的函数名，相比于 release 包体体积有小幅上升，线上版本推荐使用 release 包。**
