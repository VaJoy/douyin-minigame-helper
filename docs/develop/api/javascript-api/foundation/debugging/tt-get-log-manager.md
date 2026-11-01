---
title: "tt.getLogManager"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/debugging/tt-get-log-manager
update_time: 2025-01-02
---

## 语法

```js
tt.getLogManager(option)
```
基础库 3.55.0 开始支持本方法，这是一个**同步**方法。
获取反馈日志管理器对象。

## 示例代码
```js
const logger = tt.getLogManager({
  syncToConsole: true,
  level: 1,
});

logger.debug("关键日志点1")
// ...
logger.info("关键日志点2")
// ...
logger.log("关键日志点3")
// ...
logger.warn("关键日志点4")
// ...
logger.error("关键日志点4")
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| option | Object | 否 | {} | 3.55.0 | -  **对象字段** - **level**（number）：取值为0/1，取值为0表示会把一些基础库的运行时信息（内容见下方）写入日志，取值为1则不会。默认值是 0 - **syncToConsole**（boolean）：true表示 log 内容会在 vConsole 或 IDE 控制台上展示， false 表示不展示 |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| logger | Object | 返回的日志管理器实例  **对象字段** - **log**（Function）：打印 log 等级日志，接收任意数量任意可被 JSON.stringify 序列化的参数 - **debug**（Function）：打印 debug 等级日志，接收任意数量任意可被 JSON.stringify 序列化的参数 - **info**（Function）：打印 info 等级日志，接收任意数量任意可被 JSON.stringify 序列化的参数 - **warn**（Function）：打印 warn 等级日志，接收任意数量任意可被 JSON.stringify 序列化的参数 - **error**（Function）：打印 error 等级日志，接收任意数量任意可被 JSON.stringify 序列化的参数 |

## 使用限制
1. 只有抖音、抖音极速版、抖音火山版支持。
2. 最多保存5M的日志内容，超过5M后，旧的日志内容会被删除。同时，平台也会删除长期未使用的小游戏的反馈日志。
3. 每次调用最多1000个字符，超出后截断。
4. 平台会做基本的频控，调用频率过高时会抛错。谨慎打日志，避免在无限循环里面调用打日志接口，避免直接重写 console.log 的方式打日志，

## 前置条件
需要在 tt.login 调用登录后使用

## 背景
反馈日志能力，支持在用户提交反馈时上传开发者用此api打印的日志，平台上使用详见[反馈日志能力介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/performance-tuning-tool/feedback-log-capability)

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
