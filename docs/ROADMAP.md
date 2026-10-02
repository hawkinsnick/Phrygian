# Roadmap

## 0.2.0 — Source acquisition and alignment

The repository contains a licensed, source-attributed UD Phrygian-KUL reference snapshot with 203 sentences, 1,921 tokens, and 162 distinct Trismegistos identifiers. This layer is deliberately separate from the canonical epigraphic corpus.

Canonical `data/records.json` remains empty until inscription-level readings can be reconciled with authoritative epigraphic editions and the project's provenance and review schema. This is a scientific gate.

## Next gates

1. Reconcile UD/TM-linked records to authoritative epigraphic editions and exact locators.
2. Establish Old/Neo-Phrygian period metadata from authoritative catalogues.
3. Build a source-dependence graph so digital derivatives are not counted as independent witnesses.
4. Admit canonical records only after source reading, restoration, provenance, and review fields are supportable.
5. Expand source coverage without treating corpus size as evidence quality.

See `research/expert-review-queue.json` for the human-validation boundary.


## Pre-Expert identity reconciliation — 2026-10-02

`research/tm-reconciliation-ledger.json` now accounts for all 162 Trismegistos identity anchors represented by the 203 licensed UD reference sentences. This is identity/source reconciliation only: authoritative edition locators, physical-object identities, period assignments and provenance remain unset until source-level evidence supports them. No record is thereby admitted to the canonical epigraphic layer.
