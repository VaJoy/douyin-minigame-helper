---
title: "Camera"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/camera/camera
update_time: 2024-07-24
---

摄像头对象实例
## 方法
**Camera.start(string face, bool beautify, Object option)**
启动摄像头
**Camera.pause()**
暂停摄像头录制
**Camera.resume()**
恢复摄像头录制
**Camera.destroy()**
销毁摄像头
**Camera.setBeautifyParam(number whiten, number smoothen, number enlargeEye, number slimFace)**
设置摄像头美化参数
## Bug&Tip
- 当退出游戏，或者摄像头不再使用，谨记调用 destroy 方法释放摄像头。
