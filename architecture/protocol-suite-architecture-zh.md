# CHA2A Protocol Suite Architecture

**Agent Cloud 协议族总体架构与外部协议复用策略**

> 状态：草案（v0.2）｜ 日期：2026-10-01
> 定位：本族的**上位架构**。`governance-architecture` 与 `agent-passport` 在其下展开；Group & Collaboration、Federation、Marketplace/Commerce 等分册亦在此框架下展开
> 原则：**已有标准能用就不另造**——对已有成熟能力优先 Adopt，其次 Map、Profile-Extend、Adapter，**最后才 Define**
> 相关：`governance-architecture.md`（其下的架构层）· `assembly.md`（四槽组装）· `question.md`（判定格式）· `naming.md`（寻址）

---

## 0. 核心主张

> **互认不改信任根；证据不靠运营方。**

**展开表述**：任何跨信任域的 agent 协作，其**授权与证据**都应能被**不属于任何一方**的第三方独立验证。

**为什么必须有这一句**：它是本族内部一切取舍的判据。§10「需要 Define 的区域」、§4 的分层结构、以及各分册的取舍顺序，都要由它裁定——**没有它，每一条都会被保留，结果是写不完。**

**对照参考**：OAuth 的主张是「令牌代替密码做委托授权」；DID Core 是「标识符与文档解耦、可解析」；APS 是「每一跳权限只减不增」；ARIA 是「membrane」。本族此前缺这一句。

---

## 1. 文档定位

本文档定义 CHA2A 面向 Agent Cloud 的长期协议族（Protocol Suite）架构。目标不是重新发明所有底层协议，而是建立一个**可组合、可互操作、可扩展**的 Agent Cloud 协议体系。

对已有成熟能力优先 **Adopt**；需要跨协议语义转换时 **Map**；对 Agent Cloud 场景进行约束或扩展时 **Profile / Extend**；不同协议之间无法直接互操作时采用 **Adapter**；只有 Agent Cloud 核心能力缺少现有规范时才 **Define**。

**这五种关系的最终判据是 §0 的核心主张**：凡不能服务于「互认不改信任根、证据不靠运营方」的能力，一律不进入 Define。

---

## 2. 总体设计原则

- **复用优先**——已有标准能够满足需求时优先采用，而不是另造协议。
- **组合优先**——CHA2A 的核心价值是把 Identity、Governance、Interoperability、Group、Federation、Marketplace 等能力**组织起来**。
- **协议与实现分离**——实验实现不能反向绑架长期架构；实现不足应记录为 **Implementation Gap**。
- **开放互操作**——允许不同 DID Method、Passport、Credential、Registry 和 agent Protocol 共存。
- **Federation-first**——大型伙伴可以保留自己的 Registry / Trust Domain，通过 Federation 接入 Agent Cloud。
- **可演进**——标准尚未稳定的区域采用 Profile、Extension、Versioning 和 Capability Negotiation 保留变化空间。
- **够用即止**——每一份分册必须写明**够用判据**：满足什么条件即视为完备，不再扩写。**没有这条纪律，规范族会持续膨胀。**
- **不预设信任根**——本族不要求任何参与者更换自己的信任根；所有与信任根相关的差异，一律通过**互认**（§10 原创 ③④）处理，而非通过统一化处理。

---

## 3. 总体模型

```
CHA2A Protocol Suite
├── Identity            DID / VC · Passport · Credential
├── Governance          Organization · Admin / Role · Delegation · Policy / Trust
├── Interoperability    A2A · MCP · RCS
├── Collaboration       Group · Workflow · Task
├── Evidence / Trust    evidence · verification · status · audit
├── Federation          Registry / Trust Domain · Partner Registry · Resolution
└── Marketplace         Discovery · Offering / Rental · Commerce
                              ↓
                          Agent Cloud
```

---

## 4. 协议族建议分层

**末列「够用判据」用于界定每层写到什么程度即止**（见 §2「够用即止」）。

