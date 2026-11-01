---
title: "tt.showModal"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/interface/interaction/tt-show-modal
update_time: 2024-07-24
---

## 语法

```js
tt.showModal(title, content, confirmText, showCancel, cancelText)
```
基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
显示模态弹窗。

## 示例代码
```js
tt.showModal({
  title: "请求获得定位权限",
  content: "获得你的地理位置能够更好的为你推荐本地信息",
  success(res) {
    if (res.confirm) {
      console.log("confirm, continued");
    } else if (res.cancel) {
      console.log("cancel, cold");
    } else {
      // what happend?
    }
  },
  fail(res) {
    console.log(`showModal调用失败`);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| title | string | 否 |  | 1.0.0 | 标题 |
| content | string | 否 |  | 1.0.0 | 内容 |
| confirmText | string | 否 | 确定 | 1.0.0 | 确定按钮的文案，最多 4 个字符 |
| showCancel | boolean | 否 | true | 1.0.0 | 是否显示取消按钮 |
| cancelText | string | 否 | 取消 | 1.0.0 | 取消按钮的文案，最多 4 个字符 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **confirm**（boolean）：是否点击了确定按钮 - **cancel**（boolean）：是否点击了取消按钮 - **errMsg**（string）："showModal:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："showModal:fail " + 详细错误信息 |

## 使用限制
- 暂不支持 confirmColor 和 cancelColor 参数。
- title 的长度限制：

- android 端限制为 **1** 行，每行约 13 个汉字。
- iOS 端限制为 **3** 行，每行约 17 个汉字。

- content 的长度限制：

- android 端没有限制，Modal 最高为屏幕高度，内容滚动；
- iOS 端限制为 **3** 行，每行约 17 个汉字。

- 输入参数的 title 和 content 不可同时为空。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/interface/interaction/tt-show-modal) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-show-modal%22%7D) / [在线试玩](https://developer.open-douyin.com/docs/playground?project_id=tma-demo&version=1.0.0.10&entry=tt-show-modal&codes_select=js&type=mini-game&sdk_version=1.0.0.205)
