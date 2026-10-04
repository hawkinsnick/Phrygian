# Source reconciliation checkpoint — 4 October 2026

This checkpoint makes the reference layer reproducible and exposes defects and representation differences. It does not release a new critical edition or certify completeness.

## What a researcher can inspect

| Artifact | Evidence and limits |
|---|---|
| `analysis/reference-replay.json` | All 203 source sentences and 1,921 integer tokens replayed from pinned source bytes; per-sentence token-row hashes and complete anomaly locators. All ten columns and comments remain in the pinned CoNLL-U source. |
| `research/g12-primary-edition.json` | Publisher-located G-12 metadata and rights; candidate join to TM1001271 remains uncertified. |
| `analysis/g12-edition-comparison.json` | Seven licensed publisher lines with original HTML and superscript positions, compared at inventory level with ten UD sentences. |
| `analysis/g12-reference-fingerprint-audit.json` | Reproducible text-level candidate join: after a declared Unicode/diacritic/vacat normalization, TM1001271 is the unique exact match among all 162 UD TM groups. This is dependent digital-text evidence, not an inspected Trismegistos catalogue identity, physical-line alignment, or independent witness. |
| `research/titus-heading-catalogue.json` | 305 discovery headings: 194 Old-Phryg., 7 Mys., 104 Neo-Phryg. Heading subdivisions and comparison material are not new physical inscriptions. |
| `analysis/titus-identity-unit-audit.json` | Mechanical label-unit audit: 263 integer labels, 33 letter-suffixed labels, five Roman subdivisions, one qualified label, one range and two labels with trailing punctuation. It exposes twelve shared numeric-stem groups without collapsing them; eight contain both an unsuffixed parent heading and suffixed headings, demonstrating catalogue hierarchy rather than extra stones. |
| `analysis/titus-heading-hierarchy-audit.json` | Twenty-three explicit co-listed label edges: eighteen integer-to-suffix edges and five letter-heading-to-Roman-subdivision edges. Every parent heading is present in the same reported period/provenance scope; edges are catalogue structure, not physical relationships. |

Run these offline checks from the extracted repository:

```sh
python scripts/replay_reference.py --check
python scripts/reconcile_g12.py --check
python scripts/audit_g12_reference_fingerprint.py --check
python scripts/audit_titus_identity_units.py --check
python scripts/audit_titus_heading_hierarchy.py --check
python -m unittest discover -s tests -v
```

To repeat TITUS heading acquisition, inspect a lawfully obtained copy of the linked source and run `python scripts/inspect_titus_catalogue.py PATH_TO_HTML`. Compare its byte hash to the registered snapshot. The repository does not redistribute the full TITUS HTML or its readings.

## Findings requiring attention

The pinned UD file has twelve token `Ref` values inconsistent with their local sentence/token positions. `analysis/reference-replay.json` gives every affected row, reported reference, and expected positional reference. These are diagnostic suggestions, not sanctioned identifier replacements. Six token-derived surfaces differ from the upstream sentence `text`; both representations remain intact.

The 162 distinct UD identity labels include `TM757149a` and `TM757149b`. Removing the suffix produces 161 numeric stems, but that operation does not certify 161 physical inscriptions. Keep both readings and their source IDs; establish the upstream variant/identity mapping before statistical pooling.

G-12 provides a concrete primary-source pilot. The publisher explicitly licenses the article CC BY-NC 4.0. Its text excerpt preserves underdots, punctuation, vacat and raised letters. The seven lines cannot be aligned one-to-one with the ten dependent UD sentences. UD's S/Ṣ representation and the publisher's ś/Ś remain separate in the evidence layer. A declared lossy fingerprint normalization nevertheless makes the candidate join testable: TM1001271 is the only exact normalized-string match among 162 UD TM groups, with 142 shared character four-grams and Jaccard score 1.0; the next-ranked candidate scores about 0.0201. This establishes digital transcription correspondence only. UD cites the publisher edition, so the match is dependent evidence and does not certify the external TM object page, physical identity, line alignment, reading, period terminology, or admission. No photographs are bundled and no reading has been admitted to the canonical layer.

## Remaining frontier

The mechanical TITUS audits now separate 305 headings from 272 numeric-stem groups and identify twelve stems shared by multiple headings. Twenty-three parent edges exist only because both morphologically related headings are explicitly co-listed; this includes five Roman subdivisions under `M 1d` and `W 1a`. These are representation counts, not physical-inscription counts: the audits do not expand `Bay 1-7`, strip qualification from `W 11(?)`, or decide whether suffixes denote faces, lines, variants or distinct objects. Reconcile these units with editions, the UD ledger and the larger TM discovery benchmark. Inspect an accessible authoritative TM catalogue record before promoting the exact G-12 text correspondence to an external catalogue or object identity. Map further inscriptions to their primary editions, collate damaged readings, and document source dependence. The canonical layer remains empty; this checkpoint is a verified technical and source-acquisition improvement, not a claim to have exhausted nonexpert work.
