# Passport–Registry 互操作剖面

> 状态：起草稿（v0.2）| 日期：2026-11-01 | 层级：**L4 · 剖面**
>
> 本剖面约束 Passport 验证方如何消费 Registry。它不替代 DID 方法、
> Registry API 或验证方策略。

## 1. 范围

本剖面定义跨主体验证 Passport 所需的最小 Registry 观测：

- DID Document 解析；
- 当前主体状态与撤销；
- 观测来源和新鲜度；
- fail-closed 错误语义；
- 显式跨 Registry peer 查询。

它不定义 Registry 写接口、准入决定、信任评级，也不规定 Registry 的内部存储。

## 2. 职责边界

| 组件 | 负责 | 不负责 |
|---|---|---|
| Registry | DID 解析、身份状态、撤销事实、证据索引 | Passport 签发、准入决定、策略裁决 |
| Passport 签发方 | 签名 Passport 及其授权主张 | DID 分配、当前主体状态 |
| 验证方 | 信任根配置、新鲜度策略、最终裁决 | 改写 Registry 事实 |
| Agent Card | 能力和接口发现 | 责任、授权、撤销状态 |

Registry 回答，验证方决定。

## 3. 核心观测

### 3.1 解析

解析对象必须包含：

| 字段 | 要求 |
|---|---|
| `did` | 请求的精确 DID |
| `document` | `id` 与该 DID 相同的对象 |
| `registryDid` | 响应 Registry 的 DID |
| `source` | 本地 Registry 或 peer 标识 |
| `observedAt` | 验证方取得观测的时间 |

对象 `id` 不一致、文档畸形或缺少来源时，不得作为有效解析接受。

### 3.2 状态

状态观测必须包含：

| 字段 | 要求 |
|---|---|
| `did` | 精确的主体 DID |
| `state` | `active`、`suspended`、`revoked`、`expired` 或 `unknown` |
| `available` | 布尔值 |
| `source` | 观测来源 |
| `registryDid` | 记录所属 Registry |
| `observedAt` | 验证方观测时间 |
| `timeBasis` | `source` 或 `adapter-observation` |
| `subjectRecord` | 来源特定的状态事实 |

`revision` 和 `proof` 是可选能力。声明 `revisioned-reads` 的 Registry
必须保证同一主体的 revision 单调递增。

Registry 如果提供自身断言时间，适配器宜暴露为 `sourceAssertedAt`，并将
`timeBasis` 设为 `source`。否则 `timeBasis` 必须为 `adapter-observation`；
适配器不得把自己的取得时间表述为 Registry 断言。

优先级为 `revoked` > `suspended` > `expired` > `active`。缺失、矛盾或无法映射的
状态不得转换为 `active`。

### 3.3 错误

消费方必须区分：

- `not_found`；
- `unavailable`；
- `unauthorized`；
- `conflict`；
- `malformed`；
- `stale`。

这些是观测结果，不是最终 Passport 裁决。验证方按自身策略处理，缺少必需观测时
fail-closed。

## 4. 新鲜度

新鲜度策略属于验证方。Registry 不得替其他参与方决定观测是否足够新。

观测应携带足够信息，使验证方能判断：

- 最大观测年龄；
- 是否要求 proof；
- 是否必须实时查询；
- 是否允许缓存观测。

Registry 未提供 `sourceAssertedAt` 时，适配器可以使用取得响应的时间作为
`observedAt`，但必须标记时间基准属于适配器观测。

## 5. 联邦

联邦必须显式：

1. 除验证方策略另有规定，先查本地 Registry；
2. 仅联系已配置 peer；
3. 响应携带 `source`、peer 标识、trust domain 和 `registryDid`；
4. peer 失败不得转换成本地成功；
5. 自动 peer 发现不属于本剖面。

Peer 认证可采用 mTLS、签名请求、工作负载身份，或在受控试点中使用受作用域限制的
Bearer Token。具体机制由部署选择，但信任响应前必须建立 peer 身份。长期共享
Bearer Token 不构成生产一致性声明。

## 6. Registry 写入

读互操作是必选基线，写互操作是独立能力：

- `revisioned-writes` 必须携带 `expectedRevision`；
- revision 过期返回 `conflict`；
- 写响应返回已提交 revision；
- 写权限与 peer 读权限分离。

Passport 不规定 Registry 的审批流程或计费方式。

## 7. 当前 CHA2A Registry 映射

| 当前端点 | 剖面观测 |
|---|---|
| `GET /api/v1/did/{did}` | 解析 |
| `GET /api/v1/trust/query?did=` | 状态 |
| `GET /api/v1/trust/revocations` | 撤销来源 |
| `GET /api/v1/evidence/query?did=` | 证据索引 |
| `GET /api/v1/registry/trust/{did}` | 显式 peer 状态 |

当前 API 未直接提供全部规范化字段。适配器应补充 `source`、`registryDid`、
`observedAt` 和规范化 `state`。适配器补字段不改变 Registry 自身主张。

## 8. 能力

Registry 可声明：

- `resolve`；
- `status`；
- `revocation-list`；
- `status-proof`；
- `revisioned-reads`；
- `explicit-federation`；
- `revisioned-writes`。

不支持的能力必须省略，不得以保留能力名义对外声明。

能力声明的规范位置是 Registry 发现文档 `/.well-known/cha2a` 中的
`capabilities`。另设独立能力文档需要未来版本重新规定。

## 9. 一致性

最小一致性要求：

1. DID 与文档精确绑定；
2. 提供规范化状态；
3. 提供来源和观测时间；
4. 区分 not-found 与 unavailable；
5. unknown 不得转为 active；
6. peer 来源显式且故障 fail-closed。

Proof、证据、revision 和写入属于独立能力测试。基础 `v0.2` 不强制状态 proof；
验证方可以在跨域准入策略中自行要求。

## 10. v0.2 决定

- 不强制 `sourceAssertedAt`，但强制 `timeBasis`；
- 基础 Profile 不强制状态 proof，由验证方策略决定；
- peer 必须显式配置并完成身份认证，不固定唯一技术；
- 能力声明放在 `/.well-known/cha2a`。
