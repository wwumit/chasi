# Assembly Profile — the Composition Volume

> Status: draft (v0.1)
> Date: 2026-10-10
> Position: this family's **first profile**, and the only document that specifies **how to use other people's parts**
> Principle: **if an existing standard can be used, do not invent one** — this document defines no primitive; it specifies only what each of four slots may hold, and what an assembly must then satisfy
> Related: `overview.md` §1 (the four conditions) · `question.md` (how an assembly is judged) · `naming.md` (how the objects in a slot are referred to) · `protocol-suite-architecture.md` §0 and §5 (the core claim, and the five dispositions)

---

## 1. The problem, and the approach

**The problem**: most of this family's parts are not its own — identity comes from some binding, record format from an existing standard, rules from each party itself. **"You may use other people's parts" had no decidable form**: how far an assembly has to go to count as assembled, whether a missing part means it cannot be assembled at all, and what makes an assembly hold once assembled, were all unspecified.

**The approach**: make **assembly** a first-class object. Four slots are fixed, and each slot specifies **what it may hold and what interface it must satisfy**; whether an assembly holds is judged by the four questions in `question.md`.

**This document defines no primitive.** It specifies: **whose parts you may use, and what must then hold.** Anyone who does not adopt these slots is not bound by it.

**This is a profile, not a specification.** It sits above L2 and L3 and **adds no requirement to any volume**; it specifies the conditions of one thing only — assembling according to this profile.

---

## 2. The core claim, and the four slots it yields

The suite architecture's §0 gives this family's core claim:

> **Recognition does not change the trust root; evidence does not depend on an operator.**

Expanded: in any cross-trust-domain collaboration, the **authority and the evidence** must be independently verifiable by a third party belonging to no party. The family entry, `overview.md` §1, expands that into four conditions, each carried by one volume — **and those four conditions are the four slots**:

| Slot | What it holds | What it answers | Carried by |
|---|---|---|---|
| **S1 Identifier** | a resolvable identifier for the subject | Q1 who it is | `did-method-cha2a.md` (the worked example) |
| **S2 Authority chain** | the derivation of authority and scope | Q2 who authorized it | `organization-governance.md` |
| **S3 Rule version** | **the verifiable part of the context**: the rule in force at the time | Q3 in what context it is acting | `group-collaboration.md` |
| **S4 Record** | the evidence the action left, and the end of responsibility | Q4 what it has done | `evidence-record.md` |

**Slot three holds "the context"; this document names it after the part of that context which is verifiable.** The context also includes roles and groups (see `question.md` Q3); what this document requires is that **something in the context be verifiable, namely the rule in force at the time** — otherwise Q3 cannot be judged.

---

## 3. What each slot may hold

**"May hold" is expressed in the five dispositions** (suite architecture §5): Adopt → Map → Profile-Extend → Adapter → Define. **Ask in order; only when all four answers are no may we define our own.** Wherever anything lands on Define, it must state which half of the core claim it serves.

