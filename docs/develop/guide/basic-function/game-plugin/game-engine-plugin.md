---
title: "游戏引擎插件"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/basic-function/game-plugin/game-engine-plugin
update_time: 2025-08-25
---

## 简介

在目前的小游戏生态中，绝大多数小游戏使用游戏引擎开发，使用的游戏引擎版本相似或相同，且在代码包中占比较大。为此，抖音小游戏推出游戏引擎插件能力，引擎插件能力即是游戏引擎(作为插件)单独在抖音客户端进行缓存。当小游戏首次启动时，**如果本地已经存在同类别同版本游戏引擎插件，则可直接复用本地已经存在游戏引擎插件的代码，从而提升启动速度。此外，如果使用了游戏引擎插件功能，游戏引擎插件代码包的体积将不计算在游戏本身所占用的体积内。**
### 配置使用
使用游戏引擎新版本导出抖音小游戏，在导出时勾选「启用抖音引擎插件」即可，**无需手动修改**。目前支持的游戏引擎参见附录。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/4da92a6d234445a092b28340e04a8cab~tplv-9nona0m7ha-image.image)

使用了插件分离的小游戏，启动时在 vConsole 中会输出如下的日志：

```text
plugin ttxxxxxxxxxx inject success!
```

### 版本要求
抖音客户端版本 >= 33.8.0 & 基础库版本大于3.65.0，在不满足版本要求的运行环境上会自动降级到原来的未使用引擎插件的模式，**建议开发者在低版本客户端上进行兼容测试。**
### 附录
#### 支持的游戏引擎
以下游戏引擎默认支持Cocos Creator 3.8.7 及以上版本
我们将持续与各方游戏引擎厂商合作来提供更多的游戏引擎及更全面的版本支持。
#### 使用引擎插件后的代码改动
以 Cocos Creator 为例，当使用引擎插件功能进行导出后，代码结构上会有以下几处变化：
1. 由于大部分的引擎相关代码已上传到平台侧，cocos-js 的产物将大大减小；
1. `game.json`中会新增游戏引擎插件相关的配置，此配置为游戏引擎默认填充，不建议开发者随意改动；

```json
{
  "deviceOrientation": "portrait",
  "showStatusBar": false,
  "networkTimeout": {
    "request": 5000,
    "connectSocket": 5000,
    "uploadFile": 5000,
    "downloadFile": 500000
  },
  "plugins": {
    "cocos": {
      "version": "3.8.7",
      "provider": "tt8bf0fd4d14fb3db712"
    }
  }
}
```

1. JS 代码中使用引擎插件代码的方式发生变化：

```js
// 使用引擎插件前
require('xxx.js')
// 使用引擎插件后
requirePlugin('cocos/xx.js')
```

如果在使用过程中遇到任何问题，欢迎联系技术客服获取支持。
### 支持的游戏引擎
[CocosCreator](https://www.cocos.com/creator-download)（持续更新中）
### 注意事项
1. 禁止手动修改自动生成的插件配置
1. 建议在真机环境下验证插件加载状态

{
"provider":"wxidfsdfsdfsdfsdf",
"signature": [
{
"path": "aaa-js.js",//相对插件目录的路径
"md5": "5951fef57e1b6902a1c5e5ae5a6ea441"
}
]
}

{
"plugins": {
"alias": { // 自定义的alias 是 requirePlugin 时用的 alias
"provider": "wxidfsdfsdfsdfsdf",
"version": "1.0",
"path": "aaa"//目录结构
}

xxxx-lib
--test.js //插件实现文件(可包含多个)
--plugin.json  //插件配置文件
--signature.json //插件文件校验文件

1、requirePlugin('alias') -- plugin.json中配置的alias
2、requirePlugin('alias/xxx.js') -- 指定任意js文件

{
"plugins": {
"cocos": {
"version": "3.8.7",
"provider": "tt8bf0fd4d14fb3db712"
}
API调用调整

{
"main": "index.js"  //插件入口文件
}

plugin ***** inject success/fail!
