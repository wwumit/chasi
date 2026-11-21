# Agent Action Authorization Profile

> Status: draft (v0.1) | Date: 2026-11-21 | Layer: **L4 · profile**
>
> This profile constrains how a relying party turns standing authority, current
> observations, an operation contract and evidence into a decision on one
> attempted agent action. It reuses the Passport, Registry, Organization,
> Group and evidence objects. It defines no identity method, credential
> format, policy language, transport or execution protocol.

## 1. Scope

This profile answers one question:

> May this agent attempt this action, for this principal, in this context, at
> this time?

It separates four time scales that are often collapsed:

| Object | Time scale | Question |
|---|---|---|
| Identity | persistent or local | Which subject is this? |
| Authentication | this presentation | Who presented the claim now? |
| Standing privilege | a task window | What authority may this agent hold over this task? |
| Action decision | one attempted action | Is this action permitted now? |

An execution attempt is a fifth layer: it records what was actually attempted
after authorization. An execution receipt is not a decision and does not prove
finality.

## 2. Non-goals

This profile does not:

- redefine DID, VC, A2A, MCP, OAuth, GNAP or Registry APIs;
- define a wire format for a decision;
- decide legal liability or regulatory compliance;
- assign one universal trust score;
- replace the Passport verification procedure;
- replace organization or group governance;
- require one central policy engine;
- require a human approval for every action.

## 3. Terms

| Term | Meaning in this profile |
|---|---|
| **standing privilege** | authority held by an agent over a task window, derived from a Passport grant, delegation, role or other recognized authority source |
| **operation contract** | the application-side declaration of what inputs an attempted operation requires, which checks occur before and after commitment, and what disposition applies when an input is missing, stale or conflicting |
| **decision input** | an object the decision point reads, together with its source, version, scope, observation time and coverage |
| **verification outcome** | `valid`, `invalid` or `indeterminate`, using the family's existing verdict vocabulary |
| **policy action** | `allow`, `remediate`, `deny`, `escalate` or `indeterminate` |
| **no decision** | no required check was performed or no decision was taken; this is not a policy action and not a verification outcome |
| **control-plane change** | a grant, suspension, restoration, revocation or expiry that changes future decision inputs |
| **observed effect** | an independent observation that a control-plane change has actually reached an enforcement point |

## 4. Decision model

```text
standing privilege
  + identity / authentication state
  + requested action
  + operation contract
        |
        v
collect and pin decision inputs
        |
        v
verification outcome
  valid / invalid / indeterminate
        |
        v
policy action
  allow / remediate / deny / escalate / indeterminate
        |
        v
decision record
        |
        +----> no decision, recorded separately
```

The verification outcome describes what the available evidence establishes.
The policy action describes what the relying party decides to do. Neither
replaces the other.

## 5. Operation contract

An operation contract identifies, for one operation type:

- the operation and the consequence of committing it;
- the standing privilege or authority source it consumes;
- the decision inputs required before commitment;
- the observations required after commitment;
- the checks performed before and after commitment;
- the party expected to perform each check;
- the declared scope, coverage and freshness budget of each input;
- the disposition when an input is missing, stale, unreachable or conflicting;
- whether human approval is required and which constraints bind it;
- the maximum duration of one operation and its continuation points.

An operation contract does not grant authority. It states how authority and
other inputs must be checked.

A contract that declares no authority input cannot by itself establish
authorization. A contract that leaves a required input's failure disposition
unstated is incomplete for that operation.

## 6. Decision inputs

At decision time, the decision point MUST preserve for every required input:

- the object or claim read;
- its source;
- its version or revision;
- the observed scope and coverage;
- the observation time;
- the retrieval or resolution time;
- whether the source asserted the value directly or an adapter observed it;
- any unresolved, stale or conflicting component.

When the applicable profile requires a negative authority or status finding,
the decision record MUST also preserve the authority basis: source, scope,
coverage, time basis, federation path where applicable, and residual limits.

