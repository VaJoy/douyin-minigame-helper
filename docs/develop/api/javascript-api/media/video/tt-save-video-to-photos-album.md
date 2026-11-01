---
title: "tt.saveVideoToPhotosAlbum"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/video/tt-save-video-to-photos-album
update_time: 2024-08-15
---

## 语法

```js
tt.saveVideoToPhotosAlbum(filePath)
```
基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
保存视频到系统相册。

## 示例代码
```js
tt.chooseVideo({
  sourceType: ["camera"],
  success(res) {
    const filePath = res.tempFilePath;
    tt.saveVideoToPhotosAlbum({
      filePath,
      success(res) {
        tt.showToast({
          title: `saveVideoToPhotosAlbum 调用成功`,
        });
      },
      fail(res) {
        tt.showToast({
          title: `saveVideoToPhotosAlbum 调用失败`,
        });
      },
    });
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| filePath | string | 是 |  | 1.0.0 | 视频文件路径。**不支持网络地址**， 网络资源需要先通过 [tt.downloadFile](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/network/download/tt-download-file) 下载 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："saveVideoToPhotosAlbum:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："saveVideoToPhotosAlbum:fail" + 详细错误信息 |

## 前置条件
该 API 需要用户授权方可调用，详细信息可参考[用户授权](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/user-information/authorization/authorization)。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/system/system-information/tt-save-video-to-photos-album) / [本地体验路径](tt-save-video-to-photos-album)
