---
title: "加载外部js文件的支持"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc_webgl_load_js
update_time: 2025-02-12
---

## 准备js文件
需要加载的js文件都存放在Assets/StreamingAssets/__cp_js_files目录下，**可以有多个js文件，不支持子目录。**

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/c6005e04a58c4ecab49a0b5b1ce98bae)

直接构建WebGL版本即可。
当程序启动时，js运行环境初始化完成后，就会根据配置加载外部js代码。
外部js代码中暂时不支持import/export/require这样的机制。
如果有多个js文件，会按文件名顺序依次加载。如果不同js文件中有一些依赖，需自行确保文件加载顺序。
## API接口
加载外部js代码，能够直接访问所有js环境的对象。比如tt、globalThis、window、XMLHttpRequest等，但不是所有浏览器环境的对象都支持。另外，tt对象跟普通小游戏基础库中的tt对象不完全一样，有的接口在普通小游戏有提供，但unity小游戏并未提供。

```typescript
declare const StarkAPI: {
  /**
   * 注册全局错误监听
   * @param errMsg 错误日志
   */
  registerGlobalErrorListener: (errMsg: string) => void

  /**
   * 注册加载阶段监听
   * @param res object对象，包含stage以及errMsg字段，当stage值为load_error时，errMsg有值，
   *            stage为其余值，errMsg为undefined
   * stage的值：
   *    load_start：开始加载
   *    load_framework_js：加载js胶水代码
   *    load_unity_data：加载unity data文件
   *    load_wasm：加载wasm代码
   *    compile_wasm：编译wasm代码
   *    call_main：执行wasm main函数
   *    load_completed：加载完成
   *    load_error：加载失败
   */
  registerLoadStageChangedListener: (res: { stage: string, errMsg?: string }) => void
}
```

## 示例代码

```js
tt.showToast({
  title: "cp js file loaded"
});

StarkAPI.registerGlobalErrorListener((errMsg) => {
  console.error("__global_error:" + errMsg)
});

StarkAPI.registerLoadStageChangedListener(res => {
  console.info("load stage: " + res.stage)
  if (res.stage == "load_error") {
    console.error(res.errMsg);
  }
});
```

构建WebGL版本发布运行，正常情况下，进入游戏时，会弹出一个对话框：

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/9d5c32df19ca47b6aff4edaf01e9c0f8)

#
