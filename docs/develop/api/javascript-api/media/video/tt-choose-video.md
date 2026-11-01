---
title: "tt.chooseVideo"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/video/tt-choose-video
update_time: 2024-08-15
---

## 语法

```js
tt.chooseVideo(sourceType, camera, compressed, maxDuration)
```
基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
从系统相册中选择视频，或使用相机拍摄视频，返回视频的临时文件路径。

## 示例代码
```js
tt.chooseVideo({
  sourceType: ["album", "camera"],
  compressed: true,
  success: (res) => {
    let { duration, width, height, size } = res;
    this.setData({
      videoSrc: res.tempFilePath,
      description: `视频时长：${duration}s; 视频宽度：${width}px; 视频高度：${height}px; 视频大小：${size}B`,
    });
  },
  fail: (err) => {
    let errType = err.errMsg.includes("chooseVideo:fail cancel")
      ? "取消选择"
      : "选择失败";
    tt.showModal({
      title: errType,
      content: err.errMsg,
      showCancel: false,
    });
  },
  complete: (res) => {
    console.log("完成选择");
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| sourceType | Array<string> | 否 | ["album", "camera"] | 1.0.0 | 指定视频来源为相册(album)或相机(camera) ，默认两者都有 |
| camera | string | 否 | "back" | 1.0.0 | 'front' 使用前置摄像头，'back' 使用后置摄像头，默认拉起的是后置摄像头。Android 暂不支持拉起前置摄像头 |
| compressed | boolean | 否 | true | 1.0.0 | 是否需要压缩视频源文件，默认值为 true，需要压缩 |
| maxDuration | number | 否 | 60 | 1.0.0 | 选择视频的最大时长（单位：s），取值范围(0, 180]，maxDuration <= 0 时取值 60, maxDuration > 180 时取值 180，在取值范围内为传入值 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **width**（number）：选定视频的视频宽度（单位：px） - **height**（number）：选定视频的高度（单位：px） - **tempFilePath**（string）：选定视频的临时文件路径 - **duration**（number）：选定视频的时间长度 (单位：s) - **size**（number）：选定视频的数据量大小（单位：B） - **errMsg**（string）："chooseVideo:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："chooseVideo:fail" + 详细错误信息。   回调失败的触发时机有：取消选择、参数错误、没有授权/授权失败、视频时长超过 60 秒、文件路径为空、文件路径不存在。 |

## 注意事项
- 手动取消也会触发失败回调，回调参数为 chooseVideo:fail cancel，可以通过判断详细错误信息区分取消和其他错误。
- iOS 无论 compressed 传入 true 或者 false, 都会压缩处理。
- 安卓无论 compressed 传入 true 或者 false, 都不会压缩。

## 前置条件
该 API 需要用户授权方可调用，详细信息可参考[用户授权](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/user-information/authorization/authorization)。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/foundation/tt-choose-video) / [本地体验路径](tt-choose-video)
