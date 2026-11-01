---
title: "FollowButton.show"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/follow/follow-tt/follow-button/show
update_time: 2024-09-25
---

基础库 1.19.0 开始支持本方法，这是一个**同步**方法。
显示关注按钮。

## 示例代码
2s 后显示关注按钮。
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
followButton.hide();

setTimeout(() => followButton.show(), 2000);
```

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