| Slot | The interface it must satisfy | Dispositions allowed |
|---|---|---|
| **S1 Identifier** | ① resolvable by a resolver **belonging to no party**; ② the **anchor used is configured by the verifier itself**; ③ for cross-domain use, the binding's cross-domain form | Adopt (an existing DID method) · Map (external identifier → binding identifier) · **may not Define a new identifier scheme** |
| **S2 Authority chain** | ① each basis traces back to its origin; ② each link states its **scope** (what may be done, and explicitly what may not); ③ revocation status is readable | Adopt (an existing governance model) · Map · Profile-Extend (role differences) · **may not Define** |
| **S3 Rule version** | ① each version carries a **hash** and an **effective time**; ② amendments **append**, never rewrite; ③ a reference points at **the version in force when it was made** | Adopt (an existing versioning mechanism) · Profile-Extend |
| **S4 Record** | ① **content-addressed**; ② independently checkable by a third party; ③ the end of responsibility lands on **a person or a legal entity** | Adopt (`evidence-record.md`'s existing format) · Map |

**The three "may not Define" entries are direct consequences of the core claim.**

- inventing a new identifier scheme → Q1's anchor falls back into some party's hands → violates "**recognition does not change the trust root**";
- inventing a new authority model → Q2's basis returns to this family itself → violates the same half;
- inventing a new record format → Q4's checking depends on this family's systems → violates "**evidence does not depend on an operator**".

**This is exactly why the suite architecture's §10.1 keeps only four original items**: what this family genuinely needs to define is composition rules and cross-domain semantics, not primitives.

---

## 4. How an assembly is judged

An assembly holds not when "all four slots are filled" but when **all four verdicts in `question.md` §3 are "answered"**.

| Assembly | The four questions | Verdict |
|---|---|---|
| each of the four slots holds a compliant part per §3 | Q1–Q4 | all answered → the assembly holds |
| any slot is empty | the corresponding question | not answered |
| a slot holds a part that does not satisfy §3's interface | the corresponding question | partially answered, and it must say **which item is missing and with whom** |

**"Partially answered" must say which slot it falls short in.** The division of labour: **this document specifies the slots and interfaces; `question.md` specifies the judgment format.**

**An assembly holding is not the family being sufficient.** The verdicts above concern **one assembly**. At the family level there is a stronger criterion:

> **Agents of two organizations that do not belong to each other complete one task with verifiable evidence, without using any specification from outside this family along the way.**

**If that cannot be met, the family is missing a volume** — and which volume, by working back from "what did we have to go outside for". This criterion is also the family's **adoption** criterion: **a system can be built from this family, and nothing outside it is needed along the way.**

**Its relation to A8**: A8 judges that **one assembly** contains no Define; this judges that **building a working system** contains no outside dependency at any point. The first is necessary but not sufficient for the second.

---

## 5. Assembly vectors

**A vector is a record of "an assembly plus the expected verdict".** It has the same shape as the 68 conformance vectors in `cha2a-conformance` — **those judge a single part; the vectors here judge an assembly.**

| # | Assembly | Expected verdict | Which requirement it tests |
|---|---|---|---|
| **A1** | each of the four slots holds one compliant part (S1 uses the worked binding) | Q1–Q4 **all answered** | the minimal usable assembly |
| **A2** | S1 replaced by a self-invented identifier scheme | Q1 **not answered** | §3 S1, "may not Define a new identifier scheme" |
| **A3** | S1's resolution anchor is supplied by the party being verified | Q1 **partially answered** (the anchor is not portable) | §2 core claim, "does not change the trust root" |
| **A4** | S2 has a declaration that "there was authority", with no scope | Q2 **partially answered** (scope missing) | §3 S2, interface requirement ② |
| **A5** | S3's rule is rewritten in place, version unchanged | Q3 **not answered** | §3 S3, interface requirements ②③; `naming.md` §3, requirement 2 |
| **A6** | S4 stores only a uri, no hash | Q4 **partially answered** (content unobtainable, so it cannot be checked) | `naming.md` §3, requirements 1 and 3 |
| **A7** | S4's evidence is complete, but the end of responsibility is written as "the system" | Q4 **partially answered** (the end is not a person or legal entity) | §3 S4, interface requirement ③ |
| **A8** | S1–S4 are **all** connected through **Map**, with no Define anywhere | Q1–Q4 **all answered** | see below |

**A8 is the most important one in this set.** It tests whether "this family can do composition only, and invent nothing". **If A8 comes out partially answered, the core claim does not land** — because it requires that both recognition and checking hold without inventing any primitive.

**Undecided: whether the vectors are executable.** What this section gives today is a **verdict table**, with no executable implementation. `cha2a-conformance` is the executable precedent (68 vectors, dual-verifier interlock); to make these executable in the same way, the **machine-readable form of each slot's part interface** has to be decided first.

---

## 6. What this document does not do

- it defines **no primitive** — the format of identifier, authority, rule and record belongs to their own volumes;
- it does not define the **judgment format** — that is the subject of `question.md`;
- it does not require **anyone to use this profile** — those who do not are not bound (Vision §5, "conditions, not obligations");
- it makes no **conformance judgement** — the vectors here judge an assembly, not compliance (Vision §11, capabilities 6, 7 and 8).

—— Assembly Profile · v0.1
