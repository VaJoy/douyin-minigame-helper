---
title: "tt.showActionSheet"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/interface/interaction/tt-show-action-sheet
update_time: 2024-08-29
---

## 语法

```js
tt.showActionSheet(itemList)
```
基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
显示操作菜单。

## 示例代码
```js
const itemList = ["加精", "置顶", "删除", "封禁作者"];
tt.showActionSheet({
  itemList,
  success(res) {
    console.log(`你点击了第${res.tapIndex + 1}个项目，内容是 ${itemList[res.tapIndex]}`);
  },
  fail(res) {
    console.log(`showActionSheet调用失败`);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| itemList | Array<string> | 是 |  | 1.0.0 | 菜单的选项，最多支持 6 个选项 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **tapIndex**（number）：用户点击次序，从 0 开始计数 - **errMsg**（string）："showActionSheet:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："showActionSheet:fail" + 详细错误信息 |

## 注意事项
- iOS 实现时会自动加入「取消」选项，android 不会。
- 每个选项文案长度限制：

- android 没有限制，超长内容滚动。
- iOS 每个选项最多 **1** 行，每行约 **18** 个汉字。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/interface/interaction/tt-show-action-sheet) / [本地体验路径](tt-show-action-sheet) / [在线试玩](https://developer.open-douyin.com/docs/playground?project_id=tma-demo&version=1.0.0.10&entry=tt-show-action-sheet&codes_select=js&type=mini-game&sdk_version=1.0.0.205)
