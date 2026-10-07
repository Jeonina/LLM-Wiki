---
type: summary
title: "Macaulay et al. 2016 — G&T-seq protocol: parallel sequencing of single-cell genomes and transcriptomes"
source: "[[00-Sources/papers/Separation and parallel sequencing of the genomes and transcriptomes of single cells using G&T-seq]]"
source_quality: full
source_sha256: "c71f0e7d7c597aa789da2a256e3cd3cc490c4e8b680bb9808aebd067ca2ce0de"
source_kind: paper
author: "Iain C. Macaulay, Mabel J. Teng, Wilfried Haerty, Parveen Kumar, Chris P. Ponting, Thierry Voet (corresponding)"
published: 2016-09-29
ingested: 2026-05-18
updated: 2026-10-07
doi: "10.1038/nprot.2016.138"
journal: "Nature Protocols"
tags: [G&T-seq, single-cell-multiomics, WGA, Smart-seq2, oligo-dT-bead, PicoPLEX, MDA, MAPD, protocol, Voet-lab]
entities: ["[[20-Entities/thierry-voet]]"]
concepts:
  - "[[30-Concepts/gt-seq]]"
  - "[[30-Concepts/scwga]]"
  - "[[30-Concepts/scwga-chemistries]]"
  - "[[30-Concepts/mda]]"
  - "[[30-Concepts/malbac]]"
  - "[[30-Concepts/allele-dropout]]"
  - "[[30-Concepts/copy-number-variation]]"
  - "[[30-Concepts/structural-variants]]"
  - "[[30-Concepts/tn5-tagmentation]]"
  - "[[30-Concepts/scrna-seq]]"
  - "[[30-Concepts/bisulfite-sequencing]]"
  - "[[30-Concepts/dr-seq]]"
topics:
  - "[[40-Topics/single-cell-multiomics]]"
  - "[[40-Topics/whole-genome-amplification]]"
  - "[[40-Topics/scdna-seq]]"
---

