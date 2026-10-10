# CHASI Vision

**Compliance Hub for Agent Society Infrastructure**

---

> Status: draft v2.22 | Kind: **stance (vision)**
> **This document says *why*, and *where to*. It makes no demand on the reader.** Where it conflicts with a specification, the specification governs.

---

## 0. One Sentence

> **A person need not read the inside of any agent, and need not trust any platform, in order to live and work alongside them —**
> **and to keep, throughout, room to question, to leave, and not to be watched without bound.**
>
> **This is not only a matter between people and agents.** Every relationship among organizations, groups and agents should be checkable by a third party **that belongs to none of them** — rather than booked by one of the parties.
## 1. Membership Is Plural

An agent society is not "a crowd of agents", and it is not "humans and agents". From the Internet to the Agent Internet to Agent Societies, what has increased is never the number of connections, but **which kinds of member have appeared in the society**.

| Position | Who / what | Note |
|---|---|---|
| **Subject** | **Person** | a natural person |
| | **Organization** | companies, institutions, governments, non-profits |
| | **agent** | may act as personal assistant, organizational member, business partner, research partner, social collaborator — **these are its roles, not its kind** |
| | **Group** | temporary, long-lived, cross-organizational; **a family or a community is its smallest form**; it may have rules and a memory of its own |
| **Not a subject** | **Service · tool · resource · data** | they do not belong to the society, but the society uses them — **so they too need names that can be cited, and those names must not be mistaken for subjects** |

**One agent may belong to several organizations and groups at once**, and its role in each may differ. This is the ground the whole vision stands on: **if "belongs to whom" has only one answer, there is no society, only ownership.**

**One kind that has no place here yet.** The four kinds of subject above are peers, but there will be entities that are **both an agent and an organization** — an autonomous entity that is itself a legal person, holding assets, concluding contracts, bearing responsibility and being held to it. This table gives it no place yet. **Undecided: which kind it is** — to be settled by whether its capability set differs from both an organization's and an agent's.

## 2. What Is in This Society

Not "what features will it have", but **the things a society normally has** — **this section is the body of the vision**. The third column gives the condition each one rests on; **the conditions themselves are in §3**, and are only pointed at and supplemented here:

| It has | Meaning | The condition it rests on |
|---|---|---|
| **Roles** | one agent can be assistant, colleague, counterparty and fiduciary at once | **①** — an action must state which role it was performed in |
| **Relationships** | relationships persist, change, break | **①** — the state of a relationship is readable, its termination traceable |
| **Collaboration** | some things one party cannot do alone | **①** — cross-party collaboration leaves a record that can be rebuilt |
| **Exchange** | value moves | **①** — authority and evidence are verifiable; **settlement itself is outside this family's scope, see §17** |
| **Memory** | a society needs continuity | **⑥** — public memory exists, with minimal disclosure |
| **Dispute** | things go wrong | **①④** — the handling rules exist, are declared and are checkable; a person may question |
| **Common interest** | some things belong to no one and matter to everyone | **no condition in §3 yet, see below** |
| **Evolution** | rules change, members come and go | **⑤** — rule changes leave a history |

**Two things are undecided.**

**First, common interest has no condition.** None of the seven in §3 covers it. Settling it requires deciding three things first: who may hold such a thing, how the holding is made checkable, and how the holder is held responsible. The only role in this family that could carry it is **fiduciary**, and the duty of care that role implies is not specified anywhere yet.

**Second, relationships have no object.** The condition requires the state of a relationship to be readable and its termination traceable, but the family has no relationship object: Organization and Group each have a volume, and membership is the closest thing to it, but neither covers a cross-organizational relationship itself. Settling it requires deciding the fields first: the parties, the type, when it takes effect, when it ends, and who may end it.

**One boundary.** Exchange, payment, settlement and listing are outside this family's scope (§17); the authority and evidence an exchange rests on are inside it, and their condition is **①**.

## 3. Seven Conditions That Make It Liveable

**① is necessary, not sufficient.**

| # | Condition | Meaning |
|---|---|---|
| **①** | **Verifiable** | a third party belonging to no one can answer four questions **independently**: **who it is · who authorized it · in what context it is acting · what it has done** |
| **②** | **Coexistable** | societies with different rules can coexist **without first unifying**; recognition is each party's local policy |
| **③** | **Exitable** | a member can leave, and after leaving every right and obligation has a definite destination |
| **④** | **Questionable** | a person keeps the room to question any agent's behaviour |
| **⑤** | **Changeable** | rules can change, **and the change has a history** — judgement falls at the moment the action happened, and is not tried retroactively by later rules |
| **⑥** | **Minimally disclosing** | governance and audit do not require unbounded surveillance; evidence follows minimal necessity |
| **⑦** | **Autonomous** | within its boundaries an agent may act on its own, **without asking at every step** |

**The seven conditions are not one kind of thing, and cannot be treated as seven tests of the same type.**

| Checkable of the system | To be preserved for participants |
|---|---|
| ① verifiable · ⑤ changeable · ⑥ minimally disclosing | ② coexistable · ③ exitable · ④ questionable · ⑦ autonomous |

**Where the four questions come from, and what each answer must contain.** Their normative statement is in the family entry, `overview.md` §1. **The four questions are not by themselves enough to judge** — an answer can exist in form and be useless in fact, so each question also has to say what its answer must contain:

