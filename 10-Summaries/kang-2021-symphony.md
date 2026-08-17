---
type: summary
title: "Kang et al. 2021 — Efficient and precise single-cell reference atlas mapping with Symphony"
source: "[[00-Sources/papers/Efficient and precise single-cell reference atlas mapping with Symphony]]"
source_kind: paper
author: "Joyce B. Kang, Aparna Nathan, Kathryn Weinand, Fan Zhang, Nghia Millard, Laurie Rumker, D. Branch Moody, Ilya Korsunsky, Soumya Raychaudhuri (corresponding)"
published: 2021-10-07
ingested: 2026-08-17
doi: "10.1038/s41467-021-25957-x"
journal: "Nature Communications 12:5890"
tags: [Symphony, reference-mapping, atlas, Harmony, compressed-reference, label-transfer, scArches, fetal-liver, CITE-seq]
entities: ["[[soumya-raychaudhuri]]"]
concepts: ["[[multimodal-integration-methods]]", "[[batch-effect]]", "[[cell-type-annotation]]", "[[dimensionality-reduction]]", "[[cite-seq]]", "[[trajectory-inference]]"]
topics: ["[[computational-methods]]", "[[single-cell-multiomics]]"]
---

**Citation:** Kang et al. (2021) — *Efficient and precise single-cell reference atlas mapping with Symphony* — *Nature Communications* 12, 5890. [DOI](https://doi.org/10.1038/s41467-021-25957-x)

# Kang 2021 — Symphony

> Once an atlas exists, the operation you actually perform a hundred times is **mapping a new dataset onto it** — and the obvious approach, re-integrating reference and query from scratch, is wrong on three counts: intractable at millions of cells, requires shipping the raw reference around, and **corrupts the carefully annotated reference embedding**. Symphony compresses an integrated reference into a portable form and localises query cells within the **frozen** embedding in seconds.

## Key claims

- **The reference must be frozen.** The "gold standard" of de novo joint integration is reasonable for small references and unacceptable for atlas-scale ones: it forces rebuilding for every analysis, requires "administratively cumbersome exchanges of large-scale datasets", and can corrupt an embedding that was painstakingly constructed and annotated.
- **Reference mapping ≠ classification.** Symphony places query cells in the same embedding as reference cells *without using any annotation* — deliberately, because labels get refined over time. This contrasts with supervised classifiers like scmap that assign rigid annotations. The embedding is annotation-agnostic; annotations are transferred afterwards.
- **Four requirements for an ideal reference-mapping algorithm**: remove confounding from complex study design in *both* reference and query; scale to large datasets; map accurately; and support inference of diverse query annotations.
- **Built on [[korsunsky-2019-harmony|Harmony]]**, the same group's integration method, chosen because it explicitly models complex study design — a property that makes it suitable for building references from heterogeneous sources.
- **Three demonstrations, three kinds of transferred annotation**: (1) multi-donor, multi-species query mapped to predict pancreatic cell types (discrete labels); (2) query cells localised along a **developmental trajectory** of fetal liver hematopoiesis (continuous position); (3) **surface protein expression inferred** from a multimodal CITE-seq atlas of memory T cells (a modality the query never measured).
- **Seconds, not hours** — the headline operational claim.

## Methods / evidence

Three real-world mapping tasks chosen to span annotation types, each with a de novo integration comparison as the accuracy reference. Code at github.com/immunogenomics/symphony.

## Surprising or load-bearing bits

- **Inferring an unmeasured modality by reference mapping** is the quietly radical capability: map scRNA-seq onto a CITE-seq atlas and read off predicted surface protein. It is the same idea [[lakkis-2022-scipenn|sciPENN]] pursues by deep learning and [[debnath-2026-ison|ISON]] pursues for spatial chromatin accessibility — *the reference substitutes for a measurement you did not make*. (synthesis)
- **"Map to reference" is an analogy to read alignment**, made explicitly in the abstract, and the analogy carries: a stable reference, a fast query operation, and a separation between building (expensive, rare) and mapping (cheap, constant). That separation is the actual contribution. (synthesis)
- **Freezing the reference is a scientific choice, not only an engineering one.** A moving reference means two labs mapping the same query get different answers; reproducibility requires the reference to be a fixed object. (synthesis)
- **Annotation-agnostic embedding future-proofs the reference** — labels can be revised without recomputing the embedding, which is the failure mode of supervised classifiers.
- The related-work section is a clean map of the reference-mapping landscape circa 2021: Seurat (anchor-compatible), scArches (autoencoder-compatible, scANVI/trVAE), versus de novo integrators BBKNN, Seurat anchors, and Harmony.

## Entities mentioned

- [[soumya-raychaudhuri]] — corresponding author; also the Harmony line.

## Concepts touched

- [[multimodal-integration-methods]] — reference mapping as a distinct operation from integration.
- [[cell-type-annotation]] — label transfer decoupled from embedding construction.

## Connections to other sources

- Direct dependency, same group: [[korsunsky-2019-harmony]].
- Anchor-based mapping alternative: [[butler-2018-seurat-cca]], [[hao-2021-seurat-wnn]], [[hao-2024-seurat-v5]].
- Label-transfer competitor from a different tradition: [[song-2021-scgcn]].
- Cross-modality inference cousins: [[lakkis-2022-scipenn]], [[debnath-2026-ison]], [[biancalani-2021-tangram]].
- Integration methods usable for reference building: [[haghverdi-2018-mnn]], [[welch-2019-liger]], [[ashuach-2023-multivi]], [[cao-2022-glue]].
- Taxonomy and benchmark: [[argelaguet-2021-integration-principles]], [[xiao-2024-multiomics-benchmark]].
- Atlas context: [[cao-2019-moca]], [[heumos-2023-best-practices]].

## Open questions

- **A frozen reference cannot represent cell states absent from it** — the same failure mode the landmark-projection critique in [[haghverdi-2018-mnn]] identified. Symphony inherits it by design; query-specific novel populations have nowhere correct to go. (synthesis)
- Inferred surface protein is only as good as the reference's antibody panel and the RNA–protein relationship in the reference's tissue context; transferability across tissues is untested.
- Whether Harmony's assumptions (linear, embedding-space correction) limit which references can be compressed this way is not explored.

## Related

- [[korsunsky-2019-harmony]] · [[hao-2021-seurat-wnn]] · [[cell-type-annotation]] · [[40-Topics/computational-methods]]
