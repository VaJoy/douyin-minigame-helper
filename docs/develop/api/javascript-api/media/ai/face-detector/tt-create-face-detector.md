---
title: "tt.createFaceDetector"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/ai/face-detector/tt-create-face-detector
update_time: 2025-01-02
---

基础库 1.37.0 开始支持本方法，这是一个**同步**方法。
创建一个 Detector 人脸检测器对象 。

## 示例代码
【代码示例 1】：原生接入示例
```js
const canvas = tt.createCanvas();
const ctx = canvas.getContext("2d");
class Game {
  constructor() {
    this.init();
    this.startCamera();
    this.run();
  }
  init() {
    this.camera = tt.createCamera();
    this.detector = tt.createFaceDetector();
    this.handleDetectionResult();
    tt.setKeepScreenOn();
    this.frame = 0;
  }
  startCamera() {
    this.camera.setBeautifyParam(1, 1, 1, 1);
    this.camera
      .start("front", true)
      .then((video) => {
        console.log(`succeed to open camera`);
        this.mediaStream = video;
      })
      .catch((err) => {
        console.log(err);
      });
  }
  startDetector() {
    this.mediaStream &&
      this.detector
        .detectFaces(this.mediaStream)
        .then((res) => {
          console.log(res); // 对应最下方的人脸信息（检测数据）内容说明
        })
        .catch((err) => {
          console.log(err);
        });
  }
  handleDetectionResult() {
    let actions = {
      blink: "眨眼",
      blink_left: "左眨眼",
      blink_right: "右眨眼",
      mouth_ah: "嘴巴大张",
      head_yaw: "摇头",
      head_yaw_indian: "印度式摇头",
      head_pitch: "点头",
      brow_jump: "眉毛挑动",
      mouth_pout: "嘟嘴",
    };
    this.detector.onActions((detectData) => {
      for (let act of detectData.actions) {
        console.log(`检测到 ${actions[act]} 动作`);
      }
    });
    this.detector.onBlink((detectData) => {
      console.log(`------检测到眨眼动作-----------`);
      console.log(detectData);
    });
  }
  paintVideoToCanvas() {
    let video = this.mediaStream;
    if (video) {
      const { width, height } = canvas;
      video.paintTo(canvas, 0, 0, 0, 0, width, height);
    }
  }
  run() {
    if (this.frame >= 5) {
      this.frame = 0;
      this.startDetector(); // detect faces once every five frames
    } else {
      this.frame++;
    }
    this.paintVideoToCanvas();
    requestAnimationFrame(() => {
      this.run();
    });
  }
}
new Game();
```
【示例代码 2】：cocos 接入示例
```js
const { ccclass, property } = cc._decorator;
@ccclass
export default class NewClass extends cc.Component {
    private camera: any = null;
    private video: any = null;
    private detector: any = null;
    private frame: number = 0;
    @property(cc.Sprite)
    private videoTexture: cc.Texture2D = null;
    private cameraNode;
    onLoad() {
        this.startCamera();
        this.handleDetectionResult();  //动作触发处理
    }
    startCamera() {
        this.camera = tt.createCamera();
        this.detector = tt.createFaceDetector();
        tt.setKeepScreenOn();   // 保持屏幕常亮
        this.camera.start('front', true).then(video => {
            this.video = video;
            this.initVideo();   // cocos视频映射应该在camera初始完成之后
        }).catch(err => {
            tt.showToast({
                title: '摄像机需要授权'
            });
            console.log(err);
        });
        this.camera.setBeautifyParam(1, 1, 1, 1);   //设置美白、磨皮、大眼、瘦脸, 范围：[0, 1]
    }
    initVideo() {
        this.cameraNode = new cc.Node();
        this.cameraNode.addComponent(cc.Sprite)
        this.node.insertChild(this.cameraNode, 0);
        this.videoTexture = new cc.Texture2D();
        this.videoTexture.initWithElement(this.video);
        this.videoTexture.handleLoadedTexture();
        this.cameraNode.getComponent(cc.Sprite).spriteFrame = new cc.SpriteFrame(this.videoTexture);
        this.setVideoWidth(cc.view.getVisibleSize().width)  //固定宽度进行视频缩放
        this.cameraNode.width = this.video.width;     //设置在游戏界面画的视频宽度
        this.cameraNode.height = this.video.height;   //设置在游戏界面画的视频高度
    }
    startDetector() {
        if (this.detector && this.video) {
            this.detector.detectFaces(this.video).then(res => {
                console.log(res); // 对应最下方的人脸信息（检测数据）内容说明
            })
        }
    }
    handleDetectionResult() {
        let actions = {
            blink: '眨眼',
            blink_left: '左眨眼',
            blink_right: '右眨眼',
            mouth_ah: '嘴巴大张',
            head_yaw: '摇头',
            head_yaw_indian: '印度式摇头',
            head_pitch: '点头',
            brow_jump: '眉毛挑动',
            mouth_pout: '嘟嘴'
        };
        this.detector.onActions(detectData => {
            let arr = [];
            for (let act of detectData.actions) {
                console.log(`检测到 ${actions[act]} 动作`);
                arr.push(actions[act]);
            }
            tt.showToast({
                title: arr.join('、'),
                duration: 2000
            });
        });
        this.detector.onBlink(detectData => {
            console.log(`------检测到眨眼动作-----------`)
            console.log(detectData);
        });
        this.detector.onMouthAh(detectData => {
            console.log(`------检测到嘟嘟嘴动作-----------`)
            console.log(detectData);
        });
    }
    setVideoWidth(width: number) {
        if (this.video) {
            this.video.width = width;
            this.video.height = this.video.videoHeight / this.video.videoWidth * width;
        }
    }
    update(dt) {
        this.frame++;
        if (this.frame >= 5) {
            this.startDetector();   //每五帧进行一次人脸检测
            this.frame = 0
        }
        if (this.videoTexture && this.video) {
            this.videoTexture.update({
                image: this.video,
                flipY: false
            })
        }
```
【示例代码 3】：cocos3d 接入示例
```js
import { _decorator, Component, Node, SpriteComponent, Texture2D, ImageAsset, SpriteFrame } from 'cc';
const { ccclass, property } = _decorator;
@ccclass
export default class Main extends cc.Component {
    @property(SpriteComponent)
    videoSprite: SpriteComponent = null;
    private camera: any = null;
    private video: any = null;
    private detector: any = null;
    private frame: number = 0;
    private videoTexture: Texture2D = null;
    onLoad() {
        this.startCamera();
        this.handleDetectionResult();  //动作触发处理
    }
    startCamera() {
        this.camera = tt.createCamera();
        this.detector = tt.createFaceDetector();
        tt.setKeepScreenOn();   // 保持屏幕常亮
        this.camera.start('front', true).then(video => {
            this.video = video;
            this.initVideo();   // cocos视频映射应该在camera初始完成之后
        }).catch(err => {
            tt.showToast({
                title: '摄像机需要授权'
            });
            console.log(err);
        });
        this.camera.setBeautifyParam(1, 1, 1, 1);   //设置美白、磨皮、大眼、瘦脸, 范围：[0, 1]
    }

    initVideo() {
        //************************************** */
        this.videoTexture = new cc.Texture2D();
        let img = new ImageAsset();
        img.reset(this.video);
        this.videoTexture.image = img;
        let spFrame: SpriteFrame = new SpriteFrame();
        spFrame.texture = this.videoTexture;
        this.videoSprite.spriteFrame = spFrame;
        //************************************** */

        this.setVideoWidth(cc.view.getVisibleSize().width)  //固定宽度进行视频缩放
        this.videoSprite.node.width = this.video.width;     //设置在游戏界面画的视频宽度
        this.videoSprite.node.height = this.video.height;   //设置在游戏界面画的视频高度
    }

    startDetector() {
        if (this.detector && this.video) {
            this.detector.detectFaces(this.video).then(res => {
                console.log(res); // 对应最下方的人脸信息（检测数据）内容说明
            })
        }
    }
    handleDetectionResult() {
        let actions = {
            blink: '眨眼',
            blink_left: '左眨眼',
            blink_right: '右眨眼',
            mouth_ah: '嘴巴大张',
            head_yaw: '摇头',
            head_yaw_indian: '印度式摇头',
            head_pitch: '点头',
            brow_jump: '眉毛挑动',
            mouth_pout: '嘟嘴'
        };
        this.detector.onActions(detectData => {
            let arr = [];
            for (let act of detectData.actions) {
                console.log(`检测到 ${actions[act]} 动作`);
                arr.push(actions[act]);
            }
        });
    }
    setVideoWidth(width: number) {
        if (this.video) {
            this.video.width = width;
            this.video.height = this.video.videoHeight / this.video.videoWidth * width;
        }
    }
    update(dt) {
        this.frame++;
        if (this.frame >= 60) {
            this.startDetector();   //每60帧进行一次人脸检测
            this.frame = 0
        }
        if (this.videoTexture && this.video) {
            this.videoTexture.updateImage()
        }
    }
}
```
【示例代码 4】：laya 接入示例。直接封装成 sprite，可以在舞台中直接添加
```js
export default class CameraSprite extends Laya.Sprite {
    private camera: any = null;
    private video: any = null;
    private frame: number = null;
    constructor() {
        super();
        this.init();
        this.updateToCamera();
    }
    init() {
        this.camera = tt.createCamera();
        this.camera.setBeautifyParam(1, 1, 1, 1);
        this.detector = tt.createFaceDetector();
        this.camera.start('front', true).then(video => {
            tt.setKeepScreenOn();
            let texture2D: Laya.Texture2D = new Laya.Texture2D(video.videoWidth, video.videoHeight, 1, false, false);
            texture2D.loadImageSource(video, true);
            let texture: Laya.Texture = new Laya.Texture(texture2D);
            this.texture = texture;
            this.video = video;
        }).then(err => {
            tt.showToast({
                title: '相机需要授权'
            })
        })
        this.detector.onBlink(detectData => {
            tt.showToast({
                title: 'Blink'
            })
            console.log(detectData)
        })
    }

    private startDetector() {
        if (this.detector && this.video) {
            this.detector.detectFaces(this.video).then(res => {
                console.log(res)
            }).catch(err => {
                console.log(err)
            })
        }
    }
    private renderVideo() {
        if (this.video) {
            this.texture.bitmap.loadImageSource(this.video, true);
            //对于新版提示语法错误可以用下面的语句
            //(this.texture!.bitmap as Laya.Texture2D).loadImageSource(this.video, true)
        }
    }
    private updateToCamera() {
        Laya.timer.frameLoop(1, this, () => {
            this.frame++;
            // detect once every five frames. You can customize your detection  rate based on your need.
            if (this.frame >= 5) {
                this.startDetector();
                this.frame = 0
            }
            this.renderVideo();
        })
    }
}

let camera: CameraSprite = new CameraSprite();
this.addChild(camera);
```

