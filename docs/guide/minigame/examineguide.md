---
title: "版本提审指引"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/minigame/examineguide
update_time: 2026-06-01
---

平台支持版本测试、版本审核、灰度发布、全量发布、查看线上版数据、查看灰度版数据。
## 特别提醒
- 为了保证通过率，请开发者提审前通过自测环节进行自查：[自审自查指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/agreement-and-norms/norms/standards)。
- 在审核过程中，开发者请遵循后台中的提示进行操作补全对应信息。
- 小游戏首次上线前的审核都需进行 QA 回归，预计在 1-3 个工作日。
- 自2026年4月20日起，开发者的提审将自动上线至所有已经接入抖音小游戏且符合要求的合作 App，则 QA 会默认回归多端。若任一宿主端未审核通过，则该版本需重新修改提审（其中若任一宿主端审核通过，下次提审版本号需要大于当前版本号）。
- 如果使用了网络相关功能，务必于后台配置“安全域名”的白名单，否则将影响游戏上线和正常功能。安全域名必须为 `https:// `及`wss://`协议，使用非加密传输协议的需修改服务器域名配置。
   1. request 合法域名
   1. socket 合法域名
   1. uploadFile 合法域名
   1. downloadFile 合法域名
## 版本概览

| **版本阶段** | **说明** | **适用版本** |
| --- | --- | --- |
| 线上版本 | 面向全部用户的正式版本 | 所有审核通过的版本 |
| 灰度版本 | 面向灰度用户的线上版本 | 审核通过的更新版本； 能进行灰度的前提是游戏当前有线上版本 |
| 审核版本 | 开发版本的提审阶段，通过之后可以发布上线，否则需要根据驳回原因退回修改，此版本请谨慎对外分享 | 所有版本 |
| 测试版本 | 开发版本的测试阶段，开发完成上传之后可以扫码进入测试体验，此版本请谨慎对外分享 | 所有版本 |

## 提审指引
### 1. 上传游戏包
#### 普通小游戏
1. 开发者在完成当前版本小游戏的开发与调试后，可以使用 IDE 工具编译上传游戏包。
    
![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/f297d127bc8841648bca4b09479acb8d)

1. 在「**上传**」对话框中填写「**上传版本**」、「**更新日志**」，然后点击「**确定**」。
    
![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/299bba9dbe13403a8ddcc03315dedce1)

1. 为满足开发者多项目并行测试的需求，支持最多同时上传 25 个测试版本，上传时分为“默认通道”和“通道1-24”。
   1. 未开启“选择测试通道”时，上传成功后，覆盖“默认通道”已有的测试版本。
      
![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/94f50355a20e463283c1aa0423d0f5da)

   1. 开发者如需同时保留多个测试版本，可以开启“选择测试通道” ，并根据需求选择 默认通道 或 通道1 - 24 进行上传。上传成功后，将覆盖所选通道的测试版本。 默认通道 和 通道1 - 24 通道的测试版本互不影响。
      
![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/c78cb009d9dd446abb37caa7438d1a42)

   1. 除开发者工具外，[CLI](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/developer-instrument/development-assistance/ide-cli#d6dd6956) 也支持指定测试通道进行上传。
1. 上传成功后，IDE 会提示上传成功，并引导跳转到控制台进行发布。
#### Unity 小游戏
请参照 进行开发上传。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1668149625559)

### 2. 测试版本
登录[抖音开放平台](https://developer.open-douyin.com/)，进入目标小游戏，在左侧导航栏选择「**开发版本管理**」，可以看到在 IDE 上传的测试版本代码包，此时点击体验版本扫码测试，测试完成后可点击「**提交审核**」。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/d3b7a721c3984c9a9c478963b9bbca15)

> **注意**
> - 测试版本最多支持上传 25 个版本。
> - 多测试版本能力只支持抖音、抖音极速版、抖音火山版（>=31.6.0）。如想在其他宿主上测试：
>   - 需要保证默认通道上有上传测试版本。
>   - 无论扫哪个测试通道的二维码，最终都只会打开默认通道上的测试版本，故请将要扫码体验的测试版本上传到默认通道。

### 3. 提交审核：
点击**「提交审核」**，并按要求提供三张游戏内截图。

> **注意**
> 若该版本需要灰度测试，请勿提前勾选自动发布，否则版本审核通过后将自动全量到线上。
> 如因不符合平台入驻要求无法提交审核，可咨询平台客服。平台客服咨询路径：[抖音开放平台-控制台](https://developer.open-douyin.com/console?type=2)-我的应用「小游戏 tab」-右下角「开发者助手」。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/fadc2aaa0d65449bb78335e41d47eacd~tplv-9nona0m7ha-image.image)

### 4. 全量/灰度发布
- 全量发布：点击【立即发布】，该版本将全量至线上全部合作App。
- 灰度发布：点击【灰度发布】，如灰度发布设置弹窗，灰度可覆盖的 App 为当前线上版覆盖的 App，未上线的** **App** **不可进行灰度。
    **灰度期间可调整覆盖 **App** 和灰度比例（只可增加不可减少），灰度满****15****天后将自动全量到线上。**

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/9bc3360bd99445e9afdafa69cc457070~tplv-9nona0m7ha-image.image)

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1668149625833)

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1668149626243)

### 5. 全量/灰度数据
#### **1. 总览数据**
版本发布成功后，可在平台总览页查看线上版本/灰度版本的昨日关键数据。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1668149626188)

#### **2. 用户分析**
- 可通过切换【线上版本】或【灰度版本】tab，查看当前的线上版/灰度版的用户分析数据。
- 【线上版本】的数据包含了【灰度版本】的数据（因为灰度版也在线上），而【灰度版本】中只能查看到灰度版本的数据。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1668149626288)

#### **3. 性能分析**
- 可通过切换【线上版本】或【灰度版本】tab，查看当前的线上版/灰度版的性能分析数据。
- 【线上版本】的数据包含了【灰度版本】的数据（因为灰度版也在线上），而【灰度版本】中只能查看到灰度版本的数据。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1668149626358)