| Question | Its answer must contain | Carried by |
|---|---|---|
| **Who it is** | a resolvable identifier, with a portable trust root — **not established by the party being asked about** | the identity binding; §7, "no central root" |
| **Who authorized it** | the basis of authority, **and the scope** (what may be done, and explicitly what may not) | §12's seven per-link items |
| **In what context it is acting** | **the rule in force at the time** | §4, "time coordinate" |
| **What it has done** | evidence, **and the end of responsibility** (a person or a legal entity) | §12 |

**Two items that used to be listed as separate questions are folded in above.** "How far the scope reached" is part of the answer to the second question; "who bears responsibility" is part of the answer to the fourth. They are not fifth and sixth questions — **treating them as separate questions means judging the same thing twice in two places.**

**① makes actions checkable; ②–⑦ make actions safe to take.** A world with only ① is **auditable but not liveable**: everything can be established after the fact, and nothing can be done with confidence.

## 4. Where It Is Hard

The hard part is not "building another identity protocol": identity, credentials, discovery, narrowing delegation, audit — each of these has people working on it seriously. The hard part is two things.

**First, the seven conditions sit with different people, and no single place is responsible for their holding at once.**

- ① requires **cross-system** — the party asking and the party answering usually do not use the same stack;
- ① requires the answer to come from **a party that belongs to none of them** — while the records that count today are mostly held by the parties themselves;
- ⑤ requires a **time coordinate** — "which rule was in force then" — and today no layer carries this.

These three are **gaps**: not that nobody is working on them, but that nobody is working on them in the same place.

**Second, two imbalances — but they are not a logical conflict between ① and ⑥⑦.**

① asks only that an answer be **possible** — **it contains no timing requirement and does not require recording everything**. The imbalance comes from two default choices at implementation time:

| Which way the default falls | What it becomes in implementation | Which condition it breaks |
|---|---|---|
| Verification placed **before action** | every step asks permission first | ⑦ autonomous |
| Verifiability implemented as **recording everything** | governance degrades into total surveillance | ⑥ minimally disclosing |

**So the form of the criterion here is "a default, plus a declaration when departing from it", not "choose one of the two":** first set the default position of verification and the default extent of recording; departing from the default must be justified by the party that declares it. The specific defaults are undecided.

**It has to be checkable.** Each imbalance needs a checkable form of "both hold at once", or there is no way to tell whether it has been resolved. §12 supplies one form for ①×⑦ — **an incomplete chain must be reportable** (verification need not intercept before the action, but must be able to point out afterwards which link is missing). There is no corresponding form for ①×⑥ yet.

**One unlisted relation (undecided).** ② (societies with different rules coexist, without first unifying) together with ⑤ (rules change, judgement falls at the moment the action happened) produces a **cross-society time skew**: which party's then-effective rule governs depends on whom you ask. Settling it requires deciding how cross-society rule changes take effect and are registered.

## 5. What CHASI Is

**A place.** It assembles parts from different sources, uses **experiments it designs and runs itself** to test whether those seven conditions can hold at the same time, and publishes each result as a record.

**What "test" means has to be said precisely: CHASI runs its own experiments; it does not pass judgement on anyone else's system.** What it records is "under this combination, which condition failed, and at which step of which part". Whether a given party is compliant, **judgement is left to each verifier** (§7) — hence it issues no certification, gives no ratings, sets no entry threshold (§6), and is not the final enforcer of any arbitration (§10).

- It **does not define mechanisms** — "how to identify an agent", "how to discover", "how to narrow a delegation" each have their own owners;
- what it **does specify** are **the conditions of a composition** — whose parts are used, and what that composition must satisfy. **Anyone who does not adopt that composition is not bound by it**;
- its output is **findings and records**.

**The first two items above once looked contradictory; here is their relation.** "Specifies" and "is not rules" do not conflict, because what CHASI puts forward are **conditions**, not **obligations**: it sets conditions on "a path assembled from these parts", and makes no demand of anyone who does not adopt that composition. The two capabilities in §11, "identity and resolution" and "discovery and directory", stand in the same place — **CHASI does not specify how to do it, only what the result must satisfy**.

**Its three attitudes to the existing ecosystem must all hold.** Each has a different degree of checkability; stated one by one:

