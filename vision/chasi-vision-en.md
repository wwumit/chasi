# CHASI Vision

**Compliance Hub for Agent Society Infrastructure**

---

> Status: draft v2.26 | Kind: **vision**
> **This document says *why*, and *where to*. It creates no obligation for any party.** Where it conflicts with a specification, the specification governs.

---

## 0. Summary

> **A third party belonging to no party should be able to check who acted, who authorized the action, which rules applied, what evidence was left, and who finally bears responsibility.**
>
> **The same requirement applies to every relationship among organizations, groups and agents.**

## 1. Membership Is Plural

**The Agent Society in this vision has four kinds of subject: people, organizations, agents and groups.** The kinds of member determine the boundaries of governance and collaboration; the number of connections is not the criterion.

| Position | Who / what | Note |
|---|---|---|
| **Subject** | **Person** | a natural person |
| | **Organization** | companies, institutions, governments, non-profits |
| | **agent** | may act as personal assistant, organizational member, business partner, research partner, social collaborator — **these are its roles, not its kind** |
| | **Group** | temporary, long-lived, cross-organizational; **a family or a community is its smallest form**; it may have rules and a memory of its own |
| **Not a subject** | **Service · tool · resource · data** | they do not belong to the society, but the society uses them — **so they too need names that can be cited, and those names must not be mistaken for subjects** |

**One agent may belong to several organizations and groups at once**, and its role in each may differ. Belonging therefore cannot be reduced to a single answer; identity and authority must be expressed for each context.

**One kind that has no place here yet.** The four kinds of subject above are peers, but there will be entities that are **both an agent and an organization** — an autonomous entity that is itself a legal person, holding assets, concluding contracts, bearing responsibility and being held to it. This table gives it no place yet. **Undecided: which kind it is** — to be settled by whether its capability set differs from both an organization's and an agent's.

## 2. What Is in This Society

This section lists the elements a society normally needs. The third column gives the condition each one rests on; **the conditions themselves are in §3**, and are only pointed at and supplemented here:

| It has | Meaning | The condition it rests on |
|---|---|---|
| **Roles** | one agent can be assistant, colleague, counterparty and fiduciary at once | **①** — an action must state which role it was performed in |
| **Relationships** | relationships persist, change, break | **①** — the state of a relationship is readable, its termination traceable |
| **Collaboration** | some things one party cannot do alone | **①** — cross-party collaboration leaves a record that can be rebuilt |
| **Exchange** | value moves | **①** — authority and evidence are verifiable; **settlement itself is outside this family's scope, see §17** |
| **Memory** | a society needs continuity | **①⑤⑥** — public memory exists, with minimal disclosure |
| **Dispute** | things go wrong | **①④** — the handling rules exist, are declared and are checkable; a person may question |
| **Common interest** | some things belong to no one and matter to everyone | **no condition in §3 yet, see below** |
| **Evolution** | rules change, members come and go | **⑤** — rule changes leave a history |

**Two things are undecided.**

**First, common interest has no condition.** None of the seven in §3 covers it. Settling it requires deciding three things first: who may hold such a thing, how the holding is made checkable, and how the holder is held responsible. The only role in this family that could carry it is **fiduciary**, and the duty of care that role implies is not specified anywhere yet.

**Second, relationships have no object.** The condition requires the state of a relationship to be readable and its termination traceable, but the family has no relationship object: Organization and Group each have a volume, and membership is the closest thing to it, but neither covers a cross-organizational relationship itself. Settling it requires deciding the fields first: the parties, the type, when it takes effect, when it ends, and who may end it.

**One boundary.** Exchange, payment, settlement and listing are outside this family's scope (§17); the authority and evidence an exchange rests on are inside it, and their condition is **①**.

## 3. Seven Conditions for Sustained Operation

**① is necessary, not sufficient.**

| # | Condition | Meaning |
|---|---|---|
| **①** | **Verifiable** | a third party belonging to no one can answer four questions **independently**: **who it is · who authorized it · in what context it is acting · what it has done** |
| **②** | **Coexistable** | societies with different rules can coexist **without first unifying**; recognition is each party's local policy |
| **③** | **Exitable** | a member can leave, and after leaving every right and obligation has a definite destination |
| **④** | **Accountable** | every action can be held to a specific person or legal entity, and cannot stop at "the system" |
| **⑤** | **Changeable** | rules can change, **and the change has a history** — judgement falls at the moment the action happened, and is not tried retroactively by later rules |
| **⑥** | **Minimally disclosing** | governance and audit do not require unbounded surveillance; evidence follows minimal necessity |
| **⑦** | **Autonomous** | within its boundaries an agent may act on its own, **without asking at every step** |

**The seven conditions are not one kind of thing, and cannot be treated as seven tests of the same type.**

| Checkable of the system | To be preserved for participants |
|---|---|
| ① verifiable · ⑤ changeable · ⑥ minimally disclosing | ② coexistable · ③ exitable · ④ accountable · ⑦ autonomous |

**Where the four questions come from, and what each answer must contain.** Their normative statement is in the family entry, `overview.md` §1. **The four questions are not by themselves enough to judge** — an answer can exist in form and be useless in fact, so each question also has to say what its answer must contain:

| Question | Its answer must contain | Carried by |
|---|---|---|
| **Who it is** | a resolvable identifier, with a portable trust root — **not established by the party being asked about** | the identity binding; §7, "no central root" |
| **Who authorized it** | the basis of authority, **the scope** (what may be done, and explicitly what may not), and **the time and validity** | §12's seven per-link items |
| **In what context it is acting** | **the rule in force at the time** | §4, "time coordinate" |
| **What it has done** | evidence, **and the end of responsibility** (a person or a legal entity) | §12 |

**Two items that used to be listed as separate questions are folded in above.** "How far the scope reached" is part of the answer to the second question; "who bears responsibility" is part of the answer to the fourth. They are not fifth and sixth questions — **treating them as separate questions means judging the same thing twice in two places.**

**① makes actions checkable; ②–⑦ define the range in which actions can take place safely.** With only ①, an action can be established after the fact, but participants lack dependable boundaries.

