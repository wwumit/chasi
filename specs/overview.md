# CHA2A Specification Group — Overview

> Status: draft (v0.3)
> Date: 2026-10-19
> Position: **the entry document and index of this family**; §3 gives the document order
> Layer: **L3 · specifications** — the entry and index of that layer; this repository's eight-layer index is `README.md`
> Principle: this family adds only the layer that existing standards lack — **judgement across trust domains**; identity, evidence, collaboration and transport keep the standards they already have
> Related: `README.md` (document index) · `CHA2A-Scope` (boundaries) · `did-method-cha2a.md` (the method specification)

---

## 1. Core claim

> **A verifier that belongs to no party should be able to answer four questions independently —**
> **who it is · who authorized it · in what context it is acting · what it has done —**
> **without asking the subject's operator, and without being anyone's customer.**

**This sentence defines the core**: anything the four questions cannot cover is not part of it (§4 says where the rest goes).

**"Without contacting any platform" means, precisely, without asking the party being verified.** It does not mean the verifier is offline. It queries a registry, but **a registry it configured itself**, which is the trust anchor for what that registry returns (`did-method-cha2a.md` §4.1), and not a service belonging to the subject. The difference is substantive: the question *"may I trust this?"* is answered by **the verifier's own configuration and its own checks**, never by the subject's word.

**It holds only if four conditions hold** (each carried by one volume):

| Condition | Carried by |
|---|---|
| The identity resolves, and the trust root is portable | resolution: `did-method-cha2a.md`; portability: `governance-architecture.md` principle 9 + `registry_authority` in `organization-governance.md` |
| The authorizer's own qualification is traceable | `organization-governance.md` |
| The cross-trust-domain collaboration context is verifiable | `group-collaboration.md` |
| What was done can be independently verified by a third party | `evidence-record.md` |

---

## 2. What problem this family solves

**The problem**: in the agent ecosystem, identity, evidence and collaboration each have their own standards, but **each of them stops at the boundary of a single trust domain**.

Concretely:

- an identity's trust root is bound to one vendor's registry and cannot be moved;
- "who is in this group" is recorded in one party's database and cannot be verified;
- an organization can issue permissions and revoke members, but **where the permission originally came from** has no traceable answer;
- verification records are held by one party alone, so a dispute cannot be independently re-examined.

**The way out**: do not change anyone's trust root; make **judgement across trust domains** possible.

**The family is additive.** It competes with no existing identity, evidence or collaboration standard, and displaces no one's implementation; what it adds is the layer none of them provides.

---

## 3. Documents in this family

```
The identity-core repository (`did-method-cha2a`) — the normative core of identity and evidence:

  did-method-cha2a.md          the method · the only normative document
  agent-identity.md            the agent as subject
  evidence-record.md           the record of what was done

This repository — the architecture layer (principles and constraints only; states no requirements):

  governance-architecture.md   why the family is shaped this way

This repository — the specification layer (each volume states the requirements for its own subject):

  organization-governance.md   the organization as subject
  group-collaboration.md       collaboration across domains
  question.md                  the verdict format: what counts as answering the four questions
  naming.md                    naming, reference and versioning
```

Layer L4 holds two further profiles, `assembly.md` and `lexicon.md`, laid over the layers below; this entry does not index them one by one — see the layer index in `README.md`.

**The companion volumes are peers of each other**, and the method specification has a **different** status: normative rather than informative. `governance-architecture.md` sits at the layer above them all: it explains why the family is shaped this way and **holds principles and constraints**; where a "must" belongs, it points at the volume that owns it (`governance-architecture.md` §1.1). Each answers a different question about a different subject: an organization exists without agents; an agent can act without belonging to an organization; a collaboration spans organizations; and a record outlives all of them.

**The two governance volumes (`organization-governance.md`, `group-collaboration.md`) and the architecture layer are maintained in this repository**, because their subject matter is not coupled to a DID method — `governance-architecture.md` carries no `did:cha2a` reference at all, and the other two carry the identity form and named interface points. They are written against an **identity binding**, of which this family's method is the worked example.