【示例代码 5】：egret 接入示例

<ul><li>原理：其实无论是 cocos 、 layaAir 抑或是 egret, 在游戏界面上播放离屏视频/摄像头视频的原理其实是相同的。三者的本质都是加载视频数据， 然后逐帧采集视频的纹理， 然后逐帧渲染到游戏界面上面</li><li>使用版本：主端 7.4.5</li></ul>
```js
class Cameramap extends egret.DisplayObjectContainer {
    private camera: any = null;
    private video: any = null;
    private frame: number = 0;
    private _widthSet: number = 0;
    private _heightSet: number = 0;
    private _bitmapData: egret.BitmapData = null;
    public x: number = 0;
    public y: number = 0;
    constructor() {
        super();
        this.init();
        this.update();
    }
    public get bitmapData(): egret.BitmapData {
        if (!this.video) {
            return null;
        }
        if (!this._bitmapData) {
            this._bitmapData = new egret.BitmapData(this.video);
            this._bitmapData.$deleteSource = false;
        }
        return this._bitmapData;
    }
    public get width(): number {
        return this._widthSet;
    }
    public set width(value) {
        this._widthSet = value;
    }
    public get height(): number {
        return this._heightSet;
    }
    public set height(value) {
        this._heightSet = value;
    }

    init() {
        this.$renderNode = new egret.sys.BitmapNode();
        this.camera = tt.createCamera();
        this.detector = tt.createFaceDetector();
        this.camera.setBeautifyParam(1, 1, 0, 0);
        this.camera.start('front', true).then(video => {
            this.video = video;
            let scale = this.video.videoHeight / this.video.videoWidth;
            if (!this._widthSet) {
                this.width = this.stage.width;
            }
            if (!this._heightSet) {
                this.height = this.width * scale;
            }

        }).catch(err => {
            tt.showToast({
                title: '相机需要授权'
            })
        })
        this.detector.onBlink(res => {
            tt.showToast({
                title: 'Blink'
            })
            console.log(res);
        })
    }
    renderVideo() {
        let node = <egret.sys.BitmapNode>this.$renderNode;
            let bitmapData = this.bitmapData;
            node.cleanBeforeRender();  // 清空渲染前的数据
            node.image = bitmapData;
            node.imageWidth  = bitmapData.width;
            node.imageHeight = bitmapData.height;
            egret.WebGLUtils.deleteWebGLTexture(bitmapData.webGLTexture);
            bitmapData.webGLTexture = null;
            node.drawImage(0, 0, bitmapData.width, bitmapData.height, this.x, this.y, this.width, this.height);
    }
            startDetector() {
        if (this.detector && this.video) {
                this.detector.detectFaces(this.video).then(res => {
                    console.log(res)
                }).catch(err => {
                    console.log(err);
                })
            }
    }
            update() {
                egret.lifecycle.addLifecycleListener(context => {
                    context.onUpdate = () => {
                        this.frame++;
                        if (this.frame >= 5) {
                            this.startDetector();
                            this.frame = 0;
                        }
                        if (this.video) {
                            this.renderVideo();
                        }
                    }
                })

            }
}
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| detector | Object | [Detector](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/face-detector/detector) 对象 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android