## 4. What Is Missing

§1–§3 describe an agent society that can operate sustainably.

**These capabilities serve one purpose: tracing responsibility to its source.** Starting from an action, one can find who did it, under whose authority, under which version of the rules, on what evidence, and who finally answers for it, without a break in the chain.

Identity, credentials, discovery, scope narrowing and audit already have work behind them. What is missing is two positions, and two defaults that are likely to be adopted unless they are named.

**One. The seven conditions are spread across different parties, and no single place carries them together.**

| Condition | Today | To hold |
|---|---|---|
| ① Verifiable | the asking side and the answering side usually sit in different systems | checking does not depend on either party being present |
| ① Third-party answer | the records that count are mostly held by the parties themselves | a third party belonging to no one can answer |
| ⑤ Time coordinate | no layer carries "which rule was in force then" | a rule change is itself citable |

Each of the three has someone working on it; none has a single place carrying all three. **The capabilities exist separately; what is missing is a position that carries them together.**

**Two. Two defaults make these conditions difficult to hold at the same time.**

| Default | What the world becomes | What is lost |
|---|---|---|
| verification before the action | every step asks first | ⑦ autonomy |
| verifiability as total logging | governance becomes surveillance | ⑥ minimal disclosure |

The second does not follow from ① itself. ① asks only that a question be answerable: it neither requires time nor requires recording everything. The imbalance comes from reading verification as "approve first" or "log everything".

**The criterion is therefore "a default plus a declaration when departing from it"**: verification by default happens after the fact or by sampling, and logging takes the minimum necessary; a party departing from the default states why. The default values themselves are not yet fixed.

**Each imbalance needs a checkable form in which both sides hold at once**, or there is no way to tell whether it has been solved. §12 gives one for ①×⑦: **an incomplete chain must be reportable** — verification does not intercept before the action, but it can point to the missing link afterwards. For ①×⑥ there is no such form yet.

**One unanswered time mismatch.** ② (societies with different rules can coexist) and ⑤ (rules change, and judgment attaches to the moment of action) together produce a cross-society time mismatch: which side's rule applies depends on whom you ask. Answering it requires first fixing how a cross-society rule change takes effect and is recorded.

## 5. A governable agent internet

In a governable agent internet, agents carry their own identity, authority and evidence across boundaries, and no party has to accept a centre first.

What we have in mind:

1. **Every member has an identity that can be stated.** People, organisations, agents and groups each have a resolvable identifier; one agent may belong to several organisations and groups at once, with a different role in each.
2. **Identification does not route through any single platform.** To find out who a subject is and whether it is currently valid, there is no need to ask it, and no need to ask the platform it belongs to.
3. **Authority traces back to an origin.** Every action can be followed along the authority chain to a person or a legal entity; a missing link is a missing link, and is not reported as "the system decided".
4. **Autonomy inside the scope; no authority outside it.** A delegation states what may be done and, explicitly, what may not; inside that scope an agent does not ask step by step.
5. **Judgment has a time coordinate.** The basis is the rule in force when the action happened, not the version revised afterwards.
6. **Records can be checked by a third party.** A record can be judged to have happened, and judged not to have been altered, without depending on any party's system.
7. **Memory is federated.** Each party keeps its own memory; only what is necessary crosses a boundary; disagreement about the same event is itself kept.
8. **A group can exist across organisations.** Membership and roles can be verified without a common superior and without one party's database deciding.
9. **Exit is normal, not an incident.** A member can leave; rights and obligations each have a destination; records do not disappear because someone left.
10. **People are not monitored wholesale, but can question and hold others to account.** Governance and audit take the minimum necessary; any agent's action can be traced to a party answerable for it; a person can question that party and seek accountability under law or agreement.

**Governance is distributed across the members, and a third party belonging to no one can check it.**

### 5.1 Where CHASI sits in this target state

**A venue.** It assembles parts from different sources, uses experiments it designs and runs itself to test whether these ten can hold at once, and publishes the result of every experiment as a record.

- it **defines no mechanism** — how to identify an agent, how to discover, how to narrow a delegation, each has its own owner;
- **a condition is not an obligation** — it states conditions for a path assembled from these parts, and makes no demand on those who do not use it;
- what it produces is **findings and records**, not rules.

**Three attitudes to the existing ecosystem**: **compatible** (reuse what can be reused; ask in order — adopt, map, profile-extend, adapt, define — and only define when the first four all answer no), **complementary** (fill only the gaps the ecosystem leaves in cross-organisational identity, authority, governance, evidence and accountability), **independent** (attached to no single vendor, runtime or identity system). With all three holding, there is no need to compete over "who defines the whole Agent Internet".

### 5.2 The name

CHASI = Compliance Hub for agent **Society** Infrastructure. Compliance here **does not mean "checking whether others comply"**; it means **the conditions under which verifiability can hold** (§3①): records are complete and can be checked by a third party belonging to no one.

**Undecided: whether the word should be replaced by one without the "inspection" reading** — the current name is easily read as a regulator.

### 5.3 Expectations of regulation

CHASI is not a regulator and will not become one. But a vision can hold expectations of regulation:

1. **A regulator can have its own resolver.** It does not need to own the infrastructure to read the status and evidence it needs.
2. **Regulation rests on verifiable facts, not on a platform's own account.** A platform saying "reviewed" is not the same as the fact having been checked.
3. **Regulation closes only at the boundary.** How a domain governs itself belongs to its members; the stretch that crosses out is what needs to be publicly checkable.
4. **Regulation does not buy itself with total logging.** Minimal necessity binds regulators too.
5. **A regulatory judgment can be recomputed, and leaves a record.** A regulator can itself be questioned and held to account.
6. **Responsibility lands on a person.** Every action can be traced to a specific person or legal entity; it cannot stop at "the system".

---

## 6. What this target state does not include

