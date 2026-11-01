---
title: "音频"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/basic-function/audio
update_time: 2025-08-20
---

## 音频简介
在抖音小游戏开发中,InnerAudio 和 createAudio 是两种不同层级的音频控制方案

### 音频方案对比

| **对比维度** | `createInnerAudioContext` | `AudioContext.createAudio` |
| --- | --- | --- |
| **所属体系** | 抖音小游戏封装的高层API | Web Audio API 或引擎底层 API（如 Unity 引擎） |
| **设计目标** | 快速实现基础音频播放（BGM、音效） | 精细控制音频流（专业游戏/音频可视化） |
| **适用场景** | 简单小游戏、 | 需要音频处理、混音、3D音效的复杂项目 |

### InnerAudio
创建：[tt.createInnerAudioContext](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/tt-create-inner-audio-context)
播放：[InnerAudioContext.play](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-play)
实例属性:[InnerAudioContext](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context/)
#### 示例代码

```text
// 创建音频源
const innerAudioContext = tt.createInnerAudioContext();

// 配置音频源（支持网络URL或本地路径，确保域名已配置合法）
innerAudioContext.src = 'https://xxxx.com/audio.mp3' // 替换为实际音频地址

// 设置循环播放（默认为false）
innerAudioContext.loop = true;

//监听音频进入可以播放状态，但不保证后面可以流畅播放。
innerAudioContext.onCanplay(() => {
  console.log('音频已加载完成，可以播放');
  innerAudioContext.play(); // 手动触发播放（autoplay在部分场景可能被拦截）
});

// 监听播放开始事件
innerAudioContext.onPlay(() => {
  console.log('音频开始播放');
});

// 监听播放结束事件（非循环模式下触发）
innerAudioContext.onEnded(() => {
  console.log('音频播放结束');
});

// 监听音频播放错误事件。
innerAudioContext.onError((err) => {
  console.error('音频播放错误:', err.errMsg, '错误码:', err.errCode);
  // 常见错误码：
  // 10001 - 网络错误
  // 10002 - 解码失败
  // 10003 - 格式不支持
});

// 监听停止事件（调用stop()时触发）
innerAudioContext.onStop(() => {
  console.log('音频已停止');
});

// === 控制方法 ===
// 开始播放（需用户交互触发，如按钮点击）
function startAudio() {
  innerAudioContext.play();
}

// 暂停播放（保留进度）
function pauseAudio() {
  innerAudioContext.pause();
}

// 停止播放（重置进度到0）
function stopAudio() {
  innerAudioContext.stop();
}

// 跳转到指定时间（单位：秒）
function seekAudio(time) {
  innerAudioContext.seek(time);
}

// 销毁实例（释放内存）
function destroyAudio() {
  innerAudioContext.destroy();
}

// 小游戏切换到前台时恢复播放
tt.onShow(() => {
  if (!innerAudioContext.paused) {
    innerAudioContext.play();
  }
});

// 小游戏切换到后台时暂停（避免耗电）
tt.onHide(() => {
  if (!innerAudioContext.paused) {
    innerAudioContext.pause();
  }
});
```

#### 支持的格式
不同音频格式在iOS和Android会有差异

| 格式 | iOS | Android |
| --- | --- | --- |
| mp4 | √ | √ |
| mp3 | √ | √ |
| aac | √ | √ |
| wav | √ | √ |
| m4a | √ | √ |
| ogg | X | √ |

