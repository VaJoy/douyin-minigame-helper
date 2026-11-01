---
title: "UpdateManager.applyUpdate"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/update/update-manager/update-manager-apply-update
update_time: 2024-09-25
---

基础库 1.9.0 开始支持本方法，这是一个**异步**方法。
当新版本下载完成，调用该方法会强制当前小游戏应用上新版本并重启。

## 示例代码
```js
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
});
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："UpdateManager.applyUpdate:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："UpdateManager.applyUpdate:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |
| 126101 | has no update |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