| 层 | 职责 | 够用判据 |
|---|---|---|
| **CHA2A Core** | agent、Organization、Registry、基本对象模型、版本／能力协商、基础消息和错误模型 | 任何两个按本族实现的系统，能就「对象是什么」达成一致 |
| **Governance** | Organization、Admin、agent ownership、Delegation、Role、Policy、Trust Domain、跨主体治理 | 能说清「谁签发、谁撤销、谁担责」；且与 APS §10 对齐，不重复定义其已覆盖部分 |
| **Passport & Interoperability** | Passport Profile、DID/VC binding、Agent Card mapping、A2A/MCP 等协议映射、多 DID Method 兼容 | 一份凭证，能被两种体系的**验证方**各自验证通过 |
| **Group & Collaboration** | Group、Membership、Presence、Invitation、跨 Organization Group、协同任务和群聊 | 两个互不隶属的 Organization 的 agent，可加入同一 Group 并完成一次任务 |
| **Federation** | Global Registry、Partner Registry、Trust Domain、跨 Registry Discovery、Resolution、Federation Policy | 任一参与方都不需要改自己的系统，就能被对方承认 |
| **Evidence & Trust** | Signed evidence、action／result records、verification、status、revocation、审计接口 | 第三方不依赖任一方的系统可用性，即可判定一条证据的真伪与时效 |
| **Marketplace / Commerce** | agent offering、Provider、Discovery、Invocation、Rental、Settlement interface；**支付本身不重新定义** | 身份与治理信息足以支撑一次调用，且不需要重新定义支付 |
| **Workflow / Task** | 任务生命周期、Delegation chain、异步任务、Artifact、Review 和协作状态；与 A2A Task model 做映射 | 与 A2A Task model 的映射无信息损失 |

---

## 5. 五种外部协议关系

| 关系 | 含义 |
|---|---|
| **Adopt** | 直接采用已有规范作为 CHA2A 的依赖或兼容基础 |
| **Map** | 定义 CHA2A 对象与外部协议对象之间的语义映射，例如 CHA2A agent 与 A2A Agent Card、Credential 与 Passport artifact |
| **Profile / Extend** | 已有协议基本满足需求，但 Agent Cloud 场景需要约束、配置或扩展 |
| **Adapter** | 已有协议不能直接互操作时定义适配层，而不是强行修改外部协议 |
| **Define** | 仅在 Agent Cloud 核心能力缺少现有规范且需要统一语义时，由 CHA2A 自己定义 |

---

## 6. 外部生态定位矩阵

**对象 · 版本 / 日期 / 状态 · 本族策略。**

| 对象 | 主要解决的问题 | 本族策略 | 版本 / 日期 / 状态 |
|---|---|---|---|
| **OpenA2A** | DID、agent Identity、Trust、Authorization、Transparency | Adopt ＋ Map ＋ Adapter | `did:opena2a` 0.1–0.2 draft；PR #717 merged 2026-07-04（两处版本号在来源之间不一致，未定） |
| **A2A** | Agent-to-Agent communication、Task、Agent Card、Discovery | Adopt ＋ Profile ＋ Map | Google 发起，已进入 Linux Foundation 项目 |
| **MCP** | agent／应用与工具／资源的连接 | Adopt ＋ Adapter | CHA2A 不重新定义 Tool Protocol |
| **APS** | Agent Passport、Delegation、Authority、Evidence | Study ＋ Map ＋ Profile／Adapter | `draft-pidlisnyi-aps-04`，2026-09-28，IETF Individual Draft——**不是已定标准，须标记 work in progress** |
| **ARIA / TrustLayer Foundation / W3C CG** | 跨组织 agent 身份与信任：DNS 锚定 DID ＋ VC ＋ trust ledger ＋ 三阶段准入策略 | Study ＋ Map ＋ Adapter | 注册表已上线；规范 CC-BY-4.0／SDK Apache-2.0；chair 一个 W3C CG（`public-agent-identity`） |
| **蚂蚁 ACT 2.1 / APASS / Alipay+ AMP** | 身份 ＋ 授权 ＋ 支付 ＋ 存证 | Study ＋ Map（**不 Adopt**） | ACT 2.1 已定版开源（文档 CC-BY-4.0／代码 Apache-2.0）；AMP 2026-08-17 建仓 |
| **GB/Z 185-2026 ＋ AIP ＋ 智能体身份码** | 境内 agent 互联的身份、描述、发现、交互、工具调用 | Track ＋ Map | GB/Z 185-2026 于 2026-06-26 发布；AIP 已开源；身份码节点已发证 |
| **银联 APOP《智能体支付开放协议框架》** | 智能体身份管理／意图管理／用户身份管理／支付授权管理 | Track | 2026-04-02 发布；已上架开放平台含沙箱；受邀制 |

**⚠️ 措辞须准确**：GB/Z 是**国家标准化指导性技术文件**，不是标准——**不宜被引用产生强制力**，封面不是「国家标准」，三年内必须复审（可能转国标或撤销）。

**一条会影响判断的组织事实**：IETF 目前没有任何工作组被 charter 处理 AI agent 身份或 agentic authorization。详见 §8。

---

## 7. OpenA2A 对本族的启示

当前公开 OpenA2A 资料显示，`did:opena2a` 已为 0.2 draft，并登记在 W3C DID Extensions Registry。其 Passport 页面明确把 Passport 解释为**由 did:opena2a、AIP、ATX、ATP 等既有 artifacts 组合而成**，而不是必须存在一个独立的 Passport object。

