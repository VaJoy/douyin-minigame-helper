---
title: "tt.getFeedData"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/feed-subscribe/tt-get-feed-data
update_time: 2025-10-27
---

## 语法

```js
tt.getFeedData(scene, contentID)
```
基础库 3.67.0 开始支持本方法，这是一个**异步**方法。
获取游戏是否直玩就绪状态数据。

## 示例代码
```js
tt.getFeedData({
  scene: 1, // 离线收益场景
  contentID: 'contentID123',
  success(res){
    console.log('getFeedData success', res.status, res.extra);
  },
  fail(res){
    console.log('getFeedData fail', res)
  },   
})
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| scene | number | 是 |  | 3.67.0 | 订阅的场景 ID  \|  \|  \| \| --- \| --- \| \| 值 \| 说明 \| \| 1 \| 离线收益场景 \| \| 2 \| 体力恢复场景 \| \| 3 \| 重要事件掉落 \| |
| contentID | string | 是 |  | 3.67.0 | 自定义文案的 contentID，contentID 在后台申请开通直玩能力后可获取 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："getFeedData:ok" - **extra**（string）：补充字段 - **status**（number）：当前直玩状态是否就绪 |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："getFeedData:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  | 3.67.0 |
| 10104 | invoke too frequently |  | 3.67.0 |
| 10401 | internal error |  | 3.67.0 |

## 前置条件
在使用前需前往开发者后台，在运营能力 - 推荐流直出能力中申请开通，并获取对应场景值 scene，素材 contentID

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
