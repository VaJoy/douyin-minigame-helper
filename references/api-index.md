# JavaScript API 速查

> **适用**：查 `tt.*`、实例方法与事件回调是否存在、最低基础库、授权要求、支持平台。本表 **415** 项，数据截至 2026-08-06；另有 67 篇类说明与概念页未收录（见文末）。
> **源文档**：`docs/develop/api/javascript-api/`（483 篇官方 API 文档）。
> **关联**：参数、返回值、错误码与完整示例回查 `docs/` 原文；可直接抄的代码见 `api-recipes.md`。

低于表列版本的宿主上调用会失败，运行前用 `tt.canIUse('<方法名>')` 判断。表中每项只有一句话，定位到方法后请回原文看细节。

## 基础

_33 项_

| 方法 | 说明 | 基础库 | 授权 | 平台 |
| --- | --- | --- | --- | --- |
| `UpdateManager.applyUpdate` | 当新版本下载完成，调用该方法会强制当前小游戏应用上新版本并重启 | 1.9.0 | 无需 | iOS/Android |
| `UpdateManager.onCheckForUpdate` | 当向小游戏后台请求完新版本信息，会进行回调 | 1.9.0 | 无需 | iOS/Android |
| `UpdateManager.onUpdateFailed` | 当新版本下载失败，会进行回调 | 1.9.0 | 无需 | iOS/Android |
| `UpdateManager.onUpdateReady` | 当新版本下载完成，会进行回调 | 1.9.0 | 无需 | iOS/Android |
| `tt.canIUse` | 判断小游戏的 API、回调、参数、组件等是否在当前版本可用 | 1.35.0 | 无需 | iOS/Android |
| `tt.env` | 环境变量 | 1.0.0 | — | — |
| `tt.exitMiniProgram` | 退出当前小游戏到后台 | 1.12.0 | 无需 | iOS/Android |
| `tt.getEnvInfoSync` | 获取小游戏环境信息 | 2.78.0 | 无需 | iOS/Android |
| `tt.getLaunchOptionsSync` | 返回小游戏启动参数 | 1.12.0 | — | — |
| `tt.getLogManager` | 获取反馈日志管理器对象 | 3.55.0 | 无需 | iOS/Android |
| `tt.getPerformance` | 获取性能管理器 | 1.15.0 | 无需 | iOS/Android |
| `tt.getRealtimeLogManager` | 获取实时日志管理器对象 | 3.55.0 | 无需 | iOS/Android |
| `tt.getSystemInfo` | 获取系统信息 | 1.0.0 | 无需 | iOS/Android |
| `tt.getSystemInfoSync` | 获取系统信息 | 1.0.0 | 无需 | iOS/Android |
| `tt.getUpdateManager` | 获取全局唯一的版本更新管理器，用于管理小游戏更新 | 1.9.0 | 无需 | iOS/Android |
| `tt.loadSubpackage` | 触发分包加载下载与加载（如果分包指定的是一个目录，则自动加载目录下的 game.js, 如… | 1.88.0 | — | — |
| `tt.offError` | 取消监听全局错误事件 | 1.0.0 | 无需 | iOS/Android |
| `tt.offHide` | 取消监听小游戏隐藏到后台事件 | 1.0.0 | 无需 | iOS/Android |
| `tt.offShow` | 取消监听小游戏回到前台的事件 | 1.0.0 | 无需 | iOS/Android |
| `tt.offTouchCancel` | 取消监听触点失效事件 | 1.0.0 | 无需 | iOS/Android |
| `tt.offTouchEnd` | 取消监听触摸结束事件 | 1.0.0 | 无需 | iOS/Android |
| `tt.offTouchMove` | 取消监听触点移动事件 | 1.0.0 | 无需 | iOS/Android |
| `tt.offTouchStart` | 取消监听开始触摸事件 | 1.0.0 | 无需 | iOS/Android |
| `tt.onError` | 全局监听错误事件 | 1.0.0 | 无需 | iOS/Android |
| `tt.onHide` | 监听小游戏隐藏到后台的事件 | 1.0.0 | 无需 | iOS/Android |
| `tt.onMemoryWarning` | 注册监听内存不足警告函数 | 1.28.0 | 无需 | iOS/Android |
| `tt.onShow` | 监听小游戏回到前台的事件 | 1.0.0 | 无需 | iOS/Android |
| `tt.onTouchCancel` | 监听触点失效事件 | 1.0.0 | 无需 | iOS/Android |
| `tt.onTouchEnd` | 监听触摸结束事件 | 1.0.0 | 无需 | iOS/Android |
| `tt.onTouchMove` | 监听触点移动事件 | 1.0.0 | 无需 | iOS/Android |
| `tt.onTouchStart` | 监听开始触摸事件 | 1.0.0 | 无需 | iOS/Android |
| `tt.restartMiniProgramSync` | 重启小游戏 | 2.68.0 | 无需 | iOS/Android |
| `tt.triggerGC` | 加快触发 JS 引擎 Garbage Collection（垃圾回收），GC 时机是… | 1.15.0 | 无需 | iOS/Android |

## 界面

_22 项_

| 方法 | 说明 | 基础库 | 授权 | 平台 |
| --- | --- | --- | --- | --- |
| `InteractiveButton.destroy` | 销毁按钮，释放相关的资源 | 2.46.0 | 无需 | iOS/Android |
| `InteractiveButton.hide` | 隐藏按钮 | 2.46.0 | 无需 | iOS/Android |
| `InteractiveButton.offTap` | 注销按钮点击回调事件 | 2.46.0 | 无需 | iOS/Android |
| `InteractiveButton.onTap` | 注册按钮点击回调事件 | 2.46.0 | — | — |
| `InteractiveButton.show` | 显示按钮 | 2.46.0 | 无需 | iOS/Android |
| `tt.createInteractiveButton` | 该方法创建一个 Native 按钮，位于小游戏层级最上面，覆盖在小游戏 Canvas 画布上 | 2.46.0 | 无需 | iOS/Android |
| `tt.getMenuButtonLayout` | 获取菜单按钮（右上角胶囊按钮）的布局位置信息 | 1.25.0 | 无需 | iOS/Android |
| `tt.hideKeyboard` | 隐藏键盘 | 1.0.0 | 无需 | iOS/Android |
| `tt.hideLoading` | 隐藏 loading 提示框 | 1.0.0 | 无需 | iOS/Android |
| `tt.hideToast` | 隐藏灰色背景的消息提示框 | 1.0.0 | 无需 | iOS/Android |
| `tt.offKeyboardComplete` | 取消监听键盘收起的事件 | 1.0.0 | 无需 | iOS/Android |
| `tt.offKeyboardConfirm` | 取消监听用户点击键盘确定按钮时的事件 | 1.0.0 | 无需 | iOS/Android |
| `tt.offKeyboardInput` | 取消监听键盘输入事件 | 1.0.0 | 无需 | iOS/Android |
| `tt.onKeyboardComplete` | 监听键盘收起的事件，使用 tt.onKeyboardConfirm 或者… | 1.0.0 | 无需 | iOS/Android |
| `tt.onKeyboardConfirm` | 监听用户点击键盘确定按钮时的事件 | 1.0.0 | 无需 | iOS/Android |
| `tt.onKeyboardInput` | 监听键盘输入事件 | 1.0.0 | 无需 | iOS/Android |
| `tt.showActionSheet` | 显示操作菜单 | 1.0.0 | 无需 | iOS/Android |
| `tt.showKeyboard` | 显示软键盘 | 1.0.0 | 无需 | iOS/Android |
| `tt.showLoading` | 显示灰色背景的 loading 提示框 | 1.0.0 | 无需 | iOS/Android |
| `tt.showModal` | 显示模态弹窗 | 1.0.0 | 无需 | iOS/Android |
| `tt.showToast` | 显示灰色背景的消息提示框 | 1.0.0 | 无需 | iOS/Android |
| `tt.updateKeyboard` | 更新键盘，只有当键盘处于拉起状态时才会产生效果 | 1.0.0 | 无需 | iOS/Android |

