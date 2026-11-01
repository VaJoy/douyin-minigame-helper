---
title: "命令行调用"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/development-assistance/ide-cli
update_time: 2026-04-14
---

## 介绍
开发者工具提供了命令行供外部调用，开发者可以通过命令行工具进行登录、预览、上传等操作。
小游戏命令行工具已升级至 2.0.0 版本，在命令行使用方式上同 1.x.x 版本一致。默认情况下自 2.0.0 版本起，会采集部分行为数据以帮助我们了解如何更好地改进产品，您也可以通过 set-config 命令来禁止该行为。
命令行工具安装方式：

```js
npm install -g tt-minigame-ide-cli
```

---

## 使用
### 项目对象
> 适用于普通小游戏和 Unity 小游戏新包体格式
项目对象是本模块主要的入参，可以依据下边的定义自行实现。

```typescript
interface TtMinigameIdeCli {
  setConfig: (
    config: { proxy: string; allowReportEvent?: boolean },
    useDefault?: boolean,
  ) => void;
  open: (options: {
    project: { path: string; mode?: 'full' | 'lite' };
  }) => Promise<void>;
  loginByEmail: (options: { email: string; password: string }) => Promise<void>;
  logout: () => Promise<void>;
  preview: (options: {
    project: {
      path: string; // 小游戏项目地址
    };
    page: {
      path: ''; // 不需要填，但是必须要写上一个默认值
    };
    qrcode?: {
      format: 'imageFile'; // 以文件形式保存二维码
      output: string; // 二维码保存地址
    };
    cache: boolean; // 是否使用本地缓存获取二维码
  }) => Promise<{
    shortUrl: string;
    expireTime: number;
    originSchema: string;
  }>;
  upload: (options: {
    project: {
      path: string; // 小游戏项目地址
    };
    qrcode?: {
      format: 'imageFile'; // 以文件形式保存二维码
      output: string; // 二维码保存地址
    };
    changeLog: string; // 此版本的版本日志
    version: string; // 发布的小游戏版本
  }) => Promise<{
    shortUrl: string;
    expireTime: number;
    originSchema: string;
  }>;
}
```

### 设置全局配置
主要用于配置工具的全局代理。
#### 命令行调用

```bash
Usage: tmg set-config [options]

Set tt-ide-cli config

Options:
-p, --proxy <proxy>           Set global proxy（配置全局代理）
--default                     Use default（恢复为默认配置）
-r, --allow-report-event      允许采集使用行为（yes|no），默认为 yes
```

**示例：**

```bash
tmg set-config -p http://localhost:8888 # 配置全局代理为http://localhost:8888

tmg set-config --default # 恢复为默认配置

tmg set-config -r no # 允许采集使用行为no
```

#### 代码调用

```js
const { setConfig } = require('tt-minigame-ide-cli');
setConfig(
  {
    proxy: 'http://localhost:8888', // 配置全局代理为http://localhost:8888
    allowReportEvent: false, // 是否允许采集使用行为
  },
  false, // 是否使用默认的配置
);
```

### 唤起抖音开发者工具
唤起抖音开发者工具，并打开一个小游戏项目。
#### 命令行调用

```bash
Usage: tmg open [options] <project-path>

Open target project by path

Options:
--mode <proxy>           lite | full（使用抖音开发者Lite模式 or 完整模式打开项目）
```

**示例：**

```bash
tmg open /YOUR/PROJECT/PATH --mode lite # 使用lite模式打开一个小游戏项目
```

#### 代码调用

```js
const { open } = require('tt-minigame-ide-cli');
open({
  project: {
    path: '/YOUR/PROJECT/PATH', // 项目路径
    mode: 'lite', // 打开模式 lite or full
  },
});
```

### 登录
登录到开发者平台。支持代理设置。
#### 命令行调用

```bash
Usage: tmg login [options]

Login to the developer platform

Options:

  -m, --mobile         Login by mobile

  -e, --email          Login by email

  -p, --proxy <proxy>  Login with proxy

  -h, --help           output usage information
```

**示例：**

```bash
tmg login -m # 使用手机号登录
tmg login -e # 使用邮箱登录
tmg login -m -p http://localhost:8888 # 使用手机号登录且设置代理为 http://localhost:8888
```

#### 代码调用
手机号登录暂不支持使用代码方式。

```js
const { loginByEmail } = require('tt-minigame-ide-cli');
loginByEmail({
  email: 'xxxx@email.com',
  password: '123456',
})
```

### 通过 email 登录
#### 命令行调用

```js
Usage: tmg login -e [email] [password]

Login to the developer platform by E-mail

Options:

  -p, --proxy <proxy>  Login with proxy

  -h, --help           Output usage information
```

#### 代码调用

```js
Usage: tmg login -e [email] [password]

Login to the developer platform by E-mail

Options:

  -p, --proxy <proxy>  Login with proxy

  -h, --help           Output usage information
```

### 登出（清除本地 session）
#### 命令行调用

```bash
Usage: tmg logout

Logout and clear the session.
```

#### 代码调用

