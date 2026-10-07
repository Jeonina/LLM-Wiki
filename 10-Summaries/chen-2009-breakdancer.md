---
type: summary
title: "Chen et al. 2009 — BreakDancer: an algorithm for high-resolution mapping of genomic structural variation"
source: "[[00-Sources/papers/BreakDancer_ an algorithm for high-resolution mapping of genomic structural variation]]"
source_kind: paper
author: "Ken Chen, John W. Wallis, Michael D. McLellan, David E. Larson, Joelle M. Kalicki, Craig S. Pohl, Sean D. McGrath, Michael C. Wendl, Qunyuan Zhang, Devin P. Locke, Xiaoqi Shi, Robert S. Fulton, Timothy J. Ley, Richard K. Wilson, Li Ding, Elaine R. Mardis"
published: 2009-08-09
ingested: 2026-10-07
doi: "10.1038/nmeth.1363"
journal: "Nature Methods 6:677–681"
tags: [BreakDancer, structural-variants, paired-end-mapping, read-pair, indels, inversions, translocations, Kolmogorov-Smirnov, Poisson, AML, 1000-Genomes]
entities: ["[[ken-chen]]"]
concepts: ["[[structural-variants]]", "[[copy-number-variation]]", "[[read-alignment]]", "[[sequencing-depth-and-coverage]]"]
topics: ["[[mosaic-variant-calling]]", "[[computational-methods]]", "[[hematopoietic-malignancies]]"]
---

