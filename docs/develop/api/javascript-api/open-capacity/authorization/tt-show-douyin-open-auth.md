---
title: "tt.showDouyinOpenAuth"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/authorization/tt-show-douyin-open-auth
update_time: 2025-11-24
---

## 语法

```js
tt.showDouyinOpenAuth(scopes)
```
基础库 1.93.0 开始支持本方法，这是一个**异步**方法。
提供小游戏获取抖音权限的能力，展示出抖音权限授权弹窗。

## 示例代码
```js
tt.showDouyinOpenAuth({
  scopes: {
    im: 0, // 用户无法取消
    "im.media": 2,
  },
  success(res) {
    console.log("success", res);
  },
  fail(res) {
    console.log("fail", res);
  },
  complete(res) {
    console.log("complete", res);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| scopes | Object | 否 |  | 1.93.0 | 需要获取权限的信息，其中 key 值是申请权限的 scope，value 值必须是 0，1，2（此处申请的权限在抖音开放平台必须是**已开通**状态）  scopes 的属性值必需是0, 1, 2  \|  \|  \|  \|  \| \| --- \| --- \| --- \| --- \| \| 属性值 \| 类型 \| 说明 \| 版本 \| \| 0 \| number \| 必选项（用户无法取消） \| 1.93.0 \| \| 1 \| number \| 非必选，默认选中 \| 1.93.0 \| \| 2 \| number \| 非必选，默认不选中 \| 1.93.0 \| |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **ticket**（string）：请求授权返回的票据，此处对标开放平台的 authCode - **grantPermissions**（Array<string>）：用户授权的权限 - **errMsg**（string）："showDouyinOpenAuth:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："showDouyinOpenAuth:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21100 | android：login fail %s |  |  |
| 20000 | scopes is empty |  |  |
| 10200 | auth deny |  |  |
| 21100 | android：login fail iOS：login fail loginHostFail %s |  |  |
| 21101 | request auth ticket fail %s |  |  |
| 21102 | request auth scope info fail %s |  |  |
| 21103 | request auth code fail %s |  |  |
| 21104 | no usage scope |  |  |
| 10403 | unknown error |  |  |
| 20001 | invalid param |  |  |
| 20000 | internal error |  |  |
| 10301 | feature is not supported in app |  |  |
| 21105 | auth deny |  |  |

## 使用限制
该接口只支持抖音，所以请在抖音 APP 中调用；

## 注意事项
- 每次申请授权都是该小游戏的抖音权限全量授权，请在传入 scopes 时，把需要的授权的 scopes 都传入。由于不支持增量授权，即使用户已经授权过部分抖音权限，也还是需要全量传入所有需要的权限；
- 每次申请授权的抖音权限必须是在抖音开放平台已经**申请并且审批开通**的权限，否则会导致本次授权操作失败；
- 此处授权是抖音相关的授权，如果想要申请小游戏授权，请查看 [tt.authorize](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/user-information/authorization/tt-authorize)。这两处授权的 scopes 范围不同；
- 在请求服务端接口时，**应用唯一标识** 在小游戏场景下，对应的是小游戏 appId；**应用唯一标识对应的密钥**对应的是小游戏的 APP Secret。

## 前置条件
在使用在接口前，需要小游戏拥有者登录抖音开放平台申请开通小游戏需要的权限（如下图所示）。

具体路径：控制台 -> 运营 -> 抖音开放能力

![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/image-9917331765545944.png)

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
