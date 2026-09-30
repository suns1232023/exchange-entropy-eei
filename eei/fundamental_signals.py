import pandas as pd
import numpy as np
from typing import Optional
from .utils import normalize_series


class FundamentalSignalExtractor:
    """
    Extracts and standardizes fundamental surprise signals (ΔF).
    """

    @staticmethod
    def compute_earnings_surprise(
        actual_eps: pd.Series,
        consensus_eps: pd.Series,
        price_std: Optional[pd.Series] = None
    ) -> pd.Series:
        """
        Calculates Standardized Unexpected Earnings (SUE).
        
        :param actual_eps: Reported EPS values
        :param consensus_eps: Analyst consensus estimates
        :param price_std: Volatility scale factor for normalization (optional)
        :return: Standardized Fundamental Surprise ΔF
        """
        surprise = actual_eps - consensus_eps
        
        if price_std is not None and not price_std.empty:
            sue = surprise / (price_std + 1e-8)
        else:
            sue = surprise

        return normalize_series(sue)

    @staticmethod
    def Extract_fundamental_growth_deltas(df: pd.DataFrame, columns: list) -> pd.DataFrame:
        """
        Calculates normalized period-over-period fundamental metric changes.
        """
        deltas = pd.DataFrame(index=df.index)
        for col in columns:
            if col in df.columns:
                delta_col = df[col].pct_change().fillna(0.0)
                deltas[f"delta_{col}"] = normalize_series(delta_col)
        return deltas
