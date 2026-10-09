---
type: summary
title: "Terekhanova et al. 2026 — Reactivation of a TAL1 progenitor cell enhancer region by non-coding somatic variants in T-lineage acute lymphoblastic leukemia"
source: "[[00-Sources/papers/Reactivation of a TAL1 progenitor cell enhancer region by non-coding somatic variants in T-lineage acute lymphoblastic leukemia.pdf]]"
source_quality: full
source_sha256: "1632c86fdc4c1c5a702db908a26caae5c30bd4e4869ecb1d531a55f7a21823ff"
source_kind: paper
author: "Nadezhda V. Terekhanova, Xiaolong Chen, Kin-Hoe Chow, Yu Liu, Ying Shao, Li Dong, … , David T. Teachey, A. Thomas Look (co-corresponding), Jinghui Zhang (co-corresponding)"
published: 2026-05-06
ingested: 2026-10-09
doi: "10.64898/2026.05.03.722504"
journal: "bioRxiv preprint"
tags: [T-ALL, TAL1, noncoding-somatic-variants, enhancer-reactivation, neo-enhancer, internal-tandem-duplication, indels, MYB, GATA3, RUNX1, allele-specific-expression, H3K27ac, H3K27me3, haplotype-phasing, Iso-Seq, alternative-promoter, PDX, AlphaGenome, variant-effect-prediction, St-Jude, preprint]
entities: []
concepts: ["[[variant-effect-prediction]]", "[[sequence-to-function-model]]", "[[cis-regulatory-element]]", "[[enhancer-states]]", "[[transcription-factor-motif]]", "[[chip-seq]]", "[[atac-seq]]", "[[structural-variants]]", "[[long-read-sequencing]]", "[[hematopoietic-differentiation]]", "[[chromatin-loop]]"]
topics: ["[[40-Topics/sequence-models-and-foundation-models]]", "[[40-Topics/hematopoietic-malignancies]]", "[[40-Topics/cancer-clonal-evolution]]", "[[histone-modifications]]"]
---

