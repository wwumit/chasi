# Cross-Organization Agent Governance — Architecture

> Status: architecture draft (v0.3)
> Date: 2026-10-03
> Position: the **architecture** layer of this family — one level above the specification volumes. It answers **why the family is shaped this way**; the volumes answer **what must hold**.
> **This document holds principles and constraints.** Where a "must" belongs, it points to the volume that owns it. See §1.1 — that rule is what keeps the two layers from becoming two sources of truth.
> **Relation to an identity binding.** This layer states no identity requirement of its own. It presupposes only that a subject is **identifiable across domains**, and names **`did:cha2a` as the worked example** its volumes are written against — an experimental draft (v1.1.0) recorded in the W3C DID Extensions registry. The requirements stay with the binding, and replacing the example changes nothing on this page.
> Related: `organization-governance.md` · `group-collaboration.md` (this repository) · `overview.md` · `agent-identity.md` · `evidence-record.md` · `did-method-cha2a.md` (the identity core, a companion repository) · `CHA2A Protocol Suite Architecture` (the layer above this one)

---

## 0. This layer's core claim

> **An organization is a governance subject; a group is a collaboration subject.**
> **Governance boundaries and collaboration boundaries are expressed separately, and neither presupposes a central trust root.**

Expanded: one agent may belong to one organization and take part in several groups; in each context, **on whose behalf it acts** is verifiable rather than asserted by a platform database.

**Why this layer needs its own claim**: it is the criterion for §3's objects, §4's levels, §5's authority shape and §7's constraints. Without it, every object proposed for the model looks equally worth keeping.

**How the three claims in this family relate** — they sit at different levels and must not contradict:

| Layer | Claim | What it is about | Where it lives |
|---|---|---|---|
| `CHA2A Protocol Suite Architecture` | mutual recognition changes no one's trust root; evidence does not depend on an operator | the promise | the design memo above this family |
| **this document** | an organization is a governance subject, a group a collaboration subject; boundaries expressed separately; no central root | **the shape** | this repository |
| `overview.md` §1 | a verifier that belongs to no party can answer four questions independently | the guarantee a verifier gets | the identity core, a companion repository |

If a change makes one of these three false, it is a change to the architecture, not a detail.

---

## 1. Status of this document

### 1.1 The division of labour between this layer and the volumes

This is the rule that keeps one governance model from having two descriptions:

| Layer | Says only | Out of bounds |
|---|---|---|
| **Architecture** — this document | why the family is layered this way · the object model · the core principles · **design constraints on the core that span the volumes** | a "must" or "should" appearing here |
| **Specification** — the volumes, and the identity binding in use | what must hold · objects, fields, rules, and the derivation of each | an explanation of *why the family is layered this way* |

**Where the two disagree, the specification governs anything normative and this document governs the "why".** A disagreement about *what must hold* is a defect to be fixed, not a state to be lived with.

### 1.2 够用判据 for this layer

**This document is complete when a reader can answer all four from this document alone:**

1. why the organization and the group are separate subjects rather than one hierarchy;
2. why no central trust root is presupposed, and what follows from that;
3. which object needs a verifiable identity, and when;
4. what the core data model may not foreclose.

Anything beyond those four is specification work and belongs in a volume.

---

## 2. Core principles

Each principle is stated with **what it settles** — not with what anyone must do.

| # | Principle | What it settles |
|---|---|---|
| 1 | **Local-first, federate-on-demand** | An agent runs on a local identity; a global one is an escalation, not a precondition. Cross-subject interoperability is what triggers stronger identity, not the other way round |
| 2 | **Identity ≠ DID** | Every agent needs an *identifiable context*; **a DID is the escalation of that context into something verifiable across domains**. This is why an object can exist and be named long before it has a DID |
| 3 | **Organization = trust / governance domain** | An organization is the unit that can be trusted or distrusted as a whole, and the unit that appoints and revokes |
| 4 | **Group = collaboration domain** | A group is a scope of work, not a sub-organization. It may span organizations, outlive any one of them, and be created by a task initiator rather than by an authority |
| 5 | **Role = a permission context; delegation = an authorization relationship; representation = who an agent acts for in a given context** | These are three different things and collapsing them is the usual source of authority bugs |
| 6 | **Registry = discovery and resolution infrastructure; the trust anchor is the verifier's own resolver** | A registry is where records are found. What a verifier trusts is the resolver it configured, which is why migration is possible |
| 7 | **Runtime-neutral** | Nothing here depends on a particular agent runtime, model vendor, or hosting platform |
| 8 | **Governance boundary and collaboration boundary are expressed separately** | Membership of an organization does not by itself confer anything inside a group, and a group role does not extend into an organization |
| 9 | **Trust roots stay where they are** | Registry migration and multiple coexisting registries are both permitted; no implementation may make cross-domain trust conditional on a record being resolvable through its own registry |
| 10 | **Records outlive their context** | Historical evidence is not deleted when a membership, an office or an organization ends — the record reflects the change rather than disappearing with it |