| Volume | Its subject | The question it answers | Depends on |
|---|---|---|---|
| `agent-identity.md` | the **agent** | who it is, and what it may do | `did:cha2a` |
| `organization-governance.md` | the **organization** | who is qualified to authorize it | `agent-identity.md` §7 — to name *what* is being authorized |
| `group-collaboration.md` | the **collaboration** | how agents of different organizations work together | both of the above |
| `evidence-record.md` | the **record** | how what was done is verified by a third party | `did:cha2a` — to name the signer |
| `question.md` | the **verdict** | what counts as answering the four questions, and who judges | the four above — cited, not restated |
| `naming.md` | **naming** | where names come from, and why a reference must carry a check basis | `organization-governance.md` (versioning) · `evidence-record.md` (content identity) |

**"Depends on" expresses a reference relation only.** `organization-governance.md` and `agent-identity.md` reference each other, which a tree cannot express; and a tree would have to place `group-collaboration.md` under one of them arbitrarily, when it needs both. **The four conditions in §1 are parallel for the same reason.**

`EVIDENCE.md` and `EVIDENCE_MIN_LOOP.md` are artefacts of the evidence volume, not volumes themselves.

**Note**: within this repository, apart from the method specification, every volume is an **informative companion document** (see §11 of the method specification) — normative requirements live only in the method specification. **Of these, `organization-governance.md` and `group-collaboration.md` state the requirements for their own subject; `governance-architecture.md` states none** (its §1.1). None of the three is a companion of the method. **Being informative changes a volume's status rather than its standing.**

**Conformance** is not a volume of this family: it lives in the `cha2a-conformance` repository, and §9.2 of the method specification exercises its contract.

**Language**: `overview.md` is English-first, its Chinese edition carrying `-zh`. The two companions in the identity core (`agent-identity`, `evidence-record`) are Chinese-first, their English editions carrying `-en`. Volumes in this repository are English-first, each with a `-zh` edition.

### Document order (recommended)

**A recommended order across peer volumes**; the volumes above are peers, and this sequence is one path through them:

| Order | Document | What it answers |
|---|---|---|
| 0 | this document | what this family is for, and where its boundary lies |
| 1 | `did-method-cha2a.md` | how the identifier resolves, and where the trust root is |
| 2 | `agent-identity.md` | who the agent is and what it may do |
| 3 | `organization-governance.md` | **who is qualified to authorize it** |
| 4 | `group-collaboration.md` | how agents of different organizations work together |
| 5 | `evidence-record.md` | how what was done is independently verified |
| 6 | `question.md` | what counts as answering the four questions, and who judges |
| 7 | `naming.md` | where names come from, and why a reference must carry a check basis |

**Orders 1, 2 and 5 are in the identity-core repository `did-method-cha2a`; orders 0, 3, 4, 6 and 7 are in this repository.**

**Sufficiency criterion**: a party coming to this family for the first time can, from this volume alone, say what the family is for, where its boundary lies, which volumes to consult and in what order, and which capabilities are outside it, with no oral supplement. That is the point to stop; do not extend.

---

## 4. Boundaries

### 4.1 Boundary criterion

**The four questions in §1 define the core.** Anything they cannot cover is not part of it — and §4.2–§4.4 say where that thing goes, because "not in the core" does not mean "nobody's".

### 4.2 What comes from elsewhere — dependencies, not absences

| Comes from elsewhere | For | Relation |
|---|---|---|
| W3C DID Core / Verifiable Credentials | identifier and credential syntax | **reuse** — this family adds no syntax of its own |
| A2A Task | task state machine and message semantics | **reuse**; one mapping redefined (`group-collaboration.md` §8) |
| in-toto | the shape of evidence attestations | **reuse** |
| an existing transport | moving bytes | **reuse** — transport is not this family's subject; several exist and none is required |
| agent runtime and models | execution | **outside the model** — runtime and trust judgement are independent concerns |

