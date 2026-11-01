---
title: "游戏交互"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/basic-function/game-interaction
update_time: 2025-08-27
---

## 基础交互方式
游戏开发中常用的交互方式包括点击、拖动、长按等操作。完整的设备交互API请参考[API-设备](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device)

#### 触摸事件
抖音小游戏提供了以下基础触摸事件监听接口
- 监听开始触摸事件[tt.onTouchStart](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/system/click-event/tt-on-touch-start)
- 监听触点移动事件[tt.onTouchMove](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/system/click-event/tt-on-touch-move)
- 监听触摸结束事件[tt.onTouchEnd](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/system/click-event/tt-on-touch-end)
- 监听触点失效事件[tt.onTouchCancel](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/system/click-event/tt-on-touch-cancel)

#### 文本输入
> 适用于游戏内文字输入场景，如账号登录、聊天等

- 显示文字输入键盘[tt.showKeyboard](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/interface/keyboard/tt-show-keyboard)
- 隐藏文字输入键盘[tt.hideKeyboard](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/interface/keyboard/tt-hide-keyboard)
- 监听键盘输入事件[tt.onKeyboardInput](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/interface/keyboard/tt-on-keyboard-input)
- 监听用户点击键盘 Confirm 按钮时的事件[tt.onKeyboardConfirm](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/interface/keyboard/tt-on-keyboard-confirm)
- 监听键盘收起的事件[tt.onKeyboardComplete](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/interface/keyboard/tt-on-keyboard-complete)

#### 设备-鼠标（仅适用于 PC 平台）

> 虽然鼠标事件会自动转换为触摸事件，但为获得更好的PC端体验，建议单独适配：

- 监听鼠标按键按下事件  [tt.onMouseDown](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/mouse/tt-mouse-down)
- 监听鼠标移动事件 [tt.onMouseMove](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/mouse/tt-on-mouse-move)
- 解除鼠标按键弹起事件监听 [tt.offMouseUp](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/mouse/tt-off-mouse-up)
- 解除鼠标按键按下事件监听 [tt.offMouseDown](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/mouse/tt-off-mouse-down)

### 设备-滚轮(仅适用于 PC 平台)

> 监听鼠标滚轮事件，仅适用于 PC 平台。

监听鼠标滚轮事件[tt.onWheel](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/wheel/tt-on-wheel)
取消监听鼠标滚轮[tt.offWheel](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/wheel/tt-off-wheel)

### 设备-键盘(仅适用于 PC 平台)

> 适用于Windows直播伴侣主播场景，基础库版本3.54.0+，更多 PC 适配查看[PC 小游戏接入指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/tutorial)。

- 监听键盘按键按下事件[tt.onKeyDown](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/keyboard/tt-key-down)
- 移除键盘按键弹起事件监听[tt.offKeyUp](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/keyboard/tt-off-key-up)
#### WebGL键盘输入法适配
详见[键盘输入法适配](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc_webgl_keyboard)

const deviceMotionData = { alpha: 0, beta: 0, gamma: 0 };
const accelerometerData = { x: 0, y: 0, z: 0 };
const gyroscopeData = { x: 0, y: 0, z: 0 };
const compassData = { direction: 0, accuracy: 0 };

// 启动设备运动监听
wx.startDeviceMotionListening({
success: () => {
wx.onDeviceMotionChange(res => {
deviceMotionData = res;
});
},
fail: err => {
console.error("Failed to start device motion listening:", err);
}
});

// 启动加速计
wx.startAccelerometer({
success: () => {
wx.onAccelerometerChange(res => {
accelerometerData = res;
});
},
fail: err => {
console.error("Failed to start accelerometer:", err);
}
});

// 启动陀螺仪
wx.startGyroscope({
success: () => {
wx.onGyroscopeChange(res => {
gyroscopeData = res;
});
},
fail: err => {
console.error("Failed to start gyroscope:", err);
}
});

// 启动罗盘
wx.startCompass({
success: () => {
wx.onCompassChange(res => {
compassData = res;
});
},
fail: err => {
console.error("Failed to start compass:", err);
}
});
