---
title: "tt.createImage"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/drawing/picture/tt-create-image
update_time: 2024-11-27
---

基础库 1.31.0 开始支持本方法，这是一个**同步**方法。
创建一个图片对象。

## 示例代码

【代码示例1】：结合 cocos 引擎的解决方案，cocos 3.x 版本可能不适配。

```js
export const headImgExt = ".head";
/**  * 新版本的cocos加载头像的时候，需要先下载，但是在字节小游戏平台下，会有跨域的问题。这个方法需要在进入游戏后加载前调用
* 加载头像的用法:cc.assetManager.loadRemote(url,{ext:headImgExt},(err,texture)=>{});
* 所有不想下载直接使用的图像都可以加上{ext:headImgExt}来使用  */
export function registerHeadImgLoader() {
    cc.assetManager.downloader.register(headImgExt, (content, options, onComplete) => {
        onComplete(null, content);
    });
    cc.assetManager.parser.register(headImgExt, downloadDomImage);
    function createTexture(id, data, options, onComplete) {
        let out = null,
            err = null;
        try {
            out = new cc.Texture2D();
            out._uuid = id;
            out._nativeUrl = id;
            out._nativeAsset = data;
        } catch (e) {
            err = e;
        }
        onComplete && onComplete(err, out);
    } (cc.assetManager as any).factory.register(headImgExt, createTexture);
}
function downloadDomImage(url, options, onComplete) {
    const img = new Image();
    if (window.location.protocol !== 'file:') {
        img.crossOrigin = 'anonymous';
    }
    function loadCallback() {
        img.removeEventListener('load', loadCallback);
        img.removeEventListener('error', errorCallback);
        if (onComplete) {
            onComplete(null, img);
        }
    }
    function errorCallback() {
        img.removeEventListener('load', loadCallback);
        img.removeEventListener('error', errorCallback);
        if (onComplete) {
            onComplete(new Error(url));
        }
    }
    img.addEventListener('load', loadCallback);
    img.addEventListener('error', errorCallback);
    img.src = url;
    return img;
}
```

【代码示例 2】：结合 Laya 引擎的解决方案

```js
//this.localAvatarImage : Laya.Image
const localImage = new Image()
localImage.src = localPlayer.userInfo.avatarUrl;
localImage.onload = () => {
    const scale = localImage.width / this.remoteAvatarImage.width
    const t2d = new Laya.Texture2D(localImage.width / scale, localImage.height / scale, (Laya as any).TextureFormat.R8G8B8A8)
    this.localAvatarImage.graphics.drawImage(new Laya.Texture(t2d), 0, (this.localAvatarImage.height - localImage.height / scale) / 2)
    t2d.loadImageSource(localImage)
}
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| Image | Object | object类型，属性如下：  **对象字段** - **src**（string）：图片的 URL，base64 内容，或者 ArrayBuffer 数据 - **width**（number）：图片的真实宽度 - **height**（number）：图片的真实高度 - **addEventListener**（Function）：添加事件监听器 - **removeEventListener**（Function）：移除事件监听器 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 注意事项
1. 图片的 src 可以接受网络地址，本地 ttfile:// 协议地址，base64 格式，以及 ArrayBuffer 格式的数据内容。

2. 通过该 API 直接创建图片显示的方法不需要配置图片白名单。

3. 在开放数据域中，通过该方法创建的图片只能显示与自己头像地址,即 tt.getUserInfo 返回的 avatarUrl 相同主机名的内容。

4. 如果开发者在开发时使用了引擎，部分引擎所实现图片渲染的能力可能需要先进行图片下载，如果不想配置过多的图片白名单，可以通过改写引擎的图片能力解决该问题，具体请参考代码示例。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/drawing/picture/tt-create-image) / [本地体验路径](tt-create-image) / [在线试玩](https://developer.open-douyin.com/docs/playground?project_id=tma-demo&version=1.0.0.10&entry=tt-create-image&codes_select=js&type=mini-game&sdk_version=1.0.0.205)