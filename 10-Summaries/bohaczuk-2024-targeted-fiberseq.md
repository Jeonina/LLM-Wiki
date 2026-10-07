---
type: summary
title: "Bohaczuk 2024 — Resolving the chromatin impact of mosaic variants with targeted Fiber-seq"
source: "[[00-Sources/papers/Resolving the chromatin impact of mosaic variants with targeted Fiber-seq.pdf]]"
source_quality: full
source_sha256: "858f41e815b92e24a0a751802eb073194ee278d7e246392fe2a2a79c601c2b71"
source_kind: paper
author: "Stephanie C. Bohaczuk, Zachary J. Amador, Chang Li, Benjamin J. Mallory, Elliott G. Swanson, Jane Ranchalis, Mitchell R. Vollger, Katherine M. Munson, Tom Walsh, Morgan O. Hamm, Yizi Mao, Andre Lieber, Andrew B. Stergachis (corresponding)"
published: 2024
ingested: 2026-05-13
updated: 2026-10-07
doi: "10.1101/gr.279747.124"
journal: "Genome Research 34:2269–2278"
aliases: ["Bohaczuk 2024", "targeted Fiber-seq", "mosaic Fiber-seq"]
tags: [targeted-Fiber-seq, mosaic-variants, chromatin-impact, DMPK, myotonic-dystrophy, HBG1, Stergachis-lab, UW, CRISPR-Cas9-enrichment, HLS-CATCH, CTCF-footprinting, base-editing, PacBio, FIRE]
entities: ["[[20-Entities/andrew-b-stergachis]]", "[[20-Entities/elliott-g-swanson]]"]
concepts: ["[[fiber-seq]]", "[[chromatin-accessibility]]", "[[pacbio]]", "[[cpg-island]]", "[[allele-specific-methylation]]", "[[enhancer-states]]", "[[structural-variants]]", "[[transcription-factor-motif]]"]
topics: ["[[somatic-mosaicism]]", "[[long-read-sequencing]]", "[[dna-methylation]]"]
---