## 渲染

_15 项_

| 方法 | 说明 | 基础库 | 授权 | 平台 |
| --- | --- | --- | --- | --- |
| `Canvas.getContext` | 获取画布对象的绘图上下文 | 1.31.0 | 无需 | iOS/Android |
| `Canvas.toTempFilePath` | 将当前 Canvas 保存为一个临时文件，并生成相应的临时文件路径 | 1.31.0 | 无需 | iOS/Android |
| `Canvas.toTempFilePathSync` | 将当前 Canvas 保存为一个临时文件，并生成相应的临时文件路径 | 1.31.0 | 无需 | iOS/Android |
| `cancelAnimationFrame` | 取消一个先前通过调用 requestAnimationFrame 方法添加到计划中的动画帧… | 1.0.0 | 无需 | iOS/Android |
| `requestAnimationFrame` | 该方法需要传入一个回调函数作为参数，该回调函数会在下一次重绘之前执行 | 1.0.0 | 无需 | iOS/Android |
| `tt.createBuffer` | 创建一个 buffer 对象 | 1.98.0 | 无需 | iOS/Android |
| `tt.createCanvas` | 创建一个画布对象 | 1.31.0 | 无需 | iOS/Android |
| `tt.createImage` | 创建一个图片对象 | 1.31.0 | 无需 | iOS/Android |
| `tt.exitPointerLock` | 解除锁定鼠标指针，仅适用于 PC 平台用 | 3.54.0 | 无需 | iOS/Android |
| `tt.inflate` | 提供解压缩的能力，支持由 zlib.deflateSync 和… | 1.3.0 | 无需 | iOS/Android |
| `tt.isPointerLocked` | 检查鼠标指针是否被锁定，仅适用于 PC 平台 | 3.54.0 | 无需 | iOS/Android |
| `tt.loadFont` | 加载自定义字体文件 | 1.23.0 | 无需 | iOS/Android |
| `tt.requestPointerLock` | 锁定鼠标指针，锁定后隐藏鼠标 | 3.54.0 | 无需 | iOS/Android |
| `tt.setCursor` | 修改鼠标光标，仅支持 PC 平台 | 3.54.0 | 无需 | iOS/Android |
| `tt.setPreferredFramesPerSecond` | 修改渲染帧率 | 1.15.0 | 无需 | iOS/Android |

## 数据缓存

_10 项_

| 方法 | 说明 | 基础库 | 授权 | 平台 |
| --- | --- | --- | --- | --- |
| `tt.clearStorage` | 清理 全部 本地数据缓存 | 1.0.0 | 无需 | iOS/Android |
| `tt.clearStorageSync` | 清理 全部 本地数据缓存的同步接口 | 1.0.0 | 无需 | iOS/Android |
| `tt.getStorage` | 获取本地缓存数据 | 1.0.0 | 无需 | iOS/Android |
| `tt.getStorageInfo` | 异步获取本地缓存数据的相关信息 | 1.0.0 | 无需 | iOS/Android |
| `tt.getStorageInfoSync` | 同步获取当前本地缓存数据的相关信息 | 1.0.0 | 无需 | iOS/Android |
| `tt.getStorageSync` | 获取本地缓存数据 | 1.0.0 | 无需 | iOS/Android |
| `tt.removeStorage` | 从本地缓存数据中异步删除 key 对应的值 | 1.0.0 | 无需 | iOS/Android |
| `tt.removeStorageSync` | 从本地缓存数据中删除 key 对应的值 | 1.0.0 | 无需 | iOS/Android |
| `tt.setStorage` | 以「键值对」的形式设置本地缓存数据 | 1.0.0 | 无需 | iOS/Android |
| `tt.setStorageSync` | 以「键值对」的形式设置本地缓存数据 | 1.0.0 | 无需 | iOS/Android |

## 文件

_48 项_

