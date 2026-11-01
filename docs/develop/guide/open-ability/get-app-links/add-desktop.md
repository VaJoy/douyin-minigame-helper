---
title: "添加到桌面"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/get-app-links/add-desktop
update_time: 2026-04-20
---

用户可以通过游戏右上角胶囊打开详情页，选择**添加到桌面**，添加后可直接从桌面打开小游戏。无需开发者接入，默认支持。

## 检查是否添加到桌面
### tt.checkShortcut

> 检查小游戏快捷方式是否已添加到手机桌面上。

详见[tt.checkShortcut](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/shortcut/check-shortcut)

### tt.addShortcut

> 可以将小游戏快捷方式添加到手机桌面上。

详见[tt.addShortcut](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/shortcut/add-shortcut)

## FAQ
##### Q: 无法从桌面打开开发版或体验版？
A: 添加到桌面仅支持正式版

##### Q: 桌面无法打开开发版，如何测试从桌面打开的场景？
A: 用开发者工具测试，开发者工具可自定义编译条件-进入场景

##### Q: 不同系统桌面打开的场景值是否有区别？
A: 抖音桌面打开场景值为021020
B: 抖音极速版桌面打开场景值为 101020
C: 番茄小说打开场景值为181020
D: 番茄畅听打开场景值为141020
E: 手机桌面直接打开场景值为991020
F: 今日头条打开场景值为011020
G: 今日头条极速版打开场景值为061020
H: 番茄畅听打开场景值为141020
