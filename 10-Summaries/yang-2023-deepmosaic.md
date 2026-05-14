---
type: summary
title: "Yang 2023 — Control-independent mosaic single nucleotide variant detection with DeepMosaic"
aliases: ["Yang 2023 DeepMosaic", "DeepMosaic", "CNN mosaic caller"]
tags: [DeepMosaic, mosaic-variant-calling, CNN, deep-learning, brain-mosaicism, Gleeson-lab, BSMN, UCSD]
created: 2026-05-13
updated: 2026-05-13
sources: ["Xiaoxu_2023_NatureBiotechnology.pdf"]
---

Yang, Xu, Breuss, Antaki, Ball, Chung, Shen, Li, George, Wang, Bae, Abyzov, Wei, Alexandrov, Sebat and Gleeson (UCSD, BSMN consortium) developed **DeepMosaic**, a convolutional-neural-network (CNN) framework for control-independent detection of mosaic single-nucleotide variants. The method comprises two modules: (1) DeepMosaic-VM, an image-based visualization that exports a GATK-pileup-processed RGB pileup snapshot per candidate variant; (2) DeepMosaic-CM, a CNN classifier (transfer learning from EfficientNet-b4) trained on 180,000 simulated and biologically-tested mosaic-variant images.

Benchmarked on 619,740 simulated and 530 independent amplicon-validated mosaic variants from 16 genomes and 181 exomes. DeepMosaic achieves sensitivity 0.78, specificity 0.83, and PPV 0.96 on noncancer WGS, **doubling the validation rate** over previous best-practice methods (MosaicForecast, MosaicHunter) on noncancer WES (0.43 vs 0.18). The CNN-pileup combination captures features that traditional heuristic filters miss — particularly read-edge artefacts, base-quality patterns, and strand-orientation patterns visible in raw alignment images.

## Why this matters

The image-based CNN approach represents a categorically different paradigm from heuristic-filter mosaic callers (MosaicHunter, MosaicForecast) and from feature-based ML (Strelka2, MuTect2). Yang 2023 demonstrates that the pileup image itself carries information that engineered features lose. Anchors §4 (mosaic-caller family) alongside MosaicForecast and the Ha 2023 benchmark. Important methodological lineage: the Gleeson-lab BSMN context links this to brain-somatic-mosaicism work — DeepMosaic was designed specifically for postmortem brain WGS, where matched control tissue is unavailable and clinical relevance is high.

---
**Source:** [DOI](https://doi.org/10.1038/s41587-022-01559-w) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/36593400/)

---
**Source:** [DOI](https://doi.org/10.1038/s41587-022-01559-w) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/36593400/)

## Related

- [[10-Summaries/dou-2020-mosaicforecast]]
- [[10-Summaries/ha-2023-natmethods]]
- [[10-Summaries/mcconnell-2017-science]]
- [[40-Topics/mosaic-variant-calling]]
