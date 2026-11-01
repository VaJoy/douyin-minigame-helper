---
title: "数据分组实现游戏排行"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/ranking/challenge-to-ranking
update_time: 2025-05-19
---

除了平台开放的通用组件[游戏排行榜能力介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/game-rank/ImRankIntroduce)无需开发者进行二次开发之外，平台也提供了基于开放数据域的排行榜功能，开发者通过平台将用户分组标识配置为排行榜标识后，即可筛选处理数据后自行完成 UI 的设置
## 使用步骤说明

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/image-6813994475211180.png)

1. **登录开发者管理后台后，在「运营能力-排行榜配置-数据分组配置」中完成配置 **
1. **设置用户分组**
- 设置用户分组接口文档：[tt.setUserGroup](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/relationship-chain/ranking/tt-set-user-group/)
1. **完成规范格式的后台数据上报**
- 上报接口文档地址：[tt.setUserCloudStorage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/relationship-chain/open-data/tt-set-user-cloud-storage)
1. **开发者在业务代码中获取数据**
获取排行榜数据接口文档： [tt.getCloudStorageByRelation](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/relationship-chain/open-data/tt-get-cloud-storage-by-relation)
## 示例
**下面以一个通过数据分组完成游戏排行榜功能的例子做代码解释。**
1. 在主域中设置在排行榜功能设置标识。`groupId`的生成完全由开发者决定，需结合开发者自身策略来确保其唯一性。
该步骤必须确保是在上报游戏数据前执行，若在上报数据结果后执行，上报的结果将无法同步更新排行榜数据。

```js
tt.setUserGroup({
  groupId: "test_group",
});
```

1. 按照规范上报游戏数据。
配置了数据分组后，排行榜 key 对应的数据结构需要符合相应规范。详见 [KVData](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/relationship-chain/open-data/kv-data/)。

```js
const data = {
  ttgame: {
    //这里对象里面的score 和 update_time 两个key都是固定的。
    score: 16,
    update_time: +new Date(),
  },
  cost_ms: 36500,
};

tt.setUserCloudStorage({
  KVDataList: [
    // 这里key 需要在开发者后台配置，且配置为排行榜标识后，data 结构必须符合要求，否则会 set 失败
    { key: "userrank", value: JSON.stringify(data) },
  ],
});
```

1. 获取用户排行榜数据。

```js
tt.getCloudStorageByRelation({
  type: "group",
  keyList: ["userrank"],
  extra: {
    sortKey: "userrank", // 指定的key需要在后台配置过
    groupId: "test_group", // 指定要获取的用户所属分组
  },
  success(res) {
    console.log(res);
  },
  fail(e) {
    console.log("获取数据失败");
  },
});
```

## Bug & Tip
- Tip: 数据分组相关的接口要在调用前保证用户在主域中已经登录。getCloudStorageByRelation 只能在开放数据域中使用，setUserCloudStorage 支持在主域和开放数据域中使用，setUserGroup 只在主域中可用。
