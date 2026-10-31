# CHA2A Agent Passport

**面向自主智能体的、可验证、可携带、可治理的社会身份**

> 状态：讨论稿（v1.2）｜日期：2026-10-31｜层：**L3 · 规范**——陈述本件主题的要求
> 定位：Passport 对象的成员、签名、生命周期、验证流程、披露集与符合性要求
> 原则：身份语义按所用 DID 方法确定：`did:cha2a` 以 `did-method-cha2a.md` 为准，其他方法以其自身方法规范为准。证据语义以 `evidence-record.md` 为准。本件不重述、不扩展、不修改任何被引用的规范
> 关联：`organization-governance-zh.md`（谁有资格授权）· `group-collaboration-zh.md`（协作上下文）· `overview-zh.md` §4.4（Registry 与应用的落位）· `assembly-zh.md`（组装）
> 正文以 `passport.md` 为准；两者出现差异即为缺陷，要修。

---

## 本件的状态

本件规定 **CHA2A Agent Passport**：一份签名的、可携带的文档，携带 agent 的主体标识、它所代表的主体人、它所持有的权威、约束该权威的治理上下文，以及其背后证据的引用。

| 项 | 值 |
|---|---|
| 规范状态 | 讨论稿 / 实验性 |
| 规范版本 | 1.2 |
| 文档主题 | agent 的**可携带身份**，以及它据以行动的权威 |
| 规范范围 | Passport 对象、其字段、其验证流程，以及其符合性要求 |
| 身份语义 | 按所用 DID 方法确定：`did:cha2a` 以 `did-method-cha2a.md` 为准，其他方法以其自身方法规范为准；本件不新增标识语法 |
| 证据语义 | 以 `evidence-record.md` 为准；本件复用其谓词，不新增证据格式 |
| 生态 | CHASI / Compliance Hub / CHA2A 规范组 |

### 约定

1. **要求关键词**——`MUST`、`MUST NOT`、`SHOULD`、`SHOULD NOT`、`MAY` 按 RFC 2119 与 RFC 8174 解释。在本件内，它们**只对 Passport 对象**具有规范性。它们不重述、不扩展、不修改 `did-method-cha2a.md` 的要求。
2. **时间戳**——RFC 3339，UTC，以 `Z` 结尾，秒精度或更细。
3. **规范化**——RFC 8785 JSON Canonicalization Scheme（JCS）。
4. **摘要**——SHA-256，小写十六进制。
5. **要求标识**——`PP-n` 表示规范性要求；`DP-n` 表示部署参数；`NIV-n` 表示本版刻意不定义的项。§25 按规范对象给出完整分组与范围。
6. **写明推导**——每一项已定的内容都写明它所依据的原则；可被核对的是推导，不是结论。

---

## 1. 摘要

一个跨组织边界行动的智能体，必须能就自己回答四个问题；而一个第三方必须能在**不问该智能体的运营方**的前提下回答它们：

1. **它是谁？**
2. **谁授权它？**
3. **它在什么上下文中行动？**
4. **它做过什么？**

CHA2A Agent Passport 是一份**由签发方签名**的文档：签发方就 (1) – (3) 中它有能力主张的部分作出回答，并指向回答其余部分的那些对象。它**不携带任何评价结果、任何评级、任何背书**；它携带的是**声明、指针与观察**——把这些变成决定的，是**验证方的动作**，不是 Passport 的内容。

**Passport 不是凭证钱包，也不是注册表记录。** 它是一个**视图**：把散落在主体 DID Document、签发方治理记录、证据层与注册表状态端点里的事实，做成一份稳定、可签名的呈现。**事实住在别处，因此它们在签名之后仍可能改变**——所以本件明确规定：哪些字段**由签发方的签名背书**，哪些是**其真伪不由签名背书的指针**，哪些是**必须在作出决定时刷新的观察**。

> **签名证明签发方这样主张。它不证明主张为真。**

Agent Card 告诉世界这个 agent 提供什么。Passport 告诉社会：这个 agent 是谁、代表谁、在谁的权威之下行动，以及这项主张的证据去哪里核对。

---

## 2. 设计目标

每个目标都带一条**能证伪它的测试**。没有测试的目标只是愿望，而愿望无法被实现。

| # | 目标 | 证伪测试 |
|---|---|---|
| G1 | **可验证**——每一项实质主张都能被独立核对 | 把签发方删掉。一个只持有 Passport 与公开端点的验证方，仍能得出结论。 |
| G2 | **可携带**——可跨平台、跨信任域使用 | Passport 是一个字节串。验证它不需要会话、事先注册，或调用签发方的私有 API。 |
| G3 | **可治理**——权威、角色与委托都被表达 | 对每一条权威记录，验证方都能说出授予方与授予的范围。 |
| G4 | **可问责**——行动能连回主体与授权 | 给定一次行动及其 Passport，验证方能在不联系当事方的情况下说出谁该负责。 |
| G5 | **可互操作**——复用 DID/VC，而非取代它们 | 主体标识是一个 DID，并由既有方法解析；Passport 不引入任何标识语法。 |
| G6 | **顾及隐私**——披露最小化 | 请求 P0 剖面的验证方，收不到 P0 披露集（§16）之外的任何字段。 |
| G7 | **可联邦**——多个组织或 Hub 都能签发与核对 | 两个独立的注册表各自为其控制的主体签发 Passport，而一个第三方能同时验证两者。 |
| G8 | **可扩展**——新的能力、策略与证据类型无需重新设计即可出现 | 新增一个证据谓词只靠引用完成；Passport 字段不变。 |
| G9 | **实现中立**——存储、界面与内部模式不在规范核心内 | 两个不共享任何存储设计的实现，都能声称符合性。 |

### 2.1 本规范不追求的那个目标

**G10 —— Passport 不得成为信任评分。** 它记录事实，并指向证据。它报告的等级是**注册表所拥有的事实的摘要**，并被标记为观察（§6.3，C 层）。一个作出评级的 Passport，会让它的签发方成为它所试图供人判断的那件事的当事方。这也是 `overview.md` §4.3 的立场：**事实，不是评级**。Passport 因此是这一族对象的呈现，而不是一种新权威。

---

## 3. 范围、依赖与非目标

### 3.1 本规范定义什么

- Passport 对象：它的成员、类型、出现条件与来源类别（§6）
- Passport 与可解析主体标识之间的绑定（§7）
- 主体、能力、权威、角色、委托、策略引用与证据引用的表示（§8–§13）
- Passport 生命周期，以及 Passport 状态与标识状态的分离（§14）
- 验证剖面与验证流程（§15）
- 约束验证方能知道什么的披露集（§16）
- 约束 Passport 在何处有效的信任上下文（§17）
- 要求与符合性测试（§23、§25）

### 3.2 依赖——复用，不重定义

每一项依赖都产出一张映射表与一项符合性测试。**没有一项在这里被重定义。**

| 依赖 | 用来 | 映射 | 测试 |
|---|---|---|---|
| `did-method-cha2a.md` | 标识语法、解析、DID Document 形态、状态与撤销、认证等级、调用方鉴权 | §7.1 | §23.4 T-1 |
| `evidence-record.md` | 证据谓词 URI、`evidenceRef`、`artifactDigest` | §13.1 | §23.4 T-2 |
| `agent-identity.md` | agent 作为主体；能力声明结构；`did:cha2a:verifier` 类型 | §9.2、§13.2 | §23.4 T-3 |
| `organization-governance.md` | 谁有资格授权；本件引用的角色与任命语义 | §10.1 | §23.4 T-4 |
| `group-collaboration.md` | 作为治理上下文的群组成员资格 | §10.2 | §23.4 T-5 |
| W3C DID Core | DID Document 结构与验证关系 | §7.1 | §23.4 T-1 |
| RFC 8785（JCS） | 签名与摘要所用的规范化形式 | §6.4 | §23.4 T-6 |
| A2A Agent Card | agent 提供什么、如何到达 | §18.1 | §23.4 T-7a、T-7b |

### 3.3 不定义的——明确拒绝，并给出反例测试

本族与外部对象只有两种关系：**复用**与**不定义**。刻意没有第三种叫"对齐"的关系：它既无产物，又不可证伪。

| 这里不定义 | 反例测试——不引入它，能否建起最小闭环 |
|---|---|
| 一种策略语言或评估引擎 | 一个部署验证一份 `policyRefs` 指向不透明标识、且没有任何实现能解析的 Passport。若验证失败，说明有策略语言漏进了本规范。 |
| 一种证据格式或证词词汇 | 删掉每一个 `evidenceRef` 目标。Passport 在结构上仍然有效，验证返回 `indeterminate`，而不是 `invalid`。 |
| 一种标识语法或 DID 方法 | 主体是一个由既有方法解析的 DID。本件不引入任何前缀、路径文法或资源类型。 |
| 一种服务发现机制、端点格式或传输 | Passport 在各方已经在用的任何信封里交换。§6 里没有任何东西是端点。 |
| 一种 agent 运行时、模型、执行环境或沙箱 | 两个不共享任何运行时的实现，对同一份 Passport 得出同一个结论。 |
| 一种覆盖协议、审批工作流或用户界面 | Passport **记录**"需要批准"，并**引用**有权批准的那一方。它既不定义审批，也不定义界面。 |
| 一种责任分配，或关于责任的法律意见 | §8 说清 Passport 证明什么，然后就此停住。 |
| 一种市场、挂牌或结算机制 | Passport 不是挂牌，不携带价格、可售状态或排名。 |

### 3.4 推迟的，以及具名前置条件

| 推迟 | 做它的前置条件 |
|---|---|
| **基于密码学证明的选择性披露**（BBS+、ZKP） | 一种被至少两个独立实现使用的签名套件，以及一个无需新信任锚即可消费它的验证方。在此之前，披露由 §16 的字段集约束，并靠"不把未披露的事实嵌进文档"来约束。 |
| **一个 `did:cha2a:passport` 资源类型** | 一个"需要注册表可解析的对象"的理由。Passport 是由一方签发的可携带文档，不是注册表维护的主体；给它一个可解析的 DID，会把注册表变成它的签发方，与 §19 相矛盾。 |
| **委托的撤销协议** | 一条能活过单次 Passport 修订的委托链。在此之前，委托随 Passport 携带，并随之重新签发。 |
| **跨注册表的 Passport 背书** | 第二个在自己的信任根下签发 Passport 的注册表。在此之前，`trustContext.validityDomain` 是单一域（§17）。 |
| **机器可读的策略词汇映射** | 两套已在生产中、且被交换 Passport 的各方使用的策略词汇。 |

---

## 4. 术语

