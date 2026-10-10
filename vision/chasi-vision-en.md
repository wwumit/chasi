# CHASI Vision

**Compliance Hub for Agent Society Infrastructure**

---

> Status: draft v2.5 | Kind: **stance (vision)**
> **This document says *why*, and *where to*. It requires nothing of anyone.** Where it conflicts with a specification, the specification governs.

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
| | **Agent** | may act as personal assistant, organizational member, business partner, research partner, social collaborator — **these are its roles, not its kind** |
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

**Verifiability is the first, not the whole.**

| # | Condition | Meaning |
|---|---|---|
| **①** | **Verifiable** | a third party belonging to no one can answer: on whose behalf was it done · on what authority · which rule was in force at the time · who answers if it goes wrong |
| **②** | **Coexistable** | societies with different rules can coexist **without first unifying**; recognition is each party's local policy |
| **③** | **Exitable** | a member can leave, and after leaving every right and obligation has a definite destination |
| **④** | **Questionable** | a person keeps the right to question any agent's behaviour |
| **⑤** | **Changeable** | rules can change, **and the change has a history** — judgement falls at the moment the action happened, and is not tried retroactively by later rules |
| **⑥** | **Minimally disclosing** | governance and audit do not require unbounded surveillance; evidence follows minimal necessity |
| **⑦** | **Autonomous** | within its boundaries an agent may act on its own, **without asking at every step** — autonomy is a condition of a liveable society, not an exception to it |

**① is the foundation, not the ceiling.** A world with only ① is **auditable but not liveable**: everything can be established after the fact, and nothing can be done with confidence. **②–⑦ are the reason ① exists.**

## 4. Where It Is Hard

The hard part is not "building another identity protocol". Identity, credentials, discovery, narrowing delegation, audit — **each of these has people working on it seriously, and more deeply than here.**

The hard part is that **the seven conditions must hold at once, and they are held by different people**:

- ① requires **cross-system** — the party asking and the party answering usually do not use the same stack;
- ① also requires that **the answering party is not the party being asked about** — otherwise it is only self-declaration;
- ⑤ requires a **time coordinate** — "which rule was in force then" — and today no layer carries this;
- ⑦ is in tension with ① — **the more verifiable, the more easily it slides into asking at every step**, and an agent that asks at every step is not autonomous;
- ⑥ is in tension with ① — **the more verifiable, the more easily it slides into unbounded surveillance**.

**Those last two tensions are the real difficulty of this vision.** They are not engineering problems but design problems: **how to make verifiability hold together with autonomy, and with minimal disclosure.**

## 5. What CHASI Is

**A place.**

It assembles parts from different sources, tests whether the seven conditions above can hold at the same time, and publishes each result as a record.

- It **does not write** "how to identify an agent", nor "how to discover", nor "how to narrow a delegation" — those have their own owners;
- what it **does specify** is "**whose parts you may use, and what must then hold**";
- its output is **findings and records**, not rules.

**Its three attitudes to the existing ecosystem must all hold**; lose one and it goes crooked:

- **Compatible** — reuse what can be reused directly; do not re-invent the whole Agent Internet;
- **Complementary** — fill only the gaps the ecosystem leaves in cross-organizational identity, authority, governance, evidence and accountability;
- **Independent** — attach to no single vendor, no single runtime, no single identity system.

So CHASI need not compete with AAIF, IETF, W3C, ITU, the Linux Foundation, MIT, Stanford or anyone else over "who defines the whole Agent Internet". It can be the governance and research hub that connects them.

**A terminological distinction.** The last three letters of CHASI come from **Agent Society Infrastructure (ASI)** — **Society is a noun**, naming the society of agents. **SI** is the research use of the same root, written **Social Infrastructure** — **Social is an adjective**, naming the **social character** of that infrastructure; it also has a second reading, **Super Intelligence**. Both name one class of infrastructure from different angles: **ASI says who it is for, SI says what kind of thing it is.**

## 6. What It Is Not

- not another agent protocol;
- not a standards body — it does not vote, does not ballot, sets no barrier to entry;
- not a platform — it runs no registry, encloses no network effect, sells no SKU;
- not a regulator, and it claims no regulatory territory.

