---
title: "启动数据"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/about-data/performance-analysis/startup-data
update_time: 2024-07-24
---

## 概述

启动监控提供三部分数据展示，分别是：启动性能概览、启动性能转化漏斗数据和启动性能明细数据，支持不同维度的组合检索分析，方便开发者分析小游戏启动各个阶段的性能和留存情况。支持的分析维度如下：

![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/91289eaaa90b4ded9d632ac57530e37f~tplv-goo7wpa0wc-quality:q75.image)

1.版本：支持不同版本的筛选，支持全选；

2.时间：选择指定日期进行检索；

3.小游戏入口：小游戏入口场景的筛选，支持全选；

4.小游戏宿主：小游戏运行的宿主，比如：抖音、抖音极速版等，**必须指定宿主才可以进行检索**；

5.设备类型：Android / iOS，支持全选；

6.场景入口：支持自定义启动场景的组合筛选；

## 启动性能概览

![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/f9b0a003ef984ce9bafc3fec60dc80f0~tplv-goo7wpa0wc-quality:q75.image)

这一部分展示小游戏的主要启动性能指标，包括冷启动耗时、冷启动打开率、冷启动打开次数和启动流失人数，并支持两个维度的数据对比，分别是昨日指标数据和整体大盘均值数据，开发者点击具体指标可以查看对应天级别的数据变化趋势。指标含义如下：

|  |  |
| --- | --- |
| **字段名** | **字段含义** |
| 冷启动耗时 | 用户点击冷启动小游戏到小游戏首帧显示的时间，取80分位值作为冷启动耗时 |
| 冷启动打开率 | 用户点击冷启动小游戏到首帧显示的到达率 |
| 冷启动打开次数 | 用户点击冷启动小游戏的次数 |
| 启动流失 | 用户点击冷启动小游戏但并未成功到达首帧的人数 |

## 启动性能转化漏斗数据

![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/a2daaf8747a246caa1dd6bf3523ff92f~tplv-goo7wpa0wc-quality:q75.image)

开发者可选择系统启动场景和自定义启动场景进行漏斗转化分析，其中启动点击、资源准备完成、代码注入完成、首屏渲染完成和游戏可交互为平台预定义的五个场景，启动点击、资源准备完成这两个场景在漏斗中相对顺序固定。

![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/494e47c231b54a4a9f7cdf2538de9db1~tplv-goo7wpa0wc-quality:q75.image)

支持开发者在筛选时添加自定义场景，和平台预定义的场景共同组合成漏斗转化图。注意游戏可交互场景依赖开发者主动调用接口上报，上报场景 ID 为 7001，才能准确统计此场景的耗时情况。

![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/4e5f85caf267497fb635de5c7228fc88~tplv-goo7wpa0wc-quality:q75.image)

![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/492f5b3facee429a9f86ca84ddaea158~tplv-goo7wpa0wc-quality:q75.image)

开发者可以在启动场景配置栏中进行自定义场景的添加和维护，添加完成后可以调用 [tt.reportScene](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/data-analysis/tt-report-scene) 接口进行数据上报。

## 启动性能明细数据

![](https://p9-arcosite.byteimg.com/tos-cn-i-goo7wpa0wc/e4827057dae045c887410bdf7afa3df1~tplv-goo7wpa0wc-quality:q75.image)

这一部分展示小游戏启动性能指标的明细分布数据，指标含义如下：

|  |  |
| --- | --- |
| **字段名** | **字段含义** |
| 冷启动耗时分布 | 用户点击冷启动小游戏到首帧显示的耗时-用户量级（PV）分布情况 |
| 用户冷启动流失耗时分布 | 用户点击冷启动小游戏后但未成功进入首帧的等待耗时-用户量级（PV）分布情况 |
| 主要场景冷启动耗时 | 用户在各个场景点击冷启动小游戏到首帧显示的耗时-主要场景分布情况 |
| 主要场景冷启动打开率 | 用户在各个场景点击冷启动小游戏到首帧显示的到达率-主要场景分布情况 |