**Where these principles become requirements**: principles 2, 3, 8 and 10 in `organization-governance.md` and `group-collaboration.md`; 1 and 9 in `group-collaboration.md` §9 and §4.5; 6 in the **resolver contract of the identity binding in use** — `did-method-cha2a.md` §4.1 in the worked example.

---

## 3. The object model

The model has **two planes**, and they are **two views of the same objects**: the governance plane and the collaboration plane are parallel, and a group holds no organization's internals.

```
GOVERNANCE PLANE — who may act, and on whose behalf

        Principal / Controller
                 │
                 ▼
            Organization
        ┌────────┼─────────┐
        ▼        ▼         ▼
      Admin   Policies   Agents
        │                  │
        └─── Delegation ───┘     (a relationship, not a reporting line)


COLLABORATION PLANE — who acts together, and in what scope

              Group
                │
                ▼
         Membership / Role
                │
                ▼
        a member — one of:
          · an organization        a party to this collaboration
          · an agent, a human      acting for a party, or for itself
          · an external participant (sponsored, §4.4)
              each acting member carries
          · home_org  : the organization it belongs to, if any
          · capacity  : the organization it acts for here, or itself
```

**Reading of the diagram:**

- **`Organization` is the only node that owns authority.** Admin, policies and agents hang off it because they derive their standing from it, not because they are its parts.
- **An organization is a *kind of member*.** A group spanning three organizations has **three organization members**, and the acting members' `home_org` points at them.
- **The same organization therefore appears on both planes, as two different things.** On the governance plane it is a **domain** — its admins, policies and agents. On the collaboration plane it is a **party** — one participant among the group's others. **These are two perspectives on one object**: the governance plane and the collaboration plane are parallel views, and a group holds no organization's internals. **Treating one as containing the other would merge the two boundaries that §2 principle 8 keeps apart.**
- **Whether a group has organization members is conditional.** An **intra-organization group** has none, and its members' `home_org` points at the `controller`. A **cross-organization group** whose parties are themselves accountable has one organization member per party. The conditions that make the second case required are the cross-organization profile (`group-collaboration.md` §14).
- **Whether an organization is a *participant* or a *layer* is a question of standing.** An organization appearing between a group and its members is a participant **if it is enrolled, admitted, statused and removable in its own right** (`group-collaboration.md` §14.1 P1), and a layer if it is not. The difference is not cosmetic: a **layer** nests the governance boundary inside the collaboration boundary and leaves a member acting **for itself** inside the group with nowhere to stand, while **a participant** leaves both expressible.
- **`Delegation` runs sideways** between admins and agents. An authorization relationship is not a reporting line.
- **`Membership / Role` is the only edge that crosses from one plane to the other.** Admission is where a member's `home_org` — and the authority that traces back through it — is checked; the chain is `organization-governance.md` §4's subject, and the check is `group-collaboration.md` §4.
- **`Principal / Controller` sits above the organization**, because "who may act for this organization" has to terminate somewhere.

---

## 4. The three levels

| Level | Its subject | The question it owns | Specified by |
|---|---|---|---|
| **Organization** | the governance domain — who may act for a subject, and until when | *who is qualified to authorize this?* | `organization-governance.md` |
| **Group** | the collaboration domain — how parties from different domains work together | *in what context, and on whose behalf, are they acting together?* | `group-collaboration.md` |
| **Federation** | the space between registries | *how does a verifier reach a record held by a registry that is not its own?* | `group-collaboration.md` §9 |

**The three levels are peers.** Organization does not contain group, and group does not contain federation. Two organizations can collaborate with no federation: federation is optional infrastructure at the **Federation** level, not a precondition at the **Group** level. **It follows that the corresponding volumes are peers rather than a hierarchy.**

---

## 5. Where authority comes from

The shape of an authority chain, which every implementation must be able to walk:

```
① charter  ──▶  ② office  ──▶  ③ holder  ──▶  ④ root authority basis
 what it         which roles     who holds       where the first
 exists by       exist           it, when        authority came from
```

**④ is where the chain terminates**: "who authorized this" receives an answer a third party can check. A break at any layer invalidates the chain, which is why it is traced rather than asserted.

**What this document leaves to the volumes**: whether the origin needs an external issuer (it does not), what forms a charter may take, how a threshold above one controller is met, or what happens when it cannot be met. Those are `organization-governance.md` §4, §12.1 and §12.2.

---

## 6. Identity: which objects need a DID

Applying principle 2 to the model in §3:

