# CHA2A Agent Passport

**A Verifiable, Portable and Governable Social Identity for Autonomous Agents**

> Status: draft (v1.0)
> Date: 2026-10-19
> Layer: **L3 · specifications** — states the requirements for its own subject
> Position: the members, signature, lifecycle, verification procedure, disclosure sets and conformance requirements of the Passport object
> Principle: identity semantics are normative in `did-method-cha2a.md` and evidence semantics in `evidence-record.md`; this document neither restates, extends nor amends them
> Related: `organization-governance.md` (who is qualified to authorize) · `group-collaboration.md` (collaboration context) · `overview.md` §4.4 (placement between Registry and application) · `assembly.md` (assembly)

---

## Status of This Document

This document specifies the **CHA2A Agent Passport**: a signed, portable document that carries an agent's subject identifier, the principal it acts for, the authority it holds, the governance context that bounds that authority, and references to the evidence behind it.

Every open item is disposed in §24 — as decided, as a deployment parameter, or as not-in-this-version with a stated precondition. No item is left blank.

| Item | Value |
|---|---|
| Specification status | Working Draft / Experimental |
| Specification version | 1.0 |
| Subject of the document | the **portable identity of an agent**, and the authority under which it acts |
| Normative scope | the Passport object, its fields, its verification procedure, and its conformance requirements |
| Identity semantics | normative in `did-method-cha2a.md`; this document reuses them and adds no identifier syntax |
| Evidence semantics | normative in `evidence-record.md`; this document reuses its predicates and adds no evidence format |
| Ecosystem | CHASI / Compliance Hub / CHA2A specification group |

### Conventions

1. **Requirement keywords** — `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, `MAY` are to be interpreted as described in RFC 2119 and RFC 8174. Within this document they are normative **for the Passport object only**. They do not restate, extend, or amend the requirements of `did-method-cha2a.md`.
2. **Timestamps** — RFC 3339, UTC, terminated by `Z`, second precision or finer.
3. **Canonicalization** — RFC 8785 JSON Canonicalization Scheme (JCS).
4. **Digests** — SHA-256, lowercase hexadecimal.
5. **Requirement identifiers** — `PP-n` denotes a normative requirement; `DP-n` a deployment parameter; `NIV-n` an item deliberately not defined in this version. §26 indexes every identifier.
6. **Derivation stated** — a decided item states the principle it is derived from, so that the derivation can be challenged, not only the conclusion.

---

## 1. Abstract

An agent that acts across organizational boundaries must be able to answer four questions about itself, and a third party must be able to answer them **without asking the agent's operator**:

1. **Who is it?**
2. **Who authorized it?**
3. **In what context is it acting?**
4. **What has it done?**

The CHA2A Agent Passport is a signed document in which an issuer answers as much of (1)–(3) as it is in a position to assert, and points at the objects that answer the rest. It carries no evaluation result, no rating, and no endorsement: it carries **claims, pointers, and observations**, and it is the verifier's act — not the passport's content — that turns those into a decision.

**The passport is not a credential wallet and not a registry record.** It is a *view*: a stable, signed presentation of facts that live in the subject's DID Document, in the issuer's governance records, in the evidence layer, and in the registry's status endpoints. Because the facts live elsewhere, they can change after the passport is signed; this document therefore specifies exactly which fields are **backed by the issuer's signature**, which are **pointers whose truth is not backed by it**, and which are **observations that must be refreshed at decision time**.

> **The signature proves that the issuer said it. It does not prove that it is true.**

An Agent Card tells the world what an agent offers. A Passport tells the Society who the agent is, on whose behalf and under whose authority it acts, and where the evidence for that claim can be checked.

---

## 2. Design Goals

Each goal carries the test that falsifies it. A goal without a test is an aspiration, and an aspiration cannot be implemented against.

| # | Goal | Falsification test |
|---|---|---|
| G1 | **Verifiable** — every material claim is independently checkable | Delete the issuer. A verifier that holds only the passport and public endpoints reaches a verdict. |
| G2 | **Portable** — usable across platforms and trust domains | The passport is a byte string. Verifying it requires no session, no prior registration, and no call to the issuing party's private API. |
| G3 | **Governable** — authority, roles and delegation are represented | For every authority entry, a verifier can name the granting party and the scope granted. |
| G4 | **Accountable** — actions connect to principals and authorization | Given an action and its passport, a verifier can name the party answerable for it without contacting that party. |
| G5 | **Interoperable** — reuses DID/VC rather than replacing them | The subject identifier is a DID and resolves by an existing method; the passport adds no identifier syntax. |
| G6 | **Privacy-aware** — disclosure is minimized | A verifier requesting profile P0 receives no field outside the P0 disclosure set (§16). |
| G7 | **Federation-ready** — several organizations or Hubs can issue and check | Two independent registries each issue a passport for subjects they control, and a third party verifies both. |
| G8 | **Extensible** — new capabilities, policies and evidence types appear without redesign | A new evidence predicate is added by reference; no passport field changes. |
| G9 | **Implementation-neutral** — storage, UI and internal schema are outside the normative core | Conformance is claimed by two implementations that share no storage design. |

### 2.1 The goal this specification does not pursue

**G10 — the passport MUST NOT become a trust score.** It records facts and it points at evidence. A level reported inside it is a *summary of facts owned by the registry*, and is marked as an observation (§6.3, Layer C). A passport that asserts a rating makes its issuer a party to the trust decision it is supposed to inform. This is the position recorded in `overview.md` §4.3: *facts, not ratings*. It is also why the passport is a presentation of the family's objects, not a new authority.

---

## 3. Scope, Dependencies, and Non-Goals

### 3.1 What this specification defines

- the Passport object: its members, their types, presence conditions and provenance classes (§6)
- the binding between a passport and a resolvable subject identifier (§7)
- the representation of principal, capability, authority, roles, delegation, policy references and evidence references (§8–§13)
- the passport lifecycle and the separation of passport status from identifier status (§14)
- verification profiles and the verification procedure (§15)
- the disclosure sets that bound what a verifier may learn (§16)
- the trust context that bounds where a passport is valid (§17)
- requirements and conformance tests (§23, §26)

### 3.2 Dependencies — reused, not redefined

Each dependency produces a mapping table and a conformance test. None of them is redefined here.

| Depends on | For | Mapping | Test |
|---|---|---|---|
| `did-method-cha2a.md` | identifier syntax, resolution, DID Document shape, status and revocation, certification levels, caller authentication | §7.1 | §23.4 T-1 |
| `evidence-record.md` | evidence predicate URIs, `evidenceRef`, `artifactDigest` | §13.1 | §23.4 T-2 |
| `agent-identity.md` | the agent as subject; capability declaration structure; the `did:cha2a:verifier` type | §9.2, §13.2 | §23.4 T-3 |
| `organization-governance.md` | who is qualified to authorize; the role and appointment semantics this document references | §10.1 | §23.4 T-4 |
| `group-collaboration.md` | group membership as a governance context | §10.2 | §23.4 T-5 |
| W3C DID Core | DID Document structure and verification relationships | §7.1 | §23.4 T-1 |
| RFC 8785 (JCS) | canonical form for signing and digesting | §6.4 | §23.4 T-6 |
| A2A Agent Card | what an agent offers, and how it is reached | §18.1 | §23.4 T-7a, T-7b |

### 3.3 Not defined — declined, with the counter-example test

The family maintains exactly two relations to an external object: **reuse** and **not-defining**. There is deliberately no third relation called "alignment": it produces no artefact and cannot be falsified.

| Not defined here | Counter-example test — build the minimum loop without it |
|---|---|
| a policy language or an evaluation engine | A deployment verifies a passport whose `policyRefs` point at opaque identifiers that no implementation resolves. If verification fails, a policy language has leaked into this specification. |
| an evidence format or a testimony vocabulary | Delete every `evidenceRef` target. The passport remains structurally valid and verification returns `indeterminate`, not `invalid`. |
| an identifier syntax or a DID method | The subject is a DID resolved by an existing method. This document introduces no prefix, no path grammar and no resource type. |
| a service-discovery mechanism, endpoint format, or transport | A passport is exchanged inside whatever envelope the parties already use. Nothing in §6 is an endpoint. |
| an agent runtime, model, execution environment, or sandbox | Two implementations sharing no runtime reach the same verdict on the same passport. |
| an override protocol, an approval workflow, or a user interface | The passport *records* that an approval is required and *references* the authority that may approve. It defines neither the approval nor the interface. |
| a liability allocation, or a legal opinion about responsibility | §8 states what the passport evidences and stops there. |
| a marketplace, listing, or settlement mechanism | A passport is not a listing and carries no price, no availability and no rank. |

### 3.4 Deferred, with a named precondition

| Deferred | Precondition for doing it |
|---|---|
| **Selective disclosure by cryptographic proof** (BBS+, ZKP) | a signature suite in use across at least two independent implementations, and a verifier that can consume it without a new trust anchor. Until then, disclosure is bounded by §16 field sets and by not embedding the undisclosed facts. |
| **A `did:cha2a:passport` resource type** | a reason that an object the registry can resolve is needed. A passport is a portable document issued by a party, not a subject the registry maintains; giving it a resolvable DID would make the registry its issuer and contradict §19. |
| **A revocation protocol for delegations** | a delegation chain that outlives a single passport revision. Until then, a delegation is carried in the passport and re-issued with it. |
| **Cross-registry passport endorsement** | a second registry that issues passports under its own trust root. Until then, `trustContext.validityDomain` is a single domain (§17). |
| **Machine-readable policy vocabulary mapping** | two policy vocabularies in production use by parties that exchange passports. |

---

## 4. Terminology

| Term | Definition |
|---|---|
| **Agent** | An autonomous or semi-autonomous software entity capable of acting in a defined context. |
| **Subject** | The agent a passport applies to. Identified by a DID. |
| **Principal** | A human or organization on whose behalf the subject acts. |
| **Issuer** | The party that signs a passport. It asserts the claims in Layer A (§6.3) and nothing else. |
| **Verifier** | A party that evaluates a passport and reaches a verdict. A verifier belongs to no party to the passport. |
| **Claim** | A statement asserted by the issuer and covered by the passport signature. |
| **Pointer** | A reference to an object held elsewhere. Identifies and locates; does not establish. |
| **Observation** | A fact read from a named source at a named time, recorded with both. |
| **Capability** | What the subject can do. Independent of authority. |
| **Authority** | What the subject may do, within a governance context. |
| **Delegation** | A bounded transfer of authority from a delegator to a delegatee, with scope, constraints and validity. |
| **Governance context** | The organization, groups, roles and policies within which an authority holds. |
| **Trust context** | The domain in which a passport is treated as valid, and the registry whose status observations inform that treatment. |
| **Relying party** | A party that acts on a verdict. Distinct from the verifier only in that it bears the consequence. |
| **Verdict** | One of `valid`, `invalid`, `indeterminate` (§15.3). |
| **Disclosure set** | The fields a profile permits a verifier to receive (§16). |
| **Profile** | A named set of checks and its disclosure set (§15). |

Two terms are avoided. **"Certification"** is not used of this specification or of any party to it; the family reserves it for citing regulation, because in some jurisdictions the word triggers a specific liability shape and licensing requirement. **"Authentication"** is not used as a synonym for verification: authentication is confirmation of identity at the connection layer, and verification is the determination of a fact.

---

## 5. Conceptual Model

```
                       ┌──────────────────────────────────────┐
                       │             PASSPORT                 │
                       │                                      │
   Layer A  claims ────┤ subject · principal · capabilities   │─── covered by
   (issuer asserts)    │ authority · roles · trustContext     │    the signature
                       │                                      │
   Layer B  pointers ──┤ organization · groups · policyRefs   │─── identifies, does
   (elsewhere)         │ credentials · delegation proofs      │    not establish
                       │                                      │
   Layer C  observed ──┤ status (source · observedAt)         │─── must be refreshed
   (named source)      │ level · validity · revocation        │    at decision time
                       └──────────────────────────────────────┘
                                        │
                                        ▼
                          ┌───────────────────────────┐
                          │   VERIFICATION PROCEDURE  │
                          │  profile → checks →       │
                          │  verdict + trust context  │
                          └───────────────────────────┘
                                        │
                                        ▼
                    valid  ·  invalid  ·  indeterminate
