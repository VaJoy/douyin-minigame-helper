---
title: "tt.showToast"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/interface/interaction/tt-show-toast
update_time: 2024-07-24
---

## 语法

```js
tt.showToast(icon, duration, title)
```
基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
显示灰色背景的消息提示框。

## 示例代码
```js
tt.showToast({
  title: "添加购物车成功",
  duration: 2000,
  success(res) {
    console.log(`${res}`);
  },
  fail(res) {
    console.log(`showToast调用失败`);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| icon | string | 否 | success | 1.0.0 | 图标，取值范围包括success, loading, none, fail(1.36.0版本支持) |
| duration | number | 否 | 1500 | 1.0.0 | 提示框停留时间，单位ms |
| title | string | 否 | '' | 1.0.0 | 内容。不传时当空字符串处理 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："showToast:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："showToast:fail " + 详细错误信息 |

## 使用限制
- 尚未支持 image 和 mask 参数。
- 多次弹出 toast/loading 时，后一个会**立刻**覆盖前一个。
- 当显示图标时，最多能够展示 8 个汉字长度。不显示图标时，文本可最多展示 2 行。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/interface/interaction/tt-show-toast) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-show-toast%22%7D) / [在线试玩](https://developer.open-douyin.com/docs/playground?project_id=tma-demo&version=1.0.0.10&entry=tt-show-toast&codes_select=js&type=mini-game&sdk_version=1.0.0.205)
