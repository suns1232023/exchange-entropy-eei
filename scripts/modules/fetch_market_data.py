import os
import numpy as np
import pandas as pd


def fetch_latest_market_data(data_dir: str = "data") -> pd.DataFrame:
    """抓取或生成最新的价格 (ΔP) 与基本面 (ΔF) 数据。

    在实际部署中，可对接 Yahoo Finance、Tushare 或金融 API。
    """
    np.random.seed(int(pd.Timestamp.now().timestamp()) % 1000000)
    dates = pd.date_range(end=pd.Timestamp.now(), periods=30, freq="D")

    # 模拟 30 天的价格变动与基本面惊喜值
    delta_price = np.random.normal(loc=0.01, scale=0.02, size=len(dates))
    delta_fundamental = 0.6 * delta_price + np.random.normal(
        loc=0.0, scale=0.01, size=len(dates)
    )

    df = pd.DataFrame(
        {
            "timestamp": dates.strftime("%Y-%m-%d"),
            "asset_id": "SPX500",
            "delta_price": delta_price,
            "delta_fundamental": delta_fundamental,
        }
    )
    return df
