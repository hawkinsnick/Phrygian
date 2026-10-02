# Phrygian Open Corpus

A source-attributed research corpus and reproducible toolkit for Old and Neo-Phrygian inscriptions.

## Status

**0.1.0 — project scaffold and source-policy baseline.**

This release establishes the data model, provenance rules, interoperability contract, validation workflow, and corpus-factory compatibility. It does **not** claim exhaustive coverage, independent epigraphic review, or a new critical edition.

Initial digital source target: the TITUS Phrygian corpus, which preserves Old- and Neo-Phrygian readings, uncertainty marks, directionality, restorations, and editorial conventions derived from published editions. Third-party source terms remain controlling; this repository will not redistribute material beyond what source rights permit.

## Principles

- Preserve uncertainty, damage, directionality, restorations, and editorial interventions.
- Keep source reading, normalized representation, and interpretation distinct.
- Never turn catalogue rows or alternate readings into independent witnesses by counting them.
- Do not infer sign equivalence or language relationships from visual similarity or cross-project links.
- Every imported record must remain traceable to a source URL, locator, retrieval date, and integrity hash.
- Corpus inclusion is not decipherment or linguistic validation.

## Validation

```sh
python scripts/validate.py
python -m unittest discover -s tests -v
```

See `docs/METHOD.md`, `docs/RIGHTS.md`, and `schemas/interoperability-contract.json`.
