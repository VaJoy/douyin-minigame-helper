---
title: "tt.onShareAppMessage"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/retweet/tt-on-share-app-message
update_time: 2025-11-18
---

> 基础库 1.0.0 开始支持本方法，这是一个同步方法。
本API为被动分享监听操作：监听用户点击平台提供的分享入口时触发的事件（如右上角更多面板中的分享、排行榜中的分享），以指定用户的分享内容。
主动分享调用（游戏内主动拉起发布器、好友邀请、录屏分享等）详见 [tt.shareAppMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-share-app-message)

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 该方法可以监听用户通过右上角菜单中触发的分享操作，在不同宿主端具体的操作会有所差别，在抖音中包括分享和拍抖音，在头条包括分享和发头条，以此类推。 该方法的实际调用链路为： 开发者注册此事件 用户点击小游戏菜单中的分享或者拍抖音等按钮 自动调用开发者通过** tt.onShareAppMessage** 定义的函数，并传入带有 channel 参数的对象，执行得到该函数的返回对象 接着调用** tt.shareAppMessage** ，将上一步返回的对象传入其中，拉起分享 当开发者发现虽然已成功配置分享内容，但是调试时内容无法生效时，有可能是分享内容触发了内容安全检测失败，导致分享失败。发生这种情况时，开发者可以尝试对分享内容进行内容安全检测，具体操作手段见[内容安全检测](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/server/content-security/content-security-detect/) |
| 相关教程 | 无 |

## 语法

```js
tt.onShareAppMessage(callback)
```

## 参数说明
#### callback

| 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- |
| function |  | 是 | 监听触发“转发”的函数。函数返回 [ShareParam](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/share-param) 对象，该返回对象可以用来自定义分享的内容。 | 1.0.0 |

callback 是一个回调函数，接收和返回的参数都是 object 类型的参数，属性详见 [ShareParam](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/share-param)
- 接收参数使用说明：
  - 可通过 `channel` 判断用户即将触发什么类型的分享，值含义说明详见 [ShareParam](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/share-param)
  - 可通过 `res.extra.position` 判断用户触发分享的点位：top 表示为右上角更多面板中的分享。
## 返回值
无
## 错误码

