---
title: "FileSystemManager.getSavedFileList"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/file-system-manager-get-saved-file-list
update_time: 2025-06-05
---

FileSystemManager.getSavedFileList(options)

const fileSystemManager = getFileSystemManager();

fileSystemManager.getSavedFileList({
success(res) {
res.fileList.forEach((item) => {
console.log(item.filePath, item.createTime, item.size);
});
},
fail(res) {
console.log("获取失败", res.errMsg);
},
});

基础库 1.15.0 开始支持本方法，这是一个**异步**方法。
获取该小游戏下用户目录文件列表, 用户目录以 ttfile://user 开头。

## 示例代码
```js
const fileSystemManager = getFileSystemManager();

fileSystemManager.getSavedFileList({
  success(res) {
    res.fileList.forEach((item) => {
      console.log(item.filePath, item.createTime, item.size);
    });
  },
  fail(res) {
    console.log("获取失败", res.errMsg);
  },
});
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **fileList**（Array<Object>）：文件数组，每一项是一个 FileItem - **errMsg**（string）："getSavedFileList:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："getSavedFileList:fail" + 详细错误信息 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/file/file-system-manager/file-system-manager-get-saved-file-list) / [本地体验路径](file-system-manager-get-saved-file-list)
