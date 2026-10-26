# GSE242559 menthol × Wnt3a RNA-seq audit

This forkable Terputer project analyzes the [public GSE242559](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242559) processed FPKM matrix from ND7/23 cells exposed to menthol, Wnt3a, both, or neither for six hours. It contains an [executed Jupyter notebook](notebooks/gse242559_menthol_wnt3a.ipynb), [claim-linked white paper](research/menthol-wnt3a-rnaseq/generated/white-paper.md), [critical review](research/menthol-wnt3a-rnaseq/critical-review.md), source manifest, result tables, and execution receipts.

The source describes three libraries per arm. The notebook audits 21,556 features and reports descriptive processed-abundance contrasts. Of 10,783 features passing its expression filter, 18 have an absolute menthol-by-Wnt3a interaction score ≥ 1 at pseudocount 0.1, versus four at pseudocount 1.0. `Trpm8` is low abundance and `Tac1` is not listed under that symbol. These observations do **not** reproduce the article's count-based differential-expression analysis or establish a TRPM8-dependent transcriptomic program. The [source article](https://pubmed.ncbi.nlm.nih.gov/38280896/) contains separate pharmacologic and protein evidence.

## Reproduce

The 5.4 MB GEO input is omitted from Git. Its URL, byte count, and SHA-256 are pinned in [source_manifest.tsv](research/menthol-wnt3a-rnaseq/source_manifest.tsv) and the report specification. From the repository root, with Python 3.11+ and Node.js:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python research/menthol-wnt3a-rnaseq/reproduce.py
```

The script restores and checks the source, executes the notebook in a fresh kernel, captures result and input hashes, and regenerates the report. Review the [sample QC](research/menthol-wnt3a-rnaseq/results/sample_qc.tsv), [target panel](research/menthol-wnt3a-rnaseq/results/target_markers.tsv), and [critical review](research/menthol-wnt3a-rnaseq/critical-review.md) before interpreting the interaction scores.