**Citation:** Terekhanova et al. (2026) — *Reactivation of a TAL1 progenitor cell enhancer region by non-coding somatic variants in T-lineage acute lymphoblastic leukemia* — *bioRxiv preprint* (posted 6 May 2026). [DOI](https://doi.org/10.64898/2026.05.03.722504)

# Terekhanova 2026 — TAL1 downstream enhancer I and AlphaGenome

> This St. Jude / Dana-Farber study looks at **somatic noncoding variants in pediatric T-ALL** at *TAL1* "downstream enhancer I", a region ~29 kb downstream of the *TAL1* promoter. It is mutated in 25 of 391 curated TAL1 T-ALLs (6%). The variants are **complex indels**, which often create de novo MYB binding sites, and **internal tandem duplications (ITDs, 79 bp to 10.5 kb)**. Two patient-derived xenografts (one indel, one ITD) were profiled with ChIP-seq, ATAC-seq, Hi-C, RNA-seq and PacBio Iso-Seq. On the mutant haplotype, the region binds MYB, GATA3 and RUNX1, carries H3K27ac, and drives the **short *TAL1* isoform from a promoter in exon 4**. The other haplotype carries H3K27me3. The region overlaps a +29 ATAC peak in normal HSCs and progenitors, so the authors call this **reactivation of a progenitor enhancer**, not creation of a neo-enhancer. The authors then run **AlphaGenome** ([[avsec-2026-alphagenome]]) on variants from 122 patients in all four *TAL1* enhancer regions. Avsec et al. had tested the upstream, intron and downstream-II variants but not enhancer I, so enhancer I is an unseen test. AlphaGenome scored enhancer-I variants significantly lower, although measured *TAL1* expression was similar. It also did not predict the exon-4 short-isoform transcription or the H3K27ac pattern seen in the xenografts. The authors conclude that experimental data are still needed and that the model misses unannotated alternative transcription starts.

## Key claims

- **Prevalence after manual curation.** 404 TAL1-altered T-ALLs from the Polonen et al. cohort of 1,309 WGS samples were curated down to 391. Of these, 223 (57%) had STIL-TAL1 deletion, 58 (15%) upstream-enhancer indels, 42 (11%) translocations, 28 (7%) intron-enhancer SNVs, 25 (6%) downstream-enhancer-I alterations and 15 (4%) downstream-enhancer-II alterations. Re-review of raw WGS reclassified every enhancer-I variant as either an ITD (17 samples) or an indel (8 samples).
- **Variant structure.** Enhancer-I indels are spread over a 103 bp interval rather than a single hotspot. The ITDs range from 79 to 10,520 bp, and their minimum overlap falls in the same interval. 12 of 17 ITDs are under 200 bp, and 3 are over 2 kb. The surrounding 141 bp of reference sequence already holds three MYB, four GATA3, one RUNX1 and one TAL1 binding sites. Six of eight indels create a de novo MYB site. Only 2 of 17 ITDs (12%) do so, at the junction, and the index ITD case is not one of them.
- **Index cases.** SJTALL002048 carries a complex indel: double substitution chr1:47,669,401 TA>GG plus an 18 bp deletion, which creates a de novo MYB site and removes a reference GATA3 motif. Its *TAL1* level is 7.35 TPM. SJALL015708 carries a 2.4 kb ITD and has 3.97 TPM.
- **Mono-allelic, short-isoform expression.** Six heterozygous SNPs in the xenograft and five in the patient sample were biallelic in DNA but mono-allelic in RNA. Iso-Seq detected only *TAL1*-short (exons 4–6) in both xenografts, while Jurkat expresses both long and short isoforms. Transcription starts near the previously described exon-4 alternative promoter.
- **Mutant-allele binding.** In the indel xenograft, the indel allele accounted for 77% of MYB ChIP reads, 78% of GATA3 reads and 88% of ATAC reads. H3K27ac was 70% mutant, but coverage was too low to test. MYB, GATA3 and RUNX1 co-occupied the region in the ITD case. Only MYB and GATA3 were bound in the indel case, so RUNX1 co-binding is not always required.
- **Haplotype-split chromatin.** Phasing 60 heterozygous SNPs in the indel case showed H3K27ac enriched on Hap1 at enhancer I (5 consecutive significant SNPs), at enhancer II and at exon 4. H3K27me3 was enriched on Hap2, and RNA matched Hap1. So the co-existing active and repressive peaks are separate allelic states.
- **Enhancer–promoter contact.** Public CD34+ capture Hi-C shows contact between enhancer I and the exon-4 promoter, but not the exon-1 promoter. Xenograft Hi-C shows enriched contact between exon 4 and the downstream region that is absent in DND41 (TAL1-negative), though Hi-C resolution cannot separate enhancer I from enhancer II.
- **Reactivation model.** Enhancer II matches the known +19/20/21 stem-cell enhancer, and enhancer I overlaps the +29 progenitor ATAC peak. Both are open in HSC/MPP/LMPP/CLP and closed in CD4/CD8 T cells. The upstream and intron enhancers have no ATAC peak in progenitors, so those are true neo-enhancers.
- **Clinical and molecular features.** 22 of 25 enhancer-I cases (88%) are of the TAL1 DP-like subtype (Fisher FDR = 8.94 × 10⁻⁵). The group is enriched for *CCND3* mutations (FDR < 0.05), with marginal enrichment for *FBXW7*, *MYC* and *MYB*. The authors found 73 up- and 10 down-regulated DEGs, with *EPHA3* the top hit (FDR = 3.5 × 10⁻¹¹).
- **AlphaGenome under-predicts enhancer I.** The score was the predicted *TAL1* expression change in CD34+ common myeloid progenitors (CL:0001059, the ontology Avsec et al. used). Enhancer-I variants scored significantly lower than upstream and enhancer-II variants (Wilcoxon P = 3.32 × 10⁻⁷). Measured *TAL1* RNA did not differ between these groups (P = 0.35). The gap held with indels alone (103 patients), which are closer to the 1–20 bp variants used in AlphaGenome's distillation training.
- **Recurrent variants get one score, but expression varies.** All 28 intron-enhancer cases carry the same SNV (chr1:47,696,311 C>T, hg38) and receive one score, 0.04. Measured *TAL1* expression varied across these patients, and the same held for recurrent variants in the other regions. The authors take this as a sign that factors beyond the variant shape *TAL1* level.
- **Predicted tracks miss the mechanism.** For Jurkat (upstream-enhancer insertion), predicted RNA-seq and H3K27ac tracks agreed well with measured data at exons 1 and 4. For both enhancer-I xenografts, predicted tracks showed no exon-4 transcription start and no matching H3K27ac. The indel case had the highest predicted score among enhancer-I variants (it ranks 3rd in measured expression) and did predict activation. The ITD case scored a low positive 0.08, with alternating gain and loss across the gene body.
- **Authors' conclusion about the model.** AlphaGenome does not predict enhancer-I-driven *TAL1* expression or the short isoform. This "emphasizes the importance of experimental validation". A likely cause is that GENCODE, the annotation used for AlphaGenome's evaluation, does not include the short isoform. Adding full-length transcriptome data to training could help.

## Methods / evidence

Two pediatric T-ALL xenografts came from the COG AALL0434 trial and were grown in NSG mice. Jurkat (TAL1+, upstream-enhancer insertion) and DND41 (TAL1−) served as cell-line controls. Assays: ChIP-seq for H3K27ac, H3K27me3 and MYB (40 M cells; four replicates) and for GATA3 and RUNX1 (Diagenode TF kit); ATAC-seq (Buenrostro protocol); in situ Hi-C (MboI, two replicates per xenograft); PacBio Iso-Seq (Sequel/Sequel IIe); and RNA-seq. Data were aligned to GRCh37-lite. Allelic counts used bam-readcount and indelPost for complex-indel reads, with two-sided binomial tests and BH FDR. Phasing used GATK HaplotypeCaller and SHAPEIT4 with the 1KG high-coverage panel. Motifs were scanned with FIMO against JASPAR2024 and HOCOMOCO v13. Cohort analyses reused Polonen et al. WGS calls and RNA-seq TPM for 1,335 T-ALLs. Normal references were Corces 2016 sorted-cell ATAC, Cordes 2022 bone-marrow and thymus scRNA-seq, and CD34+ capture Hi-C.

AlphaGenome was run through the public API on hg38 REF/ALT from Polonen Table S14 for 122 patients. These were 24 enhancer I (16 ITDs, 8 indels; the >10 kb ITD excluded), 14 enhancer II (3 ITDs, 11 SNVs or indels), 28 intron SNVs and 56 upstream indels. The score was `tal1_diff_in_cd34`. The comparison is group-level: predicted score per variant against measured patient *TAL1* TPM. Track-level comparisons are qualitative, in figures, for Jurkat and the two xenografts.

Weight: the mechanism rests on two xenografts with deep multi-omics plus cohort-level annotation. There is no reporter assay or genome editing of the enhancer-I variants, so causality rests on allelic imbalance, motif creation and correlation. The AlphaGenome test is a clean out-of-distribution check, because enhancer I was not in Avsec et al.'s showcase. It is also small (24 enhancer-I patients) and uses a myeloid-progenitor cell context. (synthesis)

## Limitations

**Authors' own:**
- Allele-specific expression could not be tested in the ITD case, which lacks heterozygous SNPs at *TAL1*. Phasing was possible only for the indel case (60 vs 2 heterozygous SNPs).
- Mutant-allele TF binding could not be measured in the ITD case, because the junction is ~400 bp from the bound region and creates no new site.
- H3K27ac mutant-allele enrichment (70%) could not be tested for significance because coverage was too low.
- The 22 kb distance means a direct enhancer–promoter link was not established. Hi-C resolution cannot separate enhancer I from enhancer II.
- Recurrent variants show variable expression despite identical predictions, so other factors contribute to *TAL1* level.
- The short *TAL1* isoform is missing from GENCODE, which may explain AlphaGenome's miss. ITDs are larger than the 1–20 bp variants in AlphaGenome's distillation training, which is why an indel-only check was also run.

**Reviewer notes:**
- AlphaGenome was run in CD34+ CMP tracks, not thymocytes or T-ALL cells, following the original study. The miss may reflect missing cell-type context as well as the missing isoform annotation. The paper does not separate these causes. (synthesis)
- Comparing one predicted score per variant with measured TPM across patients mixes variant effect with patient-level variation in subtype, purity and co-drivers. The test shows group-level mis-ranking, not per-variant error. (synthesis)
- Only two xenografts have mechanistic data, and both are DP-like. Whether the haplotype-split H3K27me3/H3K27ac pattern generalises to the short-ITD majority is untested. (synthesis)

## Surprising or load-bearing bits

- **A somatic, held-out test that AlphaGenome fails.** The model's own paper showcased *TAL1* noncoding variants from three regions. On the fourth, unseen region, with functional effects confirmed in the xenografts, predicted scores were significantly lower even though measured expression was the same. This is one of very few out-of-distribution somatic evaluations of a sequence-to-function model in the wiki. (synthesis)
- **The failure is about mechanism, not only magnitude.** The variant acts through an alternative promoter (exon 4) that is not in the reference annotation, and predicted tracks never place a transcription start there. Annotation-anchored training targets can hide oncogenic isoforms. The authors cite *FOXR2* and *ERG* as other cases.
- **"Neo-enhancer" is not always right.** Enhancer II matches the known stem-cell enhancer, and enhancer I matches a progenitor ATAC peak. Somatic variants can reawaken developmentally silenced enhancers that already carry the core-circuit binding sites.
- **Allelic chromatin states explain an apparent paradox.** Overlapping H3K27ac and H3K27me3 peaks at exon 4 come from different haplotypes. Bulk ChIP without phasing would misread this as a bivalent state. (synthesis)

## Concepts touched

- [[variant-effect-prediction]] — an out-of-distribution somatic test in which AlphaGenome under-ranks a functionally active enhancer class.
- [[sequence-to-function-model]] — predicted RNA and H3K27ac tracks fail to show an unannotated alternative TSS.
- [[cis-regulatory-element]] / [[enhancer-states]] — somatic reactivation of a progenitor enhancer; haplotype-specific H3K27ac vs H3K27me3.
- [[transcription-factor-motif]] — de novo MYB sites from indels; pre-existing MYB, GATA3, RUNX1 and TAL1 sites in the reference.
- [[structural-variants]] — ITDs from 79 bp to 10.5 kb as cis-activating somatic events.
- [[chip-seq]] / [[atac-seq]] — allele-resolved TF binding and accessibility in xenografts.
- [[long-read-sequencing]] — Iso-Seq shows exclusive short-isoform expression.
- [[chromatin-loop]] — enhancer-I to exon-4 contact in CD34+ capture Hi-C and xenograft Hi-C.
- [[hematopoietic-differentiation]] — *TAL1* enhancer accessibility in HSC/MPP/LMPP/CLP, lost in mature T cells.

## Connections to other sources

- Model under test: [[avsec-2026-alphagenome]] — Avsec et al. used *TAL1* upstream, intron and enhancer-II variants (CD34+ CMP tracks) as a showcase. This paper extends the test to enhancer I and finds poor agreement. The wiki summary of Avsec already flagged the CMP proxy as a limitation for cell states not seen in training.
- Contrast: [[fischbach-2026-alphagenome-aging]] — also scores real somatic variants with AlphaGenome but has no measured effects. Here, measured strong effects were under-predicted, so near-zero AlphaGenome scores alone do not show that somatic variants are inert. (synthesis)
- Enhancer marks: [[creyghton-2010-h3k27ac-enhancers]] — H3K27ac as the active-enhancer mark used to read enhancer-I activity.
- Noncoding somatic drivers in blood: [[weinstock-2025-ch-noncoding-drivers]] — a genome-wide clonal-haematopoiesis scan that also uses AlphaGenome only to assign cis target genes, without validating its predictions; together with this paper it shows AlphaGenome being applied to somatic noncoding variants faster than it is being tested on them. (synthesis)
- Earlier sequence-to-function models: [[avsec-2021-enformer]], [[linder-2025-borzoi]] — same annotation-anchored RNA targets, so they would likely share the exon-4 blind spot. Untested. (synthesis)

## Open questions

- Would AlphaGenome predictions in a T-cell or thymocyte context, rather than CD34+ CMP, recover enhancer-I activity or the exon-4 start? (synthesis)
- Do the short ITDs (<200 bp, 71% of cases), which create no MYB site, act by changing spacing or accessibility of existing sites, as the authors propose? Reporter or base-editing tests are needed.
- Is enhancer reactivation, rather than neo-enhancer creation, common in other noncoding somatic drivers? If so, sequence models trained mostly on normal-tissue chromatin may systematically misjudge them. (synthesis)
- Can retraining with full-length (Iso-Seq) transcript targets fix alternative-promoter misses, as the authors suggest?

## Related

- [[avsec-2026-alphagenome]] · [[fischbach-2026-alphagenome-aging]] · [[variant-effect-prediction]] · [[sequence-to-function-model]] · [[cis-regulatory-element]] · [[enhancer-states]] · [[40-Topics/sequence-models-and-foundation-models]] · [[40-Topics/hematopoietic-malignancies]] · [[40-Topics/cancer-clonal-evolution]]