#### 常见问题
[常见问题解疑](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/component/media-component/video#dc734499)

##### 复用已有的音频实例
对于相同的音效，应该复用已有的音频实例，而不是重新创建一个音频实例。
##### 及时销毁不需要的音频实例
如果一个音频不再需要使用了，可以调用[InnerAudioContext.destroy](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-destroy) 接口提前销毁这个实例。
##### 同时播放的音频数量限制
由于系统限制，在 Android 上最多同时播放 10 个音频，超过的部分会做有损处理，开发者无感知，但开发者应尽量避免同时播放过多音频。
##### 实际格式与后缀不符
播放文件应与实际文件封装格式相同
### WebAudio
> 小游戏是基于字节跳动小游戏引擎运行，该引擎支持标准的 Web Audio API，但需要注意平台的特性和限制。由于 Unity 在 WebGL 平台音频实现与原生平台存在较大差异，其本身仅支持有限的音频功能，这些限制也存在于小游戏 WebGL 环境中

WebAudio的开发调用方式和其他JavaScript环境基本是相同的，建议直接查阅[Web_Audio_API](https://developer.mozilla.org/zh-CN/docs/Web/API/Web_Audio_API)进行学习
#### 示例代码

```js
// 创建一个 AudioContext 和 Audio
const ctx = tt.getAudioContext();
const audio = ctx.createAudio();
// 需要先设置event监听 再设置src 确保时序正确
audio.oncanplay = () => {
  console.log("canplay called");
  audio.play();
};
audio.onplaying = () => {
  console.log("playing called");
};
audio.loop = true;
audio.startTime = 0;
audio.autoplay = true;
audio.src = "xxxx.mp3";
// 使用createMediaElementSource 从Audio对象创建一个音频源
const source = ctx.createMediaElementSource(audio);
source.connect(ctx.destination);
audio.onseeking = () => {
  console.log("seeking called");
};
audio.onwaiting = () => {
  console.log("waiting called");
};
audio.onseeked = () => {
  console.log("seeked called");
};
audio.onpause = () => {
  console.log("pause called");
};
audio.onended = () => {
  console.log("ended called");
};
audio.onstop = () => {
  // 跟 web 不同的事件
  console.log("stop called");
};
audio.onerror = (err) => {
  console.log("error called" + err.errMsg);
};
```

#### 常见问题
##### **音频资源加载失败**
  域名未加入抖音白名单，会导致访问不到资源，如放在包内则不做限制，可直接访问
  
### 低版本兼容
详见[低版本兼容](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/runtime/client-lib/compatibility)
### WebGL适配
[关于音频适配以及相关限制](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc-webgl-audio)

const innerAudioContext = wx.createInnerAudioContext({
useWebAudioImplement: false // 是否使用 WebAudio 作为底层音频驱动，默认关闭
});
innerAudioContext.src = 'https://wx_test.mp3'; // 需要自行替换链接
innerAudioContext.loop = true; // 设置循环播放
// innerAudioContext.autoplay = true; // 当可以播放时自动开始播放
innerAudioContext.onError(res => {
console.log('异常', res);
});
innerAudioContext.onPlay(() => {
console.log('开始播放')
});
innerAudioContext.onCanplay(() => {
console.log('可以播放了')
innerAudioContext.play(); // 播放
});
innerAudioContext.onStop(() => {
console.log('播放被停止')
})
innerAudioContext.onEnded(() => {
console.log('播放结束')
});
innerAudioContext.pause(); // 暂停
innerAudioContext.stop(); // 停止
innerAudioContext.destroy(); // 释放音频资源

wx.onShow(() => {
innerAudioContext.play(); // 当小游戏退后台回来时，恢复播放
})

wx.onAudioInterruptionEnd(function () {
innerAudioContext.play() // 当被其他事件中断播放结束后（如电话），恢复播放
})

**

const audioCtx = wx.createWebAudioContext()

const loadAudio = (url) => {
return new Promise((resolve, reject) => {
wx.request({
url,
responseType: 'arraybuffer',
success: res => {
console.log('res.data', res.data)
audioCtx.decodeAudioData(res.data, buffer => {
resolve(buffer)
}, err => {
console.error('decodeAudioData fail', err)
reject()
})
},
fail: res => {
console.error('request fail', res)
reject()
}
})
}

const play = () => {
// 需要自行替换链接
loadAudio('https://wx_test.mp3').then(buffer => {
let source = audioCtx.createBufferSource()
source.buffer = buffer
source.onended = () => {
console.log('播放结束')
};
source.connect(audioCtx.destination)
source.start()
}).catch(() => {
console.log('fail')
})
}

play();

wx.onShow(() => {
audioCtx.resume(); // 当小游戏退后台回来时，恢复播放
})

wx.onAudioInterruptionEnd(function () {
audioCtx.resume() // 当被其他事件中断播放结束后（如电话），恢复播放
})
