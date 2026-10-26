# Processed RNA-seq audit of menthol and Wnt3a in ND7/23 cells

> Generated evidence brief. Each statement is linked to a claim record; scientific interpretation still requires review.

**Research question:** Which metabolic and signaling responses to terpene exposure are reproducible, and which depend on cellular context or a specific target?

**Notebook:** `notebooks/gse242559_menthol_wnt3a.ipynb` · SHA-256 `2556f11ae261fe3b81eb90fd9e50e77cf8a4603be8068f0f9ca28179e1193543` · 5 executed code cells

## Abstract

**Source-reported:** GSE242559 reports twelve ND7/23 RNA-seq libraries after six hours: control, 100 µM menthol, 100 ng/mL Wnt3a, and their combination, with three replicate labels per arm. (claim C01; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242559))

**Observed in notebook:** The checksum-pinned deposited FPKM table contains 21,556 unique feature identifiers and twelve complete nonnegative abundance columns. Under a maximum arm-mean FPKM ≥ 1 filter, 10,783 features enter the descriptive interaction summary. (claim C02; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242559))

**Observed in notebook:** Among the 10,783 filtered features, 18 have an absolute descriptive menthol-by-Wnt3a interaction score of at least one log2 unit with a 0.1 FPKM pseudocount; only four do with a 1.0 pseudocount. (claim C04; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242559))

**Observed in notebook:** In a predeclared marker panel, Trpm8 has a maximum arm-mean abundance of 0.276 FPKM and a descriptive interaction score of +0.279; Gsk3b and Ctnnb1 scores are +0.073 and -0.018. Tac1 is not listed under that feature symbol in the deposited matrix. (claim C05; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242559), [2](https://pubmed.ncbi.nlm.nih.gov/38280896/))

**Source-reported:** GSE263903 is a separate mouse-lung single-cell study of a commercial menthol-mint aerosol containing nicotine and other constituents. (claim C07; [3](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE263903))

## Background

**Source-reported:** GSE242559 reports twelve ND7/23 RNA-seq libraries after six hours: control, 100 µM menthol, 100 ng/mL Wnt3a, and their combination, with three replicate labels per arm. (claim C01; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242559))

**Source-reported:** The associated article reports pharmacologic and protein-level evidence for a TRPM8–PKA/GSK-3β–substance P mechanism in its broader experimental program. (claim C06; [2](https://pubmed.ncbi.nlm.nih.gov/38280896/))

**Source-reported:** GSE263903 is a separate mouse-lung single-cell study of a commercial menthol-mint aerosol containing nicotine and other constituents. (claim C07; [3](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE263903))

## Methods

**Source-reported:** GSE242559 reports twelve ND7/23 RNA-seq libraries after six hours: control, 100 µM menthol, 100 ng/mL Wnt3a, and their combination, with three replicate labels per arm. (claim C01; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242559))

**Observed in notebook:** The checksum-pinned deposited FPKM table contains 21,556 unique feature identifiers and twelve complete nonnegative abundance columns. Under a maximum arm-mean FPKM ≥ 1 filter, 10,783 features enter the descriptive interaction summary. (claim C02; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242559)) Artifacts: [research/menthol-wnt3a-rnaseq/results/analysis_summary.json](../results/analysis_summary.json), [research/menthol-wnt3a-rnaseq/results/feature_effects.tsv.gz](../results/feature_effects.tsv.gz).

**Observed in notebook:** Within-arm sample Spearman correlations on log2(FPKM + 0.1) have a minimum of 0.972 across the twelve libraries. (claim C03; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242559)) Artifacts: [research/menthol-wnt3a-rnaseq/results/sample_qc.tsv](../results/sample_qc.tsv), [research/menthol-wnt3a-rnaseq/results/analysis_summary.json](../results/analysis_summary.json).

## Results

**Observed in notebook:** The checksum-pinned deposited FPKM table contains 21,556 unique feature identifiers and twelve complete nonnegative abundance columns. Under a maximum arm-mean FPKM ≥ 1 filter, 10,783 features enter the descriptive interaction summary. (claim C02; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242559)) Artifacts: [research/menthol-wnt3a-rnaseq/results/analysis_summary.json](../results/analysis_summary.json), [research/menthol-wnt3a-rnaseq/results/feature_effects.tsv.gz](../results/feature_effects.tsv.gz). **Limitation:** FPKM is processed abundance, not integer counts. This notebook does not reproduce the article's DESeq2 analysis or estimate differential-expression significance.

