---
title: "tt.getUserGroupTagInfo"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/im-group/tt-getusergrouptaginfo
update_time: 2025-07-31
---

## 语法

```js
tt.getUserGroupTagInfo(openId)
```
基础库 3.80.0 开始支持本方法，这是一个**异步**方法。
获取用户群聊标签信息

## 示例代码
```js
/**
 * @template {typeof tt} S
 * @template {keyof S} T
 * @template {Parameters<S[T]>[0]} Opt
 * @template {Parameters<Opt['success']>[0]} Res
 * @param {T} apiName
 * @param {S} instance
 * @returns {(opt: Opt) => Promise<Res>}
 */
function api(apiName, instance = tt) {
    return (opt = {}) => new Promise((ok, no) => {
        const originOk = opt.success;
        const originNo = opt.fail;
        const originComplete = opt.complete;
        instance[apiName].bind(instance)({
            ...opt,
            success(...args) {
                ok(...args);
                originOk?.(...args);
            },
            fail(...args) {
                no(...args);
                originNo?.(...args);
            },
            complete(res) {
                console.info('>>> 调用异步api ' + apiName + ' 的结果: ', res);
                originComplete?.(res);
            }
        })
    })

}

async function main() {
    const loginInfo = await api('login')();
    const openId = await getOpenId(loginInfo.code); // 请求服务端，在服务端换取openId

    try {
        const res = await api('getUserGroupTagInfo')({
            openId,
        });
        console.log(res.userGroupTags);
    } catch (failObj) {
        console.log(failObj.errMsg ?? failObj.message);
        if (failObj.errNo) {
            switch (failObj.errNo) {
                case 20001:
                    console.log('参数错误');
                    return;
                case 10401:
                    console.log('内部接口请求错误');
                    return;
                case 10103:
                    console.log('无网络');
                    return;
                case 21101:
                    console.log('openId 非法');
                    return;
                case 21102:
                    console.log('内部错误，获取appId 失败');
                    return;
                case 21103:
                    console.log('内部错误，兜底异常');
                    return;
                case 21104:
                    console.log('status 参数不合法');
                    return;
            }
        }
    }
}
main();
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| openId | string | 是 |  | 3.80.0 | 指定用户的openId |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | 返回结果  **对象字段** - **userGroupTags**（Array<Object>）：openId对应用户的所有群聊标签信息 - **errMsg**（string）：固定为 "getUserGroupTagInfo:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 错误信息 |
| errNo | number | 错误码 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | params.xxx should be xxx, but got xxx | 请检测参数类型和取值范围，是否和文档说明一致 | 3.80.0 |
| 10103 | network unavailable |  | 3.80.0 |
| 10401 | internal error |  | 3.80.0 |
| 21101 | open_id invalid |  | 3.80.0 |
| 21102 | mp_id 非法 |  | 3.80.0 |
| 21103 | server internal error |  | 3.80.0 |

## 注意事项
已删除的标签不会出现在返回的userGroupTags列表中

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
