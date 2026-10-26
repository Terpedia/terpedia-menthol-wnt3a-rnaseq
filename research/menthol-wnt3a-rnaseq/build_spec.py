"""Build the claim-linked Terputer report specification for GSE242559."""

import csv
import json
from pathlib import Path


root = Path(__file__).resolve().parents[2]
study = root / "research/menthol-wnt3a-rnaseq"
with (study / "source_manifest.tsv").open() as stream:
    source = next(csv.DictReader(stream, delimiter="\t"))

spec = {
    "schema_version": 2,
    "slug": "menthol-wnt3a-rnaseq",
    "title": "Processed RNA-seq audit of menthol and Wnt3a in ND7/23 cells",
    "question": "Which metabolic and signaling responses to terpene exposure are reproducible, and which depend on cellular context or a specific target?",
    "notebook": "notebooks/gse242559_menthol_wnt3a.ipynb",
    "execution_receipt": "research/execution-receipts/gse242559_menthol_wnt3a.json",
    "data_inputs": [{"path": f"research/menthol-wnt3a-rnaseq/data/{source['filename']}", "url": source["url"], "sha256": source["sha256"]}],
    "sources": [
        {"id": "geo", "title": "NCBI GEO GSE242559 deposited RNA-seq design and FPKM matrix", "url": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE242559"},
        {"id": "article", "title": "Zhang et al., Cell Death & Disease 2024, PMID 38280896", "url": "https://pubmed.ncbi.nlm.nih.gov/38280896/"},
        {"id": "aerosol", "title": "NCBI GEO GSE263903 mixed-aerosol mouse-lung single-cell study", "url": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE263903"},
    ],
    "claims": [
        {"id": "C01", "class": "source-reported", "text": "GSE242559 reports twelve ND7/23 RNA-seq libraries after six hours: control, 100 µM menthol, 100 ng/mL Wnt3a, and their combination, with three replicate labels per arm.", "sources": ["geo"], "limitation": "The matrix columns are assigned to GEO sample titles by matching treatment and replicate abbreviations; this audit does not independently verify culture pairing, randomization, batch, menthol stereochemistry, or intracellular exposure."},
        {"id": "C02", "class": "observed", "text": "The checksum-pinned deposited FPKM table contains 21,556 unique feature identifiers and twelve complete nonnegative abundance columns. Under a maximum arm-mean FPKM ≥ 1 filter, 10,783 features enter the descriptive interaction summary.", "sources": ["geo"], "artifacts": ["research/menthol-wnt3a-rnaseq/results/analysis_summary.json", "research/menthol-wnt3a-rnaseq/results/feature_effects.tsv.gz"], "limitation": "FPKM is processed abundance, not integer counts. This notebook does not reproduce the article's DESeq2 analysis or estimate differential-expression significance."},
        {"id": "C03", "class": "observed", "text": "Within-arm sample Spearman correlations on log2(FPKM + 0.1) have a minimum of 0.972 across the twelve libraries.", "sources": ["geo"], "artifacts": ["research/menthol-wnt3a-rnaseq/results/sample_qc.tsv", "research/menthol-wnt3a-rnaseq/results/analysis_summary.json"], "limitation": "High whole-transcriptome correlation is a matrix consistency check, not proof of independent cultures, correct labels, or treatment effect."},
        {"id": "C04", "class": "observed", "text": "Among the 10,783 filtered features, 18 have an absolute descriptive menthol-by-Wnt3a interaction score of at least one log2 unit with a 0.1 FPKM pseudocount; only four do with a 1.0 pseudocount.", "sources": ["geo"], "artifacts": ["research/menthol-wnt3a-rnaseq/results/analysis_summary.json", "research/menthol-wnt3a-rnaseq/results/feature_effects.tsv.gz"], "limitation": "The threshold counts are pseudocount-sensitive descriptive summaries, not significant interaction calls or pathway enrichment. Several top-ranked features are near the expression filter."},
        {"id": "C05", "class": "observed", "text": "In a predeclared marker panel, Trpm8 has a maximum arm-mean abundance of 0.276 FPKM and a descriptive interaction score of +0.279; Gsk3b and Ctnnb1 scores are +0.073 and -0.018. Tac1 is not listed under that feature symbol in the deposited matrix.", "sources": ["geo", "article"], "artifacts": ["research/menthol-wnt3a-rnaseq/results/target_markers.tsv"], "limitation": "A low transcript abundance or small transcript contrast does not exclude receptor activity, protein modification, or downstream signaling. A missing symbol may reflect annotation rather than true absence."},
        {"id": "C06", "class": "source-reported", "text": "The associated article reports pharmacologic and protein-level evidence for a TRPM8–PKA/GSK-3β–substance P mechanism in its broader experimental program.", "sources": ["article"], "limitation": "Those experiments are not reanalyzed here. The deposited FPKM contrasts alone do not establish TRPM8 binding, genetic dependency, or a replicated pathway effect."},
        {"id": "C07", "class": "source-reported", "text": "GSE263903 is a separate mouse-lung single-cell study of a commercial menthol-mint aerosol containing nicotine and other constituents.", "sources": ["aerosol"], "limitation": "Different species, tissue, formulation, assay, and design prevent pooling it with GSE242559 as replication of purified menthol."},
        {"id": "C08", "class": "proposed", "text": "A stronger dependency experiment would repeat a dose-resolved, randomized menthol × Wnt3a design with independent cultures, measured exposure, raw integer counts, and verified TRPM8 perturbation plus rescue. Estimate treatment, context, and chemical-by-genotype interactions with replicate-level uncertainty and orthogonal protein or calcium readouts.", "sources": ["geo", "article"], "limitation": "This experiment is proposed; no new perturbation or count model was performed by this project."},
    ],
    "abstract": ["C01", "C02", "C04", "C05", "C07"],
    "sections": {
        "background": ["C01", "C06", "C07"],
        "methods": ["C01", "C02", "C03"],
        "results": ["C02", "C03", "C04", "C05"],
        "interpretation": ["C04", "C05", "C06", "C07"],
        "limitations": ["C01", "C02", "C03", "C04", "C05", "C07"],
        "next_steps": ["C08"],
    },
}
(study / "report-spec.json").write_text(json.dumps(spec, indent=2) + "\n")
print(study / "report-spec.json")
