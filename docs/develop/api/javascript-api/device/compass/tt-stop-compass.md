---
title: "tt.stopCompass"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/device/compass/tt-stop-compass
update_time: 2024-08-29
---

基础库 1.2.0 开始支持本方法，这是一个**异步**方法。
停止监听罗盘数据。

## 示例代码
```js
tt.stopCompass({
  success(res) {
    //调用成功 stopCompass:ok
    console.log("stopCompass 调用成功", res);
  },
  fail(err) {
    // 调用失败 stopCompass:fail
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
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："stopCompass:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："stopCompass:fail" + 详细错误信息 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/device/compass/tt-stop-compass) / [本地体验路径](tt-stop-compass)
