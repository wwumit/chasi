# Organization Governance — the Governance Volume

> Status: draft (v0.2)
> Date: 2026-10-01
> Position: this family's volume on the **Organization as a subject** — **a peer of** `group-collaboration.md` (this repository) and of `agent-identity.md` and `evidence-record.md` (the identity core, a companion repository). It defines the **source of authority**, membership and belonging, and the evidentiary record of governance actions
> Principle: **if an existing standard can be used, do not invent one** — authority decomposes into four verifiable layers (charter → office → holder → root authority basis), stated in §4 as this volume's own answer; evidence of governance actions cites `evidence-record.md`.
> **Relation to an identity binding.** The rules below are written against an **identity binding that can name a subject across domains**; **`did:cha2a` is the worked example** (experimental draft v1.1.0, recorded in the W3C DID Extensions registry), and every field is stated so that another binding satisfying §10's interface points can take its place.
> Related: `group-collaboration.md` (this repository) · `agent-identity.md` §7 (delegation and authorization scope) · `evidence-record.md` (evidence format) · `overview.md` (family entry) · `did-method-cha2a.md` (the worked identity binding)

---

## 1. The problem, and the approach

**The problem**: §7 of `agent-identity.md` already defines that "an agent's authorization scope is declared by its **controller**". But **nothing defines what the controller's authority rests on**.

An organization can register a DID, revoke a member, amend a policy, approve cross-organizational admission — **where does the authority for these actions come from?** **A platform designates the administrator, and that designation is the whole of the authority.** It has three consequences:

1. authority is not traceable — after an incident, no one can say "who granted that authority in the first place";
2. when an organization changes its responsible person, the old permissions are left dangling;
3. when a member leaves, there is no rule for whether the authorizations it derived fall away with it.

**The way out**: define the Organization as a **subject whose source of authority is traceable** — not "an entry in a platform", but **the origin of an authorization chain that can be verified independently**.

**This volume's responsibility**:
1. define the Organization object and its fields;
2. define the **four-layer source of authority** (the core of this volume);
3. define members, roles and belonging;
4. define the evidentiary record of governance actions;
5. **cites rather than restates**: identity and the identity binding in use (`did-method-cha2a.md` in the worked example), the semantics of delegation and authorization scope (`agent-identity.md` §7), the evidence format (`evidence-record.md`), and the collaboration process (`group-collaboration.md`).

---

## 2. The four-layer chain

**This volume's answer to its own question.** "Where does an institution's authority come from" decomposes into four layers that must each be verifiable, and the chain breaks at the first one that is not. **The four layers themselves, and what each requires, are in §4** — this section fixes only what §4 does not cover: the two premises on which this volume parts ways with an authority-issuer model.

| | Adopted | Not adopted |
|---|---|---|
| Structure | the four-layer chain | — |
| Premise | **an internal charter is accepted as the basis**, so the origin may be self-attested | the premise that an external issuer must grant the authority |

The premise row is where this volume departs from an authority-issuer model: that model begins from an issuer that already exists, and this volume does not require one. **That difference is the deliverable.** The price is that the *origin* itself must be stated clearly (see §4).

---

## 3. The Organization object

| Field | Type | Required | Note |
|---|---|---|---|
| `org_id` | string | yes | stable identifier |
| `org_did` | did | **when reachable across domains** | the **cross-domain escalation** of `org_id`, written `did:cha2a:org:<id>` under the worked identity binding. An organization addressed only from inside its own domain needs none; how a counterparty resolves and verifies it is `group-collaboration.md` §4.5 |
| `charter_ref` | list of `{hash, uri?, effective_from}` | yes | the **charter basis, versioned** (see §4 layer ①). At least one entry; each entry's `hash` is the check basis and `uri` is a locator only. An amendment **appends** an entry — it never rewrites one |
| `controllers[]` | list | yes | who holds root authority. **At least one**; where there is more than one, the combination rule must be stated |
| `root_authority_ref` | list of `{hash, uri?, effective_from}` | yes | **the carrier of layer ④, "root authority basis"** — where that first authority came from. Same shape as `charter_ref`: each version carries a `hash` (the check basis) and an `effective_from`; **a platform default is not allowed** (§4 layer ④) |
| `roles[]` | list | yes | role definitions: `role_id` · `scope` · `assignable` (see §6) |
| `members[]` | list | yes | each: `member_id` · `did` · `kind` · `role_refs[]` · `joined_at` · `status` |
| `policies_ref` | uri \| hash | no | reference to the policy file |
| `registry_authority` | list of `{uri, from, to?}` | yes | which registry carries this organization's data, **as a history with time ranges** — not a current value. At least one entry; the last entry has no `to`. **Migration is allowed** (decoupled from the trust root), and a verifier needs only to know *which registry carried this DID during which period* |
| `status` | enum | yes | `active` · `suspended` · `dissolved` |

