---
title: "tt.getFileSystemManager"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/tt-get-file-system-manager
update_time: 2024-07-24
---

基础库 1.15.0 开始支持本方法，这是一个**同步**方法。
获取全局唯一的文件管理器。

## 示例代码

【代码示例1】

```js
const fileSystemManager = tt.getFileSystemManager();
```

【代码示例2】访问 包目录不需要填写前缀, 例如读取包内 app.js 文件

```js
const fileSystemManager = tt.getFileSystemManager();

fileSystemManager.readFile({
  filePath: "app.js",
  encoding: "utf8",
  success(res) {
    // app.js 文件内容
    console.log(res.data);
  },
  fail(res) {
    //
    console.error("读取失败", res.errMsg);
  },
});
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| FileSystemManager | Object | 文件管理器，[FileSystemManager](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/file/file-system-manager/file-system-manager) 类型。  ### 目录说明  小游戏文件系统分为以下 3 个部分  ### 用户目录  以 ttfile://user 开头, 开发者拥有读写权限  ### 临时目录  以 ttfile://temp 开头, 开发者拥有读权限, 无写权限  ### 包目录  小游戏包体目录, 开发者拥有读权限, 无写权限  **注意** 除 access、accessSync、readFile、readFileSync 外其他 API 均不可以访问包目录 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 注意事项
- 小游戏支持 200M 的本地文件空间存储。
- 小游戏的本地空间储存逻辑上为以 appid 为纬度，不区分预览版，正式版。

## 公告
从基础库 2.21 版本（包含）开始， 小游戏对本地空间上限进行了调整。开发者通过文件接口能够保存的文件大小上限由之前的 50M 现在变更为 200M。开发者可以根据小游戏基础库版本做适配，或者在发布时设置最低基础库版本。目前，2.21 版本已经覆盖大部分用户

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/file/tt-get-file-system-manager) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-get-file-system-manager%22%7D)