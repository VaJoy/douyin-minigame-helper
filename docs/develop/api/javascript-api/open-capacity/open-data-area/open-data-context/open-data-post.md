---
title: "OpenDataContext.postMessage"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/open-data-area/open-data-context/open-data-post
update_time: 2025-10-10
---

## 功能描述
`postMessage` 方法用于向开放数据域发送结构化消息，触发数据域内的特定逻辑处理。该接口实现了主域与开放数据域之间的安全通信机制。

### API 说明
#### tt.getOpenDataContext().postMessage

##### 参数类型说明

| 属性名 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| params | object | 传递给开放数据域的消息体 | 1.11.0 |

##### 参数规范
  消息对象中的键值对必须符合以下要求：
  - key：任意合法字符串
  - value：仅支持原生数据类型（number/string/boolean/null/undefined）
### 使用示例

```text
// 获取开放数据域上下文 
const openDataContext = tt.getOpenDataContext(); 
 
// 发送结构化消息 
openDataContext.postMessage({ 
  command: 'show',        // 自定义指令 
  leaderboardType: 'level_1',  // 自定义参数 
  debugMode: false       // 布尔类型参数 
});
```

const openDataContext = tt.getOpenDataContext();
openDataContext.postMessage({
command: 'show', // 自定义指令leaderboardType: 'level_1' // 自定义参数
});