```

The four questions of §1 map onto the model as follows.

| Question | Answered by | Layer |
|---|---|---|
| Who is it? | `subject`, `subjectKey` resolved through the DID method | A + C |
| Who authorized it? | `authority`, `delegations`, each link signed by its delegator | A + B |
| In what context is it acting? | `governanceContext`, `policyRefs`, `trustContext` | A + B |
| What has it done? | `credentials`, each a pointer with status and digest | B + C |

---

## 6. The Passport Object

A passport is a JSON document. Its normative form is defined by the members below; its wire encoding is JSON (UTF-8), and its signed and digested forms use the canonicalization of §6.4.

### 6.1 Members

Presence: **M** mandatory, **C** conditional (condition stated), **O** optional.
Provenance: **A** claim, **B** pointer, **C** observation, **D** derived.

| Member | Type | Presence | Prov. | Condition, source and meaning |
|---|---|---|---|---|
| `@context` | array of strings | M | — | First element `https://www.w3.org/ns/did/v1`; second the passport context URI (§22.1). |
| `type` | string | M | — | The string `Cha2aAgentPassport`. |
| `specVersion` | string | M | — | The version of this specification the document conforms to. |
| `passportId` | string (URN) | M | A | Identifies the **lineage**: one logical passport, stable across revisions. Form in §6.2. |
| `passportDigest` | object | M | D | `{ "algorithm": "sha256", "value": "<hex>" }` over the input of §6.4. Identifies the **revision**. |
| `subject` | string (DID) | M | A | The agent this passport applies to. MUST resolve through an identifier method the verifier supports (§7). |
| `subjectKey` | object | C | A | The subject's own verification key. Mandatory when a profile requires subject-signed actions (§15.2 P2 and above). Members in §7.2. |
| `issuer` | string (DID) | M | A | The party that signed this passport. MUST be the controller of the key named in `proof.verificationMethod`. |
| `issuedAt` | string (timestamp) | M | A | When this revision was signed. |
| `notBefore` | string (timestamp) | O | A | Earliest instant at which the revision is valid. Absent means `issuedAt`. |
| `expiresAt` | string (timestamp) | M | A | Instant after which the revision is invalid. Absence is not permitted: an authority with no end is not delegable (§11.3). |
| `principal` | object | C | A | Mandatory when the subject acts on behalf of another party. Members in §8.1. |
| `governanceContext` | object | M | A + B | Members in §10.3. An empty object is permitted and asserts that no governance context is claimed. |
| `capabilities` | array of objects | M | A | What the subject can do. An empty array is permitted. Members in §9.1. |
| `authority` | array of objects | C | A + B | Mandatory (non-empty) when the passport is presented to justify an action. Members in §9.3. |
| `delegations` | array of objects | C | A + B | Mandatory when any `authority` entry was granted through a chain of more than one link. Members in §11.1. |
| `policyRefs` | array of objects | C | B | Mandatory (non-empty) when `authority` is non-empty. Members in §12.1. |
| `credentials` | array of objects | C | B + C | Mandatory (non-empty) for profiles P3 and P4. Members in §13.3. |
| `status` | object | M | C | The subject's identifier status as read from the registry. Members in §14.3. |
| `trustContext` | object | M | A | Members in §17.1. |
| `proof` | object | M | A | The issuer's signature. Members in §6.4. |

**PP-1.** A passport MUST NOT contain a member that §6.1 does not define, unless its name begins with `x-`. Extension members MUST be ignored by a verifier that does not understand them, and MUST NOT be required for any profile to pass. *(Derivation: G8 requires extension without redesign; an unnamespaced extension would collide with a future version of this specification.)*

**PP-2.** A verifier MUST NOT reject a passport because of an `x-` member it does not recognise.

**PP-3.** A member declared mandatory MUST be present even when its value is empty (an empty array or an empty object), so that "not claimed" and "not present" are distinguishable.

### 6.2 `passportId`

```
urn:cha2a:passport:<issuer-scope>:<opaque>
```

- `issuer-scope` is the issuer's registered identifier: the host name for a domain-based issuer (`compliancehub.cn`), or the subject identifier of the issuing DID.
- `opaque` is an issuer-chosen value unique within that scope. A ULID or a UUIDv7 is RECOMMENDED so that issuance order is recoverable.

**PP-4.** `passportId` MUST NOT be a `did:cha2a` identifier. *(Derivation: a passport is a document issued by a party, not a subject the registry maintains. Assigning it a resolvable DID would place its issuance in the registry and contradict §19 R1.)*

**PP-5.** Two passports with the same `passportId` and different `passportDigest.value` are revisions of one lineage. A verifier MUST treat only the revision presented as current, and MUST NOT merge members across revisions.

### 6.3 The three provenance classes

**PP-6.** A verifier MUST classify every member it relies on into exactly one provenance class, and MUST NOT treat a Layer B or Layer C member as though the issuer's signature established it.

| Class | What the signature establishes | What it does not establish |
|---|---|---|
| **A — claim** | that the issuer asserted this value at `issuedAt` | that the value is true |
| **B — pointer** | that the issuer asserted this reference resolves to an object it considers relevant | that the object exists, is current, or says what the issuer implies |
| **C — observation** | that the issuer read this value from the named source at the named time | that the value is still current at decision time |

**PP-7.** A member of Layer C MUST carry both `source` and `observedAt`. A verifier MUST re-read Layer C members when the age of the observation exceeds `status.statusMaxAge`, and MUST NOT accept a stale observation as current (§14.4).

**PP-8.** A Layer B member MUST identify its target unambiguously (a URI, a DID, or a URN), and MUST carry a digest when the target's content is material to the claim. A pointer without a digest establishes only that an object was named.

### 6.4 Canonical form, digest and signature

**Definitions.**

- `digestInput` = the JCS serialization of the passport with the members `proof` and `passportDigest` removed.
- `passportDigest.value` = SHA-256 of the UTF-8 bytes of `digestInput`, lowercase hexadecimal.
- `proofInput` = the JCS serialization of the passport with the member `proof` removed.
- `proof.payload` = the string `proofInput`.

**PP-9.** `passportDigest.value` MUST equal the SHA-256 of the recomputed `digestInput`. A mismatch MUST produce `invalid`.

**PP-10.** The signature MUST be computed over the UTF-8 bytes of `proof.payload`.

**PP-11.** The `proof` object MUST carry `type`, `created`, `verificationMethod`, `proofPurpose` and `signatureValue`, and MUST carry `payload` as specified above. The signature suite `Ed25519Signature2020` with `proofPurpose` of `assertionMethod` MUST be supported. *(Derivation: this is the shape the reference registry already emits at `/api/v1/trust/proof`, so a conforming verifier reuses one code path for both. See Appendix B, row B-4.)*

**PP-12.** `proof.verificationMethod` MUST resolve, through the issuer's DID Document, to a key listed under the `assertionMethod` verification relationship. A verifier MUST NOT use a key that the DID Document does not list for that purpose.

