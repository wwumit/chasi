# Group & Collaboration — the Cross-Organizational Collaboration Volume

> Status: draft (v0.2)
> Date: 2026-10-01
> Position: this family's volume on the **cross-organizational collaboration context** — **a peer of** `organization-governance.md` (this repository) and of `agent-identity.md` and `evidence-record.md` (the identity core, a companion repository). It defines the objects and rules of that context
> Principle: **if an existing standard can be used, do not invent one** — the task state machine aligns to A2A Task; the evidence format cites `evidence-record.md`; **the core protocol is defined by this volume**, because every external group service carries a trust model this volume rejects (§2).
> **Relation to an identity binding.** Identity is **cited, not restated**: the rules below are written against an **identity binding that resolves a subject across domains and answers for its status**, and **`did:cha2a` is the worked example** (experimental draft v1.1.0, recorded in the W3C DID Extensions registry). §9 states what this volume needs from such a binding, so another one satisfying it can take its place.
> Related: `organization-governance.md` (this repository) · `agent-identity.md` §7 (delegation and authorization scope) · `evidence-record.md` (evidence format) · `overview.md` (family entry) · `did-method-cha2a.md` (the worked identity binding)

---

## 1. The problem, and the approach

**The problem**: agents of different Organizations need to work together, but **they do not share a trust domain**.

**Recording "who is in this group" in one party's database makes membership unverifiable**, and cross-organizational collaboration can then only be accounted for separately by each side. This is not a transport problem; it is that the **collaboration context lacks verifiable membership and records**.

**The way out**: make **Group a first-class object** — membership, roles, authorization and collaboration records are all **verifiable by a third party**, rather than asserted by one party.

**This volume's responsibility**:
1. define the Group object and its fields (who created it, who is in it, who may do what);
2. define **admission** (how members from a different trust domain get in);
3. define the **cross-organizational rules** (no scope widening, revocation cascade, accountability);
4. **cites rather than restates**: identity and the identity binding in use (`did:cha2a` in the worked example), delegation and authorization scope (`agent-identity.md` §7), the evidence format (`evidence-record.md`), and the task state machine (A2A Task).

---

## 2. Where the structure comes from

**Reuse what already exists — and keep its trust model where it belongs.**

| Block | Where it comes from | What this volume adds |
|---|---|---|
| Identity and address | the identity binding in use + `agent-identity.md`; not redefined here | cross-trust-domain resolution |
| Task state machine and message semantics | A2A Task | acceptance and results are **signed**; one mapping redefined (§8) |
| Evidence format | in-toto / `evidence-record.md` | — |
| **The Group object · membership · admission** | **the collaboration plane's own subject.** The split into identity · presence · group management is the **common decomposition of any group service**, and this volume claims no part of it as its own — but that common decomposition **stops at the boundary of a single trust domain** | **this volume's own subject**: membership and admission *across* trust domains, and the rules in §5 |

**Why this volume defines the core protocol**: existing group services, including carrier messaging and federated chat, carry their own identity and account models (a phone number, an operator account, a homeserver account). **Adopting any one of them as the core protocol would import the platform assertion this family exists to remove.** They are **interoperation targets** (§11), not core dependencies.

**On ordering**: this is where the chain of §1 lands at the collaboration layer — identity resolution (who) → `agent-identity.md` (authorized to do what) → `organization-governance.md` (who was qualified to authorize it) → this volume (in which context they do it together). **Four links**: a Group admits a member whose authority traces back through its organization, and that step belongs to `organization-governance.md` §4 (the four-layer chain) — this volume's §4.1 admission gates each read it.

---

## 3. The Group object

**A Group is a first-class object**; it does not belong to any party's private database. **It contains members — and a member may be an organization.** Each acting member carries a `home_org`; a group spanning three organizations has **three organization members**, with the acting members' `home_org` pointing at them (§14). **An organization is a participant among the group's members**, rather than a layer above them. A layer would nest the governance boundary inside the collaboration boundary, and would leave a member acting **for itself** inside the group with nowhere to stand (§5.1 item ③); as a kind of member, both are expressible.

