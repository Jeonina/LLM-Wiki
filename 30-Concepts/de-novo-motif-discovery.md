---
type: concept
title: De novo motif discovery
aliases: []
tags: [motif, regulatory-elements, transcription-factors]
created: 2026-05-12
updated: 2026-10-07
---

# De novo motif discovery

> The identification of previously unannotated TF binding motifs from sequence data (e.g., ChIP-seq peaks, accessible chromatin regions). Methods include MEME, HOMER, gimmemotifs, and k-mer-based approaches.

## Why it matters

- Reveals novel regulators in poorly-annotated cell types and species.
- [[30-Concepts/chromvar]]'s k-mer-based de novo motif assembly uses covariance between similar k-mers across cells to reconstruct motifs.

## Added 2026-10-07

BROCKMAN performs motif-agnostic analysis by PCA on gapped k-mer frequencies near Tn5 insertion sites and only afterwards maps PC loadings to TFs via CIS-BP PBM and PWM specificities, so cells differing by an uncharacterised TF can still be separated ([[10-Summaries/de-boer-2018-brockman]]). TFs co-enriched on the same PC showed 2.5× more high-confidence protein–protein interactions than expected ([[10-Summaries/de-boer-2018-brockman]]).


## Related

- [[30-Concepts/transcription-factor-motif]] · [[30-Concepts/chromvar]] · [[40-Topics/single-cell-atac-seq]]