- **Not another agent protocol.** Communication, identity, discovery and narrowing delegation each have their own owners (§5);
- **Not a standards body.** It does not vote, does not ballot, sets no entry threshold;
- **Not a platform.** It **runs no registry**, encloses no network effect, sells no SKU;
- **Not a regulator.** It claims no regulatory territory and is not the final enforcer of any arbitration (§10).

**Each of the four has one boundary, next to the capabilities in §11.**

**First, it carries state, and therefore necessarily holds a directory.** Capabilities 1, 5 and 8 in §11 require it to resolve subjects, answer current status, and let entries be found — the vehicle for all three is a directory. **Directory and registry must be kept apart: a directory holds declarations, a registry settles facts. CHASI does only the former**; what this section denies is the latter.

**Second, "no entry threshold" and "let entries be found" have different subjects.** CHASI does not judge who qualifies (judgement is left to the verifier, §7); it only lets entries that **declare against a profile and attest to themselves** be found, and the verifier judges for itself whether an entry meets its own requirements. **So there is no threshold, but there are profiles** — the threshold is set by the verifier, not by CHASI.

**Third, a profile is a condition, not a licence.** The same distinction as in §5: a profile constrains "a path assembled from these parts", and does not constrain anyone who does not adopt it.

**Its only possession is credibility**, and credibility accumulates only by records being accurate. For credibility to be checkable, one more thing must be specified: **when a published record is found to be wrong, how it is corrected, by whom, and how the correction itself is recorded.** §7's "downgrades must be visible" concerns the status of a subject and does not cover published records. **Undecided: the correction rule; settling it requires deciding who has standing to challenge a published conclusion.**

**This family's own responsible entity is not yet written down.** §12 requires the end of responsibility to be a person or a legal entity; this section and the document as a whole impose that requirement on every subject, but **do not say which legal entity is responsible for the records CHASI itself publishes**. A record published by CHASI and later shown to be wrong needs a party that can be held to account. **Undecided: this family's own responsible entity.**

## 7. What CHASI Does Not Adopt for This Target State

For this target state to hold, CHASI has to exclude several easier options. Each row is a trade-off and what it binds this family to.

| Given up | Why | Therefore CHASI must |
|---|---|---|
| **No central root** | cross-domain trust cannot be established by any party's registry; the trust anchor is the one the verifier configures itself | **this family's own directory is not a trust root either** — the status it provides is an input, not an anchor; replacing this family's directory, a verifier should still be able to judge by the anchor it configured itself (§11 capability 5) |
| **No mutual recognition required** | recognition is each party's local policy; if it can be translated, it need not be agreed in advance | supply the **mapping** (§10's Map), and state **who maintains it and how its version is marked**; otherwise "can be translated" never lands |
| **Facts, not ratings** | record facts; judgement is left to each verifier. Issuing a rating would make the issuer a party to the trust judgement | no conclusive rating by this family appears in a record. §11 capability 7's "profiles and grading" **declares what must be met**, it does **not judge who has met it** |
| **Records outlive their subject** | a record must be able to outlive the organization and platform that produced it; otherwise it is a log, not evidence | see below — this is in tension with the design in §13, and is unresolved |
| **Downgrades must be visible** | a silent downgrade is a deception | a status transition must leave a trace, and be **visible to every party that relies on that status**; "visible" needs defining: who, within what time, by what route |
| **Presuppose no system** | otherwise admission would depend on one ecosystem's conditions | no identity system or runtime may be made a precondition of taking part |
| **Autonomy is not an exception** | autonomy within boundaries is the norm; a system that must ask at every step is a tool, not a member | **"asking at every step" may not be used as the means of satisfying verifiability**; verification defaults to after the fact or to sampling, and departing from that default must be justified by the declaring party (§4) |
| **Questioning and accountability replace surveillance** | questioning and holding to account do not require seeing everything; unbounded surveillance is not a precondition of accountability | **a record published by this family must let a third party belonging to none of the parties answer "who did it, on what authority"**; a record may not be visible only to the parties |

**The last two restate the conditions in §3; they are not repeated here — only what they require of this family.** §3④ and §3⑦ state conditions for sustained operation; this table says what CHASI must therefore do. **Each "therefore" entry gives a checkable landing point.**

**One unresolved tension: records outlive their subject × each organization keeps its own memory.**

The fourth row above requires that "a record be able to outlive the organization and platform that produced it"; the design in §13 is Federated — **each organization keeps its own memory**, only the necessary part is exchanged across domains, and records are **anchored rather than on-chained**. The two conflict on **availability**: if a record exists only with the organization that produced it, the organization disappears and the record disappears with it; **anchoring can prove "it was not altered", it cannot guarantee "it is still there".**

**Undecided: how a record remains obtainable after its holder is gone.** Settling it requires choosing among three paths and stating the conditions — designate a successor, place it with a third-party custodian, or keep a publicly obtainable digest in addition to the anchor. The three differ in their effect on minimal disclosure.

(For the proposal on "what an agent society ought to have", see the next section.)

## 8. Constitutional Principles for an Agent Society (a proposal)

If the Agent Society needs a set of common clauses something like a constitution, then besides protocols it needs a set of constraints. This section puts forward one, provisionally called the **CHASI Agent Society Constitutional Principles**.

The three tables bind different parties:

| Section | What it is | Who it binds |
|---|---|---|
| §3, the seven conditions | the properties a society needs for sustained operation | descriptive — if unmet, sustained operation is not possible |
| §7, CHASI's own choices | constraints this place accepts for itself | binds this family only |
| **§8, this section** | which clauses a constitution would at least have to contain | **binds no one** — whether to adopt them is the society's own decision |

§6 has stated that CHASI is not a standards body and sets no entry threshold. The clauses below may be used as they stand, rewritten, or used only in part; whether to adopt them is for each party to decide.

Of the ten clauses, seven already have a landing point and three are new:

