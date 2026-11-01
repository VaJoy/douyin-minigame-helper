---
title: "真机调试"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/game-debug/real-machine-adjust
update_time: 2025-05-13
---

## 功能概述
真机远程调试功能可以实现直接利用开发者工具，通过网络连接，对手机上运行的小游戏进行调试，帮助开发者更好的定位和查找在手机上出现的问题。
## 支持版本
- 目前仅在抖音/抖音极速版 Android 版本 23.8.0 及以上版本支持真机调试功能，iOS调试请确保抖音或抖音极速版版本为27.9.0或以上。**Profiles**面板需要抖音/抖音极速版 Android 版本` 24.4.0 `及以上版本。
- `高性能`和`高性能+`模式不支持真机调试，使用真机调试功能时请先关闭这两种模式，待发布上传之前再打开。
## ** 一、获取调试权限**
#### 背景概述
- 为了更完善管理开发者在真实移动设备上对抖音小游戏的预览/调试行为，从IDE 4.1.5 & 抖音27.3.0 起：
    （1）开发者工具真机调试功能增加了获取调试权限要求，即在预览或真机调试前，需要先获取当前小程序的预览/调试权限，开发者可基于测试成员的角色定位，进行账号绑定和授权。
    （2）游戏协作者的设备必须被添加为游戏的测试管理设备后，才能在真实移动设备上对抖音小游戏进行预览/调试。
- 平台将在2023年10月16日后，将游戏的开发调试权限升级为仅支持配置了权限的开发者才可对抖音小游戏进行开发调试。请所有开发者根据如下指引，提前完成对游戏的开发、运营人员权限配置，避免影响游戏运营。
#### 操作指引
开发者可通过以下两种方式配置调试权限
##### （一）开发者运营平台
非游戏的开发人员，如游戏运营人员的调试权限，可在开发者运营平台的【开发-开发设置-调试管理】模块设置：
点击【添加设备】按钮，拉起二维码弹窗，请该二维码分享给需要被添加为测试人员的人，让对方使用抖音app扫码绑定。请注意：
- 请控制好权限范围，勿将二维码泄漏给无关人员；
- 绑定后，模拟器将使用该抖音号作为用户标识。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/de58b5f0ff3d4ea3a96b05b546345d9d)

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/bd84da70f8dd443da1a2e639c4ea17c0)

##### （二）开发者工具（IDE）
若开发者账号没有绑定过抖音号，则在开发者工具（IDE）中点击【预览】、【真机调试】时，将拉起二维码弹窗绑定「抖音账号」从而获取调试权限，**账号绑定注意事项：**
- 账号绑定为一次性操作，目前绑定成功后暂无法解绑，请勿使用他人抖音号绑定。（后续平台将支持账号合并或解绑，具体信息见平台官方通知）
- 若开发者账号先由邮箱或手机注册获得，后使用抖音号扫码注册了新账号，那么该抖音号无法用于绑定至先前创建的开发者账号，绑定过程中会遇到绑定冲突，此时开发者可以
  - 重新创建一个抖音号进行绑定
  - 使用抖音号注册的开发者账号进行登录
- 若开发者账号由抖音扫码注册创建，则无需绑定抖音号。
- 绑定后，模拟器将使用该抖音号作为用户标识。
- AppID使用“测试号”进行开发时，预览或真机调试前必须绑定抖音号。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/15fc85f4ad4a4760a12c22ec3cc7a62b)

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/b8db7b87e0e440089cc8f1acf560a852)

### 二、发起调试流程** **
发起一个真机远程调试流程，需要先点击开发者工具的工具栏上 “真机调试” 按钮。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1670931161174)

注意：
- 等待二维码生成之后，使用抖音扫码进行调试。
- Android调试请确保抖音或抖音极速版版本为23.8.0或以上。
- iOS调试请确保抖音或抖音极速版版本为27.9.0或以上。
打开开发者工具，点击工具栏上的【真机调试】按钮，默认为**推送调试。**

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1670931475783)

使用抖音扫一扫功能扫二维码，并且在手机上点击确认进行调试。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1670932493957)

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1670932545718)

等待一段时间，抖音 APP 内自动打开小游戏，电脑端自动打开真机调试窗口。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1670932835774)

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1670932974325)

在未绑定手机的前提下，切换到 **扫码调试**。
等待二维码成功展示，使用抖音 APP 的扫一扫功能扫描二维码。 扫码成功后，电脑端自动打开真机调试窗口。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1670933135688)

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1670933236973)

调试器
在远程调试的调试器里，开发者可以在 Console 面板里对代码进行调试，在 Sources 面板里查看小游戏的源代码并进行断点单步调试。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1670933886797)

在 Sources 面板查看源代码。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1670934072382)

除了可以在调试器进行单步调试，开发者还能在代码中手动插入 debugger; 语句进行断点调试。因此，如果想要在小游戏启动的尽早时刻断点，可以在进入远程调试之前，编辑代码手动在需要断点处的代码插入 debugger; 语句来实现。
### 小游戏抖音开发者工具 4.0.4 版本
- 新增：真机调试**Profiles**面板（需要抖音/抖音极速版 Android 版本 **24.4.0 **及以上版本，iOS真机调试暂不支持该功能）。
开发者可以通过这些选项查看并调试小游戏 CPU 和内存等性能，并定位问题所在。
1. **Record JavaScript CPU Profile：**监控函数执行期花费的时间，用于分析小游戏上的JavaScript函数在执行过程中的CPU消耗信息。当开发者遇到时间过长而丢帧的问题，可使用此功能来排查问题。勾选Record Javascript CPU Profile；点击Start，开始录制；结合具体要分析的场景，做一些玩小游戏的操作；点击Stop，结束录制。Chrome DevTools提供了三种不同的查看方式：Chart，Heavy(Bottom Up)和Tree(Top Down)。Chart：按时间顺序展示的火焰图。包含两部分：Overview 总览和Call Stacks调用栈。通常来说，垂直方向并没有太大的意义，仅仅表示函数嵌套比较深而已，但是横向表示调用时间，如果调用时间太长，那么就需要优化优化了。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/screenshot-20230214-184530-1882884845683250.2.png)

1. **Take Heap Snapshot**：可以查看堆快照，进而发现内存泄露问题。选中Take Heap Snapshot，点击开始即可获取快照（它会自动停止），每次获取快照之前都会自动执行垃圾回收操作。快照最初是存储在渲染进程的内存中的，当我们录制的时候才会传输到Chrome DevTools，快照加载进来并解析，我们可以看到其具体信息，每个快照底部的数字就是可达的 js 对象的大小。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/screenshot-20230214-185113-9478700640754600.png)

如果数据传输有问题可以选择勾选“Auto save file on Android device”（设备复制功能），此时可以在安卓手机上生成heapSnapshot文件，开发者可导入到IDE中点击load加载并查看调试数据。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/飞书20230214-185546-607340323549381.2.png)

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/20230214-113547-3697993609009811.jpeg)

1. **Allocation instrumentation on timeline**：持续的记录堆分配的情况，显示了对象在什么时候被创建、什么时候存在内存泄漏等。
1. **Allocation sampling**：内存信息采样，使用采样的方法记录内存分配。此配置文件类型具有最小的性能开销，可用于长时间运行的操作。它提供了由 js 执行堆栈细分的良好近似值分配。
