# Passport–Registry Interoperability Profile

> Status: draft (v0.3) | Date: 2026-11-21 | Layer: **L4 · profile**
>
> This profile constrains how a Passport verifier consumes a Registry. It does
> not replace a DID method, Registry API, or verifier policy.

## 1. Scope

This profile defines the minimum Registry observations needed to verify a
Passport across subjects:

- DID Document resolution;
- current subject status and revocation;
- provenance and freshness of an observation;
- fail-closed error semantics;
- explicit cross-Registry peer queries.

It does not define Registry write APIs, admission decisions, trust ratings, or
the internal storage model of a Registry.

## 2. Division of responsibility

| Component | Owns | Does not own |
|---|---|---|
| Registry | DID resolution, identity status, revocation facts, evidence indexes | Passport issuance, admission decisions, policy verdicts |
| Passport issuer | The signed Passport and its authority claims | DID allocation or current subject status |
| Verifier | Trust-root configuration, freshness policy, final verdict | Rewriting Registry facts |
| Agent Card | Capability and interface discovery | Accountability, authority, revocation status |

The Registry answers. The verifier decides.

## 3. Core observations

### 3.1 Resolution

A resolved object MUST contain:

| Field | Requirement |
|---|---|
| `did` | exact DID requested |
| `document` | object whose `id` equals `did` |
| `registryDid` | DID of the responding Registry |
| `source` | local Registry or a peer identifier |
| `observedAt` | time at which the verifier obtained the observation |

An object with another `id`, a malformed document, or no provenance MUST NOT be
accepted as resolution.

### 3.2 Status

A status observation MUST contain:

| Field | Requirement |
|---|---|
| `did` | exact subject DID |
| `state` | `active`, `suspended`, `revoked`, `expired`, or `unknown` |
| `available` | boolean |
| `source` | observation source |
| `registryDid` | Registry responsible for the record |
| `observedAt` | verifier observation time |
| `timeBasis` | `source` or `adapter-observation` |
| `subjectRecord` | source-specific status facts |

`revision` and `proof` are optional capabilities. A Registry that asserts
`revisioned-reads` MUST make revisions monotonic for one subject.

If the Registry supplies its own assertion time, the adapter SHOULD expose it
as `sourceAssertedAt` and MUST set `timeBasis` to `source`. Otherwise
`timeBasis` MUST be `adapter-observation`; an adapter MUST NOT present its own
retrieval time as a Registry assertion.

`revoked` takes precedence over `suspended`, which takes precedence over
`expired`, which takes precedence over `active`. A missing, contradictory, or
unmappable state MUST NOT be converted to `active`.

### 3.3 Errors

The consumer MUST distinguish:

- `not_found`;
- `unavailable`;
- `unauthorized`;
- `conflict`;
- `malformed`;
- `stale`.

These are observations, not final Passport verdicts. A verifier applies its
policy and fails closed when the required observation is unavailable.

### 3.4 Scope, coverage and retrieval

A negative observation is local to what the source was asked and qualified to
answer. `not_found` alone MUST NOT be read as ecosystem-wide absence.

Every observation used for a definitive negative result SHOULD preserve:

| Semantic member | Requirement |
|---|---|
| `queryScope` | the subject, claim or status question actually asked |
| `coverage` | the authorities checked, whether the check is complete for that scope, and any residual limitation |
| `retrieval` | source surface, request time, response time and response digest or equivalent content binding |

Where the source cannot establish coverage for the relevant time, scope or
federation path, the verifier reports the result as unresolved/indeterminate,
not as an authoritative negative finding.

The following are different observations:

- no record in a source whose declared coverage is established;
- no record in a source whose coverage is unknown;
- source unavailable;
- a complete source that affirmatively confirms non-revocation.

An empty revocation list does not establish non-revocation unless the profile
declares the list complete for the requested subject, time and scope.

## 4. Freshness

Freshness policy belongs to the verifier. A Registry MUST NOT decide that an
observation is fresh enough for another party.

An observation should carry enough information for the verifier to apply:

- maximum observation age;
- whether a proof is required;
- whether a live lookup is required;
- whether a cached observation is permitted.

The applicable action-authorization profile MAY bind a freshness budget to a
decision class. The same observation age can be acceptable for a read-only
lookup and insufficient for an irreversible action.

If a Registry does not provide `sourceAssertedAt`, an adapter MAY use the
retrieval time as `observedAt` and MUST label the time basis as an adapter
observation.

## 5. Federation

Federation is explicit:

1. A verifier resolves through its own local Registry first, unless its policy
   says otherwise.
2. A peer is contacted only when configured.
3. The response carries `source`, peer identifier, trust domain and
   `registryDid`.
4. A peer failure MUST remain a peer failure; it MUST NOT be converted into a
   local success.
5. Automatic peer discovery is outside this profile.

Peer authentication may use mTLS, signed requests, workload identity, or a
scoped bearer token for a controlled pilot. The deployment selects the
mechanism; the profile requires that the peer identity be established before a
response is trusted. Long-lived shared bearer tokens are not a production
conformance claim.

## 6. Registry writes

Read interoperability is the required baseline. Write interoperability is a
separate capability:

- `revisioned-writes` requires `expectedRevision`;
- a stale revision returns `conflict`;
- a write response returns the committed revision;
- authorization scope is distinct from peer-read scope.

The Passport family does not prescribe Registry approval workflow or billing.

## 7. Mapping the current CHA2A Registry

The reference `did:cha2a` Registry API maps as follows:

| Current endpoint | Profile observation |
|---|---|
| `GET /api/v1/did/{did}` | resolution |
| `GET /api/v1/trust/query?did=` | status |
| `GET /api/v1/trust/revocations` | revocation source |
| `GET /api/v1/evidence/query?did=` | evidence index |
| `GET /api/v1/registry/trust/{did}` | explicit peer status |

The current API does not expose all normalized fields directly. An adapter
SHOULD add `source`, `registryDid`, `observedAt`, and normalized `state`.
Adding a field in the adapter does not change the Registry's own claim.

## 8. Capabilities

A Registry MAY declare:

- `resolve`;
- `status`;
- `revocation-list`;
- `status-proof`;
- `revisioned-reads`;
- `explicit-federation`;
- `revisioned-writes`.

Unsupported capabilities MUST be omitted, not advertised as reserved.

The canonical location for capability declarations is the Registry discovery
document at `/.well-known/cha2a`, under `capabilities`. A separate capability
document requires a future profile revision.

## 9. Conformance

Minimum conformance requires:

1. exact DID/document binding;
2. a normalized status state;
3. source and observation time;
4. not-found and unavailable distinctions;
5. no conversion of unknown state to active;
6. explicit peer provenance and fail-closed peer failure;
7. a negative result identifies the scope and coverage under which it was obtained;
8. a retrieval receipt or equivalent trace binds source, query, observation time and response content;
9. an empty revocation response is not reported as confirming non-revocation unless completeness is established.

Proof, evidence, revision and write tests are separate capability profiles.
Status proofs are not mandatory in the base v0.3 profile; a verifier may require
them under its own cross-domain admission policy.

## 10. v0.3 decisions

- `sourceAssertedAt` is not mandatory; `timeBasis` is mandatory;
- base status proof is optional and policy-driven;
- peer identity is explicit and authenticated, without prescribing one
  technology;
- capabilities are declared in `/.well-known/cha2a`;
- negative observations are scoped by coverage;
- retrieval provenance is part of the observation, not a logging convenience.
