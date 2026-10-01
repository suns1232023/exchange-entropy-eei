
import os
import json
import csv
from datetime import datetime


def append_daily_log_and_json(metrics: dict, output_dir: str = "data") -> None:
    """
    Persist the daily EEI results to three output files:

    1. eei_latest_metrics.json  — overwritten with the latest snapshot
    2. eei_history_series.csv   — appended with one new row (monotonic history)
    3. daily_log.md             — appended with a formatted Markdown entry

    The CSV append ensures the history series grows daily without losing
    previous records, matching the intent of the GitHub Actions commit step.
    """
    os.makedirs(output_dir, exist_ok=True)

    # ------------------------------------------------------------------
    # 1. Overwrite latest JSON snapshot
    # ------------------------------------------------------------------
    json_path = os.path.join(output_dir, "eei_latest_metrics.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2, ensure_ascii=False)
        f.write("\n")

    # ------------------------------------------------------------------
    # 2. Append one row to the CSV history series
    #    Columns must match the existing schema in eei_history_series.csv
    # ------------------------------------------------------------------
    csv_path = os.path.join(output_dir, "eei_history_series.csv")
    csv_columns = [
        "timestamp", "date", "eei_value", "regime",
        "cov_fundamental_price", "cov_narrative_price",
        "var_price", "sample_size",
    ]

    file_exists = os.path.isfile(csv_path)
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=csv_columns, extrasaction="ignore")
        if not file_exists:
            writer.writeheader()
        writer.writerow({col: metrics.get(col, "") for col in csv_columns})

    # ------------------------------------------------------------------
    # 3. Append formatted Markdown entry to daily log
    # ------------------------------------------------------------------
    log_path = os.path.join(output_dir, "daily_log.md")
    markdown_entry = f"""
## 📈 Daily EEI Calculation Log ({metrics['timestamp']})

| Metric | Value |
| :--- | :--- |
| **Execution Timestamp** | `{metrics['timestamp']}` |
| **Exchange Entropy Index ($EEI$)** | **`{metrics['eei_value']}`** |
| **Current Market Phase** | **`{metrics['regime']}`** |
| **Phase Description** | {metrics.get('regime_description', '—')} |
| $\\text{{Cov}}(\\Delta F, \\Delta P)$ | `{metrics['cov_fundamental_price']}` |
| $\\text{{Cov}}(\\Delta N, \\Delta P)$ | `{metrics['cov_narrative_price']}` |
| $\\text{{Var}}(\\Delta P)$ | `{metrics['var_price']}` |
| Sample Size | `{metrics.get('sample_size', 30)}` |

---
"""
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(markdown_entry)
