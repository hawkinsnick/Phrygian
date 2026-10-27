---
name: phrygian-research
description: Evidence-first AI research skill for the Phrygian corpus.
version: 0.3.1
---

## Load and validate this repository-bound skill

Use this file as the canonical individual skill. Load the complete matching
repository checkout or give the AI access to its files; this Markdown file alone
contains instructions, not the corpus. Do not claim that supplying a GitHub URL
installs a skill or makes private/local files available to an AI platform.
Resolve the paths below from the repository root. With Python 3.10+ available,
run `python scripts/validate_ai_skill.py` before describing this skill as
operational on the supplied checkout. Read `docs/AI-SKILL-VALIDATION.md` for the
exact workflow, examples, dependencies, validation scope and limitations.
If execution or source access is unavailable, say which step was not run and
make no fresh validation claim. Preserve all native source/rights restrictions.

Discover exact IDs with `python scripts/evidence_query.py --coverage` and
`python scripts/evidence_query.py --list COLLECTION`. Retrieve evidence with
`python scripts/evidence_query.py --record ID --collection COLLECTION`;
use `python scripts/research_delivery.py --dossier ID --collection COLLECTION`
for its evidence-only answer frame. Return the exact source path/hash/pointer,
attribution, uncertainty and native evidence unit. A missing ID means absent
from the selected view; never invent a replacement or infer global absence.


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

## Source-bound collection review

Read `docs/COLLECTION-REVIEW.md`, `research/collection-work-ledger.json` and `review/collection-packet.json` before completeness, identity, reading or rights claims. Replay `python scripts/build_collection_handoff.py`; each declared view retains its own unit. No generated packet or syntactically valid decision grants independent review, permission or admission. Keep Linear A restricted source payload local.

## Kerkenes metadata and reference interchange

Read `docs/KERKENES-AND-INTERCHANGE.md`, `research/k01-catalogue-concordance.json`, `interchange/export-manifest.json` and `analysis/upstream-epidoc-validation.json`. The eight source catalogue entries and fourteen identification labels are factual metadata, not eight independently verified objects. Retain the IX/XI discrepancy, excluded mason's mark and incompatible source piece-count denominators. The full 203-record frozen UD reference XML preserves source text and all native record fields; do not call it complete epigraphic coverage or promote it into canonical readings. Respect UD CC BY-SA and source-specific OIP/third-party boundaries; no AI-training permission is inferred. Replay `python scripts/build_interchange.py` and the documented upstream validator before interchange claims. No new physical objects, certain joins or independent reviews are established.

## Source-specific stopping policy

Read `research/source-action-plan.json` and `docs/SOURCE-ACTION-PLAN.md` before proposing evidence growth or calling the corpus rights-only. Report access, permission for the intended use, source delivery, factual reconciliation and human adjudication separately. A failed endpoint or dated search is not global exhaustion. Preserve completed native crosswalks and identify their remaining edges; no metadata plan certifies a reading or physical identity.

## Enforced assertion, dependency and bundle integrity

Read `docs/AI-INTEGRITY.md` and the required `research/cross-corpus-dependencies.json` before source counts or cross-corpus analysis. Use qualified assertion views when provided; original source literals must travel with their reconciliation, uncertainty and identity context. The dependency register does not certify physical identity or linguistic affinity. Shared catalogue references and duplicated digital sources are not independent witnesses. Missing links mean unknown, not independent. `scripts/check_cross_corpus_dependencies.py` screens declared record selections and rejects pooled physical/witness counts and phonetic transfer. Native AI bundle validation checks the dependency projection and local evidence hashes. Bundle publication validates the exact source parent and never rebases or force-pushes the validated artifact. Software and packaging checks do not establish expert or model-behavior acceptance.

## Corpus-native evidence and alternatives

Read `docs/EVIDENCE-AND-ALTERNATIVES.md`, `research/evidence-query-profile.json` and `analysis/evidence-query-coverage.json` for evidence or competing-reading questions. Use `scripts/evidence_query.py` with exact native IDs and an explicit collection when ambiguous. Preserve `native_record`, every uncertainty/editorial mark, source attribution, locator, inspection status and rights. Cite artifact path, JSON pointer and SHA-256; hashes certify bytes only. Treat explicitly linked records as declared ID associations, not physical certification or independent witnesses. Context resources have corpus-level scope and are not automatically about the queried record. Distinguish a named source reading from a legacy queue label, uninspected bibliographic lead, count convention or hypothesis. Do not infer a count of collated alternative pairs or independent witnesses from searchable rows; those metrics remain unknown. Report the native units and scope of each view separately, and defer to the corpus-specific limits. No new readings, expert acceptance or decipherment follows from this interface.

