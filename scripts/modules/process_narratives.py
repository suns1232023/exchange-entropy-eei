import numpy as np
import pandas as pd


def extract_daily_narratives(data_dir: str = "data") -> pd.DataFrame:
    """提取最新的社媒叙事与噪音得分 (ΔN)。

    在实际部署中，可对接 Twitter/X, Reddit 或新闻 NLP 提取管道。
    """
    dates = pd.date_range(end=pd.Timestamp.now(), periods=30, freq="D")

    # 模拟社媒叙事情绪/噪音得分
    delta_narrative = np.random.normal(loc=0.005, scale=0.025, size=len(dates))

    df = pd.DataFrame(
        {
            "timestamp": dates.strftime("%Y-%m-%d"),
            "asset_id": "SPX500",
            "delta_narrative": delta_narrative,
        }
    )
    return df
