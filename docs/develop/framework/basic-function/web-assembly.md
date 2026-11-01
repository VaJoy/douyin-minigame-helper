---
title: "TTWebAssembly"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/basic-function/web-assembly
update_time: 2025-08-25
---

自基础库版本 3.7.0.0 起，抖音小游戏在 JS 线程和 Worker 线程中提供了全局的 `TTWebAssembly` 对象，支持加载包内经过 brotli 压缩的 wasm 文件（文件后缀为 `*.wasm.br`）。

`TTWebAssembly` 与 Web 标准的 `WebAssembly` 类似，在执行计算密集型任务时，相比 JavaScript 能提供更好的性能表现。

> **平台差异说明**：iOS 平台目前不支持 SIMD 等 WebAssembly 提案特性。

## API 参考

#### `TTWebAssembly.compile(path)`
编译指定的 WebAssembly 模块。

**参数**：
`path` {string}：必须为包内 wasm 文件路径
**返回值**：
返回 Promise 对象：
  - 成功时 resolve 一个 `TTWebAssembly.Module` 实例
  - 失败时 reject（文件读取失败或编译错误）
#### `TTWebAssembly.instantiate(path, importObject)`
创建 WebAssembly 实例。

**参数**：
- `path` {string}：必须为包内 wasm 文件路径
- `importObject` {Object}：可选导入对象
**返回值**：
返回 Promise 对象：
  - 成功时 resolve 包含以下属性的对象：
    - `module`：`TTWebAssembly.Module` 实例
    - `instance`：`TTWebAssembly.Instance` 实例
  - 失败时 reject（文件读取失败、编译错误或导入对象不匹配）
### 核心类

#### `TTWebAssembly.Module`
通过 `TTWebAssembly.compile` 方法构造，功能与 WebAssembly 标准保持一致。

#### `TTWebAssembly.Global`
用于在 JavaScript 和 Instance 之间传递全局状态，实现与 WebAssembly 标准相同。

#### `TTWebAssembly.Table`
用于实现不同 Instance 之间的动态链接，功能与 WebAssembly 标准一致。

#### `TTWebAssembly.Memory`
用于在 JavaScript 和 Instance 之间共享内存，实现与 WebAssembly 标准相同。

#### `TTWebAssembly.Instance`
可通过以下方式构造：
1. `TTWebAssembly.instantiate` 方法
1. `new TTWebAssembly.Instance(module, importObject)` 构造函数
**属性**：
`exports`：包含实例导出的 Table、Global、Memory 或函数