| Field | Type | Required | Note |
|---|---|---|---|
| `group_id` | string | yes | stable identifier (unique within this volume's scope) |
| `group_did` | did | no | extensible; **optional** |
| `controller` | id, **or a set under §14.3** | yes | who is accountable for this Group's governance — may be an Organization, or the task initiator. **Several parties may hold it only under §14.3's conditions**, because §5.3 item ② must stay determinable |
| `created_by` | id | yes | the initiator (may differ from `controller`) |
| `members[]` | list | yes | each: `member_id` · `did?` (a participant admitted under §4.4 may have none) · `home_org?` · **`guarantor?`** (the guarantor's identifier, scope and term, see §4.4) · `joined_at` · `status` |
| `roles[]` | list | yes | a role is **expressed separately from** Organization membership |
| `policies` | inline object, **or a reference to a rule version carrying a `hash` and an `effective_from`** (`naming.md` §2.2) | yes | at minimum: admission tier · **who must consent to admission (§4.3)** · **who can see the full audit (§5.3 item ③)** · **visibility (§5.3 item ④)** · who may dissolve · **ledger location and the disagreement rule (§5.3)**. Group rules are **rule versions**, so a reference must point at **the version in force when it was made** |
| `capabilities[]` | list | no | may be combined with Presence (§7) |
| `endpoints[]` | list | no | discovery entry points |
| `status` | enum | yes | see the nine states in §6 |

**Sufficiency criterion**: a verifier that is **any party other than the creator**, using only the fields above and the credentials each member holds itself, can independently reconstruct "**who was in this Group, when, and in what capacity**".

---

## 4. Membership and admission

**Membership must be verifiable.**

### 4.1 The three admission gates (all required)

| # | Requirement | Note |
|---|---|---|
| ① | **Identity is verifiable** | at least at a verifiable tier; **a bare assertion is not accepted** (cf. the L0–L4 tiers of the worked identity binding, `did-method-cha2a.md`) |
| ② | **Both sides confirm separately** | the inviter confirms the invitation; the invitee's administrator confirms that its member joins. **Trust requires each side's own confirmation** — A having confirmed does not mean B accepts |
| ③ | **Seat and scope** | this member's permission context inside the Group is **expressed separately from its role inside its own Organization** |

### 4.2 What should be recorded on joining

Each member leaves a verifiable record on joining: `who` (DID) · `by_whom` (who approved) · `accepted_by` (which party accepted it into this Group, and on which side) · `at` (when) · `as_what` (in what capacity/role) · `home_org`.

> **`accepted_by` is the field that matters when the question is asked.** A verified authorization chain shows that a member *may* act for its organization; it does not by itself show that the other side *agreed to be bound here*. Whether the two organizations are contractually bound is outside this family (see `organization-governance.md` §12.1 item 5); what this family requires is that the acceptance is on the record.

### 4.3 Who must consent to admission

**The default is two confirmations** — the inviter's and the member's home organization's (gate ②). A third approver is **not** required by default, because independent verifiability (gate ①) is what replaces trust in a third party.

**But a Group may require more, and must be able to say so.** `policies` therefore names **whose consent admission needs**: the inviter alone, the inviter plus the home organization, or additionally all existing members, or a declared quorum. This is a declared policy, not a fixed rule — a consortium in which every member must agree can express that, and a Group that does not care leaves the default.

### 4.4 Sponsored participants

A participant with **no organization behind it**, or with **no DID**, has no second confirmer under gate ②. Such a participant may still be admitted, but only **under a named sponsor** — a member who vouches for it and thereby carries the accountability for it.

- **The sponsorship is a governed action and must be recorded as evidence**: who sponsored · whom · for what scope · from when to when.
- **Admission requires a sponsor.** Gate ① is never waived: an unverifiable participant is admitted *because a verifiable party stands behind it*, not because the requirement was set aside.
- **The sponsorship ends when the sponsor does.** A sponsor's removal or departure ends the sponsored participant's seat with it.

### 4.5 Identifying an organization across domains

**An organization always has an identifiable context; it acquires a DID when it has to be verifiable by a counterparty.** This is the architecture's `Identity ≠ DID` principle applied to organizations:

| | |
|---|---|
| `org_id` | **always present** — the organization's own stable identifier, meaningful inside its own domain |
| the organization's identifier under the identity binding (worked example: `did:cha2a:org:<id>`) | the **cross-domain escalation** — what makes the organization resolvable and verifiable by a party that is not one of its members |

**What an admitting party checks, in order:**

1. **the identifier resolves** — through a resolver **the admitting party configured** (`did-method-cha2a.md` §4.1 in the worked example). A party is never asked to take an organization's word for its own identity;
2. **the status is current** — the organization's registry answers, or admission fails closed by class (§5.2);
3. **the authority traces back** — the chain runs to the organization's charter basis, which is `organization-governance.md` §4's subject, not this volume's.

An organization addressed only from inside its own domain is **identified by `org_id` alone**. The DID appears at the boundary, and this section is what it is for.

---

## 5. Cross-organizational rules (the core of this volume)

### 5.1 No scope widening

**A downstream permission may not exceed the upstream granted scope.**

It must be enforced at three points:

| # | Point | Requirement |
|---|---|---|
| ① | **At delegation** | the upstream granted scope (scope / target / term) may not be widened. **A missing field does not mean unlimited** — absent is treated as not permitted |
| ② | **Group role** | a role inside the Group **may not extend** a permission inside the Organization |
| ③ | **Two identities** | authorities are **separated, not intersected**: acting in one capacity uses that capacity's scope, acting in another uses the other's, and the two are **never added together**. An agent cannot obtain, by stacking them, a permission that neither holds alone — and **no extra restriction is imposed either**: requiring the *intersection* of the two would shrink authority by a rule this volume never derived, and would make dual-capacity representation unusable. **Every action must state which capacity it is taken in** |

> Item ③ is the key difference between this volume and "multiple agents within one organization": inside a single trust domain, stacking permissions is natural; **across domains, stacking is overreach**.

### 5.2 Revocation cascade, and how fresh the state must be

After either side revokes a member's authorization:

1. that member's **corresponding permissions inside the Group must cascade to invalid**;
2. the revocation action itself must be recorded as evidence (cites `evidence-record.md`);
3. **how fresh the state must be is graded by what the decision does**, not by one global number. A single "maximum tolerable staleness" was the earlier formulation, and it **conflicted with §11**: if an unreachable registry means fail-closed, then a window in which stale state is tolerated never opens — the state cannot be read. The two rules were mutually exclusive, not complementary.

| Class of decision | Freshness required |
|---|---|
| **Decisions that change authority** — admission, authorization, dissolution, bringing a revocation into effect | **must rest on fresh state; unreachable means denied. There is no time window** |
| **Read-only judgements** — display, audit, reporting | may carry a **declared staleness ceiling**; and the judgement **must record the timestamp of the state it relied on** |

**A hard requirement follows from the second row**: a judgement made on stale state must carry that state's timestamp into the record, or it cannot be re-examined afterwards.

### 5.3 Accountability (the defining feature of cross-organizational collaboration)

When cross-organizational collaboration goes wrong, four things must be **uniquely determinable**:

| # | Question |
|---|---|
| ① | **Which ledger holds the collaboration record** (whose storage, whose hash chain) |
| ② | **Who has the authority to dissolve** |
| ③ | **Who may see the full audit** |
| ④ | **Who may not see it** |

**Accountability requires all four to be determinable** — and accountability is precisely what distinguishes it from "a multi-agent group chat inside a platform".

**The Group declares all four. This volume fixes the conservative defaults that apply where a declaration is silent:**

1. **Each party holds what it produced, and what was explicitly addressed to it.** Sharing more must be **declared**. Visibility follows the same discipline as §5.1 item ①: **absent means not permitted** — the rule that governs permissions governs exposure too.
2. **The Group declares which ledger is authoritative.** The Group must declare, in advance, **(a) how a disagreement between ledgers is detected** and **(b) the rule that resolves it**. **Neither party may be the sole author of the truth** — designating one side authoritative would move platform assertion from the platform to the Group, which is what this volume exists to remove.
3. **The record outlives the Group.** Dissolution does not require either party to delete the copies it holds (see `organization-governance.md` §8, "secures the evidence, not the content").
4. **History stands after a permission is revoked.** What a member lawfully saw before removal does not become invisible afterwards. "Who may not see it" (item ④) must be a fact determinable **at a given time**, not a value that changes retroactively — otherwise it cannot be verified. **Content belongs to the deploying parties; the collaboration record belongs to this volume**: taking a party's visible copy down is the deploying parties' content and data-protection obligation, and this volume requires only that the takedown is **recorded as an audit event**.

---

## 6. Group lifecycle

```
CREATE → INVITE → JOIN → VERIFY → ACTIVE → ROLE CHANGE → LEAVE / REMOVE → REVOKE → CLOSE
```

Three requirements on top of the nine states:

1. **every state is observable and can be recorded as evidence** — no state may be invented that exists only inside one party;
2. **every non-terminal state can be cancelled**, and cancellation is a **business transition that can be transitioned again**; it is not the same thing as "rejection" (rejection is a determination about one verification and must be monotonic);
3. **CLOSE may not leave dangling tasks** — any unterminated task must be explicitly cancelled and recorded.

---

## 7. Presence, made agent-native

It expresses not only `online` / `offline` but also `available` · `busy` · `working` · `accepting_tasks`, and can be combined with capability discovery to give task coordination real-time context.

**Boundary: Presence confers no permission.** "Online" and "available for dispatch" are separate facts.

---

## 8. The relationship between Chat and Task

**Chat is one communication mode of a Group; task collaboration is another coordination mode.** The two share the underlying mechanisms — identity, membership, signature, policy, evidence — and **the two share one protocol**.

**One point that must be redefined**: A2A's `TASK_STATE_COMPLETED` is only the **executing side's self-declaration**; there is no "pending acceptance". This volume maps the counterparty's `COMPLETED` to **pending acceptance**; the counterparty's `REJECTED` (the service side declining) and the accepting side's rejection are **the same name for different things and must be renamed to distinguish them**.

---

## 9. Cross-registry resolution and verification

**The identity binding settles this**, and what it settles is narrow.

### 9.1 Every one of the four questions ends in the same act

Each of §1's four questions terminates in *resolve the identifier and read its status*:

| Question | What it needs from a registry |
|---|---|
| who it is | the DID Document |
| who authorized it | the organization's status, and the version of its charter basis |
| in what context it acts | the member's status inside the Group |
| what it has done | the status of the record's author |

### 9.2 Settled by the identity binding

- **A DID names a record, not a location** (`did-method-cha2a.md` §4.1 in the worked example — the same rationale as `did:key`): given only a DID, a verifier cannot derive which deployment holds the record.
- **The verifier-configured resolver is the trust anchor** for the documents it returns, and **under federation the trust semantics stay the same**.
- **A federated deployment MUST NOT be assumed to trust or relay data to any other registry unless explicitly configured to do so.**
- On recognition specifically: **whether one party recognizes another's issuance is a local policy question for each party.**

**⇒ Each verifier reads for itself.** A verifier reaches a counterparty's registry because its own operator configured it to. Cross-registry verification therefore needs exactly three things, all of which this family already fixes: **resolution** (discovery), **a status answer** (`trust/query`), and **the freshness rule** of §5.2 — plus fail-closed when the registry is unreachable, graded by what the decision does (§5.2).

### 9.3 No mutual recognition is required

**Federation machinery exists to solve one problem: making one authority's assertion acceptable to another.** Co-signing thresholds, published trust lists, agreements carrying trust-level mappings, revocation pushed between authorities — **each of them presupposes that a party cannot rely on a foreign assertion until some arrangement makes it acceptable**.

**A federation level is defined within one credential scheme.** Such a level relates authorities that share a proof format and an authority model, and establishes nothing about a different scheme's levels. Why this volume departs from the premises above, and why the architecture layer states premises rather than naming documents, is `governance-architecture.md` §9.

**The family's core claim removes that problem rather than solving it.** A verifier that belongs to no party has no authority to recognize — it reads the DID Document, the status and the signature, and decides.

**What remains is a business decision.** The open question is *which registries a verifier chooses to configure*, and that is a business decision each operator makes for itself. No protocol can make it for them, and writing one would only move the decision somewhere less accountable.

### 9.4 Minimum capability set for a multi-registry resolver

Federation semantics are settled in §9.2. What remains to be built here is the **operational surface** of a resolver configured to consult more than one deployment; its minimum capability set is:

registry discovery · DID resolution hint · Passport retrieval · credential verification · status checking.

**Prior art, and where the premises differ.** Registry-assisted discovery for publishers without a DNS anchor is defined in `draft-raskar-agentic-web-federated-resolution-01` — *Registry-Assisted Discovery for AI Agents and Workloads Without DNS Discovery Anchors*, Informational Internet-Draft, 2026-07-20, Raskar · Sharaf · Chari, an individual submission carrying no IETF endorsement and no formal standing. It defines a resolution record, an AI Catalog envelope, Authority Evidence, an experimental HTTPS binding, caching and revocation, and the media type `application/agent-resolution-target+json`. Two of its rules coincide with rules stated here:

| Its rule | Where this volume states the same |
|---|---|
| A client selects its registry through local configuration or deployment policy (its §9.3) | §9.2 — the verifier-configured resolver is the trust anchor |
| Registry presence alone does not make a binding authoritative; the resolver should know which validation was performed (its §10.9) | §9.3 — a verifier that belongs to no party has no authority to recognise |

Three premises differ, and the difference is what §9.2 rests on:

| | That draft | This volume |
|---|---|---|
| **What drives resolution** | **scale** — publishers with no usable DNS anchor: small businesses, individuals, hosted workloads | **trust boundary** — a verifier that belongs to no party needs to read a record held by a registry that is not its own |
| **Registry interoperability** | **deferred**: the draft removes directory federation, global-switchboard behaviour, generic directory referrals and directory-to-directory routing from its scope, and its Appendix C leaves registry interoperability to a possible future document | **settled**: recognition is each party's local policy and no mutual recognition is required (§9.3), so a registry-to-registry arrangement has no gap to fill |
| **What a resolver must be given** | the discovery mechanism to use for a given identity | the set of authorities it will accept (C3, `governance-architecture.md` §7) |

A companion preprint from the same group — *A Global Switchboard for the Agentic Web: Connecting Discovery Islands Across Enterprises, SMBs, and Individuals*, MIT Media Lab, v0.1, 2026-07-20, marked *Request for Comments* — proposes the broader directory-of-directories model. The draft cites that preprint as background and states that the directory-to-directory function is not specified by its revision. The draft's Appendix C names three open questions that are answered here: **a common credential format for authority evidence across identity classes** (`evidence-record.md`), **transparency logs and auditable recovery procedures** (`organization-governance.md` §7 and §12), and **operational governance for independently selected registries** (§5 of this volume).

## 10. Dependencies and deferred work

**What this volume depends on.** The external dependencies shared with the identity core are listed once, in `overview.md` §4.2 — A2A for the task state machine, an existing transport, in-toto for the shape of attestations. The interface points this volume exercises in practice, including those to its sibling volumes, are in §11.

**What is deferred to a future version.**

| Item | Precondition for doing it |
|---|---|
| **push / webhook** | A long cross-organizational task should not require the counterparty to hold a long-lived connection, so the pull model of §11 serves the current version. Adding push requires **signature protection on that channel**; without it, push would introduce this volume's largest new attack surface — SSRF · forged notifications · exfiltration |

---

## 11. Interfaces to existing mechanisms

| Existing mechanism | Interface point |
|---|---|
| the identity binding (worked example: `did-method-cha2a.md`) | member identity resolution; admission gate ① depends on its L0–L4 tiers |
| `agent-identity.md` §7 | delegation and authorization scope are defined there; this volume only requires that **their scope stays within the domain that granted it** |
| `evidence-record.md` | join records, task acceptance, execution results and revocations **all use the Evidence Record format**; nothing new is invented |
| status query of the identity binding (worked example: `trust/query` of `did:cha2a`) | status and revocation are checked; **for any decision that changes authority, unreachable means denied — no staleness window**; for read-only judgements a declared ceiling applies and the state timestamp must be recorded with the judgement (§5.2); **an unreviewed break-glass is visible here** (`organization-governance.md` §7.5) |
| A2A Agent Card / ARD | discovery entry points; this volume's objects can be indexed as entries |
| **Group-service components** (carrier messaging, federated chat — RCS among them) | **interoperation targets**: reachable through a gateway or adapter, with the internal model staying agent-native. **The core protocol is defined by this volume**, and an external group service is reached through a gateway or adapter rather than imported as a core dependency |
| `organization-governance.md` | supplies "who may represent the Organization"; this volume supplies "how to collaborate once inside" |

**One cryptographic implementation, serving three places**: card signatures, credential signatures and collaboration-record signatures should share one stack (JWS + JCS canonicalization).

---

## 12. Reference implementation

- Reference registry: `https://compliancehub.cn` — the reference deployment of the worked identity binding
- Minimum loop: agents of two different Organizations → create a Group → the three admission gates → signed messages → create and assign a Task → signed result → Evidence

**Acceptance criteria**:
1. a verifier that is **not the creator of this Group** can independently reconstruct the members and the collaboration records;
2. four negative paths **must go red**: flip one byte / swap the kid / mismatched member domain / already revoked;
3. **at least one external second party is included** — a loop completed entirely in-house is only a test fixture and **leaves the core claim unverified**.

---

## 13. Fixed by this volume, and left to the deploying parties

This volume leaves **every requirement decided**. It draws one line: between what the protocol fixes and what a deploying party chooses. Each fixed item states the principle it is derived from, so that the derivation can be challenged, not only the conclusion.

### 13.1 Fixed by this volume

| # | Item | Fixed by this volume | Derived from |
|---|---|---|---|
| 1 | How many parties must approve admission | **Two confirmations by default** — the inviter's and the home organization's; independent verifiability (gate ①) is what replaces a third-party approver. `policies` names **whose consent admission needs** (§4.3), so a Group requiring unanimity or a quorum can say so | §4.1 gates ① and ② + §4.3 |
| 2 | Attribution of the collaboration record | **Each party holds what it produced and what was addressed to it**; sharing more must be declared — the same discipline as §5.1 item ①, where absent means not permitted. **No ledger is authoritative by default**: the Group declares how disagreement is detected and how it is resolved, because **neither party may be the sole author of the truth** | §5.3 + §5.1 item ① |
| 3 | Takedown of a member's visible copy | *Content* is not this volume's subject — a deploying party's content and data-protection obligation, recorded as an audit event. *Evidence* is: the record survives, and **revoking a permission does not retract history** — what a member lawfully saw before removal does not become invisible | §5.3 + §10 + `organization-governance.md` §8 |
| 4 | Cancellation semantics for unterminated tasks at CLOSE | Map to A2A's **cancelled** state | §6 requirement 3 + §2 |
| 5 | Minimum Presence value set | `online` · `offline` · `available` · `busy` · `working` · `accepting_tasks` — a default set | §7 |
| 6 | Dual representation — one agent acting for two organizations | **Separation, not intersection**: two seats, each used with its own scope, **never added**. §5.1 item ③ forbids the union of two capacities and does not require their intersection — an intersection would shrink authority by a rule this volume never derived, and would make dual-capacity representation unusable in practice. **Every action must state which seat it is taken in** | §5.1 item ③ + §4.1 gate ③ |
| 7 | Revocation propagation across registries | **Freshness is graded by what the decision does.** Decisions that change authority rest on **fresh state**; read-only judgements may use a **declared staleness ceiling** and must record the state timestamp they relied on. A single global tolerance cannot be squared with §11, where an unreachable registry means fail-closed | §5.2 + §11 |

### 13.2 Left to the deploying parties

| Parameter | Fixed by this volume | Chosen by |
|---|---|---|
| **The staleness ceiling for read-only judgements** | it must be **declared in the Group object**, and every judgement made under it **must record the state timestamp it relied on**. It does **not** apply to any decision that changes authority, which requires fresh state with no window (§5.2) | the value — it requires measurement with a real second party, and a Group whose members span jurisdictions may need more than one |

**Nothing in this volume is deferred.** What falls outside it is handed to a named companion (§10), not to a future version of itself. **The one optional extension is §14**, a profile rather than a deferral: the base runs without it.

## 14. The cross-organization profile

**Optional.** The base of this volume covers a collaboration whose parties merely **vouch** for their members. This profile is for a collaboration in which the **organizations themselves are parties** — a standing arrangement rather than a single delegation. A deployment that runs only intra-organization groups, or only one-off tasks between organizations, does not need it.

**It uses only existing core objects.** Every requirement below is an existing rule of this volume applied one level up.

### 14.1 The six requirements

| # | Requirement | Reuses |
|---|---|---|
| **P1** | A party is enrolled as **a member of this Group** whose DID resolves to an `org` resource | §3 `members[]` |
| **P2** | A member acting for a party carries `home_org` pointing at it, and **the party is enrolled before its members are** | §3 `home_org` |
| **P3** | A party passes **the same three admission gates** (§4.1), confirmed by its own administrator | §4.1, one level up |
| **P4** | A party's removal or withdrawal **cascades** to every member whose `home_org` points at it | §5.2, one level up |
| **P5** | A member may additionally hold an **independent seat** — that is how "acting for itself inside this group" is expressed | §13.1 item ⑥ |
| **P6** | `policies` declares **who must consent to a party's admission** | §4.3, one level up |

**P2 is a requirement.** Gate ② asks the invitee's administrator to confirm. If the organization is not yet a participant, that administrator is asked to perform a participant's act while holding no participant's standing — the category error this profile exists to remove.

### 14.2 The three relations between a member's `home_org` and its Group

| | `home_org` points at | What it means | Accountable for the member |
|---|---|---|---|
| **①** | **a party of this Group** | the normal case under this profile | that party |
| **②** | **an organization outside the Group** | the organization vouches for the member without joining the collaboration | that organization |
| **③** | nothing | the member acts for itself, or was admitted under §4.4 | the sponsor (§4.4), or the member |

**The distinction between ① and ② is what makes "who is accountable" determinable**: a member's organization is named but its standing inside the group is not, and the four determinations of §5.3 cannot all be answered.

### 14.3 Several parties

A Group may name **several `controller`s only under the same threshold and recovery machinery as `organization-governance.md` §12.2**: the threshold must be declared, must not be satisfiable by any single party, must not fall when a party is unreachable, and a recovery rule must have existed in advance, be time-delayed and be published. A Group naming several controllers without those conditions does not satisfy §5.3 item ②, because **"who may dissolve"** would not be determinable.

---

## 15. 中文版

中文版见 [`group-collaboration-zh.md`](./group-collaboration-zh.md)。

---

*This volume states the requirements for its own subject. Identity requirements are governed by the identity binding in use; the architecture layer above it states none (`governance-architecture.md` §1.1).*
