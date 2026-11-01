---
title: "低版本兼容"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/runtime/client-lib/compatibility
update_time: 2025-04-30
---

抖音小游戏目前迭代比较快，各个 app 之间差异也比较大，开发者需要做好兼容工作，避免因为在低版本上使用了一个不兼容的 api 而出现体验问题。一般可以通过版本号比较、api 存在判断、tt.canIUse 三种方式进行兼容处理。另外上线发布的时候也可以选择支持小游戏的最低基础库版本。
## 版本号比较
可以通过[tt.getSystemInfo](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/system/system-information/tt-get-system-info)或者[tt.getSystemInfoSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/system/system-information/tt-get-system-info-sync)得到`SDKVersion`，`SDKVersion`是三位版本号，由[大版本].[小版本].[修订版本]三部分组成，例如：1.11.1。一般会在 api 文档上标注支持该 api 的最低版本，或者在组件文档上标注支持某个属性的最低版本。
## api 存在判断
一般新增的 api 在低版本基础库上是不存在的，贸然调用会导致错误。建议做如下判断：

```js
if (tt.navigateToMiniProgram) {
  tt.navigateToMiniProgram();
} else {
  tt.showModal({
    title: "提示",
    content:
      "当前客户端版本过低，无法使用该功能，请升级客户端或关闭后重启更新。",
  });
}
```

## 基础库最低版本限制
可在 [小游戏管理页](https://developer.open-douyin.com/console?type=2) 【设置】-【基础设置】- 【服务与功能】-【基础库最低版本号】中设置

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/3ba48e3388dc4048ad7984a91654ba29)
