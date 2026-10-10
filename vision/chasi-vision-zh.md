# CHASI Vision

**Compliance Hub for Agent Society Infrastructure**

---

CHASI

Vision & Research Architecture · 人与 Agent 和谐共存的 Agent Society
v1.4 · 2026-10

## 1. Vision：一个人与 Agent 和谐共存的社会
我们正在进入一个新的互联网阶段：Internet 不再只是 People-to-People、People-to-Machine 的网络，而逐步成为 People、Organizations 与 Agents 共同参与的网络。未来的 Agent 不只是软件工具，也可能成为个人助手、组织成员、商业伙伴、研究伙伴乃至社会协作者。
CHASI 的长期 Vision，不是建立一个由 Agent 主导的世界，也不是把 Agent 纳入一个过度中心化的监管体系，而是构想一种能够让 Human、Agent 和 Organization 在共同规则之下长期共存、互信、协作和创造价值的社会基础设施。
Human  ↔  Agent  ↔  Organization
        ↕
Identity · Trust · Authority · Rules
        ↕
Governance · Evidence · Accountability
可以把它理解为一个“Agent Society 的理想国”：不是乌托邦式的绝对自由，也不是中心化控制，而是在明确的身份、权利、责任、边界和共同规则基础上形成可持续的社会秩序。

## 2. CHASI 的定位
CHASI = Compliance Hub for Agent Society Infrastructure。

**一处术语区分。** CHASI 末三字母取自 **Agent Society Infrastructure（ASI）**——**Society 是名词**，指“智能体社会”。而 **SI** 是同一词根的研究用法，写作 **Social Infrastructure**——**Social 是形容词**，指这类基础设施的**社会性质**；它另有一解 **Super Intelligence**。两者**同指一类基础设施，只是视角不同**：ASI 是**主体视角**（为谁而建），SI 是**性质视角**（它是什么性质）。**ASSI（Agent Society Social Infrastructure）**是把两个视角写全的形式，不是第三个缩写。

CHASI 不是另一个 Agent Protocol，也不是一个监管机构。它是一个开放的 Compliance & Governance Hub，为不同 Agent Runtime、Agent Protocol、Identity System、Organization 和 Agent Society 提供互操作的合规与治理基础设施。
CHASI is not another Agent protocol.
It is a compliance and governance hub for interoperable Agent Societies.
因此，“Hub”比“Center”更加准确：CHASI 的职责是连接、协调、验证、记录和赋能，而不是取代已有生态。

## 3. 从 Agent Internet 到 Agent Society
Internet
   ↓
Agent Internet
   ↓
Agent Organizations
   ↓
Agent Societies
   ↓
Human + Agent Society
Agent Internet 解决的是“Agent 如何连接”；Agent Society 进一步解决“Agent 如何共同生活与协作”。当 Agent 具备身份、记忆、角色、关系、授权和经济行为之后，社会问题就会自然出现：信任、权利、责任、规范、治理、争议和公共利益。

## 4. 理想状态：Human-Agent Coexistence
CHASI 所追求的理想状态不是“Agent 像人”，而是 Agent 与人之间形成清晰、稳定、可验证的社会契约。
人拥有最终的主体性与价值判断权。
Agent 拥有与其职责相匹配的行动能力。
Agent 的能力与权限可以被明确描述。
Agent 的授权必须可验证、可限制、可撤销。
Agent 的行动能够留下可验证的证据。
组织能够管理自己的 Agent，而不必依赖单一中心平台。
不同组织的 Agent 可以在共同规则下进行跨域协作。
出现争议时能够回答：谁授权、谁行动、依据什么规则、产生什么结果、由谁负责。

## 5. CHASI 的核心原则
Compatibility：尽量复用已有协议和标准，而不是重新发明整个 Agent Internet。
Complementarity：专注补足现有生态在跨组织身份、授权、治理、证据和问责方面的空白。
Independence：保持 CHA2A / CHASI 的架构独立性，不依附于单一厂商或单一 Agent Runtime。
Openness：允许不同协议、不同 Runtime、不同 Identity System 接入。
Human Agency：保证人的主体性、知情权、授权权和撤销权。
Accountability：Agent 的自主行动必须能够形成可验证的责任链。
Federation：不同组织可以拥有自己的治理规则，同时实现有限、可控的互操作。
Privacy：合规不等于无限监控；Evidence 应遵循最小必要披露原则。