| Clause | Content | Where it lands |
|---|---|---|
| **Identity** | any **subject** (person, organization, agent, group) should have a verifiable identity | that is §3①'s first question, "who it is"; §11 capability 1 |
| **Representation** | a subject must be able to state whom it represents | falls under §3①'s second question, "who authorized it" |
| **Authority** | an action should have a clear source of authority | that is §3①'s second question |
| **Transparency** | key actions should be able to give the necessary explanation and evidence | falls under §3①'s fourth question, "what it has done" |
| **Accountability** | autonomous action does not mean that responsibility disappears | part of the answer to §3①'s fourth question (the end of responsibility); see §12 |
| **Privacy** | governance and audit follow minimal necessity | that is §3⑥, minimally disclosing |
| **Revocability** | authority should be revocable | §11 capability 5; §12 has each link carry revocation status |
| **Proportionality** | authority should match the task and the risk | no counterpart among §3's seven. **Undecided**: who judges the match, and on what scale |
| **Due Process** | serious disputes should have appeal, arbitration or review | §13's dispute memory already assumes a "dispute process" exists, but **the document nowhere says who provides it**. **Undecided**: the provider |
| **Human Primacy** | where a person's fundamental interests are at stake, human control is retained | §7, "questioning and accountability replace surveillance". **Undecided**: which interests count as "fundamental", and who judges |

The new content is concentrated in Proportionality, Due Process and Human Primacy; the other seven are covered by §3, §7 or §11.

These clauses cannot yet be called "minimal". Removing the seven with existing landing points leaves three, but there is no criterion for which of those three cannot be removed. **Undecided: the basis for judging minimality.**

The clauses use "subject", covering person, organization, agent and group. If they bound only agents, organizations — equally capable of being authorized and held responsible — would fall outside the constitution.

## 9. How It Works

**Learn → Assemble → Test → Record → Publish.**

| Step | What it does |
|---|---|
| **Learn** | whatever is good and has been done by others, **learn it actively**, respecting intellectual property. Do not go looking for original technology of our own |
| **Assemble** | assemble parts from different sources into a path that can satisfy the seven conditions |
| **Test** | run real scenarios and record **which condition fails, and at which step of which part** |
| **Record** | each result becomes one record (content below) |
| **Publish** | publish the findings so that others can cite them (requirements below) |

The six stages of an experiment — Scenario → Experiment → Observation → Architecture → Specification → **Re-test** — are in `method/use-case-laboratory.md` §2. The table describes how one piece of work proceeds; the six stages describe the loop. The difference is Re-test.

"Record" has three uses in this document. The four items below govern the first: the finding of one experiment.

| Where | What is recorded | Who writes | What governs the content |
|---|---|---|---|
| **§9, "Record"** | the finding of one experiment | this family | the four items below |
| §12, the accountability chain | the derivation of authority for one action | the acting party | §12's seven per-link items |
| §13, societal memory | facts the society jointly holds | varies by memory class | §13's six classes |

When §6 says "credibility accumulates only by records being accurate", it means the first. An experiment record contains four items:

- **version** — state **which part, at which version**, not just "version";
- **date**;
- **conclusion** — which conditions held, which did not;
- **review condition** — not "when to review", but **what condition, once it occurs, requires a review** (for example, a part it rests on being version-bumped).

A record must carry four items to be citable; otherwise §16's "a citable public memory" cannot hold:

- **an identifier for the record** — a record needs a name that can be cited (the same requirement §1 places on non-subjects, "they too need names that can be cited");
- **where it is published** — where, and who can obtain it;
- **a licence** — how far others may cite it;
- **a survival arrangement** — §7's "records outlive their subject" requires a record to outlive the organization and platform that produced it, while §13 is Federated; this is unresolved (see §7).

**"A conclusion that does not hold must be published too."** That is: **a failure to satisfy every condition is not a reason to withhold publication**; the record must state **which condition failed, and at which step of which part**.

## 10. CHASI Architecture

```

   Subjects            Human · Organization · agent · Group
                                │
   Identity & trust    who it is · whether it can still be relied on
                                │
   Governance          who has authority · under which rules · may delegate to whom
                                │
   Evidence            on what basis this happened · whose responsibility
                                │
   Interconnection     A2A · MCP · DID/VC · OAuth

```

**The architecture has five layers, each answering one question:**

| Layer | The question it answers | What else is in it |
|---|---|---|
| Subjects | who is present | Human · Organization · agent · Group |
| Identity and trust | who it is; whether it can still be relied on | and it handles **non-subject resources that need to be referred to**: service · tool · data — **they may be named, they may not be treated as subjects** |
| Governance | who has authority, under which rules, and may delegate to whom | |
| Evidence | on what basis this happened, and whose responsibility it is | |
| Interconnection | how it composes with existing protocols, runtimes and identity systems | A2A · MCP · DID/VC · OAuth |

**Dependency runs one way.** An upper layer **may** require a lower one to provide some capability — the governance layer requires the identity layer to resolve subjects; an upper layer **may not** dictate how a lower one is implemented — the governance layer does not dictate which cryptography the identity layer uses, and the evidence layer does not dictate what organizational form the governance layer takes. The purpose is to let **every layer be replaceable**; the family's `governance-architecture`, declaring of itself that it "states no requirements", is the strict version of the same thing.

**Persons are not the only origin of authority.** The figure draws authority downward from the subject layer, but a subject's authority may come from its own founding instrument rather than from anyone's consent: §12 states that the chain ends at "**a person, an organization, a definite legal entity**"; L3's `organization-governance` decomposes authority into four layers — "charter → office → holder → root authority basis". The figure does not mean "all authority originates from persons".

**What CHASI does not own.**

- it does not define communication primitives — A2A and MCP exist;
- it does not define cryptographic primitives, nor any DID method itself — DID and VC exist;
- it builds no agent runtime, no model, no workflow engine;
- it is not a regulator, and not the final enforcer of any arbitration.

This family has a DID method (`did-method-cha2a`). It belongs to **CHA2A**, not to the CHASI architecture layer (see §14). **The architecture layer therefore does not define a DID method**; this family does not lack one.