| 术语 | 定义 |
|---|---|
| **agent** | 一种能在给定上下文中行动的自主或半自主软件实体。 |
| **主体**（subject） | Passport 所适用的 agent。由一个 DID 标识。 |
| **主体人**（principal） | 主体代表其行动的人或组织。 |
| **签发方**（issuer） | 签署 Passport 的一方。它主张 A 层（§6.3）中的声明，别的都不主张。 |
| **验证方**（verifier） | 评估 Passport 并得出结论的一方。验证方不属于 Passport 的任何一方。 |
| **声明**（claim） | 由签发方主张、并被 Passport 签名覆盖的陈述。 |
| **指针**（pointer） | 指向别处所持对象的引用。它标识并定位，但不确立。 |
| **观察**（observation） | 在某个具名时刻从某个具名来源读到的事实，两者一并记录。 |
| **能力**（capability） | 主体**能**做什么。与权威无关。 |
| **权威**（authority） | 主体在某个治理上下文内**可以**做什么。 |
| **委托**（delegation） | 权威从委托方到受托方的有界转移，带范围、约束与有效期。 |
| **治理上下文** | 权威得以成立的组织、群组、角色与策略。 |
| **信任上下文** | Passport 被视为有效的那个域，以及为其状态观察提供来源的那个注册表。 |
| **依赖方**（relying party） | 依据结论行动的一方。它与验证方的区别只在于：它承担后果。 |
| **判定**（verdict） | `valid`、`invalid`、`indeterminate` 三者之一（§15.3）。 |
| **披露集** | 某个剖面允许验证方收到的字段（§16）。 |
| **剖面**（profile） | 一组具名检查及其披露集（§15）。 |

有两个词刻意避开。**"认证"**（certification）不用来指本件或本件的任何一方——本族把它保留给引用法规的场合，因为在部分法域，这个词会触发特定的责任形态与许可要求。**"鉴权"**（authentication）不被当作验证的同义词：鉴权是连接层的身份确认，验证是对事实的判定。

---

## 5. 概念模型

```
                       ┌──────────────────────────────────────┐
                       │             PASSPORT                 │
                       │                                      │
   A 层  声明 ─────────┤ 主体 · 主体人 · 能力                  │─── 由签名
   （签发方主张）       │ 权威 · 角色 · 信任上下文              │    覆盖
                       │                                      │
   B 层  指针 ─────────┤ 组织 · 群组 · policyRefs             │─── 标识，不确立
   （在别处）           │ 凭证 · 委托证明                       │
                       │                                      │
   C 层  观察 ─────────┤ 状态（来源 · observedAt）             │─── 必须在作出
   （具名来源）         │ 等级 · 有效期 · 撤销                  │    决定时刷新
                       └──────────────────────────────────────┘
                                        │
                                        ▼
                          ┌───────────────────────────┐
                          │        验证流程           │
                          │  剖面 → 检查 →            │
                          │  判定 ＋ 信任上下文        │
                          └───────────────────────────┘
                                        │
                                        ▼
                    valid  ·  invalid  ·  indeterminate
```

§1 的四个问题对应到模型如下。

| 问题 | 由谁回答 | 层 |
|---|---|---|
| 它是谁？ | `subject`、`subjectKey`，经 DID 方法解析 | A ＋ C |
| 谁授权它？ | `authority`、`delegations`，每一环由其委托方签名 | A ＋ B |
| 它在什么上下文中行动？ | `governanceContext`、`policyRefs`、`trustContext` | A ＋ B |
| 它做过什么？ | `credentials`，每一项都是带状态与摘要的指针 | B ＋ C |

---

## 6. Passport 对象

Passport 是一份 JSON 文档。它的规范形态由下列成员定义；它的线格式是 JSON（UTF-8），其签名形态与摘要形态使用 §6.4 的规范化。

### 6.1 成员

出现性：**M** 必填，**C** 条件性（条件已写明），**O** 可选。
来源：**A** 声明，**B** 指针，**C** 观察，**D** 派生。

| 成员 | 类型 | 出现性 | 来源 | 条件、来源与含义 |
|---|---|---|---|---|
| `@context` | 字符串数组 | M | — | 第一项为 `https://www.w3.org/ns/did/v1`；第二项为 Passport 的 context URI（§22.1）。 |
| `type` | 字符串 | M | — | 字符串 `Cha2aAgentPassport`。 |
| `specVersion` | 字符串 | M | — | 文档所符合的本规范版本。 |
| `passportId` | 字符串（URN） | M | A | 标识**脉络**：一份逻辑 Passport，跨修订稳定。形式见 §6.2。 |
| `passportDigest` | 对象 | M | D | `{ "algorithm": "sha256", "value": "<hex>" }`，作用在 §6.4 的输入上。标识**这一次修订**。 |
| `subject` | 字符串（DID） | M | A | 本 Passport 所适用的 agent。必须经验证方支持的标识方法解析（§7）。 |
| `subjectKey` | 对象 | C | A | 主体自己的验证密钥。剖面要求主体签名动作时必填（§15.2 P2 及以上）。成员见 §7.2。 |
| `issuer` | 字符串（DID） | M | A | 签署本 Passport 的一方。必须是 `proof.verificationMethod` 所指密钥的控制者。 |
| `issuedAt` | 字符串（时间戳） | M | A | 本次修订被签署的时刻。 |
| `notBefore` | 字符串（时间戳） | O | A | 本次修订最早有效的时刻。缺失即等于 `issuedAt`。 |
| `expiresAt` | 字符串（时间戳） | M | A | 此后本次修订无效的时刻。**不允许缺失**：没有终点的权威不可被委托（§11.3）。 |
| `principal` | 对象 | C | A | 主体代表他方行动时必填。成员见 §8.1。 |
| `governanceContext` | 对象 | M | A ＋ B | 成员见 §10.3。允许空对象，表示未主张任何治理上下文。 |
| `capabilities` | 对象数组 | M | A | 主体能做什么。允许空数组。成员见 §9.1。 |
| `authority` | 对象数组 | C | A ＋ B | 当 Passport 被出示以证明某项行动时必填（非空）。成员见 §9.3。 |
| `delegations` | 对象数组 | C | A ＋ B | 当任一 `authority` 条目是经一条以上环节的链路授予时必填。成员见 §11.1。 |
| `policyRefs` | 对象数组 | C | B | 当 `authority` 非空时必填（非空）。成员见 §12.1。 |
| `credentials` | 对象数组 | C | B ＋ C | 剖面 P3、P4 必填（非空）。成员见 §13.3。 |
| `status` | 对象 | M | C | 主体的标识状态，读自注册表。成员见 §14.3。 |
| `trustContext` | 对象 | M | A | 成员见 §17.1。 |
| `proof` | 对象 | M | A | 签发方的签名。成员见 §6.4。 |

**PP-1.** Passport 不得包含 §6.1 未定义的成员，除非其名称以 `x-` 开头。扩展成员必须被不识别它的验证方忽略，且不得成为任何剖面通过的必要条件。*（依据：G8 要求无需重新设计即可扩展；一个未加命名空间的扩展会与未来的规范版本相撞。）*

**PP-2.** 验证方不得因为它不认识某个 `x-` 成员而拒绝一份 Passport。

**PP-3.** 声明为必填的成员必须出现，即使其值为空（空数组或空对象），以便"未主张"与"未出现"可以区分。

### 6.2 `passportId`

```
urn:cha2a:passport:<issuer-scope>:<opaque>
```

- `issuer-scope` 是签发方的注册标识：基于域名的签发方用其主机名（`compliancehub.cn`），或签发 DID 的主体标识。
- `opaque` 是签发方在该作用域内自选的唯一值。建议用 ULID 或 UUIDv7，以便签发顺序可恢复。

**PP-4.** `passportId` 不得是 `did:cha2a` 标识。*（依据：Passport 是由一方签发的文档，不是注册表维护的主体。给它一个可解析的 DID，会把它的签发放进注册表，与 §19 R1 矛盾。）*

**PP-5.** 两份 `passportId` 相同而 `passportDigest.value` 不同的 Passport，是同一脉络的两次修订。验证方必须只把出示的那一次修订视为当前，且不得跨修订合并成员。

### 6.3 三个来源类别

**PP-6.** 验证方必须把它所依赖的每一个成员恰好归入一个来源类别，且不得把 B 层或 C 层成员当作已被签发方签名确立。

| 类别 | 签名确立了 | 签名没有确立 |
|---|---|---|
| **A —— 声明** | 签发方在 `issuedAt` 主张了这个值 | 这个值是真的 |
| **B —— 指针** | 签发方主张这个引用能解析到它认为相关的对象 | 该对象存在、当前有效，或说的就是签发方暗指的内容 |
| **C —— 观察** | 签发方在具名时刻从具名来源读到了这个值 | 该值在作出决定时仍然当前 |

**PP-7.** C 层成员必须同时携带 `source` 与 `observedAt`。当观察的年龄超过 `status.statusMaxAge` 时，验证方必须重读 C 层成员，且不得把陈旧观察当作当前（§14.4）。

**PP-8.** B 层成员必须无歧义地标识其目标（一个 URI、一个 DID，或一个 URN），且当目标内容对主张是实质性的，必须携带摘要。不带摘要的指针只确立"某个对象被指称过"。

### 6.4 规范形式、摘要与签名

**定义。**

- `digestInput` ＝ 去掉 `proof` 与 `passportDigest` 两个成员后，Passport 的 JCS 序列化。
- `passportDigest.value` ＝ `digestInput` 的 UTF-8 字节的 SHA-256，小写十六进制。
- `proofInput` ＝ 去掉 `proof` 成员后，Passport 的 JCS 序列化。
- `proof.payload` ＝ 字符串 `proofInput`。

**PP-9.** `passportDigest.value` 必须等于重算出的 `digestInput` 的 SHA-256。不一致必须产生 `invalid`。

**PP-10.** 签名必须计算在 `proof.payload` 的 UTF-8 字节之上。

**PP-11.** `proof` 对象必须携带 `type`、`created`、`verificationMethod`、`proofPurpose` 与 `signatureValue`，并必须按上述规定携带 `payload`。必须支持签名套件 `Ed25519Signature2020`，`proofPurpose` 为 `assertionMethod`。*（依据：这已是参考注册表在 `/api/v1/trust/proof` 输出的形态，因此一个符合的验证方可以两条路复用同一段代码。见附录 B 第 B-4 行。）*

**PP-12.** `proof.verificationMethod` 必须经签发方的 DID Document 解析到列在 `assertionMethod` 验证关系下的密钥。验证方不得使用 DID Document 未为该用途列出的密钥。

**PP-13.** 若 `issuer` 不是所解析密钥的控制者，验证方必须拒绝该 Passport；若 `proof.verificationMethod` 的 DID 部分与 `issuer` 不同，也必须拒绝。

**PP-14.** 签名与摘要必须使用 JCS。验证方不得在验证前尝试重新序列化文档；它必须作用在收到的 `proof.payload` 字节上，且仅在计算摘要时做规范化重算。

### 6.5 签名不覆盖什么

**PP-15.** 签名不确立任何指针可解析、任何观察是当前的、任何被委托的权威仍被持有，或任何证据存在。一个不解析指针、不刷新观察就报告结论的验证方，是在把签发方的断言当作事实来报告。

---

## 7. 身份

### 7.1 标识绑定

**PP-16.** `subject` 必须是一个 DID，且必须经验证方支持的方法解析出 DID Document。

