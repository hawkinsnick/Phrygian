# Phrygian Open Corpus

A source-attributed research corpus and reproducible toolkit for Old, Middle and Neo-Phrygian inscriptions.

## AI research skill

This corpus project includes a vendor-neutral, evidence-first AI research skill in [`ai-skill/`](ai-skill/). The corpus remains the scholarly source of truth; the skill is an interface to it, not a second corpus or independent authority.

Researchers can provide the repository or AI-ready bundle to a capable AI together with [`ai-skill/SKILL.md`](ai-skill/SKILL.md). The skill preserves provenance, uncertainty, exclusions, source dependence, rights, and this project's scientific gates. Check [`ai-skill/generated/source-state.json`](ai-skill/generated/source-state.json) and the research-bundle index before substantive use.

For questions spanning corpus projects, use the **Combined Corpus Research AI** in [`combined-ai-skill/`](https://github.com/hawkinsnick/Linear-A/tree/ai-skill-v0.1/combined-ai-skill). It orchestrates registered individual skills without merging their evidence. Membership does not imply linguistic relationship, sign equivalence, chronology, decipherment, or independent replication.

## Status

**0.2.0 — source acquisition and alignment milestone.**

The repository now also preserves a separately attributed UD Phrygian-KUL machine-readable reference snapshot: 203 sentences, 1,921 tokens, and 162 distinct Trismegistos identifiers. The canonical epigraphic layer remains empty pending source-level reconciliation. The reference layer is **not** independent epigraphic review and does not constitute a new critical edition.

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

The licensed upstream README is pinned in `imports/ud-phrygian-kul-readme.md` with attribution to the UD Phrygian-KUL contributors (CC BY-SA 4.0). Run `python scripts/reconcile_source_documentation.py` to replay its two explicit edition/TM joins. The reference layer remains separate from canonical epigraphic admission. See `research/source-inspection-2026-10-02.json` for edition genealogy and representation limits.

## Source reconciliation checkpoint

See [the 4 October 2026 evidence checkpoint](docs/SOURCE-RECONCILIATION.md) for new source-located evidence, reproducible checks, unresolved anomalies and the remaining primary-source work.


## Offline corpus browser
Run `python scripts/build_corpus_browser.py` to generate `workbench/corpus-browser.html`. It searches only files explicitly admitted by `research/browser-sources.json`. Browser admission requires rights/provenance review; never recursively ingest restricted or raw upstream material. Display does not establish decipherment, source independence, or expert validation.
