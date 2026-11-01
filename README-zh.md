# CHASI: Compliance Hub for Agent Society Infrastructure

**Specifications for cross-subject identity, authority and evidence in an agent society**

> **CHASI 研究跨主体身份、授权、证据与治理的开放文档。**

## 问题与目标

**本仓讨论的核心对象是 Agent Society。** 它指由人、组织、agent 与群体共同构成、需要跨主体治理与互操作的运行环境。人工智能系统正在从生成信息，转向发现服务、通信、协作、决策、接受委托并代表主体行动。

CHASI 研究这一环境所需的治理与互操作基础设施，包括跨主体的**身份、信任、权威、关系、证据与问责**。

**CHASI 不是又一个 agent 协议，也不是监管机构。** 它连接现有协议与标准，补充跨组织场景中的治理、证据与问责接口。

**文档层面的核心划分是：** *Organization 是治理主体，Group 是协作主体。* 治理边界与协作边界**分开表达**，且**两者都不预设一个中心信任根**。

## 本仓有什么

| 层 | 文档 | 版本 |
|---|---|---|
| **L1 · 愿景** | [`chasi-vision-zh.md`](./vision/chasi-vision-zh.md) — 中文 | v2.26 |
| | [`chasi-vision-en.md`](./vision/chasi-vision-en.md) — English | v2.26 |
| **L2 · 架构**（*不陈述要求*） | [`protocol-suite-architecture-zh.md`](./architecture/protocol-suite-architecture-zh.md) · [`en`](./architecture/protocol-suite-architecture.md) —— 上位架构 | v0.2 |
| | [`governance-architecture-zh.md`](./architecture/governance-architecture-zh.md) · [`en`](./architecture/governance-architecture.md) | v0.3 |
| | [`compliance-hub-architecture-zh.md`](./architecture/compliance-hub-architecture-zh.md) · [`en`](./architecture/compliance-hub-architecture.md) | v0.1 |
| **L3 · 规范** | [`overview-zh.md`](./specs/overview-zh.md) · [`en`](./specs/overview.md) —— **本层的入口，也是本族的入口** | v0.3 |
| | [`organization-governance-zh.md`](./specs/organization-governance-zh.md) · [`en`](./specs/organization-governance.md) | v0.2 |
| | [`group-collaboration-zh.md`](./specs/group-collaboration-zh.md) · [`en`](./specs/group-collaboration.md) | v0.2 |
| | [`question-zh.md`](./specs/question-zh.md) · [`en`](./specs/question.md) | v0.2 |
| | [`naming-zh.md`](./specs/naming-zh.md) · [`en`](./specs/naming.md) | v0.4 |
| | [`passport-zh.md`](./specs/passport-zh.md) · [`en`](./specs/passport.md) —— Passport 对象 | v1.2 |
| **L4 · 剖面** | [`assembly-zh.md`](./profiles/assembly-zh.md) · [`en`](./profiles/assembly.md) | v0.3 |
| | [`lexicon-zh.md`](./profiles/lexicon-zh.md) · [`en`](./profiles/lexicon.md) | v0.3 |
| | [`compliance-profile-zh.md`](./profiles/compliance-profile-zh.md) · [`en`](./profiles/compliance-profile.md) | v0.1 |
| | [`registry-interop-zh.md`](./profiles/registry-interop-zh.md) · [`en`](./profiles/registry-interop.md) | v0.2 |
| | [`agent-card-identity-zh.md`](./profiles/agent-card-identity-zh.md) · [`en`](./profiles/agent-card-identity.md) | v0.2 |
| **L5 · 证据与一致性** | *不在本仓*——证据由 `did-method-cha2a` 承载；一致性向量与核对器在 `cha2a-conformance` | — |
| **L6 · 实现与运营** | *不在本仓*——各实现另在自己的仓 | — |
| **L7 · 方法** | [`use-case-laboratory-zh.md`](./method/use-case-laboratory-zh.md) · [`en`](./method/use-case-laboratory.md) | v1.0 |
| | [`ecosystem-matrix-zh.md`](./method/ecosystem-matrix-zh.md) · [`en`](./method/ecosystem-matrix.md) | v0.1 |
| **L8 · 分发** | *不在本仓*——分发物按次 dated，不留存于此 | — |

**哪一层归谁。** L1 陈述愿景。**L2 不陈述任何要求**——凡出现「必须」，都指向拥有该条的分册（`governance-architecture.md` §1.1）。L3 陈述要求，每一册管自己的主题。L4 承载叠在其下各层之上的剖面。L5 承载一致性向量与核对器。L6 承载实现与运营。L7 承载方法——一次实验怎么设计、怎么跑、怎么记。L8 承载对外交付物。**`specs/overview-zh.md` 是本族的入口文档**；上表是**本仓**的层索引。两者不是二选一——入口讲这一族是什么，索引讲本仓有什么。**上表的「八层」与上位架构的「八层」不是同一套**：上位架构（`protocol-suite-architecture.md` §4）分的是**协议族的功能层**（CHA2A Core · Governance · Passport & Interoperability · Group & Collaboration · Federation · Evidence & Trust · Marketplace / Commerce · Workflow / Task）；上表分的是**本仓文档的层索引**。同名不同物。