```js
const { logout } = require('tt-minigame-ide-cli');

logout();
```

### 预览小游戏
将项目上传后，扫码二维码来预览小游戏。
#### 命令行调用

```js
Usage: tmg preview [options] [entry]

preview project by remote

Options:

  -f, --force          Preview project without local cache(deprecated)

  --disable-cache      Preview project without local cache

  -s, --small          Use small QR Code, but it does not take effect in some environments

  -u, --copy           Copy remote url to clipboard

  -p, --proxy <proxy>  Preview with proxy

  -h, --help           output usage information

  -o, --output <path>  QRCode image output path
```

**示例：**

```bash
tmg preview /YOUR/PROJECT/PATH \
    -f \ # 不使用本地缓存获取二维码
    --disable-cache \ # 不使用本地缓存获取二维码
    -s \ # 展示小的二维码，在某些环境下不生效
    -u \ # 是否粘贴二维码的url到剪切板
    -p http://localhost:8888 \ # 预览时使用代理http://localhost:8888
    -o /OUTPUR/QRCODE # 将二维码保存为本地文件
```

#### 代码调用

```js
const { preview, setConfig } = require('tt-minigame-ide-cli');

(async () => {
    // 如果需要使用代理，先调用setConfig
   setConfig(
    {
      proxy: 'http://localhost:8888', // 配置全局代理为http://localhost:8888
    },
    false // 是否使用默认的配置
  );
  const res  = await preview({
    project: {
      path: '/YOUR/PROJECT/PATH', // 小游戏项目地址
    },    
    page: {
      path: '',
    },
    qrcode: {
      format: 'imageFile', // 以文件形式保存二维码
      output: './xxxx.png', // 二维码保存地址
    },
    cache: false, // false：不使用本地缓存获取二维码
  });
  console.log(res); // res中包含的shortUrl即为预览二维码字符串
})();
```

### 上传项目
把项目上传到开发者平台进行发布。
#### 命令行调用

```js
Usage: tmg upload [options] [entry]

upload project to the developer platform

Options:

  -v, --app-version <version>  App version (eg: [major].[minor].[patch])

  -c, --app-changelog <log>    Changelog for this version

  -p, --proxy <proxy>          Update request proxy

  -u, --copy                  Copy remote url to clipboard

  -h, --help                   output usage information

  -o, --output <path>          QRCode image output path
  --channel <channel>          Test Channel
  -b, --background-color <bgColor>  QRCode image output with custom background
                                    color. Color value must be in hex format
                                    (RGBA).For example, solid white color is
                                    '#ffffffff'. (default: "#ffffff00")
```

**示例：**

```bash
tmg upload /YOUR/PROJECT/PATH \
    -v 0.0.1 \ # 发布的小游戏版本
    -c "update change log" \ # 此版本的版本日志
    -u \ # 是否粘贴二维码的url到剪切板
    -p http://localhost:8888 \ # 预览时使用代理http://localhost:8888
    -o /OUTPUR/QRCODE # 将上传后的二维码保存为本地文件
    --channel 1 # 测试通道参数，允许多个测试版本小游戏同时存在。需要传入1-24的整数，不传为默认通道。上传后                  可在开发者管理后台的版本管理界面查看多个测试版本
    -b "#ffffffff" # 输出的二维码图片背景色（16进制rgba格式）
```

#### 代码调用

```js
const { upload } = require('tt-minigame-ide-cli');
(async () => {
  const res = await upload({
    project: {
      path: '/YOUR/PROJECT/PATH', // 小游戏项目地址
    },
    qrcode: {
      format: 'imageFile', // 以文件形式保存二维码
      output: './xxxx.png', // 二维码保存地址
    },
    changeLog: 'xxxxxxxx', // 此版本的版本日志
    version: '1.0.4', // 发布的小游戏版本
    channel: '1', // 测试通道，需要传入1-24的整数字符串，不传为默认通道
    bgColor: '#ffffffff' // 输出的二维码图片背景色（16进制rgba格式）
  });
  console.log(res);
})();
```

##### 注：
1. 测试版本最多允许 25 个版本存在。需要传入 1-24 的整数字符串；如果不传入 channel 参数，为默认通道。
1. 上传多测试版本，需要保证 tt-minigame-ide-cli 版本为 2.0.12 及以上。
### 获取项目版本
获取项目线上版本号，暂不支持代码调用方式获取项目版本号。
#### 命令行使用

```js
Usage: tmg version [entry]

Get latest released version of project
```

## Unity 小游戏旧包体格式
- 使用 tt-minigame-ide-cli 预览或上传 Unity 项目，请确保 tt-minigame-ide-cli 版本为 **2.0.10** 或以上。
- 当选择安卓 Native 相关方案时，编译时间较长，请耐心等待。
- Unity依赖项目文件夹下的`project.config.json`和`game.json`文件。
**project.config.json：**