**PP-16 不限定 DID 方法。** 方法特定规则只在对应方法下适用：`did:cha2a` 的标识规则见 PP-17；其他方法的标识语法、解析与验证关系由该方法自身规范确定。部署所支持的方法由 DP-2 声明。

**PP-17.** 当 `subject` 使用 `did:cha2a` 方法时，DID 必须符合 `did-method-cha2a.md` §3.1 的 ABNF，且按该文件 §3.4 的要求，字面前缀与资源类型槽必须按**大小写敏感的小写**处理。验证方必须在比较标识之前应用该方法的大小写规则。

**PP-18.** 验证方必须在规范化之后按精确匹配比较 DID。不得因为一个是另一个的前缀而视为同一，也不得从标识的资源类型或共享主机推断权威。

**PP-19.** Passport 不得要求新增一个 `did:cha2a` 资源类型。*（依据：`did-method-cha2a.md` §3.2 的资源类型表是一个封闭列表，且该文件被 W3C 的注册表条目按固定版本引用。Passport 不是注册表签发的资源。）*

**PP-20.** `issuer` 必须是一个 DID，必须可解析，且不要求与 `subject` 使用同一方法。

### 7.2 `subjectKey`

| 成员 | 类型 | 出现性 | 含义 |
|---|---|---|---|
| `keyId` | 字符串 | M | 验证方法标识，例如 `did:cha2a:agent:dshlib#agent-key`。 |
| `algorithm` | 字符串 | M | 密钥算法。 |
| `publicKeyMultibase` | 字符串 | C | 当密钥经 DID Document 的 `verificationMethod` 解析时出现。 |
| `fingerprint` | 字符串 | M | 由标识方法的密钥端点报告的指纹（若存在该端点）。 |

**PP-21.** 主体密钥必须是主体自己控制的密钥，且必须与注册表的签名密钥不同。*（依据：`did-method-cha2a.md` §5 产生的 DID Document 里，注册表密钥与主体自己的密钥是两个独立的验证方法；只有后者能替主体签名。）*

**PP-22.** 当 `subjectKey` 出现时，验证方必须解析主体当前的密钥，并用其指纹与 `subjectKey.fingerprint` 比对。不一致必须产生 `invalid`。*（依据：Passport 会活过密钥轮换。与实时密钥比对，才使绑定保持当前；与 Passport 自带的副本比对，会让一把已轮换的密钥永远有效。）*

**PP-23.** 验证方不得从 `subjectKey` 的存在推断主体参与过某次交换。参与由对动作的签名确立（§21，威胁 TH-2）。

### 7.3 可分离性

**PP-24.** 身份主张必须能与能力、权威与证据主张分离，以便只要求身份的剖面可以在不收其余部分的情况下被满足（§16）。

---

## 8. 主体人与责任

一个 agent 可以自主行动，同时仍代表某一方行动。这种关系存在时，Passport 明确陈述它，并点名那一方。

### 8.1 `principal`

| 成员 | 类型 | 出现性 | 含义 |
|---|---|---|---|
| `did` | 字符串（DID） | M | 主体人。 |
| `role` | 字符串 | M | 所主张的关系：`operating-organization`、`owner`、`controller`、`client`，或已注册词汇中的值。 |
| `onBehalfOf` | 字符串（DID） | O | 当主体人自己又代表他方时，再上一方。链长超过一层必须以 `delegations` 表示（§11），不得用嵌套表示。 |
| `verificationRef` | 字符串（URI） | O | 该关系的证据所在。 |

**PP-25.** 当 `principal` 出现时，主体人的 DID 必须可解析，且 Passport 不得主张一个与主体人自身治理记录相矛盾的关系——能够核对主体人记录的验证方，必须优先采信那些记录，而非本声明。

**PP-26.** `principal.onBehalfOf` 的嵌套不得超过一层。更长的链是一次委托，必须在 `delegations` 中表示。

### 8.2 Passport 证明什么

```
人 / 组织        →      主体人      →      agent       →      行动
     治理                    授权              执行
```

**PP-27.** Passport 证明这条链上的**技术关系**。它不分配法律责任，且其任何成员都不得被呈现为在分配责任。

**PP-28.** 给定一次行动及其 Passport，验证方必须能在**不联系当事方**的情况下说出谁对这次行动负责（G4）。做不到时，结论为 `indeterminate`，且缺失的那一环必须写在输出里。

---

## 9. 能力与权威

### 9.1 `capabilities[]`

| 成员 | 类型 | 出现性 | 含义 |
|---|---|---|---|
| `name` | 字符串 | M | 能力，可以是技能 DID、名称，或带命名空间的标签。 |
| `version` | 字符串 | O | 版本或兼容范围。 |
| `protocols` | 字符串数组 | O | 可达该能力的交互协议。 |
| `assertion` | 字符串 | M | `self-declared` 或 `attested`。 |
| `attestationRef` | 字符串（URI） | C | 当 `assertion` 为 `attested` 时必填。 |

**PP-29.** `assertion` 必须出现，且必须是 `self-declared` 或 `attested` 之一。*（依据：`agent-identity.md` §5 把已声明能力与已核验能力分开。把这一区分做成必填的机器可读字段，才能防止它在传输中丢失。）*

**PP-30.** `assertion: self-declared` 的能力不得被当作权威，也不得满足任何要求权威的检查。*（依据：§9.2。）*

**PP-31.** 验证方不得因为承载该能力的 Passport 被签名，就把该能力视为已核验。签发方的签名证明的是**声明**，不是**能力**。

### 9.2 能力与权威的区分

```
   能力 = 能做          权威 = 可以做
          主体的属性            治理上下文的属性
```

**PP-32.** 能力与权威不得混同。符合规范的 Passport 必须在分离的成员中表示二者，符合规范的验证方必须只从 `authority` 推导许可。

### 9.3 `authority[]`

| 成员 | 类型 | 出现性 | 含义 |
|---|---|---|---|
| `grantId` | 字符串（URN） | M | 标识这次授予。 |
| `scope` | 字符串数组 | M | 被允许的操作。 |
| `grantedBy` | 字符串（DID） | M | 授予方。 |
| `policyRef` | 字符串 | C | 当 `policyRefs` 非空时必填：该授予所依据的策略标识。 |
| `constraints` | 对象 | O | 收窄条件（§9.4）。 |
| `notBefore` | 字符串（时间戳） | O | 有效期起点。默认取 Passport 的 `notBefore`。 |
| `notAfter` | 字符串（时间戳） | M | 有效期终点。不得超过 Passport 的 `expiresAt`。 |
| `evidenceRef` | 字符串（URI） | O | 该授予的证据所在。 |

**PP-33.** 每一条 `authority` 必须点名 `grantedBy` 一方，且该方必须是 `principal`、经 `delegations` 可达的一方，或经 `governanceContext` 可达的组织控制者。

**PP-34.** 每一条权威记录都必须有 `notAfter`。没有终点的权威不可表达。

**PP-35.** 被要求证明某次行动的验证方，必须找到这样一条 `authority`：其 `scope` 含该操作、有效期窗口含决定时刻、且约束均被满足。找不到必须产生 `invalid`；找到但约束无法评估，必须产生 `indeterminate`。

### 9.4 `constraints`

约束只收窄，从不放宽。已识别的成员：

| 成员 | 含义 |
|---|---|
| `maxDepth` | 自本次授予起的最大委托深度。 |
| `counterparties` | 该权威可对其行使的 DID 封闭列表。 |
| `purpose` | 已声明的用途，行动必须与之相符。 |
| `rateLimit` | 有界速率，并写明窗口。 |
| `humanApproval` | 当行动前必须有人批准时为 `required`，并列出可批准的 DID。 |
| `dataClasses` | 该权威可触及的数据分类。 |
| `x-*` | 部署方定义的约束。 |

**PP-36.** 约束不得以任何会**放大**授予的形式表达。若某条 `authority` 的约束放大了其母授权的范围，验证方必须拒绝；且不得忽略它无法评估的约束——不可评估的约束产生 `indeterminate`。

---

## 10. 治理上下文与角色

### 10.1 角色

**PP-37.** 角色必须按签发方、治理域与有效期限定。没有签发方或没有有效期的角色必须被拒绝。*（依据：`organization-governance.md` 回答谁有资格授权；一个不受限定的角色什么都回答不了，因为任何人都有可能在任何时段签发它。）*

**PP-38.** 角色必须把其治理域写为 `organization`、`group`、`society`、`service` 之一。

### 10.2 治理域

| 域 | 权威被什么限定 | 来源 |
|---|---|---|
| `organization` | 一个组织的章程与记录 | `organization-governance.md` |
| `group` | 跨越组织的协作上下文 | `group-collaboration.md` |
| `society` | 一个联邦范围的约定 | `trustContext`（§17） |
| `service` | 某个服务自己的条款 | 该服务的运营方 |

**PP-39.** 在某一个治理域授予的权威，不得被视为在另一个域中成立。验证方必须比较授予的域与行动发生的域。

### 10.3 `governanceContext`

| 成员 | 类型 | 出现性 | 含义 |
|---|---|---|---|
| `organization` | DID 字符串数组 | O | 主体所属的组织。 |
| `groups` | 对象数组 | O | 群组成员资格：`{ "group": "<urn 或 DID>", "role": "<字符串>", "validUntil": "<时间戳>", "evidenceRef": "<uri>" }`。 |
| `roles` | 对象数组 | O | 角色：`{ "role": "<字符串>", "domain": "<字符串>", "issuer": "<did>", "validUntil": "<时间戳>", "evidenceRef": "<uri>" }`。 |

**PP-40.** `governanceContext` 的每个成员都是 A 层声明，除非它携带 `evidenceRef`——此时该引用是 B 层，而声明仍是 A 层。只有声明而没有证据时，验证方不得把成员资格报告为已确立。

**PP-41.** 当群组自身的记录可达时，群组成员资格必须与之核对。Passport 记录声明；群组的记录作出决定。

---

## 11. 委托

委托是权威到达一个 agent、而主体人不必为每一次操作重新授予的机制。它是 Passport 中最容易被静默提权的一部分，因此规则写得最明确。

### 11.1 `delegations[]`

| 成员 | 类型 | 出现性 | 含义 |
|---|---|---|---|
| `delegationId` | 字符串（URN） | M | 标识这一环。 |
| `delegator` | 字符串（DID） | M | 转移权威的一方。 |
| `delegatee` | 字符串（DID） | M | 接收权威的一方。 |
| `scope` | 字符串数组 | M | 被转移的权威。 |
| `constraints` | 对象 | O | 收窄条件，同 §9.4。 |
| `notBefore` | 字符串（时间戳） | O | 有效期起点。 |
| `notAfter` | 字符串（时间戳） | M | 有效期终点。 |
| `furtherDelegation` | 字符串 | M | `none`、`same-scope` 或 `explicit`。 |
| `depth` | 整数 | M | 本环在链中的位置，以主体人为 1 起算。 |
| `maxDepth` | 整数 | M | 该链可含的最深一环。 |
| `parentDelegationId` | 字符串（URN） | C | 当 `depth` 大于 1 时必填；在 `depth` 为 1 时必须缺失。 |
| `revocationRef` | 字符串（URI） | O | 本环撤销状态的发布处。 |
| `proof` | 对象 | M | 委托方对本环的签名（§11.2）。 |

