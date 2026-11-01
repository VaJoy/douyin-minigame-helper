---
title: "tt.getRtcEngine"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/rtc/tt-get-rtc-engine
update_time: 2026-05-19
---

### 使用限制
能力目前支持抖音和抖音极速版，其他宿主暂未支持。

### 接入 RTC 的前置工作
- 需要申请开通 RTC 服务，注册生成 RTC 的 appid https://www.volcengine.com/docs/6348/69865
- Token 相关的请参考 https://www.volcengine.com/docs/6348/70121
- 开通后，可联系平台告知已开通获取token（群二维码在文档下方），平台运营人员核验后能力可正常调用

### 服务端接口：
#### 接口地址
### 
```ruby
GET https://developer.toutiao.com/api/apps/live/broadcast/generate_room_id
```

#### 输入

| 名称 | 类型 | 描述 | 是否必填 |
| --- | --- | --- | --- |
| access_token | string | 小程序的全局唯一调用凭据 [获取文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/server/interface-request-credential/non-user-authorization/get-access-token) | 是 |

#### 输出
返回值为 JSON 形式，其中包括如下字段：

```kotlin
{
    code: 0, //0 或者-1, 0 表示成功 
    data: {
        channelId: "123456789" // 频道 id
    }
    msg: 'success'
}
```

### tt.getRtcEngine(string appId)
获取 RtcEngine 实例（包含音视频应用程序调用的主要方法的接口类实例），应仅调用一次。第二次调用 `getRtcEngine` 时，需销毁上一个实例。
**参数列表**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| appId | string | 在火山申请获得的 RTC AppId，申请方式参考：https://www.volcengine.com/docs/6348/69865 |

**返回值**
RtcEngine 实例
**代码示例**

```cpp
const rtcEngine = tt.getRtcEngine("RTC AppId");
// rtcEngine.createChannel();
```

### RtcEngine
RtcEngine 实例

#### ~~RtcEngine.isSupported() ~~
> ~~该接口基础库2.48.0版本后已废弃，请勿使用~~
~~当前设备是否支持 rtc 连麦的使用~~
~~返回值 boolean~~

### 销毁
#### RtcEngine.destroy()
> 销毁 RtcEngine 实例，释放所有资源
**代码示例**

```js
// 获取rtcEngine 对象
let rtcEngine = tt.getRtcEngine("RTC AppId");
// 销毁
rtcEngine.destroy();
// 重新获取
rtcEngine = tt.getRtcEngine("RTC AppId");
// 多次获取返回不同对象，建议不要多次获取。
console.log(rtcEngine === tt.getRtcEngine("RTC AppId")); // false
rtcEngine.destroy();
console.log(rtcEngine === tt.getRtcEngine("RTC AppId")); // false
```

### 房间相关
#### RtcEngine.joinChannel(object param)
加入到通信房间

**参数列表**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| channelId | string | 加入语音频道的id |
| uid | string | 加入语音频道用户的唯一标识，建议统一使用当前用户的 openId/匿名 openId |
| token | string | token 的获取方法参考：https://www.volcengine.com/docs/6348/70121 建议开发者设置 token 的有效期为 1 天以上 |
| success | function | 成功的个回调只代表接口调用成功，不代表用户真正进房成功，真正进房需要监听onJoinChannelSuccess |
| fail | function |  |
| complete | function |  |

**返回值**

| errCode | 说明 |  |
| --- | --- | --- |
| 101 | 资源被释放了，需要重新获取实例 |  |
| 102 | api 调用失败 |  |
| 103 | 参数错误 |  |

**代码示例**

```css
rtcEngine.joinChannel({
    channelId: '123',
    uid: '123',
    token: 'token',
    success() {},
    fail () {},
})
```

#### RtcEngine.leaveChannel()
离开当前频道。离开频道时，麦克风权限仍然被占据使用，若用户退出频道，应使用disableLocalAudio()来释放麦克风。
**参数**

| success | function |  |
| --- | --- | --- |
| fail | function |  |
| complete | function |  |

**代码示例**

```js
rtcEngine.leaveChannel({
    success() {
        rtcEngine.disableLocalAudio()
    }
    fail() {}
})
```