**PP-13.** A verifier MUST reject a passport whose `issuer` is not the controller of the resolved key, and MUST reject a `proof.verificationMethod` whose DID portion differs from `issuer`.

**PP-14.** Signing and digesting MUST use JCS. A verifier MUST NOT attempt to re-serialize the document before verifying; it MUST operate on the received `proof.payload` bytes and on a canonical recomputation for the digest only.

### 6.5 What the signature does not cover

**PP-15.** The signature does not establish that any pointer resolves, that any observation is current, that any delegated authority is still held, or that any evidence exists. A verifier that reports a verdict without resolving the pointers and refreshing the observations reports the issuer's assertion as though it were a fact.

---

## 7. Identity

### 7.1 Identifier binding

**PP-16.** `subject` MUST be a DID, and MUST resolve to a DID Document through a method the verifier supports.

**PP-17.** When `subject` uses the `did:cha2a` method, the DID MUST conform to the ABNF of `did-method-cha2a.md` §3.1, and the literal prefix and resource-type slot MUST be treated as case-sensitive lowercase as required by its §3.4. A verifier MUST apply the method's normalization rules before comparing identifiers.

**PP-18.** A verifier MUST compare DIDs by exact match after normalization. It MUST NOT treat two identifiers as the same because one is a prefix of the other, and MUST NOT infer authority from an identifier's resource type or from a shared host.

**PP-19.** The passport MUST NOT require a new `did:cha2a` resource type. *(Derivation: the resource-type table of `did-method-cha2a.md` §3.2 is closed to additions by pull request, and the file is cited by a W3C registry entry at a fixed version. A passport is not a resource the registry issues.)*

**PP-20.** `issuer` MUST be a DID, MUST resolve, and MUST NOT be required to share a method with `subject`.

### 7.2 `subjectKey`

| Member | Type | Presence | Meaning |
|---|---|---|---|
| `keyId` | string | M | The verification-method identifier, e.g. `did:cha2a:agent:dshlib#agent-key`. |
| `algorithm` | string | M | The key algorithm. |
| `publicKeyMultibase` | string | C | Present when the key is resolved through the DID Document's `verificationMethod`. |
| `fingerprint` | string | M | The fingerprint reported by the identifier method's key endpoint, when one exists. |

**PP-21.** The subject key MUST be a key the subject controls, and MUST be distinct from the registry's signing key. *(Derivation: `did-method-cha2a.md` §5 produces a DID Document in which the registry key and the subject's own key are separate verification methods; only the second can sign for the subject.)*

**PP-22.** When `subjectKey` is present, a verifier MUST resolve the subject's current key and compare its fingerprint with `subjectKey.fingerprint`. A mismatch MUST produce `invalid`. *(Derivation: a passport outlives a key rotation. Comparing against the live key is what makes the binding current; comparing against the passport's own copy would make a rotated key valid forever.)*

**PP-23.** A verifier MUST NOT infer that the subject participated in an exchange from the presence of `subjectKey`. Participation is established by a signature over the action (§21, threat TH-2).

### 7.3 Separability

**PP-24.** Identity claims MUST be separable from capability, authority and evidence claims, so that a profile requiring only identity can be satisfied without receiving the rest (§16).

---

## 8. Principal and Responsibility

An agent may act autonomously while still acting for a party. Where that relationship exists, the passport states it explicitly and names the party.

### 8.1 `principal`

| Member | Type | Presence | Meaning |
|---|---|---|---|
| `did` | string (DID) | M | The principal. |
| `role` | string | M | The relationship asserted: `operating-organization`, `owner`, `controller`, `client`, or a value from a registered vocabulary. |
| `onBehalfOf` | string (DID) | O | A further party, when the principal itself acts for another. Chain length beyond one MUST be represented by `delegations` (§11), not by nesting. |
| `verificationRef` | string (URI) | O | Where the relationship is evidenced. |

**PP-25.** When `principal` is present, the principal DID MUST resolve, and the passport MUST NOT assert a relationship that the principal's own governance records contradict — a verifier able to check the principal's records MUST prefer them over this claim.

**PP-26.** `principal.onBehalfOf` MUST NOT be nested more than one level. A longer chain is a delegation and MUST be represented in `delegations`.

### 8.2 What the passport evidences

```
Human / Organization  →  Principal  →  Agent  →  Action
        governance          mandate      execution
```

**PP-27.** The passport evidences the technical relationships along this chain. It does not allocate legal liability, and no member of it MUST be presented as doing so.

**PP-28.** A verifier MUST be able to name the party answerable for an action, given the action and its passport, **without contacting that party** (G4). When it cannot, the verdict is `indeterminate` and the missing link MUST be named in the output.

---

## 9. Capability and Authority

### 9.1 `capabilities[]`

| Member | Type | Presence | Meaning |
|---|---|---|---|
| `name` | string | M | The capability, as a skill DID, a name, or a namespaced label. |
| `version` | string | O | Version or compatibility range. |
| `protocols` | array of strings | O | Interaction protocols through which the capability is reachable. |
| `assertion` | string | M | `self-declared` or `attested`. |
| `attestationRef` | string (URI) | C | Mandatory when `assertion` is `attested`. |

**PP-29.** `assertion` MUST be present and MUST be exactly one of `self-declared` or `attested`. *(Derivation: `agent-identity.md` §5 separates declared capability from verified capability. Making the distinction a mandatory, machine-readable field is what prevents the separation from being lost in transport.)*

**PP-30.** A capability with `assertion: self-declared` MUST NOT be treated as authority, and MUST NOT satisfy any check that requires authority. *(Derivation: §9.2.)*

**PP-31.** A verifier MUST NOT treat a capability as verified because the passport carrying it is signed. The issuer's signature attests to the declaration, not to the capability.

### 9.2 Capability and Authority

```
   Capability  =  can do        Authority  =  may do
                  a property of the subject        a property of a governance context
```

**PP-32.** Capability and authority MUST NOT be conflated. A conforming passport MUST represent them in separate members, and a conforming verifier MUST derive permission from `authority` alone.

### 9.3 `authority[]`

| Member | Type | Presence | Meaning |
|---|---|---|---|
| `grantId` | string (URN) | M | Identifies the grant. |
| `scope` | array of strings | M | The permitted operations. |
| `grantedBy` | string (DID) | M | The granting party. |
| `policyRef` | string | C | Mandatory when `policyRefs` is non-empty: the identifier of the policy under which the grant holds. |
| `constraints` | object | O | Narrowing conditions (§9.4). |
| `notBefore` | string (timestamp) | O | Start of validity. Defaults to the passport's `notBefore`. |
| `notAfter` | string (timestamp) | M | End of validity. MUST NOT exceed the passport's `expiresAt`. |
| `evidenceRef` | string (URI) | O | Where the grant is evidenced. |

**PP-33.** Every `authority` entry MUST name a `grantedBy` party, and every `grantedBy` party MUST be either the `principal`, a party reachable through `delegations`, or an organization controller reachable through `governanceContext`.

**PP-34.** `notAfter` MUST be present on every authority entry. An authority with no end is not expressible.

**PP-35.** A verifier asked to justify an action MUST find an `authority` entry whose `scope` contains the operation, whose validity window contains the decision time, and whose constraints are satisfied. Absence MUST produce `invalid`; an entry whose constraints cannot be evaluated MUST produce `indeterminate`.

### 9.4 `constraints`

Constraints narrow, never widen. Recognised members:

| Member | Meaning |
|---|---|
| `maxDepth` | Maximum delegation depth from this grant. |
| `counterparties` | A closed list of DIDs the authority may be exercised against. |
| `purpose` | The declared purpose, which the action must match. |
| `rateLimit` | A bounded rate, with the window stated. |
| `humanApproval` | `required` when a human approval must precede the action, together with the DIDs permitted to approve. |
| `dataClasses` | Data classifications the authority may touch. |
| `x-*` | Deployment-defined constraints. |

**PP-36.** A constraint MUST NOT be expressible in a form that widens the grant. A verifier MUST reject an authority entry whose constraints widen the scope of its parent, and MUST NOT ignore a constraint it cannot evaluate — an unevaluable constraint produces `indeterminate`.

---

## 10. Governance Context and Roles

### 10.1 Roles

**PP-37.** A role MUST be scoped by issuer, by governance domain, and by validity period. A role with no issuer or no validity period MUST be rejected. *(Derivation: `organization-governance.md` answers who is qualified to authorize; an unscoped role answers nothing, because anyone could have issued it for any period.)*

**PP-38.** A role MUST name its governance domain as one of `organization`, `group`, `society`, or `service`.

### 10.2 Governance domains

| Domain | Bounds authority by | Source |
|---|---|---|
| `organization` | one organization's charter and records | `organization-governance.md` |
| `group` | a collaboration context spanning organizations | `group-collaboration.md` |
| `society` | a federation-wide agreement | `trustContext` (§17) |
| `service` | one service's own terms | the service operator |

**PP-39.** An authority granted in one governance domain MUST NOT be treated as holding in another. A verifier MUST compare the domain of the grant with the domain the action occurs in.

### 10.3 `governanceContext`

| Member | Type | Presence | Meaning |
|---|---|---|---|
| `organization` | array of DID strings | O | Organizations the subject belongs to. |
| `groups` | array of objects | O | Group memberships: `{ "group": "<urn or DID>", "role": "<string>", "validUntil": "<timestamp>", "evidenceRef": "<uri>" }`. |
| `roles` | array of objects | O | Roles: `{ "role": "<string>", "domain": "<string>", "issuer": "<did>", "validUntil": "<timestamp>", "evidenceRef": "<uri>" }`. |

