# Cross-Organization Agent Governance

> **On this repository's name.** `authority-provenance` names the subject of the layer these volumes add: **where a subject's authority comes from, and how a third party traces that back independently.** The volumes carry the two subjects that make it operable — the **Organization** as a governance subject and the **Group** as a collaboration subject (`governance-architecture.md` §0).

Documents for agents that act **across organizational boundaries**: the **Organization** as a governance subject, and the **Group** as a collaboration subject.

## Core claim

> **An organization is a governance subject; a group is a collaboration subject.**
> **Governance boundaries and collaboration boundaries are expressed separately, and neither presupposes a central trust root.**

An agent may belong to one organization and take part in several groups. In each context, **on whose behalf it acts** is verifiable rather than asserted by a platform database.

## Documents

| Document | Version | Content |
|---|---|---|
| [`governance-architecture.md`](./governance-architecture.md) · [`-zh`](./governance-architecture-zh.md) | v0.3 | **The architecture layer.** Why the family is shaped this way: the core principles, the two-plane object model, the three levels (organization · group · federation), the constraints on the core, and the premises this architecture departs from. **States no requirements**; every "must" points at the volume that owns it |
| [`organization-governance.md`](./organization-governance.md) · [`-zh`](./organization-governance-zh.md) | v0.1 | **The Organization as a subject.** The four-layer source of authority (charter → office → holder → root authority basis), membership and belonging, non-grantable roles, lifecycle (departure · succession · re-rooting · break-glass · dissolution), the evidence of governance actions, and **what this volume fixes versus what the deploying parties choose (§12)** |
| [`group-collaboration.md`](./group-collaboration.md) · [`-zh`](./group-collaboration-zh.md) | v0.1 | **The collaboration context.** Group as a first-class object, the three admission gates, the cross-organizational rules (no scope widening · revocation cascade · accountability), lifecycle, Presence, the Chat/Task relationship, **cross-registry resolution (§9)**, and the optional **cross-organization profile (§14)** |
| [`CHANGELOG.md`](./CHANGELOG.md) | — | Revision history |

**The architecture layer is not a specification.** It holds the principles and the object model; a "must" appearing there is out of bounds (`governance-architecture.md` §1.1).

**The two volumes are peers**, not a hierarchy: one answers *who is qualified to authorize this*, the other *in what context, and on whose behalf, are they acting together*. An organization exists without agents, and a collaboration spans organizations.

## Relation to an identity binding

These volumes state **no identity requirement of their own**. They are written against an **identity binding** — something that resolves a subject across domains and answers for its status — and name **`did:cha2a` as the worked example** (experimental draft v1.1.0, recorded in the W3C DID Extensions registry).

| The binding supplies | Where it is used |
|---|---|
| cross-domain resolution of an organization or a member | `organization-governance.md` §10 · `group-collaboration.md` §4.5, §9 |
| a status and revocation answer | `group-collaboration.md` §5.2, §9.2, §11 |
| a verifiable tier per subject | `group-collaboration.md` §4.1 gate ① |

Identity, evidence and the DID method itself live in the companion repository **`did-method-cha2a`**. Every interface point is listed in §10 or §11 of the volume that exercises it, so a different binding satisfying them can take the example's place.

## Reading order

| Order | Document | What it answers |
|---|---|---|
| 0 | this document | what this family is for, and what it holds |
| 1 | `governance-architecture.md` | why the family is shaped this way |
| 2 | `organization-governance.md` | who is qualified to authorize it |
| 3 | `group-collaboration.md` | how agents of different organizations work together |

## Language convention

English-first. Each volume carries a Chinese edition with a `-zh` suffix — this document's is [`README-zh.md`](./README-zh.md). The two editions state the same rules, and their section headings and § references correspond one to one.

## Status

Experimental drafts. Each volume states requirements for its own subject; the architecture layer states none.

## Provenance

These three volumes were written inside the CHA2A specification group and moved here so that the governance model reads without assuming a particular DID method. §11 of the method specification — its companion index, which is not edited — lists `evidence-record.md`, `agent-identity.md` and `EVIDENCE.md`, and has never listed these volumes, so the move changed no reference in it. `CHANGELOG.md` records the move.

## Participation and change control

- **Licence**: Apache License 2.0 (see `LICENSE`).
- **Participation**: via GitHub issues / PRs.
- **Change discipline**: a substantive change to a volume bumps that volume's version and states its reason in `CHANGELOG.md`; editing and links may be committed on their own.
- **Review cadence**: items left to the deploying parties, and any question a volume does not answer, are revisited when that volume is version-bumped.
- **Reference deployment of the worked binding**: `https://compliancehub.cn`.
