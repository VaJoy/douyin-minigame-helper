---
title: "tt.scanCode"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/device/scan-code/tt-scan-code
update_time: 2024-09-03
---

基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
扫描二维码并返回扫描结果。

## 示例代码
```js
tt.scanCode({
  success(res) {
    console.log(`${res.result}`);
  },
  fail(res) {
    console.log(`scanCode调用失败`);
  },
});
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **result**（string）：所扫码的内容 - **errMsg**（string）："scanCode:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："scanCode:fail" + 详细错误信息 |

## 注意事项
- 暂不支持 onlyFromCamera 和 scanType。
- 返回值不支持 scanType, charSet, path, rawData。
- 对于包含 GBK 编码内容的二维码扫描时会有乱码。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/device/scan-code/tt-scan-code) / [本地体验路径](tt-scan-code)
