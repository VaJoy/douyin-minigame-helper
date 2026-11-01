---
title: "自定义编译条件"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/code-compile/custom-compile-cond
update_time: 2025-06-13
---

为了帮助开发者调试从不同场景值进入具体的页面，开发者可以在工具栏中点击【普通编译】选择【添加编译模式】自定义编译条件进行编译。在自定义编译条件页面，开发者可以配置启动页页面路径，启动参数和进入场景等参数。
已有的自定义编译条件会记录在 project.config.json 中，开发者可以将其托管于工具内部处理。
> 注：编译模式跟项目相关，每个项目可以保存自己相关的编译模式。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/e827836e1016446982f9f1a2038c7092~tplv-9nona0m7ha-image.image)

自定义编译模式弹窗：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/d3bd03bee6804621be0b04739d7fa348~tplv-9nona0m7ha-image.image)

## 模拟小游戏更新
在进行自定义编译模式设置时，还可以选择模拟更新类型，模拟器会根据不同编译模式对应的模拟更新类型，模拟小游戏更新情况，触发对应的接口，小游戏更新接口参考：[tt.getUpdateManager](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/update/tt-get-update-manager)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/f0b216f463384edd9d2e93dcac6fad1e~tplv-9nona0m7ha-image.image)
