---
type: concept
title: Duplicate Marking
aliases: [PCR duplicate removal, deduplication]
tags: [alignment, amplification, QC, library-complexity]
created: 2026-08-10
updated: 2026-10-12
---

# Duplicate Marking

> Identifying reads that are PCR copies of the same original template rather than independent observations. The standard implementation is coordinate-based — reads sharing start and end positions are duplicates — and is available as a first-class utility in the SAM toolkit ([[10-Summaries/li-2009-samtools|SAMtools]]).

> [!abstract] 한눈에
> Duplicate marking은 같은 원본 분자에서 나온 PCR 사본을 독립 관측과 구분하는 작업이고, 표준 방식은 시작·끝 좌표가 같은 read를 duplicate로 보는 것이다 ([[10-Summaries/li-2009-samtools|SAMtools]]). 이 방식은 절편화가 증폭보다 먼저일 때만 성립해서, 증폭 후 절편화하는 WGA에서는 duplicate를 걸러낼 수 없다 ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]).

## Definition

Duplicate marking flags reads that are PCR copies of one original template. The standard implementation treats reads sharing start and end positions as duplicates, and SAMtools provides it as a first-class utility ([[10-Summaries/li-2009-samtools|SAMtools]]).

## Why the definition depends on chemistry

Coordinate-based deduplication is **only valid when fragmentation precedes amplification**. Under whole-genome amplification, long amplicons are copied first and fragmented afterwards, so a single original region yields multiple inserts with non-overlapping coordinates that cannot be filtered as duplicates ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]). This is the mechanistic core of the argument for amplification-free single-cell library preparation, and it explains most of WGA's coverage pathology ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]); see [[scwga-chemistries]] and [[dlp-plus]].

## Approaches

| Approach | Example | What it does | Source |
|---|---|---|---|
| Coordinate-based marking | [[10-Summaries/li-2009-samtools\|SAMtools]] | Reads sharing start and end positions are duplicates | ([[10-Summaries/li-2009-samtools\|SAMtools]]) |
| Fragment-pair rules for Tn5 libraries | [[10-Summaries/wesley-2026-songbird\|Songbird]]; ASCENT | Songbird keeps only the longer fragment of pairs with the same start or end and orientation; ASCENT drops any read within 1 nt of another | ([[10-Summaries/wesley-2026-songbird\|Songbird]]) |
| Redundant-tag removal in peak calling | [[10-Summaries/zhang-2008-macs\|MACS]] | Removes tags beyond what sequencing depth warrants (binomial *p* < 10⁻⁵) as an amplification-artefact control | ([[10-Summaries/zhang-2008-macs\|MACS]]) |
| UMIs | [[10-Summaries/chen-2018-fastp\|fastp]] | Molecular identity carried in sequence rather than inferred from coordinates; see [[umi-molecular-barcoding]] | ([[10-Summaries/chen-2018-fastp\|fastp]]) |
| scCUT&Tag pipelines | Picard, SAMtools, Cell Ranger ATAC, MACS2 `--keep-dup=1` | Later pipelines remove PCR duplicates; the original scCUT&Tag study did not explicitly report deduplication | ([[10-Summaries/wu-2026-sccut-tag-review\|Wu 2026]]) |

Deduplication runs on the output of [[read-alignment]].

## Evidence and examples

- C-DOP-L libraries carry high duplicate rates and need roughly twice the total reads for equivalent usable yield ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]).
- DOP-PCR coverage breadth **saturates** with deeper sequencing, making it unsuitable for SNV calling ([[10-Summaries/zahn-2017-dlp|Zahn 2017]]).
- In CUT&Tag data with high duplication (mean 82%), retaining PCR duplicates slightly raised MACS2 recall but produced spurious peaks, many in heterochromatin; the benchmark recommends removing duplicates ([[10-Summaries/abbasova-2025-cut-tag-encode-benchmark|Abbasova 2025]]).
- scCUT&Tag libraries typically contain 30–50% duplicated fragments (nano-CT) ([[10-Summaries/wu-2026-sccut-tag-review|Wu 2026]]).

## Contested points

- **Coordinate deduplication is incomplete even in amplification-free Tn5 libraries:** fragment pairs with the same start or end and orientation but different lengths survive it ([[10-Summaries/wesley-2026-songbird|Songbird]]).
- **Not every duplicate is a PCR artefact.** In bulk CUT&Tag some duplicates may reflect genuine repeated tagmentation ([[10-Summaries/wu-2026-sccut-tag-review|Wu 2026]]), yet keeping them produced spurious peaks in the ENCODE comparison ([[10-Summaries/abbasova-2025-cut-tag-encode-benchmark|Abbasova 2025]]).
- **Open question:** the 30–50% duplicate figure for nano-CUT&Tag comes from a 2026 review ([[10-Summaries/wu-2026-sccut-tag-review|Wu 2026]]); the nano-CUT&Tag paper itself reports only 0.11–0.14% linear-amplification duplicates and no PCR-duplicate rate ([[10-Summaries/bartosovic-2022-nano-cut-tag|Bartosovic 2022]]). The two numbers may measure different things.

## Related

> [!cards]
> - `concept` [[30-Concepts/scwga-chemistries|scWGA chemistries]] — Amplification chemistries and their trade-offs in uniformity, dropout and error.
> - `concept` [[30-Concepts/umi-molecular-barcoding|UMI / molecular barcoding]] — Random tags that group reads by molecule of origin.
> - `concept` [[30-Concepts/read-alignment|Read alignment]] — Placing reads on a reference; the step deduplication follows.
> - `concept` [[30-Concepts/dlp-plus|DLP+]] — Amplification-free Tn5 scWGS at high cell throughput.
> - `hub` [[40-Topics/computational-methods|Computational methods]] — The tool layer: aligners, callers, imputers and integrators.

## All sources on this page

> [!info]- 8 summaries cited here
> - [[10-Summaries/abbasova-2025-cut-tag-encode-benchmark|Abbasova 2025]]
> - [[10-Summaries/bartosovic-2022-nano-cut-tag|Bartosovic 2022]]
> - [[10-Summaries/chen-2018-fastp|Chen 2018]]
> - [[10-Summaries/li-2009-samtools|Li 2009]]
> - [[10-Summaries/wesley-2026-songbird|Wesley 2026]]
> - [[10-Summaries/wu-2026-sccut-tag-review|Wu 2026]]
> - [[10-Summaries/zahn-2017-dlp|Zahn 2017]]
> - [[10-Summaries/zhang-2008-macs|Zhang 2008]]
