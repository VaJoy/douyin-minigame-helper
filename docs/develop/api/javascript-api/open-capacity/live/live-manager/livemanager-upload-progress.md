---
title: "LiveManager.uploadGameProgress"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/live/live-manager/livemanager-upload-progress
update_time: 2025-10-10
---

## 语法

```js
LiveManager.uploadGameProgress(data)
```
基础库 3.85.0 开始支持本方法，这是一个**异步**方法。
上传主播游玩场景配置。

## 示例代码
```js
const liveManager = tt.getLiveManager();

liveManager.uploadGameProgress({
    data: '当前游戏关卡: 100', // 上传游戏进度信息
    success: () => {
        console.log('上传成功');
    },
    fail: (res) => {
        console.log('上传失败', res);
    },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| data | string | 是 |  | 3.85.0 | 游玩进度配置信息，长度不超过512KB |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object类型，属性如下：  **对象字段** - **errMsg**（string）："LiveManager.uploadGameProgress:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object类型，属性如下：  **对象字段** - **errMsg**（string）："LiveManager.uploadGameProgress:fail" + 详细错误信息 - **errNo**（number）：错误码，对应信息可参考错误码说明 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 21100 | can only call in video live |  |  |
| 21101 | can only call in anchor side |  |  |
| 21102 | the game's instant play is closed. |  |  |
| 21103 | anchor's instant play is closed |  |  |
| 21104 | frequency limit |  |  |
| 21105 | data is too large |  |  |
| 21106 | server error |  |  |

## 使用限制
仅在直播场景下可调用

## 前置条件
使用前，请先前往游戏开放后台，申请开通直播即看即玩能力

## 相关课程
[直播即看即玩能力技术指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/instant-play-introduce)

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