**PP-40.** Every member of `governanceContext` is a Layer A claim unless it carries an `evidenceRef`, in which case the reference is Layer B and the claim is Layer A. A verifier MUST NOT report a membership as established when only the claim is present.

**PP-41.** Group membership MUST be checked against the group's own records when they are reachable. The passport records the claim; the group's records decide it.

---

## 11. Delegation

Delegation is the mechanism by which authority reaches an agent without the principal issuing a new grant for every operation. It is the part of the passport most exposed to silent privilege escalation, so its rules are the most explicit.

### 11.1 `delegations[]`

| Member | Type | Presence | Meaning |
|---|---|---|---|
| `delegationId` | string (URN) | M | Identifies this link. |
| `delegator` | string (DID) | M | The party transferring authority. |
| `delegatee` | string (DID) | M | The party receiving it. |
| `scope` | array of strings | M | The authority transferred. |
| `constraints` | object | O | Narrowing conditions, as §9.4. |
| `notBefore` | string (timestamp) | O | Start of validity. |
| `notAfter` | string (timestamp) | M | End of validity. |
| `furtherDelegation` | string | M | `none`, `same-scope`, or `explicit`. |
| `depth` | integer | M | The link's position in the chain, counting from the principal as 1. |
| `maxDepth` | integer | M | The deepest link the chain may contain. |
| `parentDelegationId` | string (URN) | C | Mandatory when `depth` is greater than 1; MUST be absent at `depth` 1. |
| `revocationRef` | string (URI) | O | Where this link's revocation status is published. |
| `proof` | object | M | The delegator's signature over the link (§11.2). |

### 11.2 Rules

**PP-42 — attenuation.** For every link, `scope` MUST be a subset of the parent's `scope`, and `constraints` MUST narrow the parent's. A link whose scope is not a subset MUST be rejected, and the rejection MUST name the widening member. *(Derivation: authority in this family is granted, never assumed; a subset relation is the only check that cannot be satisfied by relabelling.)*

**PP-43 — monotonicity.** A chain is valid only when every link's authority set is a subset of the link before it. A verifier MUST evaluate the whole chain and MUST NOT stop at the first link that satisfies the requested scope.

**PP-44 — explicit depth.** `depth` and `maxDepth` MUST be present on every link, MUST be integers, and `depth` MUST NOT exceed `maxDepth`.

**PP-45 — further delegation.** `furtherDelegation` MUST take one of three values: `none` forbids any child link; `same-scope` permits a child link whose scope equals this link's; `explicit` permits a child link only when this link's `constraints` names the permitted delegatees.

**PP-46 — acyclic.** A chain MUST be acyclic. A verifier MUST reject a chain in which a delegator appears more than once, including through different identifiers that normalize to the same DID.

**PP-47 — termination.** Every chain MUST terminate either at the `principal` of the passport or at an organization controller reachable through `governanceContext`. A chain that terminates at neither MUST be rejected. *(Derivation: §8.2 requires that the answerable party be nameable.)*

**PP-48 — per-link signature.** Every link MUST carry its delegator's signature over the link's canonical form, and a verifier MUST verify each link independently. A verifier MUST NOT accept a link on the strength of the passport's own signature. *(Derivation: the passport signature is the issuer's. Accepting a link under it would let an issuer manufacture authority that no delegator granted, and would remove the delegator from the record.)*

**PP-49 — validity intersection.** The validity window of a link MUST be the intersection of its own window, its parent's window, and the passport's window. An action outside any of the three MUST be rejected.

**PP-50 — revocation cascade.** Revoking a link MUST invalidate every link whose `parentDelegationId` chain includes it. A verifier that can reach a `revocationRef` MUST check it, and MUST check the refs of every ancestor link, not only the leaf.

**PP-51 — self-delegation.** A link whose `delegator` and `delegatee` are the same subject MUST be rejected.

### 11.3 What is deliberately absent

**NIV-1 — a delegation revocation protocol.** The passport names `revocationRef` per link. How a link is revoked, and how that revocation reaches a verifier, is not defined here: it is a registry or application concern, and the precondition for defining it in this document is recorded in §3.4. Until then, revocation is observed through the ref, and an unreachable ref produces `indeterminate` rather than `valid`.

**NIV-2 — the human override protocol.** `constraints.humanApproval` records that an approval is required and names who may give it. The protocol that carries the approval, its representation, and its revocation are not defined here. *(Test: a deployment satisfies every profile with `humanApproval` absent. If a profile cannot pass without it, an approval workflow has leaked into this specification.)*

---

## 12. Policy References

A passport identifies the policies under which its authority holds. It does not carry them and does not evaluate them.

### 12.1 `policyRefs[]`

| Member | Type | Presence | Meaning |
|---|---|---|---|
| `id` | string (URI or URN) | M | The policy identifier. |
| `issuer` | string (DID) | M | The party that issued the policy. |
| `version` | string | M | The policy version. |
| `scope` | array of strings | O | The operations the policy governs. |
| `effectiveFrom` | string (timestamp) | O | Start of the policy's effect. |
| `effectiveUntil` | string (timestamp) | O | End of the policy's effect. |
| `digest` | object | O | `{ "algorithm", "value" }` over the policy document, when the exact text is material. |

**PP-52.** Every member of `policyRefs` MUST carry `id`, `issuer` and `version`. A policy reference without a version MUST be rejected. *(Derivation: the family records every external object with its version and date. An unversioned policy reference cannot be checked against the policy that was in force when the authority was granted.)*

**PP-53.** Every `authority.policyRef` MUST match the `id` of exactly one entry in `policyRefs`. A dangling `policyRef` MUST produce `invalid`.

**PP-54.** A verifier MUST NOT evaluate policy. It MUST report which policy references the decision relied on, and the version of each, and leave evaluation to the application (§19 R3).

**PP-55.** A verifier that cannot reach a policy document whose `digest` is present MUST NOT report the action as permitted under that policy. It reports `indeterminate`.

---

## 13. Credentials, Attestations and Evidence

### 13.1 Reuse of the evidence layer

**PP-56.** Evidence predicate types MUST use the URIs of `evidence-record.md` §3, including the reused in-toto predicates and the `cha2a/*` namespaced predicates. This document introduces no predicate.

**PP-57.** A credential reference MUST carry `evidenceRef` and, where the content is material, `artifactDigest`. The digest form used by the evidence layer is:

```
"artifactDigest": { "sha256": "<lowercase hex>" }
```

**PP-58.** The passport MUST NOT contain an evidence body. It carries references, statuses and digests. *(Derivation: `overview.md` §4.4 R2 — what a subject can sign for itself stays with the subject; the registry and the passport store a pointer or a hash, never the content.)*

### 13.2 Verifier identity

**PP-59.** The `verifier` of a credential MUST be a registered party whose DID resolves, and whose signature over the attestation establishes that it made the statement. A verifier that cannot be resolved MUST cause the credential to be reported as unestablished, not as false.

**PP-60.** A credential MUST NOT be treated as established by the passport's signature. The signature attests to the reference, not to the attestation.

### 13.3 `credentials[]`

| Member | Type | Presence | Meaning |
|---|---|---|---|
| `id` | string | M | The credential identifier. |
| `predicateType` | string (URI) | M | As §13.1. |
| `verifier` | string (DID) | M | The attesting party. |
| `result` | string | O | The recorded result, where the predicate has one (`passed`, `failed`, or a predicate-defined value). |
| `checkedAt` | string (timestamp) | O | When the check ran. |
| `issuedAt` | string (timestamp) | M | When the credential was created. |
| `evidenceRef` | string (URI) | M | Where the evidence is archived. |
| `artifactDigest` | object | C | Mandatory when the subject content is material. |
| `status` | object | M | `{ "state": "valid"\|"revoked"\|"expired"\|"unknown", "source": "<uri>", "observedAt": "<timestamp>" }`. |

**PP-61.** Every credential MUST carry a `status` observation with a source and a time, and a verifier MUST refresh it when older than `statusMaxAge`. A credential whose status cannot be read MUST be reported as `unknown`, and a profile that requires the credential MUST then return `indeterminate`.

**PP-62.** A credential whose `result` is present and is not `passed` MUST NOT be counted toward a profile that requires a passed check.

### 13.4 Availability

**PP-63.** An issuer registers a credential reference under a commitment that `evidenceRef` resolves. When it does not resolve, the reference is unverifiable, and a verifier MUST report the resulting verdict rather than omitting the credential. *(Derivation: `evidence-record.md` §4 — a broken reference degrades the trust summary, and the degradation must be visible rather than silent.)*

---

## 14. Lifecycle and Status

### 14.1 Passport states

```
                 ┌──────────┐
   created ─────▶│  active  │◀───────────┐
                 └────┬─────┘            │
          suspended ◀──┤                  │ reinstated
                      │                  │
                 ┌────▼─────┐       ┌────┴─────┐
                 │suspended │───────┘          │
                 └────┬─────┘                  │
                      │                        │
                 ┌────▼─────┐   ┌──────────┐   │
                 │ revoked  │   │ expired  │───┘  renewed (new revision)
                 └──────────┘   └──────────┘
                   terminal
```

### 14.2 Transitions

| Transition | From → To | Who may perform it | Effect |
|---|---|---|---|
| Issue | — → `active` | the issuer | a new `passportId`, or a new revision of an existing one |
| Renew | `active` \| `expired` → `active` | the issuer | a new revision with a later `expiresAt`; `passportId` unchanged |
| Update | `active` → `active` | the issuer | a new revision with changed members; `passportId` unchanged |
| Suspend | `active` → `suspended` | the issuer, or the principal | the revision remains verifiable but no profile passes |
| Reinstate | `suspended` → `active` | the issuer | a new revision, or the withdrawal of the suspension |
| Revoke | any non-terminal → `revoked` | the issuer, or the principal | terminal; no profile passes |
| Expire | `active` → `expired` | automatic at `expiresAt` | no profile passes |

