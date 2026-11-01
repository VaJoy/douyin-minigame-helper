---
title: "RecorderManager.start"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/record/recorder-manager/recorder-manager-start
update_time: 2024-12-10
---

## 语法

```js
RecorderManager.start(params)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
开始录音。

## 示例代码

【代码示例1】：无输入参数。

预期表现：正常启动录音，录音时长等参数为默认值。

```js
const recorderManager = tt.getRecorderManager();
recorderManager.start(); // 所有参数为默认值
tt.showToast({ title: "点击了开始录音，参数为默认值" });
```

【代码示例2】：不设置 frameSize 参数示例

预期表现：正常启动录音，无 onFrameRecorded 回调。

```js
const recorderManager = tt.getRecorderManager();
const options = {
  duration: 1000,
  sampleRate: 12000,
  numberOfChannels: 1,
  encodeBitRate: 25000,
  frameSize: 100,
};
recorderManager.start(options);
tt.showToast({ title: "点击了开始录音" });
```

【代码示例 3】：设置 frameSize 示例

预期表现：正常启动录音，达到指定帧大小后在 onFrameRecorded 回调中输出帧数据，若指定帧大小大于整条语音，则在最后一帧输出，可根据 isLastFrame 判断是否是最后一帧。

```js
const recorderManager = tt.getRecorderManager();
const options = {
  duration: 60000,
  sampleRate: 12000,
  numberOfChannels: 1,
  encodeBitRate: 25000,
  frameSize: 100,
};
recorderManager.start(options);
tt.showToast({ title: "点击了开始录音" });
recorderManager.onFrameRecorded((frame) => {
  if (frame.isLastFrame) {
    tt.showToast({ title: "录音结束" });
  }
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| params | Object | 否 |  | 1.0.0 | object 类型，属性如下：  **对象字段** - **duration**（number）：录音自动完成时长，单位 ms。取值在[0, 600000]，不在这个范围里的值会被重置为 600000 - **format**（number）：格式 - **sampleRate**（number）：采样率 - **numberOfChannels**（number）：录音通道数 - **encodeBitRate**（number）：码率 - **frameSize**（number）：帧大小，单位 KB。如果设置了值，那么每当录音内容达到帧大小时会通过 [RecorderManager.onFrameRecorded](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/record/recorder-manager/recorder-manager-on-frame-recorded) 返回内容 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | Operation type is null |  |  |
| 21000 | Operation type is error |  |  |
| 21501 | invalid encodeBitRate ${encodeBitRate} , encodeBitRate should be greater than ${minRate} and less than ${maxRate} |  |  |
| 20000 | internal error |  |  |

## 使用限制
android 仅支持 wav 格式，iOS 仅支持 aac 格式

## 用户授权说明
该方法需要用户授权方可调用，详细信息可参考[用户授权](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/api/other/user-authorization/)。

## 授权要求
无需开发者授权；需要用户授权

## 支持平台
iOS、Android