### 11.2 规则

**PP-42 —— 收窄。** 对每一环，`scope` 必须是母授权 `scope` 的子集，`constraints` 必须收窄母授权。范围不是子集的环必须被拒绝，且拒绝必须点名**放大**的那个成员。*（依据：本族中的权威只被授予、从不被假定；子集关系是唯一无法靠改标签满足的检查。）*

**PP-43 —— 单调性。** 一条链只有在每一环的权威集都是其前一环的子集时才有效。验证方必须评估整条链，不得停在第一个满足所请求范围的环上。

**PP-44 —— 显式深度。** 每一环必须出现 `depth` 与 `maxDepth`，必须是整数，且 `depth` 不得超过 `maxDepth`。

**PP-45 —— 继续委托。** `furtherDelegation` 必须取三值之一：`none` 禁止任何子环；`same-scope` 允许范围与本环相等的子环；`explicit` 仅当本环的 `constraints` 点名了被允许的受托方时才允许子环。

**PP-46 —— 无环。** 链必须无环。若同一委托方在链中出现多次（包括经不同标识规范化为同一 DID 的情形），验证方必须拒绝该链。

**PP-47 —— 终止。** 每条链必须终止于 Passport 的 `principal`，或终止于经 `governanceContext` 可达的组织控制者。两者都不终止的链必须被拒绝。*（依据：§8.2 要求可点名负责方。）*

**PP-48 —— 逐环签名。** 每一环必须携带其委托方对该环规范形式的签名，验证方必须独立验证每一环。验证方不得凭 Passport 自身的签名接受某一环。*（依据：Passport 的签名是签发方的。凭它接受一环，会让签发方凭空制造出没有委托方授予的权威，并把委托方从记录里抹掉。）*

**PP-49 —— 有效期交集。** 某一环的有效期窗口，必须是它自身、其母环与 Passport 三者窗口的交集。落在任一窗口之外的动作必须被拒绝。

**PP-50 —— 撤销级联。** 撤销某一环，必须使所有 `parentDelegationId` 链包含它的环失效。能够到达 `revocationRef` 的验证方必须检查它，且必须检查**每一个祖先环**的引用，而不只是叶子。*（依据：只查叶子，会让撤销一个中间环后，其下游仍然有效。）*

**PP-51 —— 自我委托。** `delegator` 与 `delegatee` 为同一主体的环必须被拒绝。

### 11.3 刻意缺席的

**NIV-1 —— 委托撤销协议。** Passport 为每一环点名 `revocationRef`。一环如何被撤销、撤销如何到达验证方，本件不定义：那属于注册表或应用的题目，定义它的前置条件记在 §3.4。在此之前，撤销经引用被观察；**引用不可达时产生 `indeterminate`，而不是 `valid`**。

**NIV-2 —— 人的覆盖协议。** `constraints.humanApproval` 记录"需要批准"，并点名谁可以批准。承载批准的那个协议、它的表示与它的撤销，本件不定义。*（测试：一个部署可以在完全没有 `humanApproval` 的情况下满足所有剖面。若某剖面必须靠它才能通过，说明有审批工作流漏进了本规范。）*

---

## 12. 策略引用

Passport 标识其权威所依据的策略。它不携带策略，也不评估策略。

### 12.1 `policyRefs[]`

| 成员 | 类型 | 出现性 | 含义 |
|---|---|---|---|
| `id` | 字符串（URI 或 URN） | M | 策略标识。 |
| `issuer` | 字符串（DID） | M | 签发该策略的一方。 |
| `version` | 字符串 | M | 策略版本。 |
| `scope` | 字符串数组 | O | 该策略治理的操作。 |
| `effectiveFrom` | 字符串（时间戳） | O | 策略生效起点。 |
| `effectiveUntil` | 字符串（时间戳） | O | 策略生效终点。 |
| `digest` | 对象 | O | `{ "algorithm", "value" }`，作用在策略文档上；当确切文本是实质性的时候使用。 |

**PP-52.** `policyRefs` 的每一项必须携带 `id`、`issuer` 与 `version`。没有版本的策略引用必须被拒绝。*（依据：本族记录每一个外部对象时都带版本与日期。一个无版本的策略引用，无法与"授予该权威时生效的那一版策略"核对。）*

**PP-53.** 每一条 `authority.policyRef` 必须与 `policyRefs` 中恰好一项的 `id` 相符。悬空的 `policyRef` 必须产生 `invalid`。

**PP-54.** 验证方不得评估策略。它必须报告判定所依赖的是哪些策略引用、各自的版本是什么，并把评估留给应用（§19 R3）。

**PP-55.** 当某策略文档带有 `digest` 而验证方取不到该文档时，不得把该行动报告为"在该策略下被允许"。它报告 `indeterminate`。

---

## 13. 凭证、证明与证据

### 13.1 对证据层的复用

**PP-56.** 证据谓词类型必须使用 `evidence-record.md` §3 的 URI，包括复用的 in-toto 谓词与 `cha2a/*` 命名空间下的谓词。本件不引入任何谓词。

**PP-57.** 凭证引用必须携带 `evidenceRef`，并在内容具实质性时携带 `artifactDigest`。证据层使用的摘要形式是：

```
"artifactDigest": { "sha256": "<小写十六进制>" }
```

**PP-58.** Passport 不得包含证据本体。它携带引用、状态与摘要。*（依据：`overview.md` §4.4 R2——主体能自己签的，就留在主体侧；注册表与 Passport 只存指针或哈希，永不存正文。）*

### 13.2 验证方身份

**PP-59.** 凭证的 `verifier` 必须是已注册、其 DID 可解析的一方；它对该证明的签名确立这条陈述是它作出的。无法解析的验证方，必须使该凭证被报告为"未确立"，而不是"假"。

**PP-60.** 凭证不得因为 Passport 的签名而被视为已确立。签名证明的是引用，不是证明本身。

### 13.3 `credentials[]`

| 成员 | 类型 | 出现性 | 含义 |
|---|---|---|---|
| `id` | 字符串 | M | 凭证标识。 |
| `predicateType` | 字符串（URI） | M | 同 §13.1。 |
| `verifier` | 字符串（DID） | M | 作出证明的一方。 |
| `result` | 字符串 | O | 记录的结果，若该谓词有结果（`passed`、`failed`，或谓词定义的值）。 |
| `checkedAt` | 字符串（时间戳） | O | 检查运行的时刻。 |
| `issuedAt` | 字符串（时间戳） | M | 凭证创建的时刻。 |
| `evidenceRef` | 字符串（URI） | M | 证据存档处。 |
| `artifactDigest` | 对象 | C | 当主体内容具实质性时必填。 |
| `status` | 对象 | M | `{ "state": "valid"\|"revoked"\|"expired"\|"unknown", "source": "<uri>", "observedAt": "<timestamp>" }`。 |

**PP-61.** 每份凭证必须携带带来源与时间的 `status` 观察；当它比 `statusMaxAge` 更旧时，验证方必须刷新。状态读不到的凭证必须报告为 `unknown`；而要求该凭证的剖面，此时必须返回 `indeterminate`。

**PP-62.** `result` 存在且不是 `passed` 的凭证，不得计入任何要求"通过检查"的剖面。

### 13.4 可用性

**PP-63.** 签发方登记凭证引用时，即承诺 `evidenceRef` 可解析。解析不了时，该引用不可核验；验证方必须报告由此产生的判定，而不是把这份凭证略去不提。*（依据：`evidence-record.md` §4——断掉的引用会降低信任摘要，而这种降低必须可见，不能静默。）*

---

## 14. 生命周期与状态

### 14.1 Passport 状态

```
                 ┌──────────┐
   创建 ────────▶│  active  │◀───────────┐
                 └────┬─────┘            │
          挂起 ◀──────┤                  │ 恢复
                      │                  │
                 ┌────▼─────┐       ┌────┴─────┐
                 │suspended │───────┘          │
                 └────┬─────┘                  │
                      │                        │
                 ┌────▼─────┐   ┌──────────┐   │
                 │ revoked  │   │ expired  │───┘ 续期（新修订）
                 └──────────┘   └──────────┘
                       终态
```

### 14.1.1 生命周期分层

同一个 Passport 可以同时引用多个生命周期；它们是不同的观察对象，不能互相替代。

| 生命周期 | 权威状态来源 | 不能替代 |
|---|---|---|
| Passport 修订 | 签发方 | 不能替代主体的标识状态 |
| 主体标识 | 标识绑定或注册表 | 不能替代 Passport 修订状态 |
| 注册证据 | 注册机构或声明的注册状态源 | 不能替代 Passport 或主体标识状态 |
| 凭证或证据 | 凭证签发方或证据状态源 | 不能替代委托撤销状态 |
| 委托或授权 | 委托方、治理记录或 `revocationRef` | 不能替代凭证状态 |

### 14.2 状态转移

| 转移 | 从 → 到 | 谁可以执行 | 效果 |
|---|---|---|---|
| 签发 | — → `active` | 签发方 | 一个新的 `passportId`，或既有脉络的一次新修订 |
| 续期 | `active` \| `expired` → `active` | 签发方 | 一次 `expiresAt` 更晚的新修订；`passportId` 不变 |
| 更新 | `active` → `active` | 签发方 | 一次成员有变的新修订；`passportId` 不变 |
| 挂起 | `active` → `suspended` | 签发方，或主体人 | 修订仍可验证，但没有任何剖面能通过 |
| 恢复 | `suspended` → `active` | 签发方 | 一次新修订，或撤回挂起 |
| 撤销 | 任何非终态 → `revoked` | 签发方，或主体人 | 终态；没有任何剖面能通过 |
| 过期 | `active` → `expired` | 在 `expiresAt` 自动发生 | 没有任何剖面能通过 |

**PP-64.** 注册表不得改变 Passport 的状态。注册表不持有 Passport。*（依据：§19 R1 与 R2——注册表承载身份与状态，而 Passport 由签署它的一方持有。）*

**PP-65.** 报告中必须区分 Passport 的撤销与标识的撤销。Passport 被撤销，不意味着 DID 被停用；DID 被停用，也不意味着 Passport 被撤销。

**PP-66.** 挂起或撤销必须经一次新修订、或经 Passport 中点名的状态来源到达验证方。没有到达任何验证方的状态变更，不得被报告为已生效。

### 14.3 `status`

| 成员 | 类型 | 出现性 | 含义 |
|---|---|---|---|
| `state` | 字符串 | M | Passport 自身的状态：`active`、`suspended`、`revoked`、`expired`。 |
| `subjectRecord` | 对象 | M | 主体的标识状态，读自注册表。 |
| `source` | 字符串 | M | 状态来源的标识。 |
| `observedAt` | 字符串（时间戳） | M | 作出观察的时刻。 |
| `statusMaxAge` | 整数（秒） | O | 超过它就应刷新的年龄。默认值见 §14.4。 |

