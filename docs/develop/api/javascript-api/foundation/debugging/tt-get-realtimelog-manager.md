---
title: "tt.getRealtimeLogManager"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/debugging/tt-get-realtimelog-manager
update_time: 2025-01-02
---

## 语法

```js
tt.getRealtimeLogManager(option)
```
基础库 3.55.0 开始支持本方法，这是一个**同步**方法。
获取实时日志管理器对象。

## 示例代码
```js
const realtimeLogger = tt.getRealtimeLogManager({
  syncToConsole: true
});

realtimeLogger.setFilterMsg('demo1');
realtimeLogger.debug('这是真的debug 日志', 0);
realtimeLogger.addFilterMsg('demo2');
realtimeLogger.info('这是真的info 日志', true);
realtimeLogger.log('这是真的info 日志', {
  test: { test2: 2 }
});
realtimeLogger.setFilterMsg('demo3');
realtimeLogger.warn('这是真的warn 日志，', []);
realtimeLogger.error('这是真的error 日志，');
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| option | Object | 否 | {} | 3.55.0 | -  **对象字段** - **syncToConsole**（boolean）：true表示 log 内容会在 vConsole 或 IDE 控制台上展示， false 表示不展示 |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| instance | Object | 实时日志管理器的实例  **对象字段** - **log**（Function）：写 log 等级的实时日志。接收任意数量的可被 JSON.stringify 序列化的参数 - **debug**（Function）：写 debug 等级的实时日志。接收任意数量的可被 JSON.stringify 序列化的参数 - **info**（Function）：写 info 等级的实时日志。接收任意数量的可被 JSON.stringify 序列化的参数 - **warn**（Function）：写 warn 等级的实时日志。接收任意数量的可被 JSON.stringify 序列化的参数 - **error**（Function）：写 error 等级的实时日志。接收任意数量的可被 JSON.stringify 序列化的参数 - **setFilterMsg**（Function）：设置过滤关键字， 用于在后台筛选日志。每次调用会把前面通过RealtimeLogManager.addFilterMsg 和RealtimeLogManager.setFilterMsg设置的关键字覆盖 - **addFilterMsg**（Function）：追加过滤关键字，是setFilterMsg的添加接口。用于设置多个过滤关键字。最多加5个过滤关键字， 每个长度限制64个字符。 |

## 使用限制
1. **每个小游戏账号**每天限制 2000条日志，日志会保留 7 天，建议遇到问题及时定位。
2. 一条日志的限制长度 **256** 个字符，超出会被截断，避免在循环里面调用打日志接口，避免直接重写 console.log 的方式打日志，建议不要直接打印堆栈 。
3. 打印的每一个参数会通过 JSON.stringify 序列化，请避免打印自循环引用的结构。
4. setFilterMsg和addFilterMsg 可设置类似日志tag的过滤字段。如需添加多个关键字，建议使用addFilterMsg。例如addFilterMsg('scene1'), addFilterMsg('scene2'),addFilterMsg('scene3')
5. addFilterMsg 和 setFilterMsg 的参数不能有空格
6. 实时日志目前只支持在**手机端**测试。工具端的接口可以调用，但不会上报到后台。
7. **非线上版本**的日志只能通过 vconsole 来查看日志上报情况， 不会上报到后台。

## 背景
获取实时日志管理器对象。平台上的查看方式可以参考[实时日志能力介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/performance-tuning-tool/real-time-log)

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
