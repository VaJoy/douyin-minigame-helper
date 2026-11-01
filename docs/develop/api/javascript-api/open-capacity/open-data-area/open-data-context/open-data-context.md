---
title: "OpenDataContext"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/open-data-area/open-data-context/open-data-context
update_time: 2025-09-11
---

## **1. 什么是开放数据域？**

> **开放数据域**是抖音小游戏提供的一个**独立、封闭的 JavaScript 运行环境**

它的核心使命是: **安全地处理和展示玩家的社交关系数据**，例如好友的昵称、头像以及他们在游戏中的分数，而不会将这些敏感信息直接暴露给你的主游戏逻辑。

## **2. 为什么需要开放数据域？**

主要出于**用户隐私和安全**的考虑。用户的社交数据（如好友列表、昵称、头像）是敏感信息。如果允许主游戏环境直接、无限制地访问这些数据，开发者可能会无意或有意地收集、滥用这些信息。

通过设立一个隔离的环境，抖音平台确保了：

- **数据访问受控   **只有在开放数据域内，才能调用特定的 API ([开放数据域](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/open-data-base#%E5%BC%80%E6%94%BE%E6%95%B0%E6%8D%AE%E5%9F%9F-api)) 来获取好友数据。
- **逻辑隔离           **主游戏逻辑无法直接访问开放数据域内的变量或函数，反之亦然。所有通信都必须通过约定的 postMessage 机制进行，就像两个独立的网页通过 iframe 通信一样。
- **渲染隔离**          开放数据域不能直接操作主画布，它只能在一个被称为**共享画布**的专属画布上进行绘制。

### **3. 核心特性**

| 特性 | 描述 |
| --- | --- |
| **环境隔离** | 具备独立的执行上下文与全局对象空间，与主域运行环境实现完全隔离。 |
| **受限的 API 访问** | 仅支持调用抖音开放平台指定的特定 API 集合，主域的大部分 API 在此环境中处于禁用状态。 |
| **消息驱动通信机制** | 与主域之间通过 `tt.postMessage()` 和 `tt.onMessage()` 消息通信接口建立唯一通信通道，要强调的是消息是单向驱动的 |
| **专属渲染画布** | 提供独立的 `SharedCanvas` 渲染上下文，其渲染内容可作为图片纹理供主域渲染系统调用。 |

### **4. 核心 API 解析**

理解开放数据域的关键在于掌握主域和开放数据域各自的专属 API。

#### **主域**
##### [tt.setUserCloudStorage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/open-data/tt-set-user-cloud-storage)
> 将当前玩家的游戏数据（如分数、段位）上传到抖音的云端服务器。这是所有排行榜数据的来源。
代码示例

```js
 tt.setUserCloudStorage({
        KVDataList: [{
          key: 'score', // 自定义 key
          value: '9999' // value 必须是字符串
        }],
        success: () => { console.log('分数上传成功'); }
 });
```

##### [tt.getOpenDataContext](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/open-data-area/tt-get-open-data-context)
> 获取开放数据域的上下文对象

返回值为 object 类型，详细参数描述如下：

| 属性名 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| canvas | object | 开放数据域和主域共享的 canvas，与 [tt.createCanvas](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/drawing/picture/tt-create-canvas) 获取的 canvas 类型一致 | 1.11.0 |
| postMessage | function | 主域向开放数据域发送消息。该方法只能在主域中使用 | 1.11.0 |

**postMessage 类型说明**

是一个回调函数，接收类型参数如下：

| 属性名 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| params | object | 传递给开放数据域的消息。对象中 value 只能是原生类型：number、string、boolean、null、undefined。 | 1.11.0 |

代码示例

```js
const openDataContext = tt.getOpenDataContext();
openDataContext.postMessage({
  command: 'show', // 自定义指令leaderboardType: 'level_1' // 自定义参数
});
```

### 开放数据API
> 开放数据API对有限接口开放
详情可见 [开放数据API接口列表](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/open-data-base#%E5%BC%80%E6%94%BE%E6%95%B0%E6%8D%AE%E5%9F%9F-api)

{

}
