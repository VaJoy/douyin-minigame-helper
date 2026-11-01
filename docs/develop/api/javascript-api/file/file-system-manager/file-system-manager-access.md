---
title: "FileSystemManager.access"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/file-system-manager-access
update_time: 2024-07-24
---

## 语法

```js
FileSystemManager.access(path)
```
基础库 1.15.0 开始支持本方法，这是一个**异步**方法。
判断文件/目录是否存在。

## 示例代码
【代码示例1】判断临时目录路径是否存在
```js
const fileSystemManager = tt.getFileSystemManager();
const path = `ttfile://temp/some-path`; // 判断的地址

fileSystemManager.access({
  path,
  success() {
    console.log(`${path} 地址存在`);
  },
  fail(res) {
    console.log(`${path} 地址不存在或其他错误`, res.errMsg);
  }
})
```
【代码实例2】判断用户目录下路径是否存在
```js
const fileSystemManager = tt.getFileSystemManager();
const path = `ttfile://user/some-path`; // 判断的地址

fileSystemManager.access({
  path,
  success() {
    console.log(`${path} 地址存在`);
  },
  fail(res) {
    console.log(`${path} 地址不存在或其他错误`, res.errMsg);
  }
})
```
【代码示例3】判断包内路径是否存在
```js
const fileSystemManager = tt.getFileSystemManager();
// 包内路径不需要 `ttfile://` 协议
const path = "app.js"; // 判断的地址

fileSystemManager.access({
  path,
  success() {
    console.log(`${path} 地址存在`);
  },
  fail(res) {
    console.log(`${path} 地址不存在或其他错误`, res.errMsg);
  }
})
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| path | string | 是 |  | 1.15.0 | 要判断是否存在的文件/目录路径 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："access:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："access:fail " + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 10401 | error stack |  |  |
| 21101 | permission denied, $filePath |  |  |
| 21102 | no such file or directory, $filePath |  |  |
| 20000 | params $paramName is required |  |  |
| 20000 | params $paramName type is not $paramType type |  |  |
| 20000 | $paramName is invalid |  |  |
| 20001 | invalid param |  |  |
| 20000 | internal error |  |  |

## 注意事项
access 可以用于 用户目录(ttfile://user) 临时目录(ttfile://temp) 以及 包内目录(访问包内目录不需要加额外协议头)

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/file/file-system-manager/file-system-manager-access) / [本地体验路径](file-system-manager-access)