**Citation:** Bohaczuk et al. (2024) — *Resolving the chromatin impact of mosaic variants with targeted Fiber-seq* — *Genome Research* 34:2269–2278. [DOI](https://doi.org/10.1101/gr.279747.124) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/39653420/)

# Bohaczuk 2024 — targeted Fiber-seq

> Short-read chromatin assays cannot tell which allele an accessible read came from when a variant is present in only some cells, and their <150 bp reads cannot connect a variant to neighbouring regulatory elements. Bohaczuk et al. pair Fiber-seq (m6A stencilling of accessible DNA on intact nuclei) with **CRISPR–Cas9 excision of 100–250 kb loci inside agarose plugs (Sage HLS-CATCH)** and PacBio HiFi sequencing. Each read then carries sequence, CpG methylation, m6A accessibility and nucleosome/TF footprints on the same ≥10 kb molecule, at ~10-fold enrichment over untargeted Fiber-seq. Two case studies show that non-coding variants present in a subset of molecules change chromatin **beyond the element that carries the variant**: (i) somatically unstable **DMPK CTG expansions** in Myotonic Dystrophy 1 (DM1) fibroblasts create a focal ~1 kb hyper-CpG-methylated domain upstream of the repeat, ablate a putative **SIX5 enhancer**, reduce CTCF occupancy at the adjacent insulator and reduce **SIX5 promoter** accessibility, but only in carriers of >1000 repeats; (ii) **adenine base editing** of the BCL11A site in the segmentally duplicated **HBG1/HBG2** promoters in CD34⁺-derived erythroid cells lowers CpG methylation across both promoters and more than doubles HBG1 promoter accessibility.

## Key claims

- **Enrichment and coverage.** Four wells of an HLS-SAGE cassette, each loaded with 0.5–1.5 million m6A-MTase-treated nuclei, were extracted in gel, Cas9-released, eluted by pulsed-field electrophoresis, sheared to ~13 kb, barcoded and multiplexed. On GM04820 lymphoblastoid cells, the eluate was 58% of the mass loaded on one Sequel II SMRT cell and gave a median **101–164× coverage** across three targeted loci (161, 119 and 118 kb), "corresponding to ~20-fold enrichment compared to whole-genome approaches". Across all samples, the median enrichment was **10-fold**.
- **Fiber-to-fiber heterogeneity.** At the *SNRPD2/QPCTL* bidirectional promoter (chr19, Fig. 1F), every fiber had accessible chromatin, but the boundaries of the accessible patch and the position of an internal nucleosome varied between reads. "The precise pattern of accessibility within a promoter can vary quite substantially from fiber to fiber." This locus is a demonstration of heterogeneity, not a DM1 effect.
- **Repeat instability at single-molecule resolution.** In fibroblasts from four symptomatic members of one DM1 pedigree, the first-generation individual had a median pathogenic expansion of **59.5 CTGs** (range 20). Second- and third-generation individuals had **>1000 CTGs**, and individual fibers from one donor differed by almost **2000 repeats**. Reads were haplotype-phased across the 160 kb region (DeepVariant + HiPhase) to separate normal from expanded alleles.
- **Focal, directional hypermethylation.** In generations II/III, expanded haplotypes carried a **~1 kb hyper-CpG-methylated domain upstream of the repeat** that runs to the end of the overlapping CpG island. It begins immediately after the upstream CTCF element and does not include it. CpG methylation downstream of the repeat was unchanged.
- **A putative SIX5 enhancer is silenced.** An accessible element upstream of the repeat (H3K4me1/H3K27ac-positive in ENCODE fibroblasts, in a region previously proposed to hold a *SIX5* enhancer) lies inside the hypermethylated domain. Its accessibility was "largely ablated" on expanded generation II/III haplotypes (**P = 7.3 × 10⁻⁹**, Fisher's exact test with Benjamini–Hochberg FDR).
- **CTCF loss without CTCF-site methylation.** Accessibility of the upstream CTCF element also fell (**P = 3.8 × 10⁻⁹**). By single-molecule footprinting at the CTCF motif, **52%** of normal-haplotype fibers were CTCF-bound against **24%** of expanded generation II/III fibers (**P = 0.010**), with more nucleosome occupancy over the motif. The authors conclude that CpG methylation directly within the CTCF site "is not required" to inhibit CTCF binding, in contrast with in vitro oligonucleotide studies.
- **Long-range effects are specific.** Of the 96 annotated TSSs in the targeted region, only the **SIX5 promoter** lost actuation on expanded generation II/III fibers (**P = 0.028**). The canonical *DMPK* TSS was unchanged, consistent with post-transcriptional mechanisms for reduced *DMPK* mRNA. CpG methylation at the *SIX5* promoter was unchanged, so its reduced accessibility is attributed to loss of the upstream enhancer, not to silencing that spreads from the repeat.
- **A repeat-length threshold.** None of these changes appeared on the generation I allele of ~60 CTGs. The authors suggest the DM1 chromatin phenotype needs a critical repeat number, reached by age-related somatic expansion in adult-onset DM1 or present congenitally with large germline expansions.
- **Base editing is co-occurring on a fiber.** CD34⁺ HSPCs from two healthy donors were transduced with an all-in-one HDAd-ABE8e vector targeting the BCL11A motif at −113 bp of both *HBG1* and *HBG2* (the −113 A>G variant causes hereditary persistence of fetal hemoglobin in the germline), differentiated to erythroid cells and profiled across a 118 kb region from the LCR to 3′HS1. **34% and 32%** of fibers were edited at *HBG1* and *HBG2*. If one promoter on a fiber was edited, the other was much more likely to be edited (**P < 0.00001**), which the authors take to mean that efficiency depends on transduction and ABE expression.
- **Editing opens HBG1 and lowers CpG methylation.** Editing reduced CpG methylation across both promoters. It increased HBG1 promoter accessibility by **>100%** (Fisher P = 0.00030; **0.0033 after FDR**). An element 2.5 kb upstream of *HBG1* rose nominally (P = 0.024; **0.13 after FDR**). The *HBG2* promoter rose a non-significant 36%, which the authors attribute to higher baseline HBG2 accessibility on unedited fibers. Four non-promoter elements within the segmental duplication were co-accessible with the promoters on single molecules, which the authors read as putative *HBG1/HBG2* enhancers.
- **Genome structure found in the same data.** De novo assembly (hifiasm) showed that one CD34⁺ donor carried a rare **γ-globin triplication** on one haplotype. Its reads were removed as a confounder that "would have been largely hidden from short-read-based chromatin methods".

## Methods / evidence

Nuclei were treated with Hia5 m6A-MTase (100 U per million cells, 10 min, 25 °C). Three crRNAs per side flanked each target within a ~3 kb window. Libraries were run on PacBio Sequel II (8M, 30 h movie) or Revio (25M, 24 h). CpG methylation came from Primrose/Jasmine and pb-CpG-tools. m6A and nucleosome calls came from fibertools. Reads with m6A fraction <0.02 or >0.4 were excluded. Accessible elements were called with FIRE v0.0.4 (peaks at min_frac_accessible 0.15). Peak actuation was compared by Fisher's exact test with BH FDR < 5%, and ΔCpG with MethBat. CTCF footprinting classified each fiber at the CTCF core (chr19:45770329–45770342) as accessible-and-bound, accessible-but-unbound or inaccessible. Co-accessibility used a codependency score scaled to −1…+1. Samples: GM04820 LCL; DM1 fibroblast lines GM06076, GM04601, GM04602 and GM04608 from the Coriell NIGMS repository; mobilized CD34⁺ cells from two donors (with O⁶BG/BCNU selection of edited cells in some samples). Data: BioProject PRJNA1125891. Code: github.com/StephanieBohaczuk/Targeted-Fiber-seq.

Weight: a clear proof of concept. The DM1 findings come from **one pedigree of four fibroblast lines**, with one generation I individual as the only "short expansion" comparator, so the repeat-length threshold rests on a single allele. The base-editing results come from **two donors**, and one donor's triplicated haplotype was discarded. Only the *HBG1* promoter survives FDR; the "neighbouring elements" claim in the abstract rests on a nominal P value plus co-accessibility. The "mosaic" variants here are somatic repeat instability within cultured lines and incomplete ex vivo editing, not naturally arising somatic mutations in tissue. (synthesis)

## Limitations

**Authors' own:**
- The DM1 analyses were done in patient-derived fibroblasts; studies in primary patient tissues are needed to test whether a common mechanism links repeat size, somatic instability and chromatin disruption.
- Coverage of the triplicated γ-globin haplotype was insufficient for follow-up analyses, so those reads were excluded.
- The method is shown on cell lines and primary cells; translation to biopsied tissue is anticipated from whole-genome Fiber-seq on tissue nuclei, not tested here.

**Reviewer notes:**
- Targeted Fiber-seq is a bulk assay: it resolves single *molecules* but not single *cells*, so co-occurrence of features on two alleles of the same cell cannot be measured. (synthesis)
- Statistical power is set by ~100–160× fiber coverage per locus; with one family and two donors, effect sizes for weaker elements (e.g., the 2.5 kb upstream *HBG1* element) remain unresolved. (synthesis)
- Mosaicism is modelled, not observed in vivo: the tested variants are a germline repeat with somatic length drift and an engineered edit, so allele fractions and selection differ from natural somatic mosaicism. (synthesis)

## Surprising or load-bearing bits

- **The DM1 lesion is upstream and enhancer-mediated.** Reduced *SIX5* promoter accessibility, with unchanged *SIX5* promoter CpG methylation, points to loss of an upstream enhancer rather than spreading heterochromatin. This reconciles earlier reports that *SIX5* accessibility falls while methylation does not.
- **CTCF can be evicted without methylating its motif**: the first in vivo, single-molecule demonstration that reduced CTCF binding next to the CTG repeat does not need hypermethylation of the overlapping site. Nanopore studies saw variable CTCF-site methylation in DM1 but could not measure occupancy.
- **Accessibility and CpG methylation are correlated but "not interchangeable"** — the paper's own phrasing of a point that bears on any assay using one as a proxy for the other.
- **Segmental duplications become tractable.** The 92.5%-identical *HBG1/HBG2* duplication, with 100% identity over the proximal promoter, cannot be profiled with short reads; long reads assign edits, methylation and accessibility to each paralog.

## Entities mentioned

- [[20-Entities/andrew-b-stergachis]] — senior author; Fiber-seq inventor (patent co-inventor, per the competing-interest statement).
- [[20-Entities/elliott-g-swanson]] — co-author (computational experiments); later led DAF-seq.

## Concepts touched

- [[fiber-seq]] — adds targeted high-molecular-weight enrichment, multiplexing of ≥5 samples per SMRT cell, and CTCF single-molecule footprinting.
- [[chromatin-accessibility]] — haplotype-resolved, per-fiber accessibility over 100+ kb loci; accessibility and CpG methylation dissociate at the *SIX5* promoter.
- [[pacbio]] — HiFi kinetics give 5mC (Jasmine) and m6A (fibertools) from the same reads.
- [[cpg-island]] — the hyper-CpG domain runs to the end of the CpG island overlapping the repeat.
- [[allele-specific-methylation]] — phased ΔCpG between normal and expanded *DMPK* haplotypes, and between edited and unedited *HBG* fibers.
- [[enhancer-states]] — a putative *SIX5* enhancer and four candidate *HBG1/HBG2* enhancers defined by co-accessibility on single molecules.
- [[structural-variants]] — the γ-globin triplication found by de novo assembly, and repeat-length measurement from reads spanning the CTG array.
- [[transcription-factor-motif]] — per-molecule CTCF occupancy at a single motif.

## Connections to other sources

- Extends [[10-Summaries/andrewb-2020-science]] (original whole-genome Fiber-seq) by adding CRISPR targeting and single-motif CTCF footprinting.
- Complements [[10-Summaries/peter-2024-brain-fiberseq]], which runs whole-genome Fiber-seq on human brain tissue; the authors cite tissue Fiber-seq as the basis for expecting targeted Fiber-seq to work on primary tissue.
- Precedes [[10-Summaries/swanson-2025-daf-seq]], which moves from bulk single-molecule to single-cell diploid fiber architectures by replacing m6A with deamination — addressing the bulk-assay limitation noted above. (synthesis)

## Open questions

- Is the ~1 kb hyper-CpG domain a cause or consequence of the CTCF loss, and does it precede somatic expansion beyond the threshold in tissue? The single-allele comparison cannot order these events.
- Does the same enhancer-loss mechanism hold in DM1 muscle, where somatic expansion is largest, rather than in fibroblasts?
- Can targeted Fiber-seq detect the chromatin effect of a naturally occurring somatic SNV at low allele fraction (e.g., a few percent), where per-locus fiber counts would limit power? (synthesis)

## Related

- [[10-Summaries/andrewb-2020-science]]
- [[10-Summaries/peter-2024-brain-fiberseq]]
- [[10-Summaries/swanson-2025-daf-seq]]
- [[20-Entities/andrew-b-stergachis]]
- [[30-Concepts/fiber-seq]]
- [[40-Topics/somatic-mosaicism]]
- [[40-Topics/long-read-sequencing]]