**PP-64.** The registry MUST NOT be able to change the state of a passport. The registry does not hold passports. *(Derivation: §19 R1 and R2 — the registry carries identity and status, and the passport is held by the party that signed it.)*

**PP-65.** Passport revocation and identifier revocation MUST be distinguished in reporting. A revoked passport does not imply a deactivated DID, and a deactivated DID does not imply a revoked passport.

**PP-66.** A suspension or revocation MUST reach a verifier either through a new revision or through a status source named in the passport. A state change that reaches no verifier MUST NOT be reported as effective.

### 14.3 `status`

| Member | Type | Presence | Meaning |
|---|---|---|---|
| `state` | string | M | The passport's own state: `active`, `suspended`, `revoked`, `expired`. |
| `subjectRecord` | object | M | The subject's identifier status as read from the registry. |
| `source` | string | M | The identifier of the status source. |
| `observedAt` | string (timestamp) | M | When the observation was made. |
| `statusMaxAge` | integer (seconds) | O | The age beyond which the observation must be refreshed. Default (§14.4). |

`subjectRecord` mirrors the fields the identifier method's trust lookup returns:

```
{ "active": <boolean>, "status": "<string>", "level": <integer>,
  "levelName": "<string>", "verificationStatus": "<string>", "revoked": <boolean> }
```

**PP-67.** `status.subjectRecord` MUST be a Layer C observation carrying `source` and `observedAt`, and a verifier MUST refresh it rather than trusting the carried copy.

**PP-68.** A verifier MUST distinguish `active` from `verified`. An `active` record with a level of zero and a `verificationStatus` of `self-declared` satisfies a check for *existence and currency* and satisfies no check for *verification*. *(Derivation: the reference registry reports these as separate fields; reporting them as one collapses two different facts.)*

**PP-69.** The registry's record is decisive for the facts the registry owns: existence, currency, deactivation, revocation and the certification level. The issuer's signature is decisive for the claims the issuer asserts. Where the two disagree, the disagreement MUST be reported and MUST NOT be resolved silently in the issuer's favour.

### 14.4 Freshness

**PP-70.** `statusMaxAge` defaults to **300 seconds** when absent. A verifier MUST refresh any Layer C observation older than `statusMaxAge` before reaching a verdict. *(Derivation: `statusMaxAge` is a deployment parameter, DP-1. The default exists so that a passport which omits it is not thereby granted indefinite currency.)*

**PP-71.** Three timestamps carry three different meanings and MUST NOT be substituted for one another:

| Member | Meaning | What it does not mean |
|---|---|---|
| `issuedAt` | when the issuer signed this revision | that the content is current |
| `expiresAt` | when the revision stops being valid | that delegated authority is still held |
| `status.observedAt` | when the subject's registry status was read | when the passport was issued |

---

## 15. Verification

### 15.1 Inputs and output

**Inputs:** a passport `P`; the profile `Pr` requested; the operations `S` being justified, if any; the decision time `T`; the verifier's supported methods and canonicalization; a status-freshness bound.

**Output:** a verdict, the trust context used, and an itemised list of the facts relied on with the source and observation time of each.

### 15.2 Profiles

| Profile | Question it answers | Required members beyond the mandatory core |
|---|---|---|
| **P0 — Identity** | who is it | none |
| **P1 — Organization** | who does it belong to | `principal` or a non-empty `governanceContext.organization` |
| **P2 — Governance** | on whose authority | `authority`, `policyRefs`, `subjectKey`, `delegations` where the chain exceeds one link |
| **P3 — Compliance** | what is behind the claim | all of P2 plus non-empty `credentials` |
| **P4 — High assurance** | may this specific action proceed | all of P3 plus satisfying constraints, fresh status, and a delegation depth within `maxDepth` |

**PP-72.** A profile MUST be named in every verdict. A verdict reported without its profile MUST NOT be relied on.

**PP-73.** A verifier MUST NOT silently downgrade the requested profile. When a required member is missing, the verdict is `invalid` and the missing member is named.

### 15.3 The three-valued verdict

| Verdict | Means |
|---|---|
| `valid` | every check the profile requires passed |
| `invalid` | a check the profile requires failed |
| `indeterminate` | a check the profile requires could not be evaluated — an unreachable source, an unresolvable pointer, an unevaluable constraint, a stale observation that could not be refreshed |

**PP-74.** A verifier MUST distinguish `invalid` from `indeterminate`. *(Derivation: this family fails closed at the decision point. Folding "could not check" into "checked and failed" misreports the reason, and folding it into "valid" is the failure this specification exists to prevent.)*

**PP-75.** `indeterminate` MUST name the party or source that could not be reached and the check that depended on it.

### 15.4 Procedure

```
  1  STRUCTURE   P conforms to §6; specVersion supported;
                 members required by Pr are present                     → invalid on failure
  2  ISSUER      resolve P.issuer; obtain the key at proof.verificationMethod;
                 it is listed under assertionMethod;
                 verify the signature over proof.payload (PP-10..PP-14)  → invalid on failure
  3  DIGEST      recompute digestInput; compare passportDigest (PP-9)     → invalid on failure
  4  SUBJECT     resolve P.subject; compare subjectKey.fingerprint (P2+) → invalid on mismatch
  5  TIME        notBefore ≤ T ≤ expiresAt                              → invalid outside
  6  STATUS      read the subject's registry status if the observation
                 is older than statusMaxAge (PP-67, PP-70)              → indeterminate if unreachable
                                                                          invalid if revoked or inactive
  7  AUTHORITY   for each operation in S, find a covering authority entry
                 with a satisfied validity window and constraints (PP-35) → invalid if none
                                                                          indeterminate if unevaluable
  8  DELEGATION  verify each link's signature, attenuation, depth,
                 acyclicity, termination, revocation refs (PP-42..PP-51)  → invalid on failure
                                                                          indeterminate if a revocation
                                                                          ref is unreachable
  9  POLICY      every authority.policyRef resolves to a policyRefs entry
                 with a version (PP-52, PP-53)                          → invalid on failure
 10  EVIDENCE    for P3+, refresh each credential's status (PP-61)       → unknown → indeterminate
                                                                          failed result → invalid
 11  DISCLOSE    emit only the fields of the profile's disclosure set (§16)
 12  OUTPUT      verdict · trust context · facts relied on, each with
                 source and observation time
```

**PP-76.** The checks MUST be performed in an order in which a failure at an earlier step prevents reliance on a later result. A verifier MUST NOT report any Layer B or Layer C fact as established when step 2 failed.

**PP-77.** A verifier MUST record, for each fact relied on, whether it came from the issuer's claim, from a resolved pointer, or from a named observation, and MUST make that record available to the relying party.

---

## 16. Disclosure and Privacy

**PP-78.** A verifier MUST request the minimum profile that answers its question, and an issuer or holder MUST disclose only the fields of that profile's set.

### 16.1 Disclosure sets

| Profile | Fields disclosed |
|---|---|
| **P0** | `specVersion`, `subject`, `issuer`, `issuedAt`, `expiresAt`, `status.state`, `status.subjectRecord.active`, `trustContext.domain` |
| **P1** | P0 plus `principal`, `governanceContext.organization`, `governanceContext.roles[].role` with its `domain` |
| **P2** | P1 plus `capabilities`, `authority`, `policyRefs`, `subjectKey.keyId`, `subjectKey.fingerprint`, `delegations[].delegator/delegatee/scope/notAfter/depth/maxDepth` |
| **P3** | P2 plus `credentials[].id/predicateType/verifier/result/status`, `evidenceRef` |
| **P4** | P3 plus the `constraints` of the authority entries in scope, `status.source`, `status.observedAt`, and the per-link `proof` of the delegation chain |

**PP-79.** A member outside the requested profile's set MUST NOT be disclosed by default. `capabilities`, `governanceContext.groups`, `credentials` and `principal` MUST NOT appear in a P0 response.

**PP-80.** A verifier MUST NOT disclose to a third party what it learned while verifying beyond what its own decision requires.

### 16.2 What a passport MUST NOT contain

**PP-81.** A passport MUST NOT contain any of the following:

| Excluded | Why |
|---|---|
| private key material, of any party | the passport is transmitted and stored outside the holder's control |
| an evidence body, a source file, or a payload under another party's rights | §19 R2 — the pointer and its digest are carried, not the content |
| a policy document | §12 — the reference is carried, not the text |
| a capability's implementation, code, or configuration | outside the subject of this document |
| an evaluation result, a score, a rating or an endorsement | G10 |
| a credential that no profile requests | §16.1 — a passport that carries it discloses it to every verifier |
| personal data beyond the principal's identifier and declared role | minimization; the passport is not an identity dossier |

**PP-82.** A passport that discloses a member only to withhold its meaning (by encoding, by reference to a private vocabulary, or by a value a verifier must already know) MUST be treated as disclosing it.

### 16.3 Separability

**PP-83.** The identity members of a passport MUST be usable without the governance members. A deployment that requires a full passport before it will verify an identifier has removed the minimal-disclosure property, and MUST NOT claim conformance with §16.

---

## 17. Trust Context and Federation

A passport is valid within a domain, and not automatically in another.

### 17.1 `trustContext`

| Member | Type | Presence | Meaning |
|---|---|---|---|
| `domain` | string | M | The issuer's domain, as a URI or host. |
| `registryDid` | string (DID) | M | The registry whose status observations this passport relies on. |
| `validityDomain` | array of strings | M | The domains in which the passport is offered as valid. |
| `federation` | object | O | `{ "peers": [...], "recognisedBy": [...] }` — the federation relationships the issuer asserts. |
| `mapping` | array of objects | O | Vocabulary or policy mappings relied on: `{ "from": "<uri>", "to": "<uri>", "authority": "<did>" }`. |