CHASI has exactly one boundary — **the stretch that crosses subjects and crosses domains**. What happens inside a domain stays inside it; how an organization divides work or audits itself is not for CHASI to specify. CHASI asks only that it be able to say clearly what it did **when it steps outside**. This document has not yet defined "domain". **The domain is the criterion for whether CHASI applies at all**: if any subject can simply declare "this is a domain", the boundary can be sidestepped. **Undecided: the basis for judging a domain** (who declares it, whether the declaration needs to be recognized by others, whether different subjects are by themselves sufficient for "cross-domain").

**There are five dispositions of an external capability, and no sixth.** Adopt → Map → Profile-Extend → Adapter → Define. Any existing capability is judged in that order: can it be adopted, mapped, extended within its own profile, or reached through an adapter? Only when the first four all answer no do we define our own. The ordered test makes "reuse as far as possible" executable; otherwise "compatible" degrades into a slogan anyone can claim.

The five dispositions form a decision procedure and therefore need a decision record. Which dispositions were tested, and where the conclusion landed, should be checkable; otherwise there is no telling whether "define our own" was necessary or merely convenient. **Undecided: who makes the decision, where it is recorded, and which of §9's record classes it belongs to.**

**CHASI provides a composition layer.** When agents belong to different organizations and different trust domains, they need a layer that keeps "who authorized what, on what basis, and who answers for the result" verifiable. CHASI produces **cross-domain verifiability**, not new intelligence.

## 11. The Eight Core Capabilities of the Compliance Hub

The eight form **eight links in one chain**: from "who you are" to "you can be found".

The eight are **conditions of a composition**, not mechanism definitions (§5): this family does not specify "how to identify an agent" or "how to discover"; it specifies **what a path assembled from these parts must satisfy**. Each row below therefore gives both "what it does" and "what it does not do".

| # | Capability | What it does | **What it does not do** |
|---|---|---|---|
| 1 | Identity and resolution | let any subject (person / agent / organization / group) be resolved across domains and give its current status; **and let non-subject resources that need to be referred to (service / tool / data) be resolved too** | does not require any particular identity system; **and does not treat a non-subject resource as a subject — it may be named, it may not be authorized** |
| 2 | Organization and governance | carry the source of authority, membership, and the record of governance actions | does not decide how an organization governs itself internally |
| 3 | Authority and delegation | make authority declarable, limitable, revocable and traceable; support delegation layer by layer | does not make authorization decisions for people, and does not widen authority already granted |
| 4 | Group and collaboration | let subjects from different organizations collaborate under common rules | introduces no external group service as its core |
| 5 | Trust and status | answer "can it still be relied on now": revocation, downgrade, suspension, restoration | does not treat "registered" as "trustworthy"; **this family's own status answer is not a trust root either** (§7) |
| 6 | Evidence and conformance | let actions leave verifiable evidence; give **checkable test results** for conformance to a specification | **does not judge "whether someone is compliant"** — judgement is left to the verifier (§7); does not establish facts in place of a court or arbitration |
| 7 | Compliance profiles and grading | by industry and risk level, **declare what must be met**, rather than one size for all | **does not judge who has met it** (§7); does not cover every scenario with a single standard |
| 8 | Discovery and directory | let entries that **declare against a profile and attest to themselves** be found and searched | **this family does not judge who qualifies** (§6); being found is not being trusted, and a directory is not an endorsement |

**Three points.**

**First, the eight have dependencies, but not every one depends on the one before.** The real dependencies are in the first four: without identity there is no organization to speak of; without organization and authority, group collaboration has no subject. **The last four are not like that** — a profile does not need evidence in order to exist, and a directory does not need profiles. **The first four are preconditions of the last four, and the last four do not precede one another**; reading the eight as a straight line also reads confusingly against §6's "no entry threshold".

**Second, each one must land on a document that can be reviewed.** If a capability lives only in a product and not in a specification, no one else can implement it, and no one can tell whether they comply — then it is not a capability, it is a **service**. The line between capability and specification is exactly the line between whether this Hub can be called infrastructure. Capability 6 lands in L5: the conformance vectors and checkers are in `cha2a-conformance` (68 vectors, dual-verifier interlock); L5 spans two companion repositories — evidence in `did-method-cha2a`, conformance in `cha2a-conformance`, see the README index table. The Hub can produce conformance results; conformance itself is not defined here.

**Third, all eight must have a "what it does not do".** The third column matters as much as the second: **half of a Hub's definition comes from what it refuses to do.** The most important entries in that column are capabilities 6, 7 and 8 — they block "judging compliance", "judging attainment" and "judging qualification" respectively; do those three and this family becomes a regulator, which §6 has stated it is not.

## 12. Causal Accountability Chain

One of CHASI's key lines of research is turning **action by a subject** from an uncheckable execution record into a verifiable causal accountability chain.

```

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

```

Each arrow in the figure is a kind of **delegation**; each link carries the seven items below, which make the chain checkable.

**This chain is one path for tracing responsibility, not the only governance topology.** Registrars, discovery providers, credential issuers and controllers may be authorized separately; their verification paths may run in parallel, cross one another, or refer to one another. The causal accountability chain answers how one action is authorized and traced to a responsible subject; it does not force every role into a single delegation chain.

| Path | The question it answers |
|---|---|
| Causal accountability chain | how one action is derived from authority and traced to a responsible subject |
| Registration path | who may register a subject, within which scope and with what current status |
| Discovery path | who may index and return a resource, and what provenance the result carries |
| Credential path | which credential issuer makes a claim under which profile, and what its status is |
| Control path | which controller or delegated operator may make the change or perform the action |

It must ultimately answer why the action happened, who authorized it, what the scope of that authority was, whether it was exceeded, and who bears responsibility. Answering only "what happened" is insufficient for responsibility.

**"Causal" adds a derivation of justification beyond an audit log.** The three differ as follows:

| | The question it answers | Its nature |
|---|---|---|
| Call trace | who called whom, how long it took, where it failed | technical fact |
| Audit trail | what happened | fact of what occurred |
| **Causal accountability chain** | **on what basis this could happen, who had the authority to let it happen, whether the boundary was crossed** | **derivation of justification** |