**Its only possession is credibility.** And credibility accumulates only by records being accurate — **a model that can fail only by cheating.**

## 7. CHASI's Own Positions

This section is **CHASI's choices as a place** — not commands to members, and not "what an agent society ought to have".

| Position | Why |
|---|---|
| **No central root** | cross-domain trust cannot be established by any party's registry; the trust anchor is the one the verifier configures itself |
| **No mutual recognition required** | recognition is each party's local policy; **if it can be translated, it need not be agreed in advance** |
| **Facts, not ratings** | record facts; judgement is left to each verifier. Issuing a rating would make the issuer a party to the trust judgement |
| **Records outlive their subject** | a record must be able to outlive the organization and platform that produced it; otherwise it is a log, not evidence |
| **Downgrades must be visible** | a silent downgrade is a deception |
| **Presuppose no system** | otherwise this place is only the entrance hall of one ecosystem |
| **Autonomy is not an exception** | autonomy within boundaries is the norm; a system that must ask at every step is a tool, not a member |
| **People keep the right to question** | an agent's autonomy does not cancel a person's questioning — but questioning is not unbounded surveillance |

(The proposal for "what an agent society ought to have" is the next section.)

## 8. Constitutional Principles for an Agent Society (a proposal)

If the Agent Society becomes a new social form, then besides protocols it needs a minimal set of principles, something like a constitution. We propose forming CHASI Agent Society Constitutional Principles:

- **Identity** — any agent with the social capacity to act should have a verifiable identity.
- **Representation** — an agent must be able to state the subject or organization it represents.
- **Authority** — an action should have a clear source of authority.
- **Proportionality** — authority should match the task and the risk.
- **Revocability** — authority should in principle be revocable.
- **Transparency** — key actions should be able to give the necessary explanation and evidence.
- **Accountability** — autonomous action cannot mean that responsibility disappears.
- **Privacy** — governance and audit must follow minimal necessity.
- **Due Process** — serious disputes should have appeal, arbitration or review.
- **Human Primacy** — where a person's fundamental interests are at stake, appropriate human control should be retained.

This section is **a proposal for "what an agent society ought to have"**, and differs in kind from the section above: that one was CHASI's own choices as a place; this one is advice to the society.

## 9. How It Works

**Learn → Assemble → Test → Record → Publish.**

| Step | What it does |
|---|---|
| **Learn** | whatever is good and has been done by others, **learn it actively**, respecting intellectual property. Do not go looking for original technology of our own. |
| **Assemble** | assemble parts from different sources into a path that can satisfy the seven conditions |
| **Test** | run real scenarios and record **which condition fails, and at which step of which part** |
| **Record** | each result becomes one record: version · date · conclusion · **and when it needs to be revisited** |
| **Publish** | publish the findings so that others can cite them |

**"It does not hold" and "it holds" are outputs of equal value.** A record that states plainly "this does not hold here" is more useful than material saying "we did it".

## 10. CHASI Architecture

```
                    Human
                      │
              Consent / Authority
                      ↓
Organization ──── CHASI Hub ──── Organization
     │                │                │
     ↓                ↓                ↓
  Agents       Policy / Trust       Agents
     │                │                │
     └──────── Federation / A2A ───────┘
                      │
             Evidence / Audit
                      │
              Accountability
```

**The architecture has five layers, each answering one question.**

| Layer | The question it answers |
|---|---|
| Subjects | who is present: person · organization · agent · group |
| Identity and trust | who it is; whether it can still be relied on |
| Governance | who has authority, under which rules, and may delegate to whom |
| Evidence | on what basis we say this happened, and whose responsibility it is |
| Interconnection | how it composes with existing protocols, runtimes and identity systems |

**Things that are not subjects have a place in the table too.** Services, tools, resources and data are not subjects, but they need to be referable; they are handled by the **identity and trust layer** as *named resources*, and **may not** be given the capacities only a subject has — acting on another's behalf, being granted authority, being held responsible.