**每一层要么有，要么有交代。** L5 / L6 / L8 在**本仓**为空，是决定，不是遗漏：L5 由**两个**并列仓承载（证据在 `did-method-cha2a`、一致性在 `cha2a-conformance`），L6 由各实现自己的仓承载，L8 按次 dated。**L4 已有五份剖面**：组装、词表、合规、Registry 互操作和 Agent Card 身份；「高级别的生态信任态」仍预留，直到出现至少两个独立真实验证方。

**身份核心不在这里。** 身份、证据与 DID 方法本身，维护在并列仓 **`did-method-cha2a`**；各实现另在自己的仓。

**台账不在这里。** 工作计划、版本计划、台账与分发材料一律另置仓外——见下文「本仓放什么」。

### 关于 Vision 的两个版本

**一份文档，两种语言，同一个版本号。** 中文版是正本，英文版是它的译本；两版**版本号相同、二十节完全相同且顺序一致**。两者之间出现差异就是**缺陷，要修**，不是两个不同的侧重点。

**Vision 不承载工作计划。** 两版都不写时间、交付物和动作指派——路线图是另一种文件，受众不同、寿命也不同。

## 治理核心

**Organization** 与 **Group** 是这批文档承载的两个主体。一个 agent 可以属于一个组织，同时参加若干群组；在每一种语境里，**它代表谁行动**是可验证的，而不是由某个平台数据库断言的。

**两册是并列的，不是上下级**：一册回答*谁有资格作出这项授权*，另一册回答*他们在什么语境下、代表谁一起行动*。组织可以在没有智能体的情况下存在，而协作跨组织。

**架构层不是规范。** 它持有原则与对象模型；在那里出现「必须」是越界（`governance-architecture.md` §1.1）。

## 与身份绑定的关系

这批文档**不陈述任何自己的身份要求**。它们写在一个**身份绑定**之上——即某个能在跨域范围内解析主体、并为其状态作答的东西——并把 **`did:cha2a` 命名为所依据的示例**（实验性草案 v1.1.0，记录在 W3C DID Extensions 注册表）。

| 绑定提供什么 | 用在哪里 |
|---|---|
| 组织或成员的跨域解析 | `organization-governance.md` §10 · `group-collaboration.md` §4.5, §9 |
| 状态与撤销的答复 | `group-collaboration.md` §5.2, §9.2, §11 |
| 每个主体的可验证档位 | `group-collaboration.md` §4.1 gate ① |

每一个接口点都列在行使它的那一册的 §10 或 §11 里，因此**满足这些接口的另一个绑定可以取代这个示例**。

## 文档顺序

| 顺序 | 文档 | 回答什么 |
|---|---|---|
| 0 | `vision/chasi-vision-zh.md` | 这是为了什么，以及它预设怎样的社会 |
| 1 | 本文件 | 本仓装了什么，各层如何分工 |
| 2 | `governance-architecture-zh.md` | 这一族为什么长成这样 |
| 3 | `organization-governance-zh.md` | **谁有资格作出这项授权** |
| 4 | `group-collaboration-zh.md` | 不同组织的智能体如何一起工作 |
| 5 | `naming-zh.md` | 名字从哪来，以及引用为什么必须携带校验依据 |
| 6 | `question-zh.md` | **四问答成什么样算答出，以及谁判定** |
| 7 | `method/use-case-laboratory-zh.md` | **用哪些场景压测架构，一次实验必须产出什么** |

## 语言约定

架构层与各分册**英文优先**：各带一个 `-zh` 后缀的中文版。**Vision 是例外**——见上文说明；它的英文版与中文版是不同版本，且中文在前。

## 状态

实验性草案。每一册规范为自己的主题陈述要求；架构层不陈述任何要求。

## 参与与变更控制

- **许可**：Apache License 2.0（见 `LICENSE`）。
- **参与**：通过 GitHub issues / PRs。
- **贡献规则**：[`CONTRIBUTING.md`](./CONTRIBUTING.md)。
- **安全问题**：[`SECURITY.md`](./SECURITY.md)，使用私密报告，不要开公开 issue。
- **行为准则**：[`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md)。
- **本仓放什么**：**只放准备公开的内容。** “暂不公开”的含义是**尚未准备好公开**，不是“用来堆放不宜公开的东西”。工作计划、版本计划、台账、内部评审与分发材料一律另置，**任何目录、任何版本都不进本仓**。
- **变更纪律**：对某一册的实质变更，提升该册版本号。改动说明**只在该版所取代的版本曾经公开之后**才写；在那之前，迭代不对外交代。编辑与链接可以单独提交。
- **复核节奏**：留给部署方的条目、以及某一册未回答的问题，在该册版本提升时重新审视。
- **所依据绑定的参考部署**：`https://compliancehub.cn`。