### 音频相关
#### RtcEngine.enableLocalAudio()
开启内部音频采集。默认为关闭状态。

| success | function |  |
| --- | --- | --- |
| fail | function |  |
| complete | function |  |

```css
rtcEngine.enableLocalAudio();
```

#### RtcEngine.disableLocalAudio()
关闭本地麦克风推流功能

| success | function |  |
| --- | --- | --- |
| fail | function |  |
| complete | function |  |

```css
rtcEngine.disableLocalAudio()
```

#### RtcEngine.muteLocalAudioStream(object param)
控制本地音频流的发送状态：发送/不发送
使用此方法后，房间中的其他用户会收到回调： OnUserMuteAudio
**参数列表**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| success | function |  |
| fail | function |  |
| complete | function |  |

```css
rtcEngine.muteLocalAudioStream({
  success() {},
    fail () {},
});
```

#### RtcEngine.unmuteLocalAudioStream(object param)
控制本地音频流的发送状态：发送/不发送
使用此方法后，房间中的其他用户会收到回调： OnUserMuteAudio
**参数列表**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| success | function |  |
| fail | function |  |
| complete | function |  |

```css
rtcEngine.unmuteLocalAudioStream({
  success() {},
    fail () {},
});
```

#### RtcEngine.muteRemoteAudioStream(object param)
针对当前设备，静音远端用户音频流
**参数列表**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| uid | string | 语音频道用户的唯一标识 |
| success | function |  |
| fail | function |  |
| complete | function |  |

```css
rtcEngine.muteRemoteAudioStream({
    uid: 'user123456'
});
```

#### RtcEngine.unmuteRemoteAudioStream(object param)
针对当前设备，取消静音远端用户音频流
**参数列表**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| uid | string | 语音频道用户的唯一标识 |
| success | function |  |
| fail | function |  |
| complete | function |  |

```css
rtcEngine.unmuteRemoteAudioStream({
    uid: 'user123456'
});
```

#### RtcEngine.muteAllRemoteAudioStream()
静音当前设备接收的所有远端用户音频流

| success | function |  |
| --- | --- | --- |
| fail | function |  |
| complete | function |  |

```css
rtcEngine.muteAllRemoteAudioStream();
```

#### RtcEngine.unmuteAllRemoteAudioStream()
针对当前设备，取消静音所有远端用户音频流

| success | function |  |
| --- | --- | --- |
| fail | function |  |
| complete | function | ann |

```css
rtcEngine.unmuteAllRemoteAudioStream();
```

#### RtcEngine.adjustPlaybackSignalVolume(options)
调节播放音量（该方法只能加入房间成功后调用才生效）
**参数列表**
options是一个object类型，参数如下

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| volume | int | 音量可在0~400范围内进行调节  - 0 : 静音  - 100 : 原始音量  - 400 : 最大可为原始音量的 4 倍(自带溢出保护) |

**无返回值**

#### RtcEngine.adjustRecordingSignalVolume(number volume)
调节录音音量，采集麦克风的音量（该方法只能加入房间成功后调用才生效）
**参数列表**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| volume | int | 音量可在0~400范围内进行调节  - 0 : 静音  - 100 : 原始音量  - 400 : 最大可为原始音量的 2 倍(自带溢出保护) |

**无返回值**

#### RtcEngine.enableAudioVolumeIndication
启用说话者音量提示
- 该方法启用说话者音量提示。调用该方法后，将收到 audioVolumeIndication 事件回调。
- interval：收到音量提示回调的时间间隔
  - + ≤ 0：禁用音量提示功能。
  - + > 0：启用音量提示功能，并设置收到音量提示回调的时间间隔。单位为毫秒。
  - 建议设置为大于等于 200 毫秒；小于 10 毫秒时，行为未定义。
- 该方法只有在joinChannel之后才生效
**参数列表**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| interval | int | 音量提示间隔，默认 200 ms |

```css
rtcEngine.enableAudioVolumeIndication({
    interval: 200
});
```

### 回调相关

