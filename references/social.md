# 分享与社交

> **适用**：分享裂变、好友邀请、排行榜、关注抖音号、群聊、开放数据域。
> **源文档**：`docs/develop/api/javascript-api/open-capacity/` 相关 76 项；`docs/develop/guide/open-ability/social-interaction/`、`game-share/`、`relationship-chain/`。
> **关联**：分享代码片段见 `api-recipes.md` 第 3 节；分享审核要求见 `security-release.md`。

## 分享的两条路径

| 类型 | 触发方 | 用哪个 API | 说明 |
|---|---|---|---|
| 主动分享 | 开发者 | `tt.shareAppMessage(shareParam)` | 游戏内自定义按钮拉起发布器 |
| 被动分享 | 用户 | `tt.onShareAppMessage(callback)` | 用户点右上角「更多 → 分享」时回调，开发者只决定内容 |

被动分享不是可选功能：不注册回调时，平台用默认内容（游戏名 + 默认截图）。想控制内容就必须注册。

### 打开 / 关闭右上角分享入口

```js
tt.showShareMenu({ success() {}, fail() {} });   // 显示转发按钮（默认显示）
tt.hideShareMenu({ success() {}, fail() {} });   // 隐藏转发按钮
```

### 分享内容的优先级

平台按以下顺序取内容，前一个没有才用下一个：

1. 代码里传的 `title` / `desc` / `imageUrl`
2. 代码里传的、审核通过的模板素材 `templateId`
3. 后台「运营能力 > 分享设置」里配置的默认素材
4. 平台兜底图

> 素材要在开发者后台先建、先审核，通过后才有 `templateId`；未过审的内容即使代码传了也会被替换。

### 常见失败

| errNo | 原因 |
|---|---|
| 21101 | 权限被拒（渠道不支持） |
| 21102 | 未经用户点击就触发分享 |
| 21103 / 21104 | 分享的图片/视频文件不存在或不可读 |
| 21105 | 视频太短 |
| 21107 | stickerId 与 cutTemplateId 互斥 |
| — | `get shareInfo return null`：分享链接过期（有效期 45 天）或 appID 分享状态异常 |

## 好友邀请与组队

- 邀请走 `tt.shareAppMessage` 的 `channel: 'invite'`，成功回调里会带被邀请人的 `name` / `icon`（多选时只返回一个）。
- 组队分享见 `docs/develop/guide/open-ability/game-share/game-team-share.md`，核心是把队伍 ID 塞进 `query`，被邀请方通过 `tt.getLaunchOptionsSync().query` 取回。
- 定向分享（分享给指定好友）见 `relationship-chain/directional-share.md`。

## 排行榜

两种实现，别混用：

| 方案 | API | 特点 |
|---|---|---|
| IM 排行榜（原生 UI） | `tt.setImRankData` / `tt.getImRankList` | 平台直接绘制好友榜，接入快，样式不可定制，基础库 2.70.0+ |
| 自绘排行榜 | `tt.setUserCloudStorage` + `tt.getOpenDataContext` | 数据写托管 KV，在开放数据域里自己画，可控性高 |

IM 排行榜要点：
- `setImRankData` 在关键节点（结算/破纪录）写一次即可，不要每帧写。
- `getImRankList` 会**自动绘制** native UI，不需要自己渲染。

自绘排行榜要点：
- 主域 `tt.setUserCloudStorage({ KVDataList: [{ key, value }] })` 写入，`value` 必须是字符串。
- 开放数据域通过 `tt.getOpenDataContext()` 拿到上下文，用 `postMessage` 与主域通信；子域里只能用开放数据域专用 API，不能直接用主域 API。
- 好友数据只能**在开放数据域内**读取和绘制，主域拿不到好友列表（防隐私泄露）。

## 关注抖音号

```js
const btn = tt.createFollowButton({ type: 'text', style: { left: 10, top: 10 } }); // 样式字段见原文
btn.onTap(() => console.log('点击关注'));
tt.checkFollowState({ success(res) { console.log(res.isFollow); } });
```