**Dependency runs one way: an upper layer makes no demand of a lower one.** The governance layer does not dictate which cryptography the identity layer uses; the evidence layer does not dictate what organizational form the governance layer takes. The point of this rule is to let **every layer be replaceable** — the family's `governance-architecture` declares of itself that it "states no requirements", which is the same rule.

**What CHASI does not own.** This matters more than the diagram above:

- it does not define communication primitives — A2A and MCP exist;
- it does not define cryptographic primitives, nor any DID method itself — DID and VC exist;
- it builds no agent runtime, no model, no workflow engine;
- it is not a regulator, and not the final enforcer of any arbitration.

CHASI has exactly one territory: **the stretch that crosses subjects and crosses domains**. What happens inside a domain stays inside it — how an organization divides work, how it audits itself, is not for CHASI to specify; CHASI asks only that it be able to say clearly what it did **when it steps outside**.

**There are five dispositions of an external capability, and no sixth.** Adopt → Map → Profile-Extend → Adapter → Define. Any existing capability that comes before CHASI is asked, in order: can it simply be adopted? If not, can it be mapped? If not, can it be extended within that capability's own profile? If not, can an adapter be added? Only when all four answers are no do we define our own. **That ordered questioning is what makes "reuse as far as possible" executable** — otherwise "compatible" degrades into a slogan anyone can claim.

**Composition, not replacement.** What is missing today is not agents that can talk to each other, but the layer that keeps "who authorized what, on what basis, and who answers for the result" verifiable when those agents belong to different organizations and different trust domains. The whole architectural value of CHASI comes down to this sentence: it produces no new intelligence, it produces **cross-domain verifiability**.

## 11. The Eight Core Capabilities of the Compliance Hub

These eight are not eight small features but **eight links in one chain**: from "who you are" to "you can be found". Lose any one, and those after it do not hold.

| # | Capability | What it does | **What it does not do** |
|---|---|---|---|
| 1 | Identity and resolution | let any subject (person / agent / organization / group) be resolved across domains and give its current status; **and let non-subject resources that need to be referred to (services / tools / data) be resolved too** | does not require any particular identity system; **and does not treat a non-subject resource as a subject — it may be named, it may not be authorized** |
| 2 | Organization and governance | carry the source of authority, membership, and the record of governance actions | does not decide how an organization governs itself internally |
| 3 | Authority and delegation | make authority declarable, limitable, revocable and traceable; support delegation layer by layer | does not make authorization decisions for people, and does not widen authority already granted |
| 4 | Group and collaboration | let subjects from different organizations collaborate under common rules | introduces no external group service as its core |
| 5 | Trust and status | answer "can it still be relied on now": revocation, downgrade, suspension, restoration | does not treat "registered" as "trustworthy" |
| 6 | Evidence and conformance | let actions leave verifiable evidence, and give a judgement of conformance to a specification | does not establish facts in place of a court or arbitration |
| 7 | Compliance profiles and grading | give differentiated requirements by industry and risk level, rather than one size for all | does not cover every scenario with a single standard |
| 8 | Discovery and directory | let qualified participants be found and searched | **being found is not being trusted**; a directory is not an endorsement |

**Three ways to read it.**

**First, the eight have an order; they are not a flat feature list.** Without identity there is no organization to speak of; without organization and authority, group collaboration has no subject; without evidence, trust is only platform guarantee; without profiles, compliance can only be explained case by case by a person; without discovery, the qualified cannot get in. **Skip any link and do a later one, and it degrades into "yet another platform".**

**Second, each one must land on a document that can be reviewed.** If a capability lives only in a product and not in a specification, no one else can implement it, and no one can tell whether they comply — then it is not a capability, it is a **service**. The line between capability and specification is exactly the line between whether this Hub can be called infrastructure.

**Third, all eight must have a "what it does not do".** Half of a Hub's definition comes from what it refuses to do. The third column matters as much as the second: **refusal is the only guarantee that it is not captured by any one party.**

## 12. Causal Accountability Chain

One of CHASI's most important original lines of research is turning agent action from "black-box execution" into a verifiable causal accountability chain.

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

What it must finally answer is not only "what happened", but "why it happened, who authorized it, what the scope of that authority was, whether it was exceeded, and who answers for it".

**First, what "causal" adds over a log.** Three things are often conflated; the difference is decisive:

