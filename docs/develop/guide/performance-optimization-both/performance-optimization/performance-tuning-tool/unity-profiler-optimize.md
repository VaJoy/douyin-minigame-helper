---
title: "使用 Unity Profiler 进行性能调优"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/performance-optimization/performance-tuning-tool/unity-profiler-optimize
update_time: 2025-08-25
---

## 使用背景
  当小游戏在移动端运行过程中产生卡顿、发热或帧率低等情况时，可以使用此文档提供的方法，进行真机运行时的性能数据收集，方便定位性能瓶颈，进行性能优化。
## 操作流程
1. 在导出小游戏时勾选`Development`与`Connect with Profiler`

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/40600ace4a264d829b5f568e57c59844~tplv-9nona0m7ha-image.image)

1. 通过「Window」-「Analysis」-「Profiler」打开 Profiler 调试窗口
打开调试窗口后，Unity 会自动监听端口，等待调试连接。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/f1b72842161b4f1bb83860293502177f~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/4a824a0e3110410fbcd75e7b3de7170e~tplv-9nona0m7ha-image.image)

1. 当在开发者工具模拟器/真机中运行小游戏后，调试器会自动连接。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/9c0df1b236f444399f8597d2cbe5fe8c~tplv-9nona0m7ha-image.image)

## 调整 Unity Profiler IP/端口
小游戏启动后将自动通过`ws://ip:port`自动连接到 Unity Profiler，`ip`默认为编译打包机器的 IP 地址。如需修改 IP 地址，可通过修改`game.js`中的对应 IP：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/b85f115294fb45f69756fea6945faff1~tplv-9nona0m7ha-image.image)

## 注意事项
1. 并非每个 Unity 版本都能稳定连接 Profiler，如果发现无法正常连接的情况请尝试更换小版本；
1. 当小游戏无法连接 Unity Profiler 时，请检查 Unity Profiler 是否已启动监听，且IP/端口可达。通常使用"BuildSetting"-"Build And Run"在浏览器中运行产物时，UnityProfiler会默认启动监听。如果还是无法连接，可以尝试在要监听 Profiler 的电脑上执行下面的命令来手动启动监听：

```bash
# UnityEditor 为 Unity 编辑器安装路径，port 为监听端口
node ${UnityEditor}/PlaybackEngines/WebGLSupport/BuildTools/websockify/websockify.js 0.0.0.0:${port} localhost:${port}
```

## 附录
- Profiler窗口使用说明 [https://docs.unity3d.com/cn/2021.3/Manual/ProfilerWindow.html](https://docs.unity3d.com/cn/2021.3/Manual/ProfilerWindow.html)
