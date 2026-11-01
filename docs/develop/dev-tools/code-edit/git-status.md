---
title: "Git 状态展示"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/code-edit/git-status
update_time: 2025-06-04
---

> 如果编辑器中打开的抖音开放平台小程序工程目录中存在 Git 仓库，可以在源代码管理中查看目前的 Git 状态。
## 目录树
如图所示，当某些文件存在变动时，资源管理器目录树的文件右侧将展示相应的图标来表明这一状态。当某一目录下存在有变动的文件时，此目录的右侧也会展示一个圆点图标表明此情况。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1654748697425)

| 图标 | 含义 |
| --- | --- |
| U | 文件未跟踪（Untracked） |
| A | 新文件（Added, Staged） |
| M | 文件有修改（Modified） |
| +M | 文件有修改（Modified, Staged） |
| C | 文件有冲突（Conflict） |
| D | 文件被删除（Deleted） |

代码变动样式及对应含义如下：

| 图标 | 含义 |
| --- | --- |
| 小红点 | 目录下至少存在一个删除状态的文件 |
| 小橙点 | 目录下至少存在一个冲突状态的文件 |
| 小蓝点 | 目录下至少存在一个未跟踪状态的文件 |
| 小绿点 | 目录下至少存在一个修改状态的文件 |

如果某一文件存在修改（Modified），可以右键点击此文件，并选择 “与所选项目进行比较”，则可以查看当前工作区文件与 HEAD 版本的比较。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1654748697767)

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1654748697668)

代码变动样式及对应含义如下：

| 样式 | 含义 |
| --- | --- |
| 蓝色线条 | 此处的代码有变动 |
| 绿色线条 | 此处的代码是新增的 |
| 红色三角箭头 | 此处有代码被删除 |
