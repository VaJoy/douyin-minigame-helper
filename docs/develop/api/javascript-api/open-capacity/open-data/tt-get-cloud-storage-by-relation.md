---
title: "tt.getCloudStorageByRelation"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/open-data/tt-get-cloud-storage-by-relation
update_time: 2025-10-10
---

## 语法

```js
tt.getCloudStorageByRelation(type, keyList, extra)
```
基础库 1.11.0 开始支持本方法，这是一个**异步**方法。
根据关系类型获取与当前用户相关的其他用户托管数据。

## 示例代码
```js
// 获取关系类型为friend的用户托管数据（非排行榜）
tt.getCloudStorageByRelation({
  type: "friend",
  keyList: ["score"],
  success: (res) => {
    console.log("调用成功");
    console.log(res.data);
  },
  fail: (res) => {
    console.log("调用失败");
  },
  complete: (res) => {
    console.log("调用完成");
  },
});

// 获取关系类型为group的挑战排行榜数据
tt.getCloudStorageByRelation({
  type: "group",
  keyList: ["ranlList"],
  extra: {
    sortKey: "ranlList", // 指定的key需要在后台配置过
    groupId: "test_group", // 指定要获取的用户所属分组
  },
  success: (res) => {
    console.log("调用成功");
    console.log(res.data);
  },
  fail: (res) => {
    console.log("调用失败");
  },
  complete: (res) => {
    console.log("调用完成");
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| type | number | 是 |  | 1.11.0 | 关系类型  **可选值：** friend=好友关系​；recommend=平台推荐部分用户；group=群，当 type == 'group'时，传入参数extra中的 sortKey 和 groupId 两个字段必传 |
| keyList | Array<string> | 是 |  | 1.11.0 | 要获取的 key 列表 |
| extra | Object | 否 |  | 1.11.0 | 获取挑战排行榜数据时需要传的配置​  **对象字段** - **sortKey**（string）：后台配置的排行榜 key - **groupId**（string）：用户分组 id |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| data | Array<Object> | 宿主 APP 中相关用户的托管数据  **对象字段** - **avatarUrl**（string）：用户头像 url - **nickname**（string）：用户昵称 - **openid**（string）：用户的 openid - **KVDataList**（Array<Object>）：用户的托管 KV 数据列表。数据类型为 [KVData](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/relationship-chain/open-data/kv-data) |
| errMsg | string | "getCloudStorageByRelation:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | "getCloudStorageByRelation:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 10401 | get session id failed. |  |  |
| 10301 | feature is not supported in app |  |  |
| 20000 | type is null |  |  |
| 21000 | 网络错误 |  |  |
| 21000 | respo |  |  |
| 10401 | platform auth deny |  |  |
| 10101 | invalid scope |  |  |
| 10200 | system auth deny |  |  |
| 10200 | auth deny |  |  |
| 10401 | internal error/网络请求非200 |  |  |
| 10103 | network unavailable |  |  |
| 10402 | native exception |  |  |
| 20000 | internal error |  |  |

## 使用限制
目前关系数据接口仅在抖音 APP 下可用，在头条中使用暂时无法获取有效数据，只能获取用户自身数据。

## 注意事项
- types 属性中的各类型关系均需要宿主 APP 支持后，开发者才可调用接口获取到有效数据。
- 该接口一次最多返回 **100** 个同玩好友的托管数据。
- 如果你希望获取有序的排行榜数据，请使用 type = 'group'
- 该方法数据源来自 [tt.setUserCloudStorage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/relationship-chain/open-data/tt-set-user-cloud-storage)。但与 [tt.getUserCloudStorage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/relationship-chain/open-data/tt-get-user-cloud-storage) 不同，通过该接口获取的数据会经过服务器处理，额外返回好友在同个小游戏中，储存在具有相同 keylist 的数据。
- Tip:当type == 'group'时，传入参数 extra 中的 sortKey 和 groupId 两个字段必传。

## 前置条件
在主域下使用 [tt.login](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/log-in/tt-login) 确认当前用户登录后才能使用

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/open-capacity/relationship-chain/open-data/tt-get-cloud-storage-by-relation) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-get-cloud-storage-by-relation%22%7D)