**PP-84.** A verifier MUST check that its own domain appears in `validityDomain`, or that a `mapping` or federation relationship it trusts connects the passport's domain to its own. Absence MUST produce `invalid`, not `indeterminate`. *(Derivation: the absence of a trust relationship is a fact the verifier holds, not a fact it failed to reach.)*

**PP-85.** A verdict MUST name the trust context used and the mapping relied on.

**PP-86.** `federation.peers` is a Layer A claim. A verifier MUST verify a peer relationship against its own configuration before relying on it; a passport asserting a peer does not create one.

**PP-87.** Revocation and status across a federation boundary MUST be read from the source named in the passport, and an unreachable source MUST produce `indeterminate` rather than reliance on an assertion of good standing.

**PP-88.** A mapping MUST name the authority that established it. An anonymous mapping MUST be ignored.

---

## 18. Agent Passport and Agent Card

The two objects answer different questions, and the boundary between them is a decision rather than an accident.

### 18.1 Mapping — the reuse relation

| Passport member | Agent Card member | Relation |
|---|---|---|
| `subject` | `url` / identifier | the passport identifies; the card locates |
| `capabilities[].name` | `skills[].id` | the passport references; the card enumerates |
| `capabilities[].protocols` | `preferredTransport`, protocol bindings | the passport declares support; the card describes the binding |
| `authority` | — | the passport's subject matter |
| `delegations` | — | the passport's subject matter |
| `policyRefs` | — | the passport's subject matter |
| `credentials` | — | the passport's subject matter |
| — | `description`, `defaultInputModes`, `defaultOutputModes` | the card's subject matter |
| — | `provider` | the card's subject matter; the passport uses `principal` and `issuer`, which answer a different question |
| — | `securitySchemes` | the card's subject matter; the passport does not define how a service is reached |

**PP-89.** Where a fact appears in both, the Agent Card is authoritative for what the agent offers and how it is reached; the Passport is authoritative for identity, principal, authority, governance and evidence. A verifier that finds a disagreement MUST report it and MUST NOT resolve it silently.

### 18.2 Not-defining — the counter-example tests

**PP-90.** An A2A exchange MUST complete with no passport present. *(Test T-7a: remove every passport member from an exchange and the exchange still runs. If it does not, discovery or transport has leaked into this specification.)*

