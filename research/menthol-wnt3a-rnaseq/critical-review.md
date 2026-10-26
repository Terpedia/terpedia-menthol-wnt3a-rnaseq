# Critical review: GSE242559 menthol × Wnt3a audit

This is an author-side review of the [executed notebook](../../notebooks/gse242559_menthol_wnt3a.ipynb) and [claim-linked report](generated/white-paper.md), not independent peer review.

## What the data support

The [GEO series](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242559) describes a balanced 2 × 2 design in ND7/23 cells: control, 100 µM menthol, 100 ng/mL Wnt3a, and both, each with three labeled libraries after six hours. The deposited 21,556-feature FPKM table is complete and checksum pinned. A processed-abundance interaction can therefore be **described within this one cell-line study**. This is a more direct menthol exposure than the commercial MentholMint aerosol in GSE263903.

## Main weaknesses

1. **No count-based inference was reproduced.** The supplementary file contains FPKM, not integer counts, read-level QC, a design matrix, or the authors' DESeq2 model. The [raw-run manifest](raw_run_manifest.tsv) now pins the twelve SRA runs and 24 paired ENA FASTQs with checksums, but their 33.4 GB have not been downloaded or quantified. The notebook's log2(FPKM + pseudocount) differences remain descriptive. It reports no p values, adjusted p values, pathway enrichment, or statistically supported interaction.
2. **Thresholds are fragile.** Among 10,783 features passing maximum arm-mean FPKM ≥ 1, 18 interaction scores have absolute magnitude ≥ 1 with pseudocount 0.1; only four do with pseudocount 1.0. Several highest ranked features are near the expression filter. Candidate ranking should not be treated as a robust gene list.
3. **Culture provenance is incomplete.** Three replicate labels occur per arm, but the deposited matrix does not establish independent cultures, paired measurements, randomization, or batch balance. The notebook does not infer those properties from column names.
4. **Target dependency is untested by this matrix.** `Trpm8` has a maximum arm mean of 0.276 FPKM, and `Tac1` is absent under that symbol. Small or missing transcript signals cannot rule out channel function, protein modification, secretion, or annotation differences. The [associated article](https://pubmed.ncbi.nlm.nih.gov/38280896/) reports additional pharmacologic and protein experiments, which this notebook does not reproduce.
5. **Chemical and context boundaries remain.** The audit does not confirm menthol stereochemistry, intracellular dose, or viability. ND7/23 cells, Wnt3a stimulation, and six-hour exposure differ from the mouse-lung mixed-aerosol experiment GSE263903. Their expression patterns cannot be pooled as replication of one chemical effect.

## Next research step

Use the [GEO/ENA run mapping](raw_run_manifest.tsv) to download and checksum the raw FASTQs on appropriately sized compute; verify culture and batch metadata, choose a versioned rat reference and annotation, and fit a replicate-aware menthol × Wnt3a count model. A target-dependency claim also needs an independently replicated menthol × Wnt3a × TRPM8-perturbation experiment with perturbation efficacy, rescue, viability, calcium or protein readouts, and measured exposure.
