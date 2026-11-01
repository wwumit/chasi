# CHASI: Compliance Hub for Agent Society Infrastructure

**Specifications for cross-subject identity, authority and evidence in an agent society**

> **CHASI documents open interfaces for cross-subject identity, authority, evidence and governance.**

## Problem and objective

**The central object of this repository is the Agent Society.** It is an operating environment composed of people, organizations, agents and groups that requires cross-subject governance and interoperability. AI systems are moving from generating information toward discovering services, communicating, collaborating, making decisions, accepting delegated authority and acting on behalf of a subject.

CHASI studies the governance and interoperability infrastructure this environment requires, including **identity, trust, authority, relationships, evidence and accountability** across subjects.

**CHASI is not another agent protocol, and it is not a regulator.** It connects existing protocols and standards and adds governance, evidence and accountability interfaces for cross-organizational use.

**At the document level, the core division is:** *an organization is a governance subject; a group is a collaboration subject.* Governance boundaries and collaboration boundaries are **expressed separately**, and **neither presupposes a central trust root**.

## What is in this repository

| Layer | Document | Version |
|---|---|---|
| **L1 · vision** | [`chasi-vision-en.md`](./vision/chasi-vision-en.md) — English | v2.26 |
| | [`chasi-vision-zh.md`](./vision/chasi-vision-zh.md) — 中文 | v2.26 |
| **L2 · architecture** *(states no requirements)* | [`protocol-suite-architecture.md`](./architecture/protocol-suite-architecture.md) · [`-zh`](./architecture/protocol-suite-architecture-zh.md) — the upper architecture | v0.2 |
| | [`governance-architecture.md`](./architecture/governance-architecture.md) · [`-zh`](./architecture/governance-architecture-zh.md) | v0.3 |
| | [`compliance-hub-architecture.md`](./architecture/compliance-hub-architecture.md) · [`-zh`](./architecture/compliance-hub-architecture-zh.md) | v0.1 |
| **L3 · specifications** | [`overview.md`](./specs/overview.md) · [`-zh`](./specs/overview-zh.md) — **the entry to this layer, and to the family** | v0.3 |
| | [`organization-governance.md`](./specs/organization-governance.md) · [`-zh`](./specs/organization-governance-zh.md) | v0.2 |
| | [`group-collaboration.md`](./specs/group-collaboration.md) · [`-zh`](./specs/group-collaboration-zh.md) | v0.2 |
| | [`question.md`](./specs/question.md) · [`-zh`](./specs/question-zh.md) | v0.2 |
| | [`naming.md`](./specs/naming.md) · [`-zh`](./specs/naming-zh.md) | v0.4 |
| | [`passport.md`](./specs/passport.md) · [`-zh`](./specs/passport-zh.md) — the Passport object | v1.2 |
| **L4 · profiles** | [`assembly.md`](./profiles/assembly.md) · [`-zh`](./profiles/assembly-zh.md) | v0.3 |
| | [`lexicon.md`](./profiles/lexicon.md) · [`-zh`](./profiles/lexicon-zh.md) | v0.3 |
| | [`compliance-profile.md`](./profiles/compliance-profile.md) · [`-zh`](./profiles/compliance-profile-zh.md) | v0.1 |
| | [`registry-interop.md`](./profiles/registry-interop.md) · [`-zh`](./profiles/registry-interop-zh.md) | v0.1 |
| | [`agent-card-identity.md`](./profiles/agent-card-identity.md) · [`-zh`](./profiles/agent-card-identity-zh.md) | v0.1 |
| **L5 · evidence and conformance** | *not in this repository* — evidence lives in `did-method-cha2a`; conformance vectors and checkers in `cha2a-conformance` | — |
| **L6 · implementation and operation** | *not in this repository* — implementations live in their own repositories | — |
| **L7 · method** | [`use-case-laboratory.md`](./method/use-case-laboratory.md) · [`-zh`](./method/use-case-laboratory-zh.md) | v1.0 |
| | [`ecosystem-matrix.md`](./method/ecosystem-matrix.md) · [`-zh`](./method/ecosystem-matrix-zh.md) | v0.1 |
| **L8 · distribution** | *not in this repository* — distribution is dated per delivery and is not kept here | — |

