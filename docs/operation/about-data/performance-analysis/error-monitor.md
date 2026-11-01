---
title: "错误监控"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/about-data/performance-analysis/error-monitor
update_time: 2025-05-06
---

### 一、大盘趋势

#### 小游戏实时趋势

![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/185b9f424c12421ab5f6a6053a657448~tplv-goo7wpa0wc-quality:q75.image)

展示小游戏在一段时间内的错误数或影响用户数的趋势图。

#### 宿主异常排行榜

![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/387f73297ad94268a66c1ed8be9cb170~tplv-goo7wpa0wc-quality:q75.image)

按错误数、影响用户数，对宿主排序。用户可以清楚看到在哪些宿主中的错误较多。

#### 维度

- 宿主应用
- 宿主大版本号
- 发布阶段
- 机型
- 城市

#### 错误列表

![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/c0bb7c7275444df3956343fcbdf82ab7~tplv-goo7wpa0wc-quality:q75.image)

平台根据错误堆栈，对 JS 错误做聚类，自动生成一条条 issue。列表中，展示了每一条 issue 的错误摘要、时间、迷你趋势图、等级以及处理状态。点击一条 issue 后，可进入该条 issue 的详情分析页。

### 二、详情分析页

点击 issue 列表中的 issue，即可进入该 issue 的详情分析页。

#### 错误摘要

![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/74452f6e7cb7489fa2725b04a7d584af~tplv-goo7wpa0wc-quality:q75.image)

错误摘要中，展示了错误文件、错误 message 等一些信息。

#### 错误趋势

![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/04dca6a367d045498466d8e353fd28a7~tplv-goo7wpa0wc-quality:q75.image)

错误趋势为该 issue 在所选时间范围内的趋势图，指标分为异常数和影响用户数。

#### 详情信息

![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4d7e498bfaa54fb386de2f836387cd17~tplv-goo7wpa0wc-quality:q75.image)

详情信息中，展示了这段时间内发生该类 issue 的所有用户的详细信息，除了上方展示的基础信息外，下方提供了错误堆栈、面包屑、extra 的功能。点击右上方的换页，可以切换用户信息。

- 错误堆栈：JS 错误堆栈，当前为混淆堆栈。
- 面包屑：用户发生该错误时的行为上下文。
- extra：该用户发生错误时，上报的额外信息。