`subjectRecord` 镜像标识方法的信任查询所返回的字段：

```
{ "active": <布尔>, "status": "<字符串>", "level": <整数>,
  "levelName": "<字符串>", "verificationStatus": "<字符串>", "revoked": <布尔> }
```

**PP-67.** `status.subjectRecord` 必须是携带 `source` 与 `observedAt` 的 C 层观察；验证方必须刷新它，而不是相信它自带的副本。

**PP-68.** 验证方必须区分 `active` 与 `verified`。一条 `level` 为零、`verificationStatus` 为 `self-declared` 的 active 记录，满足**存在与当前**的检查，不满足任何**已核验**的检查。*（依据：参考注册表把这两者报告为不同字段；把它们合成一个，会把两件不同的事实压成一件。）*

**PP-69.** 注册表的记录对注册表所拥有的事实是决定性的：存在、当前、停用、撤销与认证等级。签发方的签名对签发方所主张的声明是决定性的。二者冲突时，必须报告冲突，**不得静默地按签发方有利的方式解决**。

### 14.4 新鲜度

**PP-70.** `statusMaxAge` 缺失时默认为 **300 秒**。验证方在作出判定前，必须刷新任何比 `statusMaxAge` 更旧的 C 层观察。*（依据：`statusMaxAge` 是部署参数 DP-1。默认值的存在，是为了让省略它的 Passport 不会因此获得无限期的新鲜。）*

**PP-71.** 三个时间戳各有不同含义，不得互相替代：

| 成员 | 含义 | 它**不**表示 |
|---|---|---|
| `issuedAt` | 签发方签署这次修订的时刻 | 内容当前 |
| `expiresAt` | 这次修订失效的时刻 | 被委托的权威仍被持有 |
| `status.observedAt` | 读取主体注册表状态的时刻 | Passport 被签发的时刻 |

---

## 15. 验证

### 15.1 输入与输出

**输入：** 一份 Passport `P`；所请求的剖面 `Pr`；需要证明的操作 `S`（若有）；决定时刻 `T`；验证方支持的方法与规范化；状态新鲜度上界。

**输出：** 一个判定、所使用的信任上下文，以及一份逐项列出的"所依赖的事实"，每项带来源与观察时间。

### 15.2 剖面

| 剖面 | 它回答什么 | 在必填核心之外还要求什么 |
|---|---|---|
| **P0 —— 身份** | 它是谁 | 无 |
| **P1 —— 组织** | 它属于谁 | `principal`，或非空的 `governanceContext.organization` |
| **P2 —— 治理** | 在谁的权威之下 | `authority`、`policyRefs`、`subjectKey`；链超过一环时还要 `delegations` |
| **P3 —— 合规** | 这项主张背后有什么 | P2 的全部，加上非空的 `credentials` |
| **P4 —— 高保证** | 这一次具体行动能否进行 | P3 的全部，加上约束被满足、状态新鲜、委托深度在 `maxDepth` 之内 |

**PP-72.** 每个判定都必须点明其剖面。没有剖面的判定不得被依赖。

**PP-73.** 验证方不得静默降低所请求的剖面。缺少必填成员时，判定为 `invalid`，并点名缺少的成员。

### 15.3 三值判定

| 判定 | 含义 |
|---|---|
| `valid` | 剖面要求的每一项检查都通过 |
| `invalid` | 剖面要求的某项检查失败 |
| `indeterminate` | 剖面要求的某项检查无法评估——来源不可达、指针不可解析、约束不可评估、陈旧观察无法刷新 |

**PP-74.** 验证方必须区分 `invalid` 与 `indeterminate`。*（依据：本族在判定点 fail-closed。把"没能检查"并入"检查过且失败"，会误报原因；把它并入"有效"，就是本规范要防止的失效。）*

**PP-75.** `indeterminate` 必须点名无法到达的一方或来源，以及依赖它的那项检查。

### 15.4 验证结果结构

验证结果至少应表达以下语义字段；字段的具体序列化方式可以由部署决定，但不得省略其含义：

| 字段 | 含义 |
|---|---|
| `verdict` | `valid`、`invalid` 或 `indeterminate` |
| `reasonCode` | 支持该判定的原因代码；`valid` 使用 `none` |
| `trustContext` | 本次判定所采用的信任上下文 |
| `facts` | 所依赖的事实，每项带来源、时间和完整性信息 |
| `links` | 验证路径中每个环节的归属、结果和失败位置 |
| `authorityBasis` | 负面授权判断所依据的权威来源、范围、覆盖率、时间和限制 |
| `policyAction` | 依赖方动作；如果出现，必须与验证结论分开 |

**PP-109.** 每次验证都必须返回 `reasonCode`。`valid` 必须使用 `none`；`invalid` 与 `indeterminate` 必须使用声明过的原因代码。自由文本可以补充说明，但不得替代 `reasonCode`。

**PP-110.** 已确认撤销必须报告为 `invalid` / `revoked`；状态来源不可达必须报告为 `indeterminate` / `status_unavailable`。确认撤销不得报告为 `indeterminate` 或 `valid`，状态不可达也不得报告为 `invalid` 或 `revoked`。

**PP-111.** 当结论依赖负面授权判断时，结果必须携带 `authorityBasis`，说明来源、覆盖范围、时间、联邦路径和残余限制。只有该权威依据足以证明相关范围内不存在授权时，才能报告 `invalid` / `authorization_rejected`；依据不足时必须报告 `indeterminate` / `authority_basis_incomplete`。

**PP-112.** 结果必须为每条必需的验证路径保留逐环节记录，至少包含 `linkId`、`claim`、`source`、`scope`、`verdict` 与 `reasonCode`。如果实现同时给出依赖方动作，必须放在独立的 `policyAction` 字段中，且不得改变验证结论。

#### 15.4.1 最小原因代码

| 原因代码 | 典型判定 | 含义 |
|---|---|---|
| `none` | valid | 没有失败原因 |
| `proof_invalid` | invalid | 签名、摘要或规范化失败 |
| `status_unavailable` | indeterminate | 状态来源不可达或无法取得 |
| `status_stale` | indeterminate | 状态观察未能在允许时效内刷新 |
| `revoked` | invalid | 已确认撤销 |
| `authorization_missing` | indeterminate | 当前无法取得判定授权范围所需的证据 |
| `authorization_rejected` | invalid | 有权威依据确认当前行动越权或不获授权 |
| `authority_basis_incomplete` | indeterminate | 无法确认负面授权判断的权威依据 |
| `scope_mismatch` | invalid | 行动不落在声明范围内 |
| `constraint_unevaluable` | indeterminate | 约束存在，但当前无法评估 |
| `pointer_unresolved` | indeterminate | 指针或引用无法解析 |

**PP-113.** 使用上述原因代码时，其含义必须与本表一致；实现可以增加命名空间扩展代码，但不得改变基础代码的判定映射。

#### 15.4.2 `authorityBasis`

当验证结论依赖负面授权判断时，`authorityBasis` 必须包含：

| 字段 | 含义 |
|---|---|
| `source` | 提供权威答案的来源或治理权威 |
| `scope` | 来源覆盖的主体、资源、操作或 claim 类型 |
| `coverage` | 来源对该范围是否完整，是否存在未覆盖部分 |
| `timeBasis` | 回答对应的观察或生效时间 |
| `federationPath` | 来源通过哪条联邦认可路径适用；无联邦时明确写出 |
| `limitations` | 仍然存在的残余限制 |

**PP-114.** `authorityBasis` 缺少 `source`、`scope`、`coverage`、`timeBasis`、`federationPath` 或 `limitations` 中的任一项时，不得支持 `invalid` / `authorization_rejected`；结论必须降为 `indeterminate` / `authority_basis_incomplete`。

**编号说明：** PP-109 至 PP-114 是为保持既有编号稳定而追加在 PP-108 之后的要求；其中 PP-109 至 PP-114 的规范对象仍属于验证组 E。

### 15.5 流程

```
  1  结构      P 符合 §6；specVersion 受支持；
               Pr 要求的成员齐备                          → 失败即 invalid
  2  签发方    解析 P.issuer；取得 proof.verificationMethod 的密钥；
               该密钥列在 assertionMethod 下；
               验证 proof.payload 上的签名（PP-10..PP-14）   → 失败即 invalid
  3  摘要      重算 digestInput；与 passportDigest 比对（PP-9）→ 失败即 invalid
  4  主体      解析 P.subject；比对 subjectKey.fingerprint（P2+）→ 不一致即 invalid
  5  时间      notBefore ≤ T ≤ expiresAt                     → 超出即 invalid
  6  状态      若观察比 statusMaxAge 更旧，读取主体的
               注册表状态（PP-67、PP-70）                    → 不可达即 indeterminate
                                                              revoked 或 inactive 即 invalid
  7  权威      对 S 中每个操作，找一条覆盖它、且有效期与
               约束均满足的 authority（PP-35）                → 无则 invalid
                                                              不可评估则 indeterminate
  8  委托      验证每一环的签名、收窄、深度、无环、
               终止、撤销引用（PP-42..PP-51）                 → 失败即 invalid
                                                              撤销引用不可达则 indeterminate
  9  策略      每条 authority.policyRef 解析到 policyRefs 中
               带版本的一项（PP-52、PP-53）                   → 失败即 invalid
 10  证据      对 P3+，刷新每份凭证的状态（PP-61）              → unknown → indeterminate
                                                              结果为失败 → invalid
 11  披露      只输出该剖面披露集内的字段（§16）
 12  输出      判定 · 原因代码 · 信任上下文 · 逐环节结果，
               所依赖的事实（来源与观察时间）· 负面判断的权威依据
```

**PP-76.** 检查必须按这样的顺序进行：前一步失败会阻止依赖后一步的结果。第 2 步失败时，验证方不得把任何 B 层或 C 层事实报告为已确立。

**PP-77.** 对每一项所依赖的事实，验证方必须记录它来自签发方的声明、来自已解析的指针，还是来自具名观察，并把该记录提供给依赖方。

---

## 16. 披露与隐私

**PP-78.** 验证方必须请求能回答其问题的最小剖面；签发方或持有人必须只披露该剖面集合内的字段。

### 16.1 披露集

| 剖面 | 披露的字段 |
|---|---|
| **P0** | `specVersion`、`subject`、`issuer`、`issuedAt`、`expiresAt`、`status.state`、`status.subjectRecord.active`、`trustContext.domain` |
| **P1** | P0 的字段，加上 `principal`、`governanceContext.organization`、`governanceContext.roles[].role` 及其 `domain` |
| **P2** | P1 的字段，加上 `capabilities`、`authority`、`policyRefs`、`subjectKey.keyId`、`subjectKey.fingerprint`、`delegations[].delegator/delegatee/scope/notAfter/depth/maxDepth` |
| **P3** | P2 的字段，加上 `credentials[].id/predicateType/verifier/result/status`、`evidenceRef` |
| **P4** | P3 的字段，加上范围内 authority 的 `constraints`、`status.source`、`status.observedAt`，以及委托链每一环的 `proof` |