### 4.3 Positions this family takes, and what is deferred

**Positions** — these are choices about what this family **is**, not gaps in it:

| Position | Why |
|---|---|
| **Facts, not ratings.** The family records **facts** and **drillable evidence**; a level is a *trust summary* | a rating is an opinion, and issuing one makes its issuer a **party to the trust decision** — which is what §1 avoids |
| **Facts, not endorsement.** The family provides verifiable facts | the same reason; and in some jurisdictions the wording of an endorsement **changes the liability shape and triggers licensing** (§6) |
| **`did:cha2a` is the worked example; other DID methods retain their own identifier syntax and resolution.** | methods may coexist; cross-method interoperability uses mapping, and **adoption of this one is each party's choice** |

**Deferred** — the capability is real and wanted, and each has a named precondition:

| Deferred | Precondition for doing it |
|---|---|
| **Payment and settlement** | an agent-native settlement path that does not require the counterparty to join one operator's domain. The licensed hubs in play today are invitation-only |
| **Marketplaces / stores / listings** | a distribution layer in which recognition stays with each party, as §1 requires |
| **Behaviour monitoring · content audit · content compliance** | a disclosure layer that can be evaluated without this family taking a position on content |

**Only the positions table is about what this family is.** The deferred-work table is **work with a named precondition** — and filing it as a boundary is how a family talks itself out of its own subject matter.

### 4.4 Where the rest lives: Registry or application

**Placement rule: whoever can sign for itself must hold it itself.**

| # | Rule | Why |
|---|---|---|
| **R1** | The Registry carries **identity and status only** — DID ↔ DID Document, the L0–L4 trust summary, revocation, and the status of organizations and members. It answers *"who is this, and is it current"* | the first of §1's four questions |
| **R2** | **What a subject can sign for itself stays with the subject.** The Registry stores a pointer or a hash, never the content | `organization-governance.md` §8 — "secures the evidence, not the content" — generalized |
| **R3** | **The Registry holds identity and status; decisions live in the application.** Admission, authorization and policy evaluation all happen there. **The Registry answers; the application decides** | `group-collaboration.md` §5.3 — a Registry that decides *is* the platform assertion this family exists to remove |
| **R4** | **The collaboration surface — Group, Task, collaboration records — belongs to the applications** | `group-collaboration.md` §3 |
| **R5** | **Fail-closed belongs at the decision point.** The Registry reports "not found", or is unreachable; **refusing is the application's act** | `group-collaboration.md` §5.2 |
| **R6** | **Every cross-boundary assertion is signed by the party that asserts it.** The Registry relays and indexes; it does not assert on a subject's behalf. The one exception is the DID Document itself, which the Registry signs as controller | `did-method-cha2a.md` §4.3–§4.4 |

**Placement:**

| Concept | Registry | Application |
|---|---|---|
| DID · DID Document · keys | resolution entry point | cache |
| L0–L4 · `trust/query` · revocation | **single source of truth** | consume |
| Organization object | **a pointer only** (hash · version · status) | charter text · roles · members · controllers |
| The acts behind the four-layer traceback (appointment, grant, revocation) | — | performed subject-side, recorded as evidence |
| Delegation · authorization scope | — | the credential is held by the agent |
| Group · membership · admission · Presence | — | collaboration side |
| Task state machine | — | collaboration side (A2A) |
| Collaboration records · ledger · disagreement rule | — | each party's own |
| Evidence Record | — | produced by its author |
| Break-glass · dissolution · re-rooting | — | performed subject-side, recorded as evidence |

These rules are informative — they describe the division a conforming deployment must end up with, and the requirements themselves live in the volumes cited. They are stated here because "which component holds this" is the first question asked of this family, and answering it late is how a registry quietly becomes the platform.

**One existing endpoint needs this said explicitly.** The reference registry exposes `GET /api/v1/evidence/query?did=<did>`. Under R2 and R4 that is an **index and pointer service**: its answer is a location and a status. **Verification of a record is done against its author's signature, and that is the only thing that establishes it.** A Registry that both indexed evidence and vouched for it would be the assertion-by-one-party §1 rules out.

