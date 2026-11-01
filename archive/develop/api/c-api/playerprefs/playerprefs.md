---
title: "PlayerPrefs"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/playerprefs/playerprefs
update_time: 2025-05-30
---

TTSDK 的 PlayerPrefs 模块。

> 注意：
> - WebGL 方案中，使用 TT.PlayerPrefs 首次会进行数据迁移，迁移成功后就等同于使用 TTFileSystemManager。
> - Native 方案中，使用 Unity.PlayerPrefs 方案存储数据。

## TT.PlayerPrefs
> 6.0.0 开始支持本方法
获取 PlayerPrefs 实例。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static TTPlayerPrefs PlayerPrefs;
```

### 返回说明

| 类型 | 说明 |
| --- | --- |
| TTPlayerPrefs | 返回 TTPlayerPrefs 实例对象，并对 TTPlayerPrefs 对象做相关数据操作 |

### 代码示例

```csharp
public void TestPlayerPrefs()
{
    TTPlayerPrefs playrePrefs = TT.PlayerPrefs;
}
```

## TTPlayerPrefs.SetInt
> 6.0.0 开始支持本方法
设置 int 类型。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public void SetInt(string key, int value)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| key | string | -- | 是 | 数据存储的关键字 |
| value | int | -- | 是 | 数据存储的内容值 |

### 代码示例

```csharp
public void TestPlayerPrefs()
{
    TT.PlayerPrefs.SetInt("keyInt", 123);
}
```

## TTPlayerPrefs.GetInt
> 6.0.0 开始支持本方法
获取 int 类型。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public int GetInt(string key, int defaultValue = 0)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| key | string | -- | 是 | 获取存储的关键字 |
| float | int | 0 | 否 | 获取存储的内容值 |

### 代码示例

```csharp
public void TestPlayerPrefs()
{
    int value4 = TT.PlayerPrefs.GetInt("intKey3");
}
```

## TTPlayerPrefs.SetFloat
> 6.0.0 开始支持本方法
设置 float 类型。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public void SetFloat(string key, float value)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| key | string | -- | 是 | 数据存储的关键字 |
| value | float | -- | 是 | 数据存储的内容值 |

### 代码示例

```csharp
public void TestPlayerPrefs()
{
    TT.PlayerPrefs.SetFloat("floatKey4", 88.8f);
}
```

## TTPlayerPrefs.GetFloat
> 6.0.0 开始支持本方法
获取 float 类型的值。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public float GetFloat(string key, float defaultValue = 0)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| key | string | -- | 是 | 获取存储的关键字 |
| defaultValue | float | 0 | 否 | 获取存储的内容值 |

### 代码示例

```csharp
public void TestPlayerPrefs()
{
    float value5 = TT.PlayerPrefs.GetFloat("floatKey4");
}
```

## TTPlayerPrefs.SetString
> 6.0.0 开始支持本方法
设置 string 类型的值。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public void SetString(string key, string value)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| key | string | -- | 是 | 数据存储的关键字 key |
| value | string | -- | 是 | 数据存储的内容值 value |

### 代码示例

```csharp
public void TestPlayerPrefs()
{
    TT.PlayerPrefs.SetString("key1", "value1");
}
```

## TTPlayerPrefs.GetString
> 6.0.0 开始支持本方法
获取 string 类型的值。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public string GetString(string key, string defaultValue = "")
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| key | string | -- | 是 | 获取存储的关键字 key |
| defaultValue | string | "" | 否 | 获取存储的内容值 value |

### 代码示例

```csharp
public void TestPlayerPrefs()
{
    string value1 = TT.PlayerPrefs.GetString("key1");
}
```

## TTPlayerPrefs.HasKey
> 6.0.0 开始支持本方法
判断是否包含指定 key 的数据存储。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public bool HasKey(string key)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| key | string | -- | 是 | 数据存储的关键字 key |

### 代码示例

```csharp
public void TestPlayerPrefs()
{
    var key = "key1";
    var has = TT.PlayerPrefs.HasKey(key);
}
```

## TTPlayerPrefs.DeleteKey
> 6.0.0 开始支持本方法
删除指定 key 对应的数据。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public void DeleteKey(string key)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| key | string | -- | 是 | 获取存储的关键字 key |

### 代码示例

```csharp
public void TestPlayerPrefs()
{
    var key = "key1";
    TT.PlayerPrefs.DeleteKey(key);
}
```

## TTPlayerPrefs.DeleteAll
> 6.0.0 开始支持本方法
删除所有数据。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public void DeleteAll()
```

### 代码示例

```csharp
public void TestPlayerPrefs()
{
    TT.PlayerPrefs.DeleteAll();
}
```

## TTPlayerPrefs.Save
> 6.0.0 开始支持本方法
保存所有数据到持久化存储中。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public void Save()
```

### 代码示例

```csharp
public void TestPlayerPrefs()
{
    TT.PlayerPrefs.Save();
}
```
