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
- G-12 has seven publisher lines and ten candidate UD sentences. A declared lossy fingerprint normalization makes TM1001271 the unique exact text match among 162 UD TM groups; because UD depends on the publisher edition, this is reproducible dependent text correspondence, not physical-line alignment, external catalogue certification, or an independent witness.
- Only 3 of 162 TM groups currently have record-specific edition lineage explicit in inspected evidence. A corpus-level statement about principal sources must never be expanded into 159 unproved record-level joins.
- Read `research/new-phrygian-primary-dossier.json` and replay `analysis/new-primary-comparison.json`: TM1002268 matches the general formula on Anfosso p. 112 rather than the separate p. 113 fragment; the catalogue bridge remains unresolved and must not be used as a diplomatic transcription of that fragment pending resolution. TM1002269 matches the short published edition text, with a longer competing reconstruction in the commentary. Preserve both reading possibilities and distinguish UD numbers from primary catalogue and survey inventory numbers. Neither comparison certifies an external TM identity or creates an independent witness.
- TITUS heading catalogue includes Old-Phryg., Mys., and Neo-Phryg. sections; Mys. is a comparison section, not automatically Phrygian evidence.
- The TITUS identity-unit audit retains 305 headings, 272 mechanical numeric-stem groups and twelve multi-heading stems as incompatible counting views. Eight multi-heading groups co-list an unsuffixed parent heading with suffixes; this is catalogue hierarchy, not a certified physical relationship or inscription count.
- The TITUS hierarchy audit permits only 23 relations whose parent and child headings are both co-listed in the same period/provenance scope (18 integer-to-suffix and five letter-to-Roman-subdivision). These remain label relations, never physical-object relations.


## Offline corpus browser
Run `python scripts/build_corpus_browser.py` to generate `workbench/corpus-browser.html`. It searches only files explicitly admitted by `research/browser-sources.json`. Browser admission requires rights/provenance review; never recursively ingest restricted or raw upstream material. Display does not establish decipherment, source independence, or expert validation.


## Linear A method-parity gate
Phrygian has reached the machine-resolvable pre-expert method-parity baseline for the evidence currently lawful to use: source dependence, disagreements, rights controls, discovery/counting cautions, rights-allowlisted browser, read-only API, loss-aware exports, reproducible audits and reviewer packaging are explicit. Read `docs/RIGHTS-ONLY-READINESS.md` and `research/residual-blocker-ledger.json` before completeness claims. Further systematic critical-edition growth is constrained by rights/access to Brixhe–Lejeune, Obrador-Cursach, TITUS and item-level evidence. The licensed UD layer remains dependent reference evidence and must not be promoted into an independently verified critical edition. Expert adjudication remains downstream.


## Maximum pre-expert campaign (2026-10-06)

The earlier rights-only declaration has been narrowed. Protected systematic extraction from Brixhe-Lejeune, Obrador-Cursach and uncertain-rights digital editions remains rights-gated, but lawful public record-level factual metadata and identity reconciliation are still an open corpus-development lane.

Read `research/catalogue-denominator-control.json`, `research/subcorpus-source-genealogy.json`, and `research/public-object-metadata-lane.json`.
- Never divide 162 UD TM labels into the TM 536-attestation benchmark as an exact coverage percentage before identity reconciliation.
- TITUS's 305 headings include subdivisions/alternatives and a Mysian comparison section; they are not 305 unique Phrygian inscriptions.
- UD, TITUS and their underlying editions must be counted by reading lineage, not as independent epigraphic confirmations.
- Public monument pages may support attributed factual object/layout/direction metadata when individually inspected; dependent displayed readings remain non-canonical until source-level verification.
- Keep canonical epigraphic admission sealed rather than using a licensed NLP corpus as a substitute for critical epigraphy.


### Public monumental and Kerkenes expansion
The lawful factual-metadata lane now extends beyond M-03/M-06. Consult `research/public-object-metadata-lane.json` for controlled Midas City and selected outlier records. Preserve catalogue namespaces: the public source explicitly distinguishes its Menekse Kayalar W-11 from Brixhe W-11, represented there as MPhr-01. Never merge these by label alone.

For K-01, consult `research/k01-open-primary-route.json`. ISAC/OI exposes OIP 135 as a publisher-hosted downloadable excavation volume with inscription fragments cat. nos. 13-20 and an inventory/catalogue concordance. Treat this as lawful inspection access, not automatic redistribution permission. Extract attributed factual provenance/identity controls only where inspected; do not copy protected figures, prose or critical text merely because the PDF is downloadable.


### Gordion and Kerkenes small-object frontier
Read `research/gordion-institutional-discovery.json` and `research/coverage-denominator-register.json`. Penn Museum's Digital Gordion reports 11 Early Phrygian stone inscriptions and 245 graffiti, primarily on vases. These are source-reported category counts, not automatically unique-object totals, and expose a major small-object frontier omitted by monument-focused discovery resources.

Read `research/kerkenes-oip148-graffiti-route.json` alongside the K-01 dossier. OIP 148 provides a separate publisher-hosted archaeological route for pot marks/graffiti and context. Never classify every mark as linguistic Phrygian, and never count a repeated discussion of K-01 as a new witness.
