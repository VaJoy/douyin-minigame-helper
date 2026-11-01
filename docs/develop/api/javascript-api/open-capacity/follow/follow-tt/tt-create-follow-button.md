---
title: "tt.createFollowButton"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/follow/follow-tt/tt-create-follow-button
update_time: 2024-09-25
---

## 语法

```js
tt.createFollowButton(options)
```
基础库 1.19.0 开始支持本方法，这是一个**同步**方法。
创建关注头条号按钮。

## 示例代码
```js
// 创建关注头条号按钮
const btn = tt.createFollowButton({
  type: "image",
  image: "images/follow_btn.png",
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
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| options | Object | 否 |  | 1.19.0 | object 类型，属性如下：  **对象字段** - **type**（string）：按钮的类型，取值 image 或 text。image 对应图片按钮，text 对应文本按钮 - **image**（string）：按钮的背景图片，type 为 image 时必填。仅支持本地图片，目录包括代码包目录、临时文件目录和本地用户目录 - **style**（Object）：按钮的样式 |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| FollowButton | Object | [FollowButton](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/follow/follow-tt/follow-button/follow-button) 对象实例 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21101 | /s |  |  |
| 10401 | internal error |  |  |
| 10301 | feature is not supported in app |  |  |
| 20000 | invalid param |  |  |
| 21000 | invalid param |  |  |
| 21000 | /s |  |  |

## 使用限制
只支持在今日头条 App 上使用

## 前置条件
使用该 API 前需先在平台绑定账号，审核通过才可以使用接口关注账号。

具体路径：【开发者平台】-【基础设置】-【关联设置】- 【头条号绑定】

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