**Citation:** Chen et al. (2009) — *BreakDancer: an algorithm for high-resolution mapping of genomic structural variation* — *Nature Methods* 6:677–681. [DOI](https://doi.org/10.1038/nmeth.1363)

# Chen 2009 — BreakDancer

> BreakDancer was an early answer to the question of how to call structural variants from short-insert Illumina paired-end reads. It has two complementary algorithms. **BreakDancerMax** clusters *anomalously mapped read pairs* (ARPs: wrong separation or orientation) and scores each cluster with a Poisson model. It calls five SV classes: deletions, insertions, inversions, and intra- and inter-chromosomal translocations. **BreakDancerMini** takes the *normally* mapped pairs that Max ignores and runs a sliding-window Kolmogorov–Smirnov test on insert-size distributions. This catches 10–100 bp indels that sit below the ARP separation threshold. Combined, they span indels from 10 bp to 1 Mb. Library- and sample-level p-values are pooled with Fisher's method, so trio, population and tumour–normal designs gain power.

## Key claims

- **Simulation** used Venter chr17, with 844 SVs of 20–7,953 bp, 50-bp reads, 200 ± 20 bp inserts and 100× physical coverage.
  - Only 365 of the 844 variants (43.2%) had ≥2 flanking ARPs. BreakDancerMax found 324 of these (89%) at a 1.48% false-positive rate.
  - Of 214 detected deletions, 203 (95%) were typed correctly with accurate sizes (r = 0.92). Of 109 insertions, 72 (66%) were typed correctly, with poorer size estimates (r = 0.65).
  - BreakDancerMini alone found 543 variants (64.3%) at a 7.3% false-positive rate, 75.0% of them shorter than 60 bp. The merged set found 621 of 844 (74%) at a 9.1% false-positive rate.
  - With 10–20 bp indels added (1,897 variants), Max alone found 24% and Max plus Mini 68.0% (false-positive rate 10.3%).
- **The Poisson confidence score beats raw ARP counts.** It separates variants with identical ARP support and reduces dependence on the separation threshold.
- **Comparison with VariationHunter and MoDIL** used the NA18507 Yoruban genome (MAQ maps).
  - BreakDancer recovered 59/92 (64.1%) large fosmid deletions, comparable to VariationHunter.
  - The authors state that BreakDancerMini had "substantially higher sensitivity and specificity" than VariationHunter or MoDIL.
  - Mini's size estimates correlated with known deletion/insertion polymorphisms at r > 0.8.
  - The two competitors used a different mapper (MrFast), so this is not a mapper-controlled comparison.
- **AML tumour/normal** (cytogenetically normal AML; 21× haploid coverage each):
  - At Q ≥ 60, the joint six-library run called 7,087 SVs. 46.4% of the deletions overlapped DGV, and 37 of 116 array-detected inherited CNVs (31.9%) were recovered.
  - Tumour-only calls gave 223 putative somatic SVs.
  - PCR validation of 167 indels: 110 validated, but in **both** tumour and normal, so as germline. 31 failed and 26 were no-calls, giving a 78% validation rate (89% at Q ≥ 80).
  - No putative somatic indel validated as tumour-specific in that PCR set.
- **Local assembly is a confirmation tool, not a sensitivity tool.** Assembly (Velvet plus Phrap) had a low false-positive rate (6 of the variant calls, 6%, failed to validate). Its false-negative rate was high: 26 of 53 "nonvariant" calls (49%) actually validated.
- **1000 Genomes trios, chromosome 5:**
  - CEU child NA12878 (~15× physical coverage): 125 deletions called, 63% overlapping DGV. Joint analysis of the trio raised recovery of known deletions from 25–35% to 40–57%.
  - YRI child NA19240 (50–70×): 246 deletions called.
  - About 72–77% of each parent's deletions were also called independently in the child, against 31–37% overlap between unrelated families.
- **Analytic detectability model.** With 200 bp inserts (s.d. 20), indels shorter than about 40 bp are hard to detect from ARPs. Deletions over 60 bp plateau at around 30× and those over 100 bp at around 20×. Insertions over 100 bp cannot be detected, because they are capped by insert size and read length.

## Methods / evidence

**BreakDancerMax:**
- Classifies each confidently mapped pair into one of six types (normal, deletion, insertion, inversion, intra- or inter-chromosomal translocation). It uses separation, orientation and the empirical per-library insert-size distribution.
- Finds regions anchoring excess ARPs, and links regions joined by ≥2 ARPs.
- Scores each event by a Poisson tail probability given anchoring-region size, ARP count and genome-wide ARP rate. Libraries are combined by Fisher's χ² with 2m degrees of freedom and converted to a Phred-like Q.

**BreakDancerMini:**
- Slides a window of μ + 3σ − 2l along the genome and computes two-sample KS statistics (D ≥ 2.3) against the genome-wide insert-size ECDF, separately for each strand.
- Opposite-orientation anomalous regions must support the same small indel.
- It makes no normality assumption about inserts. This matters because some AML libraries were visibly non-Gaussian.

**Validation:** PCR plus Sanger sequencing on the AML tumour and matched skin normal. Mapping was done with MAQ 0.7.1 to NCBI build 36. The software is written in Perl and takes 3–5 h per human chromosome at ~50×.

Weight: a well-validated methods paper for its era, with honest reporting of false-positive rates and of the validation outcome. The key limits are 36–50 bp reads, MAQ alignment and short inserts. Inversion and translocation validation is thin (4 of 13 inversions and 2 of 6 intra-chromosomal translocations validated with high-quality data). It is bulk germline/somatic SV calling with no single-cell component.

## Surprising or load-bearing bits

- **Most simulated SVs are invisible to read-pair signal.** Only 43.2% of the known chr17 variants had ≥2 ARPs at 100× physical coverage. The ceiling is set by the library geometry (insert-size s.d. versus variant size), not by the caller. (synthesis)
- **The somatic set did not survive validation as somatic.** All validated indels were present in tumour and normal alike. Tumour-only read-pair calls in this design were dominated by germline variants missed in the normal, a recurring lesson for any somatic SV caller that relies on unmatched depth. (synthesis)
- **Pooling across related genomes adds sensitivity** for shared variants. This is the same logic later used for population-scale SV calling. (synthesis)
- 3 insertions looked like ancestral alleles (closer to chimp than to the human reference). At least 4 inherited deletions carried 10–20 bp (A+T)-rich insertions at the breakpoints, which the authors attribute to transposon insertion.

## Concepts touched

- [[structural-variants]] — a read-pair (end-sequence profiling) detection approach covering the 10 bp–1 Mb size range, with an analytic model of detectability versus insert size and coverage.
- [[copy-number-variation]] — deletion calls are benchmarked against DGV and array CNVs. The authors point to read-depth integration as future work.
- [[read-alignment]] — calls depend on mapping-quality thresholds (MAQ MQ > 10 vs. > 35 changes recall and DGV concordance).
- [[sequencing-depth-and-coverage]] — physical coverage, not sequence coverage, governs ARP-based sensitivity.

## Connections to other sources

- SV landscape and why short reads miss SVs: [[eichler-2007-completing-sv-map]]. BreakDancer is one of the paired-end ESP-style methods that followed the fosmid-based maps.
- Long-read SV calling as the later alternative: [[liu-2025-nanopore-lscc-svs]]. In single cells, [[sanders-2020-sctrip]] (Strand-seq-based SV discovery) addresses the same variant classes without paired-end insert anomalies.
- SV consequences for 3D genome structure: [[spielmann-2018-sv-3d-genome]], [[lupianez-2015-tad-disruption]].
- Same-era alignment tooling: [[li-2009-samtools]], [[li-2009-bwa]]. BreakDancer here runs on MAQ (Li, Ruan & Durbin 2008) map files, and the acknowledgements thank H. Li for methodology discussions.
- [[ken-chen]] (first author here) is the same name as the MD Anderson PI behind [[wang-2021-medalt]]. The clipping gives no affiliations, so this identity is not confirmed from the source.

## Open questions

- Inversions and translocations remained hard to validate, often overlapping tandem or inverted repeats. Longer reads and inserts are suggested but not tested.
- The authors say read-depth integration should help, but "an effective integration method is yet to be discovered."
- The Q score is "not necessarily a Phred quality score". Calibration of SV confidence to true error probability remains open.
- How well do read-pair ARP methods transfer to single-cell WGA data, where chimeras and uneven coverage generate anomalous pairs without true SVs? This is not addressed here. (synthesis)

## Related

- [[structural-variants]] · [[copy-number-variation]] · [[40-Topics/mosaic-variant-calling]]
