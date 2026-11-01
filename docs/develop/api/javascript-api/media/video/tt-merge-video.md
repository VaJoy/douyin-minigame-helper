---
title: "tt.mergeVideo"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/video/tt-merge-video
update_time: 2024-08-15
---

## 语法

```js
tt.mergeVideo(videoPaths)
```
基础库 2.58.0 开始支持本方法，这是一个**异步**方法。
将视频进行合并。

## 示例代码
```js
let shareParam = {
  videoPath: "",
};

let task = tt.mergeVideo({
  videoPaths: [videoPath1, videoPath2],
  success(res) {
    tt.showModal({
      title: "合并成功",
      content: JSON.stringify(res),
    });
    shareParam.videoPath = res.videoPath;
  },
  fail(res) {
    tt.showModal({
      title: "合并失败",
      content: JSON.stringify(res),
    });
  },
});

task.onProgressUpdate((res) => {
  console.log("progress: " + res.progress);
  tt.showToast({
    title: JSON.stringify(res.progress),
  });
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| videoPaths | Array<string> | 是 |  | 2.58.0 | 视频的文件路径，支持ttfile和相对路径；至少2个元素，按照顺序合并 |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| （返回值） | Object | object 对象，属性如下：  **对象字段** - **onProgressUpdate**（Function）：进度更新回调函数， 入参类型是 { progress: number }，表示合并操作的进度 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **videoDuration**（number）：合并后的视频时长，单位毫秒 - **videoPath**（string）：合并后的视频ttfile路径 - **errMsg**（string）："mergeVideo:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："mergeVideo:fail" + 详细错误信息 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
