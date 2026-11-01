---
title: "小游戏配置"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/mini-game-configuration
update_time: 2025-03-31
---

小游戏根目录下的 `game.json` 文件用来对小游戏进行配置。文件内容为一个 JSON 对象，有以下属性。
## 配置项说明

| 属性 | 类型 | 必填 | 默认值 | 描述 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| deviceOrientation | String | 否 | 'landscape' | 设置屏幕方向 | – |
| showStatusBar | Boolean | 否 | false | 是否显示状态栏 | – |
| networkTimeout | Object | 否 | – | 网络请求的超时时间，单位：毫秒 | – |
| workers | String | 否 | – | 多线程 Worker 配置项，详细请参考 [Worker 文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/worker/worker/) | – |
| ttNavigateToMiniGameAppIdList | String Array | 否 | – | 需要跳转的小游戏列表。**相关接口已废弃，不建议使用** | 1.23.0 |
| openDataContext | String | 否 | – | 小游戏开放数据域目录，详见 [开放数据域](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/relationship-chain/open-data-area/tt-get-open-data-context/) | 1.11.0 |
| subPackages | Object | 否 | – | 分包结构配置，详见 [分包加载](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/subpackages/introduction) | 1.88.0 |
| menuButtonStyle | String | 否 | – | 设置小游戏右上角更多面板深浅色模式，具体 UI 效果见下方合法值说明 | 3.16.0 |
| enableIOSHighPerformanceMode | Boolean | 否 | false | iOS 操作系统上小游戏是否开启高性能模式，详见 [普通小游戏高性能模式](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/runtime-performance/high-performance-mode) | 3.43.0 |
| plugins | Object | 否 | - | 插件配置，指定依赖的插件， 可以通过 requirePlugin 能力加载插件。**插件功能还在内测中， 声明平台不支持的插件会有编译报错，如不需要，请删除game.json中的 plugins字段** | 3.65.0 |

## deviceOrientation 的合法值

| 值 | 说明 |
| --- | --- |
| portrait | 竖屏。不随用户手机的旋转而旋转。 |
| landscape | home 键在屏幕右侧的横屏。当用户的手机没有锁定屏幕方向时，横屏的方向会随着手机的旋转而旋转。 |

## networkTimeout
各类网络请求的超时时间，单位均为毫秒。

| 属性 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| request | Number | 否 | 60000 | [tt.request](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/network/initiate-a-request/tt-request/) 的超时时间，单位：毫秒。 |
| connectSocket | Number | 否 | 60000 | [tt.connectSocket](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/network/websocket/tt-connect-socket/) 的超时时间，单位：毫秒。 |
| uploadFile | Number | 否 | 60000 | [tt.uploadFile](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/network/onload/tt-upload-file/) 的超时时间，单位：毫秒。 |
| downloadFile | Number | 否 | 60000 | [tt.downloadFile](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/network/download/tt-download-file/) 的超时时间，单位：毫秒。 |

## menuButtonStyle 的合法值

| 值 | 说明 |
| --- | --- |
| light | 浅色模式。适合用于背景色偏亮。 |
| dark | 深色模式。适合用于背景色偏暗。 |

### 
## workers
使用 [Worker](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/worker/worker/) 处理多线程任务时，设置 Worker 代码放置的目录
## ttNavigateToMiniGameAppIdList
> 注意：基础库 1.23.0 开始支持，低版本需做兼容处理。
> 当小游戏需要使用跳转类接口到其他小游戏时，需要先在配置文件中声明需要跳转的小游戏 appId 列表，最多允许填写 10 个。
> 该字段涉及接口`tt.createMoreGamesButton``tt.showMoreGamesModal`已废弃，不建议继续使用。
## plugins
插件配置, 类型是一个 Object，key 是插件别名， value 类型如下:

| 属性 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| provider | string | 否 |  | 插件id |
| version | string | 否 |  | 插件版本 |

示范用例如下:

```json
{
    "plugins": {
        "cocos": {
            "provider": "ttxxxxxxx",
            "version": "1.0.0"
        }
    }
}
```
