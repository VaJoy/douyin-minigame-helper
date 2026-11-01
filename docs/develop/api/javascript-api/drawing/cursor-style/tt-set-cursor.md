---
title: "tt.setCursor"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/drawing/cursor-style/tt-set-cursor
update_time: 2025-01-03
---

## 语法

```js
tt.setCursor(path, x, y)
```
基础库 3.54.0 开始支持本方法，这是一个**同步**方法。
修改鼠标光标，仅支持 PC 平台

## 示例代码
```js
// 默认图标
tt.setCursor('default');
// CSS 标准支持图标
tt.setCursor('copy');
// 指定文件
tt.setCursor('xxx.ico', 10, 10);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| path | string | 是 |  | 3.54.0 | 指定光标：  - 支持自定义图片和关键字（参考 [CSS 标准](https://developer.mozilla.org/en-US/docs/Web/CSS/cursor)） - 图片文件可选 ttfile:// 文件路径或者代码包路径 - 图片文件支持 ico 和 cur 格式，推荐图标大小 32x32 - 传入 'default' 代表恢复系统默认 |
| x | number | 否 |  | 3.54.0 | 横向偏移量，只有自定义文件光标有效 |
| y | number | 否 |  | 3.54.0 | 纵向偏移量，只有自定义文件光标有效 |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| success | boolean | 接口调用是否成功；  光标设置成功受图片格式和大小影响，需要预览验证； |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 999999 | invalid param |  |  |
| 999988 | The feature is not available in current operating system |  |  |

## 使用限制
只支持 PC 端使用该能力

## 相关课程
[PC 端小游戏接入指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/tutorial)

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/foundation/cursor) / [本地体验路径](tt-cursor)