| errNo | errMsg | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| 20000 | internal error | 小游戏框架内部错误，有需要请[创建工单](https://developer.open-douyin.com/work-order-page?tab=workOrderRecord)咨询 | 1.0.0 |
| 20001 | invalid param | 参数错误 | 1.0.0 |

## 代码示例
示例一：

```js
tt.onShareAppMessage(function (res) {
  console.log(res.channel);
  // do something
  const shareData = {
    success() {
      console.log("分享成功");
    },
    fail(e) {
      console.log("分享失败", e);
    },
  };
  const r = Object.assign({ channel: res.channel }, shareData);
  //channel值无法修改，并会在调用tt.shareAppMessage时自动带上
  switch (res.channel) {
    case "video":
      r.extra = {
        videoTopics: ["test1 videoTopics", "test2 videoTopics"], // 抖音小视频话题列表
        videoPath: "videotest.mp4", // 如果为抖音或者头条小视频，可以直接传本地视频路径
        //以抖音为例，使用videoPath后，用户点击拍抖音时会去分享开发者指定的视频。
      };
      break;
    default:
        if (res.extra.position === "top") {    // 为用户点击右上角更多面板中的分享
            r.templateId = "",     // 替换为审核通过的templateId
        } else {    // 为用户点击游戏内平台拉起的分享，如排行榜中的分享
             r.templateId = "",     // 替换为审核通过的templateId
        }
      break；
  }
  return r;
});
```

tt.onShareAppMessage(function (res) {
console.log(res.channel);
// do something
const shareData = {
title: "分享标题",
query: "k1=v1&k2=v2",
success() {
console.log("分享成功");
},
fail(e) {
console.log("分享失败", e);
},
};
const r = Object.assign({ channel: res.channel }, shareData);
//channel值无法修改，并会在调用tt.shareAppMessage时自动带上
switch (res.channel) {
case"video":
r.extra = {
videoTopics: ["test1 videoTopics", "test2 videoTopics"], // 抖音小视频话题列表
videoPath: "videotest.mp4", // 如果为抖音或者头条小视频，可以直接传本地视频路径
//以抖音为例，使用videoPath后，用户点击拍抖音时会去分享开发者指定的视频。
};
break;
case"article":
default:
break;
}
return r;
});

tt.onShareAppMessage(function (res) {
console.log(res.channel);// do somethingconst shareData = {title: "分享标题",query: "k1=v1&k2=v2",success() {
console.log("分享成功");},fail(e) {
console.log("分享失败", e);},};const r = Object.assign({ channel: res.channel }, shareData);//channel值无法修改，并会在调用tt.shareAppMessage时自动带上switch (res.channel) {case "video":
r.extra = {videoTopics: ["test1 videoTopics", "test2 videoTopics"], // 抖音小视频话题列表videoPath: "videotest.mp4", // 如果为抖音或者头条小视频，可以直接传本地视频路径//以抖音为例，使用videoPath后，用户点击拍抖音时会去分享开发者指定的视频。};break;case "article":default:break;}return r;});

### 语法

```js
tt.onShareAppMessage(callback)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
监听用户点击右上角菜单中的“转发”按钮时触发的事件。

### 示例代码

示例一：

```js
tt.onShareAppMessage(function (res) {
  //当监听到用户点击了分享或者拍抖音等按钮后，会执行该函数
  console.log(res.channel);
  // do something
  return {
    //执行函数后，这里是需要该函数返回的对象
    templateId: "", // 替换成通过审核的分享ID
    title: "分享标题",
    query: "k1=v1&k2=v2",
    success() {
      console.log("分享成功");
    },
    fail(e) {
      console.log("分享失败", e);
    },
  }; //返回的对象会传入tt.shareAppMessage进行最终分享
});
```

示例二：

```js
tt.onShareAppMessage(function (res) {
  console.log(res.channel);
  // do something
  const shareData = {
    title: "分享标题",
    query: "k1=v1&k2=v2",
    success() {
      console.log("分享成功");
    },
    fail(e) {
      console.log("分享失败", e);
    },
  };
  const r = Object.assign({ channel: res.channel }, shareData);
  //channel值无法修改，并会在调用tt.shareAppMessage时自动带上
  switch (res.channel) {
    case "video":
      r.extra = {
        videoTopics: ["test1 videoTopics", "test2 videoTopics"], // 抖音小视频话题列表
        videoPath: "videotest.mp4", // 如果为抖音或者头条小视频，可以直接传本地视频路径
        //以抖音为例，使用videoPath后，用户点击拍抖音时会去分享开发者指定的视频。
      };
      break;
    case "article":
    default:
      break;
  }
  return r;
});
```

### 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.0.0 | 监听触发“转发”的函数。函数可以返回 [ShareParam](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/share-param) 对象，该返回对象可以用来自定义分享的内容。  **对象字段** - **args_0**（Object）：object 类型，属性如下： |

### 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |
| 20001 | invalid param |  |  |

### 注意事项
- 该方法可以监听用户通过右上角菜单中触发的分享操作，在不同宿主端具体的操作会有所差别，在抖音中包括分享和拍抖音，在头条包括分享和发头条，以此类推。
- 该方法的实际调用链路为：

1. 开发者注册此事件
2. 用户点击小游戏菜单中的分享或者拍抖音等按钮
3. 自动调用开发者通过 **tt.onShareAppMessage** 定义的函数，并传入带有 channel 参数的对象，执行得到该函数的返回对象
4. 接着调用 **tt.shareAppMessage** ，将上一步返回的对象传入其中，拉起分享

- 当开发者发现虽然已成功配置分享内容，但是调试时内容无法生效时，有可能是分享内容触发了内容安全检测失败，导致分享失败。发生这种情况时，开发者可以尝试对分享内容进行内容安全检测，具体操作手段见[内容安全检测](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/server/content-security/content-security-detect/)

### 授权要求
无需开发者授权；无需用户授权

### 支持平台
iOS、Android