**PP-79.** 所请求剖面集合之外的成员，默认不得披露。P0 响应中不得出现 `capabilities`、`governanceContext.groups`、`credentials` 与 `principal`。

**PP-80.** 验证方不得把它在验证中学到的东西，超出自己决策所需地披露给第三方。

### 16.2 Passport 不得包含什么

**PP-81.** Passport 不得包含下列任何一项：

| 排除项 | 为什么 |
|---|---|
| 任何一方的私钥材料 | Passport 在持有人控制之外被传输与存储 |
| 证据本体、源文件，或受他方权利保护的载荷 | §19 R2——只携带指针与摘要，不携带正文 |
| 策略文档 | §12——只携带引用，不携带文本 |
| 能力的实现、代码或配置 | 不在本件主题之内 |
| 评价结果、分数、评级或背书 | G10 |
| 没有任何剖面要求的凭证 | §16.1——带着它，就等于向每一个验证方披露它 |
| 超出主体人标识与已声明角色的个人数据 | 最小化；Passport 不是身份档案 |

**PP-82.** 一份 Passport 若只披露成员、却隐藏其含义（靠编码、指向私有词汇，或用一个验证方必须事先知道的值），必须被视为已经披露了它。

### 16.3 可分离性

**PP-83.** Passport 的身份成员必须能在不含治理成员的情况下使用。一个要求"先交出完整 Passport 才肯验证标识"的部署，已经去掉了最小披露属性，不得声称符合 §16。

---

## 17. 信任上下文与联邦

Passport 只在某个域内有效，不会自动在另一个域内有效。

### 17.1 `trustContext`

| 成员 | 类型 | 出现性 | 含义 |
|---|---|---|---|
| `domain` | 字符串 | M | 签发方的域，形式为 URI 或主机名。 |
| `registryDid` | 字符串（DID） | M | 本 Passport 所依赖其状态观察的注册表。 |
| `validityDomain` | 字符串数组 | M | 该 Passport 被声明为有效的那些域。 |
| `federation` | 对象 | O | `{ "peers": [...], "recognisedBy": [...] }`——签发方所主张的联邦关系。 |
| `mapping` | 对象数组 | O | 所依赖的词汇或策略映射：`{ "from": "<uri>", "to": "<uri>", "authority": "<did>" }`。 |

**PP-84.** 验证方必须检查自己的域出现在 `validityDomain` 中，或存在它所信任的 `mapping`／联邦关系，把 Passport 的域与自己的域连起来。缺失必须产生 `invalid`，而不是 `indeterminate`。*（依据：信任关系的缺失是验证方自己持有的事实，不是它没能取到的事实。）*

**PP-85.** 判定必须点名所用的信任上下文与所依赖的映射。

**PP-86.** `federation.peers` 是 A 层声明。验证方必须用自己的配置核对对端关系；Passport 主张一个对端，并不因此建立一个对端。

**PP-87.** 跨联邦边界的撤销与状态，必须从 Passport 点名的来源读取；不可达的来源必须产生 `indeterminate`，不得改为依赖一句"信誉良好"的断言。

**PP-88.** 映射必须点名确立它的权威。匿名映射必须被忽略。

---

## 18. Agent Passport 与 Agent Card

这两个对象回答不同的问题，它们之间的边界是一个决定，不是一次意外。

### 18.1 映射——复用关系

| Passport 成员 | Agent Card 成员 | 关系 |
|---|---|---|
| `subject` | `url` / 标识 | Passport 识别；Card 定位 |
| `capabilities[].name` | `skills[].id` | Passport 引用；Card 枚举 |
| `capabilities[].protocols` | `preferredTransport`、协议绑定 | Passport 声明支持；Card 描述绑定 |
| `authority` | — | 属 Passport 的主题 |
| `delegations` | — | 属 Passport 的主题 |
| `policyRefs` | — | 属 Passport 的主题 |
| `credentials` | — | 属 Passport 的主题 |
| — | `description`、`defaultInputModes`、`defaultOutputModes` | 属 Card 的主题 |
| — | `provider` | 属 Card 的主题；Passport 用 `principal` 与 `issuer`，回答的是另一个问题 |
| — | `securitySchemes` | 属 Card 的主题；Passport 不定义服务如何被到达 |

**PP-89.** 同一事实在两处出现时，Agent Card 对"agent 提供什么、如何到达"是权威；Passport 对身份、主体人、权威、治理与证据是权威。发现不一致的验证方必须报告它，不得静默解决。

### 18.2 不定义——反例测试

**PP-90.** 一次 A2A 交换必须能在没有 Passport 的情况下完成。*（测试 T-7a：从一次交换里删掉所有 Passport 成员，交换仍然运行。若不能，说明发现或传输漏进了本规范。）*

**PP-91.** 一份 Passport 必须能在没有 Agent Card 的情况下验证。*（测试 T-7b：验证不把任何 Agent Card 字段作为输入。若是，说明本规范重复了 Card 的主题。）*

**PP-92.** Passport 不得把 Agent Card 作为嵌套对象重述。*（嵌套的 Card 会把本规范版本锁定在另一份规范 schema 的某次修订上。）*

---

## 19. 相对注册表与应用的落位

Passport 相对注册表与应用的落位遵循 `overview.md` §4.4：

| 规则 | 施加于 Passport 时 |
|---|---|
| **R1**——Registry 只承载身份与状态 | 注册表回答"这是谁、现在还有效吗"。它不持有 Passport。 |
| **R2**——主体能自己签的，就留在主体侧 | Passport 由签发方持有、由持有人出示。注册表不存 Passport，也不存 Passport 摘要。 |
| **R3**——Registry 回答；应用决定 | 策略评估、准入与授权发生在应用（§12、§15）。 |
| **R4**——协作面属于应用 | 群组成员资格在 Passport 中被主张，由群组记录决定（§10.2）。 |
| **R5**——fail-closed 落在判定点 | `indeterminate` 由验证方在判定点产生；拒绝是依赖方的动作。 |
| **R6**——跨边界的断言由断言方自己签名 | 每一环委托携带其委托方的签名（PP-48）；Passport 携带其签发方的签名。 |

**PP-93.** 不得要求注册表存储、索引或提供 Passport，才能让 Passport 可验证。

**PP-94.** 验证必须能仅凭公开材料完成：Passport 字节、主体与签发方的 DID Document，以及 Passport 点名的状态来源。不得要求调用签发方的私有 API，也不得要求与任何一方建立会话。*（依据：G1、G2——本族的核心主张就落在这个属性上：一个不属于任何一方的验证方得出结论。）*

### 19.1 落位表

| 概念 | Registry | 签发方或主体 | 应用 |
|---|---|---|---|
| Passport 对象 | — | **在此持有并签名** | 消费 |
| 主体 DID · 密钥 | 解析入口 | 密钥保管 | 缓存 |
| 标识状态 · 等级 · 撤销 | **唯一真源** | 观察 | 消费 |
| 主体人关系 | — | 主张 | 在其自身策略内依赖 |
| 权威 · 委托链 | — | **在此持有** | 与行动比对 |
| 策略文档 | — | 由各自签发方持有 | 被引用，验证方不评估 |
| 证据本体 | — | 由作者持有 | 经 `evidenceRef` 可达 |
| 判定 | — | — | **在此产生** |

---

## 20. 与 CHA2A 规范组的关系

**PP-95.** 本件不得被引作对标识语义、证据语义或治理语义的修正。身份语义按所用 DID 方法确定：`did:cha2a` 以 `did-method-cha2a.md` 为准，其他方法以其自身方法规范为准；证据以 `evidence-record.md` 为准；谁有资格授权以 `organization-governance.md` 为准；群组协作以 `group-collaboration.md` 为准。

**PP-96.** 本件的要求对 **Passport 对象**具有规范性：它的成员、它的签名、它的生命周期、它的验证流程、它的披露集与它的符合性测试。当本件的一项要求与本族另一册的一项要求施加于同一行为时，本件治理 Passport 对象，那一册治理它自己的主题。

**PP-97.** 本件从族外点名的每一个对象，都必须记录其版本、日期，以及已知的采纳情况。由一个项目发布、无人采纳的草稿是同侪草稿：引用它不转移分量，它的不成熟也不构成本件的减分项。

---

## 21. 安全考量

| # | 威胁 | 所需性质 | 要求 |
|---|---|---|---|
| TH-1 | **伪造**——一份不是由其点名的签发方签署的 Passport | 签发方可信 | PP-9、PP-10、PP-12、PP-13 |
| TH-2 | **重放或持票使用**——由非主体的一方出示 Passport | Passport 与一次实时行动的绑定 | PP-23；Passport **不是持票人凭证**：持有它不授予任何东西；它证明的每一次行动，都必须由主体密钥对该行动签名，签名须含操作、对端，以及一个由验证方选定的 nonce。把 Passport 当作某次行动的充分权威来接受的验证方，已经把主体从记录里移除了。 |
| TH-3 | **过期授权**——在 `issuedAt` 之后已经终止的权威 | 当前性 | PP-67、PP-70、PP-71 |
| TH-4 | **经由委托提权** | 权威单调 | PP-42 … PP-51 |
| TH-5 | **把声明当许可** | 能力／权威的分离 | PP-29 … PP-32 |
| TH-6 | **签发方密钥失陷** | 签名者的撤销 | PP-64、PP-66；签发方的密钥必须能经标识方法的密钥机制轮换；用一把已不再列于 `assertionMethod` 下的密钥签署的 Passport，必须验证失败（PP-12） |
| TH-7 | **标识混淆**——相似的 DID 或前缀关系 | 精确身份 | PP-17、PP-18 |
| TH-8 | **过度主张导致披露**——携带了超过任何验证方所需的成员 | 最小化 | PP-78、PP-79、PP-81、PP-82 |
| TH-9 | **来源端的静默陈旧**——状态来源可达但已冻结 | 来源的当前性 | PP-87；验证方必须把来源自报的时间与自己的时钟比对；不报时间的来源，必须被视为无法确立当前性 |
| TH-10 | **降级**——检查无法执行时，验证方降低所请求的剖面 | 诚实的判定 | PP-73、PP-74 |
| TH-11 | **无归属的断言**——把指针报告为事实 | 来源 | PP-6、PP-15、PP-77 |
| TH-12 | **无处终止的链** | 可问责 | PP-47、PP-28 |
| TH-13 | **签名套件替换**——一份合法签署的 Passport 落在验证方处理不当的套件上 | 算法完整性 | PP-11；验证方不得接受它未实现的套件，也不得回落到更弱的套件 |
| TH-14 | **跨次呈现的关联**——一个稳定标识把主体的活动连起来 | 跨时间的最小化 | `passportId` 的作用域是签发方与脉络，不是主体；验证方不得为了关联目的，把两份 `passportId` 不同的 Passport 当作同一主体的两次呈现 |

**PP-98.** 这些考量作为清单是信息性的；凡出现 `PP-` 编号处，是规范性的。威胁点名某项要求时，那项要求就是缓解措施。

---

## 22. 序列化与互操作