- **Compatible** — reuse what can be reused directly; do not re-invent the whole Agent Internet. **Its checkable form is in §10**: for any external capability, ask in order — Adopt → Map → Profile-Extend → Adapter → Define; only when all four answers are no may we define our own.
- **Complementary** — fill only the gaps the ecosystem leaves in cross-organizational identity, authority, governance, evidence and accountability. **No criterion yet**: settling it requires being able to list which capabilities are already mature — the list in §15 currently has only names, with no version, date or adoption evidence.
- **Independent** — attach to no single vendor, no single runtime, no single identity system. **No criterion yet**: settling it requires deciding how "attachment" is judged (for example, whether the family's specifications remain readable and implementable after any one party is swapped out).

When all three hold, CHASI need not compete with anyone over "who defines the whole Agent Internet". But this is **not a deduction from the three**: the non-competition follows from **complementary** (filling only gaps) and **independent** (attaching to nothing), not from **compatible**; and standards bodies, open-source foundations and research institutions are not the same kind of object in that sentence — the first two define specifications that can be adopted, the third produces research, and their competitive relation to CHASI differs.

**The formal reading of the name.** CHASI = Compliance Hub for Agent **Society** Infrastructure; the last three letters come from **Society** (a noun, naming the society of agents) and **Infrastructure**. **Other readings (such as reading SI as Social Infrastructure, or as Super Intelligence) appear in no judgement this family makes**, and are not developed here.

**What "Compliance" means in this document has to be said precisely.** This family makes no compliance judgements — capabilities 6, 7 and 8 in §11 respectively block "judging compliance", "judging attainment" and "judging qualification". So Compliance in the name **does not mean "checking whether someone else complies", but "the conditions required for verifiability to hold"** (§3①): records that are complete and can be checked by a third party belonging to none of the parties. **Undecided: whether the word should be replaced with one free of the "inspection" ambiguity** — as it stands the name is easily read as a regulator.

## 6. What It Is Not

- not another agent protocol — it defines no mechanism for communication, identity, discovery or narrowing delegation; those have their own owners (§5);
- not a standards body — it does not vote, does not ballot, sets no entry threshold;
- not a platform — it runs no registry, encloses no network effect, sells no SKU;
- not a regulator, and it claims no regulatory territory; not the final enforcer of any arbitration (§10).

**Three of these four denials need their boundary stated, or they collide with §11.**

**First, it carries state, and therefore necessarily holds a directory.** Capabilities 1, 5 and 8 in §11 require it to resolve subjects, answer current status, and let entries be found — the vehicle for all three is a directory. **Directory and registry must be kept apart: a directory holds declarations, a registry settles facts. CHASI does only the former**; what this section denies is the latter.

**Second, "no entry threshold" and "let entries be found" do not conflict, because their subjects differ.** CHASI does not judge who qualifies (judgement is left to the verifier, §7); it only lets entries that **declare against a profile and attest to themselves** be found, and the verifier judges for itself whether an entry meets its own requirements. **So there is no threshold, but there are profiles** — the threshold is set by the verifier, not by CHASI.

**Third, a profile is a condition, not a licence.** The same distinction as in §5: a profile constrains "a path assembled from these parts", and does not constrain anyone who does not adopt it.

**Its only possession is credibility**, and credibility accumulates only by records being accurate. For that sentence to be checkable, at least one more thing must be specified: **when a published record is found to be wrong, how it is corrected, by whom, and how the correction itself is recorded.** There is currently no correction mechanism anywhere — §7's "downgrades must be visible" concerns the status of a subject, not a published record. **Undecided: the correction rule; settling it requires deciding who has standing to challenge a published conclusion.**

**This family's own responsible entity is not yet written down.** §12 requires the end of responsibility to be a person or a legal entity; this section and the document as a whole impose that requirement on every subject, but **do not say which legal entity is responsible for the records CHASI itself publishes**. A record published by CHASI and later shown to be wrong needs a party that can be held to account. **Undecided: this family's own responsible entity.**

## 7. CHASI's Own Positions

This section is **CHASI's choices as a place** — not commands to members, and not "what an agent society ought to have".

| Position | Why | Therefore CHASI must |
|---|---|---|
| **No central root** | cross-domain trust cannot be established by any party's registry; the trust anchor is the one the verifier configures itself | **this family's own directory is not a trust root either** — the status it provides is an input, not an anchor; replacing this family's directory, a verifier should still be able to judge by the anchor it configured itself (§11 capability 5) |
| **No mutual recognition required** | recognition is each party's local policy; if it can be translated, it need not be agreed in advance | supply the **mapping** (§10's Map), and state **who maintains it and how its version is marked**; otherwise "can be translated" never lands |
| **Facts, not ratings** | record facts; judgement is left to each verifier. Issuing a rating would make the issuer a party to the trust judgement | no conclusive rating by this family appears in a record. §11 capability 7's "profiles and grading" **declares what must be met**, it does **not judge who has met it** |
| **Records outlive their subject** | a record must be able to outlive the organization and platform that produced it; otherwise it is a log, not evidence | see below — this is in tension with the design in §13, and is unresolved |
| **Downgrades must be visible** | a silent downgrade is a deception | a status transition must leave a trace, and be **visible to every party that relies on that status**; "visible" needs defining: who, within what time, by what route |
| **Presuppose no system** | otherwise this place is only the entrance hall of one ecosystem | no identity system or runtime may be made a precondition of taking part |
| **Autonomy is not an exception** | autonomy within boundaries is the norm; a system that must ask at every step is a tool, not a member | **"asking at every step" may not be used as the means of satisfying verifiability**; verification defaults to after the fact or to sampling, and departing from that default must be justified by the declaring party (§4) |
| **People keep room to question** | an agent's autonomy does not cancel a person's questioning; but questioning is not unbounded surveillance | **a record published by this family must let a third party belonging to none of the parties answer "who did it, on what authority"**; a record may not be visible only to the parties |

**The last two restate the conditions in §3; they are not repeated here — only what they require of this family.** §3④ and §3⑦ say what a society needs in order to be liveable; this table says what CHASI must therefore do. **Each "therefore" entry gives a checkable landing point.**

**One unresolved tension: records outlive their subject × each organization keeps its own memory.**

The fourth row above requires that "a record be able to outlive the organization and platform that produced it"; the design in §13 is Federated — **each organization keeps its own memory**, only the necessary part is exchanged across domains, and records are **anchored rather than on-chained**. The two conflict on **availability**: if a record exists only with the organization that produced it, the organization disappears and the record disappears with it; **anchoring can prove "it was not altered", it cannot guarantee "it is still there".**

**Undecided: how a record remains obtainable after its holder is gone.** Settling it requires choosing among three paths and stating the conditions — designate a successor, place it with a third-party custodian, or keep a publicly obtainable digest in addition to the anchor. The three differ in their effect on minimal disclosure.

