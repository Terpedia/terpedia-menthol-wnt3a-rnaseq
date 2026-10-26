# GSE242559 menthol × Wnt3a RNA-seq audit

This forkable Terputer project analyzes the [public GSE242559](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242559) processed FPKM matrix from ND7/23 cells exposed to menthol, Wnt3a, both, or neither for six hours. It contains an [executed Jupyter notebook](notebooks/gse242559_menthol_wnt3a.ipynb), [claim-linked white paper](research/menthol-wnt3a-rnaseq/generated/white-paper.md), [critical review](research/menthol-wnt3a-rnaseq/critical-review.md), source manifest, result tables, and execution receipts.

The source describes three libraries per arm. The notebook audits 21,556 features and reports descriptive processed-abundance contrasts. Of 10,783 features passing its expression filter, 18 have an absolute menthol-by-Wnt3a interaction score ≥ 1 at pseudocount 0.1, versus four at pseudocount 1.0. `Trpm8` is low abundance and `Tac1` is not listed under that symbol. These observations do **not** reproduce the article's count-based differential-expression analysis or establish a TRPM8-dependent transcriptomic program. The [source article](https://pubmed.ncbi.nlm.nih.gov/38280896/) contains separate pharmacologic and protein evidence.

## Raw-run provenance for count reanalysis

The [raw-run manifest](research/menthol-wnt3a-rnaseq/raw_run_manifest.tsv) joins each of the twelve GEO sample records to its SRA experiment and ENA run, then records both paired FASTQ URLs, byte sizes, and MD5 checksums. [Source hashes and retrieval time](research/menthol-wnt3a-rnaseq/raw_run_sources.json) pin the GEO SOFT and ENA API responses used for that join. The 24 FASTQs total 33,399,533,782 bytes (33.4 GB). Regenerate the mapping with `python3 research/menthol-wnt3a-rnaseq/build_raw_run_manifest.py` and review any archive changes before replacing the committed manifest. No raw reads were downloaded or quantified in this project, and no count-based model has been fit. The manifest provides an auditable starting point for that work.

## Reproduce

The 5.4 MB GEO input is omitted from Git. Its URL, byte count, and SHA-256 are pinned in [source_manifest.tsv](research/menthol-wnt3a-rnaseq/source_manifest.tsv) and the report specification. From the repository root, with Python 3.11+ and Node.js:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python research/menthol-wnt3a-rnaseq/reproduce.py
```

The script restores and checks the source, executes the notebook in a fresh kernel, captures result and input hashes, and regenerates the report. Review the [sample QC](research/menthol-wnt3a-rnaseq/results/sample_qc.tsv), [target panel](research/menthol-wnt3a-rnaseq/results/target_markers.tsv), and [critical review](research/menthol-wnt3a-rnaseq/critical-review.md) before interpreting the interaction scores.
