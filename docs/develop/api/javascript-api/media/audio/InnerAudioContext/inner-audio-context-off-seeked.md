---
title: "InnerAudioContext.offSeeked"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/InnerAudioContext/inner-audio-context-off-seeked
update_time: 2024-10-23
---

## 语法

```js
InnerAudioContext.offSeeked(callback)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
取消监听音频完成 [seek](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/api/media/audio/inner-audio-context/inner-audio-context-seek/) 操作的事件。

## 示例代码
```js
const dataUrl = "https://someaudiourl"; // 合法的音频资源地址

const innerAudioContext = tt.createInnerAudioContext();
innerAudioContext.autoplay = true;
innerAudioContext.src = dataUrl;

innerAudioContext.onError((error) => {
  tt.showToast({ title: "音频播放失败" });
});

function onseeked() {
  tt.showToast({ title: "跳转完成" });
}
innerAudioContext.onSeeked(onseeked);
innerAudioContext.offSeeked(onseeked);

setTimeout(() => innerAudioContext.seek(3), 1000);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.0.0 | 取消回调的方法 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/inner-audio-context-off-seeked) / [本地体验路径](inner-audio-context-off-seeked)