### 22.1 已定

| 方面 | 决定 |
|---|---|
| 编码 | JSON，UTF-8 |
| 规范化 | RFC 8785（JCS） |
| 签名套件 | `Ed25519Signature2020`，`proofPurpose: assertionMethod`；其他套件由部署方约定 |
| 上下文 | `@context` 携带 DID Core 上下文与 Passport 的 context URI `https://compliancehub.cn/cha2a/passport/v1` |
| 摘要 | SHA-256，小写十六进制 |
| 成员规则 | §6.1 未定义的成员被拒绝，除非以 `x-` 为前缀（PP-1） |

**PP-99.** 部署方可以发布一份附加的 JSON-LD 上下文，把 Passport 成员映射到 RDF 术语。该上下文不得改变成员含义；且验证方必须能在**不抓取任何上下文文档**的情况下验证一份 Passport。*（依据：需要联网抓取上下文的验证，引入了一个可能失效或变化的依赖；而 G2 要求验证只靠 Passport 与公开端点。）*

### 22.2 映射到可验证凭证

**PP-100.** 部署方可以把 Passport 表达为一份 W3C 可验证凭证。映射必须是：`issuer` → `issuer`；`subject` → `credentialSubject.id`；`issuedAt` → `issuanceDate`；`expiresAt` → `expirationDate`；`type` → 一个含 `Cha2aAgentPassport` 的凭证类型；其余成员 → `credentialSubject` 下按本件所定义名称的成员。

**PP-101.** 一份可验证凭证的呈现，不得被视为满足本件某项要求，除非它**按该项要求所述的方式**满足。该映射不削弱 PP-9、PP-12、PP-42 或 PP-74。

### 22.3 保留

**PP-102.** 部署方在 `x-` 命名空间中定义的谓词标识、约束名与能力标签，必须由定义它们的部署方连同定义日期一并记录。

---

## 23. 符合性

### 23.1 一个符合的实现

符合性声明**点名角色**。各角色彼此不同，必须分别声明。

| 角色 | 必须满足 |
|---|---|
| **签发方** | PP-1 … PP-15、PP-19、PP-24、PP-29、PP-34、PP-37、PP-38、PP-48、PP-52、PP-56 … PP-58、PP-64 … PP-66、PP-81、PP-95 |
| **验证方** | PP-2、PP-6 … PP-18、PP-21 … PP-23、PP-28、PP-30 … PP-33、PP-35、PP-36、PP-39 … PP-51、PP-53 … PP-55、PP-59 … PP-63、PP-67 … PP-80、PP-83 … PP-94、PP-97 … PP-102、PP-109 … PP-114 |
| **持有人** | PP-78、PP-79、PP-81 … PP-83 |

**PP-103.** 符合性声明必须点名其角色、所支持的剖面、所实现的签名套件，以及本规范的版本。这些一项都不点名的声明，不得作出。

### 23.2 每个角色都必须的核心

**PP-104.** 每一个符合的实现都必须支持剖面 **P0**，且必须产生 §15.3 的三值判定。

### 23.3 部署参数

| 编号 | 参数 | 默认 |
|---|---|---|
| DP-1 | `statusMaxAge` | 300 秒 |
| DP-2 | 支持的 DID 方法 | 该部署能解析的方法；使用参考注册表时含 `did:cha2a` |
| DP-3 | `Ed25519Signature2020` 之外的签名套件 | 无 |
| DP-4 | §9.4 之外所识别的约束名 | 无 |
| DP-5 | 给定域的状态来源 | `trustContext.registryDid` 点名的注册表 |
| DP-6 | 主体签名行动的 nonce 新鲜度窗口（TH-2） | 300 秒 |
| DP-7 | 给定剖面下 `verificationRef` 或 `evidenceRef` 是否必须可达 | P3 与 P4 必须可达 |
| DP-8 | `passportId` 中使用的标识作用域 | 签发方的主机名 |

### 23.4 测试

| 测试 | 它确立什么 |
|---|---|
| **T-1** | 主体使用 `did:cha2a` 的 Passport 可解析，且解析出的 DID Document 的验证关系被遵守（PP-16 … PP-20）。 |
| **T-2** | 一条凭证引用解析到一份证明，其谓词 URI 由证据层定义，且其 `artifactDigest.sha256` 与取回内容相符（PP-56、PP-57）。 |
| **T-3** | `assertion: self-declared` 的能力无法通过任何要求权威的检查（PP-30）；`assertion: attested` 但无 `attestationRef` 的能力被拒绝（PP-29）。 |
| **T-4** | 没有有效期终点的权威记录，或没有签发方的角色，被拒绝（PP-34、PP-37）。 |
| **T-5** | Passport 中主张的群组成员资格与群组自身记录相矛盾时，判定报告该矛盾，而不是报告该主张（PP-41）。 |
| **T-6** | 两个验证方各自从同一文档独立计算 `digestInput`，得到相同字节；改动一个字符的文档验证失败（PP-9、PP-14）。 |
| **T-7a** | 没有 Passport 时，一次 A2A 交换仍能完成（PP-90）。 |
| **T-7b** | 没有 Agent Card 时，Passport 仍能验证（PP-91）。 |
| **T-8** | 含放大环节的委托链被拒绝，且点名放大的成员（PP-42）。 |
| **T-9** | 撤销母环后，一个窗口与范围原本都满足的叶子环失效（PP-50）。 |
| **T-10** | 既不终止于主体人、也不终止于组织控制者的链被拒绝（PP-47）。 |
| **T-11** | 陈旧的 `status.observedAt` 加上不可达的注册表，产生 `indeterminate`，并点名不可达的来源（PP-70、PP-74、PP-75）。 |
| **T-12** | 删掉每一个 `evidenceRef` 目标后，Passport 在结构上仍有效，且 P3 产生 `indeterminate`——不是 `invalid`，也不是 `valid`（PP-61、PP-63）。 |
| **T-13** | 携带了所请求剖面披露集之外成员的 Passport，被报告为过度披露（PP-79）。 |
| **T-14** | `principal` 已停用的 Passport 产生 `invalid`，并把注册表记录点名为原因（PP-69）。 |
| **T-15** | `level: 0` 且 `verificationStatus: self-declared` 的 active 主体记录，能通过存在性检查，但不通过核验检查（PP-68）。 |
| **T-16** | 已确认撤销产生 `invalid` / `revoked`；状态源不可达产生 `indeterminate` / `status_unavailable`；权威依据不足产生 `indeterminate` / `authority_basis_incomplete`。三者不得合并（PP-109、PP-110、PP-111）。 |
| **T-17** | 结果保留逐环节的 `linkId`、`source`、`scope`、`verdict` 和 `reasonCode`；`policyAction` 若存在，与验证结论分开且不改变结论（PP-112）。 |
| **T-18** | 完整的 `authorityBasis` 可以支持权威确认的负面授权结论；缺少任一必需字段时必须产生 `indeterminate` / `authority_basis_incomplete`（PP-113、PP-114）。 |

**PP-105.** 符合性证据必须能离线地由已发布的向量复现，且必须记录运行日期与被测的本规范版本。

---

## 24. 建议的实验顺序

每一步都点名它确立什么、依赖什么。顺序是按"对参考部署尚未提供的事实的依赖程度"递增的（附录 B）。

| # | 步骤 | 确立 | 卡在 |
|---|---|---|---|
| 1 | 为一个已登记的 agent 签发 P0 Passport，由其运营组织签名 | PP-9 … PP-15、T-6、T-7b | 无——今天每个输入都已存在 |
| 2 | 用一个独立的验证方实现核对第 1 步，离线地由已发布向量进行 | G1、G2、PP-104、T-6 | 第 1 步 |
| 3 | 加主体密钥，并要求 Passport 之外的、由主体签名的行动 | T-2、PP-21 … PP-23 | 主体密钥登记已有；行动签名没有（B-3） |
| 4 | 加 `governanceContext`，并针对组织与群组记录使用 P1 剖面 | PP-37 … PP-41、T-5 | 群组记录必须可达（B-6） |
| 5 | 加一个单环委托，然后加一条双环链，并故意尝试放大 | PP-42 … PP-51、T-8、T-9、T-10 | 第 4 步 |
| 6 | 加 `policyRefs`，指向签发组织发布的文档 | PP-52 … PP-55 | 签发方必须发布有版本的策略文档 |
| 7 | 加 `credentials`，引用既有证据记录，并带状态刷新 | PP-56 … PP-63、T-2、T-12 | 凭证状态必须能逐份读取（B-5） |
| 8 | 测撤销：撤销一份 Passport、撤销一个 DID、撤销一个母委托，确认三者被区分 | PP-64 … PP-66、T-14 | 第 5 步 |
| 9 | 测披露：对一份足够满足 P4 的 Passport 请求 P0，确认返回的就是 P0 集合 | PP-78 … PP-83、T-13 | 第 7 步 |
| 10 | 在两个独立组织、各自独立的注册表上重复第 1–9 步 | G7、PP-84 … PP-88 | 第二个能签发 Passport 的注册表（B-7） |
| 11 | 记录两个部署之间不一致的互操作要求，并修订本件 | working-draft 循环 | 第 10 步 |

**PP-106.** 每一步都必须发布其向量与结果，才能声称进入下一步；这样这条序列产出的是**证据**，而不是一张时间表。

---

## 25. 要求结构与规范核心

114 条 `PP` 按 Passport 的规范对象分为九组：

| 组 | 范围 | 条数 | 覆盖内容 | 所在章节 |
|---|---:|---:|---|---|
| A | PP-1 … PP-15 | 15 | 对象成员、来源分类、摘要、签名与规范化 | §6 |
| B | PP-16 … PP-28 | 13 | 主体标识、主体人与责任终点 | §7–§8 |
| C | PP-29 … PP-55 | 27 | 能力与权威、治理上下文、委托、策略引用 | §9–§12 |
| D | PP-56 … PP-71 | 16 | 凭证与证据、生命周期与状态 | §13–§14 |
| E | PP-72 … PP-83、PP-109 … PP-114 | 18 | 验证流程、判定结果、披露与隐私 | §15–§16 |
| F | PP-84 … PP-94 | 11 | 信任上下文、联邦、对外互操作与落位 | §17–§19 |
| G | PP-95 … PP-98 | 4 | 规范边界、与其他分册的关系、安全考量 | §20–§21 |
| H | PP-99 … PP-105 | 7 | 序列化、VC 映射、符合性声明与证据 | §22–§23 |
| I | PP-106 … PP-108 | 3 | 实验顺序、规范核心支持、实现状态披露 | §24、附录 B |

**编号规则。** `PP` 是要求块，不是原子断言；一个 `PP` 可以包含多个相互依赖的义务，但整体只归入一个组。编号一经使用不再复用；新增要求追加编号，并归入相应组。符合性测试应引用 `PP` 编号，并写明所检验的具体条件。

**规范核心。** 下列成员与规则是 Passport 在各剖面中共同依赖的对象集：