## 5. Status and House Conventions

**Status**: Experimental. Each volume states its own status (draft).

**Four house conventions**:

1. **Normative requirements live only in `did-method-cha2a.md`.** Informative content in the other volumes must not be cited as a requirement.
2. **Every item is either decided, marked as a deployment parameter, or marked as not-in-this-version.** The family does not use blank space as a conclusion, and it does not use a placeholder number as one either. A decided item **states the principle it is derived from**, so that the derivation can be challenged, not only the conclusion; a deployment parameter fixes the semantics and leaves only the value to the deploying parties. **A rule is stated as what holds and why it holds** — never as a verdict on what is wrong, and never as commentary on the state of the field. Where something has to be excluded, the volume states the **condition** and the **consequence** of violating it, so that the claim can be tested rather than accepted.
3. **Implementation status must be recorded**: where a document describes a capability the implementation does not yet provide, the gap is stated item by item with a date, not omitted.
4. **The family has exactly two relations to an external object.** **Reuse** — the family depends on it — which produces a mapping table and a conformance test. **Not-defining** — the family declines it — which produces a scope statement and a counter-example test: *build the minimum loop without it*. There is **no third relation called "alignment"**: it produces no artefact and cannot be falsified, and the claim that some external document "already covers" something is a claim about someone else's document, which can be wrong. **Every external object this family names is recorded with its status** — version, date, and adoption evidence. **A draft published by one project and adopted by nobody is a peer draft, not an authority**: citing it does not transfer its weight here, and its immaturity does not discredit this family either. **This is not the same axis as the five relations in the upper architecture §5.** This item classifies by **artefact** (reuse → a mapping table and a conformance test; not-defining → a scope statement and a counter-example test); §5 classifies by **decision ladder** (Adopt → Map → Profile-Extend → Adapter → Define). **The two are not mutually exclusive**: an object is first given a disposition on the ladder, then classified by what this item requires as its artefact. **Undecided: the full mapping from the five levels to the two classes.**

**This document's standing**: it is the **family entry and index**, and it is **informative**; it **states no normative requirement**. The four house conventions are shared discipline across the volumes, carried here for reference. Normative requirements live only in `did-method-cha2a.md` (item 1 above).

---

## 6. Terminology

| Term | How this family uses it |
|---|---|
| **verification** | the **determination of a fact** (whose key signed it, under which rule, what its status is). **This is this family's business** |
| **authentication** | confirmation of identity **at the connection layer**. Avoid using it as a loose synonym for verification |
| **certification** | **never used to refer to this family**; used only when citing regulation or describing a third party |
| **trust summary** | the aggregate result of L0–L4 — a *summary of facts*, not a score and not a guarantee |
| **delegation** | a scoped, time-bounded, revocable authorization relationship |
| **representative** | a member acting for a subject in a given context |

> The three-way split (verification / authentication / certification) is not wording fastidiousness: **in some jurisdictions the word "certification" triggers a specific liability shape and licensing requirement**. This family's products and documents use "verification" throughout.

---

## 7. Participation and change control

- **Licence**: Apache License 2.0 (see `LICENSE`).
- **Participation**: via GitHub issues / PRs. Adding a volume, or making a substantive change to an existing volume, should update the document index in `README.md`.
- **Change discipline**:
  1. substantive changes to the method specification (grammar, operations, DID Document shape, security model) require a version bump;
  2. non-substantive changes (editing, links, index) may be committed on their own;
  3. **a note describing what changed is written only once the version it supersedes has been public.**
- **Review cadence**: items left to the deploying parties, and any question a volume does not answer, are revisited when that volume is version-bumped. There is no separate review process.
- **Reference implementation**: `https://compliancehub.cn` (see `README.md`).

---

## 8. 中文版

中文版见 [`overview-zh.md`](./overview-zh.md)。

---

*This document is an informative overview; normative requirements are governed by `did-method-cha2a.md`.*
