# Compliance Hub Architecture

> Status: draft (v0.1) | Date: 2026-10-19 | Layer: **L2 · architecture** — states no requirements
> Position: the **component decomposition and operating shape** of the Hub. A peer of `governance-architecture` (why the family is layered) and `protocol-suite-architecture` (how the protocol suite is layered) — not a layer above either.
> Principle: this document states architecture and the division of labour only. Where a requirement exists, it belongs to the volume that owns it; this document points there and does not restate it.
> Related: `protocol-suite-architecture.md` · `governance-architecture.md` · `../specs/overview.md` · `../specs/group-collaboration.md` · `../profiles/assembly.md` · `did-method-cha2a.md` (companion repository)

---

## 0. Position

**Compliance Hub is an infrastructure layer for cross-subject participation, identity verification, authority and accountability, not a compliance information site.**

The website is one client of that layer, not the layer itself.

---

## 1. Position within the family

```
CHASI
├── Vision                          why, and where it is going
├── Architecture
│   ├── governance-architecture     why the family is layered this way
│   ├── protocol-suite-architecture how the protocol suite is layered
│   └── compliance-hub-architecture what the Hub is made of   ← this document
├── Specifications                  what must hold, per subject
├── Profiles                        how the parts are assembled
└── Method                          how an experiment is run and recorded
```

`ComplianceHub.cn` is the reference deployment of this architecture. It carries no architectural privilege: a partner Hub may implement the same components under its own trust root.

---

## 2. The questions it answers

A Hub that only answers "who are you" is a directory. The architecture exists to carry the chain:

**Identity → Authority → Policy → Action → Evidence → Accountability**

Each arrow is a hand-off, and the record must survive the hand-off. Where it does not, the chain breaks at that point; the break should itself be recorded as a checkable finding.

---

## 3. Design principles

| # | Principle | What it fixes |
|---|---|---|
| 1 | **Compliance enables autonomy** | compliance earns trust and widens legitimate autonomy; it is not only a restriction |
| 2 | **Federation over centralisation** | a Hub works with organisational and partner Hubs; it does not become a universal central authority |
| 3 | **Evidence over assertion** | a consequential claim is carried by verifiable evidence, not by a statement |
| 4 | **Policy-aware autonomy** | authorisation is contextual, scoped and policy-bound |
| 5 | **Human-centred accountability** | autonomous action stays connected to a person or a legal entity |
| 6 | **Protocol neutrality** | reuse A2A, MCP, DID/VC and other mature technologies |
| 7 | **Implementation freedom** | standardise semantics and interoperability points before internal implementation |
| 8 | **Progressive trust** | admission and authorisation may rest on different levels of evidence |
| 9 | **Lifecycle governance** | compliance is continuous: registration, admission, action, monitoring, audit, renewal, revocation |

---

## 4. Reference architecture

```
                          Compliance Hub

 ┌──────────┬────────────┬───────────┬──────────────┐
 │ Identity │ Governance │  Policy   │   Evidence   │
 │ Registry │   Roles    │   Rules   │ Attestation  │
 │ Passport │   Groups   │   Scope   │   History    │
 └──────────┴────────────┴───────────┴──────────────┘
               │
      ┌────────┴────────┐
      │ Accountability  │
      │  Audit / Trace  │
      └────────┬────────┘
               │
        Interoperability
               │
    Agent Society / Federation
```

The four upper components are peers. Accountability sits below them because it consumes all four. Interoperability is the boundary, not a component.

---

## 5. Components

### 5.1 Identity and registry

Identifiers and registry records for agents, humans, organisations, groups, services and authorities. Resolution, status and revocation are carried by the identity binding; this document does not define them.

### 5.2 Portable claims (the Passport)

A portable representation of identity, principal, capabilities, roles, authorisations, attestations and references to evidence.

**It carries references and claims, not the evidence itself.** A Passport that embeds everything becomes a central data container, which contradicts principle 2.

> The field-level definition and verification procedure of the Passport are a separate working draft. This document defines only the component's place in the architecture.

### 5.3 Governance

Organisation governance, group governance, membership, roles, rules, decisions, disputes and human override.

### 5.4 Policy

Policies governing admission, authorisation, delegation, data access, transactions and actions. **Not yet specified** (see §13).

### 5.5 Delegation and authorisation

Who authorised an agent, what was delegated, scope, conditions, duration, limits, and whether further delegation is permitted.

Scope must be expressible at a granularity that can be compared with an action. **A scope that cannot be compared is a declaration, not an authorisation.**

### 5.6 Evidence and attestation

Evidence supporting identity, capability, policy compliance, actions, certifications and governance decisions. Records are content-addressed; the registry holds summaries, not bodies.

### 5.7 Accountability and audit

Records connecting principal, authorisation, agent, action, policy and evidence. The chain ends at a person or a legal entity; an endpoint written as "the system" is a missing link, not an answer.