An input that cannot be obtained MUST NOT be replaced by an application-supplied
identifier or a default value and then reported as verified.

## 7. Verification outcome

| Outcome | Meaning |
|---|---|
| `valid` | every required claim is established for this action and decision time under the applicable profile |
| `invalid` | a required claim is authoritatively established as false, revoked, out of scope or otherwise not applicable |
| `indeterminate` | a required claim cannot be established because evidence is missing, unreachable, stale, conflicting or outside established coverage |

`invalid` MUST NOT become `valid` by policy.

`indeterminate` MUST NOT be reported as `valid`, and a reachable but
insufficient source MUST not be treated as an authoritative negative finding.

This profile uses the existing CHASI verdict names. Where an implementation
internally uses `verified / unresolved / rejected`, the mapping is:

```text
verified   <-> valid
rejected   <-> invalid
unresolved <-> indeterminate
```

The mapping does not permit a `policyAction` to alter the verification outcome.

## 8. Policy action

| Action | Meaning |
|---|---|
| `allow` | the action may proceed under this decision |
| `remediate` | the action is held while a correctable input, approval or action parameter is corrected and re-evaluated |
| `deny` | the action must not proceed |
| `escalate` | the decision is transferred to a qualified human, authority or specialist process |
| `indeterminate` | the decision point cannot determine a safe action from the available inputs |

`remediate` MUST name the correction required and the condition for
re-evaluation. `escalate` MUST name the receiving authority or role and the
scope of the escalation. `indeterminate` MUST state what remains unresolved.

No policy action may convert an `invalid` verdict into `allow`.
An `indeterminate` verdict must never be upgraded to `allow` merely because the
action is urgent or no one is available to decide.

### 8.1 Default reference mapping

| Verification outcome | Default policy action |
|---|---|
| `invalid` | `deny`; escalation is allowed for investigation or remedy, but the action is not allowed |
| `valid` and policy satisfied | `allow` |
| `valid` and local policy not satisfied | `deny`, `remediate` or `escalate` |
| `indeterminate` with a correctable input | `remediate` |
| `indeterminate` without a correctable input | `deny`, `escalate` or `indeterminate` under declared policy |

The mapping is a reference profile. A deployment may make policy stricter but
may not turn `invalid` or `indeterminate` into `allow`.

## 9. No decision

“No decision” is a distinct record state. It applies when:

- the decision point was not reached;
- a required check was not executed;
- the service failed before a verdict was formed;
- a policy did not authorize anyone to take the decision.

A no-decision record MUST identify:

- the attempted action;
- the missing check or decision;
- the responsible role or service;
- the time and source of the observation;
- the disposition applied by the surrounding system.

If surrounding policy stops the action, that stop is a separate policy action
or control-plane act. It does not retrospectively create a verification verdict.

## 10. Standing privilege lifecycle

Standing privilege may be:

```text
granted -> active -> suspended -> active
                      \-> revoked
             \-> expired
```

The exact representation is owned by the applicable authority source. This
profile requires the decision point to re-evaluate current applicability before
a consequential action.

A decision must record the standing-privilege version or observation it used.
When the source changes during a long-running task, the operation contract
declares continuation points at which the decision point re-consults the
source.

For a worker dispatched before a change and started after it:

- the worker's first check records the version it read;
- the parent dispatch record preserves the version the parent used;
- neither record inherits freshness from the other.

## 11. Control-plane changes and observed effect

A control-plane change has at least three distinct states:

1. **recorded** — the authoritative source records the change;
2. **acknowledged** — an enforcement point or platform reports receipt;
3. **observed effect** — an independent observation shows that subsequent
   decisions no longer use the superseded state.

A recorded revocation alone does not prove that every decision point has
stopped accepting the revoked authority. An acknowledgement alone does not
prove effect.

The profile does not define a control-plane protocol. It requires a deployment
to state:

- which decision points must receive the change;
- the maximum time allowed before effect;
- how coverage is measured;
- what happens when a decision point is disconnected;
- how conflicting copies are detected and recorded.

