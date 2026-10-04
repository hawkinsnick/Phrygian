# Source reconciliation checkpoint — 4 October 2026

This checkpoint makes the reference layer reproducible and exposes defects and representation differences. It does not release a new critical edition or certify completeness.

## What a researcher can inspect

| Artifact | Evidence and limits |
|---|---|
| `analysis/reference-replay.json` | All 203 source sentences and 1,921 integer tokens replayed from pinned source bytes; per-sentence token-row hashes and complete anomaly locators. All ten columns and comments remain in the pinned CoNLL-U source. |
| `research/g12-primary-edition.json` | Publisher-located G-12 metadata and rights; candidate join to TM1001271 remains uncertified. |
| `analysis/g12-edition-comparison.json` | Seven licensed publisher lines with original HTML and superscript positions, compared at inventory level with ten UD sentences. |
| `research/titus-heading-catalogue.json` | 305 discovery headings: 194 Old-Phryg., 7 Mys., 104 Neo-Phryg. Heading subdivisions and comparison material are not new physical inscriptions. |

Run these offline checks from the extracted repository:

```sh
python scripts/replay_reference.py --check
python scripts/reconcile_g12.py --check
python -m unittest discover -s tests -v
```

To repeat TITUS heading acquisition, inspect a lawfully obtained copy of the linked source and run `python scripts/inspect_titus_catalogue.py PATH_TO_HTML`. Compare its byte hash to the registered snapshot. The repository does not redistribute the full TITUS HTML or its readings.

## Findings requiring attention

The pinned UD file has twelve token `Ref` values inconsistent with their local sentence/token positions. `analysis/reference-replay.json` gives every affected row, reported reference, and expected positional reference. These are diagnostic suggestions, not sanctioned identifier replacements. Six token-derived surfaces differ from the upstream sentence `text`; both representations remain intact.

The 162 distinct UD identity labels include `TM757149a` and `TM757149b`. Removing the suffix produces 161 numeric stems, but that operation does not certify 161 physical inscriptions. Keep both readings and their source IDs; establish the upstream variant/identity mapping before statistical pooling.

G-12 provides a concrete primary-source pilot. The publisher explicitly licenses the article CC BY-NC 4.0. Its text excerpt preserves underdots, punctuation, vacat and raised letters. The seven lines cannot be aligned one-to-one with the ten dependent UD sentences. UD's S/Ṣ representation and the publisher's ś/Ś remain separate. The publisher title's New Phrygian terminology and UD's Middle Phrygian classification are attributed separately. No photographs are bundled and no reading has been admitted to the canonical layer.

## Remaining frontier

Reconcile TITUS heading identities, subdivisions and editions with the UD ledger and the larger TM discovery benchmark. Verify the G-12 TM join using an accessible authoritative catalogue. Map further inscriptions to their primary editions, collate damaged readings, and document source dependence. The canonical layer remains empty; this checkpoint is a verified technical and source-acquisition improvement, not a claim to have exhausted nonexpert work.
