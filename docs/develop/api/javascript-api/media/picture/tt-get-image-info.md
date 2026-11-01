---
title: "tt.getImageInfo"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/picture/tt-get-image-info
update_time: 2024-09-26
---

## 语法

```js
tt.getImageInfo(src)
```
基础库 1.10.0 开始支持本方法，这是一个**异步**方法。
获取图片信息。

## 示例代码
```js
tt.chooseImage({
  success(res) {
    tt.getImageInfo({
      src: res.tempFilePaths[0],
      success(res) {
        console.log(res.width, res.height);
      },
    });
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| src | string | 是 |  | 1.10.0 | 图片路径，可以是相对路径、临时文件路径或存储文件路径、网络图片 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **path**（string）：返回图片的本地路径，若为网络图片则该 API 首先会下载图片再返回下载到本地后的临时路径 - **type**（string）：图片格式 - **width**（number）：图片宽度(单位: px) - **height**（number）：图片高度(单位: px) - **errMsg**（string）："getImageInfo:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："getImageInfo:fail" + 详细错误信息 |

## 前置条件
如果要获取网络图片的信息，需要预先在开发者平台**配置 download 的域名白名单。**

具体步骤为：[开发者平台](https://developer.open-douyin.com/console?type=2) -> 选择目标小游戏 -> 开发设置 -> 服务器域名 -> downloadFile 合法域名。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/media/picture/tt-get-image-info) / [本地体验路径](tt-get-image-info)
