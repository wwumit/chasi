# 跨组织 Agent 治理

> **关于本仓的名字。** `chasi` 是本族的 umbrella 名——**C**ompliance **H**ub for **A**gent **S**ociety **I**nfrastructure。本仓承载本族的**立场（L1）**、**架构（L2）**、**规范（L3）**与**剖面（L4）**；身份核心与各实现另在并列仓。本仓自 2026-10-03 至 2026-10-09 名为 `authority-provenance`，umbrella 名取代了它——**一个只命名某一层的名字，装不下整族**。改名与重构记录在 `CHANGELOG.md`。

本仓收录**跨组织边界**行动的 Agent 的文档：**Organization** 作为治理主体，**Group** 作为协作主体。

## 核心主张

> **Organization 是治理主体，Group 是协作主体。**
> **治理边界与协作边界分开表达，且两者都不预设一个中心信任根。**

一个 Agent 可以同属一个 Organization、参与多个 Group。在每个上下文里，**它代表谁**是可验证的，而不是由平台数据库断言。

## 文档

| 文档 | 版本 | 内容 |
|---|---|---|
| [`governance-architecture-zh.md`](./architecture/governance-architecture-zh.md) · [`en`](./architecture/governance-architecture.md) | v0.3 | **架构层。** 为什么这一族是这样分层的：核心原则、双平面对象模型、三个层面（organization · group · federation）、对核心的约束，以及本架构去弃的前提。**不陈述任何要求**；凡出现「必须」，都指向拥有该条的分册 |
| [`organization-governance-zh.md`](./specs/organization-governance-zh.md) · [`en`](./specs/organization-governance.md) | v0.1 | **Organization 作为主体。** 权威的四个来源层（设立依据 → 职位 → 任职者 → 根权威依据）、成员与归属、不可授予的角色、生命周期（退出 · 继任 · 重设根 · Break-Glass · 解散）、治理动作的证据，以及**本册已定与留给部署方的部分（§12）** |
| [`group-collaboration-zh.md`](./specs/group-collaboration-zh.md) · [`en`](./specs/group-collaboration.md) | v0.1 | **协作上下文。** Group 作为一等对象、准入门三道、跨组织规则（不放大 · 撤销级联 · 责任归属）、生命周期、Presence、Chat 与 Task 的关系、**跨 Registry 的解析（§9）**，以及可选的**跨组织 profile（§14）** |
| [`CHANGELOG.md`](./CHANGELOG.md) | — | 变更记录 |

**架构层不是规范。** 它承载原则与对象模型；在它里面出现「必须」即为越界（`governance-architecture.md` §1.1）。

**两册彼此并列**，不是层级：一册回答*谁有资格授权这件事*，另一册回答*他们在什么上下文里、代表谁一起行动*。组织可以没有 Agent 而存在，协作跨越组织。

## 与身份绑定的关系

各册**不自行陈述任何身份要求**。它们针对一个**身份绑定**书写——即能跨域解析主体、并对其状态作答的东西——并把 **`did:cha2a` 作为工作示例**（实验性草案 v1.1.0，已记入 W3C DID Extensions 注册表）。

| 绑定提供 | 用在何处 |
|---|---|
| 组织或成员的跨域解析 | `organization-governance.md` §10 · `group-collaboration.md` §4.5、§9 |
| 状态与撤销的回答 | `group-collaboration.md` §5.2、§9.2、§11 |
| 每个主体的可核验档位 | `group-collaboration.md` §4.1 第①道 |

身份、证据与 DID 方法本身维护在并列仓库 **`did-method-cha2a`**。每个接口点都列在使用它的那一册的 §10 或 §11 中，因此另一个满足这些接口点的绑定可以接替这个示例。

## 读法顺序

| 顺序 | 文档 | 回答的问题 |
|---|---|---|
| 0 | 本文档 | 这一族是干什么的、它承载什么 |
| 1 | `governance-architecture.md` | 为什么这一族是这样分层的 |
| 2 | `organization-governance.md` | 谁有资格授权它 |
| 3 | `group-collaboration.md` | 不同组织的 Agent 怎么一起干活 |

## 语言约定

英文优先。每册都带一个 `-zh` 后缀的中文版；**本文件的中文版即本文件**，英文正本是 [`README.md`](./README.md)。两个版本陈述同一批规则，章节标题与 § 引用一一对应。

## 状态

实验性草案。各册陈述其自身主题的要求；架构层不陈述任何要求。

## 来源

这三册写于 CHA2A 规范组内部，随后迁到本仓，使治理模型的阅读不预设某个 DID 方法。主规范 §11——它的分册索引，未被编辑——把规范组列为 `evidence-record.md`、`agent-identity.md` 与 `EVIDENCE.md`，而这三册从来不在该列表里，因此这次迁移没有改动主规范中的任何引用。迁移记录在 `CHANGELOG.md`。

## 参与与变更控制

- **许可**：Apache License 2.0（见 `LICENSE`）。
- **参与**：经 GitHub issues / PRs。
- **变更纪律**：对某一册的实质性变更会递增该册版本，并在 `CHANGELOG.md` 说明理由；编辑与链接可单独提交。
- **复核节奏**：留给部署方的条目，以及某一册未回答的问题，在该册版本递增时一并复看。
- **所用绑定的参考部署**：`https://compliancehub.cn`。

---

English edition: [`README.md`](./README.md).
