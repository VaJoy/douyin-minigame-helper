---
title: "tt.setGroupTag"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/im-group/tt-set-group-tag
update_time: 2025-07-31
---

## 语法

```js
tt.setGroupTag(openId, tagId, status)
```
基础库 3.80.0 开始支持本方法，这是一个**异步**方法。
设置用户群聊标签

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
    const openId = await getOpenId(loginInfo.code); // 请求服务端，在服务端换取当前用户的 openId

    try {
        await api('setGroupTag')({
            openId, // 根据需要传对应用户的openId，不一定是当前用户
            tagId: 'xxx',
            status: 1,
        });
    } catch (failObj) {
        console.log(failObj.errMsg ?? failObj.message);
        if (failObj.errNo) {
            switch (failObj.errNo) {
                case 20001:
                    console.log('参数错误');
                    return;
                case 10103:
                    console.log('无网络');
                    return;
                case 10401:
                case 21103:
                    console.log('内部服务器错误');
                    return;
                case 21101:
                    console.log('openId 不存在');
                    return;
                case 21102:
                    console.log('内部错误，appId 无能获取');
                    return;
                case 21104:
                    console.log('tagId 现在无法设置');
                    return;
                case 21105:
                    console.log('tagId 不存在');
                    return;
                case 21106:
                    console.log('tagId 已过期');
                    return;
                case 21107:
                    console.log('status 不合法');
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
| openId | string | 否 |  | 3.80.0 | 用户的 openId |
| tagId | string | 否 |  | 3.80.0 | 群聊标签的 id，可在开发者后台中获取 |
| status | number | 否 |  | 3.80.0 | number 类型，群聊标签的佩戴状态  **可选值：** 1=佩戴；3=删除 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 固定为"setGroupTag:ok" |
| isSandboxRequest | boolean | 是否为沙盒环境调用，当标签状态为「待上架」时，返回 true，表示本次调用不会对真实用户设置生效 |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 错误信息 |
| errNo | number | 错误码 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | params.xxx should be xxx, but got xxx | 请根据开发文档和实际错误信息修改 | 3.80.0 |
| 10103 | network unavailable |  | 3.80.0 |
| 21101 | open_id invalid |  | 3.80.0 |
| 21102 | mp_id 非法 |  | 3.80.0 |
| 21103 | server internal error |  | 3.80.0 |
| 21104 | 当前标签状态不支持设置用户标签 |  | 3.80.0 |
| 21105 | 标签不存在 |  | 3.80.0 |
| 21106 | 当前标签已过期 |  | 3.80.0 |
| 21107 | status 非法 |  | 3.80.0 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