| 方法 | 说明 | 基础库 | 授权 | 平台 |
| --- | --- | --- | --- | --- |
| `FileSystemManager.access` | 判断文件/目录是否存在 | 1.15.0 | 无需 | iOS/Android |
| `FileSystemManager.accessSync` | 判断文件/目录是否存在 | 1.15.0 | 无需 | iOS/Android |
| `FileSystemManager.appendFile` | 在文件结尾追加内容，文件不存在时会新建 | 3.1.0 | 无需 | iOS/Android |
| `FileSystemManager.appendFileSync` | 在文件结尾追加内容，文件不存在时会新建 | 3.1.0 | 无需 | iOS/Android |
| `FileSystemManager.close` | 关闭文件 | 3.74.0 | 无需 | iOS/Android |
| `FileSystemManager.closeSync` | 关闭文件 | 3.74.0 | 无需 | iOS/Android |
| `FileSystemManager.copyFile` | 复制文件 | 1.15.0 | 无需 | iOS/Android |
| `FileSystemManager.copyFileSync` | 同步复制文件 | 1.15.0 | 无需 | iOS/Android |
| `FileSystemManager.fstat` | 获取文件的状态信息 | 3.74.0 | 无需 | iOS/Android |
| `FileSystemManager.fstatSync` | 获取文件的状态信息 | 3.74.0 | 无需 | iOS/Android |
| `FileSystemManager.ftruncate` | 对文件内容进行截断操作 | 3.74.0 | 无需 | iOS/Android |
| `FileSystemManager.ftruncateSync` | 对文件内容进行截断操作 | 3.74.0 | 无需 | iOS/Android |
| `FileSystemManager.getFileInfo` | 获取 临时目录 (ttfile://tmep) 或 用户目录 (ttfile://user… | 1.15.0 | 无需 | iOS/Android |
| `FileSystemManager.getSavedFileList` | 获取该小游戏下用户目录文件列表, 用户目录以 ttfile://user 开头 | 1.15.0 | 无需 | iOS/Android |
| `FileSystemManager.mkdir` | 在 用户目录 下创建目录 | 1.15.0 | 无需 | iOS/Android |
| `FileSystemManager.mkdirSync` | 在 用户目录 下创建目录 | 1.15.0 | 无需 | iOS/Android |
| `FileSystemManager.open` | 打开文件，返回文件描述符 | 3.74.0 | 无需 | iOS/Android |
| `FileSystemManager.openSync` | 打开文件，返回文件描述符 | 3.74.0 | 无需 | iOS/Android |
| `FileSystemManager.read` | 读文件 | 3.74.0 | 无需 | iOS/Android |
| `FileSystemManager.readCompressedFile` | 读取指定压缩类型的本地文件内容 | 3.74.0 | 无需 | iOS/Android |
| `FileSystemManager.readCompressedFileSync` | 读取指定压缩类型的本地文件内容 | 3.74.0 | 无需 | iOS/Android |
| `FileSystemManager.readFile` | 读取本地文件内容 | 1.15.0 | 无需 | iOS/Android |
| `FileSystemManager.readFileSync` | 读取本地文件内容 | 1.15.0 | 无需 | iOS/Android |
| `FileSystemManager.readSync` | 读文件 | 3.74.0 | 无需 | iOS/Android |
| `FileSystemManager.readZipEntry` | 读取压缩包内的文件 | 2.90.0 | 无需 | iOS/Android |
| `FileSystemManager.readdir` | 读取目录内文件列表 | 1.15.0 | 无需 | iOS/Android |
| `FileSystemManager.readdirSync` | 读取目录内文件列表 | 1.15.0 | 无需 | iOS/Android |
| `FileSystemManager.removeSavedFile` | 删除该小游戏下用户目录内的文件，用户目录以 ttfile://user 开头 | 1.15.0 | 无需 | iOS/Android |
| `FileSystemManager.rename` | 重命名文件，可以把文件从 oldPath 移动到 newPath | 1.15.0 | 无需 | iOS/Android |
| `FileSystemManager.renameSync` | 重命名文件，可以把文件从 oldPath 移动到 newPath | 1.15.0 | 无需 | iOS/Android |
| `FileSystemManager.rmdir` | 删除目录, 只能是 ttfile://user 下的目录 | 1.15.0 | 无需 | iOS/Android |
| `FileSystemManager.rmdirSync` | 删除目录，开发者只能删除 用户目录(ttfile://user) 下的目录 | 1.15.0 | 无需 | iOS/Android |
| `FileSystemManager.saveFile` | 保存临时文件到用户目录, 用户目录以 ttfile://user 开头 | 1.15.0 | 无需 | iOS/Android |
| `FileSystemManager.saveFileSync` | 保存临时文件到用户目录, 用户目录以 ttfile://user 开头 | 1.15.0 | 无需 | iOS/Android |
| `FileSystemManager.stat` | 获取文件 Stats 对象 | 1.15.0 | 无需 | iOS/Android |
| `FileSystemManager.statSync` | 获取文件 Stats 对象 | 1.15.0 | 无需 | iOS/Android |
| `FileSystemManager.truncate` | 对文件内容进行截断操作，只有用户目录ttfile://user下的文件可以截断 | 3.1.0 | 无需 | iOS/Android |
| `FileSystemManager.truncateSync` | 对文件内容进行截断操作，只有用户目录ttfile://user下的文件可以截断 | 3.1.0 | 无需 | iOS/Android |
| `FileSystemManager.unlink` | 删除文件，只能在 ttfile://user 开头的用户目录下操作 | 1.15.0 | 无需 | iOS/Android |
| `FileSystemManager.unlinkSync` | 删除文件，只能删除 用户目录(ttfile://user)下的文件 | 1.15.0 | 无需 | iOS/Android |
| `FileSystemManager.unzip` | 解压文件 | 1.15.0 | 无需 | iOS/Android |
| `FileSystemManager.write` | 写入文件 | 3.74.0 | 无需 | iOS/Android |
| `FileSystemManager.writeFile` | 写文件，只能写入用户目录(ttfile://user) | 1.15.0 | 无需 | iOS/Android |
| `FileSystemManager.writeFileSync` | ​写文件 | 1.15.0 | 无需 | iOS/Android |
| `FileSystemManager.writeSync` | 写入文件 | 3.74.0 | 无需 | iOS/Android |
| `Stats.isDirectory` | 判断当前文件是否一个目录 | 1.15.0 | — | — |
| `Stats.isFile` | 判断当前文件是否一个普通文件 | 1.15.0 | — | — |
| `tt.getFileSystemManager` | 获取全局唯一的文件管理器 | 1.15.0 | 无需 | iOS/Android |

## 位置

_1 项_

| 方法 | 说明 | 基础库 | 授权 | 平台 |
| --- | --- | --- | --- | --- |
| `tt.getLocation` | 获取设备当前的地理位置 | 1.0.0 | 需用户 | iOS/Android |

## 设备

_45 项_

| 方法 | 说明 | 基础库 | 授权 | 平台 |
| --- | --- | --- | --- | --- |
| `tt.addPhoneCalendar` | 向系统日历添加事件 | 2.52.0 | 需用户 | iOS/Android |
| `tt.getClipboardData` | 获取系统剪贴板内容 | 1.0.0 | 无需 | iOS/Android |
| `tt.getNetworkType` | 获取设备当前所处的网络类型 | 1.0.0 | 无需 | iOS/Android |
| `tt.getScreenBrightness` | 获取屏幕亮度 | 1.79.0 | 无需 | iOS/Android |
| `tt.offAccelerometerChange` | 解绑加速度数据监听器 | 1.94.0 | 无需 | iOS/Android |
| `tt.offCompassChange` | 解绑罗盘数据变化监听器 | 1.94.0 | 无需 | iOS/Android |
| `tt.offDeviceMotionChange` | 移除设备方向变化事件的监听函数，但不会停止获取设备方向数据 | 2.92.0 | 无需 | iOS/Android |
| `tt.offDeviceOrientationChange` | 移除屏幕转向切换事件的监听函数 | 3.66.0 | 无需 | iOS/Android |
| `tt.offGyroscopeChange` | 移除陀螺仪监听，但不会停止获取陀螺仪数据 | 1.72.0 | 无需 | iOS/Android |
| `tt.offKeyDown` | 移除键盘按键按下事件的监听函数，仅适用于 PC 平台 | 3.54.0 | 无需 | iOS/Android |
| `tt.offKeyUp` | 移除键盘按键弹起事件的监听函数，仅适用于 PC 平台 | 3.54.0 | 无需 | iOS/Android |
| `tt.offMouseDown` | 解除鼠标按键按下事件的监听，仅适用于 PC 平台 | 3.54.0 | 无需 | iOS/Android |
| `tt.offMouseMove` | 解除鼠标移动事件的监听，仅适用于 PC 平台 | 3.54.0 | 无需 | iOS/Android |
| `tt.offMouseUp` | 解除鼠标按键弹起事件的监听，仅适用于 PC 平台 | 3.54.0 | 无需 | iOS/Android |
| `tt.offNetworkStatusChange` | 移除网络状态变化事件的监听函数 | 1.91.0 | 无需 | iOS/Android |
| `tt.offNetworkWeakChange` | 移除弱网状态变化事件的监听函数 | 3.44.0 | 无需 | iOS/Android |
| `tt.offWheel` | 取消监听鼠标滚轮事件 | 3.54.0 | 无需 | iOS/Android |
| `tt.onAccelerometerChange` | 监听加速度数据 | 1.0.0 | 无需 | iOS/Android |
| `tt.onCompassChange` | 监听罗盘数据变化事件，罗盘数据会在用户手机发生“朝向变化/加速前进&后退/摇一摇”等手势时… | 1.2.0 | 无需 | iOS/Android |
| `tt.onDeviceMotionChange` | 监听设备方向变化事件 | 2.92.0 | 无需 | iOS/Android |
| `tt.onDeviceOrientationChange` | 监听屏幕转向切换事件 | 3.66.0 | 无需 | iOS/Android |
| `tt.onGyroscopeChange` | 监听陀螺仪数据变化，数据变化及回调函数被调用的频率取决于启动陀螺仪实例时传入的参数，该方法… | 1.72.0 | 无需 | iOS/Android |
| `tt.onKeyDown` | 监听键盘按键按下事件，仅适用于 PC 平台 | 3.54.0 | 无需 | iOS/Android |
| `tt.onKeyUp` | 监听键盘按键弹起事件，仅适用于 PC 平台 | 3.54.0 | 无需 | iOS/Android |
| `tt.onMouseDown` | 鼠标按键按下事件的监听函数，仅适用于 PC 平台 | 3.54.0 | 无需 | iOS/Android |
| `tt.onMouseMove` | 鼠标移动事件的监听函数，仅适用于 PC 平台 | 3.54.0 | 无需 | iOS/Android |
| `tt.onMouseUp` | 鼠标按键弹起事件的监听函数，仅适用于 PC 平台 | 3.54.0 | 无需 | iOS/Android |
| `tt.onNetworkStatusChange` | 监听网络状态变化 | 1.0.0 | 无需 | iOS/Android |
| `tt.onNetworkWeakChange` | 监听弱网状态变化事件 | 3.44.0 | 无需 | iOS/Android |
| `tt.onWheel` | 监听鼠标滚轮事件，仅适用于 PC 平台 | 3.54.0 | 无需 | iOS/Android |
| `tt.scanCode` | 扫描二维码并返回扫描结果 | 1.0.0 | 无需 | iOS/Android |
| `tt.setClipboardData` | 设置系统剪贴板内容 | 1.0.0 | 无需 | iOS/Android |
| `tt.setDeviceOrientation` | 切换横竖屏，接口调用成功后会触发 tt.onDeviceOrientationChange… | 3.66.0 | 无需 | iOS/Android |
| `tt.setKeepScreenOn` | 设置是否保持屏幕常亮状态 | 1.0.0 | 无需 | iOS/Android |
| `tt.setScreenBrightness` | 设置屏幕亮度 | 1.79.0 | 无需 | iOS/Android |
| `tt.startAccelerometer` | 开始监听加速度数据 | 1.0.0 | 无需 | iOS/Android |
| `tt.startCompass` | 开始监听罗盘数据 | 1.2.0 | 无需 | iOS/Android |
| `tt.startDeviceMotionListening` | 创建设备方向监听实例，开始监听设备方向的变化 | 2.92.0 | 无需 | iOS/Android |
| `tt.startGyroscope` | 创建陀螺仪实例，准备获取陀螺仪数据 | 1.73.0 | 无需 | iOS/Android |
| `tt.stopAccelerometer` | 停止监听加速度数据 | 1.0.0 | 无需 | iOS/Android |
| `tt.stopCompass` | 停止监听罗盘数据 | 1.2.0 | 无需 | iOS/Android |
| `tt.stopDeviceMotionListening` | 销毁设备方向监听实例，停止监听设备方向的变化 | 2.92.0 | 无需 | iOS/Android |
| `tt.stopGyroscope` | 停止获取陀螺仪数据，调用该方法后会销毁陀螺仪实例，并会自动调用… | 1.72.0 | 无需 | iOS/Android |
| `tt.vibrateLong` | 使手机发生较长时间的振动（400 ms) | 1.0.0 | 无需 | iOS/Android |
| `tt.vibrateShort` | 使手机发生较短时间的振动 | 1.0.0 | 无需 | iOS/Android |

## 网络

_12 项_

| 方法 | 说明 | 基础库 | 授权 | 平台 |
| --- | --- | --- | --- | --- |
| `RequestTask.abort` | 中断请求任务 | — | — | — |
| `SocketTask.close` | 关闭 WebSocket 连接的方法 | 1.0.0 | — | — |
| `SocketTask.onClose` | 监听 WebSocket 与服务器连接断开的事件 | 1.0.0 | — | — |
| `SocketTask.onError` | 监听 WebSocket 发生错误的事件 | 1.0.0 | — | — |
| `SocketTask.onMessage` | 监听 WebSocket 接收到服务器发送信息的事件 | 1.0.0 | — | — |
| `SocketTask.onOpen` | 监听 WebSocket 连接服务器成功的事件 | 1.0.0 | — | — |
| `SocketTask.send` | 通过 WebSocket 连接发送数据 | — | — | — |
| `UploadTask.offProgressUpdate` | 移除上传进度变化事件的监听函数 | 2.1.0 | — | — |
| `tt.connectSocket` | 创建一个 WebSocket 连接实例，并通过返回的SocketTask操作该连接 | 1.0.0 | 无需 | iOS/Android |
| `tt.downloadFile` | 客户端直接发起一个 HTTPS GET 请求，下载网络文件到本地临时目录 | 1.0.0 | 无需 | iOS/Android |
| `tt.request` | 发起一个网络请求 | 1.0.0 | 无需 | iOS/Android |
| `tt.uploadFile` | 将本地文件上传到网络 | 1.0.0 | 无需 | iOS/Android |

## 媒体

_109 项_

| 方法 | 说明 | 基础库 | 授权 | 平台 |
| --- | --- | --- | --- | --- |
| `AudioContext.createAnalyser` | 创建并返回一个新的 AnalyserNode 对象实例 | 1.34.0 | 无需 | iOS/Android |
| `AudioContext.createAudio` | 用于新建一个 Audio 对象，对齐 HTMLAudioElement | 1.34.0 | 无需 | iOS/Android |
| `AudioContext.createBuffer` | 新建一个空白的 AudioBuffer 对象，以便用于填充数据，通过… | 1.34.0 | 无需 | iOS/Android |
| `AudioContext.createBufferSource` | 创建一个新的 AudioBufferSourceNode 节点, 该节点可以播放… | 1.34.0 | 无需 | iOS/Android |
| `AudioContext.createDelay` | 创建并返回一个新的 DelayNode，DelayNode 是一个用于延迟的节点，为输入的… | 1.34.0 | 无需 | iOS/Android |
| `AudioContext.createEqualizer` | 创建并返回一个新的 EqualizerNode，EqualizerNode 是一个均衡器节… | 1.34.0 | 无需 | iOS/Android |
| `AudioContext.createF0Detection` | 创建并返回一个新的 F0DetectionNode，F0DetectionNode 是一个… | 1.34.0 | 无需 | iOS/Android |
| `AudioContext.createFading` | 创建并返回一个新的 FadingNode，用于控制音频数据淡入淡出的节点 | 1.34.0 | 无需 | iOS/Android |
| `AudioContext.createFastForward` | 创建并返回一个新的 FastForwardNode，FastForwardNode 可以快… | 1.34.0 | 无需 | iOS/Android |
| `AudioContext.createGain` | 创建并返回一个新的 GainNode 对象实例，GainNode 是一个… | 1.34.0 | 无需 | iOS/Android |
| `AudioContext.createMediaElementSource` | 创建并返回一个新的 MediaElementAudioSourceNode，该对象是由… | 1.34.0 | 无需 | iOS/Android |
| `AudioContext.createMediaStreamSource` | 创建并返回一个新的 MediaStreamAudioSourceNode 对象节点，是作为… | 1.34.0 | 无需 | iOS/Android |
| `AudioContext.createOscillator` | 创建并返回一个新的 OscillatorNode | 1.34.0 | 无需 | iOS/Android |
| `AudioContext.createReverb` | 创建并返回一个新的 ReverbNode 对象实例，ReverbNode 是一个混响节点… | 1.34.0 | 无需 | iOS/Android |
| `AudioContext.createStreamFileWriter` | 创建并返回一个新的 StreamFileWriterNode，StreamFileWrit… | 1.34.0 | 无需 | iOS/Android |
| `AudioContext.createVolumeDetection` | 创建并返回一个新的 VolumeDetectionNode，用于获取输入源的音量检测数据 | 1.34.0 | 无需 | iOS/Android |
| `AudioContext.decodeAudioData` | 用于异步解码音频文件， 并以 ArrayBuffer 的形式返回音频文件中的内容 | 1.34.0 | 无需 | iOS/Android |
| `Camera.destroy` | 销毁摄像头实例 | 1.40.0 | 无需 | iOS/Android |
| `Camera.pause` | 暂停摄像头视频画面 | 1.40.0 | 无需 | iOS/Android |
| `Camera.resume` | 恢复摄像头画面 | 1.40.0 | 无需 | iOS/Android |
| `Camera.setBeautifyParam` | 设置美颜参数 | 1.40.0 | 无需 | iOS/Android |
| `Camera.start` | 启动摄像头，该方式返回一个 Promise 对象，是个异步方法 | 1.40.0 | 无需 | iOS/Android |
| `GameRecorderManager.clipVideo` | 剪辑精彩的视频片段 | 1.6.1 | 无需 | iOS/Android |
| `GameRecorderManager.getMark` | 获取录屏水印宽高 | 1.69.0 | 无需 | iOS/Android |
| `GameRecorderManager.offError` | 取消监听录屏错误事件 | 1.6.1 | 无需 | iOS/Android |
| `GameRecorderManager.offInterruptionBegin` | 取消监听录屏中断开始事件 | 1.6.1 | 无需 | iOS/Android |
| `GameRecorderManager.offInterruptionEnd` | 取消监听录屏中断结束事件 | 1.6.1 | 无需 | iOS/Android |
| `GameRecorderManager.offPause` | 取消监听录屏暂停事件 | 1.6.1 | 无需 | iOS/Android |
| `GameRecorderManager.offResume` | 取消监听录屏继续事件 | 1.6.1 | 无需 | iOS/Android |
| `GameRecorderManager.offStart` | 取消监听录屏开始事件 | 1.4.1 | 无需 | iOS/Android |
| `GameRecorderManager.offStop` | 取消监听录屏结束事件 | 1.6.1 | 无需 | iOS/Android |
| `GameRecorderManager.onError` | 监听录屏错误事件 | 1.6.1 | 无需 | iOS/Android |
| `GameRecorderManager.onInterruptionBegin` | 监听录屏中断开始事件 | 1.6.1 | 无需 | iOS/Android |
| `GameRecorderManager.onInterruptionEnd` | 监听录屏中断结束事件 | 1.6.1 | 无需 | iOS/Android |
| `GameRecorderManager.onPause` | 监听录屏暂停事件 | 1.6.1 | 无需 | iOS/Android |
| `GameRecorderManager.onResume` | 监听录屏继续事件 | 1.6.1 | 无需 | iOS/Android |
| `GameRecorderManager.onStart` | 监听录屏开始事件 | 1.4.1 | 无需 | iOS/Android |
| `GameRecorderManager.onStop` | 监听录屏结束事件，可以获得录屏地址 | 1.6.1 | 无需 | iOS/Android |
| `GameRecorderManager.pause` | 暂停录屏 | 1.6.1 | 无需 | iOS/Android |
| `GameRecorderManager.recordClip` | 记录精彩的视频片段，调用时必须是正在录屏，以调用时的录屏时刻为基准，指定前 x 秒，后… | 1.6.1 | 无需 | iOS/Android |
| `GameRecorderManager.resume` | 继续录屏 | 1.6.1 | 无需 | iOS/Android |
| `GameRecorderManager.start` | 开始录屏 | 1.4.1 | 无需 | iOS/Android |
| `GameRecorderManager.stop` | 停止录屏 | 1.6.1 | 无需 | iOS/Android |
| `InnerAudioContext.destroy` | 销毁当前实例 | 1.0.0 | 无需 | iOS/Android |
| `InnerAudioContext.offCanplay` | 取消 监听 canplay 事件 | 1.0.0 | 无需 | iOS/Android |
| `InnerAudioContext.offEnded` | 取消监听自然播放结束事件 | 1.0.0 | 无需 | iOS/Android |
| `InnerAudioContext.offError` | 取消监听音频播放错误事件 | 1.0.0 | 无需 | iOS/Android |
| `InnerAudioContext.offPause` | 取消监听 pause 事件 | 1.0.0 | 无需 | iOS/Android |
| `InnerAudioContext.offPlay` | 取消监听 play 事件 | 1.0.0 | 无需 | iOS/Android |
| `InnerAudioContext.offSeeked` | 取消监听音频完成 seek 操作的事件 | 1.0.0 | 无需 | iOS/Android |
| `InnerAudioContext.offSeeking` | 取消监听音频开始进行 seek 操作的事件 | 1.0.0 | 无需 | iOS/Android |
| `InnerAudioContext.offStop` | 取消监听 stop 事件 | 1.0.0 | 无需 | iOS/Android |
| `InnerAudioContext.offTimeUpdate` | 取消监听 timeUpdate 事件 | 1.0.0 | 无需 | iOS/Android |
| `InnerAudioContext.offWaiting` | 取消监听音频加载中的事件 | 1.0.0 | 无需 | iOS/Android |
| `InnerAudioContext.onCanplay` | 监听音频进入可以播放状态，但不保证后面可以流畅播放 | 1.0.0 | 无需 | iOS/Android |
| `InnerAudioContext.onEnded` | 监听音频自然播放结束事件 | 1.0.0 | 无需 | iOS/Android |
| `InnerAudioContext.onError` | 监听音频播放错误事件 | 1.0.0 | 无需 | iOS/Android |
| `InnerAudioContext.onPause` | 监听音频暂停事件 | 1.0.0 | 无需 | iOS/Android |
| `InnerAudioContext.onPlay` | 监听音频播放事件 | 1.0.0 | 无需 | iOS/Android |
| `InnerAudioContext.onSeeked` | 监听音频完成 seek 操作的事件 | 1.0.0 | 无需 | iOS/Android |
| `InnerAudioContext.onSeeking` | 监听音频开始进行 seek 操作的事件 | 1.0.0 | 无需 | iOS/Android |
| `InnerAudioContext.onStop` | 监听音频停止播放事件 | 1.0.0 | 无需 | iOS/Android |
| `InnerAudioContext.onTimeUpdate` | 监听音频进度更新事件 | 1.0.0 | 无需 | iOS/Android |
| `InnerAudioContext.onWaiting` | 音频加载中事件，当音频因为数据不足，需要停下来加载时会触发 | 1.0.0 | 无需 | iOS/Android |
| `InnerAudioContext.pause` | 暂停播放 | 1.0.0 | 无需 | iOS/Android |
| `InnerAudioContext.play` | 播放音频 | 1.0.0 | 无需 | iOS/Android |
| `InnerAudioContext.seek` | 跳转到指定位置播放 | 1.0.0 | 无需 | iOS/Android |
| `InnerAudioContext.stop` | 停止播放 | 1.0.0 | 无需 | iOS/Android |
| `RecorderManager.offError` | 取消监听录音错误事件 | 1.0.0 | 无需 | iOS/Android |
| `RecorderManager.offFrameRecorded` | 取消监听已录制完指定帧大小的文件事件 | 1.0.0 | 无需 | iOS/Android |
| `RecorderManager.offPause` | 取消监听录音暂停事件 | 1.0.0 | 无需 | iOS/Android |
| `RecorderManager.offResume` | 取消监听录音继续事件 | 1.0.0 | 无需 | iOS/Android |
| `RecorderManager.offStart` | 取消监听录音开始事件 | 1.0.0 | 无需 | iOS/Android |
| `RecorderManager.offStop` | 取消监听录音停止事件 | 1.0.0 | 无需 | iOS/Android |
| `RecorderManager.onError` | feat/game/new-error-code | 1.0.0 | 无需 | iOS/Android |
| `RecorderManager.onFrameRecorded` | 监听已录制完指定帧大小的文件事件 | 1.0.0 | 无需 | iOS/Android |
| `RecorderManager.onPause` | 监听录音暂停事件 | 1.0.0 | 无需 | iOS/Android |
| `RecorderManager.onResume` | 监听录音继续事件 | 1.0.0 | 无需 | iOS/Android |
| `RecorderManager.onStart` | 监听录音开始事件 | 1.0.0 | 无需 | iOS/Android |
| `RecorderManager.onStop` | 监听录音停止事件 | 1.0.0 | 无需 | iOS/Android |
| `RecorderManager.pause` | 暂停录音 | 1.0.0 | 无需 | iOS/Android |
| `RecorderManager.resume` | 继续录音 | 1.0.0 | 无需 | iOS/Android |
| `RecorderManager.start` | 开始录音 | 1.0.0 | 需用户 | iOS/Android |
| `RecorderManager.stop` | 停止录音 | 1.0.0 | 无需 | iOS/Android |
| `tt.addAudioTrack` | 调用本方法可为本地视频添加额外的音轨 | 2.16.0 | 无需 | iOS/Android |
| `tt.chooseImage` | 从系统相册中选择图片，或使用相机拍摄图片，选取成功后将存入本地临时文件，并在… | 1.0.0 | 无需 | iOS/Android |
| `tt.chooseVideo` | 从系统相册中选择视频，或使用相机拍摄视频，返回视频的临时文件路径 | 1.0.0 | 无需 | iOS/Android |
| `tt.createCamera` | 创建并返回一个 camera 对象实例 | 1.40.0 | 需用户 | iOS/Android |
| `tt.createFaceDetector` | 创建一个 Detector 人脸检测器对象 | 1.37.0 | 无需 | iOS/Android |
| `tt.createHandDetector` | 创建一个手势识别器 Detector 实例对象 | 1.66.0 | 无需 | iOS/Android |
| `tt.createInnerAudioContext` | 创建并返回内部 audio 上下文 innerAudioContext 实例，通过它能够操… | 1.0.0 | 无需 | iOS/Android |
| `tt.createOffscreenVideo` | 创建一个离屏视频对象，与上屏视频对象自动绘制视频不同，离屏对象需要自行绘制 | 1.37.0 | — | — |
| `tt.createVideo` | 创建一个上屏 Video 视频对象 | 1.37.0 | — | — |
| `tt.getAudioContext` | 获取并返回音频处理模块对象 AudioContext | 1.34.0 | 无需 | iOS/Android |
| `tt.getGameRecorderManager` | 获取全局唯一的录屏管理器 ，该功能只能录制到小游戏全局唯一的上屏 canvas 上的内容… | 1.6.1 | 无需 | iOS/Android |
| `tt.getImageInfo` | 获取图片信息 | 1.10.0 | 无需 | iOS/Android |
| `tt.getInnerAudioOption` | 查询小游戏当前音频播放路由状态，包括是否外放及当前音频路由 | 4.26.0 | 无需 | iOS/Android |
| `tt.getRecorderManager` | 获取全局唯一的 recorderManager | 1.6.1 | 无需 | iOS/Android |
| `tt.getRtcEngine` | 能力目前支持抖音和抖音极速版，其他宿主暂未支持 | — | — | — |
| `tt.mergeVideo` | 将视频进行合并 | 2.58.0 | 无需 | iOS/Android |
| `tt.offAudioRouteChange` | 用于取消 onAudioRouteChange 注册的 callback | 4.26.0 | 无需 | iOS/Android |
| `tt.onAudioRouteChange` | 监听小游戏音频播放路由或音频设备变化事件 | 4.26.0 | 无需 | iOS/Android |
| `tt.pauseMicrophone` | 暂停麦克风的使用 | 2.4.0 | 无需 | iOS/Android |
| `tt.previewImage` | 预览一组图片 | 1.0.0 | 无需 | iOS/Android |
| `tt.requestMicrophone` | 向端上发出麦克风请求，调起麦克风功能 | 1.23.0 | 无需 | iOS/Android |
| `tt.resumeMicrophone` | 恢复对系统麦克风的使用，调用该 API 后，会再次获取麦克风设备的权限 | 2.4.0 | 无需 | iOS/Android |
| `tt.saveImageToPhotosAlbum` | 保存图片到系统相册 | 1.0.0 | 无需 | iOS/Android |
| `tt.saveVideoToPhotosAlbum` | 保存视频到系统相册 | 1.0.0 | 无需 | iOS/Android |
| `tt.setInnerAudioOption` | 用于在 RecorderManager 录音会话内设置小游戏音频播放路由优先从扬声器输出 | 4.26.0 | 无需 | iOS/Android |

## Worker

_4 项_

| 方法 | 说明 | 基础库 | 授权 | 平台 |
| --- | --- | --- | --- | --- |
| `Worker.onMessage` | 监听接收 主线程/Worker线程 向当前线程发送的消息 | 1.0.0 | 无需 | iOS/Android |
| `Worker.postMessage` | 向 主线程/Worker线程 发送消息 | 1.0.0 | 无需 | iOS/Android |
| `Worker.terminate` | 结束当前 worker 线程 | 1.0.0 | 无需 | iOS/Android |
| `tt.createWorker` | 创建一个 Worker 线程 | 1.0.0 | 无需 | iOS/Android |

## 数据分析

_2 项_

| 方法 | 说明 | 基础库 | 授权 | 平台 |
| --- | --- | --- | --- | --- |
| `tt.reportAnalytics` | 自定义分析数据上报接口，调用后，会将数据上报到抖音开放平台，开发者可以进入抖音开放平台「数… | 1.8.0 | 无需 | iOS/Android |
| `tt.reportScene` | 自定义启动场景数据上报接口，调用该接口上报场景数据（场景需在开发者后台配置）后，开发者可以… | 2.88.0 | 无需 | iOS/Android |

## 支付

_2 项_

| 方法 | 说明 | 基础库 | 授权 | 平台 |
| --- | --- | --- | --- | --- |
| `tt.openAwemeCustomerService` | 发起抖音钻石支付 | 2.64.0 | 无需 | iOS/Android |
| `tt.requestGamePayment` | 发起支付 | 1.0.0 | — | — |

## 广告

_36 项_

| 方法 | 说明 | 基础库 | 授权 | 平台 |
| --- | --- | --- | --- | --- |
| `BannerAd.destroy` | 销毁广告实例 | 1.3.0 | 无需 | iOS/Android |
| `BannerAd.hide` | 隐藏广告 | 1.3.0 | 无需 | iOS/Android |
| `BannerAd.offError` | 解除绑定 error 事件的监听器 | 1.3.0 | 无需 | iOS/Android |
| `BannerAd.offLoad` | 解除绑定 load 事件的监听器 | 1.3.0 | 无需 | iOS/Android |
| `BannerAd.offResize` | 解除绑定 resize 事件的监听器 | 1.3.0 | 无需 | iOS/Android |
| `BannerAd.onError` | 绑定 error 事件的监听器 | 1.3.0 | 无需 | iOS/Android |
| `BannerAd.onLoad` | 绑定 load 事件的监听器 | 1.3.0 | 无需 | iOS/Android |
| `BannerAd.onResize` | 绑定 resize 事件的监听器 | 1.3.0 | 无需 | iOS/Android |
| `BannerAd.show` | 广告创建后默认是隐藏的，可以通过该方法显示广告 | 1.3.0 | 无需 | iOS/Android |
| `GridGamePanel.destroy` | 销毁游戏推荐组件实例 | 2.82.0 | 无需 | iOS/Android |
| `GridGamePanel.hide` | 隐藏游戏推荐组件 | 2.82.0 | 无需 | iOS/Android |
| `GridGamePanel.offStateChange` | 解绑游戏推荐组件实例状态变化事件的监听器 | 2.82.0 | 无需 | iOS/Android |
| `GridGamePanel.onStateChange` | 绑定游戏推荐组件实例状态变化事件的监听器 | 2.82.0 | 无需 | iOS/Android |
| `GridGamePanel.show` | 展示游戏推荐组件 | 2.82.0 | 无需 | iOS/Android |
| `InterstitialAd.destroy` | 销毁插屏广告实例 | 1.71.0 | 无需 | iOS/Android |
| `InterstitialAd.load` | 加载插屏广告 | 1.71.0 | 无需 | iOS/Android |
| `InterstitialAd.offClose` | 取消监听插屏广告关闭事件 | 1.71.0 | 无需 | iOS/Android |
| `InterstitialAd.offError` | 取消监听插屏错误事件 | 1.71.0 | 无需 | iOS/Android |
| `InterstitialAd.offLoad` | 取消监听插屏广告加载事件 | 1.71.0 | 无需 | iOS/Android |
| `InterstitialAd.onClose` | 监听插屏广告关闭事件 | 1.71.0 | 无需 | iOS/Android |
| `InterstitialAd.onError` | 监听插屏错误事件 | 1.71.0 | 无需 | iOS/Android |
| `InterstitialAd.onLoad` | 监听插屏广告加载事件 | 1.71.0 | 无需 | iOS/Android |
| `InterstitialAd.show` | 显示插屏广告 | 1.71.0 | 无需 | iOS/Android |
| `RewardedVideoAd.destroy` | 通过 destroy 方法主动销毁广告实例 | 1.92.0 | 无需 | iOS/Android |
| `RewardedVideoAd.load` | 通过 load 方法主动预加载广告内容 | 1.3.0 | 无需 | iOS/Android |
| `RewardedVideoAd.offClose` | 解除绑定 close 事件的监听器 | 1.3.0 | 无需 | iOS/Android |
| `RewardedVideoAd.offError` | 解除绑定 error 事件的监听器 | 1.3.0 | 无需 | iOS/Android |
| `RewardedVideoAd.offLoad` | 解除绑定 load 事件的监听器 | 1.3.0 | 无需 | iOS/Android |
| `RewardedVideoAd.onClose` | 绑定 close 事件的监听器 | 1.3.0 | 无需 | iOS/Android |
| `RewardedVideoAd.onError` | 绑定 error 事件的监听器 | 1.3.0 | 无需 | iOS/Android |
| `RewardedVideoAd.onLoad` | 绑定 load 事件的监听器 | 1.3.0 | 无需 | iOS/Android |
| `RewardedVideoAd.show` | 广告创建后默认是隐藏的，可以通过该方法显示广告 | 1.3.0 | 无需 | iOS/Android |
| `tt.createBannerAd` | 开发者可以在小游戏中使用 Banner 广告获得收入 | 1.3.0 | 无需 | iOS/Android |
| `tt.createGridGamePanel` | 创建游戏推荐组件实例 | 2.82.0 | 无需 | iOS/Android |
| `tt.createInterstitialAd` | 创建插屏广告，开发者可以在小游戏中使用插屏广告获得收入 | 1.71.0 | 无需 | iOS/Android |
| `tt.createRewardedVideoAd` | 开发者可以在小游戏中使用 Video 广告获得收入 | 1.3.0 | 无需 | iOS/Android |

## 开放能力

_76 项_

| 方法 | 说明 | 基础库 | 授权 | 平台 |
| --- | --- | --- | --- | --- |
| `FollowButton.destroy` | 销毁关注按钮 | 1.19.0 | 无需 | iOS/Android |
| `FollowButton.hide` | 隐藏关注按钮，调用 FollowButton.show 可重新显示关注按钮 | 1.19.0 | 无需 | iOS/Android |
| `FollowButton.offTap` | 移除指定的按钮点击监听事件 | 1.19.0 | 无需 | iOS/Android |
| `FollowButton.onTap` | 监听按钮点击事件 | 1.19.0 | 无需 | iOS/Android |
| `FollowButton.show` | 显示关注按钮 | 1.19.0 | 无需 | iOS/Android |
| `LiveManager.checkRoomIsValid` | 检查直播间/对应小玩法挂载状态是否有效 | 3.60.0 | 无需 | iOS/Android |
| `LiveManager.getLiveSetting` | 获取直播环境配置信息 | 3.85.0 | 无需 | iOS/Android |
| `LiveManager.getLiveStatus` | 获取关联玩法的主播/直播间信息 | 3.60.0 | 无需 | iOS/Android |
| `LiveManager.navigateToLive` | 跳转到指定直播间 | 3.60.0 | 无需 | iOS/Android |
| `LiveManager.offInstantPlayStatusChange` | 取消监听即看即玩开关状态变化 | 3.85.0 | 无需 | iOS/Android |
| `LiveManager.offXScreenSizeChange` | 取消监听X分屏全屏/半屏切换事件 | 3.60.0 | 无需 | iOS/Android |
| `LiveManager.onInstantPlayStatusChange` | 注册即看即玩开关状态变化监听函数 | 3.85.0 | 无需 | iOS/Android |
| `LiveManager.onXScreenSizeChange` | 监听X分屏全屏/半屏切换事件 | 3.60.0 | 无需 | iOS/Android |
| `LiveManager.syncGameProgress` | 观众侧同步主播游玩进度配置信息 | 3.85.0 | 无需 | iOS/Android |
| `LiveManager.uploadGameProgress` | 上传主播游玩场景配置 | 3.85.0 | 无需 | iOS/Android |
| `OpenDataContext.postMessage` | postMessage 方法用于向开放数据域发送结构化消息，触发数据域内的特定逻辑处理 | — | — | — |
| `tt.addShortcut` | 可以将小游戏快捷方式添加到手机桌面上 | 2.46.0 | 无需 | iOS/Android |
| `tt.authenticateRealName` | 拉起实名认证窗口 | 1.80.0 | 无需 | iOS/Android |
| `tt.authorize` | 向用户请求单项能力授权（如地理位置、摄像头等） | 1.80.0 | 无需 | iOS/Android |
| `tt.bindUnionGroup` | 给指定公会绑定公开群 | 3.51.0 | 无需 | iOS/Android |
| `tt.checkFeedSubscribeStatus` | 查询用户直玩订阅的授权情况 | 3.34.0 | 无需 | iOS/Android |
| `tt.checkFollowAwemeState` | 提供从小游戏查看抖音号是否关注的能力 | 2.70.0 | 无需 | iOS/Android |
| `tt.checkFollowState` | 查看用户是否已关注小游戏绑定的头条号（注意这个头条号是小游戏开发者在开发者平台绑定的官方头… | 1.30.0 | 无需 | iOS/Android |
| `tt.checkGroupInfo` | 查询用户通过小游戏平台创建的群的信息如游戏开发者在平台创建了群聊 ABC，那么游戏侧可以基… | 2.70.0 | 无需 | iOS/Android |
| `tt.checkScene` | 确认当前宿主版本是否支持跳转某个小游戏入口场景，目前仅支持「侧边栏」场景 | 2.92.0 | 无需 | iOS/Android |
| `tt.checkSession` | 用户的登录态具有时效性，随着用户未使用小游戏的时间增加，用户的登录态越容易失效 | 1.0.0 | 无需 | iOS/Android |
| `tt.checkShortcut` | 检查小游戏快捷方式是否已添加到手机桌面上 | 2.46.0 | 无需 | Android |
| `tt.createContactButton` | 创建客服按钮 | 1.55.0 | — | — |
| `tt.createFollowButton` | 创建关注头条号按钮 | 1.19.0 | 无需 | iOS/Android |
| `tt.getCloudStorageByRelation` | 根据关系类型获取与当前用户相关的其他用户托管数据 | 1.11.0 | 无需 | iOS/Android |
| `tt.getFeedData` | 获取游戏是否直玩就绪状态数据 | 3.67.0 | 无需 | iOS/Android |
| `tt.getGameClubData` | 获取游戏站数据 | 3.77.0 | 无需 | iOS/Android |
| `tt.getImRankData` | 获取排序好的「好友/总榜」数据源，开发者基于数据源自行渲染返回的数据 | 2.70.0 | 无需 | iOS/Android |
| `tt.getImRankList` | 获取排行榜列表，调用 API 后， 根据参数自动绘制游戏好友排行榜（ native UI ） | 2.70.0 | 无需 | iOS/Android |
| `tt.getLiveManager` | 获取直播间管理器对象 | 3.60.0 | 无需 | iOS/Android |
| `tt.getOpenDataContext` | 获取开放数据域 | 1.11.0 | 无需 | iOS/Android |
| `tt.getSetting` | 获取用户已经授权过的配置 | 1.3.0 | 无需 | iOS/Android |
| `tt.getSharedCanvas` | 开放数据域下调用，获取主域和开放数据域共享的 canvas | 1.11.0 | 无需 | iOS/Android |
| `tt.getUnionGroupInfo` | 获取公会绑定群信息 | 3.51.0 | 无需 | iOS/Android |
| `tt.getUserCloudStorage` | 获取当前用户托管数据当中对应 key 的数据 | 1.11.0 | 无需 | iOS/Android |
| `tt.getUserGroupTagInfo` | 获取用户群聊标签信息 | 3.80.0 | 无需 | iOS/Android |
| `tt.getUserInfo` | 获取已登录用户的基本信息或特殊信息，首次使用的用户会弹出授权提示窗，若用户同意，则会返回用… | 1.0.0 | 需用户 | iOS/Android |
| `tt.hideShareMenu` | 隐藏转发按钮 | 1.5.0 | 无需 | iOS/Android |
| `tt.joinGroup` | 在平台创建群聊，获得 groupid 后，游戏内通过这个方法引导用户加入抖音群 | 2.70.0 | 无需 | iOS/Android |
| `tt.joinUnionGroup` | 加入指定公会绑定的公开群 | 3.51.0 | 无需 | iOS/Android |
| `tt.login` | 调用该 API 可以获取用户临时的登录凭证 | 1.0.0 | 无需 | iOS/Android |
| `tt.navigateToScene` | 调用该API可以跳转到某个小游戏入口场景，目前仅支持跳转「侧边栏」场景 | 2.92.0 | 无需 | iOS/Android |
| `tt.navigateToVideoView` | 跳转到分享的视频播放页面 | — | — | — |
| `tt.offFeedStatusChange` | 取消监听 Feed 流进入/退出小游戏事件 | 3.59.0 | 无需 | iOS/Android |
| `tt.offShareAppMessage` | 取消监听用户点击右上角菜单的“转发”按钮时触发的事件 | 1.0.0 | 无需 | iOS/Android |
| `tt.onFavoriteStateChange` | 监听用户点击右上角菜单中的【收藏】按钮时触发的事件 | 1.87.0 | 无需 | iOS/Android |
| `tt.onFeedStatusChange` | 监听 Feed 流进入/退出小游戏事件 | 3.59.0 | 无需 | iOS/Android |
| `tt.onMessage` | 在开放数据域中调用，监听主域发送的消息 | 1.11.0 | 无需 | iOS/Android |
| `tt.onNeedPrivacyAuthorization` | 注册隐私授权需要用户确认时的回调 | 4.17.0 | 无需 | iOS/Android |
| `tt.onRealNameAuthenticationComplete` | 监听实名认证成功，在用户未实名的情况下，打开游戏后会主动弹出实名认证弹框，用户完成认证后会… | 2.25.0 | 无需 | iOS/Android |
| `tt.onShareAppMessage` | 本API为被动分享监听操作：监听用户点击平台提供的分享入口时触发的事件（如右上角更多面板中… | 1.0.0 | 无需 | iOS/Android |
| `tt.openAwemeUserProfile` | 跳转个人抖音号主页，用户可以选择关注/取消关注抖音号 | 1.84.0 | 无需 | iOS/Android |
| `tt.openCustomerServiceConversation` | 平台提供的小游戏客服能力，按钮界面由开发者绘制后，点击调用该 api 可拉起客服界面 | 2.66.1 | 无需 | iOS/Android |
| `tt.openFeedback` | 打开反馈页 | 3.76.0 | 无需 | iOS/Android |
| `tt.openSetting` | 打开设置页面，返回用户设置过的授权结果 | 1.3.0 | 无需 | iOS/Android |
| `tt.removeUserCloudStorage` | 删除当前宿主 APP 中有群功能的同玩该游戏的用户托管数据当中对应 key 的数据 | 1.11.0 | 无需 | iOS/Android |
| `tt.requestFeedSubscribe` | 向用户请求授权，允许游戏在满足一定的条件后出现在 Feed 流中 | 3.34.0 | 无需 | iOS/Android |
| `tt.requestSubscribeMessage` | 调起客户端订阅消息界面，返回用户订阅消息的操作结果 | 1.73.0 | 无需 | iOS/Android |
| `tt.setGroupTag` | 设置用户群聊标签 | 3.80.0 | 无需 | iOS/Android |
| `tt.setImRankData` | 在关键的游戏场景，设置写入用户的排行榜数据（游戏成绩信息），该数据会上传到服务端 | 2.70.0 | 无需 | iOS/Android |
| `tt.setImRankDataInOpenContext` | 在关键的游戏场景，设置写入用户的排行榜数据（游戏成绩信息）,该数据会上传到服务端，该方法设… | 2.74.0 | 无需 | iOS/Android |
| `tt.setUserCloudStorage` | 对用户存储的数据进行写入操作, 允许同时写多组 KV 数据 | 1.11.0 | 无需 | iOS/Android |
| `tt.setUserGroup` | 设置用户分组 | 1.17.0 | 无需 | iOS/Android |
| `tt.shareAppMessage` | 本API为主动调用转发相关方法（游戏内主动拉起发布器、好友邀请、录屏分享等） | 1.0.0 | 无需 | iOS/Android |
| `tt.shareMessageToFriend` | 给指定的好友分享游戏信息 | 2.74.0 | 无需 | iOS/Android |
| `tt.showDouyinOpenAuth` | 提供小游戏获取抖音权限的能力，展示出抖音权限授权弹窗 | 1.93.0 | 无需 | iOS/Android |
| `tt.showFavoriteGuide` | 在小游戏内调起关注小游戏的引导组件，用于引导用户关注小游戏 | 1.41.0 | 无需 | iOS/Android |
| `tt.showRevisitGuide` | 调起引导用户复访的提示弹窗，目前仅抖音宿主支持 | 2.94.0 | 无需 | iOS/Android |
| `tt.showShareMenu` | 显示当前小游戏页面的转发按钮 | 1.5.0 | 无需 | iOS/Android |
| `tt.storeFeedData` | 存储游戏是否直玩就绪状态 | 3.67.0 | 无需 | iOS/Android |
| `tt.unbindUnionGroup` | 解除指定公会和公开群的绑定关系 | 3.51.0 | 无需 | iOS/Android |

## 未收录的类与概念页

下列页面不是可调用方法，按需查原文：

`API 概览`、`AnalyserNode`、`Audio`、`AudioBuffer`、`AudioBufferSourceNode`、`AudioContext`、`AudioNode`、`AudioParam`、`AuthSetting`、`BannerAd`、`Camera`、`ContactButton`、`DelayNode`、`DetectData`、`Detector`、`DownloadTask`、`EqualizerNode`、`F0DetectionNode`、`FadingNode`、`FastForwardNode`、`FileSystemManager`、`FollowButton`、`GainNode`、`GameRecorderManager`、`GridAd`、`GridGamePanel`、`HandInfo`、`Image`、`ImageFile`、`InnerAudioContext`、`InteractiveButton`、`InterstitialAd`、`KVData`、`LoadSubpackageTask`、`MediaElementAudioSourceNode`、`MediaStreamAudioSourceNode`、`OpenDataContext`、`OscillatorNode`、`RTC实时语音文档介绍`、`RankResItem`、`RecorderManager`、`RequestTask`、`ReverbNode`、`RewardedVideoAd`、`ShareParam`、`SocketTask`、`Stats`、`StreamFileWriterNode`、`Touch`、`UpdateManager`、`UploadTask`、`Video`、`VolumeDetectionNode`、`Worker`、`tt.getUserGroupTagInfo`、`tt.setGroupTag`、`主动查询订单状态`、`小游戏组队分享能力`、`插屏广告注意事项`、`支付签名生成算法`、`数据分组实现游戏排行`、`服务端回调接口`、`本地数据缓存`、`游戏币扣除接口`、`游戏币赠送接口`、`激励视频广告注意`、`获取游戏币余额`
