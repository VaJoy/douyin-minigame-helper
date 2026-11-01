---
title: "FileSystemManager"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/file-system-manager
update_time: 2025-08-05
---

> 基础库版本 1.15.0 开始支持。
文件管理器，[tt.getFileSystemManager](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/api/file/tt-get-file-system-manager/) 的返回值。
## 属性说明

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| access | Function | 判断文件/目录是否存在 |
| accessSync | Function | 同步判断文件/目录是否存在 |
| saveFile | Function | 保存临时文件到本地。此接口会移动临时文件，因此调用成功后，tempFilePath 将不可用 |
| saveFileSync | Function | 同步保存临时文件到本地。此接口会移动临时文件，因此调用成功后，tempFilePath 将不可用 |
| getSavedFileList | Function | 获取该小程序下已保存的本地缓存文件列表 |
| removeSavedFile | Function | 删除该小程序下已保存的本地缓存文件 |
| copyFile | Function | 复制文件 |
| copyFileSync | Function | 同步复制文件 |
| getFileInfo | Function | 获取该小程序下的 本地临时文件 或 本地缓存文件 信息 |
| mkdir | Function | 创建目录 |
| mkdirSync | Function | 同步创建目录 |
| readdir | Function | 读取目录内文件列表 |
| readdirSync | Function | 同步读取目录内文件列表 |
| readFile | Function | 读取本地文件内容 |
| readFileSync | Function | 同步读取本地文件内容 |
| rename | Function | 重命名文件，可以把文件从 oldPath 移动到 newPath |
| renameSync | Function | 同步重命名文件，可以把文件从 oldPath 移动到 newPath |
| rmdir | Function | 删除目录 |
| rmdirSync | Function | 同步删除目录 |
| stat | Function | 获取文件 Stats 对象 |
| statSync | Function | 同步获取文件 Stats 对象 |
| unlink | Function | 删除文件 |
| unlinkSync | Function | 同步删除文件 |
| unzip | Function | 解压文件 |
| writeFile | Function | 写文件 |
| writeFileSync | Function | 同步写文件 |
| readZipEntry | Function | 读取压缩包内的文件 |
| truncate | Function | 对文件内容进行截断操作 |
| truncateSync | Function | 同步对对文件内容进行截断操作 |
| appendFile | Function | 在文件结尾追加内容 |
| appendFileSync | Function | 同步在文件结尾追加内容 |
| open | Function | 打开文件，返回文件描述符 |
| openSync | Function | 同步打开文件，返回文件描述符 |
| close | Function | 关闭文件 |
| closeSync | Function | 同步关闭文件 |
| read | Function | 读取文件 |
| readSync | Function | 同步读取文件 |
| write | Function | 写入文件 |
| writeSync | Function | 同步写入文件 |
| fstat | Function | 获取文件的状态信息 |
| fstatSync | Function | 同步获取文件的状态信息 |
| ftruncate | Function | 对文件内容进行截断操作 |
| ftruncateSync | Function | 同步对文件内容进行截断操作 |
| readCompressedFile | Function | 读取指定压缩类型的本地文件内容 |
| readCompressedFileSync | Function | 同步读取指定压缩类型的本地文件内容 |