An audit log records **the order of events**; an accountability chain records **the derivation between authority and action**. The former can tell you "Agent B initiated a transfer at 14:03"; the latter must be able to tell you "Agent B could initiate it because A obtained authority over scope R from the organization, and delegated a subset of R to B, and this call did not exceed that subset".

**What every link must carry** (without which the link does not hold):

- **subject** — who;
- **basis of authority** — whose power, of what kind. **This is not a self-declaration**: it must be traceable to its origin along the four-layer decomposition in L3 `organization-governance` §4 (charter → office → holder → root authority basis), see §10;
- **scope** — what may be done, and **explicitly what may not**. **Scope is also the line between autonomy and responsibility** (see below);
- **time and validity** — when it takes effect, when it lapses;
- **delegation depth** — which layer of delegation this is, and how many hops from the original authority;
- **constraints** — under what conditions it is permitted;
- **evidence reference** — on what basis this link is to be believed.

**An accountability chain fails, and failure comes in two kinds, with different handling:**

| Failure | What it is | How it is seen |
|---|---|---|
| **Missing link** | the basis for a link cannot be found: the source of authority cannot be resolved (the subject is gone or revoked); evidence is missing or held by one party alone | **identified** by the verifier — which link is missing, and with whom |
| **Excess of scope** | the links are all there, but the action exceeded the scope of its link; a sub-delegation exceeded its parent; time is out of alignment (authority had lapsed while the action still happened); across domains, the counterparty does not recognize the form of authority | obtained by **comparing scope**, not by finding a missing link |

Neither kind is an anomaly; both are the norm. **So the point is not "guaranteeing it never breaks", but that each kind has its own checkable form** — "a break must be visible" expands into two rules:

- **a missing link must be identifiable**: the record must be able to point out which link is missing, with whom, and what is missing;
- **an excess of scope must be comparable**: each link's scope must be written to a degree that **can be compared against the action**; declaring "there was authority" is not enough.

**Scope is the boundary between autonomy and responsibility.** §3⑦ allows an agent to act autonomously within its boundaries, **without asking at every step**; this section requires the end of responsibility to fall on a person or legal entity. The condition under which both hold is: **scope is given by the principal, within scope the agent is autonomous, and outside scope there is no authority**. The principal bears "the scope it drew", not "the actions it approved one by one". **Undecided: when a link does not state its scope, whether the default is "no authority" or "the same as the parent".** The family's practice elsewhere is conservative (§6, "does not treat registered as trustworthy", and the scope comparison both depend on it), but this section does not state it.

**What is verifiable, and what can only be declared.** Scope of authority, time, revocation status, delegation depth — verifiable. Intention, good faith, "I did my best" — declarable only. Conflating the two causes the commonest failure of accountability chains: **a declaration taken for a proof**. The verifiable part should be listed with a checking method for each item; the rest should be marked explicitly as declaration. A declaration may not be dressed up as proof through visualisation. **Undecided: the criterion for "minimally sufficient"** — how small the verifiable part can be, and what it must still cover, so as neither to over-record (§3⑥) nor to under-support judgement.

**The end of responsibility must be a person or a legal entity, not "the system".** Automation may lengthen the chain of action, but it does not change where responsibility lies: the chain must end at a subject capable of bearing responsibility — a person, an organization, a definite legal entity. **If the only way to write the end of a chain is "the model decided on its own", then responsibility has not disappeared; the chain is missing a link** (the first kind of failure above). **Undecided: when the chain crosses outside this family's scope** (the counterparty does not recognize the form of authority), where the end falls.

## 13. Societal Memory: the public memory of an Agent Society

Agent Memory is personal memory; Societal Memory is shared memory. **They are not "one scaled up"; they serve different subjects**: personal memory serves "I remember what I did", societal memory serves "**what we jointly hold to have happened, under which rules, and why those rules later changed**".

A mature Agent Society needs to keep six kinds of memory, with the **writer and read scope** of each as follows (**retention** is discussed below):

| Memory | Content | Who writes | Who reads |
|---|---|---|---|
| Event Memory | what happened | the parties | those connected to the event |
| Decision Memory | why this decision was made | the deciding subject | those affected by it |
| Commitment Memory | who promised what | the promiser | the promisee |
| Policy Memory | when and why a rule changed | whoever may change the rule | those bound by it |
| Evidence Memory | what an action rested on | the acting party | whoever needs to verify |
| Dispute Memory | how a dispute arose and was resolved | **the dispute process** (provider undecided, see §8) | the parties and overseers |

**The retention periods of the six classes are not specified.** §7's "records outlive their subject" requires a record to outlive its subject; the retention period is where that requirement becomes a condition in time. **Undecided: the retention period of each of the six, and who decides what happens at expiry** (delete, archive, or withdraw obtainability while keeping verifiability).

**Verifiable and obtainable are two different requirements.**

- **must be verifiable** — it can be checked that it was not altered;
- **must be obtainable** — the content can be read.

The "who reads" column above is about **obtainability**, not verifiability. The two can diverge: a record can be unobtainable to most and verifiable to all. Therefore:

- **every class of memory must be verifiable**, without exception;
- **the extent of obtainability is specified class by class in the table above**, and must state **who authorizes obtaining it** (the table gives "who reads", not "who approves").

**Undecided: who authorizes obtaining it.** This section, §8's Due Process and §11 capability 1 all assume an authorizing role exists; this document does not yet name it.

**Verifiable memory is not blockchain.** Blockchain settles "order and immutability", at the price of full replication and full publicity. What societal memory actually needs is three things — **verifiable, controllably disclosed, forgettable** — and blockchain gives only the first half, and is of no help exactly where it is hardest (**who deletes, and by whose rules**). The direction is therefore **anchoring rather than on-chaining**: anchor "the state of a record at a moment" in a public place, so that tampering can be detected, while the record itself stays with its rights-holder, to be produced on demand, by permission, with minimal disclosure.

**But anchoring only settles "not altered", not "still there".** §7's "records outlive their subject" requires a record to outlive the organization and platform that produced it; the Federated design in this section has each organization keep its own memory; **when the holder is gone, anchoring cannot get the content back. Undecided: how a record remains obtainable after its holder is gone.** Three possible paths — designate a successor, place it with a third-party custodian, or keep a publicly obtainable digest in addition to the anchor; the three differ in their effect on minimal disclosure, and one must be chosen with its conditions written out.

