# Ancient Corpus Factory AI Skill

## Purpose

Use this skill to create, audit, extend, or align an ancient-language/epigraphic corpus while preserving provenance, uncertainty, rights boundaries, and corpus-specific evidence units.

## Non-negotiable safeguards

- Never infer permission to redistribute from public web access.
- Never silently normalize away damage, uncertainty, restorations, directionality, editorial marks, or alternate readings.
- Never count catalogue entries or alternate editions as independent physical witnesses without explicit evidence.
- Never infer language identity, script identity, sign equivalence, decipherment, or genetic relationship from interoperability or visual similarity.
- Preserve upstream licenses/terms per source.
- Prefer metadata-only/provenance-only capture when redistribution rights are unclear.
- Treat checksums as integrity evidence, not scholarly validation.
- Keep independent expert review as a separate release gate.

## Workflow

1. Inspect the target repository and existing family contracts before changing schemas.
2. Register candidate sources with URL, authority, locator strategy, rights status, and retrieval date.
3. Choose the closest native record profile; do not force a universal record model.
4. Create raw/source-evidence and derived layers separately.
5. Add deterministic validation and negative tests before importing at scale.
6. Generate machine-readable exports only from validated records.
7. Run interoperability checks.
8. Report exact coverage and exclusions; never call a corpus exhaustive unless source reconciliation supports that claim.
9. When a source changes, refresh only the affected adapter/records and rerun validation.
10. When the GitHub corpus updates, re-read the repository's current VERSION, schemas, METHOD, rights docs, and release status before analysis.

## AI portability

This skill is plain Markdown plus repository files and is designed to be understandable by any AI system that can read a Git repository. It does not depend on proprietary hidden state. The repository remains the source of truth.

## Factory entry points

- `factory/corpus-manifest.schema.json`
- `factory/bootstrap.py`
- `schemas/interoperability-contract.json`
- project-specific `docs/METHOD.md` and rights documentation

## Output discipline

Always distinguish:
- observed/source text,
- editorial reconstruction,
- normalized representation,
- interpretation,
- project inference,
- independent scholarly review.

If any distinction is unavailable, mark it unknown rather than filling it speculatively.
