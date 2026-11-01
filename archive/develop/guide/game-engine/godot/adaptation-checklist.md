---
title: "适配清单"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/godot/adaptation-checklist
update_time: 2026-01-26
---

## 一、适配清单
### 1.屏幕大小适配
  **1.1 详细说明**：小游戏的渲染是基于一个设备屏幕相同大小的 canvas 进行 gl 绘制的。
  **1.2 适配参考**：计算关系：device pixel size * device pixel ratio == canvas size == frame buffer size == godot viewport size

### 2.适配安全区域
  **2.1 详细说明**：GUI 交互区域应避开手机刘海屏和小游戏容器上层胶囊按钮，避免发生交互阻塞。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/8d7fe48115a54376935f9d21b1fc3c48~tplv-9nona0m7ha-image.image)

  **2.2 适配参考**：
  - 获取安全区域：[tt.getSystemInfoSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/system/system-information/tt-get-system-info)
  - 获取胶囊按钮区域：[tt.getMenuButtonLayout](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/interface/menu/tt-get-menu-button-layout)

### 3.游戏包体大小
  **3.1 详细说明**： 小游戏用户对包体大小非常敏感，游戏包体不能超出抖音小游戏[包体大小限制](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/dev-guide/bytedance-mini-game#a0981165)。
  **3.2 适配参考**：如果包体大小超出限制，可以采用下面的方法：
  - 分离资源包，使用资源分包能力；（详见 [SDK文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/godot/sdk-usage-guide#af6d2309)）
  - 分离资源包，通过 CDN 进行下发；
  - 对资源包采用 brotli 压缩（谨慎使用）；（详见 [SDK文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/godot/sdk-usage-guide#a8faadfd)）

### 4.支持的文件格式
  **4.1 详细说明**：抖音小游戏限制了[可以上传的文件类型](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/bytedance-mini-game#a2755c7f)（其中`.pck` 暂时不在支持范围内），如果需要手动从包内加载文件，请先确认文件后缀。
  **4.2 适配参考**：如果包内需要包含 `.pck` 文件，建议将后缀名称修改为 `.bin`。
  **4.3 补充说明**：使用 SDK 进行 pack 导出将导出 `.bin` 文件，运行时可以用 `.pck` 后缀直接加载。

### 5.文件访问
  **5.1 详细说明**：小游戏可以访问的目录有 2 类
  - **包内目录**：是小游戏打包上传时就已经包含在内的目录（包括主包和子包），它们是只读的，可以使用 `FileAccess`通过相对路径进行读取。
  - **用户目录**：是抖音为每个小游戏分配的持久化本地磁盘空间，与 godot 的`user://`目录进行了绑定。用户目录空间有限，请合理分配。
  **5.2 适配参考**：可以使用 `FileAccess` 对上述文件目录进行访问
  - 读取包内文件（只读不可写）。需要开发者自行保证文件存在。

```python
var in_package_file_path = 'path/relative/to/game.js'

# 访问文件前需要调用 mount_ttpkg_file 方法
# 调用 mount_ttpkg_file 前，file_exists 返回 false
FileAccess.file_exists(in_package_file_path)

tt.mount_ttpkg_file(in_package_file_path)

# 调用 mount_ttpkg_file 后，file_exists 返回 true
FileAccess.file_exists(in_package_file_path) 

FileAccess.open(in_package_file_path, FileAccess.READ)
```

  - 读写用户目录

```python
FileAccess.open('user://savegame.cfg', FileAccess.READ)
FileAccess.open('user://savegame.cfg', FileAccess.WRITE)
```

### 6.定制加载页
  **6.1 详细说明**：从游戏启动到引擎加载完成展示首个画面之间的会展示加载页面，可以对加载页面进行自定义。
  **6.2 适配参考**：有两种自定义方式，部分自定义和完全自定义。
> ⚠️ 注意事项：手动修改 game.js 需要在导出选项中时勾选 **Custom Game Js**，避免 game.js 被覆盖。
  - 方式一：部分自定义 —— 使用平台内置的加载页面，通过参数调整页面样式。
    - 代码示例：

```js
// game.js

function main() {
    // ... 省略
    launcher.start({
        canvas: createCanvas(),
        config: config,
        options: {
            loadingPageStyleConfig: {
                designWidth: 375,
                designHeight: 667,
                materialConfig: {
                    backgroundImage: "images/loading.png"                
                }
            },
        }
    });
}
```

【折叠】附 `loadingPageStyleConfig` 完整可用参数：

```typescript

interface CustomLoadingCommonStyle {
  width: number;
  height: number;
  bottom: number;
}

// 缩放模式, 取值和效果参考，https://github.com/egret-labs/egret-docs/blob/master/Engine2D/screenAdaptation/zoomMode/README.md
type CustomLoadingScaleMode =
  | ''
  | 'NO_BORDER'
  | 'EXACT_FIT'
  | 'FIXED_HEIGHT'
  | 'FIXED_WIDTH'
  | 'SHOW_ALL'
  | 'FIXED_NARROW'
  | 'FIXED_WIDE';

type CustomLoadingColorString =
  // 颜色关键字
  | 'red'
  | 'green'
  | 'blue'
  | 'yellow'
  | 'black'
  | 'white'
  // 十六进制形式，支持 3 位和 6 位，带或不带 # 前缀
  | `#${string}`
  // RGB 形式
  | `rgb(${number}, ${number}, ${number})`
  // RGBA 形式
  | `rgba(${number}, ${number}, ${number}, ${number})`
  // HSL 形式
  | `hsl(${number}, ${number}%, ${number}%)`
  // HSLA 形式
  | `hsla(${number}, ${number}%, ${number}%, ${number})`;

export interface CustomLoadingConfig {
  totalLaunchTime: number; // 默认总启动耗时，即加载动画默认播放时间，可根据游戏实际情况进行调整
  /**
   * !!注意：修改设计宽高和缩放模式后，需要修改文字和进度条样式。默认设计尺寸为667*375
   */
  designWidth: number; // 设计宽度，单位px
  designHeight: number; // 设计高度，单位px
  scaleMode: CustomLoadingScaleMode; // 缩放模式
  // 以下配置的样式，尺寸相对设计宽高
  textConfig: {
    // 文字样式
    style: {
      lineHeight: number;
      color: CustomLoadingColorString; // like '#ffffff',
      fontSize: number;
    } & CustomLoadingCommonStyle;
  };
  // 进度条样式
  barConfig: {
    style: {
      padding: number;
      backgroundColor: CustomLoadingColorString;
    } & CustomLoadingCommonStyle;
  };
  // 一般不修改，控制icon样式
  iconConfig: {
    visible: boolean; // 是否显示icon
    style: CustomLoadingCommonStyle;
  };
  // 加载页的素材配置
  materialConfig: {
    // 背景图或背景视频，两者都填时，先展示背景图，视频可播放后，播放视频
    backgroundImage: string; // 背景图片，推荐使用小游戏包内图片；当有视频时，可作为视频加载时的封面
    backgroundVideo: string; // 加载视频，网络url
    iconImage: string; // icon图片，一般不更换
  };
}
```

  - 方式二：完全自定义 —— 关闭平台内置的加载页面，开发者根据需要实现自定义的加载页面。
    - 代码示例：

```js
// game.js

function main() {
    // ... 省略
    launcher.start({
        canvas: createCanvas(),
        config: config,
        options: {
            disableLoadingPage: true,
            onLoadProgress: onLoadProgress
        }
    });
}
/**
 * @param progress: number 表示当前加载进度，取值范围 0~1
 * @param hint: string 表示当前加载所处阶段，取值范围如下：
 *     - download 下载资源包
 *     - compile  wasm 编译
 *     - callmain 初始化
 *     - finished 已完成
 **/
function onLoadProgress(progress, hint) {
    console.log(progress, hint)
}
```

## 二、已知问题
### 1.文字输入事件
**1.1 关键词**：文字输入
**1.2 问题描述**：`LineEdit` 在 Web 平台下不触发 `text_changed`和 `text_submitted` 信号
**1.3 已知涉及范围**：Godot 4.5

### 2.旧版本 iOS 音频播放
**2.1 关键词**：版本兼容，音频播放
**2.2 问题描述**：在 iOS 旧版本抖音，`AudioPlayer` 仅支持`PLAYBACK_TYPE_SAMPLE`，不支持 `PLAYBACK_TYPE_STREAM`
**2.3 已知涉及范围**：基础库版本 3.95.0.0 以下
**2.4建议解决方案**：如果没有特殊的混音需求，建议使用 SAMPLE 模式（性能和兼容性更佳）