(For the proposal on "what an agent society ought to have", see the next section.)

## 8. Constitutional Principles for an Agent Society (a proposal)

If the Agent Society becomes a new social form, then besides protocols it needs a set of clauses something like a constitution. This section puts forward one, provisionally called the **CHASI Agent Society Constitutional Principles**.

**First, the relation of this section to §3 and §7, or the three tables will be read as three sets of requirements.**

| Section | What it is | Who it binds |
|---|---|---|
| §3, the seven conditions | the properties a society needs in order to be liveable | descriptive — not met, and it is not liveable |
| §7, CHASI's own positions | this place's own choices | binds this family only |
| **§8, this section** | which clauses a constitution would at least have to contain | **binds no one** — whether to adopt them is the society's own decision |

**Hence this section is written in conditional form, not in commands.** §6 has stated that CHASI is not a standards body and sets no entry threshold; this section has neither the power nor the intention to impose it on anyone. The clauses below may be used as they stand, rewritten, or used only in part.

**Of the ten clauses, those that repeat existing sections are pointed at, not restated:**

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
| **Human Primacy** | where a person's fundamental interests are at stake, human control is retained | §7, "people keep room to question". **Undecided**: which interests count as "fundamental", and who judges |

**Only three of these are genuinely new** — Proportionality, Due Process, Human Primacy. The other seven are already covered by §3, §7 or §11. The value of this section lies in putting forward those three, not in restating the seven.

**"Minimal" needs care.** On the table above, removing the seven repeats leaves three; but "minimal" needs a criterion to hold — **undecided: which clause cannot be removed next, and on what basis that is judged**. Until then this section should not call itself minimal.

**The wording throughout is "subject", not "Agent".** §1 distinguishes four kinds of subject — person, organization, agent, group; if these clauses bound only agents, then organizations — equally capable of being authorized and of being held responsible — would fall outside the constitution.

## 9. How It Works

**Learn → Assemble → Test → Record → Publish.**

| Step | What it does |
|---|---|
| **Learn** | whatever is good and has been done by others, **learn it actively**, respecting intellectual property. Do not go looking for original technology of our own |
| **Assemble** | assemble parts from different sources into a path that can satisfy the seven conditions |
| **Test** | run real scenarios and record **which condition fails, and at which step of which part** |
| **Record** | each result becomes one record (content below) |
| **Publish** | publish the findings so that others can cite them (requirements below) |

**This section is only a summary; the method is a separate document.** The six stages of an experiment — Scenario → Experiment → Observation → Architecture → Specification → **Re-test** — are written in `method/use-case-laboratory.md` §2. The five steps above contain **no Re-test**: the table says "how one piece of work proceeds", that document describes **a loop**. The two descriptions are meant to be read together, and its six stages are not repeated here.

**"Record" means at least three different things across this document; this section defines only the first.**

| Where | What is recorded | Who writes | What governs the content |
|---|---|---|---|
| **§9, this section's "Record"** | the finding of one experiment | this family | the four items below |
| §12, the accountability chain | the derivation of authority for one action | the acting party | §12's seven per-link items |
| §13, societal memory | facts the society jointly holds | varies by memory class | §13's six classes |

When §6 says "credibility accumulates only by records being accurate", it means **the first**. Four items:

- **version** — state **which part, at which version**, not just "version";
- **date**;
- **conclusion** — which conditions held, which did not;
- **review condition** — not "when to review", but **what condition, once it occurs, requires a review** (for example, a part it rests on being version-bumped).

**"Publish" must state what is needed for a record to be citable**, or §16's "a citable public memory" cannot hold:

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

**The architecture has five layers, each answering one question.** (The figure and the table are the same thing: the figure arranges them by layer, the table adds what else each layer contains.)

| Layer | The question it answers | What else is in it |
|---|---|---|
| Subjects | who is present | Human · Organization · agent · Group |
| Identity and trust | who it is; whether it can still be relied on | and it handles **non-subject resources that need to be referred to**: service · tool · data — **they may be named, they may not be treated as subjects** |
| Governance | who has authority, under which rules, and may delegate to whom | |
| Evidence | on what basis this happened, and whose responsibility it is | |
| Interconnection | how it composes with existing protocols, runtimes and identity systems | A2A · MCP · DID/VC · OAuth |

**Dependency runs one way, but this has to be stated precisely.** An upper layer **may** require a lower one to provide some capability — the governance layer requires the identity layer to resolve subjects; an upper layer **may not** dictate how a lower one is implemented — the governance layer does not dictate which cryptography the identity layer uses, and the evidence layer does not dictate what organizational form the governance layer takes. The purpose is to let **every layer be replaceable**; the family's `governance-architecture`, declaring of itself that it "states no requirements", is the strict version of the same thing.

**Persons are not the only origin of authority.** The figure draws authority downward from the subject layer, but a subject's authority may come from its own founding instrument rather than from anyone's consent: §12 states that the chain ends at "**a person, an organization, a definite legal entity**"; L3's `organization-governance` decomposes authority into four layers — "charter → office → holder → root authority basis". The figure does not mean "all authority originates from persons".

**What CHASI does not own.**

- it does not define communication primitives — A2A and MCP exist;
- it does not define cryptographic primitives, nor any DID method itself — DID and VC exist;
- it builds no agent runtime, no model, no workflow engine;
- it is not a regulator, and not the final enforcer of any arbitration.

