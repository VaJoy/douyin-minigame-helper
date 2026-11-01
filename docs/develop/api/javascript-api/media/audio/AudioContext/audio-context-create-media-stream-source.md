---
title: "AudioContext.createMediaStreamSource"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/audio-context-create-media-stream-source
update_time: 2024-09-19
---

## 语法

```js
AudioContext.createMediaStreamSource(steamId)
```
基础库 1.34.0 开始支持本方法，这是一个**同步**方法。
创建并返回一个新的 [MediaStreamAudioSourceNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-buffer-source-node) 对象节点，是作为音频源运行，该节点的输入源目前只能是来自于麦克风。

## 示例代码
```js
async function main() {
  const streamID = await tt.requestMicrophone();
  const context = tt.getAudioContext();
  const sourceNode = context.createMediaStreamSource(streamID);
  sourceNode.isSampleSource = true; //设置该参数，可以在录屏时带上麦克风声音源

  /**
   * 检测音量以确认麦克风确实起效了
   */
  const volumeDetectionNode = context.createVolumeDetection();
  sourceNode.connect(volumeDetectionNode);
  volumeDetectionNode.connect(context.destination);

  setInterval(() => {
    const { size, data } = volumeDetectionNode.getVolumeDetectionData();
    const averageVolume =
      data.reduce((prev, volume) => prev + volume, 0) / size;
    console.log(`[API: microphone] average volumn: ${averageVolume}`);
  }, 2000);
}
main();

/* 
  输出：
  [API: microphone] average volumn: 0.000010016467299465149
  [API: microphone] average volumn: 0.000004972311089659343
  ...
*/
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| steamId | number | 是 |  | 1.34.0 | 创建麦克风获取到的流 id |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| MediaStreamAudioSourceNode | Object | [MediaStreamAudioSourceNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/media-stream-audio-source-node) 对象实例 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
