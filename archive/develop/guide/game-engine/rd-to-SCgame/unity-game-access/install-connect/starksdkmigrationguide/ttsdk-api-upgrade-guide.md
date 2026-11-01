---
title: "TTSDK API 升级工具使用说明"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/install-connect/starksdkmigrationguide/ttsdk-api-upgrade-guide
update_time: 2024-10-12
---

## 背景
抖音 Unity 小游戏提供的 C# SDK，在版本 【6.0.0】 之后升级了 API 的调用方式，由原来的 `StarkSDK.API` 升级为 `TT` 的调用形式。
原 StarkSDKSpace 名称空间的 `StarkSDK.API `依然可正常使用，但之后版本会逐渐废弃，建议开发者尽快升级到 `TT` 的调用形式
**推荐：**
- 新接入 Unity C# SDK 的开发者，直接使用 TTSDK 名称空间 `TT` 的 API 调用形式
- 已经使用低版本 StarkSDSpace 名称空间 `StarkSDK.API`的开发者，升级后可更改为使用 `TT` 的 API 调用形式，抖音小游戏也提供了脚本文件方便协助修改升级，运行脚本后还需要开发者手动检查

## 升级 TTSDK
- 接入参考文档：[旧版StarkSdk API迁移TTSDK API说明文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/starksdk-migration-guide)
- C# SDK 版本：【6.0.0】及以上

## API 升级工具使用

> - API 升级脚本的操作会修改本地给定目录的代码，请做好代码备份！！！
> - 升级工具是文本替换，做不到 100% 准确，运行后还需要手动检查！！！

升级 TTSDK （原 StarkSDK，6.0.0 版本后改名为 TTSDK）后，建议升级 API 调用方式到 TT。协助脚本使用如下：
- 入口：「ByteGame」->「TTSDK API UPDATE」

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/415d14fc4c8d40bca675ef4cebb7306e)

- 替换目录：InputPath 输入项目的代码目录，从 Assets 开始，如 Assets/Scripts/Demo，本升级工具会扫描改目录下的 CS 文件，并检查 Stark 调用替换为 TT 调用

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/d4f8cbb03f324d28a5dda057e63dd2b2)

- 确认操作：再次确认开始替换操作

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/ff9d7492cb2b489d9d0384a444223c6c)

### 工具运行后检查
- 成功运行后，会将一些提示操作写入 前面输入的 <InputPath>/note.txt 文件中，可打开该文件参考做一些修改
- 项目中全局检查，参考官方文档和 API 说明手动更正替换不全或有误的地方