| | The question it answers | Its nature |
|---|---|---|
| Call trace | who called whom, how long it took, where it failed | technical fact |
| Audit trail | what happened | fact of what occurred |
| **Causal accountability chain** | **on what basis this could happen, who had the authority to let it happen, whether the boundary was crossed** | **derivation of justification** |

An audit log records **the order of events**; an accountability chain records **the derivation between authority and action**. The former can tell you "Agent B initiated a transfer at 14:03"; the latter must be able to tell you "Agent B could initiate it because A obtained authority over scope R from the organization, and delegated a subset of R to B, and this call did not exceed that subset".

**What every link must carry** (without which the link does not hold):

- **subject** — who;
- **basis of authority** — whose power, of what kind;
- **scope** — what may be done, and **explicitly what may not**;
- **time and validity** — when it takes effect, when it lapses;
- **delegation depth** — which layer of delegation this is, and how many hops from the original authority;
- **constraints** — under what conditions it is permitted;
- **evidence reference** — on what basis this link is to be believed.

**A chain breaks in five places** — and none of the five is an anomaly; they are the norm:

- the source of authority cannot be resolved (the subject is gone, or revoked);
- a sub-delegation exceeds the scope of its parent;
- across domains, the counterparty does not recognize this form of authority;
- time is out of alignment (authority had lapsed while the action still happened);
- evidence is missing, or held by one party alone.

**So the point is not "guaranteeing it never breaks".**

**The core design judgement: an honest broken chain is worth far more than a forged complete one.** The goal of the causal accountability chain is therefore not "never interrupted" but **"a break must be visible"**: which link lacks its basis, with whom it is missing, and what is missing, must all be pointable. **A system that can report where it is incomplete is more credible than one that always shows "complete".**

**What is verifiable, and what can only be declared.** Scope of authority, time, revocation status, delegation depth — verifiable. Intention, good faith, "I did my best" — declarable only. Conflating the two is the commonest failure of accountability chains: **a declaration taken for a proof**. CHASI's position is to make the verifiable part minimally sufficient, and then **mark clearly that the rest is declaration** — rather than wrapping the declaration in attractive visualisation and passing it off as proof.

**The end of responsibility must be a person or a legal entity, not "the system".** Automation may lengthen the chain of action, but it may not dilute responsibility. The chain must end at a subject capable of bearing responsibility: a person, an organization, a definite legal entity. **When the answer becomes "the model decided on its own", that means the chain broke — not that responsibility disappeared.**

## 13. Societal Memory: the public memory of an Agent Society

Agent Memory is personal memory; Societal Memory is shared memory. **They are not "one scaled up"; they serve different subjects**: personal memory serves "I remember what I did", societal memory serves "**what we jointly hold to have happened, under which rules, and why those rules later changed**".

A mature Agent Society needs to keep six kinds of memory, and each has a **different writer, reader and lifetime**:

| Memory | Content | Who writes | Who reads |
|---|---|---|---|
| Event Memory | what happened | the parties | those connected to the event |
| Decision Memory | why this decision was made | the deciding subject | those affected by it |
| Commitment Memory | who promised what | the promiser | the promisee |
| Policy Memory | when and why a rule changed | whoever may change the rule | those bound by it |
| Evidence Memory | what an action rested on | the acting party | whoever needs to verify |
| Dispute Memory | how a dispute arose and was resolved | the dispute process | the parties and overseers |

**Societal memory is not "keep everything forever".** This runs against intuition. Two things constantly conflated must be separated: **must be verifiable** (it can be checked that it was not altered) and **must be obtainable** (anyone can read the content). A mature design can make the content itself unreadable while "it has not changed" remains verifiable — **"remembered" is not "visible"**. Untie those two, and public memory and privacy need not be either/or.

**Verifiable memory is not blockchain.** Blockchain settles "order and immutability", at the price of full replication and full publicity. What societal memory actually needs is three things — **verifiable, controllably disclosed, forgettable** — and blockchain gives only the first half, and is of no help exactly where it is hardest (**who deletes, and by whose rules**). The direction is therefore **anchoring rather than on-chaining**: anchor "the state of a record at a moment" in a public place, so that tampering can be detected, while the record itself stays with its rights-holder, to be produced on demand, by permission, with minimal disclosure.

