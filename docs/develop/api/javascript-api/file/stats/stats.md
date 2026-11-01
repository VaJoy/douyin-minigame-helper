---
title: "Stats"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/stats/stats
update_time: 2025-02-17
---

> 基础库 1.15.0 开始支持本对象。
描述文件状态的对象。
## 属性

| 名称 | 数据类型 | 描述 |
| --- | --- | --- |
| mode | string | 文件的类型和存取的权限，对应 `POSIX` `stat.st_mode` |
| size | number | 文件大小，单位：`B`，对应 `POSIX` `stat.st_size` |
| lastAccessedTime | number | 文件最近一次被存取或被执行的时间，UNIX 时间戳，对应 `POSIX` `stat.st_atime` |
| lastModifiedTime | number | 文件最后一次被修改的时间，UNIX 时间戳，对应 `POSIX` `stat.st_mtime` |

## 方法

| 名称 | 参数 | 返回值 | 描述 |
| --- | --- | --- | --- |
| [isDirectory](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/file/stats/stats-is-directory) | 无 | boolean | 判断当前文件是否一个目录 |
| [isFile](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/file/stats/stats-is-file) | 无 | boolean | 判断当前文件是否一个普通文件 |

## 代码示例

```js
const fs = getFileSystemManager();
const stat = fs.statSync("./path");

console.log("mode:", stat.mode);
console.log("size:", stat.size);
console.log("lastAccessedTime:", stat.lastAccessedTime);
console.log("lastModifiedTime:", stat.lastModifiedTime);

console.log("isDirectory:", stat.isDirectory());
console.log("isFile:", stat.isFile());
```