| 事件名称 | 说明 |
| --- | --- |
| joinChannelSuccess | 当加入房间成功时回调该事件 |
| rejoinChannelSuccess | 从用户掉线后重新加入房间成功回调该事件 |
| connectionLost | 当网络连接断开时回调该事件 |
| connectionInterrupted | ** **当用户意外从房间内掉线时回调该事件，此时房间将继续尝试加入房间 |
| userJoined | 当有其他用户加入到相同的房间后收到该事件 |
| userOffline | 当用户离开房间时回调该事件 |
| networkQuality | 当收到网络质量报告时会触发该事件回调 |
| firstLocalAudioFrame | 当收到本地第一帧音频的时候上报该事件 |
| firstRemoteAudioFrame | 当收到远端流的第一帧音频的时候上报该事件 |
| userMuteAudio | 当远端用户流开/禁声音时回调该事件 |
| ~~userEnableAudio~~ | ~~当远端用户是否包含音频流的回调~~ RTC3.15废弃 |
| userEnableLocalAudio | 当远端用户允许开启音频设备时回调该事件 |
| warning | 当内部发生警告信息时回调该事件 |
| error | 当内部发生不可逆转测错误时回调 |

> 多次注册会存在多个回调函数，可以通过RtcEngine.removeAllListener(String event) 取消该事件对应的所有监听函数。

#### RTCEngine.onJoinChannelSuccess(Function cb)
首次加入房间成功。用户手动调用 joinChannel，加入房间成功后触发该事件回调。
加入房间失败没有单独的事件，需要通过 onError 事件判断

```js
rtcEngine.onJoinChannelSuccess( (data)=> {
    console.log("onJoinChannelSuccess " + data['elapsed']);
});
```

**返回值**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| elapsed | int | 从调用joinChannel开始到加入房间成功所经历的时间（毫秒单位） |

#### RTCEngine.offJoinChannelSuccess(Function cb)
取消该事件监听

#### RTCEngine.onRejoinChannelSuccess
重新加入房间。用户网络较差，失去与服务器的连接时，进行重连成功后触发该事件回调

```js

rtcEngine.onRejoinChannelSuccess( ()=> {
    console.log("onRejoinChannelSuccess " + data['elapsed']);
});
```

**返回值**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| elapsed | int | 从用户掉线到重新加入房间成功经历的时间（毫秒单位） |

#### RTCEngine.offRejoinChannelSuccess(Function cb)
取消该事件监听

#### RTCEngine.onNetworkQuality
当收到网络质量报告时会触发该事件回调

```js
rtcEngine.onNetworkQuality( ()=> {
    console.log(`onNetworkQuality uid=${data.uid} txQuality=${data.txQuality} rxQuality=${data.rxQuality}`);
});
```

**返回值**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| uid | string | 远端通话用户标识 |
| txQuality | int | 所属用户的媒体流上行网络质量  * ByteNetworkQuality的取值为:  * \| 变量名称 \| 描述 \|  * \| -2 \| 网络质量未知 \|  * \| 4 \| 网络质量极好 \|  * \| 3 \| 用户主观感觉和 excellent 差不多，但码率可能略低于 excellent \|  * \| 2 \| 用户主观感受有瑕疵但不影响沟通 \|  * \| 1 \| 勉强能沟通但不顺畅 \|  * \| 0 \| 网络质量非常差，基本不能沟通 \|  * \| -1 \| 完全无法沟通 \| |
| rxQuality | int | 所属用户的媒体流下行网络质量 |

#### RTCEngine.offNetworkQuality(Function cb)
取消该事件监听

#### RTCEngine.onUserJoined
远端可见用户加入房间的回调。
- 远端可见用户断网后重新连入房间时，房间内其他用户将收到该事件。
- 新进房用户会收到进房前已在房内的可见用户的进房回调通知。

```js
rtcEngine.onUserJoined( ()=> {
    console.log("onUserJoined " + data['uid'] + data['elapsed']);
});
```

**返回值**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| uid | string | 远端用户标识 |
| elapsed | int | 从加入房间到收到该事件经历的时间（毫秒单位） |

#### RTCEngine.offUserJoined(Function cb)
取消该事件监听

