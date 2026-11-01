# CHA2A Protocol Suite Architecture

**The Agent Cloud protocol suite: overall architecture, and a strategy for reusing external protocols**

> Status: draft (v0.2) | Date: 2026-10-01
> Position: this family's **upper architecture**. `governance-architecture` and `agent-passport` unfold beneath it, as do the Group & Collaboration, Federation and Marketplace/Commerce volumes
> Principle: **if an existing standard can be used, do not invent one** — prefer Adopt for mature capability, then Map, Profile-Extend, Adapter, and **only then Define**
> Related: `governance-architecture.md` (the architecture layer beneath) · `assembly.md` (the four-slot assembly) · `question.md` (the judgment format) · `naming.md` (addressing)

---

## 0. The core claim

> **Recognition does not change the trust root; evidence does not depend on an operator.**

**Expanded**: in any cross-trust-domain agent collaboration, the **authority and the evidence** must be independently verifiable by a third party **belonging to no party**.

**Why this sentence has to exist**: it is the criterion for every trade-off inside this family. §10 (the region that needs Define), the layering in §4, and the order of work in each volume are all decided by it — **without it, every item gets kept, and nothing ever gets finished.**

**For comparison**: OAuth's claim is "a token instead of a password, for delegated authorization"; DID Core's is "identifier decoupled from document, resolvable"; APS's is "authority only ever decreases at each hop"; ARIA's is "membrane". This family previously lacked such a sentence.

---

## 1. What this document is

This document defines CHA2A's long-term protocol suite architecture for Agent Cloud. The goal is not to re-invent every underlying protocol, but to build a protocol system for Agent Cloud that is **composable, interoperable and extensible**.

For existing mature capability, prefer **Adopt**; where semantics must be translated across protocols, **Map**; where the Agent Cloud scenario needs constraint or extension, **Profile / Extend**; where protocols cannot interoperate directly, use an **Adapter**; and only where an Agent Cloud core capability has no existing specification, **Define**.

**The final criterion for these five relations is §0's core claim**: any capability that cannot serve "recognition does not change the trust root, evidence does not depend on an operator" does not go into Define.

---

## 2. Overall design principles

- **Reuse first** — where an existing standard meets the need, adopt it rather than inventing a protocol.
- **Composition first** — CHA2A's core value is **organizing** Identity, Governance, Interoperability, Group, Federation and Marketplace capabilities.
- **Protocol and implementation separated** — an experimental implementation must not capture the long-term architecture; a shortfall is recorded as an **Implementation Gap**.
- **Open interoperability** — different DID Methods, Passports, Credentials, Registries and Agent Protocols are allowed to coexist.
- **Federation-first** — a large partner may keep its own Registry / Trust Domain and join Agent Cloud through federation.
- **Evolvable** — where a standard is not yet stable, Profile, Extension, Versioning and Capability Negotiation keep room to change.
- **Sufficient and stop** — every volume must state a **sufficiency criterion**: what condition makes it complete, so that it stops there. **Without this discipline a specification family expands forever.**
- **No trust root is presupposed** — this family requires no participant to change its own trust root; every difference involving a trust root is handled through **recognition** (§10, original items ③ and ④), never through unification.

---

## 3. The overall model

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

## 4. The proposed layering of the protocol suite

**The last column, "sufficiency criterion", says how far each layer has to be written and no further** (see §2, "sufficient and stop").

