---
title: "新手教程"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/dev-guide/newbie-tutorial
update_time: 2025-12-23
---

本教程将引导你创建一个最简单的 **“点一点”** 游戏，目标是让新手了解整个开发流程。
完整代码: [开发者工具中预览](https://developer.open-douyin.com/ide/minicode/9dd1ed46257a621de7b34372865c9683)

## **第一步：准备阶段 - 了解技术与环境**
抖音小游戏是基于抖音生态的轻量化游戏应用，依托平台流量、社交传播和即时体验优势，实现快速获量和高用户留存。其核心特点包括：
•**即点即玩：**点击秒开，无需下载，适配多终端及横竖屏。
•**平台流量赋能**：算法精准推荐，多入口曝光（短视频挂载、直播小摇杆、游戏中心等），支持付费+自然流量结合。
•**低门槛开发**：主流引擎兼容（Cocos/Unity），提供账号授权、支付变现（IAP + IAA）及数据分析能力。
•**社交裂变驱动**：短视频自动生成传播（如通关录像）+ 强邀请机制（组队奖励/好友排行榜）。
•**轻量化运营**：单局 3 分钟内，快速迭代热点活动（如节日玩法）并通过A/B测试优化分享策略。

**核心技术：**
- **JavaScript**: 游戏逻辑的编程语言。
- **Canvas 2D**: 用于在网页上绘制图形的API，用来绘制游戏画面。
- **抖音小游戏开放平台**: 提供发布、运营和特定API（如分享、振动）的平台。

**准备工作：**
1. 前往抖音开放平台，注册一个开发者账号。可参考 [注册与入驻](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/minigame/register)
1. 下载并安装“抖音小游戏开发者工具”。下载地址： [抖音开放平台官网](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/developer-instrument-update-and-download)
1. 在开发者工具中，创建一个新的小游戏项目。模板通常会提供一个“Hello World”示例。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/81b0edbffe8045d9b372fb4100a41308~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/a09d61aa342042d7a755ef29afe22bb6~tplv-9nona0m7ha-image.image)

## **第二步：理解项目结构**
当你创建一个新项目后，你会看到类似这样的文件结构：

```json
my-douyin-game/
├── game.js          // 小游戏的主入口文件
├── game.json        // 小游戏的配置文件（窗口、页面等）
├── icon.png        // icon
└── project.config.json // 
```

- `game.js`: 程序启动的第一个文件，它负责初始化游戏。
- `game.json`: 非常重要！这里配置小游戏的窗口大小、初始页面、网络超时时间等。
- `project.config.json`：是小游戏的项目配置文件，主要包括了针对小游戏项目配置的一些信息，例如项目名称，App ID，项目配置等内容。这些内容可以在开始创建项目的过程中通过开发者工具生成，开发者也可以根据需要进行修改和配置。详见[项目配置文件](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/code-edit/project-config)

## **第三步：编写代码 - 创建“点一点”游戏**
让我们开始编写一个最简单的游戏。
**1. 修改 **`game.json`
确保你的 `game.json` 配置正确，特别是 `deviceOrientation` 要设置为 `"portrait"`（竖屏），因为抖音小游戏主要在竖屏下体验。

```json
{
    "deviceOrientation": "portrait",
    "showStatusBar": false,
    "networkTimeout": {
        "request": 5000
    }
}
```

**2. 编写主逻辑 ****(**`game.js`**)**
我们将所有代码写在 `game.js` 中。