## 12. Human approval

When an operation contract or applicable policy requires human approval, the
approval evidence MUST bind:

- the exact action or action digest;
- the principal and acting agent;
- the operation contract version;
- the summary actually displayed to the approver;
- the approver's role and authority;
- the decision outcome and reason;
- the validity window;
- whether the agent or an interested party self-approved.

An approval that does not bind the action may not be reused for a materially
different action.

## 13. Decision record

A decision record MUST preserve at least:

| Member | Purpose |
|---|---|
| `decisionId` | identifies this decision event |
| `actionDigest` | binds the decision to the attempted action |
| `contract` | operation-contract identifier, version and digest |
| `principal` and `agent` | identifies on whose behalf and by whom |
| `processInstance` | distinguishes one task run from another |
| `executionInstance` | distinguishes a retry or repeated execution within one process |
| `inputRefs` | pins every required input, source, version, time, scope and coverage |
| `verificationOutcome` | `valid`, `invalid` or `indeterminate` |
| `policyAction` | the selected policy action, or absent for a no-decision record |
| `reasonCodes` | preserves each independent cause |
| `policyProfile` | policy/profile identifier and version |
| `verifier` | verifier implementation or authority |
| `decidedAt` | decision time |
| `unresolved` | every unresolved element that remains |
| `noDecision` | present only when no decision was formed |

Two actions that differ in any action-describing field declared by the
operation contract MUST NOT produce the same normalized action binding.
Content binding and occurrence binding are separate properties.

## 14. Failure semantics

The decision point MUST distinguish:

- no object found within declared coverage;
- source unavailable;
- source cannot establish coverage for the relevant scope;
- source conflicts with another required source;
- object found and authoritatively negative;
- object found, status stale;
- check not executed;
- decision taken but execution not attempted;
- execution attempted but result unknown;
- execution receipt received but finality not established.

These states MUST NOT be collapsed into a single boolean.

## 15. Conformance

Minimum conformance cases:

1. valid authority, satisfied policy, fresh status and matching action digest
   produces `valid` / `allow`;
2. confirmed revocation produces `invalid` / `deny`;
3. unavailable status produces `indeterminate`, never `valid`;
4. insufficient authority coverage produces `indeterminate`, not `invalid`;
5. an authoritative out-of-scope finding produces `invalid`;
6. action-digest mismatch or replay produces `invalid`;
7. a verified identity with no covering authority does not produce `allow`;
8. a valid verification with unsatisfied local policy does not automatically
   produce `allow`;
9. an approval displayed for another action cannot satisfy this action;
10. a recorded control-plane change without observed effect is not reported as
    effective;
11. a required check that was not executed produces a no-decision record, not
    `indeterminate` and not `deny`;
12. two actions with different content cannot share the same normalized action
    binding;
13. a retry with identical content remains distinguishable by execution
    instance while content binding remains stable.

Negative cases should outnumber positive cases in any public conformance suite.
Each vector should identify the requirement it exercises and its expected
reason code.

## 16. Relationship to the other profiles

- **Passport** supplies identity, authority, delegation and verification
  objects. This profile consumes them.
- **Registry Interop** supplies status, coverage and retrieval observations.
- **Agent Card Identity** supplies discovery references, never authorization.
- **Organization Governance** supplies the authority behind organization roles.
- **Group Collaboration** supplies collaboration context and membership.
- **Evidence records** establish what happened after the decision.

This profile does not make the Passport an action executor and does not make a
Registry a decision point.

## 17. v0.1 decisions

- standing privilege and action decision are separate;
- operation contracts state checks and failure dispositions but grant no
  authority;
- verification outcome and policy action remain separate;
- no decision is a distinct record state;
- policy actions are `allow`, `remediate`, `deny`, `escalate` and
  `indeterminate`;
- no encoding, transport, policy language or central engine is required;
- runtime attestation and cross-platform intervention protocols remain outside
  this first version.

