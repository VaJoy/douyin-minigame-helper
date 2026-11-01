---
title: "网络通信适配"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc_webgl_network
update_time: 2024-10-17
---

> 此文档描述小游戏开发时网络通信适配问题
> 更多详情见[Unity WebGL 抖音小游戏适配方案](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/sc_webgl_overall)

如果使用native方案，支持直接访问 IP 套接字来实现网络连接。无需额外适配。

以下适配方案针对webgl方案：
由于安全性的影响，JavaScript 代码没有直接访问 IP 套接字来实现网络连接。因此，该.NET 网络类（System.Net 命名空间中的一切，特别是**System.Net.Sockets**）在 WebGL 中不能工作。UnityEngine.Network* 类也是这样，编译 WebGL 时将找不到这些类。

## **HTTP 通信**
Unity 支持在 WebGL 中使用 UnityWebRequest 类。

### **使用方式**
以下为使用协程方式发送 GET、POST 请求到服务器的示例：

```csharp
 IEnumerator Get(){UnityWebRequest webRequest = UnityWebRequest.Get("https://mysite.com");yield return webRequest.SendWebRequest();if (webRequest.isHttpError||webRequest.isNetworkError)
            Debug.Log(webRequest.error);else{
            Debug.Log(webRequest.downloadHandler.text);}}

IEnumerator Post(){WWWForm form = new WWWForm();//键值对
    form.AddField("key", "value");
    form.AddField("name","mafanwei");
    form.AddField("blog","qwe25878");UnityWebRequest webRequest = UnityWebRequest.Post("https://mysite.com",form);yield return webRequest.SendWebRequest();if (webRequest.isHttpError||webRequest.isNetworkError)
        Debug.Log(webRequest.error);else{
        Debug.Log(webRequest.downloadHandler.text);}}
```

**注意**
- 在 Unity WebGL 环境下**禁止**使用以下代码：

```csharp
while(!www.isDone) {}
```

WebGL不支持多线程，所以不能阻止线程等待 UnityWebRequest 下载完成，否则您的应用程序将冻结。取而代之的做法是使用协程和 yield 语句等待下载完成。
- HttpWebRequest在WebGL下不支持，需要替换成UnityWebRequest

## **TCP 网络通信**
如果游戏使用 TCP 进行网络通信，在 Unity WebGL 中开发者需要使用 WebSocket 进行替代。
### 
### **客户端**
支持 Unity WebSocket 的第三方插件比较多，可以从 Github 或 AssetStore 找到。这里以[UnityWebSocket](https://github.com/psygames/UnityWebSocket)为例。

```csharp
// 命名空间
using UnityWebSocket;

// 创建实例
string address = "ws://echo.websocket.org";
WebSocket socket = new WebSocket(address);

// 注册回调
socket.OnOpen += OnOpen;
socket.OnClose += OnClose;
socket.OnMessage += OnMessage;
socket.OnError += OnError;

// 连接
socket.ConnectAsync();
// 发送 string 类型数据
socket.SendAsync(str);
// 或者 发送 byte[] 类型数据（建议使用）
socket.SendAsync(bytes);

// 关闭连接
socket.CloseAsync();
```

### **服务端**
如果服务端使用 TCP 接入，则需要使用 WSS<-->TCP 的代理层。解决方案也很多：
- 使用 Ngnix、 [websockify-js](https://github.com/novnc/websockify-js)/[websockify](https://github.com/novnc/websockify)做反向代理（推荐）
- 改造原有TCP服务兼容wss服务
**使用TCP方案时，在处理数据包时，请注意数据的“粘包”问题，需要游戏服务器和客户端自行处理。**
## 
## UDP 网络通信
如果游戏使用 UDP 进行网络通信，在 Unity WebGL 中开发者需要使用 SDK 提供的 API 进行替代。

### 客户端
此处以 C# SDK 提供的 UDPSocket API 为例：

```csharp
using TTSDK;

// 创建 UDPSocket 实例
TTUDPSocket socket = TT.CreateUDPSocket();

// 绑定事件监听
socket.OnError(OnError);
socket.OnClose(OnClose);
socket.OnListening(OnListening);
socket.OnMessage((res) => {
    Debug.Log("收到消息：" + res.message);
});

// 绑定任意可用端口
int port = socket.Bind();

// 预先连接到指定地址
socket.Connect(new UDPSocketConnectOption {
    address = "xxx.xxx.xxx.xxx",
    port = xxxx
});

// 向指定地址发送消息
socket.Send(new UDPSocketSendOption {
    address = "xxx.xxx.xxx.xxx",
    port = xxxx,
    message = new byte[] { 1, 2, 3, 4 } // 支持发送 byte[] 或 string 类型的数据
});

// 移除绑定的事件监听
socket.OffError(OnError);
socket.OffClose(OnClose);
socket.OffListening(OnListening);
socket.OffMessage(OnMessage);

// 关闭连接
socket.Close();
```

**由于 UDP 协议不可靠的特性，开发者在使用 UDP 通信时，需要注意自行处理丢包、乱序等问题。**
