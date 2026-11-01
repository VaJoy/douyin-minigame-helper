---
title: "ShareParam"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/retweet/share-param
update_time: 2025-11-13
---

开发者最终传递给发布器的数据，可以根据约定传入部分自定义数据。不同场景的传参如下：
> 目前支持的分享方式详见[内容转发分享](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/user-ops/gain-user/retweet)
## 普通IM分享

| 属性 | 类型 | 默认值 | 可选值 | 是否必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
| channel | string |  | 不传或传空字符串，默认分享方式 invite，拉起邀请面板分享游戏给好友 | 否 | 转发内容类型 |
| templateId | string |  |  | 否 | •分享素材模板 id，指定通过平台审核的 templateId 来选择分享内容，需在平台设置且通过审核。参考[拍摄视频并发布至抖音](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/open-capacity/operation/douyin_task) •如有个性化分享诉求，请在对应场景的调用点传入对应的templateId |
| desc | string |  |  | 否 | 分享文案，不传则默认使用后台配置内容或游戏简介 |
| title | string |  |  | 否 | 转发标题，不传则默认使用后台配置或当前小游戏的名称 |
| query | string |  |  | 否 | 查询字符串，必须是 key1=val1&key2=val2 的格式。从这条转发消息进入后，可通过 tt.getLaunchOptionsSync 或 tt.onShow 获取启动参数中的 query 用来实现信息透传 |
| success | Function |  |  | 否 | 分享成功后执行的回调函数 |
| fail | Function |  |  | 否 | 分享失败或者用户取消发布器后执行的回调函数 |
| complete | Function |  |  | 否 | 分享完成（无论成功与否）后执行的回调函数 |

## 组队IM分享
> 整体接入教程详见 [小游戏组队分享能力](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/retweet/minigameteamshare)

| 属性 | 类型 | 默认值 | 可选值 | 是否必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
| channel | string |  | 不传或传空字符串，默认分享方式 invite，拉起邀请面板分享游戏给好友，仅抖音 20.6 及以上版本 | 否 | 转发内容类型 |
| templateId | string |  |  | 否 | •分享素材模板 id，指定通过平台审核的 templateId 来选择分享内容，需在平台设置且通过审核。 •如有个性化分享诉求，请在对应场景的调用点传入对应的templateId |
| desc | string |  |  | 否 | 分享文案，不传则默认使用后台配置内容或游戏简介 |
| title | string |  |  | 否 | 转发标题，不传则默认使用后台配置或当前小游戏的名称 |
| query | string |  |  | 否 | 查询字符串，必须是 key1=val1&key2=val2 的格式。从这条转发消息进入后，可通过 tt.getLaunchOptionsSync 或 tt.onShow 获取启动参数中的 query 用来实现信息透传 |
| extra | object |  |  | 否 | 可以通过 extra 设置附加信息，以指定该消息为组队分享消息。详见组队分享extra |
| success | Function |  |  | 否 | 分享成功后执行的回调函数 |
| fail | Function |  |  | 否 | 分享失败或者用户取消发布器后执行的回调函数 |
| complete | Function |  |  | 否 | 分享完成（无论成功与否）后执行的回调函数 |

