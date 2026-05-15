---
type: summary
title: "Mali et al. 2025 — Conformational Heterogeneity: a metric for cell-to-cell 3D-genome variability"
source: "[[00-Sources/papers/Quantifying conformational heterogeneity of 3D genome organization in fruit fly]]"
source_kind: paper
author: "Samira Mali, Igor S. Tolokh, Erik Cross, Alexey V. Onufriev (corresponding)"
published: 2025-07-03
ingested: 2026-05-15
doi: "10.1371/journal.pone.0326927"
journal: "PLOS One"
tags: [3D-genome, Hi-C, scHi-C, polymer-model, conformational-heterogeneity, lamina, LAD, Drosophila, computational]
entities:
  - "[[20-Entities/alexey-onufriev]]"
concepts:
  - "[[30-Concepts/conformational-heterogeneity]]"
  - "[[30-Concepts/single-cell-hi-c]]"
  - "[[30-Concepts/lamina-associated-domains]]"
  - "[[30-Concepts/nuclear-lamina]]"
  - "[[30-Concepts/topologically-associating-domain]]"
topics:
  - "[[40-Topics/3d-genome]]"
  - "[[40-Topics/chromatin-architecture]]"
---

**Citation:** Mali et al. (2025) — *Conformational Heterogeneity: a metric for cell-to-cell 3D-genome variability* — *PLOS One*. [DOI](https://doi.org/10.1371/journal.pone.0326927)

# Mali et al. 2025 — Conformational Heterogeneity metric

> Thesis: cell-to-cell variability of 3D chromatin folding has been described qualitatively for a decade, but no compact, distribution-aware metric exists for it. The authors define **Conformational Heterogeneity (C.H.)** as the standard deviation, across single cells, of the *per-cell-averaged* Euclidean inter-loci distance ⟨R_s⟩ at genomic separation *s*. Applied to three independently constructed 3D models of the *Drosophila* X chromosome — two trained on bulk Hi-C + lamina-DamID, one on scHi-C — the metric exposes that **bulk-trained and scHi-C-trained models diverge in opposite directions** at 1–10 Mb separations. The metric is also sensitive enough to register **increased structural noise upon nuclear-lamin depletion**, supporting the prediction that transcription should be noisier in lamin-depleted nuclei.

## Key claims

- **C.H.(s) = stdev_cells(⟨R_s⟩)** (Eq 4). By averaging *within* each nucleus first and then taking dispersion *across* nuclei, the metric isolates inter-cell heterogeneity from intra-cell conformational dynamics. An ensemble of identical-but-internally-variable nuclei would yield C.H. = 0.
- **Relative C.H.** = stdev(⟨R_s⟩) / mean(⟨R_s⟩) — dimensionless, makes models with different length-unit conventions (arbitrary DPD units vs microns) directly comparable.
- **Resolution dependence**: higher-resolution models show larger C.H. near the resolution limit. The **MC-TAD algorithm** is introduced to "up-convert" lower-resolution (e.g., 118-kb TAD-level) models to ~14-kb or even ~2-kb resolution by sampling all permissible chromatin paths threading through TAD-internal bins; this allows fair comparison with native 10-kb single-cell Hi-C models.
- **Model divergence at 1–10 Mb**:
  - Tolokh 2023 + Li 2017 (both bulk-Hi-C + lamina-DamID trained): Relative C.H. dips to ~0.05 around 1 Mb, rises to ~0.2 at 10 Mb.
  - Ulianov 2021 (scHi-C trained from 20 BG3 cells): opposite curve — peaks ~0.18 at ~0.8 Mb, drops to ~0.05 at 10 Mb.
  - Authors trace this to (i) Tolokh/Li models retain dense weak TAD-TAD contacts from bulk Hi-C that aren't present in 20-cell scHi-C; (ii) Ulianov simulation box is smaller (~2 μm) than the modeled fly nucleus, suppressing long-range cell-to-cell spread.
- **Lamin depletion ↑ heterogeneity**: in the Tolokh model, removing LAD–NE affinity raises Relative C.H. at nearly all genomic separations. Consistent with experimental loss of chromosome-territory structure upon lamin knockdown. **Prediction**: cellular noise in transcription should rise in lamin-depleted nuclei.
- **Methodological recommendation**: scHi-C-trained 3D models should incorporate bulk-Hi-C restraints as a supplementary fit until single-cell map ensembles are large enough to represent true population distributions.

## Methods / evidence

- **Three model ensembles compared**: (1) Li 2017 — machine-learning population of 10,000 chromatin structures matching bulk Hi-C + lamina-DamID contact matrix (Pearson r=0.984 to experimental); (2) Tolokh 2023 — Langevin dynamics of 18 diploid nuclei, ~11 h biological time each; (3) Ulianov 2021 — dissipative particle dynamics of 20 single-cell models matching 20 scHi-C maps at 10-kb resolution.
- **MC-TAD ("Monte-Carlo TAD")**: enumerates permissible chromatin paths through N³ bins in a TAD-cube; for N=4 (≈2-kb resolution within a 118-kb TAD), σ_R = 0.40 a.u. used as up-conversion noise injection.
- **Comparator baselines**: ensembles of approximate orientation-random Hilbert curves (space-filling fractal) and freely-jointed chains (FJC, end-to-end ∝ √s). All realistic models exceed FJC/Hilbert C.H. up to ~500 kb, indicating that real chromatin has more cell-to-cell structural diversity than random-polymer null models at sub-Mb scales.

## Surprising or load-bearing bits

- **The same bulk Hi-C map can arise from different distributions of single-cell maps** — explicitly demonstrated (S1 Text). C.H. distinguishes these distributions where bulk Hi-C cannot. Direct methodological consequence: bulk Hi-C is *underdetermined* for the per-cell 3D structure question.
- **Resolution near the limit dominates the C.H. number**; beyond ~100 kb the underlying polymer model takes over, and extrapolation from 10 kb to 2 kb has minor effect except at the smallest separations.
- **The prediction that lamin depletion increases transcriptional noise** is testable: scDam&T-seq or scNMT-seq in lamin-knockdown vs WT cells should show greater cell-to-cell expression variance with no necessary change in mean expression.
- **Generalization beyond fly**: lamin-depletion-driven loss of chromosome territories is conserved in mammals (cited Ulianov 2019), so the C.H.-noise prediction transfers — addressable with scHi-C of progerin or LMNA-mutant mammalian cells.

## Entities mentioned

- [[20-Entities/alexey-onufriev]] — corresponding; Virginia Tech; biophysics / chromatin polymer modeling.
- Sergey Ulianov, Ekaterina Khrameeva — scHi-C *Drosophila* dataset providers (Ulianov 2021).
- Frank Alber — Li 2017 model genome structures; acknowledged.

## Concepts touched

- [[30-Concepts/conformational-heterogeneity]] — *defines* the concept (new wiki entry).
- [[30-Concepts/single-cell-hi-c]] — exposes a sample-size limitation of current scHi-C: with ~20 cells, single-cell-trained models miss frequent weak TAD-TAD contacts that bulk Hi-C captures.
- [[30-Concepts/lamina-associated-domains]] / [[30-Concepts/nuclear-lamina]] — lamin depletion as a perturbation that elevates structural heterogeneity.
- [[30-Concepts/topologically-associating-domain]] — TADs as the natural resolution unit for 3D models; MC-TAD generates intra-TAD path ensembles.

## Connections to other sources

- **Builds on / depends on** [[10-Summaries/de-luca-2021-scdamid-protocol]] and [[10-Summaries/rooijers-2019-scdamt-seq]] (lamina-DamID data that feeds Tolokh/Li training).
- **Extends** [[10-Summaries/nagano-2013-nature]] / [[10-Summaries/tan-2018-science]] / [[10-Summaries/hong-2025-sc3d-genome-review]] — moves from descriptive single-cell-3D maps to a single-number metric for population-level heterogeneity comparison.
- **Bridges to** [[10-Summaries/elliott-2025-naturebiotechnology]] — DAF-seq's 63% inter-cell actuation divergence is the chromatin-actuation analogue of C.H. for accessibility rather than 3D distance.
- **Methodologically relevant to** [[10-Summaries/jiang-2026-stark-scnucleome]] — STARK / SSCE quality metric is a *per-cell* structural fidelity score, complementary to *across-cell* C.H.

## Open questions

- **Higher moments**: C.H. is the second moment of the ⟨R_s⟩ distribution; what about skewness/kurtosis? Distributions could be Gaussian or strongly multi-modal (e.g., locus-position bistability) and C.H. alone won't distinguish them.
- **Time evolution within interphase**: does C.H. itself evolve as cells progress through G1→S→G2? Tolokh's 11-hour trajectories sample one cell-cycle window; extending to cycling cells via scHi-C cell-cycle phase data (Nagano 2017) is the natural follow-up.
- **Disease / cancer**: C.H. as a biomarker? Chromatin re-arrangements in laminopathies, premature aging, cancer (cited Perez-Rathke 2019, Wang 2023) could be quantified — but this requires substantially larger scHi-C cohorts than currently exist.
- **Cross-organism**: dimensionless Relative C.H. is meant to be comparable across organisms; an experimental test against mammalian scHi-C atlases would validate this.

---
**Source:** [DOI](https://doi.org/10.1371/journal.pone.0326927) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/40608785/) · [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12225887/) · [Code/Data](https://github.com/Onufriev-Lab/hi-c_model_validation)

## Related

- [[30-Concepts/conformational-heterogeneity]] · [[30-Concepts/single-cell-hi-c]] · [[30-Concepts/lamina-associated-domains]] · [[30-Concepts/nuclear-lamina]] · [[30-Concepts/topologically-associating-domain]]
- [[10-Summaries/de-luca-2021-scdamid-protocol]] · [[10-Summaries/rooijers-2019-scdamt-seq]]
- [[40-Topics/3d-genome]] · [[40-Topics/chromatin-architecture]]
