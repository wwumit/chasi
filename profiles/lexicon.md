# Lexicon — the Terminology Volume

> Status: draft (v0.1)
> Date: 2026-10-10
> Position: the **single source for this family's terminology**. Where any document conflicts with it, this volume governs
> Principle: **one concept, one word** — the same thing written two ways in two places means it may be judged twice
> Related: all volumes

---

## 1. How to use this volume

Three columns:

| Column | Meaning |
|---|---|
| **Preferred** | the only form this family uses |
| **Forbidden** | words that **may not be used for this concept** |
| **Why** | one line on what the distinction rests on |

**Only terms at risk of divergence are listed.** A word that already has one meaning and one form across the family does not go in — otherwise this volume swells into a dictionary.

**"Forbidden" does not mean the word may not be used**; it means it may not be used for *this* concept. "Assertion", for instance, is a usable word — it may not be used for "declaration".

**This volume contains no definitions.** Definitions live in the volumes; this one fixes only **which word is written**.

---

## 2. Conflicts found in practice, and how they were settled

The four below were **measured**, not imagined; this volume **also fixed the non-preferred side** in each case:

| # | Conflict | Settled as |
|---|---|---|
| 1 | `集体` in `naming.md` vs `群体` in Vision §1 | **群体**. The Vision is L1 and §1 already defines it; `naming.md` was corrected |
| 2 | `验证者` in `naming.md` (of a hash) vs `验证方` (everywhere, the party that judges) | **They were never the same concept**: `验证方` is a party; a hash is not a party, it is the **check basis**. `naming.md` was corrected |
| 3 | `凭据` in Vision §4 vs `凭证` in `organization-governance.md` | **凭证** |
| 4 | `构件` in `protocol-suite-architecture.md` §9 vs `件` across the family (185 uses) | **件** |

---

## 3. The lexicon

| Preferred | Forbidden | Why |
|---|---|---|
| **主体** (subject) | `Agent` used as the general term | §1 distinguishes four kinds of subject: person, organization, agent, group. Using `Agent` as the general term leaves organizations and groups outside |
| **agent** | `Agent` as a kind of member | **Proper names keep the capital** (`Agent Society` · `Agent Internet` · `Agent Runtime`); as a kind of member it is lower-case |
| **群体** (group) | `集体` | one of the member kinds (a family or a community is its smallest form). `Group` is the name of **the collaboration-domain object** (see `group-collaboration.md`), not of a member kind |
| **组织** (organization) | `Organization` in Chinese prose | Chinese prose writes 组织; field names and proper names use `Organization` |
| **验证方** (verifier) | `验证者` | **the party that reaches the verdict**, the same party as "the verifier judges" in `question.md` §4 |
| **校验依据** (check basis) | `验证者` when referring to a hash | a hash is **the thing you check against**, not a party. See `naming.md` §1 |
| **凭证** (credential) | `凭据` · `证书` | identity and authority credentials. `证书` refers specifically to the X.509 form and is not used generically |
| **件** (part) | `构件` · `组件` | this family's own term ("whose parts you may use, and what must then hold", see `assembly.md`). `artifact` is kept in English only where it is an existing object's name |
| **记录** (record) | (none; must be qualified) | it has **three senses**: ① experiment record (the finding of one experiment, Vision §9) ② accountability-chain record (the derivation of authority for one action, Vision §12) ③ societal memory (six classes, Vision §13). **"Record" alone must mean one of them** |
| **判定** (judgment) | `评级` (rating) · `认证` (certification) | this family **gives a judgment format only; it issues no ratings and no certifications** (Vision §11, capabilities 6/7/8). The three are not synonyms; conflating them reads this family as a regulator |
| **名录** (directory) | `注册表` (registry) | **a directory holds declarations; a registry settles facts** (Vision §6). This family holds a directory, not a registry |
| **注册表** (registry) | `名录` (directory) | as above — what the party that carries a subject's status and answers for it operates |
| **合规** (compliance) | (none; must point back to verifiability) | this family makes no compliance judgement. Vision §5 defines Compliance in the name as **the conditions required for verifiability to hold** (§3①) |
| **可核验** (verifiable) | `合规` used as a synonym | the name of the condition in §3① |
| **槽** (slot) | `位` · `插槽` | S1–S4 in `assembly.md` |
| **剖面** (profile) | `profile` in Chinese prose | the name of layer L4: a constraint laid over the layers below |
| **够用判据** (sufficiency criterion) | `完成判据` | each layer and volume states "what condition makes it complete, so that it stops there" (`protocol-suite-architecture.md` §4) |
| **授权依据** (basis of authority) | `权威依据` | **the two are not synonyms and may not be swapped**: `授权依据` is a field on **each link** of the accountability chain (one of Vision §12's seven); `根权威依据` is the **fourth layer** of the L3 four-layer decomposition. The former must be traceable to its origin along the latter |
| **根权威依据** (root authority basis) | `授权依据` | as above |
| **声明** (declaration) | `断言` (assertion) · `自证` used interchangeably | `声明` is made by a party and **can be checked**; `自证` is made about oneself (the form `assembly.md` requires, with the verifier deciding whether it holds); `断言` is a claim with nothing to check against, and is what this family exists to remove (Vision §12, "a declaration taken for a proof") |
| **承诺** (commitment) | `承诺书` | one of `naming.md`'s four object classes; **its object model is undecided**, and this volume fixes only how it is addressed |
| **规则版本** (rule version) | `政策版本` | one of `naming.md`'s four classes; a policy is one kind of rule |
| **第三方** (third party) | — | not the same as `验证方`: `第三方` stresses **belonging to no party** (the wording of §3①); `验证方` stresses **reaching the verdict**. One subject can be both |

---

## 4. What this volume does not do

- it defines no concept — definitions live in the volumes;
- it does not list terms with no risk of divergence;
- it does no **automatic substitution** of synonyms — every conflict it lists has been fixed in place (§2);
- it does not fix **English** usage, except the few points noted here (proper names capital, `agent` lower-case); English has its own conventions in each volume.

—— Lexicon · v0.1
