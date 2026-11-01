---
title: "网络请求"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/basic-function/network
update_time: 2024-07-24
---

小游戏网络请求相关的 API 包括以下几种：
- [tt.request](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/network/initiate-a-request/tt-request)
- [tt.downloadFile](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/network/download/tt-download-file)
- [tt.uploadFile](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/network/onload/tt-upload-file)
- [tt.connectSocket](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/network/websocket/tt-connect-socket)
每个小游戏使用网络相关的 API 前需要事先设置域名白名单，小游戏只能与白名单中指定的域名进行网络通信。
## 配置域名白名单
配置前需要确保域名满足以下条件：
- 配置的域名只支持 HTTPS 协议。
- 配置的域名不能使用 IP 地址（小游戏的局域网 IP 除外）或 localhost。
- 配置的域名不能带上端口号，比如配置`https://server.com:8080`是非法的。小游戏默认支持白名单域名所有端口号的网络请求。
- 配置的域名必须经过 ICP 备案。
配置域名白名单的流程如下：
1. 进入[开发者平台](https://microapp.bytedance.com/)并在右上角进行登录。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1657270949867)

1. 找到自己要设置的小游戏，点击进入详情。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1657270949498)

1. 左侧菜单栏点击开发管理-开发设置。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1657270949394)

1. 点击修改，编辑服务器域名。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1657270949525)

## 小游戏网络请求 API 的特性
### 超时时间
- 默认超时时间和最大超时时间都是 60s。
- 超时时间可以在 app.json 中通过 [networkTimeout](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/mini-game-configuration) 配置。
### 使用限制
- 网络请求的请求头中的 `referer` 字段和 `user-agent`不可设置。
- [tt.request](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/network/initiate-a-request/tt-request) 的最大并发限制是 15 个。
- [tt.downloadFile](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/network/download/tt-download-file), [tt.uploadFile](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/network/onload/tt-upload-file), [tt.connectSocket](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/network/websocket/tt-connect-socket) 的最大并发限制是 5 个。
### 返回值编码
建议服务器返回值使用 UTF-8 编码。对于非 UTF-8 编码，小游戏会尝试进行转换，但是会有转换失败的可能。
### 回调函数
只要成功接收到服务器返回，无论 statusCode 是多少，都会进入 success 回调。请开发者根据业务逻辑对返回值进行判断。
## HTTPS 证书的要求
小游戏必须使用 HTTPS/WSS 发起网络请求。请求时系统会对服务器域名使用的 HTTPS 证书进行校验，如果校验失败，则请求不能成功发起。
由于系统限制，不同平台对于证书要求的严格程度不同。为了保证小游戏的兼容性，建议开发者按照最高标准进行证书配置，并使用相关工具检查现有证书是否符合要求。对证书要求如下：
**HTTPS 证书必须有效：**
- 证书必须被系统信任，即根证书已被系统内置。
- 部署 SSL 证书的网站域名必须与证书颁发的域名一致。
- 证书必须在有效期内。
- 证书的信任链必需完整（需要服务器配置）。
**iOS 不支持自签名证书。**
**iOS 下证书必须满足苹果 **[**App Transport Security(ATS)**](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW33)** 的要求。**
**TLS 必须支持 1.2 及以上版本。部分旧 Android 机型还未支持 TLS 1.2，请确保 HTTPS 服务器的 TLS 版本支持 1.2 及以上版本。**
**部分 CA 可能不被操作系统信任，请开发者在选择证书时注意小游戏和各系统的相关通告。**
证书有效性可以使用 `openssl s_client -connect example.com:443` 命令验证，也可以使用其他在线工具。
除了网络请求 API 外，小游戏中其他 HTTPS 请求如果出现异常，也请按上述流程进行检查。如 HTTPS 的图片无法加载、音视频无法播放等。
## 跳过域名校验
在字节小游戏开发者工具中，可以临时开启 `不校验合法域名、web-view(业务域名)、TLS 版本以及 HTTPS 证书` 选项，跳过服务器域名的校验。此时，开发者工具和手机调试模式中，不会进行服务器域名的校验。
在服务器域名配置成功后，建议开发者关闭此选项进行开发，并在各平台下进行测试，以确认服务器域名配置正确。
