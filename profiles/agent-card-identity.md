# Agent Card Identity Extension Profile

> Status: draft (v0.2) | Date: 2026-11-01 | Layer: **L4 · profile**
>
> This profile adopts the A2A Agent Card as the capability-discovery object and
> adds only an identity reference. It does not redefine A2A.

## 1. Scope

An Agent Card answers:

- what the agent is called;
- what interfaces and capabilities it exposes;
- which skills it offers;
- how a client authenticates and invokes it.

An Agent Card does not establish accountability, authority, or current trust
state. Those remain with the Passport, DID Document and Registry.

## 2. Reused objects

This profile uses:

- `/.well-known/agent-card.json`;
- A2A Agent Card fields and `capabilities.extensions[]`;
- DID resolution for `agent_did`;
- CHA2A Passport for authority and accountability;
- a Registry observation for current status and revocation.

## 3. CHA2A extension

The provisional extension identifier is:

```text
urn:cha2a:ext:agent-identity:v1
```

The identifier remains provisional for v0.2. A final HTTP URI must not be
published until its namespace and resolution policy are stable.

The extension carries references, not a second credential:

```json
{
  "uri": "urn:cha2a:ext:agent-identity:v1",
  "required": true,
  "params": {
    "agent_did": "did:cha2a:agent:example",
    "passport": {
      "uri": "https://agent.example/passports/example",
      "digest": "sha256:...",
      "media_type": "application/vnd.cha2a.passport+json",
      "profile": "cha2a-passport-v1.2"
    },
    "registry_did": "did:cha2a:registry:example"
  }
}
```

Required members:

| Member | Requirement |
|---|---|
| `agent_did` | DID; must equal the verified Passport subject |
| `registry_did` | DID of the Registry the verifier should consult |

Optional Passport reference:

| Member | Requirement |
|---|---|
| `uri` | absolute HTTP(S) URI |
| `digest` | REQUIRED when the Passport object is present; `sha256:` digest of the fetched artifact |
| `media_type` | media type of the Passport representation |
| `profile` | Passport object/profile version |

## 4. Authority boundary

- `agent_did` is a claim until DID resolution and signature verification pass.
- The Card MUST NOT assert `trust_level`, `revoked`, admission status, or a
  conclusive trust rating.
- The extension MUST NOT replace the Passport issuer, authority scope,
  governance domain, delegation chain, or Registry status.
- A Card MAY reference a Passport. It MUST NOT make an unsigned Passport
  authoritative by embedding it.

## 5. Discovery and hosting

The preferred canonical location is the agent origin:

```text
https://agent.example/.well-known/agent-card.json
```

A Registry-hosted Card is allowed as an indexed or fallback representation.
It MUST identify the Registry-hosted source. The hosted representation MUST
preserve the original Card bytes and signatures, or explicitly state that the
copy is not signature-verifiable. A hosted copy does not become a new
authority and MUST NOT be confused with the agent-origin Card.

## 6. Verification sequence

1. Fetch the Agent Card.
2. Verify the Card signature if one is present. A verifier policy may require
   a signature and reject an unsigned Card.
3. Extract `agent_did` and `registry_did`.
4. Resolve `agent_did`.
5. Fetch the referenced Passport and enforce its required `digest`.
6. Verify the Passport subject, issuer, authority and validity.
7. Query Registry status and revocation.
8. Apply the verifier's own admission policy.

Card discovery is not trust. Being listed in a Registry is not trust. A
successful Passport verification is not admission.

## 7. A2A compatibility

- Use A2A snake_case fields for public cards.
- Do not publish the CHA2A extension as required unless the agent is prepared
  to support the complete verification sequence.
- Keep private/catalog projections separate from the canonical well-known card.
- Existing camelCase catalog projections require adapters; they do not define
  the public Card format.

### 7.1 Signature profile

When a public Card carries `signatures[]`, the profile uses A2A detached JWS:

- each signature has `protected` and `signature`;
- the protected header is base64url-encoded JSON;
- `alg` is `EdDSA`;
- `kid` selects the verification key;
- the detached payload is
  `BASE64URL(protected) + "." + BASE64URL(JCS(card without signatures))`.

A verifier MUST reject a malformed signature, an unresolved `kid`, or a
signature that does not verify. Presence of a signature establishes the signing
key, not the truth of capability claims.

By default, `kid` resolves to the subject DID Document verification method
`#agent-key`. A Registry-controlled `#registry-key` MUST NOT count as proof
that the subject signed the Card unless the verifier policy explicitly allows
that key.

## 8. Conformance

Minimum conformance requires:

1. valid A2A Card structure;
2. one CHA2A identity extension;
3. `agent_did` and `registry_did` present and syntactically valid;
4. Passport reference, if present, has an absolute URI and SHA-256 digest;
5. no embedded dynamic trust level or revocation claim;
6. verification sequence executes without treating Card presence as trust.
7. any present Card signature verifies under the selected `kid`.
8. a verifier that requires signatures rejects an unsigned Card;
9. `#registry-key` is rejected under the default subject-held key policy.

## 9. v0.2 decisions

- the extension remains the provisional URN above;
- public discovery signatures remain verifier-policy controlled;
- Passport and Card need not share an origin;
- Registry-hosted fallback is a byte-preserving cache, not a new authority;
- IANA media-type registration and a final namespace URI are deferred.
