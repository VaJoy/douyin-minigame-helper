---
title: "tt.onFavoriteStateChange"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/favorite/tt-on-favorite-state-change
update_time: 2024-07-31
---

## 语法

```js
tt.onFavoriteStateChange(callback)
```
基础库 1.87.0 开始支持本方法，这是一个**同步**方法。
监听用户点击右上角菜单中的【收藏】按钮时触发的事件。

## 示例代码
```js
tt.onFavoriteStateChange((isFavorited) => {
  if (isFavorited) {
    console.log("收藏成功");
  } else {
    console.log("收藏失败");
  }
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 否 |  | 1.87.0 | 收藏后的回调函数  **对象字段** - **args_0**（Object）：object类型，说明如下： |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 注意事项
当网络波动或者其他情况可能会出现收藏失败。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