**Which layer owns what.** L1 states the vision. **L2 states no requirements** — where a "must" belongs, it points at the volume that owns it (`governance-architecture.md` §1.1). L3 states the requirements, each volume for its own subject. L4 holds profiles over the layers below. L5 holds conformance vectors and checkers. L6 holds implementations and operations. L7 holds the method — how an experiment is designed, run and recorded. L8 holds what is delivered outward. **`specs/overview.md` is the family's entry document**; the table above is **this repository's** layer index. They are not alternatives: the entry says what the family is, the index says what this repository holds. **The "eight layers" above are not the same set as the upper architecture's "eight layers"**: the upper architecture (`protocol-suite-architecture.md` §4) splits the **protocol suite's functional layers** (CHA2A Core · Governance · Passport & Interoperability · Group & Collaboration · Federation · Evidence & Trust · Marketplace / Commerce · Workflow / Task); the table above is **this repository's layer index**. Same name, different things.

**Every layer is either present or accounted for.** L5, L6 and L8 are empty *here* by decision, not by omission: L5 is held by **two** companion repositories (evidence in `did-method-cha2a`, conformance in `cha2a-conformance`), L6 by the implementations' own repositories, L8 is dated per delivery. **L4 now holds five profiles**: assembly, lexicon, compliance, Registry interoperability and Agent Card identity; the high-grade ecosystem trust state stays reserved until at least two independent real verifiers exist.

**The identity core is elsewhere.** Identity, evidence and the DID method itself live in the companion repository **`did-method-cha2a`**; implementations live in their own repositories.

**The ledger is not here.** Internal work plans, version plans, ledgers and distribution material are kept outside this repository — see "What belongs in this repository" below.

### A note on the Vision's two editions

**One document, two languages, one version.** The Chinese edition is the source text and the English is its translation; both carry **the same version and the same twenty sections in the same order**. A divergence between them is a **defect to be fixed**, not two different emphases.

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

## Document order

| Order | Document | What it answers |
|---|---|---|
| 0 | `vision/chasi-vision-en.md` | what this is for, and what kind of society it assumes |
| 1 | this document | what this repository holds, and how the layers divide |
| 2 | `governance-architecture.md` | why the family is shaped this way |
| 3 | `organization-governance.md` | **who is qualified to authorize it** |
| 4 | `group-collaboration.md` | how agents of different organizations work together |
| 5 | `naming.md` | where names come from, and why a reference must carry a check basis |
| 6 | `question.md` | **what counts as having answered the four questions, and who judges** |
| 7 | `method/use-case-laboratory.md` | **which scenarios stress the architecture, and what an experiment must produce** |

## Language convention

English-first for the architecture layer and the volumes: each carries a Chinese edition with a `-zh` suffix. **The Vision is the exception** — see the note above; its English and Chinese editions are different versions, and the Chinese is ahead.

## Status

Experimental drafts. Each specification volume states requirements for its own subject; the architecture layer states none.

## Participation and change control

- **Licence**: Apache License 2.0 (see `LICENSE`).
- **Participation**: via GitHub issues / PRs.
- **Contribution rules**: [`CONTRIBUTING.md`](./CONTRIBUTING.md).
- **Security reports**: [`SECURITY.md`](./SECURITY.md), using private reporting
  rather than a public issue.
- **Conduct**: [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md).
- **What belongs in this repository**: **only material intended for publication.** "Not yet public" means *not yet ready for publication*, not a place to park things that should not be published. Work plans, version plans, ledgers, internal reviews and distribution material are kept elsewhere and do not enter it, in any directory and at any revision.
- **Change discipline**: a substantive change to a volume bumps that volume's version. A note describing what changed is written **only once the version it supersedes has been public** — before that, the iteration is not narrated. Editing and links may be committed on their own.
- **Review cadence**: items left to the deploying parties, and any question a volume does not answer, are revisited when that volume is version-bumped.
- **Reference deployment of the worked binding**: `https://compliancehub.cn`.
