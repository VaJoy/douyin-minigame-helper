---
title: "更新机制"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/runtime/update-mechanism
update_time: 2025-06-13
---

## 静默更新机制
当开发者在管理后台发布新版本的小游戏后，若用户本地存在历史版本，首次打开时可能仍会使用旧版本。抖音客户端会在特定时机自动检查本地缓存的小游戏版本，发现更新后将静默下载最新版本。需要注意的是：

1. 新版本发布后不会立即覆盖所有用户
1. 最迟在发布后24小时内完成全量用户覆盖
1. 用户下次启动时将优先完成版本更新

## 更新触发时机

### 后台检测更新
- 客户端会定期检查最近使用过的小游戏版本状态
- 发现更新后将在下次启动时自动完成版本同步
- 确保新版本发布24小时后所有用户都能使用最新版本

### 冷启动检测
每次小游戏**冷启动**时都会执行版本检查：
1. 发现更新时异步下载新版本代码包
1. 继续使用当前本地版本运行
1. 新版本将在下次冷启动时生效

## 强制更新方案

### 通过API强制更新
使用tt.getUpdateManagerAPI实现主动更新提示：

```js
constupdateManager=tt.getUpdateManager();

updateManager.onUpdateReady((res)=>{
    tt.showModal({
        title:"更新提示",
        content:"新版本已就绪，是否立即应用？",
        success:(res)=>{
            if(res.confirm){
            updateManager.applyUpdate();
            }
        }
    });
});

updateManager.onUpdateFailed((err)=>{
    console.log("更新失败原因",err);
    tt.showToast({
        title:"更新失败，请重试",
        icon:"none"
    });
});
```

### 开发者工具调试
在抖音开发者工具中可通过以下路径调试强制更新功能：编译模式→编辑编译模式→模拟更新

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/aca9a60c85744453a87b3c4c77b7fbdb~tplv-9nona0m7ha-image.image)

**注意：该功能仅支持工具调试，真机环境不可用**

## 版本控制设置
为确保用户始终使用最新版本，可通过管理后台设置最低可用版本：
1.访问[小游戏管理后台](https://developer.open-douyin.com/console?type=2)
2. 进入【设置】→【基础设置】
3. 在「小游戏最低可用版本」中设置为最新版本号

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/b501c24207c7423e8df876fee528a3fd~tplv-9nona0m7ha-image.image)

const updateManager = tt.getUpdateManager();
updateManager.onUpdateReady((res) => {
tt.showModal({
title: "更新提示",
content: "新版本已经准备好，是否重启小游戏？",
success: (res) => {
if (res.confirm) {
// 新的版本已经下载好，调用 applyUpdate 应用新版本并重启
updateManager.applyUpdate();
}
},
});
updateManager.onUpdateFailed((err) => {
// 新的版本下载失败
console.log("版本下载失败原因", err);
tt.showToast({
title: "新版本下载失败，请稍后再试",
icon: "none",
});
