# Corpus Factory and portable AI skill

The factory separates reusable engineering from corpus-specific scholarship.

The reusable layer handles manifests, provenance expectations, interoperability safeguards, validation structure, and project bootstrapping. Each corpus retains its own source adapter, native evidence model, rights matrix, coverage accounting, and review gates.

The AI skill in `skill/` is deliberately repository-native. Any AI assistant capable of reading the repository can follow it; it instructs the assistant to re-read the live repository state before every substantive operation so corpus updates automatically become the authoritative context on the next use.

This is **refresh-on-use**, not a claim that external AI systems receive push updates automatically.
