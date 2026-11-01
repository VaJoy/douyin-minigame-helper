---
title: "UDPSocket"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/internet/udp-socket
update_time: 2025-01-13
---

UDPSocket 为 Unity 小游戏提供了 UDP 通信的能力。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 该接口仅支持 WebGL 方案。接入参考：[网络通信适配](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc_webgl_network#1dbceceb)。 如果使用 native 方案，支持直接访问 IP 套接字来实现网络连接。无需额外适配。 |
| 注意事项 | 以下适配方案针对 webgl 方案： 由于安全性的影响，JavaScript 代码没有直接访问 IP 套接字来实现网络连接。因此，该  .NET 网络类（System.Net 命名空间中的一切，特别是 **System.Net****.Sockets**）在 WebGL 中不能工作。UnityEngine.Network* 类也是这样，编译 WebGL 时将找不到这些类。 |
| 相关教程 | 无 |

## CreateUDPSocket
> 6.0.0开始支持该方法，仅WebGL支持该方法
创建一个 UDP Socket 实例。
### **语法 **

```csharp
public static TTUDPSocket CreateUDPSocket()
```

### 参数说明
无参数。
### 返回值

| 类型 | 说明 |
| --- | --- |
| TTUDPSocket | UDPSocket 实例 |

### 代码示例

```csharp
private void Test(){
    _udpClient = TT.CreateUDPSocket();
}
```

## TTUDPSocket
UDPSocket 实例。

### TTUDPSocket.Bind
> 6.0.0开始支持该方法，仅WebGL支持该方法
绑定一个系统随机分配的可用端口，或绑定一个指定的端口号。bind 成功会触发 onListening 监听。
#### **语法 **

```csharp
public int Bind(int? port = null)
```

#### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| port | int? | null | 否 | bind指定的端口号，合法值：[0, 65535]。传入0或者不传，则绑定一个系统随机分配的可用端口。 |

#### 返回值

| **类型** | **说明** |
| --- | --- |
| int | 绑定成功的端口号 |

#### 代码示例

```csharp
private void Test(){
    var resPort = _udpClient.Bind();
    Debug.Log($"bind() -> {resPort}");
}
```

### TTUDPSocket.Close
> 6.0.0开始支持该方法，仅WebGL支持该方法
关闭 UDP Socket 实例。
在关闭之后，将无法再调用 Bind、Connect 等方法。
#### **语法 **

```csharp
public void Close()
```

#### 参数说明
无参数。
#### 代码示例

```csharp
private void Test(){
    socket.Close();
}
```

### TTUDPSocket.Connect
> 6.0.0开始支持该方法，仅WebGL支持该方法
预先连接到指定的 IP 和端口。
#### **语法 **

```csharp
public void Connect(UDPSocketConnectOption option)
```

#### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| option | UDPSocketConnectOption | -- | 是 | 连接消息的参数 |

UDPSocketConnectOption 属性：

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | -- | 是 | 要发送消息的地址 |
| port | int | -- | 是 | 要发送消息的端口号 |

#### 代码示例

```csharp
private void Test(){
    var option = new UDPSocketConnectOption()
    {
        address = strAddress,
        port = port
    };
    Debug.Log($"connect({JsonMapper.ToJson(option)})");
    _udpClient.Connect(option);
}
```

### TTUDPSocket.OnMessage
> 6.0.0开始支持该方法，仅WebGL支持该方法
预先连接到指定的 IP 和端口。
#### **语法 **

```csharp
public void OnMessage(
    Action<UDPSocketOnMessageListenerResult> listener, 
    bool needInfo = false)
```

#### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| listener | Action<UDPSocketOnMessageListenerResult> | -- | 是 | 事件监听函数 |
| needInfo | bool | false | 否 | 回调中是否带有本地和远端地址信息 |

**UDPSocketOnMessageListenerResult 属性：**

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| localInfo | LocalInfo | 本地信息 |
| remoteInfo | RemoteInfo | 远端信息 |
| message | byte[] | 消息内容 |

**LocalInfo 属性：**

| 属性名 | 类型 |
| --- | --- |
| address | string |
| family | string |
| port | int |

**RemoteInfo 属性：**

| 属性名 | 类型 |
| --- | --- |
| address | string |
| family | string |
| port | int |
| size | ulong |

#### 代码示例

```csharp
private void Test(){
    _udpClient.OnMessage((res) =>
    {
        Debug.Log($"[TEST] UDPClient {udpClient} OnMessage: " + res.message);
    });
}
```

### TTUDPSocket.OffMessage
> 6.0.0开始支持该方法，仅WebGL支持该方法
移除收到消息事件的事件监听函数。
#### **语法 **

```csharp
public void OffMessage(Action<UDPSocketOnMessageListenerResult> listener = null)
```

#### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| listener | Action<UDPSocketOnMessageListenerResult> | null | 否 | 事件监听函数 |

#### 代码示例

```csharp
Test() {
    _udpClient.OffMessage(Listen());
}

void Listen(UDPSocketOnMessageListenerResult result){
    Debug.Log($"[TEST] UDPClient  OnMessage: " + result.message);
}
```

### TTUDPSocket.OnClose
> 6.0.0开始支持该方法，仅WebGL支持该方法
监听关闭的事件。
#### **语法 **

```csharp
public void OnClose(Action<GeneralCallbackResult> listener)
```

#### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| listener | Action<GeneralCallbackResult> | -- | 是 | 事件监听函数 |

**GeneralCallbackResult 属性：**

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 错误信息 |

#### 代码示例

```csharp
void Test() {
    _udpClient.OnClose(Listen());
}

void Listen(UDPSocketOnMessageListenerResult result){
    Debug.Log($"[TEST] UDPClient {_udpClient} OnClose: " + res.errMsg);
}
```

### TTUDPSocket.OffClose
> 6.0.0开始支持该方法，仅WebGL支持该方法
移除关闭事件的事件监听函数。
#### **语法 **

```csharp
public void OffClose(Action<GeneralCallbackResult> listener)
```

#### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| listener | Action<GeneralCallbackResult> | -- | 是 | 事件监听函数 |

**GeneralCallbackResult 属性：**

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 错误信息 |

#### 代码示例

```csharp
void Test() {
    _udpClient.OffClose(Listen());
}

void Listen(UDPSocketOnMessageListenerResult result){
    Debug.Log($"[TEST] UDPClient {_udpClient} OnClose: " + res.errMsg);
}
```

### TTUDPSocket.OnError
> 6.0.0开始支持该方法，仅WebGL支持该方法
监听错误的事件。
#### **语法 **

```csharp
public void OnError(Action<GeneralCallbackResult> listener)
```

#### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| listener | Action<GeneralCallbackResult> | -- | 是 | 事件监听函数 |

**GeneralCallbackResult 属性：**

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 错误信息 |

#### 代码示例

```csharp
void Test() {
    _udpClient.OnError(Listen());
}

void Listen(UDPSocketOnMessageListenerResult result){
    Debug.Log($"[TEST] UDPClient {_udpClient} OnError: " + res.errMsg);
}
```

### TTUDPSocket.OffError
> 6.0.0开始支持该方法，仅WebGL支持该方法
移除错误事件的事件监听函数。
#### **语法 **

```csharp
public void OffError(Action<GeneralCallbackResult> listener)
```

#### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| listener | Action<GeneralCallbackResult> | -- | 是 | 事件监听函数 |

**GeneralCallbackResult 属性：**

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 错误信息 |

#### 代码示例

```csharp
void Test() {
    _udpClient.OffError(Listen());
}

void Listen(UDPSocketOnMessageListenerResult result){
    Debug.Log($"[TEST] UDPClient {_udpClient} OnError: " + res.errMsg);
}
```

### TTUDPSocket.OnListening
> 6.0.0开始支持该方法，仅WebGL支持该方法
监听开始监听数据包的事件。
#### **语法 **

```csharp
public void OnListening(Action<GeneralCallbackResult> listener)
```

#### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| listener | Action<GeneralCallbackResult> | -- | 是 | 事件监听函数 |

**GeneralCallbackResult 属性：**

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 错误信息 |

#### 代码示例

```csharp
void Test() {
    _udpClient.OnListening(Listen());
}

void Listen(UDPSocketOnMessageListenerResult result){
    Debug.Log($"[TEST] UDPClient {_udpClient} OnListening: " + res.errMsg);
}
```

### TTUDPSocket.OffListening
> 6.0.0开始支持该方法，仅WebGL支持该方法
移除错误事件的事件监听函数。
#### **语法 **

```csharp
public void OffListening(Action<GeneralCallbackResult> listener)
```

#### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| listener | Action<GeneralCallbackResult> | --- | 是 | 事件监听函数 |

**GeneralCallbackResult 属性：**

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 错误信息 |

#### 代码示例

```csharp
void Test() {
    _udpClient.OffListening(Listen());
}

void Listen(UDPSocketOnMessageListenerResult result){
    Debug.Log($"[TEST] UDPClient {_udpClient} OnListening: " + res.errMsg);
}
```

### TTUDPSocket.Send
> 6.0.0开始支持该方法，仅WebGL支持该方法
向指定 IP 和端口发送消息。
支持发送 string 或 byte[] 二进制数据。
#### **语法 **

```csharp
public void Send(UDPSocketSendOption option)
```

#### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| option | UDPSocketSendOption | -- | 是 | 发送消息的参数 |

UDPSocketSendOption 属性：

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | -- | 是 | 要发送消息的地址 |
| port | int | -- | 是 | 要发送消息的端口号 |
| message | object | -- | 是 | 要发送的数据 |
| length | double? | null | 否 | 发送数据的长度，仅当 message 为 ArrayBuffer 类型时有效 合法值：自然数，传入0的时候，会设为 message.byteLength |
| offset | double? | null | 否 | 发送数据的偏移量，仅当 message 为 ArrayBuffer 类型时有效 合法值：自然数，大于等于 message.byteLength 时参数不合法，会被强制设为0。 |
| setBroadcast | bool? | null | 否 | 向指定地址发消息时，是否要开启广播 |

#### 代码示例

```csharp
private string _udpAddress = "xxxxxx";
private void Test(){
    _udpClient.Send(new UDPSocketSendOption
    {
        address = _udpAddress,
        port = _udpPort,
        message = "Send string from Unity."
    });
    Debug.Log($"UDPClient 实例已 SendString：${_udpAddress}");
}
```

### TTUDPSocket.ToString
> 6.0.0开始支持该方法，仅WebGL支持该方法
返回该对象的字符串表示。
#### **语法 **

```csharp
public override string ToString()
```

#### 参数说明
无参数。
#### 返回值

| 类型 | 说明 |
| --- | --- |
| string | 返回该对象的字符串表示。 |

#### 代码示例

```csharp
void Test() {
    Debug.Log($"{_udpClient}.ToString()}");
}
```
