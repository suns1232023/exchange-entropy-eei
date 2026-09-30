import pandas as pd
import numpy as np
from typing import Tuple, Union


def normalize_series(series: Union[pd.Series, np.ndarray]) -> Union[pd.Series, np.ndarray]:
    """
    Standardize a series to zero mean and unit variance (Z-score).
    """
    if isinstance(series, pd.Series):
        mean = series.mean()
        std = series.std()
        if std == 0 or np.isnan(std):
            return pd.Series(0.0, index=series.index)
        return (series - mean) / std
    else:
        arr = np.asarray(series, dtype=float)
        mean = np.mean(arr)
        std = np.std(arr)
        if std == 0 or np.isnan(std):
            return np.zeros_like(arr)
        return (arr - mean) / std


def align_time_series(
    df_fundamentals: pd.DataFrame,
    df_narratives: pd.DataFrame,
    df_prices: pd.DataFrame
) -> pd.DataFrame:
    """
    Aligns different time-series datasets by date index and drops missing entries.
    """
    aligned = pd.concat(
        [df_fundamentals, df_narratives, df_prices],
        axis=1,
        join="inner"
    ).dropna()
    return aligned
