---
title: "FileSystemManager.statSync"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/file-system-manager-stat-sync
update_time: 2025-06-05
---

const fileSystemManager = tt.getFileSystemManager();
tt.chooseImage({
success(res) {
const tempFile = res.tempFilePaths[0];
try {
const stat = fileSystemManager.statSync(tempFile);
console.log("是否是目录:", res.stat.isDirectory());
console.log("是否是文件:", res.stat.isFile());
} catch (err) {
console.log("调用失败", err);
}
},
});

FileSystemManager.statSync(path, recursive)

const fileSystemManager = tt.getFileSystemManager();
const stats = fs.statSync(`ttfile://user`, true)
if (Array.isArray(stats)) {
stats.forEach(({ path, stat }) => {
console.log(path, stat.isDirectory())
})
} else {
console.log(stats.isDirectory())
}

## 语法

```js
FileSystemManager.statSync(path, recursive)
```
基础库 1.15.0 开始支持本方法，这是一个**同步**方法。
获取文件 Stats 对象。

## 示例代码
【代码示例 1】查询单一文件 stat：
```js
const fileSystemManager = tt.getFileSystemManager();
tt.chooseImage({
  success(res) {
    const tempFile = res.tempFilePaths[0];
    try {
      const stat = fileSystemManager.statSync(tempFile);
      console.log("是否是目录:", res.stat.isDirectory());
      console.log("是否是文件:", res.stat.isFile());
    } catch (err) {
      console.log("调用失败", err);
    }
  },
});
```
【代码示例 2】递归查询用户目录 stat：
```js
const fileSystemManager = tt.getFileSystemManager();
const stats = fs.statSync(`ttfile://user`, true)
if (Array.isArray(stats)) {
  stats.forEach(({ path, stat }) => {
    console.log(path, stat.isDirectory())
  })
} else {
  console.log(stats.isDirectory())
}
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| path | string | 是 |  | 1.15.0 | 文件/目录路径 |
| recursive | boolean | 否 |  | 3.1.0 | 是否递归获取目录下的每个文件的 Stat 信息 |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| stats | Stats \| array | StatItem[] \| [Stats](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/file/stats/stats)。当查询结果是多个时，为数组类型；当结果唯一时，为 Stat 对象类型  StatItem 是个 object 类型，属性如下：  \|  \|  \|  \|  \| \| --- \| --- \| --- \| --- \| \| 属性名 \| 类型 \| 说明 \| 最低支持版本 \| \| path \| string \| 以传参 path 为根路径的相对路径 \| 3.1.0 \| \| stat \| [Stats](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/file/stats/stats) \| 与路径相对应的 Stat 对象 \| 3.1.0 \| |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 10401 | error stack |  |  |
| 21101 | permission denied, $apiName $dirPath |  |  |
| 21102 | no such file or directory, $apiName $dirPath |  |  |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/file-system-manager-stat-sync) / [本地体验路径](file-system-manager-stat-sync)
