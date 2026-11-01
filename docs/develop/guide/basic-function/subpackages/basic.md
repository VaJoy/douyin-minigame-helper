---
title: "分包加载"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/basic-function/subpackages/basic
update_time: 2026-02-10
---

> 基础库 1.88.0 及以上版本开始支持，开发者工具请使用大于等于 2.0.6 的版本，推荐使用最新版本，可[点击下载](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/developer-instrument/developer-instrument-update-and-download)。
## 使用方法
1. 分包配置
假设游戏的目录结构如下：

```text
├── game.js
├── game.json
├── images
│   ├── a.png
│   ├── b.png
├── stage1
│   └── game.js
│   └── images
│       ├── 1.png
│       ├── 2.png
└── stage2.js
```

`game.json` 中的配置：
> 注意这里 subPackages 是驼峰命名

```json
{
  ...
  "subPackages": [
    {
      "name": "stage1",
      "root": "stage1/" // 可以指定一个目录，目录根目录下的 game.js 会作为入口文件，目录下所有资源将会统一打包
    }, {
      "name": "stage2",
      "root": "stage2.js" // 也可以指定一个 JS 文件
    }
  ]
  ...
}
```

`subPackages` 中，每个分包的配置有以下几项：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| name | string | 分包别名，[tt.loadSubpackage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/subpackages/tt-loadsubpackage)可以使用 |
| root | string | 分包根目录或者 js |

1. 分包加载
通过 [tt.loadSubpackage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/subpackages/tt-loadsubpackage) API 来触发分包的下载，调用 [tt.loadSubpackage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/subpackages/tt-loadsubpackage) 后，将触发分包的下载与加载（如果分包指定的是一个目录，则自动加载目录下的 game.js, 如果分包指定的是一个 js 文件，则自动加载该 js 文件），在加载完成后，通过 [tt.loadSubpackage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/subpackages/tt-loadsubpackage) 的 success 回调来通知加载完成。
同时，[tt.loadSubpackage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/subpackages/tt-loadsubpackage) 会返回一个 [LoadSubpackageTask](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/subpackages/LoadSubpackageTask)，可以通过 [LoadSubpackageTask](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/subpackages/LoadSubpackageTask) 获取当前下载进度。
示例代码：

```text
const loadTask = tt.loadSubpackage({
  name: 'stage1', // 填写 game.json 中 subPackages 填写的分包名称 name
  success: function(res) {
    // 分包加载成功后通过 success 回调
  },
  fail: function(res) {
    // 分包加载失败通过 fail 回调
  }
});

loadTask.onProgressUpdate(res => {
  console.log('下载进度', res.progress);
  console.log('已经下载的数据长度', res.totalBytesWritten);
  console.log('预期需要下载的数据总长度', res.totalBytesExpectedToWrite);
});
```

## 打包原则
配置在 `subPackages` 字段内的目录或 js 文件，将按照配置打包成一个个「分包」，没有配置在 `subPackages` 中的目录和 js，将会被打包到主包中。

## 引用原则
- stage1 无法引用 stage2 的 JS 文件，但可以引用自己 package 内的 JS 文件
- stage1 无法使用 stage2 的资源，但可以使用自己 package 内的资源

## 低版本兼容
由抖音小游戏后台编译来处理旧版本客户端的兼容，后台会编译两份代码包，一份是分包后代码，另外一份是整包的兼容代码。新客户端用分包，老客户端还是用的整包，完整包会把各个 `subPackages` 里面的资源打包在一起。开发者可以通过以下代码进行兼容

```text
// 如果需要动态加载分包下的一个 js, 假设是 stage1 是一个分包目录
if (tt.loadSubpackage) { // 新版本支持分包，有 tt.loadSubpackage API，代码包被打成了多个包，需要调用 tt.loadSubpackage 加载对应的 js
    tt.loadSubpackage({
        name: 'stage1',
        success: function (res) {
            require('stage1/a.js');//这里可以加载分包中的其他非入口文件,并且没有被加载过的
        }
    });
} else { // 老版本不支持分包，没有 tt.loadSubpackage API, 代码包被打成了整包，直接加载即可
    require('stage1/a.js');
}
```

## 提升用户体验建议
启动阶段如需加载分包，建议展示加载进度。
展示出加载进度的场景，能避免用户加载较大分包时出现的黑屏情况，长时间的黑屏会导致黑屏流失率上升。
