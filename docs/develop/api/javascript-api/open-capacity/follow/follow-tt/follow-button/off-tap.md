---
title: "FollowButton.offTap"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/follow/follow-tt/follow-button/off-tap
update_time: 2024-09-25
---

## 语法

```js
FollowButton.offTap(callback)
```
基础库 1.19.0 开始支持本方法，这是一个**同步**方法。
移除指定的按钮点击监听事件。

## 示例代码
```js
const followButton = tt.createFollowButton({
  type: "image",
  image: "images/follow-button.png",
  style: {
    left: 20,
    top: 40,
    width: 150,
    height: 40,
    lineHeight: 40,
    backgroundColor: "#ff0000",
    textColor: "#ffffff",
    textAlign: "center",
    fontSize: 16,
    borderRadius: 4,
    borderWidth: 1,
    borderColor: "#ff0000",
  },
});

function onTap(res) {
  const { buttonId, errCode, errMsg } = res;
  tt.showModal({
    title: "关注",
    content: `关注按钮id：${buttonId}, errCode: ${errCode}, 详细信息：${errMsg}`,
  });
}
followButton.onTap(onTap);
followButton.offTap(onTap);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 否 |  | 1.19.0 | 将要移除的目标回调事件 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