#### RTCEngine.onUserOffline
远端可见用户离开房间，包含断网情况

```js
rtcEngine.onUserOffline( ()=> {
    console.log("onUserOffline " + data['uid'] + data['elapsed']);
});
```

**返回值**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| uid | string | 离线用户的标识 |
| reason | int | 用户离线的原因 0,// quit normal 1,// user lost |

#### RTCEngine.offUserOffline(Function cb)
取消该事件监听

#### RTCEngine.onConnectionInterrupted
** **RTC 连接断开。该事件与 connectionLost 类似，但会在断开连接后立即触发

```js
rtcEngine.onConnectionInterrupted( ()=> {
   console.log("onConnectionInterrupted");
});
```

**无返回值**

#### RTCEngine.offConnectionInterrupted(Function cb)
取消该事件监听

#### RTCEngine.onConnectionLost
网络连接断开超过 10 秒，仍然会继续重连。该事件和上面事件类似，不过是超过 10 秒后触发

```js
rtcEngine.onUserOffline( ()=> {
   console.log("onConnectionLost");
});
```

**无返回值**

#### RTCEngine.offConnectionLost(Function cb)
取消该事件监听

#### RTCEngine.onFirstLocalAudioFrame
当收到本地第一帧音频的时候上报该事件

```js
rtcEngine.onFirstLocalAudioFrame( ()=> {
   console.log("onFirstLocalAudioFrame");
});
```

**返回值**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| elapsed | int | 返回StreamIndex: 0-视频流；1-屏幕流 |

#### RTCEngine.offFirstLocalAudioFrame(Function cb)
取消该事件监听

#### RTCEngine.onFirstRemoteAudioFrame
接收到来自远端某音频流的第一帧时，收到该回调。
* 当首次接收到房间内任一用户的音频流时触发该回调。

```js
rtcEngine.onFirstRemoteAudioFrame( ()=> {
   console.log("onFirstRemoteAudioFrame " + data['uid'] + data['elapsed']);
});
```

**返回值**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| uid | string | 远端用户标识 |
| elapsed | int | 返回StreamIndex: 0-视频流；1-屏幕流 从加入房间开始到收到该事件经历的时间（毫秒单位） |

#### RTCEngine.offFirstRemoteAudioFrame(Function cb)
取消该事件监听

#### RTCEngine.onUserMuteAudio
远端用户调用 muteLocalAudioStream 方法
* 改变本地音频推流状态时，房间内其他用户会收到此回调。
* @param muted 是否被静音
* true: 远端用户禁止推送音频数据；
false: 远端用户开启推送音频数据

```js
rtcEngine.onUserMuteAudio( ()=> {
   console.log("onUserMuteAudio " + data['uid'] + data['muted']);
});
```

**返回值**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| uid | string | 远端用户标识 |
| muted | boolean | 是否被静音  true: 远端用户禁止推送音频数据；  false: 远端用户开启推送音频数据 |

#### RTCEngine.offUserMuteAudio(Function cb)
取消该事件监听

#### RTCEngine.onUserEnableLocalAudio
远端用户enableLocalAudio/disableLocalAudio 开启/关闭音频设备采集时，房间内其他人会收到这个回调。
- userMuteAudio 和 userEnableLocalAudio 分别代表开/关 本地麦克风采集 和开/关 推送本地数据。
- 之所以有这样的区分，是因为 开/关 本地麦克风采集成本 的远大于 开/关 推送本地数据。因为麦克风采集需要调用系统接口，而 开/关推送数据只是标识位的改变。

```js
rtcEngine.onUserEnableLocalAudio(()=> {
   console.log("onUserEnableLocalAudio " + data['uid'] + data['enabled']);
});
```

**返回值**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| uid | string | 远端用户标识 |
| enabled | boolean | 该用户是否开启了音频设备采集 true: 远端用户允许开启音频设备； false: 远端用户禁止开启音频设备； |

#### RTCEngine.offUserEnableLocalAudio(Function cb)
取消该事件监听

#### RTCEngine.onAudioVolumeIndication
当收到音量信息时回调该事件,需要调用 enableAudioVolumeIndication 后才可以
- 对于本地用户：只要进行本地音频采集，回调内就会包含本地音频流的音量信息。
- 对于远端用户：回调内会包含其发送的音频流的音量信息。

