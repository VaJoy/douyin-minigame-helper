---
title: "Touch"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/system/click-event/touch
update_time: 2024-07-24
---

Touch 对象表示在触控设备上的触摸点。通常是指手指或者触控笔在触屏设备或者触摸板上的操作。
---
## 属性
### number identifier
Touch 对象的唯一标识符，只读属性。一次触摸动作(指手指的触摸)在平面上移动的整个过程中, 该标识符不变。
可以根据它来判断跟踪的是否是同一次触摸过程。
### number screenX
触点相对于屏幕左边沿的 X 坐标。
### number screenY
触点相对于屏幕上边沿的 Y 坐标。
