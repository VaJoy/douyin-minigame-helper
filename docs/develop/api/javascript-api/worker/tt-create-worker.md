---
title: "tt.createWorker"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/worker/tt-create-worker
update_time: 2025-06-05
---

tt.createWorker("workers/index.js");

tt.createWorker(scriptPath)

## 语法

```js
tt.createWorker(scriptPath)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
创建一个 Worker 线程。

## 示例代码
```js
tt.createWorker("workers/index.js");
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| scriptPath | string | 是 |  | 1.0.0 | worker 入口文件的绝对路径 |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| Worker | Object | [Worker](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/worker/tt-create-worker) 对象 |

## 使用限制
- 目前限制最多只能创建一个 Worker，创建下一个 Worker 前请调用 [Worker.terminate](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/worker/worker-terminate/) 销毁当前 Worker 实例。
- scriptPath 为入口文件的绝对路径，且不以 / 开头。

## 前置条件
接口使用前需要在 game.json 中配置 workers 字段，表示 worker 代码根目录。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/worker/tt-create-worker) / [本地体验路径](tt-create-worker)
