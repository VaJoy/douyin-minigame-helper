---
title: "tt.showLoading"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/interface/interaction/tt-show-loading
update_time: 2024-07-24
---

## 语法

```js
tt.showLoading(title)
```
基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
显示灰色背景的 loading 提示框。该提示框不会主动隐藏。

## 示例代码
```js
tt.showLoading({
  title: "请求中，请稍后...",
  success(res) {
    console.log(`${res}`);
  },
  fail(res) {
    console.log(`showLoading调用失败`);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| title | string | 是 |  | 1.0.0 | 内容，最多显示 7 个汉字长度的文本 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："showLoading:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："showLoading:fail " + 详细错误信息 |

## 注意事项
- 尚未支持mask参数。
- loading 的实现基于 toast，等同于icon为loading，duration为24小时的 toast。
- 多次弹出 toast/loading 时，后一个会**立刻**覆盖前一个。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/interface/interaction/tt-show-loading) / [本地体验路径](tt-show-loading) / [在线试玩](https://developer.open-douyin.com/docs/playground?project_id=tma-demo&version=1.0.0.10&entry=tt-show-loading&codes_select=js&type=mini-game&sdk_version=1.0.0.205)
