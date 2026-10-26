"""Join official GEO sample-to-experiment links with ENA FASTQ metadata."""

import csv
import gzip
import hashlib
import io
import json
import re
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


HERE = Path(__file__).resolve().parent
GEO_URL = "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE242nnn/GSE242559/soft/GSE242559_family.soft.gz"
ENA_URL = "https://www.ebi.ac.uk/ena/portal/api/search?" + urllib.parse.urlencode({
    "result": "read_run", "query": 'study_accession="PRJNA1013943"',
    "fields": "run_accession,experiment_accession,sample_accession,secondary_sample_accession,fastq_ftp,fastq_md5,fastq_bytes,library_layout",
    "format": "tsv", "limit": "0",
})


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "Terpedia GSE242559 raw-run audit"})
    with urllib.request.urlopen(request, timeout=60) as stream:
        return stream.read()


with (HERE / "sample_manifest.tsv").open(newline="") as stream:
    samples = list(csv.DictReader(stream, delimiter="\t"))
if len(samples) != 12 or len({row["gsm"] for row in samples}) != 12:
    raise ValueError("Expected twelve unique GSE242559 sample labels")

geo_gz = fetch(GEO_URL)
geo_text = gzip.decompress(geo_gz).decode("utf-8")
sample_to_experiment = {}
current_gsm = None
for line in geo_text.splitlines():
    if line.startswith("^SAMPLE = "):
        current_gsm = line.partition(" = ")[2].strip()
    elif line.startswith("!Sample_relation = SRA:"):
        experiment = re.search(r"\bSRX\d+\b", line)
        if current_gsm and experiment:
            sample_to_experiment[current_gsm] = experiment.group()
if set(sample_to_experiment) != {row["gsm"] for row in samples}:
    raise ValueError("GEO sample-to-SRA experiment mapping does not match the pinned sample manifest")

ena_bytes = fetch(ENA_URL)
ena_rows = list(csv.DictReader(io.StringIO(ena_bytes.decode("utf-8")), delimiter="\t"))
by_experiment = {}
for row in ena_rows:
    by_experiment.setdefault(row["experiment_accession"], []).append(row)
if set(by_experiment) != set(sample_to_experiment.values()):
    raise ValueError("ENA experiments do not exactly match GEO sample relations")

columns = ["gsm", "matrix_column", "condition", "replicate", "experiment_accession",
           "run_accession", "biosample_accession", "library_layout", "mate",
           "fastq_url", "fastq_md5", "fastq_bytes"]
manifest = []
for sample in samples:
    experiment = sample_to_experiment[sample["gsm"]]
    runs = by_experiment[experiment]
    if len(runs) != 1 or runs[0]["library_layout"] != "PAIRED":
        raise ValueError(f"Expected one paired ENA run for {experiment}")
    run = runs[0]
    urls = run["fastq_ftp"].split(";")
    md5s = run["fastq_md5"].split(";")
    sizes = run["fastq_bytes"].split(";")
    if not (len(urls) == len(md5s) == len(sizes) == 2):
        raise ValueError(f"Expected two complete FASTQ mate records for {experiment}")
    for mate, (url, md5, size) in enumerate(zip(urls, md5s, sizes), start=1):
        if not re.fullmatch(r"[0-9a-f]{32}", md5) or int(size) <= 0:
            raise ValueError(f"Invalid checksum or size for {experiment} mate {mate}")
        manifest.append({
            "gsm": sample["gsm"], "matrix_column": sample["matrix_column"],
            "condition": sample["condition"], "replicate": sample["replicate"],
            "experiment_accession": experiment, "run_accession": run["run_accession"],
            "biosample_accession": run["sample_accession"], "library_layout": "PAIRED",
            "mate": mate, "fastq_url": "https://" + url.removeprefix("https://").removeprefix("ftp://"),
            "fastq_md5": md5, "fastq_bytes": int(size),
        })

with (HERE / "raw_run_manifest.tsv").open("w", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=columns, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(manifest)
receipt = {
    "accession": "GSE242559", "bioproject": "PRJNA1013943",
    "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
    "geo_soft_url": GEO_URL, "geo_soft_gz_sha256": hashlib.sha256(geo_gz).hexdigest(),
    "ena_api_url": ENA_URL, "ena_response_sha256": hashlib.sha256(ena_bytes).hexdigest(),
    "sample_manifest_sha256": hashlib.sha256((HERE / "sample_manifest.tsv").read_bytes()).hexdigest(),
    "raw_run_manifest_sha256": hashlib.sha256((HERE / "raw_run_manifest.tsv").read_bytes()).hexdigest(),
    "samples": len(samples), "runs": len(ena_rows), "fastq_files": len(manifest),
    "total_fastq_bytes": sum(row["fastq_bytes"] for row in manifest),
    "reads_downloaded": False, "counts_estimated": False,
}
(HERE / "raw_run_sources.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps({key: receipt[key] for key in ("samples", "runs", "fastq_files", "total_fastq_bytes")}))
