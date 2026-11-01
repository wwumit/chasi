# Compliance Profile

> Status: draft (v0.1) | Date: 2026-10-19 | Layer: **L4 · profile** — laid over the layers below; adds no requirement to any volume
> Position: declares **what must hold**, by industry and by risk band, for the four slots of `assembly.md`
> Principle: a profile declares conditions; it does not judge who meets them (Vision §11 capability 7). The verdict belongs to the verifier (`question.md`).
> Related: `assembly.md` (four slots) · `../specs/naming.md` §2.2 (rule version) · `../specs/question.md` (judgment) · `../specs/organization-governance.md` · `../specs/group-collaboration.md` (admission)

---

## 1. Problem and approach

**Problem.** Compliance requirements tend to be applied uniformly: one set of demands for every industry and every risk band. Applied uniformly, they are either too heavy — small deployments cannot meet them — or too light, so high-risk cases pass.

**Approach.** Make the **compliance profile** a first-class object: a **versioned declaration** stating, per industry and per risk band, how far each of the four slots must be satisfied. The profile itself judges nobody.

---

## 2. What the Profile Specifies

- **A profile is a rule version** — it carries a hash and an `effective_from`, and amendments append (`naming.md` §2.2).
- **A profile only declares.** It states what must hold; it never states who has met it.
- **A profile can be cited.** A passport, an admission record or a check report points at *the version in force when it was made*.
- **A profile introduces no primitive.** It constrains the four slots of `assembly.md`; it defines no identifier, no authority model and no record format.

---

## 3. The object

| Field | Type | Required | Meaning |
|---|---|---|---|
| `profileId` | string | ✔ | stable identifier |
| `profileVersion` | `{hash, effective_from, uri?}` | ✔ | the rule version (`naming.md` §2.2) |
| `industry` | string[] | ✔ | industry labels; `*` means cross-industry |
| `riskBand` | enum | ✔ | risk band; this profile fixes the semantics, the deployment fixes the values |
| `slots` | object | ✔ | constraints for S1–S4 |
| `disclosure` | object | ✔ | what may be obtained, and by whom |
| `review` | object | ✔ | **review conditions**, not a review date |
| `status` | enum | ✔ | `draft` · `active` · `withdrawn` |

**Sufficiency criterion**: a party belonging to no side can, from the object alone, tell which four-slot conditions apply to a given industry and risk band, and find the version in force at a stated time.

---

## 4. What a profile may constrain, per slot

| Slot | A profile may require | A profile may not require |
|---|---|---|
| **S1 identifier** | resolution independent of the verified party being online; a portable trust root | a specific DID method |
| **S2 authority chain** | traceability to the origin; scope comparable with the action | how an organisation governs itself internally |
| **S3 rule version** | the version in force at the time of the action as the basis | a particular regulation database or vendor |
| **S4 record** | third-party recomputation; the end of responsibility on a person or a legal entity | retention of everything |

**Nothing in this table may weaken condition ① (verifiability).** A lower risk band may require less, but it may not require less than the four questions being answerable.

---

## 5. Risk bands

This profile fixes no numeric scale. It fixes three things:

1. **The band is a property of the scenario, not of the subject.** It is not the same axis as L0–L4, which describe how much has been attested about a subject.
2. **Whoever declares the band must state its basis.** A band without a stated basis is a label, not a declaration.
3. **Different bands may require different evidence sets**, but a lower band never lowers ①.

---

## 6. Relation to admission and judgment

Admission uses the profile: the receiving domain checks the materials against the profile it declared, then decides. **The decision stays with the receiving domain** (`overview.md` §4.4 R3; `group-collaboration.md` §4.3).

A profile is not an entry threshold. It is chosen by a verifier or a receiving domain; the family imposes no single profile on everyone.

---

## 7. What this document fixes, and what it leaves to the deployment

| Fixed here | Left to the deployment |
|---|---|
| the object's fields and their requiredness | the industry taxonomy |
| the rule-version form (hash + `effective_from`) | the values of the risk bands |
| what each slot may and may not require | which profile each domain adopts |
| the rule that a lower band never lowers ① | the disclosure sets for each band |

---

## 8. Undecided

| Item | Precondition |
|---|---|
| the numeric risk scale and its mapping | a mapping used by two independent deployments |
| precedence when several profiles apply to one subject | a precedence rule — partially in `../specs/group-collaboration.md` §8 |
| where profiles are published for discovery | who maintains the list |

---

## 9. What this document does not do

- it does not judge who meets a profile;
- it does not fix a numeric risk scale;
- it does not define a policy language;
- it does not name a regulation database or a product;
- it does not replace the admission rules of `organization-governance.md` or `group-collaboration.md`.

---

This profile is laid over the layers below and adds no requirement to any volume; when a deployment chooses to use it, it constrains the four slots.