**Observed in notebook:** Within-arm sample Spearman correlations on log2(FPKM + 0.1) have a minimum of 0.972 across the twelve libraries. (claim C03; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242559)) Artifacts: [research/menthol-wnt3a-rnaseq/results/sample_qc.tsv](../results/sample_qc.tsv), [research/menthol-wnt3a-rnaseq/results/analysis_summary.json](../results/analysis_summary.json). **Limitation:** High whole-transcriptome correlation is a matrix consistency check, not proof of independent cultures, correct labels, or treatment effect.

**Observed in notebook:** Among the 10,783 filtered features, 18 have an absolute descriptive menthol-by-Wnt3a interaction score of at least one log2 unit with a 0.1 FPKM pseudocount; only four do with a 1.0 pseudocount. (claim C04; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242559)) Artifacts: [research/menthol-wnt3a-rnaseq/results/analysis_summary.json](../results/analysis_summary.json), [research/menthol-wnt3a-rnaseq/results/feature_effects.tsv.gz](../results/feature_effects.tsv.gz). **Limitation:** The threshold counts are pseudocount-sensitive descriptive summaries, not significant interaction calls or pathway enrichment. Several top-ranked features are near the expression filter.

**Observed in notebook:** In a predeclared marker panel, Trpm8 has a maximum arm-mean abundance of 0.276 FPKM and a descriptive interaction score of +0.279; Gsk3b and Ctnnb1 scores are +0.073 and -0.018. Tac1 is not listed under that feature symbol in the deposited matrix. (claim C05; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242559), [2](https://pubmed.ncbi.nlm.nih.gov/38280896/)) Artifacts: [research/menthol-wnt3a-rnaseq/results/target_markers.tsv](../results/target_markers.tsv). **Limitation:** A low transcript abundance or small transcript contrast does not exclude receptor activity, protein modification, or downstream signaling. A missing symbol may reflect annotation rather than true absence.

## Interpretation

**Observed in notebook:** Among the 10,783 filtered features, 18 have an absolute descriptive menthol-by-Wnt3a interaction score of at least one log2 unit with a 0.1 FPKM pseudocount; only four do with a 1.0 pseudocount. (claim C04; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242559)) Artifacts: [research/menthol-wnt3a-rnaseq/results/analysis_summary.json](../results/analysis_summary.json), [research/menthol-wnt3a-rnaseq/results/feature_effects.tsv.gz](../results/feature_effects.tsv.gz). **Limitation:** The threshold counts are pseudocount-sensitive descriptive summaries, not significant interaction calls or pathway enrichment. Several top-ranked features are near the expression filter.