- 关注对象是开发者后台绑定的官方抖音号，不是任意账号。
- `checkFollowState` 在部分宿主上返回的是头条号关注态，注意区分。

## 群聊

```js
tt.joinGroup({
  groupid: '998877',        // 后台创建群聊后获得
  sessionFrom: 'game_over', // 场景标识，可回溯来源
  success(res) { console.log('入群成功'); },
  fail(res) { console.log(res); },
});
```

- 需要先在开发者后台「运营 > 群聊」创建群并绑定抖音号，拿到 `groupid`。
- 群满员时 `joinGroup` 会失败，应在游戏内做「换二群」的降级逻辑，可配合查询群状态。
- 公会群（`tt.bindUnionGroup` / `tt.joinUnionGroup` / `tt.getUnionGroupInfo` / `tt.unbindUnionGroup`，基础库 3.51.0+）是另一套，面向公会运营，普通游戏用不到。

## 开放数据域

- 是一个独立的 JS 运行环境，只能访问 `tt.getUserCloudStorage` 等少数接口，用于展示好友排行榜、群排行。
- 主域与子域通过 `postMessage` 单向传消息，子域绘制结果通过共享 canvas（`tt.getSharedCanvas`）回传给主域贴图。
- 子域代码要单独打包，在 `game.json` 里用 `openDataContext` 指定目录。
- **Cocos 项目**只需要在节点上挂 `SubContextView` 组件，构建时勾「生成开放数据域工程模板」，模板与定制方式见 `cocos-publish.md`。

### 子域收到的第一条消息是引擎发的

挂上 `SubContextView` 后，子域的 `onMessage` 会收到形如这样的消息（`cocos-engine-3.8.6/cocos/ui/sub-context-view.ts:222-230`）：

```js
const viewportMsg = {
  fromEngine: true,
  type: 'engine',
  event: 'viewport',
  x: 0, y: 0, width: 0, height: 0,   // 视窗矩形，已除过 dpr
};
```

规则：

- **什么时候发**：组件 `onLoad` 时发一次；之后组件节点的位移、缩放、尺寸变化都会再发一次（`sub-context-view.ts:252-256` 监听 `TRANSFORM_CHANGED` / `SIZE_CHANGED`）。
- **官方模板只处理这一种消息**：收到 `type === 'engine' && event === 'viewport'` 就更新视窗并重画（`platforms/minigame/openDataContext/index.js`）。
- **不要把 `type === 'engine'` 的消息全部过滤掉。** 很多人照抄过滤逻辑只留业务消息，结果排行榜在旋转屏幕、改分辨率、拖拽容器后**不再重绘**，画面停在旧视窗尺寸上。正确做法是：认 `viewport` 就重画，其他 `engine` 消息忽略。
- 主域发业务消息时自己带 `type`，并**避免用 `'engine'`**，双方约定私有前缀（如 `'rank'`、`'ui'`）。

### 组件会静默失效，不报错

```
sub-context-view.ts:126-135
```

`minigame.getOpenDataContext` 不存在时，组件直接把自己 `enabled = false`。现象是「场景里挂着 SubContextView，运行时一片空白，控制台干净」。开发者工具正常、个别老宿主空白时优先查这里。

### 分辨率与刷新频率

- `sharedCanvas` 的尺寸直接取组件的「设计分辨率」，默认 **640 × 960**（`sub-context-view.ts:116-117`、`:163-164`）。子域里 CSS 的宽高不要超过它，否则内容溢出画布。
- 微信有「共享画布至少一边大于 513 否则不出图」的补丁，**抖音没有这个分支**（`sub-context-view.ts:151-162` 只在微信平台生效），小尺寸画布在抖音上是安全的。
- 组件的 `fps`（默认 60）只节流「把 sharedCanvas 上传成纹理」这一步（`sub-context-view.ts:268-280`），**不节流子域自己的重绘**。子域每帧重画的话主域这边一点都省不下来，节流要在子域里自己做。
- 子域内容节点的 layer 跟随组件所在节点（`sub-context-view.ts:255`、`:264-266`）。要控制这层排行榜的渲染层级，请改 `SubContextView` 所在节点的 layer，不要改内部的 content 节点。