## 6. CHASI Architecture
                    Human
                      │
              Consent / Authority
                      ↓
Organization ──── CHASI Hub ──── Organization
     │                │                │
     ↓                ↓                ↓
   Agents        Policy / Trust      Agents
     │                │                │
     └────── Federation / A2A ────────┘
                      │
             Evidence / Audit
                      │
              Accountability

**架构分五层，每层回答一个问题。**

| 层 | 回答的问题 |
|---|---|
| 主体层 | 谁在场：Human · Organization · Agent · Group |
| 身份与信任层 | 它是谁；现在还信不信得过 |
| 治理层 | 谁有权、按什么规则、可以委托给谁 |
| 证据层 | 凭什么说这件事发生过、是谁的责任 |
| 互联层 | 与既有的协议、Runtime、身份体系如何组合 |

**依赖方向是单向的：上层不向下层提出要求。** 治理层不规定身份层必须用哪种密码学；证据层不规定治理层必须用哪种组织形态。这条规则的作用是让**每一层都可以被替换**——族内 `governance-architecture` 自陈“不陈述任何要求”，同一条道理。

**CHASI 不拥有什么。** 这一节比上面那张图更重要：

- 不定义通信原语——A2A、MCP 已有；
- 不定义密码学原语，也不定义 DID 方法本身——DID、VC 已有；
- 不做 Agent Runtime、不做模型、不做工作流引擎；
- 不做监管机构，也不做仲裁的最终执行者。

CHASI 的领域只有一处：**跨主体、跨域的那一段**。域内的事归域内——一家组织内部怎么分工、怎么审计自己，不该由 CHASI 规定；CHASI 只要求它在**跨出去**的时候能说清楚。

**对外部能力只有五种处置，没有第六种。** 采用（Adopt）→ 映射（Map）→ 剖面扩展（Profile-Extend）→ 适配（Adapter）→ 自定义（Define）。任何一种既有能力来到 CHASI 面前，都先问：能不能直接采用？不能，能不能映射？不能，能不能在它的剖面上扩展？不能，能不能加一层适配？只有四问皆否，才自定。**这个自上而下的问责顺序，才是“尽量复用”这句原则的可执行形式**——否则“兼容”会退化成一句谁都可以声称的口号。

**组合，而非替代。** 今天缺的不是能互相通信的 Agent，而是当这些 Agent 分属不同组织、不同信任域时，让“谁授权了什么、凭什么、结果谁负责”依然可验证的那一层。CHASI 的全部架构价值集中在这一句上：它不生产新的智能，它生产**跨域可验证性**。

## 7. Compliance Hub 的八项核心能力

这八项不是八个小功能，而是**一条链上的八个环节**：从“你是谁”到“你能被发现”。任何一环缺失，后面的都不成立。

| # | 能力 | 做什么 | **不做什么** |
|---|---|---|---|
| 1 | 身份与解析 | 让任一主体（人／Agent／组织／群组）在跨域范围内被解析，并给出其当前状态 | 不规定主体必须采用哪一种身份体系 |
| 2 | 组织与治理 | 承载权威的来源、成员归属、治理动作的记录 | 不替组织决定它自己内部怎么治理 |
| 3 | 授权与委托 | 让授权可声明、可限制、可撤销、可追溯，支持逐层子委托 | 不代替人做授权决定，也不扩大已授予的授权 |
| 4 | 群组与协作 | 让分属不同组织的主体在共同规则下协作 | 不引入任何外部群组服务作为核心 |
| 5 | 信任与状态 | 回答“现在还能不能信它”：撤销、降级、暂停、恢复 | 不把“注册过”当作“可信” |
| 6 | 证据与一致性 | 让行动留下可验证的证据，并对规范一致性给出判定 | 不代替司法或仲裁去认定事实 |
| 7 | 合规剖面与分级 | 按产业与风险等级给出差异化要求，而非一刀切 | 不用同一个标准覆盖所有场景 |
| 8 | 发现与名录 | 让合格参与者可被发现、可被检索 | **被发现不等于被信任**，名录不是信任背书 |

