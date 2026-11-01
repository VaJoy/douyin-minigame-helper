---
title: "游戏深度保护"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/development-assistance/code-protect
update_time: 2025-01-23
---

《游戏深度保护》是一款小游戏代码保护工具，通过代码加固，混淆，添加水印等方式，提高小游戏代码资产安全水平。

## 使用说明
### 运行环境要求
下载并安装 4.3.5 或更高版本的开发者工具。

### 初始化配置
打开开发者工具，进入小游戏项目，点击 编辑器活动栏 - 实验 - 游戏深度防护 - 初始化配置，将在项目根目录生成一个 `code.fortify.config.json `文件。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/258e570a7e5f41e69510953d3e395a24~tplv-9nona0m7ha-image.image)

### 配置文件说明
- `enable` 代表功能是否开启，其中 `local` 是模拟器场景， `preview` 是真机预览场景，`upload` 是上传场景。
- `obfuscation` 代表代码混淆配置项。
  - `level` 代表不同加固等级，1 最低，3 最高，不同加固等级会影响代码体积与性能，若无特殊要求，建议选择最高等级 3。
  - `files` 代表待加固的文件路径（相对于小游戏工程目录）。
- `watermark` 代表代码水印配置项，**开启水印要求必须进行代码混淆**。

```js
{
    "enable": {
        "local": false,    
        "preview": false,
        "upload": true
    },
    "watermark": {
        "name": "水印保护",
        "files": []
    },
    "obfuscation": {
        "name": "代码混淆",
        "tasks": [
            {
                "level": 1,
                // 以下为文件路径示例
                "files": ["game.js", "js/core.js", "src/lib/index.js"]
            },
            {
                "level": 2,
                "files": []
            },
            {
                "level": 3,
                "files": []
            }
        ]
    }
}
```

> **注意**
> 当 `enable` 字段不存在时，我们会抛出警告 ⚠️ ，并提供默认值（**上传场景默认开启，其余场景默认关闭**）。
> ![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/a9131e135a27489a99f14195be98319e~tplv-9nona0m7ha-image.image)

### 是否开启深度防护
在上传时，出现「已开启代码深度防护」，代表开启成功。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/0befd828b95a49718ff3f253a1083a41~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/df6b778c69e341b1b2ebba2d1b1f15f5~tplv-9nona0m7ha-image.image)

### 使用限制
- **请不要使用第三方平台加固后的产物进行二次加固，因其可能带来安全风险、兼容性问题及不可控的质量隐患。**
- 小于20KB的JS文件可能无法正常添加水印（在添加水印中会被忽略），可以尝试将若干个小JS文件合并，然后再添加水印。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/b7a1e44693f24e5fa853f404d34c76c9~tplv-9nona0m7ha-image.image)

- 大于15MB的JS文件可能无法正常加固，IDE会提示编译器内存占用异常。
  - 可以尝试将它拆分为若干个小JS文件，然后再逐一加固。
  - 可以将混淆等级调低后进行重试。
- 上传场景有最大时间限制，可能会遇到编译超时的错误。
  - 建议精简加固列表，诸如引擎产物，第三方工具包，polyfill 等无需加固。
#### 适用范围
目前只针对于小游戏的 js 代码文件，其它类型的文件（如 ts, json, wasm 等）暂不支持。
