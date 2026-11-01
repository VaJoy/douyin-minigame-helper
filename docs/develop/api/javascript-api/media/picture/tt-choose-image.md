---
title: "tt.chooseImage"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/picture/tt-choose-image
update_time: 2024-08-15
---

## 语法

```js
tt.chooseImage(count, sourceType)
```
基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
从系统相册中选择图片，或使用相机拍摄图片，选取成功后将存入本地临时文件，并在 success 回调中返回相应路径列表。

## 示例代码
```js
tt.chooseImage({
  sourceType: ["album"],
  count: 3,
  success(res) {
    this.setData({
      images: res.tempFilePaths,
    });
  },
  fail(res) {
    console.log(`chooseImage调用失败`);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| count | number | 否 | 9 | 1.0.0 | 最多可以选择的图片数量，拍照时此选项无效 |
| sourceType | Array<string> | 否 | ["album", "camera"] | 1.0.0 | 指定图片来源，album 从相册选图，camera 使用相机，默认二者都有 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **tempFiles**（Array<Object>）：图片对象数组，对象结构详见下表 - **tempFilePaths**（Array<string>）：图片的本地文件路径列表 - **errMsg**（string）："chooseImage:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："chooseImage:fail" + 详细错误信息  回调失败执行时机有：手动取消、参数错误，没有授权、文件路径为空、文件路径不存在。 |

## 注意事项
- Android 上所选图片总大小不能超过 **180M**。
- 暂不支持sizeType参数。
- 手动取消也会触发失败回调，回调参数为 chooseImage:fail cancel，可以通过判断详细错误信息区分取消和其他错误。

## 前置条件
该 API 需要用户授权方可调用，详细信息可参考[用户授权](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/api/other/user-authorization)。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/media/picture/tt-choose-image) / [本地体验路径](tt-choose-image)