**PP-91.** A passport MUST verify with no Agent Card present. *(Test T-7b: verification takes no Agent Card field as input. If it does, this specification has duplicated the card's subject matter.)*

**PP-92.** A passport MUST NOT restate an Agent Card as a nested object. *(A nested card version-locks this specification to one revision of another specification's schema.)*

---

## 19. Placement Relative to the Registry and the Application

The passport's placement relative to the registry and the application follows `overview.md` §4.4:

| Rule | Applied to the passport |
|---|---|
| **R1** — the Registry carries identity and status only | the registry answers *who is this, and is it current*. It does not hold the passport. |
| **R2** — what a subject can sign for itself stays with the subject | the passport is held by its issuer and presented by its holder. The registry stores no passport and no passport digest. |
| **R3** — the Registry answers; the application decides | policy evaluation, admission and authorization happen in the application (§12, §15). |
| **R4** — the collaboration surface belongs to the applications | group membership is claimed in the passport and decided by the group's records (§10.2). |
| **R5** — fail-closed belongs at the decision point | `indeterminate` is produced by the verifier, at the decision point, and refusing is the relying party's act. |
| **R6** — every cross-boundary assertion is signed by the party that asserts it | every delegation link carries its delegator's signature (PP-48); the passport carries its issuer's. |

**PP-93.** The registry MUST NOT be required to store, index or serve a passport for a passport to be verifiable.

**PP-94.** Verification MUST be possible from public material alone: the passport bytes, the subjects' and issuers' DID Documents, and the status sources named in the passport. No call to the issuer's private API and no session with any party MUST be required. *(Derivation: G1, G2 — this is the property the family's core claim rests on: a verifier belonging to no party reaches the verdict.)*

### 19.1 Placement table

| Concept | Registry | Issuer or subject | Application |
|---|---|---|---|
| passport object | — | **held and signed here** | consumed |
| subject DID · keys | resolution entry point | key custody | cache |
| identifier status · level · revocation | **single source of truth** | observed | consumed |
| principal relationship | — | asserted | relied on within its own policy |
| authority · delegation chain | — | **held here** | evaluated against the action |
| policy documents | — | held by their issuer | referenced, not evaluated by the verifier |
| evidence body | — | held by its author | reachable through `evidenceRef` |
| verdict | — | — | **produced here** |

---

## 20. Relationship to the CHA2A Specification Group

**PP-95.** This document MUST NOT be cited as amending identifier semantics, evidence semantics, or governance semantics. Identity is normative in `did-method-cha2a.md`; evidence is normative in `evidence-record.md`; who is qualified to authorize is normative in `organization-governance.md`; group collaboration is normative in `group-collaboration.md`.

**PP-96.** The requirements of this document are normative for the **Passport object**: its members, its signature, its lifecycle, its verification procedure, its disclosure sets and its conformance tests. Where a requirement here and a requirement in another volume of the family apply to the same conduct, this document governs the passport object and the other volume governs its own subject.

**PP-97.** Every object this document names from outside the family MUST be recorded with its version, its date, and what is known of its adoption. A draft published by one project and adopted by nobody is a peer draft: citing it transfers no weight, and its immaturity does not discredit this document.

---

## 21. Security Considerations

| # | Threat | Property required | Requirement |
|---|---|---|---|
| TH-1 | **Forgery** — a passport not signed by its named issuer | issuer authenticity | PP-9, PP-10, PP-12, PP-13 |
| TH-2 | **Replay or bearer use** — a passport presented by a party that is not the subject | binding of the passport to a live act | PP-23; a passport is **not a bearer token**: possessing it grants nothing, and every action it justifies MUST carry a signature by the subject key over that action, including the operation, the counterparty and a verifier-chosen nonce. A verifier that accepts a passport as sufficient authority for an act has removed the subject from the record. |
| TH-3 | **Stale authorization** — authority that ended after `issuedAt` | currency | PP-67, PP-70, PP-71 |
| TH-4 | **Privilege escalation through delegation** | monotonic authority | PP-42 … PP-51 |
| TH-5 | **Declaration passing as permission** | the capability/authority separation | PP-29 … PP-32 |
| TH-6 | **Issuer key compromise** | revocation of the signer | PP-64, PP-66; the issuer's key MUST be rotatable through the identifier method's key mechanism, and a passport signed with a key that is no longer listed under `assertionMethod` MUST fail verification (PP-12) |
| TH-7 | **Identifier confusion** — a lookalike DID or a prefix relationship | exact identity | PP-17, PP-18 |
| TH-8 | **Disclosure by over-claiming** — a passport that carries more than any verifier needs | minimization | PP-78, PP-79, PP-81, PP-82 |
| TH-9 | **Silent staleness at the source** — a status source that is reachable but frozen | currency of the source | PP-87; a verifier MUST compare the source's own reported time with its own clock, and a source that reports no time MUST be treated as unable to establish currency |
| TH-10 | **Downgrade** — a verifier that reduces the requested profile when a check cannot be performed | honest verdict | PP-73, PP-74 |
| TH-11 | **Unattributed assertion** — a pointer reported as a fact | provenance | PP-6, PP-15, PP-77 |
| TH-12 | **Chain that terminates nowhere** | answerability | PP-47, PP-28 |
| TH-13 | **Signature-suite substitution** — a legitimately signed passport under a suite the verifier mis-handles | algorithm integrity | PP-11; a verifier MUST NOT accept a suite it does not implement, and MUST NOT fall back to a weaker one |
| TH-14 | **Correlation across presentations** — a stable identifier linking a subject's activity | minimization across time | `passportId` is scoped to the issuer and the lineage, not to the subject; a verifier MUST NOT treat two passports with different `passportId` as the same subject's presentations for linking purposes |

**PP-98.** These considerations are informative as a list and normative where a `PP-` identifier appears. Where a threat names a requirement, that requirement is the mitigation.

---

## 22. Serialization and Interoperability

### 22.1 Decided

| Aspect | Decision |
|---|---|
| Encoding | JSON, UTF-8 |
| Canonicalization | RFC 8785 (JCS) |
| Signature suite | `Ed25519Signature2020`, `proofPurpose: assertionMethod`; other suites by deployment agreement |
| Context | `@context` carries the DID Core context and the passport context URI `https://compliancehub.cn/cha2a/passport/v1` |
| Digest | SHA-256, lowercase hexadecimal |
| Membership rule | members not defined in §6.1 are rejected unless prefixed `x-` (PP-1) |

**PP-99.** A deployment MAY publish an additional JSON-LD context that maps the passport members to RDF terms. Such a context MUST NOT change the members' meanings, and a verifier MUST be able to verify a passport without fetching any context document. *(Derivation: a verification that requires a network fetch of a context introduces a dependency that can fail or change, and G2 requires verification from the passport and public endpoints only.)*

### 22.2 Mapping to Verifiable Credentials

**PP-100.** A deployment MAY express a passport as a W3C Verifiable Credential. The mapping MUST be: `issuer` → `issuer`; `subject` → `credentialSubject.id`; `issuedAt` → `issuanceDate`; `expiresAt` → `expirationDate`; `type` → a credential type including `Cha2aAgentPassport`; the remaining members → `credentialSubject` members under their names as defined here.

**PP-101.** A Verifiable Credential presentation MUST NOT be treated as satisfying a requirement of this document unless it satisfies the requirement as stated. The mapping does not weaken PP-9, PP-12, PP-42 or PP-74.

### 22.3 Reserved

**PP-102.** Predicate identifiers, constraint names and capability labels defined in `x-` namespaces MUST be recorded by the deployment that defines them, together with the date of definition.

---

## 23. Conformance

### 23.1 A conforming implementation

A conformance claim names a **role**. The roles are distinct and are claimed separately.

| Role | Must satisfy |
|---|---|
| **Issuer** | PP-1 … PP-15, PP-19, PP-24, PP-29, PP-34, PP-37, PP-38, PP-48, PP-52, PP-56 … PP-58, PP-64 … PP-66, PP-81, PP-95 |
| **Verifier** | PP-2, PP-6 … PP-18, PP-21 … PP-23, PP-28, PP-30 … PP-33, PP-35, PP-36, PP-39 … PP-51, PP-53 … PP-55, PP-59 … PP-63, PP-67 … PP-80, PP-83 … PP-94, PP-97 … PP-102 |
| **Holder** | PP-78, PP-79, PP-81 … PP-83 |

**PP-103.** A conformance claim MUST name its role, the profiles it supports, the signature suites it implements, and the version of this specification. A claim that names none of these MUST NOT be made.

### 23.2 Mandatory core for every role

**PP-104.** Every conforming implementation MUST support profile **P0** and MUST produce the three-valued verdict of §15.3.

### 23.3 Deployment parameters

| ID | Parameter | Default |
|---|---|---|
| DP-1 | `statusMaxAge` | 300 seconds |
| DP-2 | supported DID methods | the methods the deployment resolves; `did:cha2a` where the reference registry is used |
| DP-3 | signature suites beyond `Ed25519Signature2020` | none |
| DP-4 | constraint names recognised beyond §9.4 | none |
| DP-5 | the status source for a given domain | the registry named in `trustContext.registryDid` |
| DP-6 | the nonce freshness window for subject-signed actions (TH-2) | 300 seconds |
| DP-7 | whether a `verificationRef` or `evidenceRef` must be reachable for a given profile | reachable for P3 and P4 |
| DP-8 | the identifier scope used in `passportId` | the issuer's host name |

### 23.4 Tests

| Test | What it establishes |
|---|---|
| **T-1** | A passport whose subject uses `did:cha2a` resolves, and the resolved DID Document's verification relationships are honoured (PP-16 … PP-20). |
| **T-2** | A credential reference resolves to an attestation whose predicate URI is as defined by the evidence layer, and whose `artifactDigest.sha256` matches the fetched content (PP-56, PP-57). |
| **T-3** | A capability with `assertion: self-declared` fails a check that requires authority (PP-30), and an `assertion: attested` capability without `attestationRef` is rejected (PP-29). |
| **T-4** | An authority entry with no validity end, or with a role lacking an issuer, is rejected (PP-34, PP-37). |
| **T-5** | A group membership claimed in a passport is contradicted by the group's own records, and the verdict reports the contradiction rather than the claim (PP-41). |
| **T-6** | Two verifiers computing `digestInput` independently from the same document obtain the same bytes, and a document mutated in one character fails verification (PP-9, PP-14). |
| **T-7a** | An A2A exchange completes with no passport present (PP-90). |
| **T-7b** | A passport verifies with no Agent Card present (PP-91). |
| **T-8** | A delegation chain with a widening link is rejected and the widening member is named (PP-42). |
| **T-9** | Revoking a parent link invalidates a leaf link whose window and scope are otherwise satisfied (PP-50). |
| **T-10** | A chain terminating at neither the principal nor an organization controller is rejected (PP-47). |
| **T-11** | A stale `status.observedAt` with an unreachable registry produces `indeterminate`, and the unreachable source is named (PP-70, PP-74, PP-75). |
| **T-12** | Deleting every `evidenceRef` target leaves the passport structurally valid and produces `indeterminate` for P3, not `invalid` and not `valid` (PP-61, PP-63). |
| **T-13** | A passport carrying a member outside the requested profile's disclosure set is reported as over-disclosing (PP-79). |
| **T-14** | A passport whose `principal` is deactivated produces `invalid` with the registry's record named as the reason (PP-69). |
| **T-15** | An `active` subject record with `level: 0` and `verificationStatus: self-declared` passes an existence check and fails a verification check (PP-68). |

**PP-105.** Conformance evidence MUST be reproducible offline from published vectors, and MUST record the date of the run and the version of this specification tested.

---

## 24. Disposition of the v0.1 Open Issues

The v0.1 draft listed eleven open issues. None remains open as blank space.

| v0.1 item | Disposition | Where |
|---|---|---|
| Exact JSON / JSON-LD data model | **decided** — JSON with JCS canonicalization, the member set of §6.1, an optional RDF context | §6, §22.1, PP-99 |
| Normative DID / VC profile | **decided for DID** (PD-16 … PP-20, reuse of `did-method-cha2a.md`); **mapping decided, profile deferred** for VC | §7, §22.2, PP-100 |
| Credential and attestation formats | **reused, not defined** — the evidence layer's predicates and digest form | §13.1, PP-56, PP-57 |
| Policy expression and evaluation interface | **decided as a reference**: identifier, issuer, version, scope, window, optional digest. Evaluation is excluded | §12, PP-52 … PP-55 |
| Delegation-chain semantics | **decided** — attenuation, monotonicity, depth, acyclicity, termination, per-link signature, validity intersection, revocation cascade | §11, PP-42 … PP-51 |
| Revocation protocol | **registry-side, observed** — `status` and per-link `revocationRef`; the protocol itself is **NIV-1** with a precondition | §11.3, §14.3 |
| Federation trust model | **decided for the single-domain case** — `validityDomain` plus verified `mapping`; multi-registry endorsement deferred | §17, PP-84 … PP-88 |
| Privacy-preserving verification | **decided as disclosure sets**; **cryptographic selective disclosure is deferred** with a precondition | §16, §3.4 |
| Human Override protocol | **not in this version (NIV-2)** — the requirement is recorded and the authority named; the protocol is excluded with a counter-example test | §11.3, PP-36 |
| Interoperability mapping to Agent Card and A2A | **decided** — the mapping of §18.1, the boundary of PP-89, and the two counter-example tests | §18, T-7a, T-7b |
| Relationship between Passport and organizational identity systems | **decided as placement** — the passport references, the organization's records decide | §10, §19, PP-41, PP-93 |

---

## 25. Recommended Experimental Sequence

Each step names what it establishes and what it depends on. The order is the order of increasing dependence on facts the reference deployment does not yet provide (Appendix B).

| # | Step | Establishes | Blocked by |
|---|---|---|---|
| 1 | Issue a P0 passport for an existing registered agent, signed by its operating organization | PP-9 … PP-15, T-6, T-7b | nothing — every input exists today |
| 2 | Verify step 1 with an independent verifier implementation, offline from published vectors | G1, G2, PP-104, T-6 | step 1 |
| 3 | Add subject keys and require a subject-signed action alongside the passport | T-2, PP-21 … PP-23 | agent key registration exists; action signing does not (B-3) |
| 4 | Add `governanceContext` and a P1 profile against organization and group records | PP-37 … PP-41, T-5 | group records must be reachable (B-6) |
| 5 | Add a one-link delegation, then a two-link chain with a deliberate widening attempt | PP-42 … PP-51, T-8, T-9, T-10 | step 4 |
| 6 | Add `policyRefs` pointing at documents published by the issuing organization | PP-52 … PP-55 | an issuer must publish versioned policy documents |
| 7 | Add `credentials` referencing the existing evidence records, with status refresh | PP-56 … PP-63, T-2, T-12 | credential status must be readable per credential (B-5) |
| 8 | Test revocation: revoke a passport, revoke a DID, revoke a parent delegation, and confirm the three are distinguished | PP-64 … PP-66, T-14 | step 5 |
| 9 | Test disclosure: request P0 from a passport rich enough for P4, and confirm the P0 set is what returns | PP-78 … PP-83, T-13 | step 7 |
| 10 | Repeat steps 1–9 across two independent organizations with separate registries | G7, PP-84 … PP-88 | a second registry issuing passports (B-7) |
| 11 | Record the interoperability requirements the two deployments disagreed on, and revise this document | the working-draft cycle | step 10 |

**PP-106.** Each step MUST publish its vectors and its result before the next step is claimed, so that the sequence produces evidence rather than a schedule.

---

## 26. Normative Core — Requirement Index

```
IDENTITY      subject · subjectKey · issuer · identifier normalization
PRINCIPAL     principal · answerable party · one-level onBehalfOf
CAPABILITY    assertion ∈ {self-declared, attested} — never authority
AUTHORITY     grantId · scope · grantedBy · policyRef · constraints · notAfter
DELEGATION    attenuation · monotonicity · depth · acyclic · terminates · signed per link
POLICY        id · issuer · version — referenced, never evaluated
EVIDENCE      predicate by reference · evidenceRef · artifactDigest · status observed
STATUS        passport state ⊥ identifier state · source · observedAt · statusMaxAge
VERIFICATION  profile named · three-valued verdict · procedure order · provenance reported
DISCLOSURE    disclosure set per profile · excluded members
TRUST CONTEXT validityDomain · verified mapping · trust context named in the verdict
```

These members and rules form the normative conceptual core of the CHA2A Agent Passport.

**PP-107.** A conforming implementation MUST support every element of this core at profile P0, and MUST support the remainder to the extent that it claims the profiles that require them.

---

## Appendix A. Worked Example

Values are taken from the reference deployment at `compliancehub.cn` on 2026-10-04 and are illustrative, not normative.

**Resolved subject** — `did:cha2a:agent:dshlib`, whose DID Document carries two verification methods: `#registry-key`, controlled by `did:cha2a:registry:compliancehub.cn`, and `#agent-key`, controlled by the subject itself.

**Subject key** — from `/api/v1/agent/did:cha2a:agent:dshlib/keys`: `#agent-key`, Ed25519, fingerprint `2dfd3d33898f3063`, status `active`, registered 2026-08-27.

**Issuer** — `did:cha2a:org:compliancehub.cn`, active, level 0, `verificationStatus: self-declared`.

**Evidence** — one credential: `cred-mt1d9g3n-8bd39a`, predicate `https://in-toto.io/attestation/test-result/v0.1`, verifier `did:cha2a:verifier:dshlib`, result `passed`, `evidenceRef` `https://compliancehub.cn/evidence/dshlib/dshlib-agent/test-result.json`, `artifactDigest.sha256` `3b467db41f469d4478f37e12187107b56748d03ac9768e31471b19c07edf3852`.

```json
{
  "@context": [
    "https://www.w3.org/ns/did/v1",
    "https://compliancehub.cn/cha2a/passport/v1"
  ],
  "type": "Cha2aAgentPassport",
  "specVersion": "1.0",
  "passportId": "urn:cha2a:passport:compliancehub.cn:01J9Z6Q0K7R3M8WQ2V5N4TB1XA",
  "subject": "did:cha2a:agent:dshlib",
  "subjectKey": {
    "keyId": "did:cha2a:agent:dshlib#agent-key",
    "algorithm": "Ed25519",
    "publicKeyMultibase": "z6MkrzFfbUGZbdA4ev6v1RF2Ezvd7dPpDnU47CsD5yQ11GsR",
    "fingerprint": "2dfd3d33898f3063"
  },
  "issuer": "did:cha2a:org:compliancehub.cn",
  "issuedAt": "2026-10-04T10:00:00Z",
  "expiresAt": "2027-01-04T10:00:00Z",
  "principal": {
    "did": "did:cha2a:org:compliancehub.cn",
    "role": "operating-organization"
  },
  "governanceContext": {
    "organization": ["did:cha2a:org:compliancehub.cn"],
    "roles": [
      {
        "role": "catalog-publisher",
        "domain": "organization",
        "issuer": "did:cha2a:org:compliancehub.cn",
        "validUntil": "2027-01-04T10:00:00Z"
      }
    ]
  },
  "capabilities": [
    {
      "name": "did:cha2a:skill:catalog-publish",
      "version": "1.x",
      "protocols": ["a2a"],
      "assertion": "self-declared"
    }
  ],
  "authority": [
    {
      "grantId": "urn:cha2a:grant:compliancehub.cn:01J9Z6Q4Q1H7B2N8K5M3WP0ZRT",
      "scope": ["skill:publish", "skill:update"],
      "grantedBy": "did:cha2a:org:compliancehub.cn",
      "policyRef": "https://compliancehub.cn/policies/catalog-publishing",
      "constraints": { "rateLimit": { "max": 20, "window": "1d" } },
      "notAfter": "2027-01-04T10:00:00Z"
    }
  ],
  "policyRefs": [
    {
      "id": "https://compliancehub.cn/policies/catalog-publishing",
      "issuer": "did:cha2a:org:compliancehub.cn",
      "version": "2.1",
      "scope": ["skill:publish"],
      "effectiveFrom": "2026-09-01T00:00:00Z"
    }
  ],
  "credentials": [
    {
      "id": "cred-mt1d9g3n-8bd39a",
      "predicateType": "https://in-toto.io/attestation/test-result/v0.1",
      "verifier": "did:cha2a:verifier:dshlib",
      "result": "passed",
      "checkedAt": "2026-08-20T10:18:00Z",
      "issuedAt": "2026-08-20T10:17:19Z",
      "evidenceRef": "https://compliancehub.cn/evidence/dshlib/dshlib-agent/test-result.json",
      "artifactDigest": {
        "sha256": "3b467db41f469d4478f37e12187107b56748d03ac9768e31471b19c07edf3852"
      },
      "status": {
        "state": "valid",
        "source": "https://compliancehub.cn/api/v1/evidence/query?did=did%3Acha2a%3Aagent%3Adshlib",
        "observedAt": "2026-10-04T10:00:00Z"
      }
    }
  ],
  "status": {
    "state": "active",
    "source": "https://compliancehub.cn/api/v1/trust/query?did=did%3Acha2a%3Aagent%3Adshlib",
    "observedAt": "2026-10-04T10:00:00Z",
    "statusMaxAge": 300,
    "subjectRecord": {
      "active": true,
      "status": "active",
      "level": 2,
      "levelName": "L2 source",
      "verificationStatus": "registry-confirmed",
      "revoked": false
    }
  },
  "trustContext": {
    "domain": "https://compliancehub.cn",
    "registryDid": "did:cha2a:registry:compliancehub.cn",
    "validityDomain": ["https://compliancehub.cn"],
    "federation": { "peers": [], "recognisedBy": [] }
  },
  "passportDigest": {
    "algorithm": "sha256",
    "value": "<sha256 of JCS(P without proof and passportDigest)>"
  },
  "proof": {
    "type": "Ed25519Signature2020",
    "created": "2026-10-04T10:00:00Z",
    "verificationMethod": "did:cha2a:org:compliancehub.cn#registry-key",
    "proofPurpose": "assertionMethod",
    "payload": "<JCS(P without proof)>",
    "signatureValue": "<base64 detached Ed25519 signature over payload>"
  }
}
```

**What this example demonstrates.** The passport is verifiable at P3 with no private call to any party. Its `capabilities` entry is self-declared and therefore satisfies no authority check; its `authority` entry says what may be done; the credential is a pointer whose status must be refreshed; and the subject record is an observation, not a claim — the issuer asserts it read the registry, not that the registry says so now.

**What the example exposes.** The issuer is `level: 0` with `verificationStatus: self-declared`. Under PP-68 this satisfies an existence check and no verification check, which is the correct outcome and the reason the two fields are separate.

**On the signature suite.** The reference registry's `/api/v1/trust/proof` emits the same suite and the same payload-string convention over `{"did":…,"type":"TrustProof","created":…}`. That payload proves the DID was live when the proof was made; it does not bind any claim value. A passport signature over `proofInput` therefore reuses the suite and the verification code path while binding the content — which is the difference between a liveness proof and a claim.

---

## Appendix B. Implementation Status Against This Specification

Recorded 2026-10-04, item by item, against the reference deployment. The gaps are stated rather than omitted.

| # | Capability this specification requires | Status in the reference deployment | Consequence |
|---|---|---|---|
| B-1 | Passport issuance and verification | **not implemented** — no passport endpoint exists; `/api/v1/passport` and `/api/passports` return 404 with a `text/html` body | steps 1–2 of §25 are greenfield |
| B-2 | Subject identifier resolution | **implemented** — `/api/v1/did/{did}` returns a DID Core document | PP-16, PP-17 satisfied |
| B-3 | Subject-held key, registered and rotatable | **implemented for registration** — `/api/v1/agent/{did}/keys` returns `#agent-key` with fingerprint and rotation state; **not implemented for action signing** — no endpoint or convention records a subject signature over an action | PP-21 satisfied; PP-23 and threat TH-2 unexercised |
| B-4 | Signature suite and signed payload | **implemented as a liveness proof** — `/api/v1/trust/proof` returns `Ed25519Signature2020` over a payload of `{did, type, created}` | PP-11 satisfied; the payload **does not bind claim content**, so a passport needs its own payload (PP-10) |
| B-5 | Credential status readable per credential | **partially implemented** — `/api/v1/evidence/query?did=` returns credentials with `verifier`, `result`, `checkedAt`, `evidenceRef` and `artifactDigest.sha256`; there is no per-credential status endpoint | PP-61 satisfiable at subject granularity only; T-12 is exercisable, per-credential revocation is not |
| B-6 | Group records reachable for verification | **not implemented** — the registry exposes no group surface, by design (`overview.md` §4.4 R4) | PP-41 requires an application-side source |
| B-7 | A second registry issuing passports under its own root | **not present** — `/api/v1/registry/peers` returns an empty array | G7 and PP-84 … PP-88 are untested |
| B-8 | Status observation with a source time | **implemented** — `/api/v1/trust/query` returns `status`, `active`, `level`, `levelName`, `verificationStatus`, `revoked`, `created`, `updated` | PP-67, PP-68 satisfiable |
| B-9 | Revocation listing consistent with record status | **gap** — the registry reports one resource with `status: revoked` while `/api/v1/trust/revocations` returns an empty list | PP-69 and PP-87 cannot be relied on until the two agree; recorded here rather than omitted |
| B-10 | Discovery of registry capabilities | **implemented, and wider than the method specification's example** — `/.well-known/cha2a` advertises nine capabilities and fifteen endpoints, while `did-method-cha2a.md` §5.2 illustrates four capabilities and names `advisory-feed` where the deployment serves `advisory` | a verifier MUST read the discovery document rather than assume the example's contents |
| B-11 | A registered independent verifier | **specified but unexercised** — the evidence layer's credential at Appendix A names `did:cha2a:verifier:dshlib`, while the registry's registered types include no `verifier` | PP-59 cannot be fully checked |

**PP-108.** A deployment claiming conformance MUST publish a table of this shape, dated, and MUST update it when a row changes.

---

*CHASI · CHA2A specification group · Agent Passport · v1.0 · 2026-10-19*
