---
title: "数据缓存"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/data-cache/data-caching
update_time: 2025-09-08
---

## TT.Save
> 6.0.0 开始支持本方法，WebGL支持该方法
保存游戏数据接口，所有游戏数据保存上限 50M。
### **语法 **

```csharp
public static bool Save<T>(T serializableObject, string saveName = "")
```

### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| serializableObject | object | -- | 是 | 可序列化的数据(存档类需标记为 [Serializable]) |
| saveName | string | "" | 否 | 数据名 |

### 代码示例

```csharp
[Serializable]
class SaveData
{
    public int IntValue = 99;
    private float FloatValue = 1.0f;
    public string StrValue = "Stark gogo";
    public Dictionary<String, bool> map;
    public List<String> listStr;
    
    public override string ToString()
    {
        StringBuilder sb = new StringBuilder();
        sb.Append("IntValue:").Append(IntValue).Append("\n")
            .Append("FloatValue:").Append(FloatValue).Append("\n")
            .Append("StrValue:").Append(StrValue).Append("\n")
            .Append("Map:\n");
    
        foreach (KeyValuePair<string, bool> entry in map)
        {
            sb.Append("Key:").Append(entry.Key).Append("->Value:").Append(entry.Value).Append("\n");
        }
    
        sb.Append("List:");
    
        foreach (string str in listStr)
        {
            sb.Append(" ").Append(str);
        }
    
        return sb.ToString();
    }
}

private void SaveTest() {
    SaveData sd = new SaveData();
    sd.IntValue = 77;
    sd.StrValue = "Save test";
    sd.map = new Dictionary<string, bool>();
    sd.map.Add("Sekiro", true);
    sd.map.Add("Monkey", false);
    sd.listStr = new List<string>();
    sd.listStr.Add("list1");
    sd.listStr.Add("list2");
    
    bool ret = TT.Save<SaveData>(sd);
}
```

## TT.LoadSaving
> 6.0.0 开始支持本方法，WebGL支持该方法
加载游戏数据接口，返回数据类型需为 Serializable。
### **语法 **

```csharp
public static T LoadSaving<T>(string saveName = "")
```

### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| saveName | string | "" | 否 | 数据名 |

### 返回值

| **类型** | **说明** |
| --- | --- |
| object | 可序列化的数据(存档类需标记为 [Serializable]) |

### 代码示例

```csharp
private void Test() {
    SaveData loaded = TT.LoadSaving<SaveData>();
    
    if (null == loaded)
    {
        Debug.Log("Load failed, save-file not existed");
    }
    else
    {
        Debug.Log("UD_Load\n{0}", loaded.ToString());
    }
}
```

## TT.DeleteSaving
> 6.0.0 开始支持本方法，WebGL支持该方法
删除游戏数据接口。
### **语法 **

```csharp
public static void DeleteSaving<T>(string saveName = "")
```

### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| saveName | string | "" | 否 | 数据名 |

### 代码示例

```csharp
private void Test() {
    TT.DeleteSaving<SaveData>();
}
```

## TT.ClearAllSavings
> 6.0.0 开始支持本方法，WebGL支持该方法
删除所有游戏数据。
### **语法 **

```csharp
public void ClearAllSavings();
```

### 参数说明
无参数。
### 代码示例

```csharp
private void Test() {
    TT.ClearAllSavings();
}
```

## TT.CleanAllFileCache
> 6.5.3 开始支持本方法，WebGL支持该方法
异步删除所有通过网络缓存到本地的文件。
### **语法 **

```csharp
public static void CleanAllFileCache(Action<bool> callback)
```

### 参数说明
如果删除成功，返回true，否则返回false。
### 代码示例

```csharp
private void Test() {
    TT.CleanAllFileCache((result) =>
            {
                if (result)
                {
                    Debug.Log($"异步清理文件缓存成功");
                }
                else
                {
                    Debug.Log($"异步清理文件缓存失败");
                }
            });
}
```

#
