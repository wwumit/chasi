# CHASI Use Case Laboratory

**第一批 Agent Society 核心 Use Cases**

从场景实验驱动 CHASI / CHA2A 的 Architecture、Governance 与 Protocol Evolution

---

> 状态：草案 v1.0 ｜ 日期：2026-10-04 ｜ 种类：**方法（method）**
> 本件是**一组实验性场景**，不是需求规格书，也不是立即冻结的规范。它回答的是“用什么场景去压测架构”，不回答“什么时候做哪个”。

---

## 1. 文档定位

本文件提出 CHASI 第一批 Use Case Laboratory。它不是传统意义上的需求规格书，也不是立即冻结的标准规范，而是一组用于「思想实验 → 场景设计 → 原型验证 → 架构修正 → 规范演进」的实验性场景。

CHASI 可以借鉴 ITU-T Focus Group TIDA 等相关工作对 Use Case 的研究方法，但不以标准化程序为约束。目标更加开放：**用真实、复杂、跨组织的场景，主动暴露 Agent Society 在 Identity、Trust、Delegation、Policy、Evidence、Governance 与 Accountability 方面的缺口。**

## 2. 核心方法：Use Case 驱动架构演进

六个步骤，闭环：

- **Scenario**——定义真实世界中的参与者、组织、agent、任务和环境。
- **Experiment**——让场景真正运行，或至少建立可执行的模拟。
- **Observation**——记录冲突、异常、治理问题和协议缺口。
- **Architecture**——把反复出现的问题提升为架构能力。
- **Specification**——形成可讨论、可复用的 Profile / Protocol。
- **Re-test**——再次运行场景，验证新设计。

```
Scenario → Experiment → Observation → Architecture → Specification → Re-test
                                        ↑                              │
                                        └──────────────────────────────┘
```

**闭环是这一节唯一的要求：** 一个场景若不能回到 `Re-test`，它就只是演示，不是实验。

## 3. 第一批旗舰 Use Cases

| # | 场景 | 一句话 |
|---|---|---|
| UC-01 | 跨组织 Group Collaboration | 三个组织为一次共同任务临时成立 Group |
| UC-02 | Agent Joining a New Society | 一个 agent 第一次进入别的组织主导的 Society |
| UC-03 | Federated Agent Society | 不共享中心平台，各自保有身份、策略与治理 |
| UC-04 | Agentic Commerce | agent 代表人或组织完成有经济后果的交易 |
| UC-05 | Human–agent Coexistence | 一个 Personal agent 同时服务多方，并保有人的控制 |

## 4. UC-01：跨组织 Group Collaboration

这是第一优先级，也是目前已有 Group / Governance 工作最适合直接进入实验的场景。

**典型情境**：Organization A、B、C 各自拥有 agent；三方为了完成一个共同任务临时成立 Group。Group 有自己的 Membership、Role、Policy、Task 和 Lifecycle。**agent 的原始组织归属不能因为加入 Group 而消失。**

流程：

- A 创建任务并邀请 B、C 参加。
- 各 Organization 派出指定 agent。
- Group 建立成员资格、角色和共同 Policy。
- agent 获得任务范围内的 Delegation，而非无限权限。
- 任务过程中产生 Message、Action、Evidence 和 Provenance。
- 任务完成后 Group 解散或转入下一生命周期。
- 所有授权、执行和结果都可以追溯。

**重点验证**：Group 是否应该成为一等治理对象；Organization Policy 与 Group Policy 冲突时如何处理；agent 离开 Group 后权限如何撤销；Evidence 应归属于谁。

## 5. UC-02：Agent Joining a New Society

一个 agent 原本属于 Organization A，现在第一次进入 Organization B 主导的 Society / Group。

流程：

- 发现 Society 的规则与入口要求。
- 证明自己的 Identity、Organization affiliation 和 capability。
- 接受 Society 的 Terms / Policy。
- 获得有限 Scope 的 Membership / Role。
- 通过行为逐渐形成 Trust / Reputation。
- 发生违规时触发限制、暂停或 Revocation。
- 离开 Society 后保留必要 Evidence，但终止运行权限。

**重点验证**：Identity 与 Admission 是否分离；External Credential 是否等于内部 Trust；Trust 是否可以累积；Society 是否需要自己的 Constitution / Policy Layer。

## 6. UC-03：Federated Agent Society

Organization A、B、C 不共享一个中心平台，但需要让各自的 agent 在共同任务中协作。

流程：

- 各 Organization 保持自己的 Identity、Policy、Registry 和 Governance。
- 通过 Federation 建立相互承认的 Trust Relationship。
- agent 可以跨域发现服务和协作对象。
- Delegation 在 Federation 边界上必须明确 Scope。
- Evidence 可以跨域验证，但不必要求所有数据集中存储。
- Federation 可以撤销成员、信任或权限。

