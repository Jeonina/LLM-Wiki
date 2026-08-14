---
type: summary
title: "Bankevich et al. 2012 — SPAdes: a new genome assembly algorithm and its applications to single-cell sequencing"
source: "[[00-Sources/papers/SPAdes_ A New Genome Assembly Algorithm and Its Applications to Single-Cell Sequencing - Anton Bankevich, Sergey Nurk, Dmitry Antipov, Alexey A. Gurevich, Mikhail Dvorkin, Alexander S. Kulikov, Valery M. Lesin, Sergey I. Nikolenko, Son Pham,]]"
source_kind: paper
author: "Anton Bankevich, Sergey Nurk, Dmitry Antipov, Alexey A. Gurevich, Mikhail Dvorkin, Alexander S. Kulikov, Valery M. Lesin, Sergey I. Nikolenko, Son Pham, Andrey D. Prjibelski, Alexey V. Pyshkin, Alexander V. Sirotkin, Nikolay Vyahhi, Glenn Tesler, Max A. Alekseyev, Pavel A. Pevzner (corresponding)"
published: 2012-05-01
ingested: 2026-08-13
doi: "10.1089/cmb.2012.0021"
journal: "Journal of Computational Biology 19:455–477"
tags: [SPAdes, paired-de-Bruijn-graph, multisized-de-Bruijn-graph, k-bimer-adjustment, A-Bruijn, single-cell-assembly, chimera-detection, Hammer]
entities: ["[[pavel-pevzner]]"]
concepts: ["[[single-cell-genome-assembly]]", "[[mda]]", "[[sequencing-depth-and-coverage]]", "[[highly-repetitive-regions]]"]
topics: ["[[whole-genome-amplification]]", "[[computational-methods]]"]
---