```js
rtcEngine.onAudioVolumeIndication( ()=> {
   console.log("onAudioVolumeIndication " + data['uid'] + data['volume']);
});
```

**返回值**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| uid | string | 用户id |
| volume | number | 音量大小，范围[0,255] |
| speakerNumber | number | 音频源数量 |

#### RTCEngine.offAudioVolumeIndication(Function cb)
取消该事件监听

#### RTCEngine.onWarning(Function cb)
当内部发生警告信息时回调该事件

```js
rtcEngine.onWarning( ()=> {
   console.log("onWarning");
});
```

**返回值**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| warn | int | 离线用户的标识 /**  ***@brief **获取房间信息失败警告  * SDK获取room信息失败（包含超时，返回非200的错误码） 每隔两秒重试一次，  * 连续失败5次后，报该warning，并继续重试  * 提示用户:进入房间失败，请稍后再试  */  **BRWARN_GET_ROOM_FAILED = -2000,**   /**  ***@brief **加入房间失败警告  * 发送token或reconnect时，收到6xx错误  * 提示用户已经掉线，请稍后再试  */  **BRWARN_JOIN_ROOM_FAILED = -2001,**   /**  ***@brief **发布媒体数据失败警告  * publish时，收到5xx错误 重试3次，如果还失败，向业务方报该warning  * 提示用户发布本地媒体数据失败，请稍后再试  */  **BRWARN_PUBLISH_STREAM_FAILED = -2002,**   /**  ***@brief **订阅媒体数据404警告  * subscribe时，收到404错误向业务方报该warning  * 提示用户，获取对方媒体数据失败，请退出重试  */  **BRWARN_SUBSCRIBE_STREAM_FAILED_404 = -2003,**   /**  ***@brief **订阅媒体数据5xx警告  * subscribe时，收到5xx错误  */  **BRWARN_SUBSCRIBE_STREAM_FAILED_5xx = -2004,**   /**  *@brief 函数调用顺序错误  * 函数不应该被调用  */  **BRWARN_INVOKE_ERROR = -2005,**   /**  ***@brief **发布媒体数据失败警告  * 提示用户发布本地截屏数据失败，请稍后再试  */  **BRWARN_PUBLISH_SCREEN_FAILED = -2006,**   /**  ***@brief** 函数调用顺序错误  * 函数不应该被调用，调用 EnableAutoSubscribe 后才能调用 subscribeStream  * */  **BRWARN_SUBSCRIBE_STREAM_FORBIDEN = -2010,**   /**  * @biref 发送自定义广播消息失败  * 当前信令服务器没有链接或链接断开，自定义广播消息发送失败  */  **BRWARN_SEND_CUSTOM_MESSAGE = -2011,**   /**  ***@brief **没有获取到摄像机权限  * 当前app没有获取到摄像机权限  */  **BRWARN_PERMISSION_CAMERA = -5001,**   /**  ***@brief **没有获取到麦克风权限  * 

  * 当前app没有获取到麦克风权限  */  **BRWARN_PERMISSION_MICROPHONE = -5002,** |

#### RTCEngine.offWarning(Function cb)
取消该事件监听

#### RTCEngine.onError
当内部发生不可逆转的错误时回调，比如加入房间失败

```js
rtcEngine.onError( ()=> {
   console.log("onError " + data['err']);
});
```

