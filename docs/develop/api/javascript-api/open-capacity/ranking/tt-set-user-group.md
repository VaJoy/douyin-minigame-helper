---
title: "tt.setUserGroup"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/ranking/tt-set-user-group
update_time: 2025-10-10
---

tt.setUserGroup({
groupId: "test_group",
});

## 语法

```js
tt.setUserGroup(groupId)
```
基础库 1.17.0 开始支持本方法，这是一个**异步**方法。
设置用户分组。

## 示例代码
```js
tt.setUserGroup({
  groupId: "test_group",
  success() {
    console.log("设置用户分组成功");
  },
  fail(res) {
    console.log(`设置用户分组失败, ${res.errMsg}`)
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| groupId | string | 是 |  | 1.17.0 | 分组唯一 id。开发者自定义，确保唯一性 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："setUserGroup:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："setUserGroup:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21000 | Invalid Session. |  |  |
| 20000 | groupId is empty |  |  |

## 相关课程
[游戏排行分组教程](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/relationship-chain/ranking/challenge-to-ranking)

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/tt-set-user-group) / [本地体验路径](tt-set-user-group)
