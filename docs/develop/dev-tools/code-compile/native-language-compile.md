---
title: "原生语言编译"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/code-compile/native-language-compile
update_time: 2025-06-16
---

## 简介
原生语言编译是开发者工具推出的编译工具升级版本，由原生语言 Rust 开发而成，可以极大地提升代码编译速度。

## 版本支持
[开发者工具](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/developer-instrument-update-and-download)从 4.1.7 起支持该功能。

## 开启原生编译
1. 开发者可通过详情页工程配置模块的「开启原生语言快速编译」选项来开启或关闭该功能。
1. 也可在 project.config.json 文件中将 nativeCompile 字段值修改为 true 或 false 进行设置。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/d4d3b5fa70c943988516779ad21bddea~tplv-9nona0m7ha-image.image)

> ⚠️：目前原生语言编译属于实验功能，只作用于开发场景，不会影响线上。如果编译结果有问题影响项目开发，可以取消勾选，回退到正常编译，并请到社区反馈。