因此 CHA2A **不应把「重新发明一种 Agent Passport 数据格式」作为目标**。更合理的方向是定义 **CHA2A Passport Profile / Federation Envelope**：规定不同 DID Method、Credential、Agent Card、Trust Proof、Delegation 和 Evidence **如何进入 Agent Cloud，并可被跨 Registry / Trust Domain 验证**。

---

## 8. APS 对本族的启示

APS 是当前公开的 IETF Individual Internet-Draft，最新公开版本为 `draft-pidlisnyi-aps-04`（2026-09-28）。其重点覆盖 Agent Passport、代表主体、Delegation、Authority lifecycle、Policy approval、Enforcement、Signed evidence 等。

因此 APS 应作为**重点参考和互操作对象**，而不是作为 CHA2A 已采用的标准。其当前状态必须标记为 **work in progress**。

**IETF 组织现状**（直接影响本族对 IETF 的预期）：

- WIMSE 只章程化到 workload identity（另有一份 agent 专项文件 AIMS）；
- 拟议的 DAWN 章程把 AI agent／tool／skill 的身份管理列为 **out of scope**；
- 拟议的 `agentproto` 章程承诺其参考架构**复用**现有身份、认证与授权积木，而非定义新的；
- 目前**没有任何 WG 被 charter**。

**APS 另有两处对本族有直接指导**：

1. 其 §11 已把 **Adapter Contracts** 写成规范的一部分（含 MCP／A2A／OAuth ID-JAG 绑定，并规定「适配器无法承载某维度时应当怎么办」），可作为本族互操作分册的形态参考；
2. 其官网 Erratum（2026-08-17）自述：已发布的 TypeScript 与 Go 验证器在**父子双方都携带该字段时**才比较 spend 与 depth，且不检查跨跳的有效期包含关系——即**「省略字段」可绕过其核心不变量**。**本族在对应分册中应把「字段缺失即拒绝」写死。**

---

## 9. Passport 的重新定位

CHA2A Passport 的长期定位应从「发明一种新的 agent 身份证件」升级为「**Agent Cloud 可互操作的身份与治理组合层**」。

**下列件中，绝大多数已由外部规范定义。本族对该层的贡献只在两处**：① 规定这些件**如何组合**成一个可被验证的整体；② 规定当件来自不同信任根时的**互认语义**。凡超出这两处的字段定义，一律不做。

- DID / public keys
- Organization / Controller
- Owner / Principal
- Credentials
- Capabilities
- Delegation
- Authorization
- Agent Card
- Trust proofs
- Evidence
- Status / Revocation
- Registry / Trust Domain

---

## 10. 真正需要 Define 的区域

### 10.1 原创（Define）——四条，本族唯一的技术差异点

| 原创项 | 内容 | 够用判据 |
|---|---|---|
| **① Cross-Organization Group** | 跨 Organization 的 Group 成员资格、邀请、授权与协作规则 | 两个互不隶属的 Organization 的 agent 可加入同一 Group 并完成一次任务 |
| **② Registry Federation 与 Trust Domain Federation 的统一语义** | 联邦的**语义模型**，而不只是发现 | 任一参与方不需改自己的系统即可被承认 |
| **③ 不同 Passport / DID / Credential 体系进入同一 Agent Cloud 的 Federation Profile**（即「互认」） | 互认：等价关系由谁建立、由谁签发、范围如何限定、失效如何级联 | **互认不改变任何一方的信任根** |
| **④ 互认之后：证据的第三方独立验证** | 一条证据如何被不属于任何一方的第三方验证；验证不依赖任一方的系统可用性 | 第三方**仅凭公开信息与证据本身**，即可判定其真伪与时效 |

**为什么第 ④ 条必须单列**：这是本族区别于 APS 与 ARIA 的关键。APS 的信任落在其自身的 trust authority 上，ARIA 落在其自身的注册表上——**两者都没有回答「不属于任何一方的第三方怎么验」**。它同时也是 §0 主张的后半句。

### 10.2 对齐（Adopt / Map / Profile）——五条，不做原创定义

