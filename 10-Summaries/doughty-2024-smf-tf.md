---
type: summary
title: "Doughty et al. 2024 — Single-molecule states link transcription factor binding to gene expression"
source: [
  "[[00-Sources/papers/Single-molecule states link transcription factor binding to gene expression]]",
  "[[00-Sources/papers/Single-molecule chromatin configurations link transcription factor binding to expression in human cells.pdf]]"
]
source_quality: full
source_sha256: ["804be1c6586d6085985333e64d7688b238de3315ec0e1476da41afe559f42abc", "123bccb722046419bf2a6d365451ddd884933793299ac4a64f7fa65347f61802"]
aliases: ["doughty-2024-single-molecule-chromatin-config", "Doughty 2024", "SMF TF binding"]
source_kind: paper
author: "Benjamin R. Doughty, Michaela M. Hinks, Julia M. Schaepe (equal contribution), Georgi K. Marinov, Abby R. Thurm, Carolina Rios-Martinez, Benjamin E. Parks, Yingxuan Tan, Emil Marklund, Danilo Dubocanin, Lacramioara Bintu, William J. Greenleaf (Bintu and Greenleaf co-corresponding)"
published: 2024-11-20
created: 2026-05-13
ingested: 2026-05-13
updated: 2026-10-07
doi: "10.1038/s41586-024-08219-w"
journal: "Nature (2024); preprint bioRxiv 10.1101/2024.02.02.578660"
tags: [single-molecule-footprinting, SMF, NOMe-seq, M.CviPI, EM-seq, amplicon, transcription-factor, transcription-factors, enhancer, rTetR-VP48, ISGF3, interferon, BAF, p300, thermodynamic-model, kinetic-model, K562, Greenleaf-lab, Bintu-lab, preprint-merged]
entities: ["[[20-Entities/william-greenleaf]]"]
concepts: ["[[30-Concepts/single-molecule-footprinting]]", "[[30-Concepts/nome-seq]]", "[[30-Concepts/em-seq]]", "[[30-Concepts/chromatin-accessibility]]", "[[30-Concepts/enhancer-states]]", "[[30-Concepts/atac-seq]]", "[[30-Concepts/chip-seq]]", "[[30-Concepts/transcription-factor-motif]]", "[[30-Concepts/fiber-seq]]", "[[30-Concepts/samosa]]", "[[30-Concepts/daf-seq]]"]
topics: ["[[40-Topics/chromatin-architecture]]"]
---