#### 组队分享extra

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| useTeamInvitationStyle | boolean | false | 否 | 标识该消息为组队消息 |
| activityID | string |  | 否 | 组队消息 的唯一标识，通过[createActivityId](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/dynamic-sharing/create-activity-id)获取，useTeamInvitationStyle 为true时必填 |
| templateInfo | array |  | 否 | 组队消息 的模板信息，Array<[TemplateInfo](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/share-param#0d80faba)>类型，useTeamInvitationStyle为true时必填 |
| versionType | string | current | 否 | 指定通过动态消息进入的小游戏版本：线上版current、测试版latest |

TemplateInfo类型说明
object 类型，属性如下：

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| name | string |  | 是 | 参数名，有效值：当前房间人数memberCount、房间人数上限roomLimit |
| value | string |  | 是 | 参数值 |

## 视频/录屏分享

| 属性 | 类型 | 默认值 | 可选值 | 是否必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
| channel | string |  | video，发布视频到抖音 | 否 | 转发内容类型 |
| desc | string |  |  | 否 | 分享文案，不传则默认使用后台配置内容或游戏简介 |
| title | string |  |  | 否 | 转发标题，不传则默认使用后台配置或当前小游戏的名称 |
| query | string |  |  | 否 | 查询字符串，必须是 key1=val1&key2=val2 的格式。从这条转发消息进入后，可通过 tt.getLaunchOptionsSync 或 tt.onShow 获取启动参数中的 query 用来实现信息透传 |
| extra | object |  |  |  | 可以通过 extra 设置以下附加信息，详见视频分享extra |
| success | Function |  |  | 否 | 分享成功后执行的回调函数 |
| fail | Function |  |  | 否 | 分享失败或者用户取消发布器后执行的回调函数 |
| complete | Function |  |  | 否 | 分享完成（无论成功与否）后执行的回调函数 |

### 视频分享extra

| 属性 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| withVideoId | boolean |  | 是否支持跳转到播放页， 以及支持获取视频信息等接口 （为 true 时会在 success 回调中带上 videoId） |
| videoPath | string |  | 视频地址 ，分享一个本地视频。如果 videoPath 不传入会拉起摄像头拍摄界面，否则直接跳转到发布器发布传入的视频 |
| videoTopics | array |  | 视频话题(仅抖音支持)，目前已由 hashtag_list 代替并即将废弃，为保证兼容性，建议同时设置 hashtag_list |
| createChallenge | boolean | FALSE | 是否分享为挑战视频 ( 仅头条支持 ) |
| video_title | string | "" | 视频的默认标题 |
| hashtag_list | array |  | 视频话题，若字符串中间包含空格，则取第一个空格前的内容作为话题(仅抖音支持) |
| videoTag | string |  | 分享视频的标签 |
| defaultBgm | string |  | 抖音 PGC 音乐的短链(仅抖音支持，需要基础库版本大于 1.90) 。形如[https://v.douyin.com/JmcxWo8/](https://v.douyin.com/JmcxWo8/%EF%BC%8C)[ ](https://v.douyin.com/JmcxWo8/%EF%BC%8C) ， 参考 [抖音小游戏录屏带配乐能力](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/gain-user/record-with-bgm) |
| cutTemplateId | string |  | 抖音上可用的剪映模板 ID， 参考 [录屏添加剪映视频模板能力](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/gain-user/capcut-with-game) |
| abortWhenCutTemplateUnavailable | boolean | FALSE | 剪映模板不可用或者剪映模板 ID 无效的时候是否直接回调失败 |

## 图文分享

| 属性 | 类型 | 默认值 | 可选值 | 是否必填 | 说明 |
| --- | --- | --- | --- | --- | --- |
| channel | string |  | picture，指定发布图文内容，仅抖音、抖音极速版、抖音火山版 25.9 及以上版本 | 否 | 转发内容类型 |
| desc | string |  |  | 否 | 分享文案，不传则默认使用后台配置内容或游戏简介 |
| title | string |  |  | 否 | 转发标题，不传则默认使用后台配置或当前小游戏的名称 |
| query | string |  |  | 否 | 查询字符串，必须是 key1=val1&key2=val2 的格式。从这条转发消息进入后，可通过 tt.getLaunchOptionsSync 或 tt.onShow 获取启动参数中的 query 用来实现信息透传 |
| extra | object |  |  |  | 可以通过 extra 设置附加信息，详见图文分享 extra |
| success | Function |  |  | 否 | 分享成功后执行的回调函数 |
| fail | Function |  |  | 否 | 分享失败或者用户取消发布器后执行的回调函数 |
| complete | Function |  |  | 否 | 分享完成（无论成功与否）后执行的回调函数 |

### 图文分享extra

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| picturePath | string[] |  | 否 | 发布的图片地址，仅支持本地图片路径（即游戏包内路径和ttfile://路径）channel=picture时，本参数必传。 |
| contentTitle | string |  | 否 | 作品标题 |
| contentDescription | string |  | 否 | 作品描述信息 |
| hashtag_list | array |  | 否 | 视频话题，若字符串中间包含空格，则取第一个空格前的内容作为话题 |

## 分享内容优先级
支持两种形式来指定转发的内容（图片、标题、文案），最终按照优先级规则进行选择， 详情参考[内容转发](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/gain-user/retweet)
1. 代码指定分享内容（title、desc）

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/c25dbe6906224530b0d70b0c87d394af~tplv-9nona0m7ha-image.image)

1. 指定审核通过的模板素材 templateId 场景优先级：端内分享代码指定分享内容 > 指定模板 > 平台默认；端外分享指定模板 > 平台默认
## Bug & Tip
- Tip：端外分享不支持通过代码设置自定义分享内容。
- Tip：如果需要获取视频信息或者跳转视频播放页，以及获取抖音视频排行榜时，需要填写 withVideoId 为 true。
- Tip：头条拍视频不支持设置 title 。