**重点验证**：CHA2A 应如何与现有 A2A、MCP、DID/VC 等能力互操作；哪些能力应复用，哪些需要 Profile 或 Extension。

## 7. UC-04：Agentic Commerce

agent 不只是交换信息，而是代表 Human / Organization 完成具有经济后果的交易。

流程：

- 发现服务和 Provider。
- 检查 Capability、Trust、Policy 和价格。
- 根据 Delegation Scope 进行谈判。
- 形成 Contract / SLA。
- 执行服务并产生 Evidence。
- 完成 Payment / Settlement。
- 发生争议时，根据 Evidence、Policy 和 Contract 进行 Dispute Resolution。

**重点验证**：经济行为的授权边界、合同主体、agent Liability、证据链以及跨组织争议处理。

## 8. UC-05：Human–agent Coexistence

这是最能体现 CHASI 长期 Vision 的场景。一个 Personal agent 可能同时服务于一个 Human、一个家庭 Group、一个 Organization、多个专业 Society，并与其他 agent 发生交易。

要点：

- Human 是 Principal，但 agent 具有一定自主性。
- Organization 可以获得有限的 Delegated Authority。
- 不同 Society 对 agent 有不同规则。
- Private Memory 与 Organizational Memory 必须分离。
- Human 可以发出 Override / Stop。
- agent 的 Delegation Chain 必须能够追溯到授权来源。
- 发生冲突时需要明确 Authority、Privacy、Consent 与 Accountability 的优先级。

**重点验证**：agent 到底“属于谁”不是简单的所有权问题，而是 **Identity、Authority、Loyalty、Privacy、Memory、Responsibility 和 Economic Interest 的组合治理问题**。

## 9. 五个场景共享的 Common Model

```
Human / Principal
        ↓
Organization
        ↓
agent
        ↕
Group / Society
        ↓
Identity · Trust · Delegation · Policy
        ↓
Task · Action · Evidence · Provenance
        ↓
Governance · Accountability · Federation
```

这五个 Use Case 不应形成五套独立模型。**实验的目的恰恰是压力测试同一个 Common Model**，并找出哪些对象、关系和治理机制可以跨场景复用。

## 10. 每个 Use Case 的标准实验模板

- **Actors**——Human / Organization / agent / Group / Society / Service。
- **Context**——为什么发生、谁发起、已有信任和身份关系是什么。
- **Goal**——希望完成什么任务。
- **Authority**——谁有权做什么。
- **Scenario Flow**——逐步描述 agent interaction。
- **Governance**——适用哪些 Policy、Role、Membership 和生命周期规则。
- **Compliance**——需要满足哪些约束。
- **Evidence**——必须留下什么证据。
- **Failure Modes**——授权冲突、身份失效、agent 误用、Policy 冲突、恶意行为等。
- **Protocol Requirements**——哪些需要 CHA2A Profile / Extension。
- **Experiment**——如何模拟或实现。
- **Observation**——实际发生了什么。
- **Architecture Change**——实验导致什么架构修改。
- **Specification Change**——最终形成什么规范变化。

**模板的意义在于后五项。** 前九项是场景要交代的，后五项才是实验要产出的——**只有前者没有后者的场景，写出来读着漂亮，什么也不会改变。**

## 11. 与 ITU-T Focus Group TIDA 的关系

CHASI 可以关注并借鉴 ITU-T Focus Group TIDA 等相关工作形成的场景研究，但自身 Use Case Laboratory 不需要等待标准组织形成最终共识。五条态度：

- **兼容**——尽量采用已有术语、模型和公开协议。
- **互补**——把重点放在跨组织 Agent Society、治理和合规这些尚未充分闭环的部分。
- **实验性**——允许提出尚未成熟、甚至最终可能被否定的假设。
- **可验证**——每一个重要理念都尽可能转化成可执行 Scenario。
- **可演进**——Use Case 结果直接推动 Architecture 和 Specification 更新。

## 12. 第一批场景要回答的问题

第一批场景并不是为了展示几个 Demo，而是为了回答一个根本问题：**当 agent 从“工具”逐渐变成具有身份、授权、关系、责任和自主性的社会参与者以后，现有 Internet / Cloud / AI agent 技术栈是否足以支撑这种社会结构？**

CHASI 的价值应当通过这些场景逐渐显现：不是另起炉灶，而是在现有 agent、Identity、Protocol、Cloud 和 Governance 体系之上，补齐 Agent Society 所需要的社会基础设施。

最终目标是形成一个持续循环：**真实场景产生问题，实验产生证据，证据推动架构，架构形成规范，规范再进入新的场景验证。**

—— CHASI Use Case Laboratory · v1.0
