---
title: "绑定头条号"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/user-ops/-retention/binding-toutiao-account
update_time: 2024-07-24
---

### 一、说明

进行客户端展示相关配置，有利于增加小程序的曝光

1. 搜索关键词：请在开发者后台配置。精确寻址，通用词、泛词等词汇均会被审核同学拒绝
2. 分享设置分享相关文案及图片请在开发者后台自行配置
3. 获取内测资格只有获取内测资格才可以进行 4，5 条操作
4. 小视频、个人主页 tab：获得内测资格的头条号在绑定小程序后进行小视频、个人主页 tab 相关操作，具体教程见下文
5. 头条号作者编辑文章插入卡片：获得内测资格的头条号在绑定小程序后可以在图文编辑器中进行手动插入，可以自选落地页以及卡片样式

### 二、获取开通资格

功能权限需要申请配置，申请流程如下：

邮件到[developer@bytedance.com](mailto:developer@bytedance.com)，邮件中需要包含：

1. 小游戏名称
2. 头条号名称
3. appid
4. mid
5. 头条号主页链接

> 1.若账号较多，请将表格保存至附件发送
>
> 2.appid 获取方式：在开发者平台-开发-小程序 Key 中获取
>
> 3.mid 获取方式：选择主页链接，如头条小程序头条号主页链接，[https://www.toutiao.com/c/user/106116465495/#mid=1616272632042504，其中，mid=1616272632042504](https://www.toutiao.com/c/user/106116465495/#mid=1616272632042504%EF%BC%8C%E5%85%B6%E4%B8%AD%EF%BC%8Cmid=1616272632042504)

### 三、头条号绑定小游戏

1. 进入头条号后台，在实验室中选择「小程序」（有内测资格的头条号才会有小程序功能）。

![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1651589093387)

2. 新建绑定。

![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1651589093674)

3. 输入 Appid，点击确定绑定即可。

![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1651589093712)

4. 此时绑定状态显示等待确认，需要到开放平台对应小程序的设置中确认绑定。

![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1651589093693)

5. 确认后，需要审核，审核通过即可.

#### 四、文章插入小游戏

1. 进入图文发布入口，在图文编辑器中可以看到小程序图标。

![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1651589094129)

2. 在想要插入的位置选择对应插入的小程序就可以啦，点击高级设置可以编辑介绍文案和落地地址呢～

![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1651589094304)

![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1651589094210)

### 五、头条号首页底部插入小程序入口

效果图：

![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1651589094660)

1. 进入头条号后台，选择自定义菜单，并新建菜单。
2. 按照提示选择要配置的小程序。

![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1651589095148)
