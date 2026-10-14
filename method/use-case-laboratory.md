# CHASI Use Case Laboratory

**The first batch of core Agent Society Use Cases**

Driving CHASI / CHA2A architecture, governance and protocol evolution from scenario experiments

---

> Status: draft v1.0 | Date: 2026-10-04 | Kind: **method**
> This is **a set of experimental scenarios**, not a requirements specification and not a specification frozen for adoption. It answers "which scenarios do we use to stress the architecture"; it does not answer "which one we do when".

---

## 1. What This Document Is

This document proposes the first batch of the CHASI Use Case Laboratory. It is not a requirements specification in the traditional sense, nor a standards specification frozen for immediate adoption; it is a set of experimental scenarios for **thought experiment → scenario design → prototype validation → architecture revision → specification evolution**.

CHASI can draw on the way ITU-T Focus Group TIDA and related work studies use cases, without being bound by a standards process. The aim is more open: **to use real, complex, cross-organizational scenarios to expose, on purpose, where the Agent Society is still open in identity, trust, delegation, policy, evidence, governance and accountability.**

## 2. The Core Method: Use Cases Drive Architecture Evolution

Six steps, closed into a loop:

- **Scenario** — define the participants, organizations, agents, tasks and environment in the real world.
- **Experiment** — actually run the scenario, or at least build an executable simulation.
- **Observation** — record the conflicts, anomalies, governance problems and protocol gaps.
- **Architecture** — raise recurring problems into architectural capabilities.
- **Specification** — form a discussable, reusable profile or protocol.
- **Re-test** — run the scenario again and check the new design.

```
Scenario → Experiment → Observation → Architecture → Specification → Re-test
                                        ↑                              │
                                        └──────────────────────────────┘
```

**The loop is the only requirement in this section:** a scenario that cannot get back to `Re-test` is a demonstration, not an experiment.

## 3. The First Batch of Flagship Use Cases

| # | Scenario | In one line |
|---|---|---|
| UC-01 | Cross-organization group collaboration | three organizations form a group for one joint task |
| UC-02 | An agent joining a new society | an agent enters, for the first time, a society led by another organization |
| UC-03 | Federated agent society | no shared central platform; each keeps its own identity, policy and governance |
| UC-04 | Agentic commerce | an agent concludes a transaction with economic consequences on behalf of a person or organization |
| UC-05 | Human–agent coexistence | one personal agent serves several parties at once, with human control preserved |

## 4. UC-01: Cross-Organization Group Collaboration

This is the first priority, and the scenario that the existing Group and governance work is best placed to enter directly.

**Typical situation**: Organizations A, B and C each have agents; to complete one joint task the three form a group for the duration. The group has its own membership, roles, policy, task and lifecycle. **An agent's original organizational belonging may not disappear because it joined the group.**

Flow:

- A creates the task and invites B and C.
- Each organization sends designated agents.
- The group establishes membership, roles and a common policy.
- Agents receive delegation **within the scope of the task**, not unlimited authority.
- During the task, messages, actions, evidence and provenance are produced.
- When the task ends, the group dissolves or moves to its next lifecycle.
- Every authorization, execution and result can be traced.

**What it is meant to verify**: whether a group should be a first-class governance object; how a conflict between organizational policy and group policy is handled; how an agent's authority is revoked after it leaves the group; to whom evidence belongs.

## 5. UC-02: An Agent Joining a New Society

An agent belonging to Organization A enters, for the first time, a society or group led by Organization B.

Flow:

- Discover the society's rules and entry requirements.
- Prove its identity, organizational affiliation and capability.
- Accept the society's terms and policy.
- Obtain membership or a role with a limited scope.
- Build trust and reputation gradually through behaviour.
- On a violation, trigger restriction, suspension or revocation.
- On leaving the society, keep the necessary evidence but end the authority to operate.

**What it is meant to verify**: whether identity and admission are separate; whether an external credential equals internal trust; whether trust can accumulate; whether a society needs its own constitution or policy layer.

## 6. UC-03: Federated Agent Society

Organizations A, B and C share no central platform, but need their agents to collaborate on a joint task.

Flow:

- Each organization keeps its own identity, policy, registry and governance.
- A mutually recognized trust relationship is established through federation.
- Agents can discover services and counterparties across domains.
- Delegation must state its scope explicitly at the federation boundary.
- Evidence can be verified across domains without requiring all data to be stored centrally.
- The federation can revoke a member, a trust relationship or a permission.

