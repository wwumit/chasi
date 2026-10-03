# Changelog

## 2026-10-03 — repository split (first release of this repository)

### What moved, and from where

`governance-architecture.md`, `governance-architecture-zh.md`, `organization-governance.md`, `organization-governance-zh.md`, `group-collaboration.md` and `group-collaboration-zh.md` moved here from `wwumit/did-method-cha2a` (`cha2a-registry`) at commit `56efed4`. The reason is that the governance model is not coupled to a DID method: measured against that repository, `governance-architecture.md` carried **zero** `did:cha2a` occurrences, zero API endpoints and zero references to the reference registry, and the other two carried only the identity form and named interface points.

### Why the move changed no reference on the other side

§11 of the method specification is its companion index, and it is not edited. It lists `evidence-record.md`, `agent-identity.md` and `EVIDENCE.md` as the CHA2A specification group. **The three volumes moved here were never in that list.** `overview.md` §5 of that repository recorded the gap as an open exception; the move removes the need for the exception, and `overview.md` now points here instead.

### What changed in the content

The volumes are written against an **identity binding** and name `did:cha2a` as the worked example. Concretely:

- the three volume titles no longer carry `CHA2A`;
- the front matter of each states the relation to an identity binding, and records the example's status (experimental draft, v1.1.0, W3C DID Extensions registry);
- citations of the method specification became **interface points**, each marked as the worked example — `organization-governance.md` §1 item 5, §3, §7.5, §9, §10, §11; `group-collaboration.md` §1 item 4, §2, §4.1, §4.5, §9.1, §9.2, §10, §11;
- `group-collaboration.md` §9 is now headed by what the *identity binding* settles rather than by the method specification;
- the closing note of each volume states that the volume carries the requirements for its own subject, rather than deferring to the method specification;
- `governance-architecture.md` §0's table of the family's three claims gained a column recording **where each claim lives**, since two of the three now live in a companion repository.

### `group-collaboration.md` §9.4 — prior art recorded

§9.4 previously said the resolver's operational surface "remains to be built", without qualification. It now records the prior art and the premise differences:

- **`draft-raskar-agentic-web-federated-resolution-01`**, *Registry-Assisted Discovery for AI Agents and Workloads Without DNS Discovery Anchors*, Informational Internet-Draft, 2026-07-20, Raskar · Sharaf · Chari — an individual submission carrying no IETF endorsement and no formal standing. Recorded with the two rules it shares with this volume (registry selection by local configuration; registry presence does not make a binding authoritative) and the three premises that differ (scale versus trust boundary; registry interoperability deferred versus settled; the resolver is given a mechanism versus a set of accepted authorities).
- ***A Global Switchboard for the Agentic Web***, MIT Media Lab, v0.1, 2026-07-20, *Request for Comments* — the broader directory-of-directories model from the same group, cited by the draft as background and stated there to be outside that revision's protocol scope.
- The draft's Appendix C names three open questions that this family answers: a common credential format for authority evidence across identity classes (`evidence-record.md`), transparency logs and auditable recovery procedures (`organization-governance.md` §7 and §12), and operational governance for independently selected registries (`group-collaboration.md` §5).

### Corrections made while moving

- `governance-architecture.md` §9: the closing paragraph opened with the same sentence twice ("A federation level relates authorities that share a proof format and an authority model. Such a level relates authorities that share a proof format and an authority model;"). The first is replaced by the subject of the paragraph, "A federation level is defined within one credential scheme."
- `governance-architecture.md` §9: the reference to the reading conventions now names its source (`overview.md` §5), which is in the companion repository.
- `group-collaboration.md` §11, Chinese edition: the group-service row carried two negations that the English edition did not ("不采用任何外部群组服务作为核心协议，也不引入其账号或信任模型"); it now states the same rule as the English edition.
- `group-collaboration-zh.md` §9.3: a stray space inside `本族的 核心主张` removed.
- `MAINTAINERS.md`: the change process no longer cites §9 of the method specification, which is in the companion repository.

### What did not change

Every rule, table, threshold, derivation and fixed-versus-deploying-parties row is otherwise as it stood at `56efed4`.
