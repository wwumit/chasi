# Naming, Reference and Versioning — the Addressing Volume

> Status: draft (v0.4)
> Date: 2026-10-19
> Position: this family's volume on **how objects are referred to** — where the names of the four classes come from, how versions are marked, and why a reference must be independently checkable
> Principle: **if an existing standard can be used, do not invent one** — organizations and groups cite an identity binding rather than inventing one; everything else is content-addressed
> Related: `organization-governance.md` (versioning of charters and rules) · `evidence-record.md` (content identity for records) · `did-method-cha2a.md` (the worked identity binding)

---

## 1. One general rule

> **The hash is the check basis; names, uris, repository names and version numbers are all just locators.**

This rule is already fixed in `organization-governance.md` §4① — in `charter_ref`, the `hash` is the check basis and the `uri` is only a locator. This volume **generalizes it to the three of the four classes that need content addressing** (rule version, commitment, record). The fourth (organization · group) does not apply: their names come from the identity binding, not from content addressing.

**Two things follow:**

- **a locator may change; the check basis may not.** Changing a domain, a repository name or a file path does not change *which* thing this is;
- **a reference that gives only a locator is not acceptable.** A reference with a uri and no hash cannot prove that "the thing then had this content".

---

## 2. The four classes

| Class | What it is | Where the name comes from |
|---|---|---|
| **Organization · group** | social subjects such as Organization and Group | **cites an identity binding** (worked example `did:cha2a`), **does not invent one** |
| **Rule version** | charters, policies, group rules — anything **with an effective time** | **content-addressed** (hash) plus `effective_from` |
| **Commitment** | something one party commits to another, referable by others | **content-addressed** (hash) |
| **Record** | evidence and facts that have been checked | **content-addressed** (hash); the content stays off-chain |

**These four are classes of objects, not the four slots of an assembly.** For the relation — which class supplies which slot — see `assembly.md` §2.1.

### 2.1 Organization · group

**Rule**: the identifier comes from the **identity binding**, not from this family. Where cross-domain addressing is needed, use the binding's cross-domain form (`org_did` in `organization-governance.md`).

- **Positive example**: `did:cha2a:org:<id>` — the binding's cross-domain form; the counterparty resolves it against **a resolver it configured itself**.
- **Counter-example**: inventing an `org://acme` scheme. It works inside its own domain, but **a counterparty across domains does not recognize it**, and so Q1 (who it is) cannot be answered.

**Non-subject resources (services · tools · resources · data) take the same path.** Vision §1 requires them to have **names that can be referenced** and **not to be mistaken for subjects** — this family invents no naming scheme for them; it uses the binding's existing **resource types** (in the worked example, `skill` · `mcp_server` · `ai_tool` · `llm` · `package` and so on), distinguished from subjects by a **type label**.

### 2.2 Rule version

**Rule**: each version carries a **hash** (the check basis), an **`effective_from`** (when it takes effect) and an optional **uri** (a locator only). **An amendment appends a version; it never rewrites an existing entry.**

- **Positive example**: `{hash: "sha256:…", uri: "https://a.example/charter/3", effective_from: "2026-09-01"}`. Older appointments remain valid — their basis is **the version in force when they were made**.
- **Counter-example**: rewriting a charter in place without changing the version. That makes "which rule was in force at the time" (Q3) **permanently unanswerable**.

### 2.3 Commitment

**Rule**: content-addressed. Once published, a reference to a commitment points at **that content**, not at "the current state of the commitment".

- **Positive example**: the hash of the commitment's content, plus the identifiers of the promiser and the promisee.
- **Counter-example**: referring to "commitment number 3". Sequence numbers get renumbered by later records, so the same reference points at different content at different times.

**Undecided: the commitment object model.** Vision §13 has Commitment Memory (who committed to what; the promiser writes, the promisee reads), but **the family has no object definition for a commitment** — its fields, when it takes effect, revocation and fulfilment state are all unspecified. This volume can only fix how it is addressed.

### 2.4 Record

**Rule**: **content-addressed, with the content off-chain.** A record is anchored by hash so that tampering can be detected; the content itself stays with its rights-holder, produced on demand, by permission, with minimal disclosure (Vision §13, "anchoring rather than on-chaining").

- **Positive example**: `artifactDigest` (`evidence-record.md`'s content-identity, sha512) — even if the URL stops working, the hash still proves that "the evidence then existed and had this content".
- **Counter-example**: storing only a uri. Change the host and **there is no way to prove it is the same thing you got**.

---

## 3. Three hard requirements on a reference

1. **A reference must carry the check basis.** Any reference to a rule version, a commitment or a record carries a hash (or its equivalent);
2. **A reference to a rule version must point at "the version in force when it was made".** "Latest version" may not be substituted; a commitment or a record has no version, and its reference points at **that one piece of content**;
3. **A locator failing must not affect verification.** Not being able to obtain the content is one thing; **not being able to prove it is the same content** is another — the second rests on the hash alone.

**All three are checkable**: take a reference; if swapping its uri leaves it unable to say what it refers to, requirement 1 fails; if it is **a reference to a rule version** and drifts with "the latest version", requirement 2 fails; if not obtaining the content means it can neither be checked nor reported, requirement 3 fails.

**Sufficiency criterion**: a verifier belonging to no party can, from the naming rules for the four classes and the three requirements above, decide whether any given reference is usable for third-party checking — without knowing any party's implementation. That is the point to stop; do not extend.

---

## 4. What this volume does not do

- it does not define the **identity binding** — that is the subject of `did-method-cha2a.md`;
- it does not define **hash algorithms or record format** — that is the subject of `evidence-record.md`;
- it does not define the **commitment object model** (see §2.3, undecided);
- it does not do **name registration** — this family runs no registry (Vision §6); name resolution is carried by each party's identity binding.

—— Naming, Reference and Versioning · v0.4
