# Ecosystem Matrix

**A register of external parts: what this family depends on, how deeply, and on what evidence**

> Status: draft (v0.1) | Date: 2026-10-10 | Layer: L7, method
> Position: the **data source** behind Vision §15. §15 gives only "what the object is" and "our relation to it"; this document supplies the evidence columns
> Principle: **a name without its evidence is not an entry**
> Related: `chasi-vision` §5 (complementary) · §10 (the five dispositions) · §15 · `protocol-suite-architecture.md` §6 and §14

---

## 1. What this document settles

Vision §5 says "**complementary** — fill only the gaps the ecosystem leaves in cross-organizational identity, authority, governance, evidence and accountability", and notes "**no criterion yet**: settling it requires being able to list which capabilities are already mature".

**This document is that list.** With it, "complementary" turns from a statement into a decidable requirement: **for each object, this family does only what that object does not cover** — and what it covers is in the adoption-evidence column.

**It is also the data behind the only one of §5's three attitudes that had no criterion.** Compatible's form is in `assembly.md` §3; independent still has none (see §6).

---

## 2. The format

| Column | How to read it |
|---|---|
| **Object** | only the name in general use, not a product name |
| **Version / date** | from the object's own public information; **where none is available it is "—"**, not a word like "unknown" |
| **Strategy** | the **five dispositions** from `protocol-suite-architecture.md` §5: Adopt · Map · Profile-Extend · Adapter · Define. "Study" and "Track" are observation grades for when no disposition is taken |
| **Adoption evidence** | **where in this repository it is cited, and how deeply.** This is the document's main column — the others explain it |
| **Licence** | how the object is licensed. **Where no first-hand source was obtained it reads "unchecked"** |
| **Status** | institutional · individual draft · community project |
| **Review condition** | **not "when to review" but "what condition, once it occurs, requires a review"** — the same form Vision §9 requires of a "record" |

**Why a review *condition* rather than a review *date*:** a date goes stale unnoticed; a condition does not — once it holds, the reader knows for themselves that the entry is out of date.

---

## 3. Table A · what this family's specifications depend on directly

| Object | Version / date | Strategy | Adoption evidence (in this repository) | Licence | Status | Review condition |
|---|---|---|---|---|---|---|
| **DID / VC** | W3C Recommendations; this family's worked example `did:cha2a` v1.1.0 | **Adopt** | the identity binding is the shared premise of every volume: `organization-governance.md` (front matter · §10 · §11), `group-collaboration.md` (§4.5 · §9 · §11), `assembly.md` S1, `naming.md` §2.1. **This family does not invent its own identifiers** | unchecked | institutional | when the identity binding is version-bumped, or the registry entry changes |
| **A2A** | a Linux Foundation project | **Adopt + Map** (with **one redefinition**) | `group-collaboration.md` §2: the task state machine is **aligned to A2A Task**; §8 **redefines** the counterparty's `TASK_STATE_COMPLETED` (the executing side's **self-declaration**) as **pending acceptance**, and separates the counterparty's `REJECTED` from our own "rejection" as **the same name for different things**. `protocol-suite-architecture.md` §3 lists it under Interoperability | **Apache-2.0** (LICENSE in the `a2aproject/A2A` repository, taken first-hand 2026-10-10) | institutional | when the A2A Task model changes |
| **MCP** | Linux Foundation (LF Projects, LLC) | **Adopt** (no redefinition of a tool protocol) | `protocol-suite-architecture.md` §11 states "it does not reimplement MCP's Tool / Resource / Prompt protocol"; §3 lists it under Interoperability | **Apache-2.0** (**transitioning from MIT**; non-specification documentation CC-BY-4.0; per its own licence file, taken first-hand 2026-10-10) | institutional | when the MCP protocol changes |
| **OAuth / OIDC** | IETF | **Undecided** | the only mention in the repository is `protocol-suite-architecture.md` §8, that APS's Adapter Contracts include an OAuth ID-JAG binding. **This family's list of things it does not redefine does not cover authentication / authorization frameworks as a class** — it is absent from §11's eight items | unchecked | institutional | when `protocol-suite-architecture.md` §11 adds that class |
| **RCS** (carrier messaging / federated chat) | GSMA | **Adapter** (an interoperability target, not core) | `group-collaboration.md` §11: RCS is **a "group service component"** — reached through a gateway or adapter, with **the internal model staying agent-native**. `protocol-suite-architecture.md` §3 lists it under Interoperability | unchecked | institutional | when a gateway implementation appears |

---

## 4. Table B · tracked (no specification of this family depends on them; they are positioning and interoperability objects only)