**Sufficiency criterion**: a verifier that **does not belong to this Organization**, given only the fields above, the versions pointed to by `charter_ref`, and the credentials each member holds, can independently reconstruct "**who was entitled, at what time, to do what on behalf of this organization**".

---

## 4. Where authority comes from (the core of this volume)

Four layers; **every layer must be verifiable**, and a break at any layer invalidates the whole chain.

| # | Layer | The question it answers | Requirement |
|---|---|---|---|
| **①** | **Charter** | what this Organization exists by virtue of | must point to a **verifiable, versioned basis**: each version carries a **hash** (the check basis) and an **`effective_from`** date, with a `uri` optionally alongside as a locator only. An appointment records **which version it was made under**, so a verifier can answer *"was that version in force at the time?"* — a single hash proves *which document*, not *which basis was in force*. **The content of a charter is the organization's own affair**; the requirement is that the basis exists, is verifiable, and is versioned |
| **②** | **Office** | which roles exist, and what each may do | role and permission context are **expressed separately**; **an office is a post that holders fill for a bounded period** |
| **③** | **Holder** | who holds it, and from when to when | holding office is a **time-bounded relationship**, not a permanent attribute; appointment and removal must be recorded as evidence |
| **④** | **Root authority basis** | where that first authority came from | must point to a **verifiable origin**. **It may not be "the platform's default"** — a platform default is not verifiable, which is the same as having no origin |

The layer names are the conventional ones.

**Sufficiency criterion (carrying §3 forward)**: the verifier can trace back through the four layers **to the origin independently**, **without contacting any platform**.

> **One thing that must be nailed down**: if ④'s origin can only be supplied by a platform, then §3's sufficiency criterion can never hold. **This is the dividing line between "traceable" and "platform assertion".**

**What this criterion leaves to contract and law**: it answers *whether the holder is entitled to act for that organization*. It does **not** establish that two organizations are bound to each other. Bindingness is a matter of contract and law, outside this family (§12.1 item 5); what this volume requires is that one party's **acceptance** of another party's representative is recorded as a governed action (§8) — that record is what will be produced when the question is asked.

---

## 5. Members and belonging

### 5.1 Kinds of member

At least three kinds are distinguished (consistent with the membership model in `group-collaboration.md` §4):

| Kind | Note |
|---|---|
| `human` | a natural-person member |
| `agent` | an agent member owned by the organization |
| `external` | a non-member (cross-organizational participant, or an outsider with no DID) — **always handled as cross-domain** |

### 5.2 Expressing belonging

- **Every member *of this organization* must have an explicit belonging** (`org_id` may not be empty) — *within an organization*, a member without a belonging does not exist. **This scope matters**: it is a rule about the organization's own membership, not about participants everywhere. A **Group** member may carry **no `home_org`**, and that is a legitimate case with its own path (`group-collaboration.md` §4.4);
- **"On whose behalf" must be distinguishable**: whether an agent is acting **for the Organization** or **for itself** in a given context must be determinable. The two authorities are **not combined** (see `group-collaboration.md` §5.1 item ③);
- **Belonging and authority are separate**: joining an organization grants no role automatically.

### 5.3 Division of labour with §7 of `agent-identity.md`