**"Does not define a DID method" has to say who does not define it.** This family has a DID method (`did-method-cha2a`); it is a product of **CHA2A**, not of the CHASI architecture layer (§14 gives the two levels). What this section says is that **the architecture layer does not define it** — not that this family does not build one.

**Scope boundary: "domain" must be defined first, or this boundary cannot be judged.** CHASI has exactly one territory — **the stretch that crosses subjects and crosses domains**; what happens inside a domain stays inside it, and how an organization divides work or audits itself is not for CHASI to specify — CHASI asks only that it be able to say clearly what it did **when it steps outside**. But the document nowhere defines "domain". This matters, because **the domain is the criterion for whether CHASI applies at all** — a subject that can simply declare "this is a domain" could sidestep the requirements of this section. **Undecided: the basis for judging a domain** (who declares it, whether the declaration needs to be recognized by others, whether different subjects are by themselves sufficient for "cross-domain").

**There are five dispositions of an external capability, and no sixth.** Adopt → Map → Profile-Extend → Adapter → Define. Any existing capability that comes before CHASI is asked, in order: can it simply be adopted? If not, can it be mapped? If not, can it be extended within that capability's own profile? If not, can an adapter be added? Only when all four answers are no do we define our own. **That ordered questioning is what makes "reuse as far as possible" executable** — otherwise "compatible" degrades into a slogan anyone can claim.

**These five dispositions are a decision procedure, and therefore need a decision record.** Which of the four questions was asked, and where the conclusion landed, should be checkable; otherwise there is no telling whether "define our own" was necessary or merely convenient. **Undecided: who makes the decision, and where it is recorded** — and which of §9's three record classes it belongs with.

**Composition, not replacement.** What is missing today is not agents that can talk to each other, but the layer that keeps "who authorized what, on what basis, and who answers for the result" verifiable when those agents belong to different organizations and different trust domains. The whole architectural value of CHASI comes down to this sentence: it produces no new intelligence, it produces **cross-domain verifiability**.

## 11. The Eight Core Capabilities of the Compliance Hub

These eight are not eight small features but **eight links in one chain**: from "who you are" to "you can be found".

**First, what kind of thing these eight are.** They are **conditions of a composition**, not mechanism definitions (§5): this family does not specify "how to identify an agent" or "how to discover"; it specifies **what a path assembled from these parts must satisfy**. Each row below therefore gives both "what it does" and "what it does not do".

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

**Three ways to read it.**

**First, the eight have dependencies, but not every one depends on the one before.** The real dependencies are in the first four: without identity there is no organization to speak of; without organization and authority, group collaboration has no subject. **The last four are not like that** — a profile does not need evidence in order to exist, and a directory does not need profiles. **The first four are preconditions of the last four, and the last four do not precede one another**; reading the eight as a straight line also reads confusingly against §6's "no entry threshold".

**Second, each one must land on a document that can be reviewed.** If a capability lives only in a product and not in a specification, no one else can implement it, and no one can tell whether they comply — then it is not a capability, it is a **service**. The line between capability and specification is exactly the line between whether this Hub can be called infrastructure. **This also gives capability 6 its landing point**: the conformance vectors and checkers are in L5 (`cha2a-conformance`, 68 vectors, dual-verifier interlock; L5 lives in the companion repository, see the README index table); the table says the Hub can produce results, not that this family defines conformance here.

**Third, all eight must have a "what it does not do".** The third column matters as much as the second: **half of a Hub's definition comes from what it refuses to do.** The most important entries in that column are capabilities 6, 7 and 8 — they block "judging compliance", "judging attainment" and "judging qualification" respectively; do those three and this family becomes a regulator, which §6 has stated it is not.

## 12. Causal Accountability Chain

One of CHASI's most important original lines of research is turning **action by a subject** from "black-box execution" into a verifiable causal accountability chain.

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

Each arrow in the figure is a kind of **delegation**; the seven items below are what **each link** must carry — two views of one thing: the figure gives the shape of the chain, the fields give its checkable conditions.

What it must finally answer is not only "what happened", but "why it happened, who authorized it, what the scope of that authority was, whether it was exceeded, and who bears responsibility".

**First, what "causal" adds over a log.** Three things are often conflated; the difference is decisive:

| | The question it answers | Its nature |
|---|---|---|
| Call trace | who called whom, how long it took, where it failed | technical fact |
| Audit trail | what happened | fact of what occurred |
| **Causal accountability chain** | **on what basis this could happen, who had the authority to let it happen, whether the boundary was crossed** | **derivation of justification** |

An audit log records **the order of events**; an accountability chain records **the derivation between authority and action**. The former can tell you "Agent B initiated a transfer at 14:03"; the latter must be able to tell you "Agent B could initiate it because A obtained authority over scope R from the organization, and delegated a subset of R to B, and this call did not exceed that subset".

**What every link must carry** (without which the link does not hold):

- **subject** — who;
- **basis of authority** — whose power, of what kind. **This is not a self-declaration**: it must be traceable to its origin along the four-layer decomposition in L3 `organization-governance` §2 (charter → office → holder → root authority basis), see §10;
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

**How autonomy and responsibility are reconciled is precisely through the scope item.** §3⑦ allows an agent to act autonomously within its boundaries, **without asking at every step**; this section requires the end of responsibility to fall on a person or legal entity. The condition under which both hold is: **scope is given by the principal, within scope the agent is autonomous, and outside scope there is no authority** — so what the principal bears is "the scope it drew", not "the actions it approved one by one". **Undecided: the default when a link does not state its scope** — treated as "no authority" (conservative) or as "the same as the parent" (permissive). This family's practice elsewhere is conservative (§6, "does not treat registered as trustworthy", and §12's scope comparison both depend on it), but this section does not state it.

