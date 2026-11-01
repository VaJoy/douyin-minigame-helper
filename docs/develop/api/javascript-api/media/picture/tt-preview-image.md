---
title: "tt.previewImage"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/picture/tt-preview-image
update_time: 2024-08-15
---

## 语法

```js
tt.previewImage(current, urls)
```
基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
预览一组图片。

## 示例代码
```js
tt.previewImage({
  urls: ["image1", "image2", "image3"],
  current: "image3",
  success(res) {
    console.log(`previewImage调用成功`);
  },
  fail(res) {
    console.log(`previewImage调用失败`);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| current | string | 否 | urls[0] 的内容 | 1.0.0 | 当前显示图片的链接，不填则默认为 urls 中的第一张 |
| urls | Array<string> | 是 |  | 1.0.0 | 需要预览的图片地址列表 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："previewImage:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："previewImage:fail" + 详细错误信息 |

## 注意事项
- 抖音不支持预览图片保存功能。
- 当 urls 中存在多个相同的图片地址，预览时会选择 current 地址对应的第一张图片进行展示，可通过给图片地址增加 query 或 hash 值避免地址重复。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/media/picture/tt-preview-image) / [本地体验路径](tt-preview-image)
