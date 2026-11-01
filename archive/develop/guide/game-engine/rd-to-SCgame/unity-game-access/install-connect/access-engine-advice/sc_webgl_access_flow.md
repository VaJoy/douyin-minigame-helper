---
title: "WebGL方案接入流程"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/install-connect/access-engine-advice/sc_webgl_access_flow
update_time: 2025-06-11
---

> 文档说明：本文档描述使用Unity开发的游戏，在WebGL平台下，使用SC方案接入抖音小游戏的接入方法及可能遇到的问题。
> *了解更多：*[接入指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_access_guide)** **

目前 WebGL 方案支持 Unity 版本比较宽泛，具体版本及推荐参考：[推荐的引擎版本](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/overview-and-compatibility/sc_webgl_recommended_engine_version)
如使用团结引擎，推荐使用MiniGame平台
### 构建
#### WebGL平台（Unity，团结引擎）
1. 安装好 Unity WebGL 平台，即能够切换到如下所示的平台（构建工具在构建时也会切换）：

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/a15bb4e1077e4b8c9c4984c81d267715)

1. 安装TTSDK：[如何安装TTSDK](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/install-sdk)
1. 构建：参考该文档WebGL构建部分：[构建与调试](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_build)

#### MiniGame平台（团结引擎）
参考团结引擎官方文档：[抖音平台支持](https://docs.unity.cn/cn/tuanjiemanual/Manual/DouyinSDK.html)
### 发布
发布流程请参考文档：[游戏发布](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_publish)
### 测试
- iOS版本测试：从 Apple Store 中下载最新版本的抖音（确认抖音版本号 >= 17.7.0）。
- Android版本测试：安装最新版本抖音（确认抖音版本号 >= 19.0.0）。

使用 StarkSDKTools 发布工具工具生成二维码，用抖音扫码即可运行。
运行成功的话，可以看到屏幕右下角有一个按钮【**vConsole**】，这个按钮是一个日志显示的入口，只会有测试环境会出现，主要方便测试阶段排查问题。**线上版本不会出现这个按钮**。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/a474bac264a94c08b79901dee7fdddda)

### FAQ
1. 目前Unity编译出来的WebGL版本默认不支持中文，需要单独放一个中文字体库。
可以自行找一个喜欢的并支持中文的字体库。也可以下载下面这个中文字体库：

附件下载：[simhei.ttf.zip](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/7031fa022977461cbe623c9a48bd3a23)

1. WebGL不支持动态库，如有使用so，需找到webgl版本替代。
1. 同上，WebGL不支持SQLite数据库，可以使用[iBoxDB](https://www.iboxdb.com/)替代。
1. 支持C源码的原生插件
1. 支持C#插件
1. iOS上运行WebGL发热比较厉害，建议限帧运行。Application.targetFrameRate 建议值为22~30之间。
1. WebGL2.0支持情况：iOS支持15.0及以上系统，[Android WebGL2.0支持](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/android-webgl2)。
1. iOS下录屏：不建议使用。(判断平台，只在android下录屏分享)
   1. 会有录屏权限提醒；
   1. 对性能有消耗。
   1. iOS14.0系统以下不支持录屏
   1. 如果判断性能比较富裕，就是想要开启ios的录屏，那么iOS14.0及以上系统需要添加录屏白名单。

python -m http.server -d index.html文件所在的目录路径 8080 (端口号随便定，有效就行)

cd index.html文件所在的目录路径
python -m SimpleHTTPServer 8080 (端口号随便定，有效就行)

chmod +x ./http-utils # Windows下不需要执行这一行
## Mac下执行
./http-utils -dir index.html文件所在的目录路径 -port 8080 (随便定)
## Windows下执行（可以手动拖动http-utils.exe文件到命令行窗口）
.\http-utils.exe -dir index.html文件所在的目录路径 -port 8080 (随便定)