| Volume | Answers |
|---|---|
| `agent-identity.md` §7 | **what the agent may do** (authorization scope, scope, delegation chain) |
| **this volume** | **who is entitled to declare it** (the Organization's source of authority, the recognition of a representative) |

**⇒ Each answers a different question: one governs "the scope that was granted", the other governs "the grantor's qualification".**

---

## 6. Roles, and roles that cannot be granted

### 6.1 Roles

An Organization may hold several roles, for example: administrator · agent management · security · group management · audit. Role and permission context are expressed separately; a member may hold several roles (**each governed by its own scope; they are not combined**).

### 6.2 Roles that cannot be granted

**Convention: non-grantable roles are expressed as structural prohibitions — they do not enter a weight comparison and cannot be overridden by a higher weight; they are not given a large number.**

At least two kinds must be included:

| # | Non-grantable | Note |
|---|---|---|
| ① | **Root authority itself** | root authority cannot be granted or acquired by an ordinary role; changing it is an **explicit re-establishment action** (see §7.4) |
| ② | **"Granting permissions to oneself" as a class of action** | no role may widen its own permissions, or those of a subject it derived; **including widening them by omitting a field** |

> **"Field absent means not permitted"** — writing nothing means nothing, not infinity. This is the same principle as §5.1 item ① of `group-collaboration.md`.

---

## 7. Lifecycle

The original draft handled only one case: a member leaving. The four states below take their defaults in the **conservative** direction.

### 7.1 Four continuity rules (rules first, then actions)

| # | Rule | Meaning |
|---|---|---|
| **L1** | **Identity continuity ≠ authority continuity** | the identity still existing does not mean the permissions still exist |
| **L2** | **A successor does not inherit the predecessor's delegation tree** | a change of person requires fresh authorization |
| **L3** | **Re-delegation produces new authority** | validity cannot be extended by "citing the old authorization" |
| **L4** | **Independent chains do not merge** | two unrelated authorization chains may not be added together to produce a new permission |

> **Scope of L4**: it governs chains from **different roots**. It says nothing about the internal composition of a single root — how many controllers it has, or what threshold they use (§12.2). Two of the corrections in §12.1 are precisely this boundary having been drawn too widely.

### 7.2 Departure / stepping down

**All derived authorizations of that holder fall away with it**; permission **may not be retained because "the identity still exists"** (L1). Historical evidence is **not deleted** — it only reflects the lifecycle change.

### 7.3 Succession / handover

A successor **does not inherit** the predecessor's delegation tree (L2); fresh authorization is required (L3); **the handover action itself must be recorded as evidence** (§8).

The same rule covers **absorption**: when an organization is absorbed by another, its holders are **re-appointed under the surviving root** rather than carried across (§12.1 item 9).

### 7.4 Re-rooting

When the root authority is replaced:

1. **credentials issued by the old root must be explicitly disposed of** — either revoked or re-signed, choose one and record it;
2. **two roots may not coexist for long without a declaration**;
3. the re-rooting action itself is recorded as evidence, together with the reason;
4. **re-rooting is itself a root-level action.** Where several controllers exist it needs the declared threshold; where the threshold is unreachable it proceeds **only under the recovery rule the charter declared in advance** (§12.2). It may **never** be performed by improvising a lower threshold.

### 7.5 Break-glass

Only **time-bounded, scope-bounded, and subject to mandatory post-hoc review** overrides are permitted.

**It may not be a silent, standing channel.** Test: if a break-glass action cannot later be identified by a third party as "this was an emergency action", it does not conform to this volume.

Three clarifications, because a directly stated version of this rule fails exactly where the rule is needed most:

1. **The reviewer's qualification is not "external" but "not the beneficiary, and entitled to see the evidence".** Where no such person exists inside the organization — three people, one controller — **a counterparty in the Group may serve as a lawful reviewer**: but the visibility is not granted automatically — item ③ of §5.3 in `group-collaboration.md` (**who can see the full audit**) is a **declaration item** for the Group, and absent a declaration that volume's conservative default applies (missing means not allowed). **For an organization to use this path, the Group must declare item ③.** Requiring an *external* reviewer would make break-glass unavailable in precisely the organizations that need it.
2. **"Unreviewed" is an absence read off the chain**, rather than an entry somebody writes. A verifier that finds a break-glass with no corresponding review record has found an unreviewed one. Nothing needs to be written for this to be true, which is why the rule does not depend on an actor who may not exist.
3. **Authorizations granted under break-glass lapse at their own time limit**, whether or not a review happened; renewal goes through the ordinary authorization path.

**An unreviewed break-glass must be visible in the status query** (`trust/query` under the worked identity binding; `group-collaboration.md` §11), so that a party deciding on admission can see it. **This volume makes it visible and attaches no score**; what a counterparty does with it is the counterparty's decision.

### 7.6 Dissolution

1. **credentials are revoked, not deleted**, and historical evidence is **retained** — it records only that the organization dissolved;
2. **the DID stays resolvable and returns `dissolved`.** It may not become unresolvable: **"dissolved" and "not found" must stay distinguishable**, because a verifier's fail-closed behaviour depends on exactly that distinction. A DID that returns 404 is indistinguishable from one that never existed, and this volume does not permit that ambiguity (§12.1 item 4);
3. the dissolution action is recorded as evidence, with its effective time.

---

## 8. Governance actions and their evidentiary record

The following actions **must be recorded as evidence** (format cited from `evidence-record.md`, not invented here):

| Action | At minimum record |
|---|---|
| Register / revoke an agent | who · when · by virtue of which office |
| Member joins / leaves | who approved · in what role · start and end |
| Grant / revoke an authorization | granted to whom · scope · term · basis |
| Role change | before and after · approver |
| Policy change | before and after · version · approver |
| Re-rooting / handover | basis · old and new root · disposal of old credentials |
| Break-glass | trigger reason · scope · time limit · post-hoc review conclusion |
| **Accepting another organization's representative** | which representative · on whose behalf · the scope accepted · the basis verified · who accepted · from when to when |

**One hard requirement**: the audit chain **secures evidence by hash, leaving content outside the chain** — only the minimum necessary goes on the chain (hash + type + handle + time); the content may be deleted, and **"the content was deleted" is itself recorded as an audit event**.

**Sufficiency criterion**: the evidence of a governance action can have its authenticity and timeliness verified by a third party **without depending on any party's system availability**.

---

## 9. Dependencies and deferred work

**What this volume depends on.** The external dependencies shared with the identity core are listed once, in `overview.md` §4.2. The interface points this volume exercises — the identity binding for the organizational identifier, `evidence-record.md` for the format of governance evidence, and `group-collaboration.md` §4.5 for how an organization is identified across domains — are in §10.

**Nothing in this volume is deferred to a future version.** What falls outside it is held by a named companion (§10), not by a later release of this one.

---

## 10. Interfaces to existing mechanisms

| Existing mechanism | Interface point |
|---|---|
| the identity binding (worked example: `did-method-cha2a.md`) | registration and resolution of the organizational identifier (`did:cha2a:org:<id>`); **it is decoupled from the registry authority and may migrate**; `registry_authority` is kept as a **time-ranged history**, so an old credential still resolves to the registry that carried it then (§12.1 item 7). **How a counterparty resolves and verifies an organization is `group-collaboration.md` §4.5** |
| `agent-identity.md` §7 | delegation and authorization scope are defined there; this volume supplies the "grantor's qualification" |
| `evidence-record.md` | all governance actions in §8 **use the Evidence Record format uniformly** |
| `group-collaboration.md` | that volume's membership model and three admission gates depend on this volume's "who may represent the organization" |
| status query of the identity binding (worked example: `trust/query` of `did:cha2a`) | to check organization and member status; **fail-closed when offline** |
| `nationalStandardId` (`agent-identity.md` appendix) | an organization that needs to map to a regional identity-code scheme uses the same mechanism |

**One cryptographic implementation, serving four places**: identity credentials, governance-action evidence, collaboration records, and card signatures — all share one stack (JWS + JCS canonicalization).

---

## 11. Reference implementation

- Reference registry: `https://compliancehub.cn` (see `README.md`)
- Minimum loop: one organization → registered by virtue of a charter → a controller named → two roles appointed → one agent joins as an `agent` member → one grant → one revocation → every action drillable to evidence

**Acceptance criteria**:
1. a verifier that **does not belong to this organization** can trace back to the origin of authority through the four layers of §4 **without contacting any platform**;
2. four negative paths **must go red**: flip one byte / swap the kid / mismatched organization domain / already revoked;
3. **each of L1–L4 has one counter-example test** (for example: the identity remains but the permission must lapse; a successor citing the predecessor's authorization must be rejected).

---

## 12. Fixed by this volume, and left to the deploying parties

This volume leaves **every requirement decided**. It draws one line: between what the protocol fixes and what a deploying party chooses. Each fixed item states the principle it is derived from, so a reader can challenge the derivation rather than the conclusion.

### 12.1 Fixed by this volume

| # | Item | Fixed by this volume | Derived from |
|---|---|---|---|
| 1 | The verifiable form of a charter | `charter_ref` is a **versioned basis**: each entry carries a **hash** (the check basis) and an **`effective_from`** date, optionally a `uri` (locator only), and every appointment records the version it was made under. A single hash would prove *which document*, not *which basis was in force* when the appointment was made | §4 layer ① + layer ④ "a platform default is not an origin" |
| 2 | Combination rule for several controllers | The threshold for root-level actions is a **charter-declared** parameter. **L4 governs chains from different roots**; co-controllers of one root are one root, and a k-of-n threshold does not merge independent chains. Three things are fixed: it must be declared, it must not be satisfiable by **any single controller**, and an unavailable controller **never lowers it** | L4 (scope stated in §7.1) + §7.4 + §12.2 |
| 3 | Who reviews a break-glass action | The reviewer must be **not the beneficiary** and **entitled to see the evidence**; where no such person exists inside the organization, **a counterparty in the Group may serve** — but only if that Group has **declared** its audit visibility under `group-collaboration.md` §5.3 item ③ (that volume's default is "missing means not allowed", so it is not granted automatically). Authorizations lapse at their own time limit and do not renew automatically, regardless of review. An unreviewed break-glass is an **absence read off the chain**, not an entry, and must be **visible in the status query** — with no score and no rating attached | §7.5 + `group-collaboration.md` §5.3 item ③ and §11 |
| 4 | Disposal of credentials and evidence on dissolution | Credentials are **revoked, not deleted**; historical evidence is **retained**. The DID **stays resolvable and returns `dissolved`** — a 404 is indistinguishable from a DID that never existed, and a verifier's fail-closed behaviour depends on that distinction | §7.2 + §7.6 + §8 |
| 5 | Mutual recognition of an organizational representative | **Recognition is the four-layer traceback of §4.** The four-layer traceback of §4 is the technical answer; **whether the organizations are contractually bound is outside this family**. What the volume requires is that **one party's acceptance of another's representative is recorded as evidence** | §4 sufficiency criterion + §8 |
| 6 | Minimum role set | **Roles are custom.** Only the two non-grantable classes in §6.2 are fixed | §6.2 structural prohibitions + §4 layer ④ |
| 7 | Continuity of evidence across registry migration | Continuity follows from **the evidence chain** — which holds only because `registry_authority` is kept as a **history with time ranges**, so a verifier can tell which registry carried the DID during which period. The migration record carries old carrier · new carrier · effective time | §3 + §8 sufficiency criterion |
| 8 | Charter amendment | An amendment **appends a version** carrying its own `effective_from`; existing appointments stay valid because their basis is the version in force when they were made. Amendment is a governed action and must be recorded. If it changes the root authority basis, §7.4 applies | §4 layer ① + §7.4 + §8 |
| 9 | Mergers | Two shapes are admissible and **neither pools authority**: one entity survives — root unchanged, absorbed holders **re-appointed** under §7.3, absorbed credentials disposed of per §7.4 item 1 — or a new entity is chartered and both predecessors dissolve. **A merger requires every credential to be re-signed or revoked**, or it becomes a lawful wrapper for forged credentials. **Legal succession is outside this family** | L4 (scope stated in §7.1) + §7.3 + §7.4 |

### 12.2 Left to the deploying parties

Semantics fixed here; only the value is the deploying parties' choice.

| Parameter | Fixed by this volume | Chosen by |
|---|---|---|
| Threshold for root-authority actions when there are several controllers | it must be **declared**; it must **not be satisfiable by any single controller**; an unavailable controller **never lowers it** | the values of k and n |
| **Recovery rule for when the threshold is unreachable** | it must **exist in the charter in advance**, be **time-delayed**, and be **published**. Improvising a lower threshold at the moment of need is the attack, not the remedy | its shape and its delay |
| Who reviews a break-glass invoked by the root authority | must **not be the beneficiary** and must be **entitled to see the evidence**; a counterparty in a shared Group qualifies | whether the charter names one, or leaves it to the Group |

**The same machinery governs a Group with several parties.** A group that names more than one controller reuses this table rather than inventing a threshold of its own (`group-collaboration.md` §14.3) — so a consortium's joint governance is the same problem as a multi-controller organization's, solved once.

**Nothing in this volume is deferred.** What falls outside it is handed to a named companion (§9), not to a future version of itself.

## 13. 中文版

中文版见 [`organization-governance-zh.md`](./organization-governance-zh.md)。

---

*This volume states the requirements for its own subject. Identity requirements are governed by the identity binding in use; the architecture layer above it states none (`governance-architecture.md` §1.1).*
