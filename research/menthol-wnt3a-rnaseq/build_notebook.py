"""Build the source-pinned GSE242559 processed-expression notebook."""

from pathlib import Path

import nbformat


root = Path(__file__).resolve().parents[2]
output = root / "notebooks/gse242559_menthol_wnt3a.ipynb"
cells = [
    nbformat.v4.new_markdown_cell("""# Menthol × Wnt3a in ND7/23 cells: processed RNA-seq audit

**Question.** Does the deposited 12-library matrix show a context-sensitive menthol response in the presence of Wnt3a?

GSE242559 reports three libraries for each of control, 100 µM menthol, 100 ng/mL Wnt3a, and their combination after 6 h. This notebook audits the deposited FPKM matrix, not raw counts. Its contrasts and interaction scores describe processed abundance and are **not** DESeq2 results, adjusted-p-value calls, a validated pathway test, or proof of TRPM8 dependency. The source article's pharmacology is separate evidence."""),
    nbformat.v4.new_code_cell("""import csv
import hashlib
import json
from pathlib import Path
import numpy as np
import pandas as pd

root = Path.cwd()
study = root / 'research/menthol-wnt3a-rnaseq'
data_path = study / 'data/GSE242559_FPKM_anno.txt.gz'
with (study / 'source_manifest.tsv').open() as source:
    source_manifest = list(csv.DictReader(source, delimiter='\\t'))
with (study / 'sample_manifest.tsv').open() as source:
    samples = pd.DataFrame(list(csv.DictReader(source, delimiter='\\t')))
assert len(source_manifest) == 1 and len(samples) == 12
expected = source_manifest[0]['sha256']
actual = hashlib.sha256(data_path.read_bytes()).hexdigest()
assert actual == expected, 'Downloaded source hash differs from the pinned GEO file'
assert data_path.stat().st_size == int(source_manifest[0]['bytes'])
matrix = pd.read_csv(data_path, sep='\\t', compression='gzip')
columns = samples['matrix_column'].tolist()
assert matrix['id'].is_unique and not matrix['id'].isna().any()
assert len(set(columns)) == 12 and set(columns) <= set(matrix)
values = matrix.set_index('id')[columns].apply(pd.to_numeric, errors='raise')
assert np.isfinite(values.to_numpy()).all() and (values.to_numpy() >= 0).all()
assert samples.groupby('condition').size().to_dict() == {'Control': 3, 'Menthol': 3, 'Menthol+Wnt3a': 3, 'Wnt3a': 3}
print('source_sha256', actual, 'features', len(values), 'libraries', len(columns))"""),
    nbformat.v4.new_code_cell("""# Source matrix QC. Each column is one library; sample titles do not document pairing.
log_values = np.log2(values + 0.1)
rows = []
for sample in samples.itertuples(index=False):
    column = values[sample.matrix_column]
    peers = samples.loc[(samples.condition == sample.condition) & (samples.matrix_column != sample.matrix_column), 'matrix_column'].tolist()
    correlations = [log_values[sample.matrix_column].corr(log_values[peer], method='spearman') for peer in peers]
    rows.append({'gsm': sample.gsm, 'matrix_column': sample.matrix_column, 'condition': sample.condition,
                 'replicate_label': sample.replicate, 'features_detected_fpkm_gt_0': int((column > 0).sum()),
                 'sum_fpkm': float(column.sum()), 'within_condition_min_spearman': min(correlations)})
qc = pd.DataFrame(rows)
qc.to_csv(study / 'results/sample_qc.tsv', sep='\\t', index=False)
print(qc[['condition', 'matrix_column', 'features_detected_fpkm_gt_0', 'within_condition_min_spearman']].to_string(index=False))"""),
    nbformat.v4.new_markdown_cell("""## Factorial description

For every feature, transform each sample as log2(FPKM + 0.1), then average within each named arm. The menthol contrast without Wnt3a is `M − C`; with Wnt3a it is `MW − W`. Their difference is a descriptive interaction score. Replicate labels are treated as labels, not inferred pairs. The deposited matrix does not supply integer counts, library QC, or the authors' DESeq2 fit, so no p values are assigned here."""),
    nbformat.v4.new_code_cell("""groups = {name: samples.loc[samples.condition == name, 'matrix_column'].tolist()
          for name in ('Control', 'Menthol', 'Wnt3a', 'Menthol+Wnt3a')}
means = {name: log_values[cols].mean(axis=1) for name, cols in groups.items()}
raw_means = {name: values[cols].mean(axis=1) for name, cols in groups.items()}
effect = pd.DataFrame(index=values.index)
effect['max_group_mean_fpkm'] = pd.concat(raw_means, axis=1).max(axis=1)
effect['menthol_without_wnt3a_log2_fpkm_delta'] = means['Menthol'] - means['Control']
effect['menthol_with_wnt3a_log2_fpkm_delta'] = means['Menthol+Wnt3a'] - means['Wnt3a']
effect['wnt3a_without_menthol_log2_fpkm_delta'] = means['Wnt3a'] - means['Control']
effect['interaction_difference'] = effect['menthol_with_wnt3a_log2_fpkm_delta'] - effect['menthol_without_wnt3a_log2_fpkm_delta']
effect['expressed'] = effect.max_group_mean_fpkm >= 1
effect.index.name = 'feature_id'
effect.to_csv(study / 'results/feature_effects.tsv.gz', sep='\\t',
              compression={'method': 'gzip', 'mtime': 0})
selected = effect.loc[effect.expressed].copy()
selected['abs_interaction'] = selected.interaction_difference.abs()
priority = selected.sort_values('abs_interaction', ascending=False).head(25).drop(columns='abs_interaction').reset_index()
priority.to_csv(study / 'results/priority_genes.tsv', sep='\\t', index=False)
print('expressed_features', len(selected), 'top_descriptive_interactions')
print(priority.head(10).to_string(index=False))"""),
    nbformat.v4.new_code_cell("""# A declared marker panel, with absent source features recorded as absent rather than zero.
markers = ['Trpm8', 'Tac1', 'Gsk3b', 'Ctnnb1', 'Prkaca', 'Prkacb']
panel = []
for name in markers:
    matches = effect.loc[[feature for feature in effect.index if feature.casefold() == name.casefold()]]
    if matches.empty:
        panel.append({'marker': name, 'source_feature': '', 'present_in_matrix': False,
                      'max_group_mean_fpkm': None, 'menthol_without_wnt3a_log2_fpkm_delta': None,
                      'menthol_with_wnt3a_log2_fpkm_delta': None, 'interaction_difference': None})
    else:
        feature = matches.index[0]
        row = matches.iloc[0]
        panel.append({'marker': name, 'source_feature': feature, 'present_in_matrix': True,
                      'max_group_mean_fpkm': row.max_group_mean_fpkm,
                      'menthol_without_wnt3a_log2_fpkm_delta': row.menthol_without_wnt3a_log2_fpkm_delta,
                      'menthol_with_wnt3a_log2_fpkm_delta': row.menthol_with_wnt3a_log2_fpkm_delta,
                      'interaction_difference': row.interaction_difference})
panel = pd.DataFrame(panel)
panel.to_csv(study / 'results/target_markers.tsv', sep='\\t', index=False)
print(panel.to_string(index=False))"""),
    nbformat.v4.new_code_cell("""# Pseudocount sensitivity and descriptive summary, not statistical discovery counts.
log_values_pc1 = np.log2(values + 1.0)
mean_pc1 = {name: log_values_pc1[cols].mean(axis=1) for name, cols in groups.items()}
interaction_pc1 = ((mean_pc1['Menthol+Wnt3a'] - mean_pc1['Wnt3a'])
                   - (mean_pc1['Menthol'] - mean_pc1['Control']))
summary = {
    'source_accession': 'GSE242559', 'source_sha256': actual, 'assay': 'processed FPKM from bulk RNA-seq',
    'features': len(values), 'libraries': len(columns), 'replicates_per_arm': 3,
    'expressed_feature_filter': 'maximum arm mean FPKM >= 1', 'expressed_features': len(selected),
    'pseudocount_primary': 0.1,
    'interaction_abs_ge_1_pc_0_1': int((selected.interaction_difference.abs() >= 1).sum()),
    'interaction_abs_ge_1_pc_1_0': int((interaction_pc1.loc[selected.index].abs() >= 1).sum()),
    'interaction_sign_concordance_pc_0_1_vs_1_0': float((np.sign(selected.interaction_difference) == np.sign(interaction_pc1.loc[selected.index])).mean()),
    'minimum_within_arm_spearman': float(qc.within_condition_min_spearman.min()),
    'limitations': ['Processed FPKM is not raw integer count data; no formal differential-expression or pathway significance is estimated.',
                    'The matrix does not establish paired replicates, independent culture provenance, or batch balance.',
                    'Menthol stereochemistry and measured cellular exposure are not confirmed in this audit.',
                    'Expression interaction is not evidence of TRPM8 binding or genetic dependency.']
}
(study / 'results/analysis_summary.json').write_text(json.dumps(summary, indent=2) + '\\n')
print(json.dumps(summary, indent=2))"""),
    nbformat.v4.new_markdown_cell("""## Interpretation

The notebook yields a reproducible **processed-expression description** of a 2 × 2 menthol/Wnt3a design. A large interaction score can nominate features for count-based analysis; it does not prove a pathway or a target. The GSE263903 lung aerosol study is a different species, tissue, assay, and mixed formulation, so the two studies cannot be pooled as independent replication of purified menthol."""),
]
notebook = nbformat.v4.new_notebook(cells=cells, metadata={"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}})
output.parent.mkdir(parents=True, exist_ok=True)
nbformat.write(notebook, output)
print(output.relative_to(root))