```js
// game.js

class ClickGame {
  constructor() {
    this.canvas = tt.createCanvas();
    this.ctx = this.canvas.getContext("2d");
    this.init();
  }

  async init() {
    // 初始化配置
    this.config = {
      targetScore: 10,
      totalTime: 10,
      blockSize: 100,
    };

    this.blockSize = 100; // 方块的大小
    this.blockX = 0;
    this.blockY = 0; // 方块的坐标

    this.score = 0;
    this.timeLeft = this.config.totalTime;

    // 初始化方块位置
    this.initBlockPosition();

    // 开始游戏循环
    this.gameLoop();
  }

  initBlockPosition() {
    this.blockX = (this.canvas.width - this.config.blockSize) / 2;
    this.blockY = (this.canvas.height - this.config.blockSize) / 2;
  }

  gameLoop() {
    this.draw();
    requestAnimationFrame(() => this.gameLoop());
  }

  // 绘制图片方块
  drawBlock() {
    this.ctx.fillStyle = "#ff4d4f";
    this.ctx.fillRect(this.blockX, this.blockY, this.blockSize, this.blockSize);
  }

  draw() {
    // 清空画布
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

    // 绘制方块
    this.drawBlock();

    // 绘制UI
    this.drawUI();
  }

  drawUI() {
    // 绘制分数
    this.ctx.fillStyle = "#000000";
    this.ctx.font = "20px Arial";
    this.ctx.textAlign = "left";
    this.ctx.fillText(`分数: ${this.score}/${this.config.targetScore}`, 20, 30);
  }

  handleClick(x, y) {
    // 检测点击
    if (this.isBlockClicked(x, y)) {
      this.score++;

      // 移动方块到随机位置
      this.moveBlockRandomly();
    }
  }

  isBlockClicked(x, y) {
    return (
      x > this.blockX &&
      x < this.blockX + this.config.blockSize &&
      y > this.blockY &&
      y < this.blockY + this.config.blockSize
    );
  }

  moveBlockRandomly() {
    this.blockX = Math.random() * (this.canvas.width - this.config.blockSize);
    this.blockY = 100 + Math.random() * (this.canvas.height - 200);
  }
}

// 初始化游戏
const game = new ClickGame();

// 触摸事件
tt.onTouchStart((e) => {
  const touch = e.touches[0];
  game.handleClick(touch.clientX, touch.clientY);
});
```

## **第四步：测试与调试**
1. **在模拟器中测试**：在开发者工具的左侧是模拟器，你可以直接点击屏幕上的红色方块，看分数是否会增加，方块是否会移动。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/61dd5d6d7ff540d9a633aa3aa8e683d9~tplv-9nona0m7ha-image.image)

1. **真机预览**：这是**非常重要**的一步！
  - 在开发者工具顶部，点击“真机预览”。
  - 用你的抖音App扫描生成的二维码。
  - 在手机抖音里体验你的游戏，确保触摸、显示等一切正常

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/0a9de504b71840ebba525994240e8216~tplv-9nona0m7ha-image.image)

1. **使用调试器**：开发者工具提供了类似Chrome浏览器的调试功能，你可以设置断点、查看Console日志、监控网络请求等。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/3e95984b084b4a2c8a337811c96cc598~tplv-9nona0m7ha-image.image)

## **第五步：完善与优化**
现在你的核心功能已经完成，可以添加更多元素让它更像一个完整的游戏：
- **使用图片资源**：用精美的图片代替纯色方块。

```js
// 图片资源管理
const resources = {
  blockImage: null,
  loaded: 0,
  total: 0,
};

// 加载图片函数
function loadImage(src) {
  return new Promise((resolve, reject) => {
    const img = new Image();
    img.onload = () => resolve(img);
    img.onerror = reject;
    img.src = src;
  });
}

// 初始化图片资源
async function initResources() {
  try {
    resources.blockImage = await loadImage("imgs/block.png");
    console.log("资源加载完成");
  } catch (error) {
    console.error("资源加载失败:", error);
  }
}

class ClickGame {
...

async init() {
    ...
    // 初始化资源
    await initResources();
    ...
}

   // 绘制图片方块
  drawBlock() {
    if (resources.blockImage) { // 改动
      this.ctx.drawImage(
        resources.blockImage,
        this.blockX,
        this.blockY,
        this.blockSize,
        this.blockSize
      );
    } else {
      // 备用纯色方块
      this.ctx.fillStyle = "#ff4d4f";
      this.ctx.fillRect(
        this.blockX,
        this.blockY,
        this.blockSize,
        this.blockSize
      );
    }
  }

...
}
```

- **加入音效**：使用 `tt.createInnerAudioContext()` 在点击时播放音效。
新建文件`src/audioManager.js`

```js

// 音效管理
const audioManager = {
    clickSound: null,
    backgroundMusic: null,
    
    init() {
      // 点击音效
      this.clickSound = tt.createInnerAudioContext();
      this.clickSound.src = 'audio/click.mp3';
      
      // 背景音乐
      this.backgroundMusic = tt.createInnerAudioContext();
      this.backgroundMusic.src = 'audio/bgm.mp3';
      this.backgroundMusic.loop = true;
      
    },
    
    playClick() {
      if (this.clickSound) {
        this.clickSound.seek(0);
        this.clickSound.play();
      }
    },
    
    
    playBackgroundMusic() {
      if (this.backgroundMusic) {
        this.backgroundMusic.play();
      }
    },
    
    stopBackgroundMusic() {
      if (this.backgroundMusic) {
        this.backgroundMusic.stop();
      }
    }
  };

  exports.audioManager = audioManager;
```