**三条读法。**

**第一，这八项有先后，不是并列的功能清单。** 没有身份，组织无从谈起；没有组织与授权，群组协作没有主体；没有证据，信任就只剩平台担保；没有剖面，合规只能靠人逐案解释；没有发现，合格者也进不来。**跳过任何一环去做后面的，都会退化成“又一个平台”。**

**第二，每一项都必须能落到一份可被审阅的文档上。** 一项能力若只存在于产品里、不存在于规范里，别人就无法照着实现，也无法判断自己是否合规——那它就不是能力，是**服务**。能力与规范的分界，正是这套 Hub 能不能被称作“基础设施”的分界。

**第三，八项都要有“不做什么”。** 一个 Hub 的定义，一半来自它拒绝做什么。上表第三列与第二列同等重要：**拒绝，是它不被任何一方收编的唯一保证。**

## 8. Causal Accountability Chain
CHASI 最重要的原创研究方向之一，是把 Agent 行动从“黑盒执行”转变为可验证的因果责任链。
Human
  ↓ consent / mandate
Organization
  ↓ delegation
Agent A
  ↓ sub-delegation
Agent B
  ↓ action
Tool / API / Transaction
  ↓
Evidence → Outcome → Accountability
最终能够回答的不只是“发生了什么”，而是“为什么发生、谁授权、授权范围是什么、是否超越权限、谁承担责任”。

**先要说清：“因果”比一份日志多了什么。** 三样东西常被混为一谈，差别却是决定性的：

| | 回答的问题 | 性质 |
|---|---|---|
| 调用链 trace | 调用了谁、耗时多少、在哪失败 | 技术事实 |
| 审计轨迹 audit trail | 发生了什么 | 已发生的事实 |
| **因果责任链 causal chain** | **凭什么这件事可以发生、谁有权让它发生、有没有越界** | **正当性的推导** |

审计日志记录**事件的顺序**；责任链记录**授权与行动之间的推导关系**。前者能告诉你“Agent B 在 14:03 发起了一次转账”；后者要能告诉你“Agent B 之所以可以发起，是因为 A 从组织取得了范围 R 的授权、又把 R 的一个子集委托给了 B，而这次调用没有超出那个子集”。

**链上每一环必须携带的东西**（缺一则该环不成立）：

- **主体**——是谁；
- **授权依据**——凭谁的什么权力；
- **范围**——能做什么，以及**明确地不能做什么**；
- **时间与有效期**——何时生效、何时失效；
- **委托深度**——这是第几层委托，离最初的权威还有几跳；
- **约束条件**——在什么条件下才允许；
- **证据引用**——这一环凭什么被相信。

**链会在五种地方断。** 授权来源不可解析（主体已消失或被撤销）；子委托超出了母授权的范围；跨域时对端不承认这种授权形式；时间错位（授权已过期而行动仍在发生）；证据缺失或被单方独占。**这五种不是异常，而是常态**——所以关键不在于“保证不断”。

**核心设计判断：一条诚实的断链，比一条伪造的完整链有价值得多。** 因此因果责任链的目标不是“永不中断”，而是**断了必须能被看见**：缺的是哪一环、缺在谁那里、缺的是什么，都要能被指出来。**一个能报告自己在哪里不完整的系统，比一个永远显示“完整”的系统可信。**

**哪些可验证，哪些只能声明。** 授权范围、时间、撤销状态、委托深度——可验证。意图、善意、“我已经尽力了”——只能声明。把两者混在一起谈，是责任链最常见的一种失效：**声明被当成了证明**。CHASI 的立场是把可验证的部分做到最小充分，然后**明确标出剩下的部分属于声明**——而不是用一套漂亮的可视化，把声明包装成证明。