| Layer | Responsibility | Sufficiency criterion |
|---|---|---|
| **CHA2A Core** | Agent, Organization, Registry, the basic object model, version/capability negotiation, basic message and error model | any two systems implementing this family can agree on **what an object is** |
| **Governance** | Organization, Admin, agent ownership, Delegation, Role, Policy, Trust Domain, cross-subject governance | it can say who issues, who revokes and who is responsible; and it aligns with APS §10 rather than redefining what that covers |
| **Passport & Interoperability** | Passport Profile, DID/VC binding, Agent Card mapping, A2A/MCP mappings, multiple DID Methods | one credential verifies under the verifiers of two different systems |
| **Group & Collaboration** | Group, Membership, Presence, Invitation, cross-organization groups, joint tasks and group chat | agents of two organizations that do not belong to each other can join one group and complete a task |
| **Federation** | Global Registry, Partner Registry, Trust Domain, cross-registry discovery, resolution, federation policy | no participant has to change its own system in order to be recognized by another |
| **Evidence & Trust** | signed evidence, action/result records, verification, status, revocation, audit interface | a third party can decide the authenticity and currency of one piece of evidence **without depending on any party's system being available** |
| **Marketplace / Commerce** | agent offering, Provider, discovery, invocation, rental, settlement interface; **payment itself is not redefined** | identity and governance information suffice to support one invocation, and no payment definition is needed |
| **Workflow / Task** | task lifecycle, delegation chain, asynchronous tasks, artifacts, review and collaboration state; mapped to the A2A Task model | the mapping to the A2A Task model loses no information |

---

## 5. The five relations to external protocols

| Relation | Meaning |
|---|---|
| **Adopt** | take an existing specification directly as a dependency or compatibility base |
| **Map** | define a semantic mapping between CHA2A objects and external objects, e.g. CHA2A Agent to A2A Agent Card, Credential to Passport artifact |
| **Profile / Extend** | the existing protocol nearly suffices, but the Agent Cloud scenario needs constraint, configuration or extension |
| **Adapter** | where protocols cannot interoperate directly, define an adaptation layer rather than forcing a change to the external protocol |
| **Define** | only where an Agent Cloud core capability has no existing specification and needs unified semantics does CHA2A define it itself |

---

## 6. Positioning matrix for the external ecosystem

**Object · version / date / status · this family's strategy.**

| Object | What it mainly addresses | This family's strategy | Version / date / status |
|---|---|---|---|
| **OpenA2A** | DID, agent identity, trust, authorization, transparency | Adopt + Map + Adapter | `did:opena2a` 0.1–0.2 draft; PR #717 merged 2026-07-04 (two version numbers disagree between sources; unresolved) |
| **A2A** | agent-to-agent communication, Task, Agent Card, discovery | Adopt + Profile + Map | initiated by Google, now a Linux Foundation project |
| **MCP** | connecting agents/applications to tools and resources | Adopt + Adapter | CHA2A does not redefine a tool protocol |
| **APS** | Agent Passport, delegation, authority, evidence | Study + Map + Profile/Adapter | `draft-pidlisnyi-aps-04`, 2026-09-28, IETF Individual Draft — **not a settled standard; must be marked work in progress** |
| **ARIA / TrustLayer Foundation / W3C CG** | cross-organizational agent identity and trust: DNS-anchored DID + VC + trust ledger + a three-stage admission policy | Study + Map + Adapter | registry live; specification CC-BY-4.0 / SDK Apache-2.0; chairs a W3C CG (`public-agent-identity`) |
| **Ant ACT 2.1 / APASS / Alipay+ AMP** | identity + authorization + payment + attestation | Study + Map (**not** Adopt) | ACT 2.1 released and open (docs CC-BY-4.0 / code Apache-2.0); AMP repository opened 2026-08-17 |
| **GB/Z 185-2026 + AIP + the agent identity code** | identity, description, discovery, interaction and tool invocation for domestic agent interconnection | Track + Map | GB/Z 185-2026 published 2026-06-26; AIP open-sourced; identity-code nodes have issued |
| **UnionPay APOP (Open Protocol for Agent Payment)** | agent identity management, intent management, user identity management, payment authorization management | Track | published 2026-04-02; listed on the open platform with a sandbox; invitation-based |

**⚠️ The wording has to be exact**: GB/Z is a **national guiding technical document**, not a standard — **it should not be cited in a way that gives it mandatory force**; its cover is not that of a "national standard"; and it must be reviewed within three years (it may become a standard, or be withdrawn).

**One organizational fact that affects judgement**: no IETF working group is currently chartered to handle AI agent identity or agentic authorization. See §8.

---

## 7. What OpenA2A suggests for this family

OpenA2A's public material shows `did:opena2a` at 0.2 draft, registered in the W3C DID Extensions Registry. Its Passport page explains Passport as **composed from the existing artifacts did:opena2a, AIP, ATX and ATP**, rather than as a separate Passport object that must exist.

