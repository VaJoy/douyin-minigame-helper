---
title: "tt.saveImageToPhotosAlbum"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/picture/tt-save-image-to-photos-album
update_time: 2024-08-15
---

## 语法

```js
tt.saveImageToPhotosAlbum(filePath)
```
基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
保存图片到系统相册。

## 示例代码
```js
tt.saveImageToPhotosAlbum({
  filePath: "somepath",
  success(res) {
    console.log(`saveImageToPhotosAlbum调用成功`);
  },
  fail(res) {
    console.log(`saveImageToPhotosAlbum调用失败`);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| filePath | string | 是 |  | 1.0.0 | 图片文件路径，可以是临时文件路径(如调用 [tt.downloadFile](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/network/download/tt-download-file) 返回的路径），也可以是永久文件路径，**不支持网络路径** |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："saveImageToPhotosAlbum:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："saveImageToPhotosAlbum:fail" + 详细错误信息 |

## 注意事项
手动取消也会触发失败回调，错误信息为 saveImageToPhotosAlbum:fail cancel，可以通过判断详细错误信息区分取消和其他错误。

## 前置条件
该 API 需要用户授权方可调用，详细信息可参考[用户授权](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/user-information/authorization/authorization)，可在 [tt.authorize](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/user-information/authorization/tt-authorize) 中查看相关错误码信息。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/media/picture/tt-save-image-to-photos-album) / [本地体验路径](tt-save-image-to-photos-album)