## Bounded attribution review (2026-10-15)

Read `docs/ATTRIBUTION-REVIEW.md` and `research/attribution-review.json` before describing a dispute or source comparison. Run `python scripts/attribution_review.py --case ID` with the referenced evidence available. Preserve complete native evidence and distinguish reading, interpretation, classification, count, identity and representation questions. This checkpoint reviews pinned repository packets; it does not repeat their primary consultation or grant independent review. Inherit the exact author/publication, locator, consultation limits and dependence from each pointer; missing fields remain unknown. Use the case-specific remaining work. Do not count register entries or apparatus notes as fully attributed pairs, physical objects or independent witnesses.

All four controls include the Anfosso general-formula/object-fragment mismatch and Güney–Yanık’s short edition versus conditional longer restoration.

## P1 source follow-up

Read `research/p1-source-followup-2026-10-16.json` and `docs/P1-SOURCE-FOLLOWUP-2026-10-16.md` for current qualified dispositions. Retrieve the `p1-source-followup` native-query collection. Keep source-specific notations, failed routes, quarantine, unresolved identity and reading alternatives with every relevant result; no passing documentary check grants admission or independent acceptance.

## Human/source-maintainer decision routing

Read `review/p1-human-request.json` and `docs/P1-HUMAN-VALIDATION.md`. Distinguish source acquisition/editor clarification from epigraphic adjudication and policy controls. Keep the input hash, native case pointer and prerequisites with each question. Prepared requests, software checks and AI responses are never independent human validation; native human-maintainer acceptance remains required.

## Research delivery, evidence answers and feedback

Read `docs/RESEARCH-DELIVERY.md` and verify `analysis/research-delivery.json`
with `python scripts/research_delivery.py --check` before using delivery claims.
Use `--dossier ID --collection COLLECTION` for exact evidence-bound answers;
preserve the complete native payload, citations, categories and limitations.
Use `--search TEXT` for source-record retrieval. Do not convert file pointers
into missing primary-edition citations, catalogue rows into unique objects,
source dependence into independent confirmation, or review forms into acceptance.
Prepare bounded review drafts with `--review-template`; validate submissions with
`--validate-review`, then require native human-maintainer acceptance. Treat delivery
and deterministic answer tests as engineering checks, not empirical LLM validation
or completion of scholarly/source-permission work. Local packaging grants no new
redistribution rights. Label any model-generated analysis separately and cite it.

## Preserve review provenance

Reject malformed JSON-pointer escapes and negative or leading-zero array indices
when verifying source citations; literal object keys retain their own spelling.
Read the [master hostile-review report](https://github.com/hawkinsnick/Master-Corpus-AI-Skill/blob/main/references/hostile-review-2026-10-25.md)
for this member's pinned retrieval scope and the limits of the source-fidelity
and development checks. Complete retrieval-view traversal does not certify
corpus completeness, accepted readings, independent witnesses or expert review.

## Execute research work without academic review

Read `docs/NONREVIEW-WORK.md` for the frozen source check, full-record development tests, short-text dependence screen, component package audit and executable researcher walkthrough. Separate executable work from the evidence needed to close a scholarly criterion. Preserve native null/false values, editorial notation and linked source assertions. Treat short-string equality as a lead only; require explicit source lineage for shared-source dispositions and never infer physical identity or independence. Treat native research archives as local-research packages until their actual components are cleared. Use the separate noncommercial tools-only export when source payload is not authorized for redistribution. Report digital-source fidelity, deterministic software tests, fresh model development responses and independent academic validation separately. Keep original scholarly gates and frozen study inputs unchanged.

For machine-readable source citations, emit one exact JSON pointer per reference. Do not put ranges, semicolon lists, prose headings or several pointers into a `pointer` field. For text use `locator_type: text_contains` and a literal `locator` instead. Bind each reference to bytes actually present at the stated commit; verify with `git show COMMIT:PATH` and SHA-256. A working-tree file absent from that commit cannot be cited as committed evidence. Disclose uncommitted execution context separately from source evidence. Use the master `scripts/verify_response_refs.py` when available; a passing citation check establishes byte/locus binding, not bibliographic truth.