**返回值**

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| err | int | /**  ***@brief **token失效错误  * 发送token或reconnect时，收到7xx错误  * getRoom调用正常，但从服务端获取的数据有误  * 重新获取token，再join room  */ ** BRERR_INVALID_TOKEN = -1000,**   /**  ***@brief **进入房间错误  * 发送token或reconnect时，收到5xx错误  * 提示用户:已经掉线，请稍后再试  */ ** BRERR_JOIN_ROOM_ERROR = -1001,**   /**  ***@brief **没有发布媒体权限  * publish时，收到403 向业务方报该error  * 提示用户:没有发布媒体数据的权限  */ ** BRERR_NO_PUBLISH_PERMISSION = -1002,**   /**  ***@brief **没有订阅媒体权限  * subscribe时，收到403 向业务方报该error  * 提示用户:没有订阅媒体数据的权限  */ ** BRERR_NO_SUBSCRIBE_PERMISSION = -1003,**   /**  ***@brief **用户重登录错误  * 用户重复登录 向业务方报该error 退出SDK  * 并提示用户:账号已在其它地方登录  */ ** BRRERR_DUPLICATE_LOGIN = -1004,**   /**  ***@brief **server端返回的数据非法  * 检查server端返回的数据，如果数据非法  */ ** BRERR_GET_ROOM_INVALID_RESPONSE = -1005,**   /**  ***@brief **server返回期望的媒体服务器地址不可用  * 重新尝试新的媒体服务器地址或者不指定地址  */ ** BRERR_INVALID_EXPECT_MS_ADDR = -1006,**   /**  ***@brief **创建媒体数据错误  * 创建SDP出错 向业务方报该error  * 提示用户:创建媒体数据失败，请稍后再试  */ ** BRERR_INVALID_SDP = -1010,**   /**  ***@brief **音频初始化失败  * 音频设备初始化失败 向业务方报该error 退出SDK  * 并提示用户:音频设备初始化失败  */ ** BRERR_ADM_INIT_FAILE = -1020,**   /**  ***@brief **音频设备启动失败错误  * 当前设备可能被其他应用占用  */ ** BRERR_START_CALL = -1021,**   /**  ***@brief **没有录音权限错误  * 当前app没有获取音频录制权限  */ ** BRERR_ADM_NO_PERMISSION = -1022,**   /**  ***@brief **没有音频全局设置权限错误  * 

  * 当前app没有没有获取音频全局设置权限  */ ** BRERR_ADM_NO_MODIFY_PERMISSION = -1023,**   /**  ***@brief **视频渲染失败  */ ** BRERR_RENDER_FAILED = -1030,**   /**  ***@brief **没有网络权限错误  * 

  * 当前app没有获取网络权限  */ ** BRERR_INM_NO_PERMISSON = -1050,** |

#### RTCEngine.offError(Function cb)
取消该事件监听

### RtcEngine.removeAllListeners(String event)
取消 RtcEngine,on 监听的所有event类型事件。当event 为空的时候，会移除所有RtcEngine上的事件监听。可传入参数如下，分别对应上面事件。当不传入时，默认移除所有事件监听

```text
         'joinChannelSuccess',
          'rejoinChannelSuccess',
          'networkQuality',
          'userJoined',
          'userOffline',
          'connectionInterrupted',
          'connectionLost',
          'firstLocalAudioFrame',
          'firstRemoteAudioFrame',
          'userMuteAudio',
          'userEnableLocalAudio',
          'audioVolumeIndication',
          'warning',
          'error',
```

## 完整示例

```js

// 1. 获取实例
const rtcEngine = tt.getRtcEngine("RTC AppId");

// 2. 监听需要的事件
rtcEngine.onJoinChannelSuccess( () => {})
rtcEngine.onConnectionLost( () => {})
rtcEngine.onWarning( () => {})
rtcEngine.onError( () => {})

// 3. 获取频道（对接开发者服务获取）和 token (参考火山 token 生成)
*let channelId = "channelIdtest";
*let token = "testToken";

// 4. 广播连麦 channelId，所有用户加入频道
rtcEngine.joinChannel({
    channelId,
    uid: 'user1',
    token
});

// 5. 开启本地推流
rtcEngine.enableLocalAudio();

rtcEngine.leaveChannel();

rtcEngine.leaveChannel();
```

## 连麦状态
RTC没有提供是否正在连麦的接口，业务方需要自己维护是否在channel里的状态
joinChannelSuccess 事件里面设置true
RejoinChannelSuccess事件里面设置true
leaveChannel 的success里面设置false
connectionLost 事件里面设置false
error 事件里面建议调用leaveChannel

## 问题反馈

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/179618a4ed264406b6127c904ece5635~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/85e93b77e30f439b9034897c54131a00~tplv-9nona0m7ha-image.image)