```js
// game.js

const { audioManager } = require("./src/audioManager.js");

class ClickGame {
    ...

    async init() {
        ...
        // 初始化资源
        audioManager.init();
        audioManager.playBackgroundMusic();
        ...
    }
    
    handleClick(x, y) {
        // 检测点击
        if (this.isBlockClicked(x, y)) {
          this.score++;
          audioManager.playClick(); // 新增
    
          // 移动方块到随机位置
          this.moveBlockRandomly();
        }
      }

}
```

- **添加倒计时**：限制在10秒内能得多少分。

```js

class ClickGame {
    ...
    init() {
        // 初始化配置
        this.config = {
          targetScore: 10,
          totalTime: 10,
          blockSize: 100,
        };
        this.timeLeft = this.config.totalTime;
        this.isGameOver = false;
        this.isVictory = false;
        
        ...
        this.startTimer();
    }
    
    startTimer() {
        this.timer = setInterval(() => {
          this.timeLeft--;
    
          if (this.timeLeft <= 0) {
            this.gameOver();
          }
        }, 1000);
      }
    
    drawUI() {
        ...
        // 绘制倒计时
        this.ctx.fillStyle = this.timeLeft <= 3 ? "#FF0000" : "#000000";
        this.ctx.textAlign = "right";
        this.ctx.fillText(`时间: ${this.timeLeft}秒`, this.canvas.width - 20, 30);
    }
    
      gameOver() {
        this.isGameOver = true;
        this.isVictory = false;
        clearInterval(this.timer);
      }
}
```

- **接入抖音API**：实现分享、震动等功能，这需要阅读官方文档。

```js
// src/douyinAPI.js

// 抖音API集成
const douyinAPI = {
    // 初始化
    init() {
      this.initShare();
    },
    
    // 分享功能
    initShare() {
      // 监听分享按钮
      tt.showShareMenu({
        success(res) {
          console.log("已成功显示转发按钮");
        },
        fail(err) {
          console.log("showShareMenu 调用失败", err.errMsg);
        },
        complete(res) {
          console.log("showShareMenu 调用完成");
        },
      });

      
      tt.onShareAppMessage(() => {
        return {
          title: '自定义分享标题',
          success() {
            console.log("分享成功");
          },
          fail(e) {
            console.log("分享失败", e);
          },
        };
      });
    },
    
    
    // 振动反馈
    vibrate() {
      if (tt.vibrateShort) {
        tt.vibrateShort();
      }
    }
  };

  exports.douyinAPI = douyinAPI;
```

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/c4db3ee7f87e4ff8931fe5ea8de398fe~tplv-9nona0m7ha-image.image)

## **第六步：上传与发布**
1. **在开发者工具中点击“上传”**：填写版本号和更新日志。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/596abaec04ae4bfd8c6bf0cedb6f538f~tplv-9nona0m7ha-image.image)

1. **前往抖音开放平台后台**：
  - 在你的应用下，会看到上传的版本。
  - 提交审核。审核人员会测试你的游戏是否合规、体验是否流畅。
审核通过后，你就可以自行发布上线了！

## **总结与建议**
恭喜你！你已经完成了第一个抖音小游戏的开发。这个简单的“点一点”游戏包含了小游戏开发的所有核心概念：
- **初始化** -> `init()`
- **游戏循环** -> `gameLoop()` 和 `requestAnimationFrame`
- **绘制** -> `draw()` 和 Canvas API
- **用户交互** -> `tt.onTouchStart`
- **游戏逻辑** -> 分数计算、碰撞检测

**给新手的下一步建议：**
1. **阅读官方文档**：这是最重要的学习途径，了解所有可用的API。
1. **学习游戏引擎**：对于更复杂的游戏，推荐使用**Cocos Creator **或 Unity。它们提供了强大的编辑器、物理引擎、动画系统，能极大提升开发效率。
1. **模仿经典游戏**：尝试复刻“2048”、“Flappy Bird”、“打飞机”等简单经典的游戏，这是极好的练习方式。

祝你开发顺利，在抖音小游戏的生态中创造出让千万用户喜爱的作品！

const blockImage = wx.createImage();
blockImage.src = ‘imgs/block.png’;
blockImage.onload = () => {
// 在draw函数中使用 ctx.drawImage(blockImage, blockX, blockY, blockSize, blockSize);
};

// 在点中方块的判断里添加
if (score >= 10) {
ctx.fillStyle = ‘green’;
ctx.font = ‘40px Arial’;
ctx.fillText(‘游戏胜利！’, canvas.width/2 - 100, canvas.height/2);
// 停止游戏循环或重置游戏
}
