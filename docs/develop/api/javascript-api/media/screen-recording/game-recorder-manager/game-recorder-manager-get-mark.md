---
title: "GameRecorderManager.getMark"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/screen-recording/game-recorder-manager/game-recorder-manager-get-mark
update_time: 2024-11-11
---

基础库 1.69.0 开始支持本方法，这是一个**同步**方法。
获取录屏水印宽高。开发者可以通过宽高计算水印添加的位置。

## 示例代码
```js
tt.getSystemInfo({
  success(res) {
    const screenWidth = res.screenWidth;
    const screenHeight = res.screenHeight;
    const recorder = tt.getGameRecorderManager();
    var maskInfo = recorder.getMark(); //获取水印的宽高
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

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| maskInfo | Object | 水印的宽高信息  **对象字段** - **markWidth**（number）：水印的宽度 - **markHeight**（number）：水印的高度 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
