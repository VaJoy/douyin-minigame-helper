---
title: "tt.loadSubpackage"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/subpackages/tt-loadsubpackage
update_time: 2024-07-24
---

> 基础库 1.88.0 开始支持本方法，低版本需做[兼容处理](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/basic-library/compatibility-description/)。
触发分包加载下载与加载（如果分包指定的是一个目录，则自动加载目录下的 game.js, 如果分包指定的是一个 js 文件，则自动加载该 js 文件），详见[分包加载](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/subpackages/basic)。
## 语法
```text
tt.loadSubpackage(options)
```
## 参数说明
object 类型，属性如下：

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- | --- |
| name | string |  | 是 | 分包的名字，可以填 game.json 中配置的 name 或者 root 值 | 1.88.0 |
| success | Function |  | 否 | 接口调用成功的回调函数 | 1.88.0 |
| fail | Function |  | 否 | 接口调用失败的回调函数 | 1.88.0 |
| complete | Function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） | 1.88.0 |

## 回调成功
object 类型，属性如下：

| 属性 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| errMsg | string | "loadSubpackage: ok" | 1.88.0 |

## 回调失败
object 类型，属性如下：

| 属性 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| errMsg | string | "loadSubpackage: fail" + 详细错误信息 | 1.88.0 |

## 返回值
[LoadSubpackageTask](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/subpackages/LoadSubpackageTask) 加载分包任务实例，用于获取分包加载状态。
## 代码示例
```text
const loadTask = tt.loadSubpackage({
name: 'stage1',
success: function(res) {
console.log('success errMsg: ' + res.errMsg);
},
fail: function(res) {
console.log('fail errMsg: ' + res.errMsg);
}
});
loadTask.onProgressUpdate(res => {
console.log('下载进度', res.progress);
console.log('已经下载的数据长度', res.totalBytesWritten);
console.log('预期需要下载的数据总长度', res.totalBytesExpectedToWrite);
});
```
## Bug & Tip
无
