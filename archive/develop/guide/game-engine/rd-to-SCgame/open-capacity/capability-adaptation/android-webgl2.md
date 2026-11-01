---
title: "Android WebGL2.0支持"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/android-webgl2
update_time: 2024-10-15
---

## 使用建议
现Unity小游戏Android平台已经完成对WebGL2.0的适配支持（iOS15.0及以上系统已支持）。
不管是WebGL1.0还是WebGL2.0，都建议先在浏览器中运行，查看console相关报错以及渲染情况，无误后再发布在抖音中调试。
当前Android WebGL2.0已在抖音、抖音极速版上全量，已无需申请添加白名单。（非抖音系App，如：头条等，暂不支持WebGL2.0能力）
## 发布相关
1. 发布工具（StarkSDKUnityTools）升级至**3.30.4**版本。
1. 勾选**WebGL2（beta）**，并打包发布。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/e2d0e6168f3e4f33bc4457ae66bdd054)

1. 因现Android WebGL2.0已经全量，无需点击该按钮“加入WebGL2.0测试白名单”，直接勾选“WebGL2（beta）”即可。
## 风险周知
- 如遇到一些特殊的材质或者场景有未适配到渲染相关问题，可以随时联系反馈。
- WebGL2.0是在抖音**29.9.0**版本开始支持，在低版本会无法运行。
- 暂仅支持抖音/抖极。
