---
title: "tt.showFavoriteGuide"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/favorite/tt-show-favorite-guide
update_time: 2024-07-30
---

## 展现形式
目前小游戏收藏引导组件支持以下两种类型，开发者可根据自身业务进行选择：
### 1. 气泡引导（type = tip）
气泡引导是一种轻量引导组件，它的调用既不会阻塞用户后续行为，也不要求用户一定去响应操作，在一定时间内向用户展现信息，便自动消失。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/other/5bce40cd7421e8fb3615b81fb60bbe33_image.png)

**展现策略：**
- 3s 后自动消失，组件箭头指向小程序菜单
- 每位用户最多触达【2 次】，最短间隔【3 天】才能第二次展现
- 若检测到用户已收藏该小程序，则不展示任何引导组件
### 2. 浮窗引导（type = bar）
浮窗引导的展现力度比气泡引导更强，用户在组件上能进行“添加”操作。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/other/0a8c6e4fabfafc7e639aef8b52e8d165_image.png)

**展现策略：**
- 10s 后自动消失
- 每位用户最多触达【2 次】，最短间隔【一周】才能第二次展现
- 若检测到用户已收藏该小程序，则不展示任何引导组件
### 3. 自定义引导（type = customize）
可以在游戏内自行绘制收藏引导入口，在用户点击入口后调用该方法，整体与游戏的契合度更强，并且能根据回调给到对应的用户发放激励奖励，牵引用户的长期留存。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/WeChat340d14228286d7e7fd2cedaeb6a7ee33-4595685665282736.png)

展现策略：
- 每位用户引导弹窗最多出现【3 次】
- 若用户触发方法前已收藏过该游戏，引导弹窗照常展示

## 语法

```js
tt.showFavoriteGuide(content, position, type)
```
基础库 1.41.0 开始支持本方法，这是一个**异步**方法。
在小游戏内调起关注小游戏的引导组件，用于引导用户关注小游戏。

## 示例代码
```js
tt.showFavoriteGuide({
  type: "customize",
  success(res) {
    console.log("isFavorited", res.isFavorited);  //此处输出 “isFavorited：true” 代表用户已收藏，若为false代表用户未收藏
  },
  fail(res) {
    console.log("自定义弹窗展示失败");
  },
});


tt.showFavoriteGuide({
  type: "bar",
  content: "一键添加到我的小程序",
  position: "bottom",
  success(res) {
    console.log("引导组件展示成功");
  },
  fail(res) {
    console.log("引导组件展示失败");
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| content | string | 否 | 一键添加到我的小程序 | 1.41.0 | 当 type == “tip” 时，可以配置文案，最多显示 12 个字符 |
| position | string | 否 | bottom | 1.41.0 | 弹窗类型为 bar 时的位置参数，可以是 bottom（贴近底部）、overtab（悬于页面 tab 区域上方） |
| type | string | 是 |  | 1.41.0 | 组件类型：bar（底部弹窗）、tip（顶部气泡）、customize（自定义组件） |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **isFavorited**（boolean）：返回是否收藏的信息，true：用户已收藏 ；  false：用户未收藏 - **errMsg**（string）："showFavoriteGuide:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："showFavoriteGuide:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |
| 10301 | feature is not supported in app isLogin/sessionId |  |  |
| 10401 | Internal error: common env error |  |  |
| 21000 | favorites function offline |  |  |
| 21000 | launch from feed not support favorites tip |  |  |
| 20000 | unknown `type` |  |  |

## 注意事项
展现策略仅在线上版、审核版有效，测试版、预览版不受限制。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/open-capacity/collect/favorite/tt-show-favorite-guide) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-show-favorite-guide%22%7D)
