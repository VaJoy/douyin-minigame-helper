---
title: "游戏设计规范"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/feed/game-design-standard
update_time: 2026-08-24
---

## 一、Feed直玩方案设计标准

| 评估维度 | 详细要求 | 案例 |
| --- | --- | --- |
| **画面规范** | 游戏画面作为背景，平台交互框架置于顶层，平台交互框架包括游戏名称、文案、「继续游戏/立即去玩」按钮等 开发者需把牵引用户的核心内容展示在「画布信息区」，更能吸引用户点击转化 横版特殊说明：推荐流直出容器会将游戏画面裁切为 4:3 尺寸并取中间区域展示，开发者需将引流核心内容集中放置于该 4:3 中间画面内，防止因平台裁切造成信息丢失 | **例：**    **负例：** |
| **方案体验规范** | 方案画面需展示游戏实机核心玩法，画面内容需与配套文案保持统一，点击可正常进游戏，游戏体验无断点/无加载卡顿，无首帧渲染加载失败/黑屏/白屏/无截图等打断项 纯功能页面：加载、菜单、登录页等 信息单一页面：仅展示 Logo、角色立绘、大段文字，无法体现游戏特色 |  |
| **弹窗规范** | 进入游戏5秒内禁止弹窗弹出，隐私弹窗建议在进游戏5-8秒采集个人信息前弹出 功能弹窗：授权、订阅、广告、加桌、分享、公告、隐私类弹窗 提示弹窗：操作教学、启动、确认、试玩、故障修复提示弹窗 奖励弹窗：离线收益、各类礼包、签到、充值、订阅奖励弹窗 |  |
| **内容合规** | 展示内容需内容合规且导向正常，不能使用攻击/冒充官方、敏感题材、低俗擦边、不良导向、诱导点击、违规引流等内容展示 冒充官方：假借抖音官方名义导流获客 不良导向：低俗擦边、暴力恐怖、不良未成年引导、山海经题材等违背公序良俗内容 敏感题材：涉政、涉恐、违法违规相关内容 诱导点击违规：大面积展示红包、金币、现金实物等福利诱导；借助卡位、画面暂停等形式强制引导用户点击 违规引流：引导私留联系方式、下载外部应用、跳转第三方外链 货不对板：展示内容与进入游戏后实际内容不符，禁止以 A 画面引流、落地却是 B 内容 |  |

## 二、违规处罚机制
不满足上述设计标准的方案，将会被拒审、下线。每个游戏所有方案违规次数会叠加计算，请务必遵循统一设计规范。

| 违规次数 | 处置 | 影响范围 |
| --- | --- | --- |
| 首次 | 违规方案下线 | 方案下线 |
| 第2次 | 违规方案下线 | 直玩获客游戏粒度下线30天 |
| 第3次 | 游戏粒度下线 | 直玩获客游戏粒度永久下线 |

## 三、常见拒审、下线原因与修改建议

