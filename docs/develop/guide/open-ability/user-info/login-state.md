---
title: "登录态管理"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/user-info/login-state
update_time: 2025-09-11
---

## 小游戏登录
小游戏可以通过抖音官方提供的登录能力方便地获取抖音提供的用户身份标识，快速建立小游戏内的用户体系。
#### 登录流程时序图

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/eceed1ffc7ac4c869495c12d220e12b1~tplv-9nona0m7ha-image.image)

##### 说明：
1. 调用 [tt.login](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/log-in/tt-login) 获取 **临时登录凭证code** ，并回传到开发者服务器。
1. 调用 [code2Session](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/log-in/code-2-session) 接口，换取 **用户唯一标识 OpenID** 、 用户在抖音开放平台账号下的唯一标识 UnionID（若当前小游戏已绑定到抖音开放平台账号） 和 **会话密钥 session_key**。
之后开发者服务器可以根据用户标识来生成自定义登录态，用于后续业务逻辑中前后端交互时识别用户身份。
**注意：**
1. 会话密钥 `session_key` 是对用户数据进行 [加密签名](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/log-in/user-login-sign) 的密钥。为了应用自身的数据安全，开发者服务器**不应该把会话密钥下发到小游戏，也不应该对外提供这个密钥**。
1. 临时登录凭证 code 只能使用一次
