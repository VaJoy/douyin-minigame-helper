---
title: "项目配置文件"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/code-edit/project-config
update_time: 2025-06-16
---

`project.config.json`是小游戏的项目配置文件，主要包括了针对小游戏项目配置的一些信息，例如项目名称，App ID，项目配置等内容。这些内容可以在开始创建项目的过程中通过开发者工具生成，开发者也可以根据需要进行修改和配置。
## 配置项说明

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| appid | string | 小游戏的 AppID |
| setting | object | 项目配置 |
| projectname | string | 项目名称 |
| packOptions | object | 打包配置选项 |
| scripts | boolean | 启用自定义处理命令 |

## setting
在 setting 中可配置以下选项：

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| es6 | boolean | 是否启用 es6 转 es5 |
| urlCheck | boolean | 不校验合法域名、web-view（业务域名）、TLS 版本以及 HTTPS 证书 |
| autoCompile | boolean | 修改文件的时候自动编译 |
| mockUpdate | boolean | 下次编译时模拟系统更新 |
| mockLogin | boolean | 开启宿主登录模拟 |
| compileHotReLoad | boolean | 是否开启热重载 |
| nativeCompile | boolean | 是否开启原生语言快速编译 |

## packOptions
> 注：此配置自 4.2.7 版本起支持。
`packOptions` 用以配置项目在打包过程中的选项。
目前该配置支持`include`和`ignore`两个配置，其中`include`用以配置打包过程中需要强制包含的文件（仅限后缀名符合白名单规则的文件），匹配的这些文件将会出现在预览或上传的结果内（该字段的优先级高于 ignore 字段）。`ignore`用以配置打包过程中需要忽略的文件，被忽略的文件不会出现在预览或上传的结果内，并且包体积计算时也会忽略这些文件。
`packOptions.ignore` 和 `packOptions.include` 为一对象数组，对象元素类型如下：

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| value | string | 路径或匹配规则 |
| type | string | 类型 |

其中，`type` 可以取的值为 `folder`、`file`、`suffix`、`prefix`、`regexp`、`glob`，分别对应文件夹、文件、后缀、前缀、正则表达式、Glob 规则。
**注：**`value` 字段的值若表示文件或文件夹路径，以小游戏目录为根目录。
示例配置如下。

```json
{
    "packOptions": {
        "ignore": [
            { "type": "file", "value": "test-folder/test.js" },
            { "type": "folder", "value": "test-folder" },
            { "type": "suffix", "value": ".jpeg" },
            { "type": "prefix", "value": "img" },
            { "type": "glob", "value": "test-folder/**/*.js" },
            { "type": "regexp", "value": "\\.sjs$" }
         ]
    }
}
```

// xxx.js has been hided by project.config.json

|____app.ttss
|____app.json
|____project.config.json
|____pages
|       |____index
|       |        |____index.js
|       |        |____index.json
|       |        |____index.ttml
|       |        |____index.ttss
|____app.js

{
"packOptions": {
"ignore": [{
"type": "file",
"value": "test/test.js"
}, {
"type": "folder",
"value": "test"
}, {
"type": "suffix",
"value": ".webp"
}, {
"type": "prefix",
"value": "test-"
}, {
"type": "glob",
"value": "test/**/*.js"
}, {
"type": "regexp",
"value": "\\.jsx$"
}]
}

{
"pages":["pages/index/index"]
}

{
"description": "项目配置文件",
"watchOptions": {
"ignore": [
"utils/util.js",
"libs/**/**"
]
}

{
"setting":{
"useCompilerPlugins":["typescript"]
}

{
"setting": {
"useCompilerPlugins": [
"typescript",
"less"
]
}

{
"navigationBarBackgroundColor":"#ffffff",
"navigationBarTextStyle":"black",
"navigationBarTitleText":"头条接口功能演示",
"backgroundColor":"#eeeeee",
"backgroundTextStyle":"light",
"usingComponents":{
"my-component":"path/to/a/custom/component"
},
"hideAnchorButton":false,
"hideAnchorButtonConfig":{
"023009":true，
"021014":false，
"021017":true
}

{
"publishVideoHookPriorityList": ["onUploadDouyinVideo", "onShareAppMessage"]
}

{
"entryPagePath":"pages/index/index"
}

{
"pages":["pages/index/index","pages/logs/logs"],
"window":{
"navigationBarTitleText":"Demo"
},
"tabBar":{
"list":[
{
"pagePath":"pages/index/index",
"text":"首页"
},
{
"pagePath":"pages/logs/logs",
"text":"日志"
}
]
},
"permission":{
"scope.userLocation":{
"desc":"用于提供个性化服务及体验"
}
},
"networkTimeout":{
"request":60000,
"connectSocket":60000,
"uploadFile":60000,
"downloadFile":60000
},
"cookie":{
"enableStore":true
},
"skeleton":{
"page":{
"pages/index/index":"pages/index/index.sk"
},
"config":{
"timeout":1500
}
},
"resizable":true
}

{
"miniprogramRoot": "./src",
"qcloudRoot": "./svr",
"setting": {
"postcss": true,
"es6": true,
"minified": true,
"urlCheck": false,
"checkSiteMap": true,
"enhance": true,
"babelSetting": {
"ignore": [
"utils/something_not_to_process.js",
"miniprogram_npm/*",
"utils/already_handle/*"
]
}
},
"packOptions": {
"ignore": []
},
"debugOptions": {}
}
