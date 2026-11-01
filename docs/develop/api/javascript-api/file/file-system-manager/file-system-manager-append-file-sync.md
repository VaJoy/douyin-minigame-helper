---
title: "FileSystemManager.appendFileSync"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/file-system-manager-append-file-sync
update_time: 2024-07-24
---

## 语法

```js
FileSystemManager.appendFileSync(filePath, data, encoding)
```
基础库 3.1.0 开始支持本方法，这是一个**同步**方法。
在文件结尾追加内容，文件不存在时会新建。只有用户目录ttfile://user下的文件可以追加。

## 示例代码
```js
const fs = tt.getFileSystemManager();

fs.appendFile({
  filePath: `ttfile://user/example.txt`,
  data: "Hello World",
  encoding: "utf8",
  success(res) {
    console.log(res)
  },
  fail(res) {
    console.error(res)
  },
})

// 同步接口
try {
  fs.appendFileSync(`ttfile://user/example.txt`, "Hello World", "utf8")
} catch (e) {
  console.error(e)
}
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| filePath | string | 是 |  | 3.1.0 | 要追加内容的文件路径，必须是用户目录，以 ttfile://user 开头 |
| data | string | 是 |  | 3.1.0 | 要写入的文本或二进制数据。支持 string 和 arraybuffer 类型 |
| encoding | number | 是 | utf-8 | 3.1.0 | 指定写入文件的字符编码  **可选值：** utf-8=

<a href="https://www.rfc-editor.org/rfc/rfc3629.html#section-4" target="_blank" rel="nofollow" class="syl-link" elementtiming="element-timing">RFC 3629, Section 4</a>

；ascii=

<a href="https://developer.mozilla.org/zh-CN/docs/Glossary/ASCII" target="_blank" rel="nofollow" class="syl-link" elementtiming="element-timing">MDN</a>

；base64=

<a href="https://tools.ietf.org/html/rfc4648#section-5" target="_blank" rel="nofollow" class="syl-link" elementtiming="element-timing">RFC 4648, Section 5</a>

；binary=

ISO-8859-1

；hex=

十六进制

；ucs2=

以小端序读取

；ucs-2=

以小端序读取

；utf16le=

以小端序读取

；utf-16le=

以小端序读取

；utf8=

<a href="https://www.rfc-editor.org/rfc/rfc3629.html#section-4" target="_blank" rel="nofollow" class="syl-link" elementtiming="element-timing">RFC 3629, Section 4</a>

；latin1=

ISO-8859-1

 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | appendFile:fail filePath is invalid |  |  |
| 21101 | appendFile:fail permission denied, appendFile %s |  |  |
| 21102 | appendFile:fail no such file or directory, appendFile %s |  |  |
| 21103 | appendFile:fail user dir saved file size limit exceeded |  |  |
| 21104 | appendFile:fail operation not permitted, appendFile %s |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/file/file-system-manager/file-system-manager-append-file-sync) / [本地体验路径](file-system-manager-append-file-sync)