**责任的终点必须是人或法人，不能是“系统”。** 自动化可以把行动的链条拉长，但不能把责任稀释掉。链的终点必须落在一个能够承担责任的主体上：一个人、一家组织、一个明确的法人实体。**当答案变成“是模型自己决定的”，那就说明责任链断了，而不是责任消失了。**

## 9. Societal Memory：Agent Society 的公共记忆
Agent Memory 是个人记忆；Societal Memory 是共同记忆。**两者不是“一个的放大版”，服务的对象不同**：个人记忆服务于“我记得我做过什么”，社会记忆服务于“**我们共同认定发生过什么、依据什么规则、后来为什么改了**”。

一个成熟的 Agent Society 需要保存六类记忆，而每一类的**写入者、读者、寿命都不相同**：

| 记忆 | 内容 | 谁写 | 谁读 |
|---|---|---|---|
| Event Memory | 发生过什么 | 当事方 | 与事件有关系的人 |
| Decision Memory | 为什么做出这个决定 | 做出决定的主体 | 受该决定影响的人 |
| Commitment Memory | 谁承诺了什么 | 承诺方 | 被承诺方 |
| Policy Memory | 规则何时、为何改变 | 有权改规则者 | 受该规则约束的人 |
| Evidence Memory | 行动依据什么 | 行动方 | 需要核验的人 |
| Dispute Memory | 争议如何产生与解决 | 争议程序 | 当事方与监督者 |

**社会记忆不是“永久保存一切”。** 这一点与直觉相反。要区分两件常被混为一谈的事：**必须可验证**（能核对它没有被改过）与**必须可取得**（内容谁都能读到）。一个成熟的设计可以让内容本身不可读，而“它没有变过”依然可验证——**“记得”不等于“看得见”**。把这两件事解开，公共记忆与隐私才不必二选一。

**可验证记忆不等于区块链。** 区块链解决的是“顺序与不可篡改”，代价是全量复制与全公开。社会记忆真正需要的是三样：**可验证、可控披露、可遗忘**——而区块链只给出前一半，且在最难的地方（**谁来删、按谁的规则删**）恰好帮不上忙。因此方向是**锚定而非上链**：把“某份记录在某时刻的状态”锚定在公开处，让篡改可以被发现，而记录本身留在它的权利人手里，按需、按权限、最小披露地出示。

**允许对同一事件有不同的记忆。** 中心化数据库有一个隐含假设：“只有一个正确版本”。但分歧才是常态：双方对同一次交易的理解可能都诚实，却不一致。因此社会记忆不应假装只有一个版本，而应保存**多个来源的记录以及它们之间的分歧**，把裁定交给争议程序，而不是交给恰好拥有数据库的那一方。**谁拥有数据库，谁就拥有历史——这正是要避免的。**

**Federated，而不是 central。** CHASI 的方向不是建立一个中心化的“全知数据库”，而是探索可验证、可授权、最小披露的 Federated Societal Memory：每个组织保有自己的记忆，跨域时只交换必要的那一部分，并让“交换过什么”本身也留下痕迹。

**与责任链的关系。** §8 的责任链回答**某一次行动**，社会记忆回答**这一类事情我们共同记得什么**。前者是纵深的（一次行动的那条链），后者是横向的（所有主体共享的那一层底）。缺了前者，记忆无从核对；缺了后者，每一次行动都要从头举证。**两者合起来，才是“可验证的社会”。**

## 10. Agent Society 的“宪法”
如果未来 Agent Society 是一种新的社会形态，那么除了协议，还需要类似“宪法”的最小原则集合。建议形成 CHASI Agent Society Constitutional Principles：
Identity：任何具有社会行动能力的 Agent 应有可验证身份。
Representation：Agent 必须能够说明其代表的主体或组织。
Authority：行动应有明确的授权来源。
Proportionality：权限应与任务和风险相匹配。
Revocability：授权原则上应可撤销。
Transparency：关键行动应能够提供必要解释和证据。
Accountability：自主行动不能意味着责任消失。
Privacy：治理与审计必须遵循最小必要原则。
Due Process：重大争议应具有申诉、仲裁或复核机制。
Human Primacy：涉及人的根本权益时，应保留适当的人类控制机制。

