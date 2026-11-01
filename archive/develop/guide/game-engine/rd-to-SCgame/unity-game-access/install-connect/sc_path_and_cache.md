---
title: "目录说明与缓存策略"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/install-connect/sc_path_and_cache
update_time: 2025-06-17
---

> 在开发游戏的过程中，会涉及部分文件读写操作，本文对抖音Unity小游戏的目录管理及磁盘管理机制进行讲解。
> *了解更多：*[抖音Unity小游戏接入指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_access_guide)** **

## 目录划分
在游戏开发角度，抖音Unity小游戏对游戏文件目录进行以下划分：

### 游戏文件目录
游戏文件目录是游戏的主体文件存放目录，该目录包含游戏在启动后下载的资源文件、apk中解压出来的资源文件、Unity的Shader缓存等内容；

开发者可以通过 **Application.**[**persistentDataPath**](https://docs.unity3d.com/ScriptReference/Application-persistentDataPath.html) 方法获得游戏文件目录的可写路径；

游戏文件目录一般情况下不会被主动清理，但在游戏总磁盘占用过大，或者长期未玩等情况时，仍有可能触发清理操作，此后玩家再次打开该游戏会触发重新下载的操作；

> **注意**，部分开发者会将<u>**游戏存档**</u>放在游戏文件目录，该目录并不保证长期存在，建议使用**玩家数据目录**；

游戏文件目录的存储上限为1GB；

> **注意**，存储上限1GB，不代表所有的资源总大小需要在1GB以内，而是需要确保玩家在游戏过程中单个场景所需要的总资源大小在1GB以内即可；Unity小游戏会在达到存储上限时，根据资源引用，淘汰掉未使用的本地资源，腾出磁盘空间；

### 游戏临时目录
游戏临时目录，是游戏存放当次运行需要的临时文件的目录。该目录会在游戏未使用时，随时清空。请不要在该目录中放置任何重要的数据文件，以免丢失导致玩家损失。

开发者可以通过 **Application.**[**temporaryCachePath**](https://docs.unity3d.com/ScriptReference/Application-temporaryCachePath.html) 方法获得游戏临时目录的可写路径；

临时目录<u>**没有存储上限**</u>；但是注意，一旦游戏退出，随时可能会被清空。

### 玩家数据目录
玩家数据目录，是用于放置用户需要长期存储的数据资产的，主要用于放存档文件。游戏存档目录不会被磁盘清理机制所清理，会长期保留在磁盘上。

开发者<u>**无法**</u>直接获得玩家数据目录的路径，而是可以通过StarkSDK提供的Save/Load接口对数据对象进行存取操作，存取的结果会保存在玩家数据目录中；具体用法可以参考[StarkSDK_Unity文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk) ；

除此之外，如果只是简单的key-value存储，也可以使用Unity提供的[PlayerPrefs](https://docs.unity3d.com/ScriptReference/PlayerPrefs.html)接口进行数据存取；

玩家数据目录的存储上限为**50M**，如果达到上限，写入操作会失败，可以使用提供的配套接口删除不需要的存档文件；

## 磁盘清理规则
为了优化用户的磁盘占用，减少宿主的负向反馈，抖音Unity小游戏对于游戏的磁盘占用有一套动态的管理机制，以下进行说明：

### 清理划分
磁盘清理从影响的范围角度，可以划分为：
1. 清空临时目录：只对游戏临时目录进行清理；
1. 磁盘缩减：保留游戏的核心文件，只清理“可恢复”的文件；用户下次打开时，不会触发游戏下载界面，直接进入游戏（游戏进入后可能会有游戏内的资源下载）；影响游戏文件目录和临时目录；
1. 删除游戏：只保留玩家数据目录的内容，清理其它游戏相关目录；用户下次打开时，会触发游戏的重新下载；

### 清理时机
1. 清空临时目录
在游戏退出后，随时可能会触发清空临时目录的操作。此外在其它磁盘清理操作时，都会顺便清理下临时目录；
1. 磁盘缩减
Unity小游戏会定期进行检查，在游戏磁盘总占用超过**280M**时，触发磁盘缩减；此外，宿主app在发现磁盘总占用较高时，也会触发小游戏进行磁盘缩减；最后，玩家在宿主中退出当前账号时，也会触发磁盘缩减；
1. 删除游戏
Unity小游戏支持同时持久化**5款**游戏，当超过上限时，会根据LRU算法，找到最早被打开的游戏，进行删除；此外，如果游戏长时间(**14天**)没有再被打开过，也会触发游戏删除操作。
1. 其它清理时机
除了以上的主动磁盘管理，如果玩家删除宿主，也会导致Unity小游戏的所有磁盘占用被清理。