**What is verifiable, and what can only be declared.** Scope of authority, time, revocation status, delegation depth — verifiable. Intention, good faith, "I did my best" — declarable only. Conflating the two is the commonest failure of accountability chains: **a declaration taken for a proof**. This family's approach is to **list the verifiable part and give a checking method for each item**, and to **mark the rest explicitly as declaration** — never to dress a declaration up as proof through visualisation. **Undecided: the criterion for "minimally sufficient"** — how small the verifiable part can be, and what it must still cover, so as neither to over-record (§3⑥) nor to under-support judgement.

**The end of responsibility must be a person or a legal entity, not "the system".** Automation may lengthen the chain of action, but it does not change where responsibility lies: the chain must end at a subject capable of bearing responsibility — a person, an organization, a definite legal entity. **If the only way to write the end of a chain is "the model decided on its own", then responsibility has not disappeared; the chain is missing a link** (the first kind of failure above). **Undecided: when the chain crosses outside this family's scope** (the counterparty does not recognize the form of authority), where the end falls.

## 13. Societal Memory: the public memory of an Agent Society

Agent Memory is personal memory; Societal Memory is shared memory. **They are not "one scaled up"; they serve different subjects**: personal memory serves "I remember what I did", societal memory serves "**what we jointly hold to have happened, under which rules, and why those rules later changed**".

A mature Agent Society needs to keep six kinds of memory, and the **writer and readers** of each are as follows (**retention** is discussed below):

| Memory | Content | Who writes | Who reads |
|---|---|---|---|
| Event Memory | what happened | the parties | those connected to the event |
| Decision Memory | why this decision was made | the deciding subject | those affected by it |
| Commitment Memory | who promised what | the promiser | the promisee |
| Policy Memory | when and why a rule changed | whoever may change the rule | those bound by it |
| Evidence Memory | what an action rested on | the acting party | whoever needs to verify |
| Dispute Memory | how a dispute arose and was resolved | **the dispute process** (provider undecided, see §8) | the parties and overseers |

**Retention is not specified.** The document gives no retention period anywhere. This is not a matter of wording: §7's "records outlive their subject" requires a record to outlive its subject, and "how long" is exactly the step where that requirement has to become a number. **Undecided: the retention period of each of the six, and who decides what happens at expiry** (delete, archive, or withdraw obtainability while keeping verifiability).

**"Verifiable" and "obtainable" are two things, and must be specified separately.**

- **must be verifiable** — it can be checked that it was not altered;
- **must be obtainable** — the content can be read.

The "who reads" column above is about **obtainability**, not verifiability. The two can diverge: a record can be unobtainable to most and verifiable to all. Therefore:

- **every class of memory must be verifiable**, without exception;
- **the extent of obtainability is specified class by class in the table above**, and must state **who authorizes obtaining it** (the table gives "who reads", not "who approves").

**Undecided: who authorizes obtaining it.** This section, §8's Due Process and §11 capability 1 all assume an authorizing role exists, and the document nowhere says so.

**Verifiable memory is not blockchain.** Blockchain settles "order and immutability", at the price of full replication and full publicity. What societal memory actually needs is three things — **verifiable, controllably disclosed, forgettable** — and blockchain gives only the first half, and is of no help exactly where it is hardest (**who deletes, and by whose rules**). The direction is therefore **anchoring rather than on-chaining**: anchor "the state of a record at a moment" in a public place, so that tampering can be detected, while the record itself stays with its rights-holder, to be produced on demand, by permission, with minimal disclosure.

**But anchoring only settles "not altered", not "still there".** §7's "records outlive their subject" requires a record to outlive the organization and platform that produced it; the Federated design in this section has each organization keep its own memory; **when the holder is gone, anchoring cannot get the content back. Undecided: how a record remains obtainable after its holder is gone.** Three possible paths — designate a successor, place it with a third-party custodian, or keep a publicly obtainable digest in addition to the anchor; the three differ in their effect on minimal disclosure, and one must be chosen with its conditions written out.

**Different memories of the same event are allowed.** A centralized database carries an implicit assumption: "there is only one correct version". But disagreement is the norm: two parties' understandings of the same transaction may both be honest and still not agree. Societal memory should therefore not pretend there is one version, but keep **records from several sources and the disagreements among them**; **no party may be the sole adjudicator of a memory it is party to** — adjudication goes to a dispute process. (**The provider of the dispute process is undecided**, see §8; this section and §8's Due Process both depend on it, and it is the writer of Dispute Memory.)

**Federated, not central.** CHASI's direction is not to build a centralized "all-knowing database" but to explore a verifiable, authorizable, minimally disclosing Federated Societal Memory: each organization keeps its own memory, and across domains only the necessary part is exchanged, with "what was exchanged" itself leaving a trace. **Undecided: who holds the trace of an exchange** — if either party to the exchange holds it alone, the problem returns to "the holder is the adjudicator".

**Its relation to the accountability chain.** **§12**'s chain answers **one action**; societal memory answers **what we jointly remember about this class of thing**. The former is vertical (the chain of one action), the latter horizontal (the layer all subjects share). Without the former, memory cannot be checked; without the latter, every action must be proved from scratch.

