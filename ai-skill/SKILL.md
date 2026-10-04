---
name: phrygian-research
description: Evidence-first AI research skill for the Phrygian corpus.
version: 0.3.1
---

# Phrygian Research Skill

This skill is an interface to the corpus in this repository. The corpus remains the canonical source of truth. Never maintain an independent scholarly dataset inside the skill.

## Governing rules
1. Separate physical/epigraphic observation, source transcription, normalization, computational derivation, scholarly interpretation, and AI-derived analysis.
2. Prefer canonical machine-readable corpus records over prose summaries for record-level questions.
3. Preserve identifiers, provenance, uncertainty, disagreements, corrections, negative results, and superseded analyses.
4. Never invent missing signs, readings, restorations, provenience, bibliography, source independence, or rights.
5. Label calculations performed by the AI and state enough method for reproduction.
6. Respect record/source-specific licensing and attribution. Repository-level licensing must not erase upstream restrictions.
7. For cross-corpus claims, establish comparability and source independence before interpreting similarity.
8. Report blocked or missing evidence rather than filling gaps.

## Corpus-specific caution
Attested Indo-European language: distinguish Old/New Phrygian evidence, transcription, restoration, morphology, and comparative interpretation; cite corpus evidence for substantive claims.

## Default research response
Give the direct answer, followed as relevant by Evidence; Evidentiary status; Uncertainty/limitations; Reproducibility; Rights/attribution.

## Synchronization
Read `ai-skill/generated/source-state.json` before substantive work. It records the corpus commit from which the AI-facing package was synchronized. Generated files are rebuildable views; canonical corpus files govern if a discrepancy is found.

## Academic-scrutiny gates
- The current repository is a scaffold/source-policy baseline, not an exhaustive corpus
- Old and Neo-Phrygian remain explicit period partitions
- Digital source entries and alternate editions are not automatically independent physical witnesses
- Normalized or Greek-script renderings never overwrite source readings
- TITUS and underlying edition rights remain controlling

## Source reconciliation checkpoint
Read `docs/SOURCE-RECONCILIATION.md` and the indexed source-reconciliation artifacts before comparing versions, counting identities, or preparing specialist review.
- Replay pinned UD bytes and all ten token columns before using derived data; retain twelve Ref diagnostics and six source-text/token-surface differences.
- 162 UD source identity labels contain two letter-suffixed labels sharing one numeric stem; neither 162 labels nor 161 numeric stems is a certified physical-inscription count.
- G-12 has seven publisher lines and ten candidate UD sentences; no physical line alignment or catalogue-certified TM join is established.
- TITUS heading catalogue includes Old-Phryg., Mys., and Neo-Phryg. sections; Mys. is a comparison section, not automatically Phrygian evidence.
- The TITUS identity-unit audit retains 305 headings, 272 mechanical numeric-stem groups and twelve multi-heading stems as incompatible counting views. Eight multi-heading groups co-list an unsuffixed parent heading with suffixes; this is catalogue hierarchy, not a certified physical relationship or inscription count.
- The TITUS hierarchy audit permits only 23 relations whose parent and child headings are both co-listed in the same period/provenance scope (18 integer-to-suffix and five letter-to-Roman-subdivision). These remain label relations, never physical-object relations.