So CHA2A **should not aim to re-invent an Agent Passport data format**. The better direction is to define a **CHA2A Passport Profile / Federation Envelope**: how different DID Methods, Credentials, Agent Cards, trust proofs, delegations and evidence **enter Agent Cloud, and can be verified across registries and trust domains**.

---

## 8. What APS suggests for this family

APS is the currently public IETF Individual Internet-Draft, latest public version `draft-pidlisnyi-aps-04` (2026-09-28). It covers Agent Passport, represented principal, delegation, authority lifecycle, policy approval, enforcement and signed evidence.

APS should therefore be treated as a **key reference and interoperability counterpart**, not as a standard CHA2A has adopted. Its current status must be marked **work in progress**.

**The state of the IETF** (which bears directly on what this family should expect of it):

- WIMSE is chartered only up to workload identity (there is a separate agent document, AIMS);
- the proposed DAWN charter puts AI agent / tool / skill identity management **out of scope**;
- the proposed `agentproto` charter commits to **reusing** existing identity, authentication and authorization building blocks rather than defining new ones;
- **no working group is chartered** at present.

**Two further points in APS bear directly on this family**:

1. its §11 makes **Adapter Contracts** part of the specification (including MCP / A2A / OAuth ID-JAG bindings, and what to do when an adapter cannot carry some dimension), which is a useful form for this family's interoperability volume;
2. its site erratum (2026-08-17) states that the released TypeScript and Go verifiers compare spend and depth **only when both parent and child carry the field**, and do not check validity-period containment across hops — that is, **omitting a field bypasses its core invariant**. **This family should write "a missing field is a refusal" into the corresponding volume.**

---

## 9. Repositioning the Passport

CHA2A Passport's long-term position should move from "inventing a new agent identity document" to being **the interoperable identity-and-governance composition layer for Agent Cloud**.

**Of the pieces below, the great majority are already defined by external specifications. This family's contribution to this layer is exactly two things**: ① specifying **how these pieces compose** into a verifiable whole; and ② specifying the **semantics of recognition** when pieces come from different trust roots. Field definitions beyond those two things are not done at all.

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

## 10. The region that genuinely needs Define

### 10.1 Original (Define) — four items, this family's only technical differentiators

| Original item | Content | Sufficiency criterion |
|---|---|---|
| **① Cross-Organization Group** | membership, invitation, authorization and collaboration rules for a group spanning organizations | agents of two organizations that do not belong to each other can join one group and complete a task |
| **② Unified semantics for registry federation and trust-domain federation** | the **semantic model** of federation, not merely discovery | no participant has to change its own system in order to be recognized |
| **③ A federation profile by which different Passport / DID / Credential systems enter one Agent Cloud** (i.e. recognition) | recognition: who establishes the equivalence, who issues it, how its scope is bounded, how invalidation cascades | **recognition changes no party's trust root** |
| **④ After recognition: independent third-party verification of evidence** | how one piece of evidence is verified by a third party belonging to no party, without depending on any party's system being available | a third party can decide its authenticity and currency **from public information and the evidence alone** |

**Why item ④ has to stand alone**: it is what distinguishes this family from APS and ARIA. APS's trust rests on its own trust authority, ARIA's on its own registry — **neither answers "how does a third party belonging to no party verify"**. It is also the second half of §0's claim.

### 10.2 Aligned (Adopt / Map / Profile) — five items, with no original definition

| Item | Reclassified as | Reason |
|---|---|---|
| The standard model of an Organization as a governance domain | aligned | APS §10 (Charter / Office / Holder / Root Authority Basis / monotonic projection / succession on departure / break-glass / re-rooting) already covers it, and more deeply |
| Identity and authorization models for Organization admin / super-user / coordinator | aligned + profile difference | as above; **Coordinator is this family's own role** and may be kept as a profile difference |
| Agent membership and its relation to an organization | aligned + difference noted | APS's identity and governance model already provides the frame |
| The unified association among project/task delegation, evidence, artifacts and governance records | aligned | covered by APS §7 + §9 (ReceiptV1, DecisionRefV1, evidence resolution, three core receipt classes) |
| How Provider, agent offering and rental/invocation relationships in a marketplace connect to identity and governance | **deferred** (depends on ①②③) | the direction is kept but has the lowest priority; §11 already declines to redefine payment clearing |

