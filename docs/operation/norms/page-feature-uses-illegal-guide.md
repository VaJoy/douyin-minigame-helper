---
title: "违规页面功能使用指南"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/norms/page-feature-uses-illegal-guide
update_time: 2025-06-09
---

### 一、功能简介

「违规页面」将展示审核侧在对小游戏进行复审时，发现小游戏内有违规页面做出的相应处理。在开发者平台进入对应小游戏后，点击「反馈中心-违规页面」即可查看。

在该看板中，会展示屏蔽时间、解除屏蔽时间、未通过页面 path+query、二维码、屏蔽原因和页面状态等信息。

平台支持对已屏蔽或已恢复页面的筛选操作，并支持开发者对相关页面进行处理并重新提交申请。

### 二、页面屏蔽查看与提审流程

1、进入开发者平台—反馈中心—违规页面，可以看到违规的小游戏页面，包括全部、已屏蔽、已恢复的小游戏页面；

![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/download_image-509000908839023.5.png)

2、屏蔽页面信息包括：屏蔽时间、解除屏蔽时间、未通过页面 path+query、二维码、屏蔽原因、页面状态、开发者操作；

3、当屏蔽状态为”已屏蔽“时，表示此时页面存在问题，请自行进行页面修改；屏蔽原因具体有如下几点：

- 内容引人不适：若页面中有部分视频、图片、文字引人不适，可以将部分内容删除，保留页面；若页面整体内容引人不适，建议将页面整个屏蔽或删除。
- 内容违反法律法规：若页面中有部分视频、图片、文字违反法律法规，可以将部分内容删除，保留页面；若页面整体存在违反法律法规风险，建议将页面整个屏蔽或删除。
- 内容色情低俗：若页面中有部分视频、图片、文字色情低俗，可以将部分内容删除，保留页面；若页面整体色情低俗，建议将页面整个屏蔽或删除。
- 内容含严重广告：需将广告删除，或屏蔽/删除页面。

4、完成修改后可点击”再次审核“，这样页面会送至审核队列再次审核，确认是否要解除屏蔽；

![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/download_image%20(5)-6017508126575846.png)

5、审核通过后，页面状态将变为“已恢复”，且不再支持送审操作；

![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/download_image%20(6)-5640487478150285.png)

6、若小游戏因为屏蔽内容多于 50 个而被下架，将在页面中提示”您的小游戏因存在较多违规内容已被下架，请将相关页面进行修改后重新提交上架申请“，且所有页面不支持提交”再次审核“。

![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/download_image%20(4)-4452899164337016.5.png)
