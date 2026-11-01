---
title: "FileSystemManager.appendFile"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/file-system-manager-append
update_time: 2024-07-24
---

## 语法

```js
FileSystemManager.appendFile(encoding, data, filePath)
```
基础库 3.1.0 开始支持本方法，这是一个**异步**方法。
在文件结尾追加内容，文件不存在时会新建。只有用户目录 ttfile://user 下的文件可以追加。

## 示例代码
```js
const fs = tt.getFileSystemManager()

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
| encoding | number | 否 | utf-8 | 3.1.0 | 指定写入文件的字符编码  **可选值：** utf-8=

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
| data | string | 是 |  | 3.1.0 | 要写入的文本或二进制数据。支持 string 和 arraybuffer 类型 |
| filePath | string | 是 |  | 3.1.0 | 要追加内容的文件路径，必须是用户目录，以 ttfile://user 开头 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："FileSystemManager.appendFile:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："FileSystemManager.appendFile:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 10401 | error stack |  |  |
| 21101 | permission denied, $filePath |  |  |
| 21102 | no such file or directory, $filePath |  |  |
| 21103 | user dir saved file size limit exceeded |  |  |
| 21104 | operation not permitted, $apiName $filePath |  |  |
| 20000 | data is invalid |  |  |
| 20001 | data is invalid |  |  |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/file/file-system-manager/file-system-manager-append-file) / [本地体验路径](file-system-manager-append-file)