**Citation:** Doughty, Hinks, Schaepe et al. (2024) — *Single-molecule states link transcription factor binding to gene expression* — *Nature*. [DOI](https://doi.org/10.1038/s41586-024-08219-w) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/39567683/). Preprint: bioRxiv [10.1101/2024.02.02.578660](https://doi.org/10.1101/2024.02.02.578660) (posted 2024-02-04, titled *Single-molecule chromatin configurations link transcription factor binding to expression in human cells*).

# Doughty 2024 — SMF links TF occupancy to expression

> **Version note (merged 2026-10-07):** this page now covers both the *Nature* paper and its bioRxiv preprint, which was previously summarised separately as `doughty-2024-single-molecule-chromatin-config`. All numbers below come from the *Nature* text. The *Nature* clipping holds the main text, Methods and Extended Data legends but **not the main-figure (Fig. 1–5) legends**, so several fitted parameters that the preprint gives in its main-figure legends cannot be checked against the published version. See [Preprint version](#preprint-version).
>
> The authors put synthetic promoter-proximal enhancers in front of a minimal CMV promoter driving **citrine** and integrated them at the *AAVS1* safe-harbour locus of K562 cells. The rTetR library carries 0–8 or 0–9 Tet operator (TetO) sites, bound by the dox-inducible synthetic TF **rTetR–VP48**. The ISRE library carries 0–6 interferon-stimulated response elements, bound by the endogenous **ISGF3** complex (IRF9–STAT1–STAT2). Each reporter molecule is read by amplicon **GpC single-molecule footprinting (SMF)**: M.CviPI methylation of nuclei, a modified enzymatic (EM-seq) conversion, PCR and MiSeq. GpCs flank every binding site, so a maximum-likelihood caller can assign each molecule its full set of bound sites, nucleosome positions and promoter state. Linking these states to flow cytometry and RT–qPCR gives a chain of simple models. A thermodynamic model links TetO number to occupancy, an additive kinetic model links occupancy to promoter activation, and a linear fit links activation to expression. The main conclusions are that apparent TF cooperativity comes from activation-domain-recruited **BAF** destabilising nucleosomes, that each bound TF adds the same amount to promoter activation, and that TF "strength" splits into separable **occupancy** and **potency** terms that multiply to give expression.

## Key claims

- **Scale and heterogeneity.** SMF with perturbations recovered "26,365,210 single molecules". Before dox, the reporters were relatively inaccessible, "with methylation probabilities around 20%". Molecules of identical sequence show distinct configurations: fully nucleosomal ("streaks of about 147 bp of protection punctuated by about 50 bp of accessibility"), fully or partly TF-bound, or mixed. Far more molecules are TF-bound than have an active promoter: "73% versus 22%, respectively, for the five-TetO enhancer". The heterogeneity is not an artefact of fast TF off-rates combined with irreversible methylation (Extended Data Fig. 2d,e).
- **Binding is bimodal, and few molecules have all sites filled.** The fraction of accessible and TF-bound enhancers rises non-linearly with TetO number, "with a large increase between four and six TetO sequences". Average occupancy shows apparent cooperativity and correlates with ATAC–seq. The distribution is bimodal: an unbound class, which neither TF-negative cells nor cell-to-cell TF concentration explains, plus "a wide distribution of occupancy within TF-bound molecules".
- **Apparent cooperativity is nucleosome-mediated, not TF–TF.** On nucleosome-bearing molecules, which are most molecules, pairs of bound TFs strongly prefer adjacent sites. On nucleosome-free molecules all pair configurations are equally represented, "consistent with independent binding on free DNA". There is no position effect: "each TetO site occupied on about 68% of nucleosome-free molecules". Clustering follows from statistical mechanics, because adjacent binding leaves room for more nucleosomes.
- **Simple competition fails; nucleosome destabilisation fits.** The two-parameter Simple Competition partition-function model (E_TF, E_nuc) "cannot reproduce the bimodality". Adding E_remodel, a TF-dependent drop in nucleosome affinity, gives a three-parameter model that recapitulates the bound fraction, average occupancy, binding distributions and microstate distributions. For the fraction of molecules with >0 TFs bound, Simple Competition gives "r² = 0.44" and Nucleosome Destabilization "r² = 0.99" (Extended Data Fig. 3g). Three alternative TF-only cooperativity models (thresholding, TF–TF interaction, cofactor scaffold) "are unable to fit the observed data".
- **Activation domains raise occupancy.** Removing VP48 gave "an average reduction in TetO occupancy of 35% across the library", which reduced TF concentration does not explain. rTetR alone is fit by Simple Competition as well as by Nucleosome Destabilization: r² = 0.86 for the bound fraction (Extended Data Fig. 4a) and r² = 0.83 and 0.96 for the destabilisation fit to occupancy and distribution (Extended Data Fig. 4e). Mass action alone is therefore enough for a DNA-binding domain that cannot recruit cofactors.
- **BAF, not p300 catalysis, destabilises nucleosomes.** The BRG1/BRM ATPase inhibitor BRM014 reduced rTetR–VP48 binding but not binding of rTetR alone, and the fit gave lower nucleosome and destabilisation energies. Simple Competition does not fully fit the BAF-inhibited data (r² = 0.78 and 0.51, Extended Data Fig. 4h). The authors' explanations are incomplete inhibition, redundant remodellers, or other activation-domain mechanisms. The p300 inhibitor A-485 caused "a marked reduction in H3K27 acetylation" but no drop in TF binding, nucleosome occupancy or fitted remodelling energy.
- **Additive promoter activation.** In three sequence backgrounds (up to nine TetOs at 19 bp spacing in two of them), the active (nucleosome-free) promoter fraction "is always proportional to the average TF occupancy with an invariable slope across backgrounds", so "each bound TF contributes equally to promoter activation". Removing VP48 eliminates active promoters but not binding. α-amanitin or flavopiridol lower the active fraction without affecting binding, so transcription does not feed back on occupancy. The active fraction is linear in citrine fluorescence and RT–qPCR. A telegraph model with on-rate ∝ average occupancy (Additive Activation) fits the data. The authors chain three fits: nucleosome destabilisation (three parameters per background), additive activation (one parameter shared across backgrounds) and a linear expression fit (one parameter shared). Together these "largely explain gene expression across the number of TetO sequences". The non-linearity therefore comes from the binding step, not from activation synergy. Alternative activation models fit with k_on/k_off = 0.13 ± 0.006 TF⁻¹ and n = 1.1 ± 0.04 (cooperative) or k_on/k_off = 0.5 ± 0.1 (thresholded) (Extended Data Fig. 5f).
- **Promoters integrate over binding events.** The chance that a molecule's promoter is active rises with the number of TFs bound on it. Among molecules with the same number bound, however, it still depends on TetO number. This implies similar timescales for binding and promoter activation, and that "promoters integrate information from multiple rounds of TF binding".
- **Occupancy and potency are separable.** Potency is the slope of active fraction against occupancy, i.e. k_on/k_off. Lowering dox reduces effective rTetR–VP48 concentration (checked by EMSA) and occupancy, but the slope stays the same, so "the potency of a TF is independent of its ability to bind DNA". BAF inhibition lowers occupancy while p300 inhibition has little effect on it, but both lower potency. The combined models correctly predict that BAF inhibition lowers expression more than p300 inhibition. Occupancy and potency "multiplicatively predict transcriptional output".
- **The interferon reporter decouples accessibility from activation.** Before IFNβ, with no reporter expression, ISREs already carry footprints and nucleosome-free regions, "consistent with pre-bound but transcriptionally inactive IRF9". After 6 h of IFNβ, footprints widen (ISGF3) and accessibility rises across enhancer and promoter, so the caller was extended to narrow (IRF9) versus wide (ISGF3) footprints. Narrow-footprint binding before stimulation is better fit by Nucleosome Destabilization than by Simple Competition. BAF inhibition before stimulation cut narrow footprints "by about 20%". Only wide footprints predict the active promoter fraction, "with a stronger fit potency than rTetR–VP48". For ISGF3, BAF inhibition lowers wide-footprint occupancy while p300 inhibition "leads to a slight increase". Both lower ISGF3 potency, with more dependence on BAF.
- **Endogenous ISG validation.** In K562 ATAC–seq, ISREs carry footprints genome-wide before stimulation, and ISRE-containing ISG promoters are more accessible than TPM-matched non-ISGs. BAF inhibition, but not p300 inhibition, decreases pre-stimulation accessibility. After stimulation, BAF inhibition lowers accessibility and ISRE footprints while p300 inhibition slightly raises both. The *ISG15*, *IFI6* and *USP18* promoter/enhancer elements installed at the reporter are accessible before stimulation and express citrine "at low levels pre-stimulation and at high levels post-stimulation". Basal and induced expression depend on BAF and p300, with induced expression depending more on BAF. Scrambling only the ISREs abolishes both expression and pre-stimulation accessibility.
- **Kinetics.** rTetR–VP48 binding reaches steady state by 8 h. Promoter activation lags by hours and reaches steady state between 8 and 24 h, while apparent potency rises over time. An ODE model (exponential binding, on-rate ∝ occupancy, single transcription, translation and decay rates) captures the delays between steps, with r² = 0.99 (occupancy), 0.90 (promoter), 0.95 (RNA) and 0.92 (protein) (Extended Data Fig. 10d). BAF inhibition slows TF binding, and both inhibitors slow promoter activation. ISGF3 shows no delay between binding and activation and has a shorter binding half-time. Its wide footprints "peak by 6 h before decreasing", while promoters stay accessible during downregulation. ISGF3 reaches maximum potency in "only 3 h" against "over 8 h" for rTetR–VP48, and its fitted promoter on-rate is ">5-fold faster".

## Methods / evidence

**Reporters.** Pooled 350 bp oligo libraries. Background 0 is random with 21 bp between TetOs. Background 1 is a mutated version with 19 bp spacing. Background 2 is a GC-rich hg38 region outside K562 DNase peaks. Each motif is flanked by GC, CGs are removed to avoid endogenous methylation, and every library includes a single-CTCF-motif control. The TetO array sits "80 bp upstream" of minCMV. The ISRE library holds 0–6 ISREs at 21 bp spacing, with GCs both flanking and inside the motif. The rTetR(3G)–VP48 or rTetR line was made by piggyBac. Reporters were integrated at *AAVS1* by TALEN-mediated HDR. Induction was 1,000 ng ml⁻¹ dox for 24 h, or 10 ng ml⁻¹ IFNβ for 6 h.

**SMF.** Omni-ATAC lysis, then 7.5 min M.CviPI at 37 °C. Excision with XbaI/AccI. EM-seq conversion modified for 500 ng input. Three rounds of PCR, then MiSeq with 374 cycles on R1. Conversion was controlled with methylated pUC19 and unmethylated lambda DNA. Native SMF was used throughout, because formaldehyde fixation "decreases the dynamic range of the methylation".

**State calling.** The caller enumerates every TetO-occupancy × nucleosome-placement state. Nucleosomes are 110–140 bp, start and end at GpCs, and have at least one accessible linker GpC between them. It picks the maximum Bernoulli-likelihood state per read, with all molecules retained.

**Models.** A Boltzmann partition function (E_TF, E_nuc, E_remodel) fit by maximum likelihood with Nelder–Mead, per biological replicate. A modified binding isotherm with a dox "leak" term. A steady-state additive activation fit with one parameter. A kinetic ODE cascade fit with scipy.

**Supporting assays.** ZE5 flow cytometry, RT–qPCR, bulk Omni-ATAC (two replicates), RNA-seq, H3K27ac and Pol II-S5P ChIP–seq with mouse spike-in, and EMSA of purified rTetR. Data: SRA PRJNA1071686 and GEO GSE276513–GSE276515. Code: github.com/GreenleafLab/amplicon-smf (Zenodo 10.5281/zenodo.13840888).

**Weight.** This is a closed quantitative system. Every link in the chain is measured, and it is perturbed several ways: activation-domain removal, two cofactor inhibitors, two transcription inhibitors, dox titration and time courses. Rival models are compared at each step. The trade-off is generality: one locus, one cell line, a minimal promoter, two inducible TFs, and many fits on only two biological replicates. (synthesis)

## Limitations

**Authors' own:**
- Only two inducible TFs were studied. Extending to others is complicated by the need for induction and by multiple TFs binding similar motifs.
- States were assigned unambiguously only because GpCs were placed deliberately. Sparser, irregular GpCs lower footprinting resolution at non-engineered loci. The authors expect general cytosine deaminases to solve this.
- Reporters sit at a single locus, so how much the findings depend on context is untested.
- The assay needs TF residence times longer than the irreversible methylation reaction, or occupancy is underestimated.

**Reviewer notes:**
- Amplicon short-read SMF reads only a ~350 bp construct. No single-molecule configurations are obtained at native loci, apart from ISG elements transplanted to *AAVS1*. Genome-wide evidence comes from bulk ATAC footprinting. (synthesis)
- "Active promoter" means a nucleosome-free TSS footprint. Its link to transcription is shown at population level (linear in MFI and RT–qPCR), not molecule by molecule. (synthesis)
- A-485 blocks CBP/p300 catalytic activity only. The conclusion that p300 does not destabilise nucleosomes does not test scaffolding roles or non-catalytic recruitment. (synthesis)

## Surprising or load-bearing bits

- **Accessibility ≠ activity.** Pre-bound IRF9 makes ISREs accessible with no reporter expression. Yet ATAC–seq signal "linearly correlates with methylation probability", so bulk accessibility reports average single-molecule accessibility accurately but not transcription.
- **Cooperativity without TF–TF contacts.** Adjacent-site preference appears only on nucleosome-bearing molecules. Remodeller recruitment after the first binding event "actively clear[s] space for more TF binding". This also explains accessibility that extends past the most distal site (Supplementary Note 1).
- **Most bound enhancers are not driving an active promoter at any moment** (73% bound vs 22% active at 5×TetO).
- **Histone acetylation is not the destabilisation step here.** Stable occupancy after p300 inhibition contradicts the model in which acetylation weakens nucleosome–DNA affinity to help binding. p300's effect instead falls on promoter activation, consistent with its role in pre-initiation complex assembly.
- **Activation domains set occupancy as well as potency.** This may explain why in vitro affinities predict in vivo occupancy poorly.

## Entities mentioned

- [[20-Entities/william-greenleaf]] — co-corresponding author (Stanford). Lacramioara Bintu, the other corresponding author, has no wiki page.

## Concepts touched

- [[30-Concepts/single-molecule-footprinting]] — GpC methyltransferase SMF on engineered amplicons. This is the short-read, amplification-compatible branch, beside the long-read m6A Fiber-seq/SAMOSA branch and deaminase footprinting.
- [[30-Concepts/nome-seq]] — the chemistry is NOMe-style M.CviPI GpC methylation.
- [[30-Concepts/em-seq]] — EM-seq conversion in place of bisulfite, with more input DNA, TET2 and oxidation enhancer.
- [[30-Concepts/chromatin-accessibility]] — single-molecule accessibility is heterogeneous: "even highly active elements are accessible only in subsets of cells". Accessibility can be decoupled from expression.
- [[30-Concepts/enhancer-states]] — enhancer microstates (unbound, nucleosomal or k-TF-bound) and promoter states (nucleosomal or active, with active substates).
- [[30-Concepts/atac-seq]] — SMF methylation is linear in ATAC peak signal. ATAC footprinting finds ISRE binding genome-wide before stimulation.
- [[30-Concepts/chip-seq]] — H3K27ac and Pol II-S5P ChIP–seq with spike-in confirm that the reporter is silent before dox and that A-485 removes H3K27ac.
- [[30-Concepts/transcription-factor-motif]] — motif number, spacing and ISRE identity are the variables manipulated. ISRE matches use the Vierstra cluster AC0188 (IRF/STAT).
- [[30-Concepts/daf-seq]] — the deaminase direction the authors name for native loci.

## Connections to other sources

- Contrast with long-read m6A stencilling: [[10-Summaries/andrewb-2020-science]] (Fiber-seq, cited as ref. 15) and [[10-Summaries/abdulhay-2020-samosa]]. These read kilobase fibres genome-wide but have neither the engineered-site resolution nor the expression link used here. (synthesis)
- Cites [[10-Summaries/shipony-2020-smac]] among methyltransferase SMF methods, and shares authors with it (Marinov, Greenleaf).
- Uses the EM-seq chemistry of [[10-Summaries/vaisvila-2021-em-seq]] (ref. 20), modified for higher input.
- Cites the deaminase footprinting preprint of [[10-Summaries/he-2024-foodie]] (ref. 64) as the route to native-locus resolution. [[10-Summaries/swanson-2025-daf-seq]] takes the same deaminase route to TF co-occupancy at endogenous loci. (synthesis)
- Single-cell GpC footprinting predecessor: [[10-Summaries/pott-2017-elife]].
- Supplies a molecular mechanism for the Greenleaf-lab view of accessibility as a dynamic TF–nucleosome equilibrium ([[10-Summaries/klemm-2019-chromatin-accessibility-review]]). (synthesis)
- Methylation-based protein mapping on single molecules from another angle: [[10-Summaries/altemose-2022-dimelo-seq]]. (synthesis)

## Open questions

- Do the occupancy/potency split and the additive promoter model hold at native loci, where GpC density is irregular and many TFs act at once? The authors point to deaminases for this.
- How do repression domains and other activation domains fit the framework, and do changes in motif spacing and affinity match what the thermodynamic model predicts? Both are listed as future work.
- Is fast ISG activation explained by pre-binding of non-activating TFs (IRF9), by chromatin marks those factors leave, or by activation domains with intrinsically different kinetics? The authors leave this open.
- What explains the different flow-cytometry distribution shapes under BAF versus p300 inhibition (Extended Data Fig. 5n)? The authors flag it as "deserving further investigation".

## Preprint version

The bioRxiv preprint, *Single-molecule chromatin configurations link transcription factor binding to expression in human cells* (posted **2024-02-04**, [10.1101/2024.02.02.578660](https://doi.org/10.1101/2024.02.02.578660)), was summarised separately until 2026-10-07 as `doughty-2024-single-molecule-chromatin-config`. Its source is the full preprint PDF. The core conclusions are the same in both versions. The differences are listed below.

**Preprint numbers that differ from the *Nature* text (superseded):**
- ~~"called binding and nucleosome occupancy across 24,715,362 single molecules"~~ → *Nature*: "recovering 26,365,210 single molecules".
- ~~TetO array "starting 170 bp upstream of a minimal promoter"~~ → *Nature*: TetOs "80 bp upstream of a minimal promoter". This may be a change of reference point rather than of construct. (synthesis)
- ~~ISG15/IFI6/USP18 reporters "only express Citrine post-stimulation"~~ → *Nature*: they express citrine "at low levels pre-stimulation and at high levels post-stimulation".

**Preprint main-figure values not found in the *Nature* clipping.** The *Nature* clipping lacks the main-figure legends, so these may survive in the published figures but cannot be confirmed. Treat them as preprint-only:
- Simple Competition fit to **average occupancy**: r² = 0.84. Fit to the 7×TetO distribution: r² = −0.72. Nucleosome Destabilization: r² = 0.99 and 0.79. This is a different quantity from the Extended Data Fig. 3g fit to the **fraction with >0 TFs bound** (Simple Competition r² = 0.44 vs Nucleosome Destabilization r² = 0.99), which appears in both versions. The "0.84 vs 0.44" contrast is therefore not a revised number. (synthesis)
- rTetR-alone Simple Competition fit: r² = 0.77 and 0.94. Nucleosome Destabilization fits under BRM014: 0.94 and 0.96. Under A485: 0.99 and 0.90.
- Additive Activation potency: k_on/k_off = 0.15 ± 0.002 TF⁻¹ (rTetR–VP48) and 0.44 ± 0.02 TF⁻¹ (ISGF3). Dox-titration fits: "All r² between 0.84–0.97".
- Kinetic parameters (7×TetO): t½ = 2.1 ± 0.3 hr, k_on = 0.11 ± 0.02 TF⁻¹ hr⁻¹, k_off = 0.16 ± 0.04 hr⁻¹, k_trs = 2.0 ± 0.4, k_decay,rna = 0.20 ± 0.05 hr⁻¹, k_trl = 1,200 ± 200, k_decay,prot = 0.16 ± 0.04 hr⁻¹.
- The 7×TetO bound class has "a mode of 3-4 sites bound". *Nature* says only "a wide distribution of occupancy".

**Findings only in the *Nature* version:**
- Per-site occupancy of "about 68%" on nucleosome-free molecules.
- BAF inhibition before stimulation lowers narrow (IRF9) footprints by "about 20%".
- Cofactor dependence of ISGF3: BAF inhibition lowers wide-footprint occupancy while p300 inhibition slightly raises it, and both lower potency.
- Genome-wide ATAC–seq under BAF and p300 inhibition, before and after IFNβ.
- BAF and p300 dependence of basal and induced expression from the ISG elements.
- An explicit statement that ISGF3 shows no delay between binding and activation.
- Pol II-S5P ChIP–seq. Active-promoter substates (k-means). Fixed versus native SMF comparison.
- Supplementary Note 1 on remodeller-driven accessibility beyond the distal site, and a kinetic-proofreading interpretation of promoter integration.
- Two new limitations: a single integration locus, and deaminases as the fix for native loci.
- GEO accessions and Zenodo archives.

**Findings framed differently in the preprint:**
- "Induced reporter expression is ablated by BAF inhibition" (Fig. S6H), stated in the IRF9 section. *Nature* reports instead the graded effects of BAF and p300 inhibition on ISGF3 occupancy, potency and expression.
- Future work named only in the preprint: testing synergy between pairs of activation domains on rTetR.

## Related

- [[30-Concepts/single-molecule-footprinting]] · [[30-Concepts/nome-seq]] · [[30-Concepts/fiber-seq]] · [[30-Concepts/daf-seq]] · [[30-Concepts/samosa]]
- [[40-Topics/chromatin-architecture]]
- [[50-Notes/droplet-vs-single-molecule-scdna]]
- [[10-Summaries/andrewb-2020-science]] · [[10-Summaries/abdulhay-2020-samosa]] · [[10-Summaries/altemose-2022-dimelo-seq]] · [[10-Summaries/swanson-2025-daf-seq]] · [[10-Summaries/he-2024-foodie]] · [[10-Summaries/pott-2017-elife]]
