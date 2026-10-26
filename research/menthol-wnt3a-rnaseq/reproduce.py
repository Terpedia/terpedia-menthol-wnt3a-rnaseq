"""Restore the pinned GEO input and regenerate the notebook and report."""

import json
import subprocess
import sys
from pathlib import Path


root = Path(__file__).resolve().parents[2]
slug = "menthol-wnt3a-rnaseq"
study = f"research/{slug}"
notebook = "notebooks/gse242559_menthol_wnt3a.ipynb"
spec = f"{study}/report-spec.json"
inputs = [
    f"{study}/data/GSE242559_FPKM_anno.txt.gz",
    f"{study}/source_manifest.tsv",
    f"{study}/sample_manifest.tsv",
]
artifacts = [f"{study}/results/{name}" for name in (
    "sample_qc.tsv", "feature_effects.tsv.gz", "priority_genes.tsv",
    "target_markers.tsv", "analysis_summary.json",
)]
commands = [
    [sys.executable, "restore-inputs.py", spec],
    [sys.executable, f"{study}/build_notebook.py"],
    [sys.executable, "notebook-runner.py", notebook, ".", "120", json.dumps(artifacts), json.dumps(inputs)],
    [sys.executable, f"{study}/build_spec.py"],
    ["node", "report-generator.mjs", spec],
]
for command in commands:
    subprocess.run(command, cwd=root, check=True)