| Object | Version / date | Strategy | Adoption evidence (in this repository) | Licence | Status | Review condition |
|---|---|---|---|---|---|---|
| **OpenA2A** | `did:opena2a` 0.1–0.2 draft; PR #717 merged 2026-07-04 (**two sources disagree**) | Adopt + Map + Adapter | `protocol-suite-architecture.md` §7: its Passport is **composed from the existing artifacts** did:opena2a, AIP, ATX and ATP — on which basis this family **does not re-invent a Passport data format**, and does a federation envelope instead | unchecked | institutional (a multi-specification stack) | when the official site clarifies the version number |
| **APS** | `draft-pidlisnyi-aps-04`, 2026-09-28 | Study + Map + Profile-Extend | `protocol-suite-architecture.md` §8, two points: ① its §11 **Adapter Contracts** are a usable form for this family's interoperability volume; ② **its erratum exposes that "omitting a field bypasses the core invariant" → this family should write "a missing field is a refusal" into the corresponding volume.** §10.2 aligns five further items one by one | an individual draft | **individual draft** (IETF Individual Submission, work in progress) | on `-05`, or on entering a working group |
| **ARIA / TrustLayer / W3C CG** | registry live | Study + Map + Adapter | `protocol-suite-architecture.md` §6 · §14 (positioning only) | CC-BY-4.0 / Apache-2.0 (**self-stated, unchecked**) | institutional (a non-profit foundation plus a W3C CG) | when its specification is finalized |
| **Ant ACT 2.1 / APASS / AMP** | ACT 2.1 released and open; AMP repository opened 2026-08-17 | Study + Map (**not** Adopt) | `protocol-suite-architecture.md` §6 · §14 (positioning only). **Its trust root is operated by one party, unlike this family's "recognition does not change the trust root"** | CC-BY-4.0 / Apache-2.0 (**self-stated, unchecked**) | institutional | when its recognition semantics are published |
| **GB/Z 185-2026 + AIP** | published 2026-06-26 | Track + Map | `protocol-suite-architecture.md` §6 · §14 (positioning only) | unchecked | **a national guiding technical document** — **not a standard**; review is mandatory within three years | the review window, or its conversion into a standard |
| **UnionPay APOP** | published 2026-04-02 | Track | `protocol-suite-architecture.md` §6 · §14 (positioning only) | unchecked | institutional (a licensed hub; invitation-based) | when the open platform drops the invitation requirement |
| **NANDA** | — | **Undecided** | listed by name only in `chasi-vision` §15 | unchecked | a research project | when it takes a definite form |
| **AAIF** | — | **Undecided** | listed by name only in `chasi-vision` §15 | unchecked | **undecided** (it is not even clear whether it is a body or a specification) | when it is clarified whether it is a body or a specification |

---

## 5. Table C · prior art and research institutions (they produce no adoptable specification)

| Object | Version / date | Strategy | Adoption evidence (in this repository) | Licence | Status | Review condition |
|---|---|---|---|---|---|---|
| **Raskar et al.** | `draft-raskar-agentic-web-federated-resolution-01`, 2026-07-20, Individual Draft | **prior art** (neither adopted nor mapped) | `group-collaboration.md` §9.4 records it item by item: **the two rules it shares** with that volume, **the three premises that differ**, and which volume of this family answers each of the three open questions in its Appendix C | an individual draft | **individual draft** | on `-02` |
| **MIT Media Lab** | *A Global Switchboard for the Agentic Web*, v0.1, 2026-07-20, Request for Comments | **prior art** | `group-collaboration.md` §9.4: that preprint proposes the directory-of-directories model; the draft above cites it as background and states that it is outside that revision's protocol scope | unchecked | a research institution | on a later version |
| **Stanford** | — | **Undecided** | listed by name only in `chasi-vision` §15 | unchecked | a research institution | when it takes a definite form |

---

## 6. Known gaps

**This document can now support the judgement of "complementary", with three qualifications.**

1. **Only 2 of the 16 licence entries were taken first-hand** (A2A and MCP, from each repository's LICENSE on 2026-10-10); **12 read "unchecked"** (2 of them "self-stated, unchecked") and **2 are individual drafts, marked "individual draft"** — **and "unchecked" is not an omission; it means the entry itself is still incomplete.** Closing it requires obtaining a first-hand licence file for each.
2. **Two statuses are undecided**: AAIF (it is not even clear whether it is a body or a specification) and NANDA (which has taken no definite form). **Those two are names only, and do not yet constitute entries.**
3. **One source disagreement**: OpenA2A's `did:opena2a` version number (0.1 and 0.2 are both stated).

**One further point**: this family **itself** (the CHA2A protocol suite · CHASI) does not appear in this table — it is not "the existing ecosystem". The relation between the two is in `chasi-vision` §14.

---

## 7. What this document does not do

- it draws **no licence-compliance conclusion** — it records *what the licence is*; **judging whether a given use is permitted is separate work**;
- it does not prescribe "the relation" for `chasi-vision` §15 — that column stays in §15, and this document supplies only the evidence;
- it carries **no internal strategy judgements** — "must be tracked", "closest to us", "unavoidable" belong to internal material, not to this table;
- it does not register **this family's own parts** — those are in the layer index (README).

—— Ecosystem Matrix · v0.1
