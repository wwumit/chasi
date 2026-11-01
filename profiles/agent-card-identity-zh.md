# Agent Card 身份扩展剖面

> 状态：起草稿（v0.1）| 日期：2026-11-01 | 层级：**L4 · 剖面**
>
> 本剖面采用 A2A Agent Card 作为能力发现对象，只增加身份引用。它不重定义 A2A。

## 1. 范围

Agent Card 回答：

- Agent 叫什么；
- 开放哪些接口和能力；
- 提供哪些技能；
- 客户端如何认证和调用。

Agent Card 不确立责任、授权或当前信任状态。这些分别由 Passport、DID Document
和 Registry 承担。

## 2. 复用对象

本剖面使用：

- `/.well-known/agent-card.json`；
- A2A Agent Card 字段和 `capabilities.extensions[]`；
- `agent_did` 的 DID 解析；
- CHA2A Passport 的责任和授权；
- Registry 的当前状态和撤销观测。

## 3. CHA2A 扩展

暂定扩展标识：

```text
urn:cha2a:ext:agent-identity:v1
```

它是暂定 URN。命名空间和解析策略稳定前，不得发布正式 HTTP URI。

扩展只携带引用，不复制第二份凭证：

```json
{
  "uri": "urn:cha2a:ext:agent-identity:v1",
  "required": true,
  "params": {
    "agent_did": "did:cha2a:agent:example",
    "passport": {
      "uri": "https://agent.example/passports/example",
      "digest": "sha256:...",
      "media_type": "application/vnd.cha2a.passport+json",
      "profile": "cha2a-passport-v1.2"
    },
    "registry_did": "did:cha2a:registry:example"
  }
}
```

必选成员：

| 成员 | 要求 |
|---|---|
| `agent_did` | DID，必须与验证通过的 Passport subject 相同 |
| `registry_did` | 验证方应查询的 Registry DID |

可选 Passport 引用：

| 成员 | 要求 |
|---|---|
| `uri` | 绝对 HTTP(S) URI |
| `digest` | 所取工件的 `sha256:` 摘要 |
| `media_type` | Passport 表示的媒体类型 |
| `profile` | Passport 对象或剖面版本 |

## 4. 权威边界

- `agent_did` 在 DID 解析和签名验证通过前只是主张。
- Card 不得声明 `trust_level`、`revoked`、准入状态或结论性信任评级。
- 扩展不得替代 Passport issuer、授权范围、治理域、委托链或 Registry 状态。
- Card 可以引用 Passport，不得通过内嵌未签名 Passport 使其获得权威。

## 5. 发现与托管

首选规范位置是 Agent 自身 origin：

```text
https://agent.example/.well-known/agent-card.json
```

Registry 托管的索引或回退 Card 可以使用，但响应必须标识其为 Registry 托管，
不得与 Agent 自身 Card 混淆。

## 6. 验证顺序

1. 获取 Agent Card；
2. 如带签名，先验证 Card 签名；
3. 提取 `agent_did` 和 `registry_did`；
4. 解析 `agent_did`；
5. 获取引用的 Passport，并按需校验 `digest`；
6. 验证 Passport subject、issuer、授权和有效期；
7. 查询 Registry 状态与撤销；
8. 验证方执行自己的准入策略。

Card 被发现不等于可信；被 Registry 收录不等于可信；Passport 验证通过也不等于准入。

## 7. A2A 兼容

- 对外 Card 使用 A2A 的 snake_case 字段；
- Agent 未实现完整验证链时，不得把 CHA2A 扩展声明为 required；
- 私有或 catalog 投影与规范 well-known Card 分离；
- 现有 camelCase catalog 通过适配器兼容，不定义公开 Card 格式。

### 7.1 签名剖面

公开 Card 携带 `signatures[]` 时，本剖面采用 A2A detached JWS：

- 每个签名包含 `protected` 与 `signature`；
- protected header 是 base64url 编码的 JSON；
- `alg` 为 `EdDSA`；
- `kid` 用于选择验签公钥；
- detached payload 为
  `BASE64URL(protected) + "." + BASE64URL(JCS(移除了 signatures 的 card))`。

签名畸形、`kid` 无法解析或验签失败时必须拒绝。签名只确立签名密钥，不证明能力
声明为真。

## 8. 一致性

最小一致性要求：

1. A2A Card 结构有效；
2. 只有一个 CHA2A 身份扩展；
3. `agent_did` 和 `registry_did` 存在且语法有效；
4. Passport 引用存在时具有绝对 URI 和 SHA-256 摘要；
5. 不内嵌动态信任等级或撤销结论；
6. 完整验证序列不得把 Card 存在当作信任。
7. 存在 Card 签名时，必须能按 `kid` 验证通过。

## 9. 开放问题

- 扩展最终命名空间 URI；
- 公开发现是否强制 Card 签名；
- Passport URI 是否必须与 Card 同源；
- 媒体类型注册；
- Registry 托管回退 Card 的语义。
