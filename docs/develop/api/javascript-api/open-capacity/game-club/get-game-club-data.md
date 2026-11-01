---
title: "tt.getGameClubData"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/game-club/get-game-club-data
update_time: 2025-07-14
---

基础库 3.77.0 开始支持本方法，这是一个**异步**方法。
获取游戏站数据

## 示例代码
```js
tt.authorize({
  scope: 'scope.gameClub',
  success: () => {
    tt.getGameClubData({
      success(res) {
        console.log('tt.getGameClubData success', res);
      },
      fail(err) {
        console.log('tt.getGameClubData fail', err);
      }
    });
  },
  fail: (err) => {
    console.log('tt.authorize fail', err);
    tt.showToast({
      title: '授权失败，请在设置页打开授权',
      icon: 'none'
    });
    // 引导到设置页打开授权
    tt.openSetting();
  },
});
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| data | Object | 游戏站数据  **对象字段** - **data**（Object）：游戏站数据 |

## 回调：失败回调
调用失败时的回调函数

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 10200 | auth deny |  |  |
| 21000 | User has not authorized |  |  |
| 21001 | server error |  |  |

## 相关课程
[「小游戏站」能力接入指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/mini-game-station/game-station-guide)

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/foundation/game-club) / [本地体验路径](tt-get-game-club-data)
