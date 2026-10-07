---
type: summary
title: "Huang et al. 2010 — The Behaviour of 5-Hydroxymethylcytosine in Bisulfite Sequencing"
source: "[[00-Sources/papers/The Behaviour of 5-Hydroxymethylcytosine in Bisulfite Sequencing]]"
source_quality: full
source_sha256: "e7106fe6843b4b005e675d5f86fc4856c8cb7e60e721a3afc5d5416ecf23bbb2"
source_kind: paper
author: "Yun Huang, William A. Pastor, Yinghua Shen, Mamta Tahiliani, David R. Liu, Anjana Rao"
published: 2010-01-26
ingested: 2026-10-07
doi: "10.1371/journal.pone.0008888"
journal: "PLoS ONE 5(1):e8888"
tags: [5hmC, bisulfite-sequencing, CMS, cytosine-5-methylenesulfonate, PCR-bias, Taq-stalling, TET, DNA-methylation, methods-caveat]
entities: []
concepts: ["[[5hmc]]", "[[bisulfite-sequencing]]", "[[tet-enzymes]]"]
topics: ["[[dna-methylation]]"]
---

**Citation:** Huang et al. (2010) — *The Behaviour of 5-Hydroxymethylcytosine in Bisulfite Sequencing* — *PLoS ONE* 5(1):e8888. [DOI](https://doi.org/10.1371/journal.pone.0008888)

# Huang 2010 — 5hmC in bisulfite sequencing

> A short methods-caveat paper from the Rao lab, written right after the same group showed TET enzymes make 5hmC. It asks what bisulfite sequencing actually does to 5hmC and finds two problems. First, bisulfite converts 5hmC almost completely to **cytosine 5-methylenesulfonate (CMS)**, which, like 5mC, resists deamination and is read as C. **Bisulfite therefore cannot tell 5mC from 5hmC.** Second, CMS **stalls Taq polymerase**, especially where CMS residues sit next to each other or 1–2 nt apart. So densely hydroxymethylated DNA is not just mislabelled as "methylated"; it may also be **under-amplified**, and therefore under-represented, in quantitative bisulfite data.

## Key claims

- **Near-complete conversion to CMS.** LC-MS of a nuclease-P1-digested 201-bp oligonucleotide after bisulfite treatment: 4.69 nM hmdCMP remained from 1.5 µM, a 5hmC→CMS conversion of **99.7%**.
- **5hmC is read as C.** Sanger traces show that every C in the control oligo converts to T, while the 5hmC oligo shows no C→T transitions. Since 5mC also does not convert, **bisulfite sequencing does not distinguish 5mC from 5hmC**.
- **Antibody-based methods split the other way.** A monoclonal anti-5mC antibody detects the 5mC oligo but not the 5hmC oligo (dot blot). Hydroxymethylated sites would therefore look methylated by bisulfite but unmethylated by antibody methods. The introduction adds that the MeCP2 MBD domain and methylation-sensitive enzymes (HpaII, McrBC) also fail to reliably handle 5hmC.
- **CMS hinders PCR.** When bisulfite-treated, the oligo with 5hmC as its sole cytosine species (28 cytosines in 201 bases) amplifies far less efficiently by real-time PCR than the C or 5mC versions.
- **The block is polymerase stalling.** Primer-extension assays with two commercial Taq polymerases (Roche, Sigma) give a ladder of incomplete products **only** with bisulfite-treated 5hmC DNA. The strongest stalls fall at a CTC near the reverse primer, a CCGC and several CC sequences. CMS stalls Taq but does not completely block it.
- **Stalling also happens in CpG context.** In 158-bp oligos with a variable CGAT / CCAT / CGCG / CCGG insert, stalling is strongest at tandem CCs and weaker but present at CpGs. CG and CGCG oligos still amplified efficiently; CC-containing oligos showed a perceptible loss of efficiency.
- **Interpretive consequence.** Loci with dense 5hmC "might be incorrectly assumed to contain methylated CpGs, and might also be underrepresented in quantitative analyses of DNA methylation status". The authors flag ES cells as a particular concern, since ~25% of 5mC there is reported to be in non-CpG context, where adjacent Cs can both be modified.

## Methods / evidence

Synthetic minigenes were PCR-amplified with dCTP, mdCTP or hmdCTP to make templates carrying a single cytosine species. Bisulfite conversion used the EpiTect kit, followed by LC-MS quantification against a 7-point hmdCMP standard curve, Sanger sequencing, SYBR real-time PCR (three replicates), ³²P primer-extension assays next to a Sanger ladder, and an anti-5mC dot blot. No genomic DNA was tested. The authors note that no 5-hydroxymethylated genomic loci had yet been identified, so the under-representation effect could not be checked in real genomes.

Weight: clean, well-controlled chemistry on synthetic templates. The indistinguishability result is definitive. The under-representation result is shown only for oligos in which 5hmC replaces *every* C (14% of bases) or sits at engineered tandem sites. Its size in real genomes, where 5hmC is far sparser, is not measured here. (synthesis)

## Surprising or load-bearing bits

- **Two separate errors, not one.** "5mC+5hmC composite" is the usual caveat on bisulfite data, but this paper adds a **coverage bias**: CMS-dense fragments drop out during amplification. A bisulfite methylome could therefore *under*-count the hydroxymethylated fraction even within the composite signal. (synthesis)
- **Single-cell protocols may be more exposed.** Single-cell bisulfite methods amplify picogram inputs through many PCR cycles. If CMS stalls the first copying steps, the bias compounds where every template molecule counts. This is an extrapolation; the paper tests only bulk oligo PCR. (synthesis)
- **The discussion floats a 5hmC mapping strategy.** Because primer extension terminates disproportionately at CMS, extension under suboptimal conditions combined with ligation-mediated PCR might locate 5hmC at single-base resolution.
- **The mechanism is left open.** CMS keeps its aromaticity, unlike thymine glycol, so the bulky-adduct analogy proposed earlier by Rein et al. may not explain the stalling.
- Background figures from the introduction: 5hmC is ~5% of cytosine species at CpGs in MspI/Taqα I sites in ES cell DNA and ~20% in cerebellar Purkinje cell DNA; 5mC is ~1% of all bases.

## Concepts touched

- [[5hmc]] — establishes that bisulfite reads 5hmC as C and that its bisulfite adduct (CMS) biases amplification.
- [[bisulfite-sequencing]] — a second, coverage-level artefact on top of the 5mC/5hmC conflation.
- [[tet-enzymes]] — motivating context: TET makes 5hmC, so methods built for 5mC must be re-examined.

## Connections to other sources

- Companion to [[tahiliani-2009-tet1-5hmc]] (same lab, same senior author): that paper discovered TET1-made 5hmC; this one shows what 5hmC does to the standard readout.
- The conflation is restated in [[jones-2012-dna-methylation-functions]] and [[flusberg-2010-smrt-methylation]]. Later methods that resolve it: [[chen-2025-sctaps-sccaps-plus]], [[bai-2024-simple-seq]], [[tavares-2026-6-base-cut-tag]], and polymerase-kinetic separation in [[flusberg-2010-smrt-methylation]].
- Bisulfite single-cell methylomes to which the caveat applies: [[smallwood-2014-natmethods]], [[luo-2017-snmc-seq]], [[krueger-2011-bismark]] (alignment/calling layer). (synthesis)

## Open questions

- How large is the CMS-induced under-representation in real genomic DNA, with natural 5hmC densities and modern bisulfite-tolerant polymerases?
- Do post-bisulfite adaptor tagging and other single-cell library schemes amplify the stalling bias or reduce it? (synthesis)
- How much of the "5mC" reported for neurons by bisulfite-based single-cell atlases is actually 5hmC, given the ~20% Purkinje-cell figure cited here? (synthesis)

## Related

- [[5hmc]] · [[bisulfite-sequencing]] · [[tahiliani-2009-tet1-5hmc]] · [[40-Topics/dna-methylation]]
