---
title: "tt.setKeepScreenOn"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/device/screen-intensity/tt-set-keep-screen-on
update_time: 2024-07-24
---

## 语法

```js
tt.setKeepScreenOn(keepScreenOn)
```
基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
设置是否保持屏幕常亮状态。

## 示例代码
```js
tt.setKeepScreenOn({
  keepScreenOn: false,
  success(res) {
    console.log(`屏幕常亮已关闭，省电中`);
  },
  fail(res) {
    console.log(`setKeepScreenOn调用失败`);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| keepScreenOn | boolean | 是 |  | 1.0.0 | 是否保持屏幕常亮 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："setKeepScreenOn:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："setKeepScreenOn:fail" + 错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 20000 | internal error |  |  |

## 使用限制
仅在当前小游戏生效，离开小游戏后设置失效。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/device/screen-intensity/tt-set-keep-screen-on) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-set-keep-screen-on%22%7D)
