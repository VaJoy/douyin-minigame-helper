---
title: "Unity Webgl 模拟器"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/development-assistance/unity-webgl-simulator
update_time: 2024-09-24
---

Unity Webgl 项目通过编译之后，将 zip 产物传入 IDE 可在模拟器中运行，模拟小游戏在字节系 App 客户端的表现，无需真机即可快速预览。基础互动方式是通过鼠标点击、拖拽来模拟手指触摸、拖动操作。
**注：**
  - **IDE 只支持 webgl 方案，不支持 Android Native 和 Instant Game 方案。**
  - **IDE 4.3.0 及以上版本支持 unity webgl 模拟器**

首次进入，模拟器默认位于主界面左侧：

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/095f4cb6a0a74bd0912c5462faab7fa2)

## 如何使用模拟器
1. 在 StarkSDK Unity 调试工具中生成 webgl 产物后，点击使用开发者打开按钮。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/bff9c63798384713b33f22933e1b6727)

1. 点击按钮后 IDE 自动导入项目并打开工程：

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/aae8c3a1c3c6468b9c51cb3d4ade25c1)

1. 当导入IDE后，若新构建 webgl 产物，则需要点击右上方详情按钮并选择 webgl 产物。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/e79bc3c4a25f4a8099ddba449fb0e080)

## 模拟器顶部功能
•**机型**：开发者可以选择不同的设备来调试小游戏，以观察小游戏在不同尺寸机型上的适配问题。
•**缩放比例**：开发者可以控制模拟屏幕的显示比例。
•**屏幕高度**：开发者可以切换分屏模式调试小游戏直播场景。
•**抖音登录**：开发者通过抖音扫码登录，在游戏序拿到真实抖音用户信息。
•**模拟工具**：模拟手机的部分操作，用以触发特定事件。目前只支持静音操作。
•**布局切换**：该功能可以将模拟器的位置与编辑器、调试器进行左右切换。
### 设备皮肤
在模拟器中，IDE 提供了常见设备皮肤（iOS/Android）供开发者直观调试小游戏在不同机型上的效果，开发者可以通过模拟器顶部菜单栏上的设备列表进行切换。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/29b56e8f5d4e4c79aad20bb15fb7c023)

### 自定义设备
除了固定的设备外，开发者可以选择不同的设备，也可以选择自定义设备，拖动模拟器来调试小游戏在不同尺寸机型上的适配问题。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/2011674db7d548beabd8ab8f04ab624c)

### **抖音测试账号登录**
从 IDE 4.3.0 版本起，模拟器支持使用抖音扫码绑定测试账号。扫码绑定后，模拟器中依赖用户身份的开放能力。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/be30b5ad29d1431b9fe8bf274d985248)

操作方法：
点击头像区域触发登录二维码，使用抖音 App 扫码登录。

![screenshot](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e7881db8193b46c7b8063238cf24ee8a~tplv-goo7wpa0wc-image.image)

登录后，头像区域展示抖音头像。

![screenshot](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/9eff27ba3cee4c2cbf5c4c78d380c905~tplv-goo7wpa0wc-image.image)

登录后再次点击头像区域，可以退出登录。

![screenshot](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/338626a6b1774634b6b0c8dddf92f3ba~tplv-goo7wpa0wc-image.image)

此外，在模拟器未登录的情况下，若用户使用抖音扫码登录 IDE，模拟器将自动绑定该抖音用户。此时用户如需更改模拟器绑定的抖音用户，可以手动退出登录后，重新使用其他抖音账号扫码绑定。
## IDE 工具栏
- 编译：编译模拟器需要加载的 webgl 项目（webgl 产物地址需要在`详情-工程配置`中设置）。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/e79bc3c4a25f4a8099ddba449fb0e080)

- 刷新页面：刷新当前页面。
- 清除缓存：可以清除文件缓存、数据缓存、登录状态和授权数据。
- 上传：填入 app 版本号及更新日志，上传小游戏应用内容到服务器（Unity 方案类型、相关方案对应的产物、屏幕方向和胶囊按钮颜色等需要在`详情-工程配置`中设置）。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/c3d40f42ff314136a489bb9b0d1840ab)

- 预览：生成二维码，预览已上传版本（Unity 方案类型、相关方案对应的产物、屏幕方向和胶囊按钮颜色等需要在`详情-工程配置`中设置）。
- 详情：展示当前小游戏的 appid、user_id、本地目录、文件系统、基础版本版本，并可以配置 Unity 方案类型、选择相关方案对应的产物、屏幕方向和胶囊按钮颜色等。
- 💡 点击「模拟器」、「调试器」三个按钮可以隐藏/显示相应的模块，界面中至少有一个模块被显示。
