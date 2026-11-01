---
title: "tt.startCompass"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/device/compass/tt-start-compass
update_time: 2024-08-29
---

基础库 1.2.0 开始支持本方法，这是一个**异步**方法。
开始监听罗盘数据。罗盘数据会在用户手机发生“朝向变化/加速前进&后退/摇一摇”等手势时触发变化。

## 示例代码
```js
tt.startCompass({
  success(res) {
    //调用成功 startCompass:ok
    console.log("调用成功", res);
  },
  fail(err) {
    // 调用失败 startCompass:fail
    tt.showModal({
      title: "调用失败",
      content: JSON.stringfy(err),
    });
  },
});
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："startCompass:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："startCompass:fail" + 详细错误信息 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/device/compass/tt-start-compass) / [本地体验路径](tt-start-compass)