---

## 11. Regions this family explicitly does not redefine

- It does not redefine the general **DID** standard.
- It does not redefine the general **Verifiable Credential** standard.
- It does not reimplement **A2A**'s basic communication semantics.
- It does not reimplement **MCP**'s Tool / Resource / Prompt protocol.
- It does not redefine **payment clearing** or any specific payment network.
- **It does not require every ecosystem participant to adopt CHA2A's own DID Method.**
- It does not redefine the format of **trust proofs, trust levels or transparency logs** (aligned with APS §7 / the ATP form).
- It does not redefine **reputation or trust-level scoring algorithms.**

---

## 12. Federation architecture

The Global Registry is **not required to be the only registry**. The long-term goal is a federable network of multiple registries: a large partner may run its own sub-registry and interoperate with the CHA2A Global Registry through a common federation protocol.

**It must be stated that federation's core is not "discovery" but "recognition".** Discovery already has reusable approaches (for example, the MCP Registry explicitly has no payment layer, and A2A agent cards are published at `/.well-known`); **this family's original contribution at the federation layer is only recognition semantics and third-party verification of evidence** (§10, original items ②③④).

---

## 13. Versioning and governance principles

- **Keep the main specification small and stable**; new complex capability goes into a volume first.
- A volume of the suite **may not conflict with Core**; evolution is handled through extension/profile.
- An experimental protocol must be marked **Experimental** and does not go straight into a core specification.
- **Every item of external-protocol tracking must record version, date, status and its effect on CHA2A.**
- An unstable external standard **is not taken as the sole basis**; it may be referenced, adapted or replaced.
- **§0's core claim is the most stable layer**; changing it requires recording the reason separately and re-examining §10's list of original items.
- **Every volume must state a sufficiency criterion when it is finalized; without one it may not enter Stable.**

---

## 14. References and status notes

- **OpenA2A `did:opena2a`**: public version 0.2 draft; the public material indicates registration in the W3C DID Extensions Registry. Its Passport page describes Passport as **composed from the artifacts did:opena2a, AIP, ATX and ATP**.
- **A2A**: the official documentation describes it as an open agent-to-agent interoperability standard; initiated by Google and now a Linux Foundation project.
- **APS**: latest public `draft-pidlisnyi-aps-04`, 2026-09-28; an IETF Individual Submission, still an Internet-Draft / work in progress.
- **ARIA / TrustLayer Foundation**: registry live (`registry.aria.bar`); specification CC-BY-4.0, SDK Apache-2.0; W3C Community Group is Agent Identity Registry Protocol (`public-agent-identity`).
- **Ant ACT 2.1**: released and open, docs CC-BY-4.0 / code Apache-2.0; APASS provides a merchant workbench / skill / CLI / SDK / OpenAPI; the Alipay+ AMP repository was opened 2026-08-17, Apache-2.0.
- **GB/Z 185-2026, *Artificial intelligence — Agent interconnection*** (7 parts): published 2026-06-26. **Its nature is a national guiding technical document, not a standard**; under Article 4 of the provisions governing such documents, it should not be cited in a way that makes it mandatory or administratively binding; under Article 10 it must be reviewed within three years of publication.
- **UnionPay APOP**: published 2026-04-02, with four capabilities — agent identity management, intent management, user identity management and payment authorization management; listed on the UnionPay open platform (with a sandbox), invitation-based.
- **The state of the IETF**: no working group is currently chartered to handle AI agent identity or agentic authorization; WIMSE is limited to workload identity; the proposed DAWN charter puts agent identity management out of scope; the proposed `agentproto` charter commits to reuse rather than new definition.

**The nature of this document: an architecture plan. It endorses no external standard and declares no formal adoption of one.**

—— CHA2A Protocol Suite Architecture · v0.2