**What it is meant to verify**: how CHA2A should interoperate with existing capabilities such as A2A, MCP and DID/VC; which capabilities can be reused and which need a profile or an extension.

## 7. UC-04: Agentic Commerce

An agent does not merely exchange information; it concludes, on behalf of a person or organization, transactions that have economic consequences.

Flow:

- Discover services and providers.
- Check capability, trust, policy and price.
- Negotiate within the scope of its delegation.
- Form a contract or SLA.
- Perform the service and produce evidence.
- Complete payment and settlement.
- On a dispute, resolve it against the evidence, the policy and the contract.

**What it is meant to verify**: the authority boundary of economic action, who the contracting party is, agent liability, the evidence chain, and dispute handling across organizations.

## 8. UC-05: Human–Agent Coexistence

This is the scenario that best expresses the long-term CHASI vision. One personal agent may serve a person, a family group, an organization and several professional societies at once, and transact with other agents.

Points:

- The human is the principal, but the agent has a measure of autonomy.
- An organization may obtain limited delegated authority.
- Different societies have different rules for the same agent.
- Private memory and organizational memory must be kept separate.
- The human can issue an override or a stop.
- The agent's delegation chain must trace back to the source of authority.
- On conflict, the priority among authority, privacy, consent and accountability must be stated.

**What it is meant to verify**: that which agent an agent "belongs to" is **not a simple question of ownership, but a combined governance problem over identity, authority, loyalty, privacy, memory, responsibility and economic interest.**

## 9. The Common Model the Five Scenarios Share

```
Human / Principal
        ↓
Organization
        ↓
Agent
        ↕
Group / Society
        ↓
Identity · Trust · Delegation · Policy
        ↓
Task · Action · Evidence · Provenance
        ↓
Governance · Accountability · Federation
```

The five use cases should not become five separate models. **The point of the experiments is precisely to stress-test one common model**, and to find which objects, relationships and governance mechanisms can be reused across scenarios.

## 10. The Standard Experiment Template for Each Use Case

- **Actors** — human / organization / agent / group / society / service.
- **Context** — why it happens, who initiates it, what trust and identity relationships already exist.
- **Goal** — what task is to be completed.
- **Authority** — who may do what.
- **Scenario flow** — the agent interactions, step by step.
- **Governance** — which policies, roles, membership and lifecycle rules apply.
- **Compliance** — which constraints must be satisfied.
- **Evidence** — what evidence must be left.
- **Failure modes** — authority conflict, identity failure, agent misuse, policy conflict, malicious behaviour.
- **Protocol requirements** — what needs a CHA2A profile or extension.
- **Experiment** — how to simulate or implement it.
- **Observation** — what actually happened.
- **Architecture change** — what architectural change the experiment led to.
- **Specification change** — what specification change finally results.

**The point of the template is in its last five entries.** The first nine are what a scenario has to state; the last five are what an experiment has to produce — **a scenario with the former and not the latter reads well and changes nothing.**

## 11. Its Relation to the ITU-T Focus Group TIDA

CHASI can follow and draw on the scenario research produced by ITU-T Focus Group TIDA and related work, but its own Use Case Laboratory need not wait for a standards body to reach final consensus. Five attitudes:

- **Compatible** — adopt existing terminology, models and open protocols where possible.
- **Complementary** — concentrate on cross-organizational agent societies, governance and compliance, which are not yet closed.
- **Experimental** — allow hypotheses that are not yet mature, and that may in the end be rejected.
- **Verifiable** — turn every important idea into an executable scenario as far as possible.
- **Evolvable** — use case results feed directly into updates of the architecture and the specification.

## 12. The Question the First Batch Is Meant to Answer

The first batch of scenarios is not there to show a few demos, but to answer one fundamental question: **now that agents are turning from "tools" into social participants with identity, authority, relationships, responsibility and autonomy, is the existing Internet / cloud / AI-agent stack enough to support that social structure?**

The value of CHASI should emerge gradually through these scenarios: not starting from scratch, but filling in — on top of the existing agent, identity, protocol, cloud and governance systems — the social infrastructure an Agent Society needs.

The end goal is a continuing loop: **real scenarios produce problems, experiments produce evidence, evidence drives the architecture, the architecture forms specifications, and the specifications go back into new scenarios for validation.**

—— CHASI Use Case Laboratory · v1.0