## 11. CHA2A 与 CHASI 的关系
建议把 CHA2A 与 CHASI 分成两个层次。
CHASI
Compliance Hub for Agent Society Infrastructure
        │
Governance / Identity / Delegation / Federation
        │
CHA2A
Agent-to-Agent / Agent Society Architecture & Protocols
CHA2A 可以继续发展为具体的 architecture、protocol、profiles 和 extensions；CHASI 则承担更高层的 Vision、Governance、Compliance Framework、Research Hub 和生态连接。
这样既可以保持技术工作的独立性，又能够让 ComplianceHub.cn 成为一个长期的公共研究与生态入口。

## 12. CHASI 与现有生态的关系
A2A / AAIF：Agent-to-Agent interoperability。
OpenA2A：开放 Agent interaction / protocol research。
MCP：Agent-to-tool / resource connectivity。
DID / VC：decentralized identity 与 verifiable credentials。
OAuth / OIDC：成熟的 authentication / authorization 基础。
NANDA：Agent Internet discovery、registry 与 infrastructure research。
MIT / Stanford：Agent Internet、human-agent interaction、memory、identity、society 等研究。
CHA2A：把这些能力组织进面向 Agent Society 的开放架构。
CHASI：在其之上提供 compliance、governance、evidence、accountability 与 federation 的 Hub。

## 13. CHASI 的生态哲学：兼容 + 互补 + 独立
这是 CHASI 最重要的战略原则。
Compatible with the ecosystem
          +
Complementary to the ecosystem
          +
Independent from any single ecosystem
          =
CHASI
因此 CHASI 不需要与 AAIF、IETF、W3C、ITU、Linux Foundation、MIT、Stanford 或其他项目竞争“谁定义整个 Agent Internet”。它可以成为连接这些不同力量的治理与研究枢纽。

## 14. ComplianceHub.cn 的长期愿景
ComplianceHub.cn 可以逐步从一个网站发展成为一个开放研究与生态平台：
CHASI Architecture：公开架构。
CHASI Principles：公开治理原则。
CHA2A Specifications：技术规范与 Profiles。
Reference Implementations：参考实现。
Compliance Profiles：不同产业和风险等级的合规配置。
Agent Society Testbeds：跨组织 Agent 实验环境。
Research Observatory：持续跟踪全球 Agent Society 研究。
Interoperability Lab：测试不同 Agent 协议与 Runtime 的互操作。
Academic Collaboration：与 MIT、Stanford 等研究团队合作。
Standards Liaison：参与 AAIF、IETF、W3C、ITU 等相关工作。

## 15. 最终 Vision
我们最终追求的并不是一个“Agent 的世界”，而是一个 Human 与 Agent 可以长期共存的世界。
在这个世界里，人不需要理解每一个底层 Agent 的技术细节，也不需要相信某一家平台；人只需要能够知道：这个 Agent 是谁、代表谁、被授予什么权力、正在做什么、为什么这么做，以及如果事情出了问题，谁能够解释、纠正和负责。
Agent 也不应该被设计成没有权利、没有边界、没有身份的纯工具。一个成熟的 Agent Society 应当允许 Agent 在明确的角色、权限和责任边界内自主协作。
Human Freedom
      +
Agent Autonomy
      +
Organizational Responsibility
      +
Verifiable Governance
      ↓
A Sustainable Agent Society
这就是 CHASI 的最终愿景：通过开放、兼容、可验证的治理基础设施，让智能体互联网从“Agent 可以互相调用”逐步走向“人和 Agent 可以共同生活、共同工作、共同创造价值”。

## 结语
如果 CHA2A 是我们对于 Agent Internet / Agent Society 的技术探索，那么 CHASI 可以成为更大的 Vision：一个不属于任何单一公司、平台或 Agent Runtime 的开放治理枢纽。
它不是为了控制 Agent，而是为了让自主性、信任、责任和自由能够同时存在。
从这个意义上说，Compliance 不是限制 Agent Society 的力量，而是使这种社会真正能够规模化存在的基础条件。
—— CHASI Vision · v1.4