**The relation between "memory" and §9's three kinds of "record" has to be stated.** §9 distinguishes three: experiment records, accountability-chain records, and societal memory. **Evidence Memory in the table above and §12's accountability chain are two views of the same data**: the chain looks at it vertically, **one action** at a time; Evidence Memory looks at it horizontally, **one class of fact** at a time. The other five classes of memory have no corresponding "record" kind, and **their fields are not yet specified**.

## 14. The Relation Between CHA2A and CHASI

CHA2A and CHASI are two levels. This section gives the division, and states that it is **not the same kind of layering as the five layers in §10**.

```

CHASI   Compliance Hub for Agent Society Infrastructure
  │     stance · governance · compliance framework · research and ecosystem connection
  │
  │     interfaces: Identity · Delegation · Federation · Governance
  ↓
CHA2A   Agent-to-Agent / Agent Society Architecture & Protocols

```

**Two senses of "layer" must be kept apart.** The five layers in §10 are **a layering of the architecture** (subjects / identity and trust / governance / evidence / interconnection); they say "which capabilities an action needs in order to hold". The levels in this section are **a layering of ownership**; they say "which document, which protocol is maintained by whom". The two are orthogonal — any one of the five layers may contain products of both CHA2A and CHASI. When §10 points here at its end, it means the latter.

**The middle line is not a layer; it is a set of interfaces.** `Identity · Delegation · Federation · Governance` in the middle of the figure are **the agreed names of interfaces between the two sides**: CHASI's governance requirements land, on the CHA2A side, on those four objects. It does not constitute a layer of its own.

**The division of ownership conflicts with an existing fact, and this has to be dealt with.** This section assigns **architecture** to CHA2A; but L2 in this repository *is* architecture (`governance-architecture`, see the index table in the README), and it says "why this family is layered as it is" and requires nothing of anyone. Only one explanation lets both stand: **`governance-architecture` is the architecture on the stance side of this family (principles and constraints), while CHA2A's architecture is the architecture on the protocol side (objects and messages)**. The wording of this section should be revised accordingly, or readers will think L2 in this repository is misfiled. **Undecided: whether that distinction holds** — if it does not, then one of this section and the README index table has to change.

**The relation between CHASI and ComplianceHub.cn has to be written down.** This section's last sentence mentions ComplianceHub.cn; §11 is titled "the eight core capabilities of the Compliance Hub"; and §5 defines CHASI as "a place". The three do not say whether they are one thing or two. **Undecided: the relation between CHASI and ComplianceHub.cn** (two names for one entity, or "a place" and "a portal" as two things). Until it is written down, this document does not count ComplianceHub.cn's duties as CHASI's duties.

**Keeping the technical work independent is the substantive aim of this section.** The CHA2A side continues to evolve architecture, protocol, profiles and extensions independently; the CHASI side carries stance, governance, compliance framework and research connection. Each side is versioned on its own, and neither blocks the other.

## 15. CHASI and the Existing Ecosystem

**The purpose of this section is to give §5's "complementary" and §10's "five dispositions" objects to compare against.** Each entry therefore has to state two things: **what the object is**, and **which disposition describes this family's relation to it**.

**First, the format: a name without its evidence is not an entry.** Elsewhere this family requires **version · date · adoption evidence** for a citation; this family's "ecosystem matrix" has fixed the columns — **object · version · date · adoption evidence · licence · status (institutional / individual draft / community project) · review date**. The table below currently has **only the object and a one-line description**; the other six columns are all empty. **So this section cannot yet support the judgement of "complementary"**, which is exactly why §5 says "no criterion yet".