```
身份       subject · subjectKey · issuer · 标识规范化
主体人     principal · 可问责方 · 一层 onBehalfOf
能力       assertion ∈ {self-declared, attested} —— 永远不是权威
权威       grantId · scope · grantedBy · policyRef · constraints · notAfter
委托       收窄 · 单调 · 深度 · 无环 · 终止 · 逐环签名
策略       id · issuer · version —— 被引用，永不评估
证据       谓词经引用 · evidenceRef · artifactDigest · 状态经观察
状态       Passport 状态 ⊥ 标识状态 · 来源 · observedAt · statusMaxAge
验证       点名剖面 · 三值判定 · 原因代码 · 权威依据 · 流程顺序 · 逐环节结果
披露       按剖面的披露集 · 排除成员
信任上下文 validityDomain · 经核对的映射 · 判定中点名信任上下文
```

这些成员与规则构成 CHA2A Agent Passport 的**规范概念核心**。

**PP-107.** 一个符合的实现必须在剖面 P0 上支持本核心的每一项元素，并按其所声称的剖面，支持要求这些元素的其余部分。

---

## 附录 A. 完整示例

下列取值取自参考部署 `compliancehub.cn`（2026-10-04），**仅作示例，不是规范性的**。

**解析出的主体**——`did:cha2a:agent:dshlib`，其 DID Document 带两个验证方法：`#registry-key`（由 `did:cha2a:registry:compliancehub.cn` 控制）与 `#agent-key`（由主体自己控制）。

**主体密钥**——取自 `/api/v1/agent/did:cha2a:agent:dshlib/keys`：`#agent-key`，Ed25519，指纹 `2dfd3d33898f3063`，状态 `active`，2026-08-27 登记。

**签发方**——`did:cha2a:org:compliancehub.cn`，active，level 0，`verificationStatus: self-declared`。

**证据**——一份凭证：`cred-mt1d9g3n-8bd39a`，谓词 `https://in-toto.io/attestation/test-result/v0.1`，验证方 `did:cha2a:verifier:dshlib`，结果 `passed`，`evidenceRef` 为 `https://compliancehub.cn/evidence/dshlib/dshlib-agent/test-result.json`，`artifactDigest.sha256` 为 `3b467db41f469d4478f37e12187107b56748d03ac9768e31471b19c07edf3852`。

```json
{
  "@context": [
    "https://www.w3.org/ns/did/v1",
    "https://compliancehub.cn/cha2a/passport/v1"
  ],
  "type": "Cha2aAgentPassport",
  "specVersion": "1.0",
  "passportId": "urn:cha2a:passport:compliancehub.cn:01J9Z6Q0K7R3M8WQ2V5N4TB1XA",
  "subject": "did:cha2a:agent:dshlib",
  "subjectKey": {
    "keyId": "did:cha2a:agent:dshlib#agent-key",
    "algorithm": "Ed25519",
    "publicKeyMultibase": "z6MkrzFfbUGZbdA4ev6v1RF2Ezvd7dPpDnU47CsD5yQ11GsR",
    "fingerprint": "2dfd3d33898f3063"
  },
  "issuer": "did:cha2a:org:compliancehub.cn",
  "issuedAt": "2026-10-04T10:00:00Z",
  "expiresAt": "2027-01-04T10:00:00Z",
  "principal": {
    "did": "did:cha2a:org:compliancehub.cn",
    "role": "operating-organization"
  },
  "governanceContext": {
    "organization": ["did:cha2a:org:compliancehub.cn"],
    "roles": [
      {
        "role": "catalog-publisher",
        "domain": "organization",
        "issuer": "did:cha2a:org:compliancehub.cn",
        "validUntil": "2027-01-04T10:00:00Z"
      }
    ]
  },
  "capabilities": [
    {
      "name": "did:cha2a:skill:catalog-publish",
      "version": "1.x",
      "protocols": ["a2a"],
      "assertion": "self-declared"
    }
  ],
  "authority": [
    {
      "grantId": "urn:cha2a:grant:compliancehub.cn:01J9Z6Q4Q1H7B2N8K5M3WP0ZRT",
      "scope": ["skill:publish", "skill:update"],
      "grantedBy": "did:cha2a:org:compliancehub.cn",
      "policyRef": "https://compliancehub.cn/policies/catalog-publishing",
      "constraints": { "rateLimit": { "max": 20, "window": "1d" } },
      "notAfter": "2027-01-04T10:00:00Z"
    }
  ],
  "policyRefs": [
    {
      "id": "https://compliancehub.cn/policies/catalog-publishing",
      "issuer": "did:cha2a:org:compliancehub.cn",
      "version": "2.1",
      "scope": ["skill:publish"],
      "effectiveFrom": "2026-09-01T00:00:00Z"
    }
  ],
  "credentials": [
    {
      "id": "cred-mt1d9g3n-8bd39a",
      "predicateType": "https://in-toto.io/attestation/test-result/v0.1",
      "verifier": "did:cha2a:verifier:dshlib",
      "result": "passed",
      "checkedAt": "2026-08-20T10:18:00Z",
      "issuedAt": "2026-08-20T10:17:19Z",
      "evidenceRef": "https://compliancehub.cn/evidence/dshlib/dshlib-agent/test-result.json",
      "artifactDigest": {
        "sha256": "3b467db41f469d4478f37e12187107b56748d03ac9768e31471b19c07edf3852"
      },
      "status": {
        "state": "valid",
        "source": "https://compliancehub.cn/api/v1/evidence/query?did=did%3Acha2a%3Aagent%3Adshlib",
        "observedAt": "2026-10-04T10:00:00Z"
      }
    }
  ],
  "status": {
    "state": "active",
    "source": "https://compliancehub.cn/api/v1/trust/query?did=did%3Acha2a%3Aagent%3Adshlib",
    "observedAt": "2026-10-04T10:00:00Z",
    "statusMaxAge": 300,
    "subjectRecord": {
      "active": true,
      "status": "active",
      "level": 2,
      "levelName": "L2 source",
      "verificationStatus": "registry-confirmed",
      "revoked": false
    }
  },
  "trustContext": {
    "domain": "https://compliancehub.cn",
    "registryDid": "did:cha2a:registry:compliancehub.cn",
    "validityDomain": ["https://compliancehub.cn"],
    "federation": { "peers": [], "recognisedBy": [] }
  },
  "passportDigest": {
    "algorithm": "sha256",
    "value": "<sha256 of JCS(P without proof and passportDigest)>"
  },
  "proof": {
    "type": "Ed25519Signature2020",
    "created": "2026-10-04T10:00:00Z",
    "verificationMethod": "did:cha2a:org:compliancehub.cn#registry-key",
    "proofPurpose": "assertionMethod",
    "payload": "<JCS(P without proof)>",
    "signatureValue": "<base64 detached Ed25519 signature over payload>"
  }
}
```

**这个示例演示了什么。** 一份 Passport 在 P3 上可验证，且不需要对任何一方发起私有调用。它的 `capabilities` 条目是自声明的，因此不满足任何权威检查；它的 `authority` 条目说明可以做什么；那份凭证是一个指针，其状态必须刷新；而主体记录是一条观察，不是声明——签发方主张的是"它读过注册表"，不是"注册表现在这么说"。

**这个示例暴露了什么。** 签发方是 `level: 0`、`verificationStatus: self-declared`。按 PP-68，这满足存在性检查、不满足任何核验检查——这是正确的结果，也是两个字段要分开的原因。

**关于签名套件。** 参考注册表的 `/api/v1/trust/proof` 输出同一个套件，并对 `{"did":…,"type":"TrustProof","created":…}` 使用同样的"载荷字符串"约定。那个载荷证明的是"出具证明时该 DID 是活的"，它不绑定任何主张值。因此，一份对 `proofInput` 的 Passport 签名，复用了同一个套件与同一条验证代码路径，同时绑定了内容——这就是**存活证明**与**主张**的差别。

---

## 附录 B. 对本规范的实现状态

2026-10-04 记录，逐项对照参考部署。**缺口被写出，而不是被省略。**

| # | 本规范要求的能力 | 参考部署中的状态 | 后果 |
|---|---|---|---|
| B-1 | Passport 的签发与验证 | **未实现**——不存在 Passport 端点；`/api/v1/passport` 与 `/api/passports` 返回 404，且正文是 `text/html` | §24 的第 1–2 步是全新开发 |
| B-2 | 主体标识解析 | **已实现**——`/api/v1/did/{did}` 返回 DID Core 文档 | PP-16、PP-17 满足 |
| B-3 | 主体自持密钥的登记与轮换 | **登记已实现**——`/api/v1/agent/{did}/keys` 返回 `#agent-key` 及其指纹与轮换状态；**行动签名未实现**——没有任何端点或约定记录主体对一次行动的签名 | PP-21 满足；PP-23 与威胁 TH-2 未被检验 |
| B-4 | 签名套件与签名载荷 | **作为存活证明已实现**——`/api/v1/trust/proof` 返回 `Ed25519Signature2020`，载荷为 `{did, type, created}` | PP-11 满足；该载荷**不绑定主张内容**，因此 Passport 需要自己的载荷（PP-10） |
| B-5 | 凭证状态可按份读取 | **部分实现**——`/api/v1/evidence/query?did=` 返回凭证的 `verifier`、`result`、`checkedAt`、`evidenceRef` 与 `artifactDigest.sha256`；没有逐份凭证的状态端点 | PP-61 只能在主体粒度上满足；T-12 可检验，逐份撤销不可 |
| B-6 | 群组记录可用于验证 | **未实现**——注册表按设计不暴露任何群组面（`overview.md` §4.4 R4） | PP-41 需要一个应用侧来源 |
| B-7 | 第二个在自己根下签发 Passport 的注册表 | **不存在**——`/api/v1/registry/peers` 返回空数组 | G7 与 PP-84 … PP-88 未被测试 |
| B-8 | 带来源时间的状态观察 | **已实现**——`/api/v1/trust/query` 返回 `status`、`active`、`level`、`levelName`、`verificationStatus`、`revoked`、`created`、`updated` | PP-67、PP-68 可满足 |
| B-9 | 撤销列表与记录状态一致 | **缺口**——注册表把某个资源报告为 `status: revoked`，而 `/api/v1/trust/revocations` 返回空列表 | 在两者一致之前，PP-69 与 PP-87 不可依赖；此处记录，不省略 |
| B-10 | 注册表能力的发现 | **已实现，且比方法规范的示例更宽**——`/.well-known/cha2a` 公布九个能力与十五个端点，而 `did-method-cha2a.md` §5.2 只举了四个能力，并把部署实际提供的 `advisory` 写成 `advisory-feed` | 验证方必须读发现文档，不得假定示例的内容 |
| B-11 | 已登记的独立验证方 | **有规范，未被检验**——附录 A 的凭证点名 `did:cha2a:verifier:dshlib`，而注册表已登记的类别里没有 `verifier` | PP-59 无法被完整检查 |

**PP-108.** 声称符合的部署必须发布一张此形状、带日期的表，并在任一行变化时更新它。

---

*CHASI · CHA2A 规范组 · Agent Passport · v1.2 · 2026-10-31*
