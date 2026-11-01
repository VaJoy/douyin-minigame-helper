---
title: "FollowButton.onTap"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/follow/follow-tt/follow-button/on-tap
update_time: 2024-09-25
---

#### errCode 取值

| 值 | 说明 |
| --- | --- |
| 0 | 关注成功 |
| 1 | 关闭弹窗，取消关注 |
| 2 | 关注失败，接口错误 |
| 3 | 关注失败，网络错误 |

## 语法

```js
FollowButton.onTap(callback)
```
基础库 1.19.0 开始支持本方法，这是一个**同步**方法。
监听按钮点击事件。当按钮时，唤起关注弹层，弹层被关闭时触发用户回调。

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

followButton.onTap((res) => {
  const { buttonId, errCode, errMsg } = res;
  tt.showModal({
    title: "关注",
    content: `关注按钮id：${buttonId}, errCode: ${errCode}, 详细信息：${errMsg}`,
  });
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.19.0 | 回调函数  **对象字段** - **res**（Object）：object 类型，属性如下： |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