**Citation:** Macaulay et al. (2016) — *Separation and parallel sequencing of the genomes and transcriptomes of single cells using G&T-seq* — *Nature Protocols*. [DOI](https://doi.org/10.1038/nprot.2016.138) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/27684873/)

# Macaulay et al. 2016 — G&T-seq Nature Protocols version

> This is the step-by-step bench and analysis protocol for G&T-seq, first described in [[10-Summaries/macaulay-2015-gt-seq]]. A single cell is lysed in guanidine-based Buffer RLT Plus. Its polyA(+) mRNA is pulled out on streptavidin beads carrying a biotinylated, Smart-seq2-tailed **oligo-dT30VN** primer. The supernatant holding the gDNA, plus every wash, is pooled into a second plate. The mRNA is then reverse-transcribed and amplified **on the beads** by a modified Smart-seq2, and the gDNA is concentrated on AMPure beads and amplified by **any WGA kit** (PicoPLEX or GenomiPhi MDA are given in full). Both products go into Nextera XT libraries. The protocol is written for 96-well plates on off-the-shelf liquid handlers (BioMek FXP before amplification, Zephyr after), and also includes a full analysis pipeline: BWA → 500-kb-bin logR copy number with a **MAPD QC gate**, GATK SNV calling, TopHat2/HTSeq/DESeq2 expression, and a chromosome-level expression-vs-copy-number check for aneuploidy. It contains no new biological experiment. Its value is the specific operating parameters (volumes, ratios, QC thresholds, sequencing depth) and the authors' stated limits of the method.

## Key claims

- **Throughput.** Done manually, paired DNA and RNA libraries from **8 single cells take ∼3 d**; with a liquid-handling robot, **96 cells** take the same time. The day plan is: day 1 cell prep through cDNA PCR, day 2 purification, QC and WGA, day 3 tagmentation and pooling, days 4–7 sequencing (∼2 d).
- **Separation step.** Cells go into **2.5 μl RLT Plus**. No RNase inhibitor is needed, because guanidine isothiocyanate inactivates RNases. Plates are stable at −80 °C for >1 month and have been processed after >6 months. 10 μl of oligo-dT beads are mixed in at 2,000 r.p.m. for 20 min. The gDNA supernatant is moved to a "gDNA collection" plate, followed by two 10-μl washes and a final 5-μl tip rinse, **all with the same tip**, to limit gDNA loss. The gDNA well ends up holding 38.5 μl.
- **RT differs from Smart-seq2 in two ways.** There is **no denaturation step** before RT, and RT runs with **constant mixing** so the beads do not settle. The authors state that G&T-seq transcriptomes match Smart-seq2 in transcripts detected, full-length coverage, GC distribution and spike-in detection, and conclude that separation adds no extra bias (citing the 2015 paper).
- **WGA choice depends on the readout.** The authors have used PicoPLEX, MDA and MALBAC on G&T-seq DNA and are "unaware of a commercially available WGA kit that would be incompatible". **PicoPLEX is preferred for copy number**; **MDA for SNVs and SVs**. Both kits typically yield >0.5 μg DNA. PicoPLEX products peak at 300–2,000 bp, MDA products at 1–20 kb.
- **Library choice depends on the readout too.** Nextera XT is enough for low-coverage copy-number profiling of PicoPLEX DNA and for cDNA. For SNV or SV work, the authors recommend **ligation-based libraries** (TruSeq, Kapa HyperPlus) on MDA DNA, and **HiSeq X** for genome-wide SNVs.
- **Sequencing depth.** 96 libraries over two HiSeq 2500 rapid-mode lanes (PE100) give **∼4–6 million reads per cell**, for both genome and transcriptome (Anticipated results). The authors advise against shallower genome sequencing unless only whole-chromosome changes are expected.
- **Copy-number pipeline.** Trim 23 bases from Nextera reads. Map with BWA 0.6.2 (aln/sampe). Keep unique reads (XT:A:U) and remove duplicates with Picard. Exclude cells with ≤2% mapped reads. Count reads in bins of **500,000 uniquely mappable positions**. Compute logR = log2(bin count / genome-wide median), apply loess GC correction, segment by piecewise constant fitting, and convert as **CN = 2^logR · ψ**, where ψ is the cell's average ploidy. Ginkgo and SNS can be used unmodified instead.
- **MAPD as the DNA QC gate.** MAPD is the median of |logR(bin k+1) − logR(bin k)|. Cells are discarded at **MAPD > 0.6 for PicoPLEX** or **> 2 for MDA**. MDA profiles that pass MAPD < 2 still separate HCC38 cancer cells from matched HCC38-BL lymphoblastoid cells, but PicoPLEX gives "substantially less-noisy" copy number.
- **RNA QC gate.** Trim with Trim Galore (q20), map with TopHat2, count with HTSeq (intersection-strict, unstranded, exon) and normalise with DESeq2. Cells with **fewer than 3,500 genes at TPM ≥ 1** were excluded in the HCC38/HCC38-BL analysis, and both cutoffs can be tuned. Successful cDNA runs 0.5–2 kb with a peak at ∼1–1.5 kb on a Bioanalyzer. Failures are mostly degraded RNA or empty wells.
- **DNA–RNA integration.** Gene models are concatenated per chromosome or arm and scored as RPKM. Each cell is median-centred against a control line with the same genetic background. Aneuploid cells appear as outliers, with higher chromosome-wide expression for gains and lower for losses, which is then compared with the DNA copy-number profile.
- **Comparison with other methods.** [[10-Summaries/dey-2015-dr-seq]] avoids physically separating DNA and RNA, so it may lose less material and could suit microfluidics. But its CEL-seq 3′-end WTA cannot see splice variants, fusion transcripts or most expressed SNVs. Its WGA is fixed to a modified MALBAC, and it needs exons masked *in silico* to call copy number. Li et al. 2015 also separated DNA and RNA physically but looked only at SNVs. Han et al. 2014 used custom microfluidics for targeted readouts. The authors' central argument is that **none of these had been shown to automate**.
- **Extensions.** The protocol also works on pools of 10–100 cells. Full-length cDNA can be read on PacBio for isoforms and fusions, and a fusion transcript can be traced to its causal rearrangement in the same cell's DNA. Either product can be screened by qPCR or used for exome or targeted sequencing. The separated gDNA can go into bisulfite sequencing, and the authors cite their own scM&T-seq (Angermueller et al. 2016, *Nat Methods*) as built on the G&T-seq platform.

## Methods / evidence

This is a protocol paper with 104 numbered steps, buffer recipes, oligo sequences, robot deck layouts (Supplementary Figs. 1–2) and a troubleshooting table (Table 1, not captured in the clipping). The core reagents are Dynabeads MyOne Streptavidin C1 with a biotin-TEG oligo-dT30VN carrying the Smart-seq2 ISPCR handle, a LNA TSO, SuperScript II, KAPA HiFi, a 1:1 AMPure cleanup for cDNA and **0.65:1 AMPure** for gDNA concentration, and a 1:0.6 cleanup for the pooled library. ERCC spike-ins are added at 1 μl of a ∼1:1,000,000 dilution after cell collection, and should be titrated per cell type so they do not use up sequencing capacity. Each plate should include multicell (10–50 cell) positive controls and empty-well negative controls. Cell types run so far are mouse blastomeres, HCC38 and HCC38-BL, human iPSC-derived neurons, and primary mouse and human cells (unpublished).

Weight: the bench parameters and QC thresholds are authoritative as the developers' own recipe. Performance claims (no extra RNA bias, WGA comparable to standalone WGA, no megabase dropouts) are **asserted with citation to the 2015 Nat Methods paper** rather than shown with new data here. The only data shown are representative Bioanalyzer traces (Fig. 2), six copy-number profiles (Fig. 3) and a genes-vs-TPM curve (Fig. 4). The analysis stack (BWA aln 0.6.2, GATK UnifiedGenotyper/IndelRealigner, TopHat2, GRCh37) was standard in 2016 but is now dated. (synthesis)

## Limitations

**Authors' own:**
- The WTA arm captures only **polyA(+) mRNA**. PolyA(−) RNAs are lost, and **strand information is lost** during WTA.
- The WGA arm has the usual single-cell WGA artefacts: GC bias, allelic dropout, polymerase base errors and chimeric molecules.
- Physical separation of mRNA and gDNA **"may contribute further to the problem of allelic dropout"**. The authors report no megabase-scale segment dropouts in normal human and mouse cells, and say genome readouts are comparable to standalone WGA.
- DR-seq's single-tube design may lose less material than G&T-seq's gDNA transfer.
- Pooling 96 libraries without per-library quantification can skew representation. Exact depth matching needs per-library quantification.
- Integrating the DNA and RNA data "requires a high level of bioinformatics expertise".

**Reviewer notes:**
- The protocol never quantifies how much gDNA is lost in the transfer and wash steps. The allelic-dropout penalty of separation is acknowledged but not measured here. (synthesis)
- The only integration analysis given is chromosome- or arm-level dosage. Integrating SNVs with expression, or the allele-specific expression mentioned in the introduction, is not given step by step. (synthesis)
- Throughput is plate-based (96 per run), which is a different scale from the droplet and combinatorial-indexing methods that came later. The "high-throughput" framing is relative to manual 2016 methods. (synthesis)

## Surprising or load-bearing bits

- **Same-tip gDNA transfer** is the step the authors credit with limiting DNA loss. It is a small detail that the whole method depends on.
- **Two separate MAPD cutoffs** (0.6 PicoPLEX, 2 MDA) give concrete, chemistry-specific numbers for single-cell copy-number QC, and show how much noisier MDA copy number is.
- **Copy number from expression alone**: median-centring chromosome-wide RPKM against a karyotypically normal control of the same genetic background can call aneuploidies from the RNA arm. The DNA arm then validates these calls rather than being the only source. (synthesis)
- The authors present DR-seq's single-tube design as a possible advantage in material retention, which is a fair concession and not only a comparison in G&T-seq's favour.

## Entities mentioned

- [[20-Entities/thierry-voet]] — corresponding author; funded via Wellcome Trust, FWO and KU Leuven; discloses co-inventorship on single-cell haplotyping and genotyping-by-sequencing patent applications.

## Concepts touched

- [[30-Concepts/gt-seq]] — the reference bench protocol and QC thresholds.
- [[30-Concepts/scwga]] / [[30-Concepts/scwga-chemistries]] — WGA-agnostic design; PicoPLEX for copy number, MDA for SNVs and SVs.
- [[30-Concepts/mda]] — GenomiPhi V2; 1–20 kb products; noisy copy number (MAPD cutoff 2).
- [[30-Concepts/malbac]] — shown to work on G&T-seq DNA; DR-seq's fixed WGA.
- [[30-Concepts/allele-dropout]] — separation named as a possible extra source.
- [[30-Concepts/copy-number-variation]] — 500-kb-bin logR, GC loess, piecewise constant segmentation, MAPD.
- [[30-Concepts/structural-variants]] — MDA plus ligation libraries recommended for SVs.
- [[30-Concepts/tn5-tagmentation]] — Nextera XT for both cDNA and PicoPLEX DNA.
- [[30-Concepts/scrna-seq]] — Smart-seq2 on beads; 3,500 genes at TPM ≥ 1 QC.
- [[30-Concepts/dr-seq]] — the one-pot alternative; G&T-seq authors list its trade-offs (material retention vs 3′-only RNA, fixed MALBAC, exon masking).
- [[30-Concepts/bisulfite-sequencing]] — separated gDNA can go into bisulfite sequencing (scM&T-seq).

## Connections to other sources

- Protocol companion to [[10-Summaries/macaulay-2015-gt-seq]]. All performance claims point back to it.
- Contrasted with [[10-Summaries/dey-2015-dr-seq]] (3′ CEL-seq, fixed MALBAC, exon masking). Later relatives are [[10-Summaries/hou-2016-sctrio-seq]] and [[10-Summaries/clark-2018-scnmt-seq]].
- The bisulfite extension (scM&T-seq, Angermueller 2016, no wiki summary yet) applies [[10-Summaries/smallwood-2014-natmethods]] scBS-seq to the separated gDNA.
- Copy-number tools named as drop-in alternatives: Ginkgo ([[10-Summaries/garvin-2015-natmethods]]) and the SNS/Baslan pipeline, which descends from [[10-Summaries/navin-2011-sns-tumor-evolution]].
- WGA trade-off citations: [[10-Summaries/hou-2015-wga-comparison]], [[10-Summaries/huang-2015-scwga-review]]. For MALBAC chemistry see [[10-Summaries/chenghang-2012-science]] and the review chapter [[10-Summaries/zong-2017-malbac-protocol]].
- Field context: [[10-Summaries/macaulay-2014-plosgenet]] (same authors' review).

## Open questions

- How much gDNA, and how much allelic dropout, does the separation step actually cost relative to standalone WGA of the same cell type? This is asserted to be comparable but not measured here. (synthesis)
- Would replacing the 2016 analysis stack (BWA aln, GATK3 UnifiedGenotyper, TopHat2) with current tools change the recommended MAPD or gene-count cutoffs? (synthesis)

## Related

- [[30-Concepts/gt-seq]] · [[40-Topics/single-cell-multiomics]] · [[40-Topics/whole-genome-amplification]] · [[30-Concepts/scwga]]
- [[10-Summaries/macaulay-2015-gt-seq]] · [[10-Summaries/dey-2015-dr-seq]] · [[10-Summaries/hou-2016-sctrio-seq]] · [[10-Summaries/clark-2018-scnmt-seq]]