**Citation:** Bankevich et al. (2012) — *SPAdes: a new genome assembly algorithm and its applications to single-cell sequencing* — *Journal of Computational Biology* 19, 455–477. [DOI](https://doi.org/10.1089/cmb.2012.0021)

# Bankevich 2012 — SPAdes

> Two of this paper's authors coauthored [[chitsaz-2011-velvet-sc|E+V-SC]] the year before and say plainly why they came back: *"one needs to change algorithmic design (rather than just modify existing tools) to fully utilize the potential of SCS."* SPAdes rebuilds assembly around the **paired de Bruijn graph** — reconstructing a string from pairs of *k*-mers at approximate distance *d*, rather than from *k*-mers alone — and makes that theoretical construct practical via ***k*-bimer adjustment**, which recovers exact distances for most read pairs.

## Key claims

- **Read pairs were the least-exploited stage of assembly.** The standard abstraction reconstructs a string from its *k*-mers; the better abstraction reconstructs it from *pairs* of *k*-mers ("*k*-bimers") at distance ≈ *d*. Paired de Bruijn graphs (Medvedev et al.) formalised this but assumed a fixed distance, which NGS does not provide — so PDBGs were a theoretical idea until this paper.
- ***k*-bimer adjustment is the bottleneck-breaker.** It derives accurate distance estimates between graph edges by jointly analysing distance histograms and paths in the assembly graph, recovering exact distances for the vast majority of adjusted *k*-bimers. The authors draw an explicit historical parallel: de Bruijn graphs were considered impractical for Sanger data until error correction made most reads error-free; PDBGs were impractical for NGS until *k*-bimer adjustment made most distances exact.
- **Four stages, each targeting one SCS pathology** — sequencing errors, non-uniform coverage, insert-size variation, chimeric reads and bireads. Stage 1 builds the assembly graph using a **multisized de Bruijn graph** (multiple *k* simultaneously, converging with [[peng-2012-idba-ud|IDBA-UD]]'s iteration idea), new bulge/tip removal, **explicit chimeric-read detection and removal**, aggregation of read-pair information into distance histograms, and backtrackable graph operations. Stage 2 is *k*-bimer adjustment. Stage 3 builds the paired assembly graph. Stage 4 constructs contigs by backtracking the simplifications.
- **SPAdes uses read pairs where E+V-SC could not.** E+V-SC deliberately discarded pairing to avoid misassemblies from chimeric read-pairs; SPAdes handles the chimeras and keeps the pairing — a direct, stated improvement over its own predecessor.
- **A "universal *A*-Bruijn assembler."** SPAdes uses *k*-mers only to build the initial graph and then "forgets" them, operating purely on graph topology, coverage, and sequence lengths. The consensus DNA sequence is restored only at the end. This lets one framework implement paired, multisized, and other *A*-Bruijn variants — and to be reused for non-assembly problems where these graphs apply.
- **Error correction is coupled and specialised**: a modification of Hammer aimed at SCS, applied for correction and quality trimming before assembly — because standard correctors like Quake implicitly assume near-uniform coverage.
- **Improves on E+V-SC for single-cell data and on Velvet and SOAPdenovo for multicell data** — i.e. it is not a single-cell-only tool.

## Methods / evidence

Benchmarking on single-cell and cultured *E. coli* datasets against E+V-SC, Velvet and SOAPdenovo. The bulk of the paper is algorithmic exposition — terminology for h-paths and h-edges, formal definitions of standard/multisized/paired de Bruijn graphs, and a worked example of paired-assembly-graph construction.

Weight: this is a computational-methods paper in a computational-biology journal, with the algorithm as the contribution and the benchmark as support. The single-cell claim rests on *E. coli* with a matched multicell control — the right design, but one organism.

## Surprising or load-bearing bits

- **The authors publicly overruling their own prior paper** — "modify existing tools" declared insufficient by two of the people who did the modifying — is a rare and useful piece of scientific bookkeeping, and it marks where single-cell assembly stopped being a patch and became a field.
- **"Forget the *k*-mers after building the graph"** is the design decision that makes SPAdes generalisable. Assembly becomes a graph-topology problem rather than a string problem, which is why SPAdes was later extended to metagenomes, plasmids, and RNA without a rewrite.
- **The Sanger-era analogy is the paper's own best framing**: a graph formalism dismissed as impractical because of data noise, rescued by a preprocessing step that removes the noise. It suggests a general recipe — when a clean abstraction fails on real data, fix the data representation rather than abandoning the abstraction.
- **Chimera detection is promoted to a named pipeline stage**, whereas [[chitsaz-2011-velvet-sc|Velvet-SC]] worked around chimeras by discarding pairing and [[peng-2012-idba-ud|IDBA-UD]] did not address them. Of the three, only SPAdes treats the [[mda|MDA]] chimera as a thing to be found and removed.
- **SPAdes is the tool that survived.** Velvet-SC and IDBA-UD are historical; SPAdes remains in routine use — a reminder that in the single-cell computational literature, the tool that reformulates the problem outlives the tools that patch it.

## Entities mentioned

- [[pavel-pevzner]] — corresponding author; de Bruijn graph assembly, and coauthor of [[chitsaz-2011-velvet-sc]].

## Concepts touched

- [[single-cell-genome-assembly]] — the paired/multisized de Bruijn reformulation and explicit chimera handling.
- [[mda]] — chimeric reads and read-pairs as the artifact class the design targets.

## Connections to other sources

- Directly supersedes: [[chitsaz-2011-velvet-sc]] (same lineage, two shared authors).
- Converges with: [[peng-2012-idba-ud]] on multi-*k* assembly, reached independently.
- Amplification context: [[dean-2002-mda]], [[huang-2015-scwga-review]] (chimeras as the reason single-cell SVs resist detection), [[hou-2015-wga-comparison]].
- Assembly quality is a WGA benchmark metric in [[hou-2015-wga-comparison]], which compares MDA and MALBAC by mitochondrial assembly stability.
- The human-genome branch, where assembly was never the goal and variant calling took its place: [[navin-2011-sns-tumor-evolution]], [[wang-2014-nuc-seq]], [[zafar-2016-monovar]].

## Open questions

- Benchmarking is on *E. coli* only in the captured sections; generalisation across genome size, GC content, and repeat structure is not established here.
- The multisized de Bruijn graph's *k* range and how it is chosen are not covered in the ingested text.
- Whether the chimera-detection step's sensitivity was measured against known chimeras is not recoverable from this source.

## Related

- [[chitsaz-2011-velvet-sc]] · [[peng-2012-idba-ud]] · [[single-cell-genome-assembly]] · [[40-Topics/whole-genome-amplification]]