| Object | What it is | Relation to it (§10's five dispositions) |
|---|---|---|
| **A2A** | Agent-to-Agent interoperability | **Adopt** — §10 already states that CHASI defines no communication primitives; A2A exists |
| **MCP** | Agent-to-tool / resource connectivity | **Adopt** — as above |
| **DID / VC** | decentralized identity and verifiable credentials | **Adopt** — §10 already states that CHASI defines no cryptographic primitives and no DID method itself |
| **AAIF** | the earlier table listed it alongside A2A, without describing it separately | **Undecided** — it must first be stated whether it is a body or a specification |
| **OpenA2A** | open agent interaction / protocol research | **Undecided** |
| **OAuth / OIDC** | authentication / authorization foundations | **Undecided** — **§10's four denials do not cover authentication / authorization frameworks as a class** |
| **NANDA** | agent Internet discovery, registry and infrastructure research | **Undecided** |
| **MIT / Stanford** | research on the agent Internet, human-agent interaction, memory, identity and society | **Undecided** — a research institution is not an object that can be "adopted" or "mapped" |

**The three "adopt" entries are read directly off the denials already written in §10**: §10 says CHASI defines no communication primitives (A2A, MCP exist) and no cryptographic primitives or DID method itself (DID, VC exist), so the relation to those objects can only be "adopt". The rest are **undecided**: not because the object is unclear, but because **which disposition applies is unclear** — settling it requires filling in the six evidence columns above.

**CHA2A and CHASI have been moved out of this table.** They are not "the existing ecosystem", they are this family itself, and the relation between them is written in §14. The earlier table listed them at the end, which matched neither this section's title nor §14.

**Research institutions and standards bodies are not the same kind of object.** MIT and Stanford produce research, not adoptable specifications; listing them in the same column as A2A and DID suggests "adopt" applies to them too. **Undecided: which word describes the relation to a research institution** — cooperation, borrowing, or merely citation as a source.

## 16. The Long-Term Form

If this works, in ten years it should be a **citable public memory**. This is the only time reference in the whole document; it is a **horizon**, not a schedule — this section contains no deliverables and no timetable.

**What is recorded is already written in §13**: six kinds of memory, each with its writer and readers. This section adds only the two things §13 does not say — **whom this memory is for and what it is used for**, and **its relation to a society's continuity**.

**First, there are two uses, and only these two.**

- so that "**why the people then thought that was allowed**" has a basis;
- so that "how it could be done next time" has a precedent.

**The corresponding non-use: it may not be used to negate past conduct retrospectively.** §3⑤ already provides that judgement falls at the moment the action happened; this is its counterpart here — **the checkability of memory may not be used to retry a judgement that was made under the rules then in force**. To check this, a record must mark "the rule in force then" and "the rule now" separately; §12's "which rule was in force at the time" already requires that.

**Second, "how common interests are held" is marked in §2 as having no condition, and this section no longer treats it as settled memory content.** §2 states that common interest has no counterpart among §3's seven conditions; settling it requires deciding who holds it, how the holding is made checkable, and how the holder is held responsible. Until that is decided, this section does not claim it will be held.

**Memory is the form in which a society continues.** The content of that sentence is a checkable causal claim: if a society cannot keep its common events, rule changes and dispute outcomes, its next round of decisions has nothing to cite from the last (§13 already states that without it, "every action must be proved from scratch").

**This memory rests on three of §3's conditions — ①, ⑤ and ⑥ — not all seven.** ① supplies verifiability, ⑤ supplies "the change has a history", ⑥ supplies minimal disclosure; those are the three that §13 actually invokes throughout. **And ③ exitable, ④ questionable and ⑦ autonomous are conditions for a society to be liveable; this section has no basis for saying they are also preconditions of memory.**

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

**These conditions are written inside this section and point outward to nothing.** This family's discipline for the public surface is "the public surface states a document's name and status only"; **a name readers cannot obtain is as good as unwritten.**

**The six fall into two classes, and the title is revised accordingly.**

| Class | Meaning | Items |
|---|---|---|
| **Undefined** | this family has not yet decided what it is | the run-time proof vocabulary |
| **Condition not met** | this family knows what it is and what is missing | the other five |

**The earlier title, "what we explicitly do not do", was only half right.** None of the six is "we do not intend to" — each states what condition would let it be done. **"Not done" describes the present scope; "the condition it would need" describes the basis for changing that scope.** Both have to be written, or readers cannot tell "we do not do this" from "we cannot do this yet".

**Two items are easily confused with existing sections, and are stated separately.**

- **"A high-grade ecosystem trust state" is not §11 capability 5.** Capability 5 answers, for **a single subject**, "can it still be relied on now" (revocation, downgrade, suspension, restoration); this item means a **cross-subject ecosystem-level trust state**, which needs ≥2 independent verifiers to hold at all. The former is in scope; the latter is not.
- **"Behavioural monitoring · content compliance" is out of scope** on the condition in the table above: what is disclosed is decided by the declaring party, and this family does only checkability. Until that disclosure layer exists, this family performs no content-related assessment.

## 18. The Status of This Document, and Its Own Rules

**Experimental.** This is a stance (vision); it changes as understanding changes. CHASI's specification documents are a separate set, each with its own version and its own way of being judged.

**This document makes no demand on the reader.** This has to be stated precisely, because the document contains many "must" and "must not" (`必须` appears 30 times, `不得` 11 times). They fall into three classes, **none of which is a demand on the reader**:

| Where it appears | Who it binds |
|---|---|
| this family's constraints on itself (e.g. §10, "may not dictate how a lower layer is implemented"; the "what it does not do" of each item in §11) | binds this family only |
| descriptions of liveability conditions (§3's seven) | descriptive — not met, and that society is not liveable |
| a proposal to society (§8's ten) | binds no one; whether to adopt it is the society's own decision |

The ten clauses in §8 read like commands in form ("should have", "must"), **which is the natural form of a constitutional clause**; they are a **proposal**, not an obligation this document imposes.

**Where this document conflicts with a specification, the specification governs.** How that is judged: **a specification (the volumes under `architecture/` and `specs/`) says "must"; this document states conditions, positions and proposals**; where the two describe the same thing inconsistently, the specification governs.

**It is living**: a position may be revised, the trace may not — so every substantive change raises the version number. **The criterion for "substantive" is that the change alters the meaning of a sentence**; wording, examples and formatting do not count.

**A note of what changed is written only once the version it supersedes has been public.** "Public" means that version was obtainable on some surface with no access restriction on this document. Before that, each version is a pre-publication iteration and carries no change note.

**There is no repository-level changelog**: the version number, plus the change note in the front matter when the condition above is met, is this document's change record.

**Word conventions.** Three usages are easily confused; they are fixed as follows:

- **proper names keep the capital** — `Agent Society`, `Agent Internet`, `Agent Runtime`;
- **as a kind of member, use lower-case `agent`** — one of the five member kinds in §1;
- **as a general term, use "subject"**, not `Agent` — §1 distinguishes four kinds of subject: person, organization, agent, group.

## Closing

If CHA2A is our technical exploration of the Agent Internet and the Agent Society, then CHASI can be a larger vision: an open governance hub belonging to no single company, platform or agent runtime.

It is not there to control agents, but so that autonomy, trust, responsibility and freedom can exist at the same time.

In that sense, what lets such a society exist at scale is not a restriction on agents but **verifiability** — which is what Compliance in this document's name refers to (see §5), not a compliance judgement.

—— CHASI Vision · v2.22