**Different memories of the same event are allowed.** A centralized database carries an implicit assumption: "there is only one correct version". But disagreement is the norm: two parties' understandings of the same transaction may both be honest and still not agree. Societal memory should therefore not pretend there is one version, but keep **records from several sources and the disagreements among them**; **no party may be the sole adjudicator of a memory it is party to** — adjudication goes to a dispute process. (**The provider of the dispute process is undecided**, see §8; this section and §8's Due Process both depend on it, and it is the writer of Dispute Memory.)

**Federated societal memory.** CHASI explores a verifiable, authorizable, minimally disclosing Federated Societal Memory: each organization keeps its own memory, and across domains only the necessary part is exchanged, with "what was exchanged" itself leaving a trace. **Undecided: who holds the trace of an exchange**; if either party to the exchange holds it alone, that holder becomes the adjudicator.

**Its relation to the accountability chain.** **§12**'s chain answers **one action**; societal memory answers **what we jointly remember about this class of thing**. The former is vertical (the chain of one action), the latter horizontal (the layer all subjects share). Without the former, memory cannot be checked; without the latter, every action must be proved from scratch.

§9 distinguishes experiment records, accountability-chain records and societal memory. **Evidence Memory in the table above and §12's accountability-chain record are two ways of organising the same data**: the chain organises it vertically around **one action**; Evidence Memory organises it horizontally around **one class of fact**. The other five classes of memory have no corresponding record kind, and **their fields are not yet specified**.

## 14. The Relation Between CHA2A and CHASI

CHA2A and CHASI are two levels. This level answers ownership; the five layers in §10 answer capability composition. They are different kinds of layering.

```

CHASI   Compliance Hub for Agent Society Infrastructure
  │     vision · governance · compliance framework · research and ecosystem connection
  │
  │     interfaces: Identity · Delegation · Federation · Governance
  ↓
CHA2A   Agent-to-Agent / Agent Society Architecture & Protocols

```

The five layers in §10 are **capability layers** (subjects / identity and trust / governance / evidence / interconnection); they answer "which capabilities an action needs in order to hold". This section is a **layering of ownership**; it answers "which document, which protocol is maintained by whom". The two are orthogonal: any one of the five layers may contain products of both CHA2A and CHASI.

**The middle line is not a layer; it is a set of interfaces.** `Identity · Delegation · Federation · Governance` in the middle of the figure are **the agreed names of interfaces between the two sides**: CHASI's governance requirements land, on the CHA2A side, on those four objects. It does not constitute a layer of its own.

**`architecture` appears on both sides and is divided by maintaining party:** CHA2A's architecture specifies protocol objects and messages; L2 in this repository, `governance-architecture`, states CHASI-side principles and constraints and specifies no implementation (see the README index table). **Undecided: whether that distinction holds**; if it does not, one of this section and the README index table has to change.

**Whether CHASI and ComplianceHub.cn are the same entity is undecided.** §11 discusses the Compliance Hub's eight core capabilities, while §5 defines CHASI as a place; they may be two names for one entity, or a place and a portal. **Undecided: the relation between CHASI and ComplianceHub.cn.** Until it is written down, ComplianceHub.cn's duties do not count as CHASI's duties.

**The two sides evolve independently.** CHA2A maintains architecture, protocol, profiles and extensions; CHASI carries vision, governance, compliance framework and research connection. Each side is versioned on its own, and neither blocks the other.

## 15. CHASI and the Existing Ecosystem

§5's "complementary" and §10's "five dispositions" need objects to compare against. The table states **what each object is** and **which disposition describes this family's relation to it**.

This table gives **what the object is** and **the relation**; version, date, adoption evidence, licence, status and review condition are in `method/ecosystem-matrix.md`. **A name without its evidence is not an entry.**

