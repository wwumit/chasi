# CHASI: Compliance Hub for Agent Society Infrastructure

**Toward a Governed, Interoperable and Human-Centric Agent Society**

> **我们设想这样一个互联网：人与自主智能体能够通过开放、可信、受治理的社会基础设施，共同参与、协作、交易与共存。**
> —— 《CHASI Vision》结语

## 立场

**下一次转变，不只是更好的 AI，而是一个 Agent Society 的出现。** 人工智能正在从"生成信息的模型"走向"能够发现服务、通信、协作、决策、委托权威、交易，并代表人与组织行动的自主智能体"。

CHASI 提出的是这个社会随之所需的**社会基础设施**的愿景：一个开放、可互操作、受治理的环境，人与智能体、组织与群组在其中能够建立**身份、信任、权威、关系、证据与问责**。

**CHASI 不是又一个 Agent 协议，也不是监管机构。** 它互补并连接已有的协议与标准，补上那一层治理与社会基础设施——当智能体从孤立的工具变成互联网规模社会中的持久参与者时，这一层就变得必要。

**其核心主张，一句话**——*Organization 是治理主体，Group 是协作主体。* 治理边界与协作边界**分开表达**，且**两者都不预设一个中心信任根**。

## 本仓有什么

| 层 | 文档 | 版本 |
|---|---|---|
| **L1 · 立场** | [`chasi-vision-zh.md`](./vision/chasi-vision-zh.md) — 中文 | v1.1 |
| | [`chasi-vision-en.md`](./vision/chasi-vision-en.md) — English | v1.0 |
| **L2 · 架构**（*不陈述要求*） | [`governance-architecture-zh.md`](./architecture/governance-architecture-zh.md) · [`en`](./architecture/governance-architecture.md) | v0.3 |
| **L3 · 规范** | [`organization-governance-zh.md`](./specs/organization-governance-zh.md) · [`en`](./specs/organization-governance.md) | v0.1 |
| | [`group-collaboration-zh.md`](./specs/group-collaboration-zh.md) · [`en`](./specs/group-collaboration.md) | v0.1 |
| **L4 · 剖面** | *预留——尚未填充* | — |

**哪一层归谁。** L1 陈述立场。**L2 不陈述任何要求**——凡出现「必须」，都指向拥有该条的分册（`governance-architecture.md` §1.1）。L3 陈述要求，每一册管自己的主题。L4 承载叠在其下各层之上的剖面。

**身份核心不在这里。** 身份、证据与 DID 方法本身，维护在并列仓 **`did-method-cha2a`**；各实现另在自己的仓。

### 关于 Vision 的两个版本

**它们不是平行版本。** 英文是 **v1.0**（16 节）；中文是 **v1.1**，是其**超集**，另带品牌附录（§A.1–§A.7）。**两者是不同版本，不是同一文本的两种语言。** 两者合一尚待处理。

## 治理核心

**Organization** 与 **Group** 是这批文档承载的两个主体。一个 Agent 可以属于一个组织，同时参加若干群组；在每一种语境里，**它代表谁行动**是可验证的，而不是由某个平台数据库断言的。

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

## 阅读顺序

| 顺序 | 文档 | 回答什么 |
|---|---|---|
| 0 | `vision/chasi-vision-zh.md` | 这是为了什么，以及它预设怎样的社会 |
| 1 | 本文件 | 本仓装了什么，各层如何分工 |
| 2 | `governance-architecture-zh.md` | 这一族为什么长成这样 |
| 3 | `organization-governance-zh.md` | **谁有资格作出这项授权** |
| 4 | `group-collaboration-zh.md` | 不同组织的智能体如何一起工作 |

## 语言约定

架构层与各分册**英文优先**：各带一个 `-zh` 后缀的中文版。**Vision 是例外**——见上文说明；它的英文版与中文版是不同版本，且中文在前。

## 状态

实验性草案。每一册规范为自己的主题陈述要求；架构层不陈述任何要求。

## 来源

治理三册写在 CHA2A 规范组内，后迁入本仓，以便治理模型在阅读时不预设某个特定的 DID 方法。主规范 §11——其并列索引，**未被编辑**——列出的是 `evidence-record.md`、`agent-identity.md` 与 `EVIDENCE.md`，从来不含这三册，因此那次迁移没有改动它里的任何引用。

## 参与与变更控制

- **许可**：Apache License 2.0（见 `LICENSE`）。
- **参与**：通过 GitHub issues / PRs。
- **变更纪律**：对某一册的实质变更，提升该册版本号，并在**该册自己的前言**里写明改了什么、为什么。本仓不设仓级 changelog——分册的版本说明就是规范的日志。编辑与链接可以单独提交。
- **复核节奏**：留给部署方的条目、以及某一册未回答的问题，在该册版本提升时重新审视。
- **所依据绑定的参考部署**：`https://compliancehub.cn`。
