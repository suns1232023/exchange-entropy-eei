import os
import json

def append_daily_log_and_json(metrics: dict, output_dir: str = "data"):
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. 更新最新的 JSON 导出文件
    json_path = os.path.join(output_dir, "eei_latest_metrics.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2, ensure_ascii=False)
        
    # 2. 追加格式化 Log 到 daily_log.md
    log_path = os.path.join(output_dir, "daily_log.md")
    markdown_entry = f"""
## 📈 Daily EEI Calculation Log ({metrics['timestamp']})

| Metric | Value |
| :--- | :--- |
| **Execution Timestamp** | `{metrics['timestamp']}` |
| **Exchange Entropy Index ($EEI$)** | **`{metrics['eei_value']}`** |
| **Current Market Phase** | **`{metrics['regime']}`** |
| $\text{{Cov}}(\Delta F, \Delta P)$ | `{metrics['cov_fund_price']}` |
| $\text{{Cov}}(\Delta N, \Delta P)$ | `{metrics['cov_narr_price']}` |
| $\text{{Var}}(\Delta P)$ | `{metrics['var_price']}` |

---
"""
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(markdown_entry)