| Object | What it is | Relation to it (§10's five dispositions) |
|---|---|---|
| **A2A** | Agent-to-Agent interoperability | **Adopt + Map** (with **one redefinition**) — §10 states that CHASI defines no communication primitives (A2A exists); the task state machine is aligned to A2A Task and §8 redefines the counterparty's `TASK_STATE_COMPLETED` as **pending acceptance** |
| **MCP** | Agent-to-tool / resource connectivity | **Adopt** — as above |
| **DID / VC** | decentralized identity and verifiable credentials | **Adopt** — §10 already states that CHASI defines no cryptographic primitives and no DID method itself |
| **AAIF** | a body or a specification; its form is unclear | **Undecided** — the object form must first be determined |
| **OpenA2A** | open agent interaction / protocol research | **Undecided** |
| **OAuth / OIDC** | authentication / authorization foundations | **Undecided** — **§10's four denials do not cover authentication / authorization frameworks as a class** |
| **NANDA** | agent Internet discovery, registry and infrastructure research | **Undecided** |
| **MIT / Stanford** | research on the agent Internet, human-agent interaction, memory, identity and society | **Undecided** — a research institution is not an object that can be "adopted" or "mapped" |

**The adoption relation follows from the denials in §10:** CHASI defines no communication primitives (A2A, MCP exist) and no cryptographic primitives or DID method itself (DID, VC exist). A2A also carries a **mapping** (one redefinition in §8), see `method/ecosystem-matrix.md`. The rest are **undecided**: the object is not unclear; what remains undecided is **which disposition applies**. OAuth / OIDC remain undecided because §10's list does not cover authentication / authorization frameworks as a class; AAIF and NANDA because their object forms are unclear.

CHA2A and CHASI are not part of the external ecosystem; they are this family itself. The relation between them is in §14.

**Research institutions and standards bodies are not the same kind of object.** MIT and Stanford produce research, not adoptable specifications; alongside A2A and DID, "adopt" does not apply to them. **Undecided: which word describes the relation to a research institution** — cooperation, borrowing, or merely citation as a source.

## 16. The Long-Term Form

If this works, in ten years it should be a **citable public memory**. Ten years is the vision's **horizon**, not a schedule; this section contains no deliverables or timetable.

§13 specifies six kinds of memory and their writers and read scopes. This section states **whom the memory is for, what it is used for**, and its relation to a society's continuity.

**First, there are two uses, and only these two.**

- so that "**why the people then thought that was allowed**" has a basis;
- so that "how it could be done next time" has a precedent.

**The corresponding non-use: it may not be used to negate past conduct retrospectively.** §3⑤ already provides that judgement falls at the moment the action happened; this is its counterpart here — **the checkability of memory may not be used to retry a judgement that was made under the rules then in force**. To check this, a record must mark "the rule in force then" and "the rule now" separately; §12's "which rule was in force at the time" already requires that.

**Second, "how common interests are held" still lacks conditions and cannot be treated as settled memory content.** §2 states that common interest has no counterpart among §3's seven conditions; settling it requires deciding who holds it, how the holding is made checkable, and how the holder is held responsible. Until those conditions are defined, this document does not claim that common interests will be held.

**Memory is the form in which a society continues.** This is a checkable causal claim: if a society cannot keep its common events, rule changes and dispute outcomes, its next round of decisions has nothing to cite from the last (§13 already states that without it, "every action must be proved from scratch").

**This memory rests on §3's ①, ⑤ and ⑥, not all seven.** ① supplies verifiability, ⑤ supplies "the change has a history", and ⑥ supplies minimal disclosure. ③ exitable, ④ accountable and ⑦ autonomous are conditions for sustained operation; this document does not claim they are also preconditions of memory.

## 17. Boundaries: what this family does not do, and the conditions each would need

The items below are **outside this family's scope**. Each is given with the **conditions it would need** — once they hold, it can be reconsidered; until then, **the basis for not doing it is the condition, not the intention**.

| Not done | The condition it would need |
|---|---|
| **Payment and settlement** | an agent-native settlement path that does not require the counterparty to join some operator's domain |
| **Markets / storefronts / listing** | a distribution layer that "leaves recognition in each party's hands" |
| **Behavioural monitoring · content audit · content compliance** | a disclosure layer that can be assessed without this family taking a position on content |
| **Federation across real registries** | a second real deployment (the online participant list is empty) |
| **A high-grade ecosystem trust state** (one L4 profile, **not** the assembly profile) | ≥2 independent real verifiers, with auditable re-verification (the online L4 instance count is 0) |
| **A run-time proof vocabulary** | the vocabulary slot is reserved, the behaviour undefined — this item differs from the five above: **it is undefined, not undone** |

The conditions are stated with each item. This family's discipline for the public surface is "the public surface states a document's name and status only"; **a name that cannot be obtained is as good as unwritten.**

The six fall into two classes:

| Class | Meaning | Items |
|---|---|---|
| **Undefined** | this family has not yet decided what it is | the run-time proof vocabulary |
| **Condition not met** | this family knows what it is and what is missing | the other five |

None of the six is permanently excluded: each states what condition would let it be reconsidered. **"Not done" describes the present scope; "the condition it would need" describes the basis for changing that scope.** Stating both distinguishes "we do not do this" from "we cannot do this yet".

**Two boundaries need to be distinguished.**

- **"A high-grade ecosystem trust state" is not §11 capability 5.** Capability 5 answers, for **a single subject**, "can it still be relied on now" (revocation, downgrade, suspension, restoration); this item means a **cross-subject ecosystem-level trust state**, which needs ≥2 independent verifiers to hold at all. The former is in scope; the latter is not.
- **"Behavioural monitoring · content compliance" is out of scope** on the condition in the table above: what is disclosed is decided by the declaring party, and this family does only checkability. Until that disclosure layer exists, this family performs no content-related assessment.

## 18. The Status and Constraints of This Document

**Experimental.** This is a vision; it changes as understanding changes. CHASI's specification documents are a separate set, each with its own version and its own way of being judged.

**This document imposes no obligation on any third party.** Its uses of "must" and "must not" occur only in three places, none of which creates such an obligation:

| Where it appears | Who it binds |
|---|---|
| this family's constraints on itself (e.g. §10, "may not dictate how a lower layer is implemented"; the "what it does not do" of each item in §11) | binds this family only |
| descriptions of sustained-operation conditions (§3's seven) | descriptive — if unmet, that society cannot operate sustainably |
| a proposal to society (§8's ten) | binds no one; whether to adopt it is the society's own decision |

The ten clauses in §8 use the form of "should" and "must"; they are a **proposal** and do not create an obligation imposed by this document.

**Where this document conflicts with a specification, the specification governs.** Specifications (the volumes under `architecture/` and `specs/`) state binding "must"; this document states conditions, judgments and proposals. Where the two describe the same thing inconsistently, the specification governs.

This document is a vision under continuing revision: every substantive change raises the version number. **The criterion for "substantive" is that the change alters the meaning of a sentence**; wording, examples and formatting do not count.

**A note of what changed is written only once the version it supersedes has been public.** "Public" means that version was obtainable on some surface with no access restriction on this document. Before that, each version is a pre-publication iteration and carries no change note.

**There is no repository-level changelog**: the version number, plus the change note in the front matter when the condition above is met, is this document's change record.

**Word conventions.** Three usages are easily confused; they are fixed as follows:

- **proper names keep the capital** — `Agent Society`, `Agent Internet`, `Agent Runtime`;
- **as a kind of member, use lower-case `agent`** — one of the four kinds of subject in §1;
- **as a general term, use "subject"**, not `Agent` — §1 distinguishes four kinds of subject: person, organization, agent, group.

## Closing

If CHA2A is our technical exploration of the Agent Internet and the Agent Society, then CHASI can be a larger vision: an open governance hub belonging to no single company, platform or agent runtime.

CHASI does not control agents; its objective is to let autonomy, trust, responsibility and freedom hold at the same time.

The basis for such a society to exist at scale is **verifiability**. Compliance in this document's name refers to that condition (see §5), not to a compliance judgement.

—— CHASI Vision · v2.26
