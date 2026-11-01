---
title: "抖音云本地调试"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/game-debug/douyin-cloud-local-debug
update_time: 2025-08-19
---

## 功能概述
抖音开发者工具支持在本地创建、开发、调试和部署抖音云函数服务，帮助开发者在抖音开发者工具中管理云端函数服务。
## 版本支持
抖音开发者工具 4.3.4 及之后版本支持该功能。下载地址：[开发者工具正式版下载](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/developer-instrument-update-and-download)。
## 准备
### 创建项目
首先需要使用 IDE 打开抖音云项目，若本地没有抖音云项目可通过如下两种方式创建抖音云项目。
#### 新建抖音云项目
在创建项目时，将**后端服务**勾选为**抖音云**，点击「新建」即可直接创建抖音云项目。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/81567aff10ad434c9e8ff256dfea4580~tplv-9nona0m7ha-image.image)

#### 将现有项目中切换为抖音云项目
在现有工程项目中的`project.config.json`文件里新增`cloudfunctionRoot`配置，其值为抖音云函数服务所在的根目录名称。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/301e7412b01a4ab89a9d6673c704dea0)

### 创建完成
当抖音云项目创建完成后，资源管理器中相应目录名称后会新增「函数服务」标记，该目录为抖音云函数的存放位置。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/951f6dbd424d4f3cab519d0996e1d563~tplv-9nona0m7ha-image.image)

## 功能介绍
### 同步函数服务
该操作可以将云端的函数服务下载到本地，如果本地已经存在同名的函数服务则会跳过：
1. 右键点击函数服务目录
1. 点击「同步函数服务」选项

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/1e3876d0ce44429684a58da32f01ec4d)

1. 同步完成后会通过弹窗展示函数服务同步信息

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/1e5f17d53ebf472aa0a53473dff5dea3)

### 新建函数服务
在 IDE 中支持快速创建函数服务模板：
1. 右键点击函数服务目录
1. 点击「新建函数服务」选项
1. 输入函数服务名称即可完成模板快速创建

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/0c8ad9f499f74b189b7e51885d1d3cde)

### 本地调试函数服务
在完成函数服务开发后，可在本地直接调试函数服务：
1. 右键点击函数服务目录中的文件或目录
1. 点击「本地调试函数服务」选项

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/e58bc911ea6b4c2db7690d37b7e93e61)

1. 输出面板中可查看调试过程中的日志信息

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/3bc2bdf2cc8545129af7e0c42c3ee5e6)

1. 调试启动完成后可在「抖音云」面板中对指定函数服务的函数进行接口调试

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/3d500693aa3842648f4ff665388790fd)

1. 除了可在「抖音云」面板中调试对应的函数服务，也支持在模拟器或真机预览过程中访问本地启动的函数服务
   1. 抖音云侧边栏中将 callContainer 的域名配置为本地域名
   1. 在代码中通过`tt.createCloud`访问指定的函数服务（由于在小游戏环境中需要`envId`与`serviceID`参数，因此该种方式只能调试已经部署过的函数服务）。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/0c9ad705e43b4122972a0a54709b49f8)

### 创建并部署函数服务
若需要将本地创建并开发完成的函数服务部署到云端，则可通过以下方式完成：
1. 右键点击函数服务目录中无「已关联」标记的函数服务目录
1. 点击「创建并部署函数服务」选项
1. 输入表单中需要填写的信息并确认
1. 在输出面板中查看部署日志

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/0bee920f91294ee496900707e4521109)

### 部署函数服务
若本地更新了已经部署过的函数服务里的代码，可通过以下方式将本地代码部署到云端：
1. 右键点击函数服务目录中有「已关联」标记的函数服务目录
1. 点击「部署服务」选项
1. 输入表单中需要填写的信息并确认
1. 在输出面板中查看部署日志

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/d53d7e7e3bd8493a8ca19812f52b4b39)

### 复制调用示例
如果想在小游戏中调试函数服务，IDE 支持快捷方式复制小游戏端的调用示例：
1. 右键菜单获取调用示例
   1. 右键菜单点击函数服务中有「已关联」标记的`JS`或`TS`文件
   1. 点击「复制小游戏端调用示例」，并将结果粘贴到小游戏代码中

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/d2b9016ab36e4971b8333ab72fd9224b)

1. 「抖音云」面板获取调用示例
   1. 在「抖音云」面板中将右上角切换为指定的函数服务名称
   1. 请求路径切换为指定的`JS`或`TS`文件
   1. 点击「复制调用示例」按钮，并将结果粘贴到小游戏代码中

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/9a11cffc2e3c46c8a53d1959926e9f0e)

> 注：在「抖音云」面板中复制调用示例时，会在调用示例中自动填充表单里的参数信息
## 常见问题
**Q：为什么在云端已经部署过的函数服务，在 IDE 中没有「已关联」标记。**
A：可执行「同步函数服务」操作或刷新资源管理器重新获取云端的部署信息。
**Q：为什么启动调试时提示端口号被占用。**
A：因为目前启动调试服务时会默认占用 8001 端口号，请确保本地没有其他工程也在进行抖音云调试或者有其他服务占用了 8001 端口号。