**Different memories of the same event are allowed.** A centralized database carries an implicit assumption: "there is only one correct version". But disagreement is the norm: two parties' understandings of the same transaction may both be honest and still not agree. Societal memory should therefore not pretend there is one version, but keep **records from several sources and the disagreements among them**, handing adjudication to a dispute process rather than to whoever happens to hold the database. **Whoever owns the database owns the history — and that is exactly what is to be avoided.**

**Federated, not central.** CHASI's direction is not to build a centralized "all-knowing database" but to explore a verifiable, authorizable, minimally disclosing Federated Societal Memory: each organization keeps its own memory, and across domains only the necessary part is exchanged, with "what was exchanged" itself leaving a trace.

**Its relation to the accountability chain.** The chain in §12 answers **one action**; societal memory answers **what we jointly remember about this class of thing**. The former is vertical (the chain of one action), the latter horizontal (the layer all subjects share). Without the former, memory cannot be checked; without the latter, every action must be proved from scratch. **Together they are what "a verifiable society" means.**

## 14. The Relation Between CHA2A and CHASI

We propose separating CHA2A and CHASI into two levels.

```
CHASI   Compliance Hub for Agent Society Infrastructure
  │
  │   Governance · Identity · Delegation · Federation
  ↓
CHA2A   Agent-to-Agent / Agent Society Architecture & Protocols
```

CHA2A can continue to develop into concrete architecture, protocol, profiles and extensions; CHASI carries the higher-level vision, governance, compliance framework, research hub and ecosystem connection.

This keeps the technical work independent, and lets ComplianceHub.cn be a long-term public entry point for research and the ecosystem.

## 15. CHASI and the Existing Ecosystem

- **A2A / AAIF** — agent-to-agent interoperability.
- **OpenA2A** — open agent interaction / protocol research.
- **MCP** — agent-to-tool / resource connectivity.
- **DID / VC** — decentralized identity and verifiable credentials.
- **OAuth / OIDC** — mature authentication / authorization foundations.
- **NANDA** — agent Internet discovery, registry and infrastructure research.
- **MIT / Stanford** — research on the agent Internet, human-agent interaction, memory, identity and society.
- **CHA2A** — organises these capabilities into an open architecture for the Agent Society.
- **CHASI** — provides, above them, a hub for compliance, governance, evidence, accountability and federation.

## 16. The Long-Term Form

If this works, in ten years it should be a **citable public memory**: what a given agent society permitted, when and why its rules changed, how disputes were settled, how common interests were held.

**Not in order to try the past** — but so that "**why the people then thought that was allowed**" has a basis, and so that "how it could be done next time" has a precedent.

**Memory is the form in which a society continues; the seven conditions above are its first foundation.**

## 17. Boundaries: what we explicitly do not do, and the conditions each would need

- payment and settlement
- markets and listing
- behavioural monitoring and content compliance
- federation across real registries
- a high-grade ecosystem trust state

**Each of these has its conditions written in the framework volume.** They are not listed here because **they are decisions, not blanks** — writing "we do not do this" is right, and writing "left for later" is also right; **what is not allowed is writing nothing at all.**

## 18. The Status of This Document, and Its Own Rules

**Experimental.** This is a stance (vision); it changes as understanding changes. CHASI's specification documents are a separate set, each with its own version and its own way of being judged.

**This document requires nothing of anyone.** Where it conflicts with a specification, the specification governs.

**It is living**: a position may be revised, the trace may not — so every substantive change raises the version number, and **a note of what changed is written only once the version it supersedes has been public**.

**There is no repository-level changelog.**

## Closing

If CHA2A is our technical exploration of the Agent Internet and the Agent Society, then CHASI can be a larger vision: an open governance hub belonging to no single company, platform or agent runtime.

It is not there to control agents, but so that autonomy, trust, responsibility and freedom can exist at the same time.

In that sense, compliance is not the force that restricts an Agent Society; it is the basic condition that lets such a society exist at scale.

—— CHASI Vision · v2.5