### 5.8 Federation

Independent Hubs and registries establishing trust relationships and exchanging the minimum information required for cross-domain participation. Recognition remains each party's local policy.

---

## 6. Operating lifecycle

```
Register → Verify → Admit → Authorise → Act → Monitor → Evidence → Audit → Renew / Revoke → Re-authorise
```

Compliance is a lifecycle, not a one-time certification. One agent may hold different permissions in different societies, and may gain or lose authority as policies, identities, memberships or evidence change.

---

## 7. Compliance as admission control

An agent seeking to join a group, an organisation or a society presents identity, portable claims, capabilities and evidence. The receiving governance domain evaluates them against its policies and decides whether — and under what conditions — the agent may participate.

```
Identity → Passport → Capability → Policy check → Governance check → Attestation → Admission
```

This is where compliance stops being documentation and becomes a runtime mechanism. **The decision belongs to the receiving domain**; the Hub supplies the materials and the record, not the verdict.

---

## 8. Multiple governance scopes

A single agent is simultaneously subject to personal policy, organisation policy, group policy, service policy and wider regulatory requirements.

```
Human policy
      ↓
Organisation policy ↔ Group policy ↔ Society policy
      ↓
Agent authorisation / action
```

Policy precedence, conflict resolution, delegation limits and human override are therefore **architectural** topics, not optional administrative features.

---

## 9. Federation

```
                    Federation layer
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
  ComplianceHub.cn   Organisation Hub    Partner Hub
        │                  │                  │
      Agents             Agents             Agents
```

Different identities, policies, platforms and protocols. A Hub can be a reference or co-ordination point without becoming the sole authority. Federation must define trust establishment, discovery, claim exchange, evidence references, authorisation semantics and revocation — **except where the identity binding already fixes them.**

---

## 10. Runtime layers

```
Applications / Agent Society use cases
              ↓
CHA2A / interoperability services
              ↓
Compliance Hub services
Identity · Governance · Policy · Delegation · Evidence · Audit
              ↓
Existing identity / credential / messaging / cloud infrastructure
```

The Hub exposes APIs and protocol endpoints, not only web pages.

---

## 11. What to standardise, and what not to

### 11.1 Written, or pointed at

| Concept | Where it stands |
|---|---|
| Identifier and identity binding | `did-method-cha2a.md` (companion repository) |
| Agent as subject, capabilities | `agent-identity.md` (companion repository) |
| Evidence and attestation | `evidence-record.md` (companion repository) |
| Portable claims (Passport) | separate working draft; not in this repository |
| Organisation authority | `organization-governance.md` |
| Group admission and collaboration | `group-collaboration.md` |
| Judgment format | `question.md` |
| Naming and references | `naming.md` |
| Assembly rules | `assembly.md` |
| **Policy and authorisation semantics** | **not yet written** |
| **Audit / accountability event model** | partial: Vision §12, `question.md` |
| **Federation trust relationship model** | partial: `group-collaboration.md` §9 |

### 11.2 Deliberately not standardised

Dashboard and UI design · database technology · cloud provider or deployment model · a specific AI model · internal workflow engine · storage architecture · implementation language · commercial service packaging.

The separation preserves the ability to move quickly while keeping a credible path to standards.

---

## 12. Minimum closed loop

A minimal implementation does not attempt the whole platform at once. A practical closed loop is:

1. registry for agents and organisations;
2. portable claims for an agent;
3. group membership and governance records;
4. scoped authorisation and delegation;
5. evidence and attestation references;
6. action and accountability events;
7. simple policy evaluation;
8. a basic federation interface.

The objective is **one complete cross-organisation governance loop** before widening the component set. The reference scenario is cross-organisation group collaboration (`group-collaboration.md`; Use Case 01 in `../method/use-case-laboratory.md`).

---

## 13. Open questions

Each is undecided, and each names what must be settled first.

| Question | Blocked on |
|---|---|
| How does evidence stay portable while respecting minimisation? | a disclosure format in use across two independent implementations |
| How are policy conflicts across organisations resolved? | a policy model (§5.4) |
| How is recursive delegation represented? | delegation-depth semantics — partially in `agent-identity.md` §7 |
| Can an agent prove compliance without revealing unnecessary information? | a selective-disclosure suite in use across two implementations |
| How does revocation propagate across federated Hubs? | a cross-registry status mechanism |
| How is human override represented and audited? | the review-record format |
| How does compliance status change as an agent acts? | a status model distinct from DID status |
| Which parts should become CHA2A specifications or independent standards? | a decision process for the family |

---

## 14. Architectural thesis

Cross-subject autonomous participation requires a set of checkable mechanisms that connect identity, authority, policy, evidence and accountability.

Compliance expands the range of autonomy that can be trusted by making its constraints checkable; it is one part of that infrastructure.

---

*This document is the architecture layer: it states no requirements. Every requirement lives in the volume that owns it.*