| Object | A DID | Why |
|---|---|---|
| **Principal / Controller** | may have one | it is the terminal subject of authority; whether it needs a verifiable identity of its own depends on whether it acts across domains |
| **Organization** | when reachable across domains | it always has an identifiable context; the DID is what makes that context verifiable by a party that is not a member. See `group-collaboration.md` §4.5 |
| **Administrator / Representative** | **when acting across domains** | it performs governed actions and must be attributable for them. It is a DID plus a role plus a delegation. **Principle 2 applies to administrators exactly as it applies to organizations and agents** |
| **Agent** | when crossing domains | locally it needs an identifiable context; crossing domains is what escalates it |
| **Group** | optional, model-dependent | a group may have an independent governance identity; nothing in the model requires it |

**The table is the principle in tabular form**, and it is the reason "identity" and "DID" are not synonyms anywhere in this family.

---

## 7. Design constraints on the core

These are the constraints **that span the volumes**, because each is a property of the model as a whole. They are stated here so that no volume can quietly foreclose one.

| # | Constraint | Why it is a constraint and not a feature |
|---|---|---|
| **C1** | **The core data model must keep federation possible.** Federation may be unimplemented — MVP may run a single registry — but no field, identifier or resolution rule may make a second registry impossible to add | this is a design constraint on the core, not a capability of it. A core that cannot federate later cannot be fixed by adding a federation layer |
| **C2** | **An agent runs on a local identity** | principle 1. If running required a DID, the model would impose a global registration on every local use |
| **C3** | **Cross-domain trust rests on the verifier's own resolver configuration** | principle 9. The resolver a verifier configured is the trust anchor; a subject's registry is not |
| **C4** | **A record must remain verifiable from the record and public material alone** | a record whose truth is established by an operator's availability is not evidence |
| **C5** | **Every boundary between two parties must be expressible bilaterally** | collaboration and federation are both bilateral; introducing a mandatory intermediary would reinstate the centre the model removes |

**C1 and C3 together are what federation's 够用判据 tests.** The criterion, which this layer owns because no volume can state it alone:

> **Between two registries neither of which belongs to the other, neither side needs to change its own implementation for the other side's verifier to complete a full identity verification and a status check.**

That criterion is a *test*, not a description. It fails if the answer requires a shared schema nobody adopted, a bilateral agreement signed in advance, or an implementation change on either side.

---

## 8. Governance events and evidence

Governance actions — registration, authorization, joining and leaving an organization, joining and leaving a group, task delegation, task results, revocation — are expected to be able to form evidence. Whether they must, and in what format, is `organization-governance.md` §8 and `evidence-record.md`.

**What this layer contributes is the shape of the requirement**, not its content: audit and governance data are held separately from live runtime state, so that an audit does not depend on the running system, and so that a system going down does not take the record with it. That is C4 in §7.

---

## 9. Premises this architecture departs from

**Why this section exists**: writing while knowing that related work exists obliges this architecture to name the premises it **departs from**. **Naming premises rather than documents is deliberate** — a premise is a claim about an *approach*, which any reader can check against whatever systems they know, while a document citation dates. Recording *which* documents hold *which* premise, at what version and what status, is a **survey**, and it belongs to the ecosystem matrix of the protocol-suite architecture rather than to this layer. Naming no object is also why the status-recording obligation of the family's reading conventions (`overview.md` §5) is not triggered here.

| # | The premise | Where it is common | What importing it would break |
|---|---|---|---|
| **D1** | **Authority is produced by an issuer** — an authority chain begins with an entity that exists before the organization does | institutional-governance models | §5's layer ④. A **self-constituted organization** would have no verifiable origin, and "who authorized this" would have no answer reachable without an external party |
| **D2** | **Mutual recognition requires a prior agreement** — two parties can rely on each other only after a treaty, a published trust list, or a conformance requirement | federation models | collaboration would **need a treaty before it could begin**; federation would turn from optional infrastructure into a **precondition** for the collaboration level; C5 fails |
| **D3** | **The registry that issued an identity is the trust root** — an identity is inseparable from the deployment that holds it | registry-mediated identity systems, **including the ones closest to this architecture** | migration becomes impossible, and a record's resolvability through the operator's own registry becomes a precondition for cross-domain trust — **C1 and C3 both fail** |
| **D4** | **Assurance is a count of agreeing authorities** — a high level means several authorities have co-signed | trust-credential systems | a single-operator deployment would be **capped below the top level**, and the level would mean "how many agreed" rather than "what has been verified". **This architecture computes levels from registered metadata and leaves *which levels to accept* to the verifier's own policy** |
| **D5** | **A record's truth holds only while its issuer's system is up** | most operational systems | evidence would stop being evidence. **C4 is the constraint that prevents it** |

**A federation level is defined within one credential scheme.** It relates authorities that share a proof format and an authority model; it establishes nothing about a different scheme's levels. **This architecture derives cross-scheme trust from the verifier's own configuration instead**, because a verifier that belongs to no party has no authority to recognise.

---

*This document is the architecture layer of this family and is informative: it states no requirements. Each requirement lives with the volume that owns it (§1.1); identity requirements live with the identity binding in use.*