| **拒审/封禁原因** | **原因详情****（仅列举常见场景，非穷尽所有场景）** | **问题示例****（非线上案例，仅作示意）** | **修改建议** |
| --- | --- | --- | --- |
| 请针对**Feed直玩**渠道来源的用户，暂时屏蔽和延迟不直接关联游戏体验的弹窗弹出 | 功能弹窗 获客版与复访版均不允许出现：订阅、授权、隐私保护、广告营销、加桌引导、侧边栏、分享引导等弹窗 |  | 第一步：通过「[获取启动信息](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/system/lifecycle/tt-get-launch-options-sync)」API能力，判断当前用户是直玩复访/获客版启动，针对该部分用户暂时屏蔽或延迟对应的弹窗弹出。 第二步：针对该部分用户自动加载到直接关联新手体验的游戏场景（如新手关卡/新手动画等），突出游戏玩法特色。 第三步：游戏客户端完成对应游戏场景加载完成后，需调用「[上报加载完成时机](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/data-analysis/tt-report-scene)」API 能力上报。 第四步：通过「[预览流进入](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/feed-subscribe/tt-feed-status-change)/[退出](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/feed-subscribe/off-feed-status-change)小游戏事件」API能力，判断用户**真实启动进入游戏至少5s后**，再恢复相应的弹窗逻辑。 *（备注：隐私保护弹窗建议在用户进入游戏后5-8s，且在游戏收集用户个人信息前弹出。）* 详细指引见：[《获客版-接入指南》](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/feed/customer-access-guide#a19700c7)-2.1 API接入、[《复访版-接入指南》](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/feed/minigame-feedpush-setting-guide)-2.1 API接入 |
|  | 提示弹窗 获客版：不允许出现如玩法教学、开启游玩、内容确认、试用试玩、异常修复等提示形态的弹窗 复访版：允许出现提示弹窗，但需与下方文案引导表述一致，避免订阅用户疑问 |  |  |
|  | 奖励弹窗 获客版：不允许出现如体力恢复、离线收益、限时礼包、新手礼包、签到奖励、订阅奖励、充值礼包等弹窗 复访版：允许出现奖励弹窗，但需与下方文案引导表述一致，避免订阅用户疑问 |  |  |
| 方案存在无法展示核心玩法的非游玩类界面 | 包括但不限于加载界面、菜单界面、选服界面、登录界面、开启界面等 |  | 第一步：通过「[获取启动信息](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/system/lifecycle/tt-get-launch-options-sync)」API能力，判断当前用户是直玩复访版/获客版启动 第二步：针对该部分用户自动加载到直接关联复访或新手体验的游戏场景 第三步：游戏客户端完成对应游戏场景加载完成后，需调用「[上报加载完成时机](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/data-analysis/tt-report-scene)」API 能力上报 详细指引见：[《复访版-接入指南》](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/feed/minigame-feedpush-setting-guide)-2.1 API接入、[《获客版-接入指南》](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/feed/customer-access-guide#a19700c7)-2.1 API接入 |
| 游戏推广素材需避免使用“与游戏玩法无关的内容”诱导用户点击参与，如“以游戏福利诱导用户参与游戏”；“以权限获取/隐私授权等方式引导用户参与游戏” | 使用玩法A作为feed展示素材，用户点击落地后却是完全不相关的玩法B，存在明显体验落差 |  | 请替换方案 |
|  | 包括不限于卡位遮挡、强制暂停、画面闪动位移等玩法，或是搭配卡位、定格、复位等干扰型交互文案，迫使用户点击画面 |  | 请替换方案 |
| 方案存在不建议推广的题材 | 包括但不限于AI山海经相关内容等 | / | 请替换方案 |
|  | 微恐题材禁止使用会对用户造成观感不适的素材，包括但不限于： 恐怖形象：怼脸恐怖画面、血腥、腐尸、鬼怪、畸变人形、阴间诡异形象等 惊吓特效：突然贴脸、镜头骤放、尖叫巨响、强光闪烁等跳吓设计 |  | 请替换方案 |
| 方案营销感重 | 包括但不限于： 出现红包、金币等广告要素 出现「元」、「¥」、「$」、「代金券」等真实货币指代的要素 出现实物奖励 | / | 请替换方案 |
| 方案禁止诱导下载或第三方引流 | 包括但不限于： 唤起任何下载，或出现“下载”等文字 出现外部的联系方式引流 存在第三方链接跳转 | / | 请及时整改游戏 游戏具体处罚规范可参考：[《小游戏行为规范》](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/norms/game-rule)- 3.6 涉及诱导下载或第三方引流行为 |
| 游戏存在同质化问题，已封禁【推荐流游戏直玩-获客能力】 | 申请直玩-获客能力上线的游戏为同质化游戏 | / | 请及时整改游戏 游戏具体处罚规范可参考：[《小游戏行为规范》](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/norms/game-rule)- 3.8 恶意提交同质化代码包 |
| 游戏存在加载折损问题 | 包括但不限「首帧渲染」失败、「场景加载」失败等 | / | 第一步：优化游戏性能，降低「首帧渲染」、「场景加载」等的耗时 性能数据标准参考： [小游戏性能评测标准_小游戏_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/performance-optimization/game-performance-standard)[Unity小游戏性能评测标准_小游戏_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/unity/performance-optimization/unity-minigame-scoring-standards) 建议Android/iOS的直玩场景加载时间均控制在40s内 第二步：检查对启动用户的渠道判断（获客or复访）是否正常（「[获取启动信息](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/system/lifecycle/tt-get-launch-options-sync)」API能力），对应的游戏场景上报是否正常（「[上报加载完成时机](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/data-analysis/tt-report-scene)」API能力） 详细指引见：[《复访版-接入指南》](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/feed/minigame-feedpush-setting-guide)-2.1 API接入、[《获客版-接入指南》](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/feed/customer-access-guide#a19700c7)-2.1 API接入 第三步：检查直玩场景加载过程，是否有依赖用户交互推进的流程阻断点，如有则会触发加载失败。请注意规避 |

## 四、优质案例参考

| **游戏** | **兵器王者** | **抓大鹅** | **狙击外星人** | **象棋达人** | **天天台球** |
| --- | --- | --- | --- | --- | --- |
| **案例** | **亮点：**轻量化锻刀场景用于直玩引流，吸引用户并顺滑跳转主场景，提升转化 | **亮点：**复用热门元素打造轻量化单元素消除关卡，低门槛快速给到爽感；通关无缝衔接日常关卡，延长时长、提升拉新转化 | **亮点**：以外星人偷锦鲤制造剧情冲突，两步点击即可射击，开镜提升沉浸；简约低多边形画风易上手，20 秒完成完整爽感体验 | **亮点**：复用短视频成熟的残局演示 + 挑战引流逻辑落地游戏内交互，直观凸显对局难点，激发挑战欲，提升参与度与点击转化 | **亮点**：台球受众基数大，改造直达击打黑球获胜高光，低门槛高反馈，新手流程结束无缝衔接创角，链路流畅 |

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/b9f3c5ab73894c9bb72841d935846ae2~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/b52dc3a935ba43cd8868859919bc5d23~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/9e530c25a97c4f0eb3e12d51555a575f~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/dbddceec0c77445e880156dfe3e8ed7e~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/7c9ad7c632954a88816d3f23c22dec04~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/0f77870bddf1474687a202e9929c3cb3~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/201f109d8cbf4f2da2d9f6f1a35dc9f0~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/b4db92254f4841a1aecc5d4e95327e1d~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/fd0ae29aa9d14f9bab5763212dc83fd8~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/2cd29edc1b33485eb7716f4ef921944e~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/77138a2b40694d3b9aec5e0d7c2dd4f7~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/50aaf8414e774dba8d7f75d48359f1d6~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/aded7095c02e41c8b1bd5ea13fbc6e71~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/69d2a34a8f3449d6907257e517b23321~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/d45197eccef9402b92984b82a3ca42a2~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/e167336f5c9743da88f92420dd326f72~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/2006b78f33944d1984065a347c3bbffb~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/e1cd50b23ed2424cba07eb32442812bd~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/2812c7cd129641cabf8c414ca604925e~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/d3fa8659bba74cb599dc0a31718f19f2~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/4d7c880a14104c82a91d372e12abffe6~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/8b775654b66d4381b2b814282b316d93~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/be5365456dd64768a219e446711a15ed~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/e4e013561a7d43449f2d92171ba3663d~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/43a2b2b3bf8f4b21830bb635bcb57438~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/87b3ad87d67242c987edc9e1e5e711a7~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/b09ac9b97a7841b082865cd89eb03043~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/728b09469fd348b88e4c01aa374ec43a~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/3726c625e1924b6d800b6ba0e77197c3~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/2ff9908ef4d34da199d8fb86de38691c~tplv-9nona0m7ha-image.image)

游戏原画16:9尺寸
⬇️ 平台处理

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/da38f0bc6d28414bb45591c241a9ec5c~tplv-9nona0m7ha-image.image)

推荐流直出裁切为4:3尺寸

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/c540fa7d710348c8bd12498055f9f30f~tplv-9nona0m7ha-image.image)

Feed效果示例

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/ef3ac2cae4864dd1a3b035f0d1a986bb~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/674f46a21bdc43fe970d2e21fcdbe46f~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/b741acecb693487e95ebf751e9166053~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/9021a72e8a9c4a7fb6218356012c7d0c~tplv-9nona0m7ha-image.image)