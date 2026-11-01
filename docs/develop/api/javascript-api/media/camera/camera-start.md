---
title: "Camera.start"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/camera/camera-start
update_time: 2025-05-19
---

Camera.start(face, beautify, option)

const camera = tt.createCamera();
camera.start("front", true, { gesture: true }).then((video) => {
// option传入gesture:true开启手势识别
console.log(video); // 摄像头返回的视频
video.focus();
});

## 语法

```js
Camera.start(face, beautify, option)
```
基础库 1.40.0 开始支持本方法，这是一个**同步**方法。
启动摄像头，该方式返回一个 Promise 对象，是个异步方法。

## 示例代码
```js
const camera = tt.createCamera();
camera.start("front", true, { gesture: true }).then((video) => {
  // option传入gesture:true开启手势识别
  console.log(video); // 摄像头返回的视频
  video.focus();
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| face | string | 是 |  | 1.40.0 | 摄像头方向，取值为 "front" 或者 "back"，默认开启前置摄像头 |
| beautify | boolean | 是 |  | 1.40.0 | 开启摄像头美颜， false 表示不开启 |
| option | Object | 否 |  | 1.40.0 | 摄像头可选参数  **对象字段** - **gesture**（boolean）：是否开启手势识别能力 |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| Promise | Promise | Promise对象，resolve 时可获取video 实例 |

## 注意事项
- 只有开启摄像头美白， 调用接口Camera.setBeautifyParam才能设置美白参数。
- 只有开启摄像头美白， 才能进行人脸检测。
- 对于摄像头开启后模糊，可以对摄像头 start 后返回的视频调用 focus 方法，参考代码示例。
- 上面代码示例中，摄像头开启后返回的 video 对象指向的是摄像头的实时数据，内部会实时更新 video 对象指向的数据。
- 开发者工具暂不支持美颜和手势识别能力，请用真机扫码调试。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
