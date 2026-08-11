# Declared priors of the blind coder (fresh agent context)

**Date:** 2026-08-11, written after reading `CODEBOOK.md` and before opening
any of the seventeen papers or any other file in this repository.
**Coder:** fresh AI agent context. I have not read
`AJ_Handover_and_Tier2_Protocol.md`, `DECLARED_PRIORS.md`, anything in
`ap44/`, any `.docx`, `G_dataset.csv`, `G_landscape.png`, `appc_tier1.py`,
or anything in `provenance/`, and I will not.

## What I know about the corpus / theory being tested

Nothing. I do not know what "the 420 code" predicts, what the corpus's
predicted G values are, what Tier 1 found, or what residual pattern (if any)
exists. I have not searched for any of these and will not.

## Training-data contamination: published G values

I cannot un-know the published literature. The protocol acknowledges this.
Below, honestly, is what I believe from training data about where each
experiment's result sits **relative to the modern consensus (CODATA-era)
mean** — direction only, no numerals recorded. Confidence is my own
subjective label (high / medium / low).

| id | prior belief (relative to consensus mean) | confidence |
|---|---|---|
| NIST-82 | slightly low | medium |
| TR&D-96 | slightly low to near mean | low |
| LANL-97 | near mean | medium |
| UWash-00 | essentially at the mean (it anchors it) | high |
| BIPM-01 | high (one of the highest) | high |
| UWup-02 | near mean, large uncertainty | medium |
| MSL-03 | slightly low | medium |
| HUST-05 | low | medium |
| UZur-06 | near mean | high |
| HUST-09 | slightly low | medium |
| LENS-14 | low, large uncertainty | medium |
| BIPM-14 | high (one of the highest) | high |
| UCI-14 | near mean | low |
| HUST-T-18 | near mean, very small uncertainty | high |
| HUST-A-18 | near mean (very slightly above HUST-T-18) | high |
| JILA-18 | low (one of the lowest) | high |
| NIST-26 | **no prior** — publication postdates my training data; I do not know this result | — |

I also hold the general training-data belief that the seventeen results are
mutually discrepant far beyond their stated uncertainties (the well-known
"big G problem"), and that the two BIPM results (high) and JILA (low) frame
the spread. I do **not** hold any prior belief connecting boundary physics
(containment, enclosure, sphericity) to the sign of any residual — I have
never seen such an analysis in training data, and I do not know what
pattern this study hypothesises.

## Apparatus knowledge from training data

I have substantial training-data knowledge of most of these apparatuses
(fibre vs strip suspensions, vacuum chambers, source-mass placement). Per
protocol I will nevertheless code each dimension from the located primary
source's apparatus/method text and figures, and record exactly which source
I coded from. Where I cannot adequately source an experiment, I will say so
in `CODING_NOTES.md` rather than code from memory alone.

## Commitments

1. I will read only apparatus/method sections; no abstracts, results,
   conclusions, or G values. Unavoidable glimpses will be logged.
2. I will pull the seventeen authoritative citations from the CODATA 2022
   adjustment review (arXiv:2409.03787) reference list, not from memory,
   taking care to extract citations only and not the results table.
3. No git commands; three files only (`DECLARED_PRIORS_CODER.md`,
   `CODED_TABLE.csv`, `CODING_NOTES.md`).
