---
title: "tt.loadFont"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/drawing/font/tt-load-font
update_time: 2024-07-24
---

## 语法

```js
tt.loadFont(path)
```
基础库 1.23.0 开始支持本方法，这是一个**同步**方法。
加载自定义字体文件。

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| path | string | 是 |  | 1.23.0 | 字体文件路径，可以是代码包文件路径，也可以是 ttfile:// 协议的本地文件路径 |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| family | string | 字体 family 值。加载失败时返回null |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/drawing/font/tt-load-font) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-load-font%22%7D) / [在线试玩](https://developer.open-douyin.com/docs/playground?project_id=tma-demo&version=1.0.0.10&entry=tt-load-font&codes_select=js&type=mini-game&sdk_version=1.0.0.205)