**Observed in notebook:** In a predeclared marker panel, Trpm8 has a maximum arm-mean abundance of 0.276 FPKM and a descriptive interaction score of +0.279; Gsk3b and Ctnnb1 scores are +0.073 and -0.018. Tac1 is not listed under that feature symbol in the deposited matrix. (claim C05; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242559), [2](https://pubmed.ncbi.nlm.nih.gov/38280896/)) Artifacts: [research/menthol-wnt3a-rnaseq/results/target_markers.tsv](../results/target_markers.tsv). **Limitation:** A low transcript abundance or small transcript contrast does not exclude receptor activity, protein modification, or downstream signaling. A missing symbol may reflect annotation rather than true absence.

**Source-reported:** The associated article reports pharmacologic and protein-level evidence for a TRPM8–PKA/GSK-3β–substance P mechanism in its broader experimental program. (claim C06; [2](https://pubmed.ncbi.nlm.nih.gov/38280896/)) **Limitation:** Those experiments are not reanalyzed here. The deposited FPKM contrasts alone do not establish TRPM8 binding, genetic dependency, or a replicated pathway effect.

**Source-reported:** GSE263903 is a separate mouse-lung single-cell study of a commercial menthol-mint aerosol containing nicotine and other constituents. (claim C07; [3](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE263903)) **Limitation:** Different species, tissue, formulation, assay, and design prevent pooling it with GSE242559 as replication of purified menthol.

## Limitations

**Claim C01 (source-reported):** GSE242559 reports twelve ND7/23 RNA-seq libraries after six hours: control, 100 µM menthol, 100 ng/mL Wnt3a, and their combination, with three replicate labels per arm. **Limitation:** The matrix columns are assigned to GEO sample titles by matching treatment and replicate abbreviations; this audit does not independently verify culture pairing, randomization, batch, menthol stereochemistry, or intracellular exposure. ([1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242559))

**Claim C02 (observed):** The checksum-pinned deposited FPKM table contains 21,556 unique feature identifiers and twelve complete nonnegative abundance columns. Under a maximum arm-mean FPKM ≥ 1 filter, 10,783 features enter the descriptive interaction summary. **Limitation:** FPKM is processed abundance, not integer counts. This notebook does not reproduce the article's DESeq2 analysis or estimate differential-expression significance. ([1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242559))

**Claim C03 (observed):** Within-arm sample Spearman correlations on log2(FPKM + 0.1) have a minimum of 0.972 across the twelve libraries. **Limitation:** High whole-transcriptome correlation is a matrix consistency check, not proof of independent cultures, correct labels, or treatment effect. ([1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242559))

**Claim C04 (observed):** Among the 10,783 filtered features, 18 have an absolute descriptive menthol-by-Wnt3a interaction score of at least one log2 unit with a 0.1 FPKM pseudocount; only four do with a 1.0 pseudocount. **Limitation:** The threshold counts are pseudocount-sensitive descriptive summaries, not significant interaction calls or pathway enrichment. Several top-ranked features are near the expression filter. ([1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242559))

**Claim C05 (observed):** In a predeclared marker panel, Trpm8 has a maximum arm-mean abundance of 0.276 FPKM and a descriptive interaction score of +0.279; Gsk3b and Ctnnb1 scores are +0.073 and -0.018. Tac1 is not listed under that feature symbol in the deposited matrix. **Limitation:** A low transcript abundance or small transcript contrast does not exclude receptor activity, protein modification, or downstream signaling. A missing symbol may reflect annotation rather than true absence. ([1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242559), [2](https://pubmed.ncbi.nlm.nih.gov/38280896/))

**Claim C07 (source-reported):** GSE263903 is a separate mouse-lung single-cell study of a commercial menthol-mint aerosol containing nicotine and other constituents. **Limitation:** Different species, tissue, formulation, assay, and design prevent pooling it with GSE242559 as replication of purified menthol. ([3](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE263903))

## Next research steps

**Proposed:** A stronger dependency experiment would repeat a dose-resolved, randomized menthol × Wnt3a design with independent cultures, measured exposure, raw integer counts, and verified TRPM8 perturbation plus rescue. Estimate treatment, context, and chemical-by-genotype interactions with replicate-level uncertainty and orthogonal protein or calcium readouts. (claim C08; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242559), [2](https://pubmed.ncbi.nlm.nih.gov/38280896/))

## Data and code availability

The source specification is `research/menthol-wnt3a-rnaseq/report-spec.json` (SHA-256 `2e4a0c1af31d70ec460a63c7efd95581d486accb0a325d642ba5becfc9cf109e`). The claim ledger and generation receipt accompany this report. File hashes identify the report files and cited result artifacts. 1 externally sourced input file has a source URL and hash listed below. The [notebook execution receipt](../../execution-receipts/gse242559_menthol_wnt3a.json) matches the saved notebook and records hashes for result files written during its fresh-kernel run. It also pins 3 declared local input files by SHA-256. It records the Python version and installed package versions. Notebook execution does not independently validate scientific interpretation.

### External data files

The following download locations and file hashes match inputs pinned by the notebook execution receipt. The generator does not download these files or verify that the URLs remain live.

| Input | Download | SHA-256 |
| --- | --- | --- |
| `research/menthol-wnt3a-rnaseq/data/GSE242559_FPKM_anno.txt.gz` | [Source file](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE242nnn/GSE242559/suppl/GSE242559_FPKM_anno.txt.gz) | `fa3149865f0445ad95d5fdb757613f89018e72fd18edc0221b7757adf9044d30` |

## References

[1] NCBI GEO GSE242559 deposited RNA-seq design and FPKM matrix. https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242559
[2] Zhang et al., Cell Death & Disease 2024, PMID 38280896. https://pubmed.ncbi.nlm.nih.gov/38280896/
[3] NCBI GEO GSE263903 mixed-aerosol mouse-lung single-cell study. https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE263903
