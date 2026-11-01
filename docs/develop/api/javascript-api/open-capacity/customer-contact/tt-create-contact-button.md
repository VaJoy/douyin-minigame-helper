---
title: "tt.createContactButton"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/customer-contact/tt-create-contact-button
update_time: 2025-10-10
---

> 基础库 1.55.0 开始支持本方法，低版本需做[兼容处理](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/basic-library/compatibility-description/)。
创建客服按钮。
详细说明请参考 [小游戏客服介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/user-ops/user-service/bytehi-im)

---

## 返回
返回一个 [ContactButton](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/customer-contact/contact-button) 对象

---

## 参数
Object 类型，属性如下：

| 属性 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| type | "image" \| "text" |  | 是 | 按钮的类型，取值 image 或 text。image 对应图片按钮，text 对应文本按钮 |
| image | string |  | 否 | 按钮的背景图片，type 为 image 时必填。仅支持本地图片，目录包括代码包目录、临时文件目录和本地用户目录 |
| text | string | 更多游戏 | 否 | 按钮上的文本内容， type 为 text 时有效 |
| style | object |  | 是 | 按钮的样式 |

#### style 参数说明

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| left | number |  | 是 | 左上角横坐标 |
| top | number |  | 是 | 左上角纵坐标 |
| width | number |  | 是 | 宽度 |
| height | number |  | 是 | 高度 |
| backgroundColor | string |  | 是 | 背景颜色 |
| borderColor | string |  | 是 | 边框颜色 |
| borderWidth | number |  | 是 | 边框宽度 |
| borderRadius | number |  | 是 | 边框圆角 |
| textAlign | "left" \| "center" \| "right" |  | 是 | 文本的水平居中方式 |
| fontSize | number |  | 是 | 字号 |
| lineHeight | number |  | 是 | 文本的行高 |
| textColor | string |  | 是 | 文本颜色 |

#### style.textAlign 属性合法值

| 值 | 说明 |
| --- | --- |
| left | 居左 |
| center | 居中 |
| right | 居右 |

---

## 返回
返回一个 ContactButton 对象

---

## 示例

```js
const button = tt.createContactButton({
  type: "image", // image | text
  image: "./test.jpg",
  style: {
    left: 20,
    top: 40,
    width: 150,
    height: 150,
    lineHeight: 40,
    backgroundColor: "#ffffff",
    textAlign: "center",
    fontSize: 16,
    borderRadius: 4,
    borderColor: "#ffffff",
    borderWidth: 1,
    textColor: "#ffffff",
  },
  success(res) {
    console.log("create success", res);
  },
  fail(res) {
    console.log("create fail", res);
  },
  complete(res) {
    console.log("create complete", res);
  },
});

// 点击事件
function handleClick() {
  console.log("点击客服按钮");
}

button.onTap(handleClick); // 监听点击事件
button.offTap(handleClick); // 取消监听点击事件

button.show(); // 显示按钮
button.hide(); // 隐藏按钮

// 错误处理
function handleError(res) {
  console.log(res.errMsg);
}

button.onError(handleError); // 监听错误
button.offError(handleError); //取消监听错误

button.destroy(); // 销毁按钮
```

## Bug&Tip
- Bug： 番茄小说和番茄畅听暂不支持客服能力，预计 2022 年 3.31 号可使用。
- Tip： 番茄小说和番茄畅听端内购游戏强制接入客服消息的限制 3.31 前可以豁免。建议开发者需要的情况可以设置一个客服按钮，点击后出现弹框，文字引导下 ：如果您对充值有问题，可以点击「右上角三个点」-「反馈与帮助」-「意见建议」选择「充值问题」进行反馈，我们会第一时间对您的问题进行跟踪处理。
