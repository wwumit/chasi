# Question and Answer — the Judgment Volume

> Status: draft (v0.2)
> Date: 2026-10-19
> Position: this family's volume on **judgment** — what counts as a verifier belonging to no party having answered the four questions
> Principle: **if an existing standard can be used, do not invent one** — judgment reuses the existing verifiable data structures rather than defining a new wrapper
> Related: `overview.md` §1 (the normative statement of the four questions, the family entry) · `organization-governance.md` (when authority holds) · `group-collaboration.md` (how a context is made verifiable) · `evidence-record.md` (record format)

---

## 1. The problem, and the approach

**The problem**: this family's core claim is that "a verifier belonging to no party can answer four questions independently". But **"can answer" has no judgment format** — what an answer must look like to count as given, who decides, and what is left behind when it cannot be answered, were all unspecified. Without this layer the core claim cannot be tested.

**The approach**: make **judgment** a first-class object. This volume gives the judgment format for the four questions: what each answer must contain, what counts as answered / not answered / partially answered, **who judges**, and which class of record the judgment goes into.

**What this volume is responsible for**:

1. fixing the normative statement of the four questions and where it comes from;
2. giving the **judgment format** for each question (the fields its answer must contain, and the boundaries between the three verdicts);
3. fixing **who judges** — the verifier, not this family;
4. fixing where a judgment is recorded;
5. **citing rather than restating**: identity (`did-method-cha2a.md`), authority (`organization-governance.md`), context (`group-collaboration.md`), records (`evidence-record.md`).

---

## 2. The four questions

The normative statement of the four questions is in the family entry, `overview.md` §1. **This volume does not rewrite it, only cites and summarizes it:**

| # | Question | What it asks |
|---|---|---|
| **Q1** | **who it is** | whether the subject has a resolvable identifier |
| **Q2** | **who authorized it** | what power its present action rests on, and how far that reaches |
| **Q3** | **in what context it is acting** | which rule was in force at the time; which role or group it is acting in |
| **Q4** | **what it has done** | the evidence the action left, and the end of responsibility |

**What the four questions do not cover is not part of this family.** `overview.md` §4 says where the rest goes.

---

## 3. The judgment format

**There are three verdicts and no more: answered, not answered, partially answered.** "Partially answered" is not a degree of "answered" but a separate verdict — **and it must be able to say which item is missing**.

| Question | Its answer must contain | The criterion for "answered" | The usual "partially answered" |
|---|---|---|---|
| **Q1** | a resolvable identifier; **a portable trust root** — not established by the party being asked about | the identifier resolves, and it resolves against **the anchor the verifier configured itself** | the identifier resolves, but only by asking the subject itself; or the anchor is held by the party being asked about |
| **Q2** | the basis of authority; **the scope** (what may be done, and explicitly what may not); time and validity | the basis traces back to its origin along the authority chain, and **the scope can be compared against the action** | only a declaration that "there was authority", with no scope; or a scope that cannot be compared against the action |
| **Q3** | **the rule in force at the time** | the record can produce the version of the rule that was in force when the action happened | only the version in force now; or a rule with no version |
| **Q4** | evidence; **the end of responsibility** (a person or a legal entity) | the evidence can be checked by a third party; the end is a subject capable of bearing responsibility | evidence exists but the end is written as "the system"; or the evidence is held by one party alone |

**"Partially answered" must be pointable.** A judgment has to state **which item is missing and with whom** — saying "not satisfied" is not a judgment.

**"Not answered" and "partially answered" differ in how much is missing.** The first means the basis for that item cannot be obtained at all; the second means it was obtained but cannot support a judgment. Both leave a record (see §5).

**Sufficiency criterion**: a verifier belonging to no party can, from the table in §3 alone, return one of "answered / not answered / partially answered" for any answer, and state which item is missing and with whom — with no need to ask this family. That is the point to stop; do not extend.

---

## 4. Who judges

**The verifier judges, not this family.** This follows from `overview.md` §1's "without being anyone's customer", and from Vision §7 "facts, not ratings" and §11's capabilities 6, 7 and 8: this family makes no compliance judgement, gives no ratings and sets no entry threshold.

So what this volume specifies is the **judgment format**, not the **judgment**. Two verifiers reaching different verdicts on the same answer is permitted — **the disagreement itself should be recorded**, rather than settled by one of the parties.

**Undecided: what to do when verifiers disagree.** Vision §13 hands adjudication to a "dispute process", and the family nowhere says who provides it.

---

## 5. Where a judgment is recorded

A judgment is not a fourth class of record. Under Vision §9's division of the three classes, judgments go in two places:

| Verdict | Which class of record | Why |
|---|---|---|
| **answered** | the accountability chain (Vision §12) | it is precisely that action's derivation of authority having been checked and passed |
| **not answered / partially answered** | the experiment record (Vision §9) plus the record of the party judged | it is a **finding** — "this cannot be answered here" is exactly what this family publishes (Vision §9, "a conclusion that does not hold must be published too") |

**Undecided: the shelf life of a judgment.** Whether an "answered" still stands after the authority is revoked depends on Vision §12's revocation cascade and Vision §13's retention periods; **both are undecided**.

---

## 6. What this volume does not do

- it does not define the **format** of identity, authority, context or evidence — those are the subjects of the four volumes;
- it does not produce a **verdict** — that is the verifier's business;
- it does not define a **dispute process** between verifiers — there is no provider yet (see §4);
- it does not say **who must accept a judgment** — this family has no such power (Vision §6).

—— Question and Answer · v0.2
