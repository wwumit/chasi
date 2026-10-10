# CHASI: Compliance Hub for Agent Society Infrastructure

**Toward a Governed, Interoperable and Human-Centric Agent Society**

> **We envision an Internet where humans and autonomous agents can participate, cooperate, transact and coexist through open, trusted and governed social infrastructure.**
> — *CHASI Vision*, closing statement

## The stance

**The next transformation is not simply better AI, but the emergence of an Agent Society.** Artificial intelligence is moving from models that generate information toward autonomous agents that can discover services, communicate, collaborate, make decisions, delegate authority, transact, and act on behalf of humans and organizations.

CHASI proposes a vision for the **social infrastructure** that society then needs: an open, interoperable and governed environment in which humans, agents, organizations and groups can establish **identity, trust, authority, relationships, evidence and accountability**.

**CHASI is not another agent protocol, and it is not a regulator.** It complements and connects existing protocols and standards, and fills the governance and social-infrastructure layer that becomes necessary when agents move from isolated tools to persistent participants in an Internet-scale society.

**Its core claim, in one line** — *an organization is a governance subject; a group is a collaboration subject.* Governance boundaries and collaboration boundaries are **expressed separately**, and **neither presupposes a central trust root**.

## What is in this repository

| Layer | Document | Version |
|---|---|---|
| **L1 · stance** | [`chasi-vision-en.md`](./vision/chasi-vision-en.md) — English | v1.1 |
| | [`chasi-vision-zh.md`](./vision/chasi-vision-zh.md) — 中文 | v1.3 |
| **L2 · architecture** *(states no requirements)* | [`governance-architecture.md`](./architecture/governance-architecture.md) · [`-zh`](./architecture/governance-architecture-zh.md) | v0.3 |
| **L3 · specifications** | [`organization-governance.md`](./specs/organization-governance.md) · [`-zh`](./specs/organization-governance-zh.md) | v0.1 |
| | [`group-collaboration.md`](./specs/group-collaboration.md) · [`-zh`](./specs/group-collaboration-zh.md) | v0.1 |
| **L4 · profiles** | *reserved — not yet populated* | — |

**Which layer owns what.** L1 states the stance. **L2 states no requirements** — where a "must" belongs, it points at the volume that owns it (`governance-architecture.md` §1.1). L3 states the requirements, each volume for its own subject. L4 holds profiles over the layers below.

**The identity core is elsewhere.** Identity, evidence and the DID method itself live in the companion repository **`did-method-cha2a`**; implementations live in their own repositories.

### A note on the Vision's two editions

**They are not parallel editions.** Both run to 15 sections, but they are **not translations of each other**, and their middles treat **different subjects**: the English covers compatibility and the social contract, the Chinese covers the architecture, the accountability chain and societal memory. They are two **different documents**; cite each by its own version.

**A vision carries no work plan.** Neither edition states dates, deliverables or assigned actions. A roadmap is a different document with a different audience and a different lifetime.

## The governance core

**The Organization** and **the Group** are the two subjects these documents carry. An agent may belong to one organization and take part in several groups; in each context, **on whose behalf it acts** is verifiable rather than asserted by a platform database.

**The two volumes are peers, not a hierarchy**: one answers *who is qualified to authorize this*, the other *in what context, and on whose behalf, are they acting together*. An organization exists without agents, and a collaboration spans organizations.

**The architecture layer is not a specification.** It holds the principles and the object model; a "must" appearing there is out of bounds (`governance-architecture.md` §1.1).

## Relation to an identity binding

These documents state **no identity requirement of their own**. They are written against an **identity binding** — something that resolves a subject across domains and answers for its status — and name **`did:cha2a` as the worked example** (experimental draft v1.1.0, recorded in the W3C DID Extensions registry).

| The binding supplies | Where it is used |
|---|---|
| cross-domain resolution of an organization or a member | `organization-governance.md` §10 · `group-collaboration.md` §4.5, §9 |
| a status and revocation answer | `group-collaboration.md` §5.2, §9.2, §11 |
| a verifiable tier per subject | `group-collaboration.md` §4.1 gate ① |

Every interface point is listed in §10 or §11 of the volume that exercises it, so a different binding satisfying them can take the example's place.

## Reading order

| Order | Document | What it answers |
|---|---|---|
| 0 | `vision/chasi-vision-en.md` | what this is for, and what kind of society it assumes |
| 1 | this document | what this repository holds, and how the layers divide |
| 2 | `governance-architecture.md` | why the family is shaped this way |
| 3 | `organization-governance.md` | **who is qualified to authorize it** |
| 4 | `group-collaboration.md` | how agents of different organizations work together |

## Language convention

English-first for the architecture layer and the volumes: each carries a Chinese edition with a `-zh` suffix. **The Vision is the exception** — see the note above; its English and Chinese editions are different versions, and the Chinese is ahead.

## Status

Experimental drafts. Each specification volume states requirements for its own subject; the architecture layer states none.

## Provenance

The three governance volumes were written inside the CHA2A specification group and moved into their own repository so that the governance model reads without assuming a particular DID method. §11 of the method specification — its companion index, which is **not** edited — lists `evidence-record.md`, `agent-identity.md` and `EVIDENCE.md`, and has never listed these volumes, so that move changed no reference in it.

## Participation and change control

- **Licence**: Apache License 2.0 (see `LICENSE`).
- **Participation**: via GitHub issues / PRs.
- **What belongs in this repository**: **only material intended to be read.** This repository is private today, but it is private *until it is ready to be read* — not a place to park things that should not be published. Work plans, version plans, ledgers, internal reviews and distribution material are kept elsewhere and do not enter it, in any directory and at any revision.
- **Change discipline**: a substantive change to a volume bumps that volume's version. A note describing what changed is written **only once the version it supersedes has been public** — before that, the iteration is not narrated. Editing and links may be committed on their own.
- **Review cadence**: items left to the deploying parties, and any question a volume does not answer, are revisited when that volume is version-bumped.
- **Reference deployment of the worked binding**: `https://compliancehub.cn`.
