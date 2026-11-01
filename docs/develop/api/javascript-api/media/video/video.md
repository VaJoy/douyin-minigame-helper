---
title: "Video"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/video/video
update_time: 2024-08-22
---

Video 是描述视频资源的对象。离屏 Video 对象可以通过接口 tt.createOffscreenVideo 创建，上屏 Video 对象可通过接口 tt.createVideo 创建。可以通过设置该对象上的属性、调用该对象上的方法来控制视频。
## 实例属性

| 属性 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| src | string | 空字符串 | 视频资源地址 |
| volume | number | 1 | 播放音量 （值范围为 0 ～ 1） |
| muted | bool | false | 是否静音（true 为静音） |
| loop | bool | false | 是否循环播放（true 为循环播放） |
| autoplay | bool | false | 是否自动播放（true 为自动播放） |
| width | number | 0 | 期望视频宽度（单位：像素） |
| height | number | 0 | 期望视频高度（单位：像素） |
| currentTime | number | 0 | 视频当前播放到的时长（单位：s） |
| duration | number | readonly | 视频总时长（单位：s） |

## 方法
### Video.play()
播放视频。
### Video.pause()
暂停视频。
### Video.stop()
停止视频。
### Video.seek(number time)
跳转到视频指定位置。

| 属性名 | 类型 | 取值 |
| --- | --- | --- |
| time | number | 单位：秒，超出视频总时长则视频停止在当前帧，小于 0 无效 |

### Video.destroy()
销毁视频。
### Video.paintTo(canvas, dx, dy, sx, sy, sw, sh)
将当前视频内容绘制到指定 canvas。

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| canvas | object | 作为绘制目标的 canvas 对象 |
| dx | number | 绘制目标的 x 坐标偏移（单位：像素） |
| dy | number | 绘制目标的 y 坐标偏移（单位：像素） |
| sx | number | 绘制源的 x 坐标偏移（单位：像素） |
| sy | number | 绘制源的 y 坐标偏移（单位：像素） |
| sw | number | 绘制源的宽度（单位：像素） |
| sh | number | 绘制源的高度（单位：像素） |

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/2021325-214013-9701646766695202.png)

**说明：**
蓝色区域：代表整个 canvas 的大小，一般是整个游戏的渲染区域。
深绿色区域（标注 sx，sy 部分）：代表视频本身的内容区域。
浅绿色区域（标注 sw，sh 部分）：代表视频最终渲染到 Canvas 上的内容。
### Video.onCanplay(function callback(scale))
监听视频进入可以播放的事件，回调函数的参数 scale 为 video 对象的宽度和高度之比。

| 属性名 | 类型 | 取值 |
| --- | --- | --- |
| scale | number | video.videoWidth / video.videoHeight |

### Video.onCandraw(function callback(scale))
> 基础库版本 1.9.6 开始支持。
监听视频首帧事件，回调函数的参数 scale 为 video 对象的宽度和高度之比。

| 属性名 | 类型 | 取值 |
| --- | --- | --- |
| scale | number | video.videoWidth / video.videoHeight |

### Video.onPlay(function callback)
监听播放视频事件。
### Video.onPause(function callback)
监听暂停视频事件。
### Video.onStop(function callback)
监听停止播放视频事件。
### Video.onEnded(function callback)
监听视频自然播放至结束的事件。
### Video.onError(function callback(errorMessage))
监听视频播放错误事件，回调函数的参数为错误信息文本。

| 属性名 | 类型 | 取值 |
| --- | --- | --- |
| errorMessage | string |  |

### Video.onTimeUpdate(function callback(object))
监听视频跳转事件，回调函数的参数为 Object 类型，具体字段如下：

| 属性名 | 类型 | 取值 |
| --- | --- | --- |
| position | number | 视频当前播放到的时长（单位：s） |
| duration | number | 视频总时长（单位：s） |

### Video.offCanplay(function callback)
取消监听视频可以播放事件。
### Video.offPlay(function callback)
取消监听视频播放事件。
### Video.offPause(function callback)
取消监听视频暂停事件。
### Video.offStop(function callback)
取消监听视频停止事件。
### Video.offEnded(function callback)
取消监听视频自然播放至结束事件。
### Video.offError(function callback)
取消监听播放视频错误事件。
## Bug & Tip
- Tip： 取消监听事件的传入参数为对应监听函数的参数，才能取消对应的监听函数。
- Tip： 为了方便开发者理解，Video 是参照 HTML5 Video 对象实现的。
- Bug: 开发者通过 onCanplay 事件监听视频开始播放的事件进行视频内容渲染时，在部分机型上会出现首帧黑屏的情况。针对这种情况，建议开发者监听 onCandraw 事件，通过此事件能够保证绘制出来的首帧不会出现黑屏。