| 条目 | 改判为 | 理由 |
|---|---|---|
| Organization 作为 Governance Domain 的标准模型 | 对齐 | APS §10（Charter / Office / Holder / Root Authority Basis / 单调投影 / 离职继任 / Break-Glass / Re-Rooting）已覆盖，且更深 |
| Organization Admin / Super-user / Coordinator 的身份与授权模型 | 对齐 ＋ Profile 差异 | 同上；其中 **Coordinator 为本族特有角色**，可作为 Profile 差异保留 |
| agent membership 与 Organization relationship | 对齐 ＋ 差异说明 | APS 的身份与治理模型已提供框架 |
| Project／Task Delegation、Evidence、Artifact 与治理记录之间的统一关联 | 对齐 | APS §7 ＋ §9 已覆盖（ReceiptV1、DecisionRefV1、Evidence Resolution、三类核心收据） |
| Marketplace 中 Provider、agent offering、租用／调用关系与身份治理的连接方式 | **后置**（依赖 ①②③） | 方向保留，但优先级最低；且 §11 已定不重新定义支付清算 |

---

## 11. 明确不重复定义的区域

- 不重新定义通用 **DID** 标准。
- 不重新定义通用 **Verifiable Credential** 标准。
- 不重新实现 **A2A** 的基础通信语义。
- 不重新实现 **MCP** 的 Tool／Resource／Prompt 协议。
- 不重新定义**支付清算**或具体支付网络。
- **不要求所有生态参与者采用 CHA2A 自己的 DID Method。**
- 不重新定义 **Trust Proof、Trust Level 与 Transparency Log** 的格式（对齐 APS §7／ATP 形态）。
- 不重新定义**信誉与信任等级的评分算法**。

---

## 12. Federation Architecture

Global Registry **不要求成为唯一注册中心**。长期目标是形成可联邦的多 Registry 网络：大型伙伴可以运行自己的子 Registry，同时通过统一 Federation Protocol 与 CHA2A Global Registry 互操作。

**须明确：Federation 的核心不是「发现」，而是「互认」。** 发现（discovery）已有可复用方案（如 MCP Registry 明确无支付层、A2A Agent Card 于 `/.well-known` 发布）；**本族在 Federation 层的原创部分只有互认语义与证据的第三方验证**（§10 原创 ②③④）。

---

## 13. 版本与治理原则

- **主规范保持小而稳定**；新增复杂能力优先进入分册。
- 协议族各分册**不得与 Core 冲突**；通过 extension／profile 处理演进。
- 实验性协议必须明确 **Experimental 状态**，不直接进入核心规范。
- **所有外部协议跟踪必须记录版本、日期、状态和对 CHA2A 的影响。**
- 对未稳定的外部标准，**不将其作为唯一依据**；可参考、可适配、可替换。
- **§0 的核心主张属于最稳定层**；其变更需单独记录变更理由，并触发对 §10 原创清单的重新审视。
- **每份分册在定稿时必须给出「够用判据」；无够用判据者不得进入 Stable。**

---

## 14. 参考资料与状态说明

- **OpenA2A `did:opena2a`**：公开版本 0.2 draft；当前公开资料显示其已登记 W3C DID Extensions Registry。其 Passport 页面把 Passport 描述为**由 did:opena2a、AIP、ATX、ATP 等 artifacts 组合而成**。
- **A2A**：官方文档将其定位为开放的 Agent-to-Agent interoperability standard；项目由 Google 发起并进入 Linux Foundation。
- **APS**：最新公开 `draft-pidlisnyi-aps-04`，2026-09-28；IETF Individual Submission，仍属 Internet-Draft／work in progress。
- **ARIA / TrustLayer Foundation**：注册表已上线（`registry.aria.bar`）；规范 CC-BY-4.0、SDK Apache-2.0；W3C Community Group 为 agent Identity Registry Protocol（`public-agent-identity`）。
- **蚂蚁 ACT 2.1**：已定版开源，文档 CC-BY-4.0、代码 Apache-2.0；APASS 提供商家工作台／Skill／CLI／SDK／OpenAPI；Alipay+ AMP 建仓于 2026-08-17，Apache-2.0。
- **GB/Z 185-2026《人工智能 智能体互联》**（7 部分）：2026-06-26 发布。**性质为国家标准化指导性技术文件，不是标准**；依据《国家标准化指导性技术文件管理规定》第四条，不宜由标准引用使其具有强制性或行政约束力；第十条，发布后三年内必须复审。
- **银联 APOP《智能体支付开放协议框架》**：2026-04-02 发布，含智能体身份管理／意图管理／用户身份管理／支付授权管理四项能力；已上架银联开放平台（含沙箱），受邀制。
- **IETF 组织现状**：目前没有任何 WG 被 charter 处理 AI agent 身份或 agentic authorization；WIMSE 限于 workload identity；DAWN 拟议章程将 agent 身份管理列为 out of scope；`agentproto` 拟议章程承诺复用而不新定义。

**文档性质：架构规划稿，不构成任何外部标准的背书或正式采用声明。**

—— CHA2A Protocol Suite Architecture · v0.2
