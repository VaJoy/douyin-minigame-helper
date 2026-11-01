---
title: "createQRCode"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/qr-code/create-qr-code
update_time: 2024-07-24
---

**接口地址：** `POST https://minigame.zijieapi.com/mgplatform/api/apps/qrcode`

**版本：** 1.0.24

获取小程序/小游戏的二维码。该二维码可通过任意 app 扫码打开，能跳转到开发者指定的对应字节系 app 内拉起小程序/小游戏，并传入开发者指定的参数。通过该接口生成的二维码，永久有效，暂无数量限制。

**注意：**

- **在使用该功能之前请记得先配置您的默认分享文案和图片，配置方式可参考[论坛](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/user-ops/gain-user/retweet)。**
- **小程序的 path 要 encode 一次，如 pages%3fparam%3dtrue，小游戏的 path 为 JSON 字符串，如{"param":true}，否则会导致取不到。**

获取小程序/小游戏的二维码。该二维码可通过任意 app 扫码打开，能跳转到开发者指定的对应字节系 app 内拉起小程序/小游戏，并传入开发者指定的参数。通过该接口生成的二维码，永久有效，暂无数量限制。

**鉴权：** `access-token`（string）

## 请求参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `is_circle_code` | boolean | 否 | 是否为圆形码，传true表示生成圆形的抖音码，传false表示生成普通的正方形二维码 |  | BodyParam |
| `set_icon` | boolean | 否 | is_circle_code 为 false 时生效，是否展示小程序/小游戏 icon，默认不展示 |  | BodyParam |
| `line_color` | Object | 否 | is_circle_code 为 false 和 auto_color 为 false 时生效，二维码线条颜色，默认为黑色  **字段** - `b`（int）：蓝色值，取值范围为[0,255]，默认为0 - `g`（int）：绿色值，取值范围为[0,255]，默认为0 - `r`（int）：红色值，取值范围为[0,255]，默认为0 |  | BodyParam |
| `access_token` | string | 是 | 调用[https://minigame.zijieapi.com/mgplatform/api/apps/v2/token](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token)生成的token | 08011218462b6b4b5054626e426e50685a7554643144644449413d3d | BodyParam |
| `auto_color` | boolean | 否 | is_circle_code 为 false 时生效，自动配置线条颜色，如果颜色依然是黑色，则说明不建议配置主色调，默认 false |  | BodyParam |
| `background` | Object | 否 | is_circle_code 为 false 时生效，二维码背景颜色，默认为白色  **字段** - `r`（int）：红色值，取值范围为[0,255]，默认为0 - `b`（int）：蓝色值，取值范围为[0,255]，默认为0 - `g`（int）：绿色值，取值范围为[0,255]，默认为0 |  | BodyParam |
| `version_type` | string | 否 | 要打开小游戏的版本，线上版为current，开发版为latest |  | BodyParam |
| `path` | string | 是 | 小程序/小游戏启动参数，小程序则格式为 encode({path}?{query})，小游戏则格式为 JSON 字符串，默认为空 |  | BodyParam |
| `appname` | string | 是 | 打开二维码的字节系 app 名称，默认为今日头条 |  | BodyParam |
| `width` | int | 是 | 二维码宽度，单位 px，最小 280px，最大 1280px，默认为 430px |  | BodyParam |
| `content-type` | string | 是 | 固定值"application/json" |  | HeaderParam |

## 返回参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `errmsg` | string | 否 | 错误信息 |  | BodyParam |
| `data` | bytes | 否 | 二维码图片 |  | BodyParam |
| `errcode` | int64 | 否 | 错误号 |  | BodyParam |

## 请求示例

```bash
curl --location 'https://minigame.zijieapi.com/mgplatform/api/apps/qrcode' \
--header 'Content-Type: application/json' \
--data '{"access_token":"0801121847443236736a456c534e72567a36726f476c5a4a75773d3d","appname":"douyin","path":"","width":280,"line_color":{"r":0,"g":0,"b":0},"background":{"r":255,"g":255,"b":255},"set_icon":false,"is_circle_code":true,"version_type":"current","auto_color":false}'
```

## 成功响应示例

```json
直接返回图片的 []byte 数组
```

## 异常响应示例

```json
{
  "errcode": 40002,
  "errmsg": "bad access_token"
}
```

## 错误码
| HTTP 状态码 | 错误码 | 描述 | 处理建议 |
| --- | --- | --- | --- |
| 200 | 0 | 成功 |  |
| 200 | -1 | 系统错误 |  |
| 200 | 40002 | access_token 错误 |  |
| 200 | 40016 | appname 错误 |  |
| 200 | 40021 | width 超过指定范围 |  |
| 200 | 60003 | 频率限制（目前 5000 次 / 分钟） |  |
| 200 | 60103 | 

没有设置分享图标

 |  |
| 200 | 40026 | 

版本参数错误

 |  |