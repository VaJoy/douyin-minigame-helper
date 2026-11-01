---
title: "GameRecorderManager.start"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/screen-recording/game-recorder-manager/game-recorder-manager-start
update_time: 2024-11-11
---

## 语法

```js
GameRecorderManager.start(options)
```
基础库 1.4.1 开始支持本方法，这是一个**同步**方法。
开始录屏。可以通过 [onStart](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/screen-recording/game-recorder-manager/game-recorder-manager-on-start) 接口监听录屏开始事件。

## 示例代码
```js
tt.getSystemInfo({
  success(res) {
    const screenWidth = res.screenWidth;
    const screenHeight = res.screenHeight;
    const recorder = tt.getGameRecorderManager();
    var maskInfo = recorder.getMark();
    var x = (screenWidth - maskInfo.markWidth) / 2;
    var y = (screenHeight - maskInfo.markHeight) / 2;

    recorder.onStart((res) => {
      console.log("录屏开始");
      // do something;
    });
    //添加水印并且居中处理
    recorder.start({
      duration: 30,
      isMarkOpen: true,
      locLeft: x,
      locTop: y,
    });
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| options | Object | 否 |  | 1.4.1 | object 类型，参数如下：  **对象字段** - **duration**（number）：录屏的时长，单位 s，必须大于 3s，最大值 300s（5 分钟）。 - **isMarkOpen**（boolean）：是否添加水印，会在录制出来的视频上添加默认水印，目前不支持自定义水印图案。 - **locTop**（number）：水印距离屏幕上边界的位置，单位为 dp。 - **locLeft**（number）：水印距离屏幕左边界的位置，单位为 dp。 - **frameRate**（number）：设置录屏帧率（仅安卓系统支持），对于性能较差的手机可以调低参数以降低录屏性能消耗。 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 10401 | activity is null |  |  |
| 21103 | record is start |  |  |
| 21104 | record not ready |  |  |
| 10208 | no permission to record screen |  |  |
| 21102 | video file path illegal |  |  |
| 10402 | App can not call recorder |  |  |
| 20000 | param:recordable is false |  |  |
| 21000 | failed to start recorder |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/game-recorder-manager-start) / [本地体验路径](game-recorder-manager-start)