```json
{
    "appid": "ttf1*********07", // unity appid
    "projectname": "sc-test2", 
    "unity": {
        "build": {
            "webgl": "/Users/bytedance/Downloads/testapp/webgl_package-20240615_123123.zip", // webgl产物文件。在预览时需要修改为生成的prepare包的路径
            "native": {
                "il2cpp": "/Users/bytedance/Downloads/testapp/upload/il2cppOutput.zip", // native 产物文件，上传时使用
                "apk": "/Users/bytedance/Downloads/testapp/upload/launcher-release.apk",// native 产物文件，上传时使用
                "fullApk": "/Users/bytedance/Downloads/testapp/upload/launcher-release.apk" // 预览调试时使用的安卓 native apk文件 
            },
            "instantGame": "/Users/bytedance/Downloads/testapp/TCE PublishServer Config.json" // ig 游戏 json 文件
        },
        "publishType": "2", // 发布方案，0：安卓原生，1：安卓原生+iOS WebGL，2：安卓WebGL+iOS WebGL，3： 安卓WebGL，4：安卓InstantGame，5：安卓InstantGame+iOS WebGL
        "starkSdkVersion": "Without StarkSDK", // sc stark tool生成，无需修改
        "unityToolsVersion": "", // sc stark tool生成，无需修改
        "unityEngineVersion": "2021.3.14f1", // sc stark tool生成，无需修改
        "arch": "both" // sc stark tool生成，无需修改
    }
}
```

**game.json：**

```json
{ 
    "deviceOrientation": "portrait", // portrait，竖屏; landscape，浅色
    "menuButtonStyle": "dark"  // dark，深色；light，浅色
}
```

### 预览

> **注意**
> 在运行 *tmg preview* 命令前，需要将project.config.json中的unity -< build -> webgl字段修改为prepare包的绝对路径。prepare包的生成方法参照[此文档](https://www.npmjs.com/package/@open-dy/tt-wasmsplit-ci)中的《开启分包》部分。

#### 命令行调用

```js
Usage: tmg preview [options] [entry]

preview project by remote

Options:

  -p, --proxy <proxy>  Preview with proxy

  -h, --help           output usage information

  -o, --output <path>  QRCode image output path
  
```

**示例：**

```bash
tmg preview /YOUR/PROJECT/PATH  # 这里的path是项目工程的根目录。该目录下应该有一个project.config.json的文件
tmg preview /YOUR/PROJECT/PATH  -o /PREVIEW/QRCODE/PATH # 预览并保存预览二维码到本地
```

#### 代码调用

```js
const { unity } = require('tt-minigame-ide-cli');
(async () => {
    const result = await unity.preview({
    projectPath: '/YOUR/PROJECT/PATH',  //这里的path是项目工程的根目录。该目录下应该有一个project.config.json的文件
    output: '/PREVIEW/QRCODE/PATH',
  });
  console.info(result);
})();
```

### 上传
#### 命令行调用

```bash
Usage: tmg upload [options] [entry]

upload project to the developer platform

Options:

  -v, --app-version <version>  App version (eg: [major].[minor].[patch])

  -c, --app-changelog <log>    Changelog for this version

  -p, --proxy <proxy>          Update request proxy

  -h, --help                   output usage information

  -o, --output <path>          QRCode image output path
  --channel <channel>          Test Channel
  -b, --background-color <bgColor>  QRCode image output with custom background
                                    color. Color value must be in hex format
                                    (RGBA).For example, solid white color is
                                    '#ffffffff'. (default: "#ffffff00")
```

**示例：**

```bash
tmg upload /YOUR/PROJECT/PATH \
    -v 0.0.1 \ # 发布的unity版本
    -c "update change log" \ # 此版本的版本日志
    -o /OUTPUR/QRCODE # 将上传后的二维码保存为本地文件
    --channel 1 # 测试通道参数，允许多个测试版本小游戏同时存在。需要传入1-24的整数，不传为默认通道。上传后                  可在开发者管理后台的版本管理界面查看多个测试版本
    -b "#ffffffff" # 输出的二维码图片背景色（16进制rgba格式）
```

#### 代码调用

```js
const { unity } = require('tt-minigame-ide-cli');
(async () => {
  await unity.upload({
    projectPath: '/YOUR/PROJECT/PATH', // 项目路径
    output: '/PREVIEW/QRCODE/PATH', // 测试二维码存储到本地
    version: '5.5.20', // 发布版本
    publishDesc: '上传日志', // 发布日志
    channel: '1', // 测试通道
    bgColor: '#ffffffff' // 输出的二维码图片背景色（16进制rgba格式）
  });
})();
```

##### 注：
1. 测试版本最多允许 25 个版本存在。需要传入 1-24 的整数字符串；如果不传入 channel 参数，为默认通道。
1. 上传多测试版本，需要保证 tt-minigame-ide-cli 版本为 2.0.12 及以上。
1. 上传需要为协作者开通至少**管理可编辑**和**开发可查看**权限。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/1492089b3b4340a59967e1910da0824f)

1. [Unity 新包体格式](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/install-connect/unity-new) 需要保证 tt-minigame-ide-cli 版本为 2.1.1 及以上，具体调用方式与普通小游戏相同；Unity 旧包体格调用方式与之前保持不变 。
