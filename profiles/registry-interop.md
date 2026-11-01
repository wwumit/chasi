# Passport–Registry Interoperability Profile

> Status: draft (v0.1) | Date: 2026-11-01 | Layer: **L4 · profile**
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
| `subjectRecord` | source-specific status facts |

`revision` and `proof` are optional capabilities. A Registry that asserts
`revisioned-reads` MUST make revisions monotonic for one subject.

If the Registry supplies its own assertion time, the adapter SHOULD expose it
as `sourceAssertedAt` and MUST distinguish it from `observedAt`.

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

## 4. Freshness

Freshness policy belongs to the verifier. A Registry MUST NOT decide that an
observation is fresh enough for another party.

An observation should carry enough information for the verifier to apply:

- maximum observation age;
- whether a proof is required;
- whether a live lookup is required;
- whether a cached observation is permitted.

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

Peer authentication may use mTLS, workload identity, or a scoped bearer token.
The deployment selects the mechanism; the profile requires that the peer
identity be established before a response is trusted.

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

## 9. Conformance

Minimum conformance requires:

1. exact DID/document binding;
2. a normalized status state;
3. source and observation time;
4. not-found and unavailable distinctions;
5. no conversion of unknown state to active;
6. explicit peer provenance and fail-closed peer failure.

Proof, evidence, revision and write tests are separate capability profiles.

## 10. Open decisions

- whether `sourceAssertedAt` is required in a future major profile;
- whether status proofs become mandatory for cross-domain admission;
- the peer identity profile: mTLS, signed request, or workload identity;
- the canonical Registry capability document.
