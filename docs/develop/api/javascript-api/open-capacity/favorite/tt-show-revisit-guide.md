---
title: "tt.showRevisitGuide"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/favorite/tt-show-revisit-guide
update_time: 2024-08-19
---

基础库 2.94.0 开始支持本方法，这是一个**异步**方法。
调起引导用户复访的提示弹窗，目前仅抖音宿主支持。为了更好的玩家体验，建议在按钮的点击回调中使用。

## 示例代码
```js
tt.showRevisitGuide({
    success() {
        console.log('成功调起复访引导弹窗');
    },
    fail(res) {
        console.log('调用失败，错误信息：%s', res.errMsg);
    }
})
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："showRevisitGuide:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："showRevisitGuide:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21100 | current host has no revisit guide |  |  |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/open-capacity/collect/favorite/tt-show-revisit-guide) / [本地体验路径](tt-show-revisit-guide)
