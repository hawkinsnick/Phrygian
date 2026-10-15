# Attribution review

All four controls include the Anfosso general-formula/object-fragment mismatch and Güney–Yanık’s short edition versus conditional longer restoration.

Existing source consultation receipts and limits are inherited exactly from the referenced native packets. This pass inspects those packets, not the underlying publications afresh. No exhaustive literature search, new autopsy or independent review is claimed.

The complete selections below name the finite native collections reviewed. Other repository records and the broader literature are outside this checkpoint. Case counts are review tasks, not inscriptions, independent witnesses or fully attributed alternative pairs.

| Complete native selection | Rows |
|---|---:|
| `research/disagreement-register.json/items` | 4 |

Use the case query to read the finding together with the complete native evidence, including any named author/publication, source locator, inspection state, qualification and source dependence. Missing metadata stays missing; a source ID alone is not proof of direct consultation.

```sh
python scripts/attribution_review.py --check
python scripts/attribution_review.py --case 'PHR-DIS-001'
python scripts/evidence_query.py --list attribution-review
```

| Review ID | Type | Finding | Remaining work |
|---|---|---|---|
| PHR-DIS-001 | SOURCE_ROLE | UD 34.2 matches a general formula, not the shorter object fragment on Anfosso p.113; no object reading correction is admitted. | TM identity and the intended UD assignment remain unverified. |
| PHR-DIS-002 | READING_COMPARISON | Güney–Yanık catalogue2 p.165 gives a short edition; p.166 n.29 discusses a conditional longer restoration. These are alternatives within one publication. | Assess the round-letter omicron/omega condition and damaged span; the TM bridge remains UD-dependent. |
| PHR-DIS-003 | COUNT_OR_IDENTITY | TITUS headings, numeric stems and co-listed relations are different documentary units. | Physical inscription census requires explicit identity evidence. |
| PHR-DIS-004 | COUNT_OR_IDENTITY | TM/UD labels and numeric stems differ because a/b labels are retained. | Resolve identifiers through direct catalogue evidence rather than numeric normalization. |

`research/attribution-review.json` pins every referenced native artifact by SHA-256 and records exact JSON pointers. `analysis/attribution-review-audit.json` is replayed by the checker. Queries reject changed input bytes before returning any case. The earlier native records remain unchanged.

Pair-attribution states describe documentary limitations, not scientific acceptance. A partial located comparison can be a real scholarly alternative without full typographic, physical-position or independent collation. `NOT_APPLICABLE` marks controls and interpretations for which a two-reading pair is not the appropriate unit. No unknown pair/witness total is replaced with zero.
