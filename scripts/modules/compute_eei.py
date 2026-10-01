
import numpy as np
import pandas as pd
from eei.eei_calculator import EEICalculator


def execute_eei_pipeline(market_df: pd.DataFrame, narrative_df: pd.DataFrame) -> dict:
    """
    Run the daily EEI covariance decomposition and classify the market phase.

    Uses EEICalculator as the single source of truth for both the EEI value
    and the phase classification, ensuring full consistency with the thresholds
    defined in EEICalculator (c1=0.7, c2=0.3) and documented in README.

    Returns a dict suitable for JSON export and daily_log.md.
    """
    # Merge market and narrative data on shared keys
    df = pd.merge(market_df, narrative_df, on=["asset_id", "timestamp"])

    delta_F = df["delta_fundamental"].values
    delta_N = df["delta_narrative"].values
    delta_P = df["delta_price"].values

    # compute_eei returns a dict; extract components explicitly
    calculator = EEICalculator()
    eei_result = calculator.compute_eei(delta_F, delta_N, delta_P)

    eei_val          = eei_result["eei"]
    cov_fund_price   = eei_result["cov_fundamental_price"]
    cov_narr_price   = eei_result["cov_narrative_price"]
    var_price        = eei_result["var_price"]   # sample variance (ddof=1), consistent with EEICalculator
    sample_size      = eei_result["sample_size"]

    # Use EEICalculator.classify_regime as the single source of truth for thresholds
    regime, regime_description = calculator.classify_regime(eei_val)

    return {
        "timestamp":              pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
        "date":                   pd.Timestamp.now().strftime("%Y-%m-%d"),
        "eei_value":              round(float(eei_val),        4),
        "regime":                 regime,
        "regime_description":     regime_description,
        "cov_fundamental_price":  round(float(cov_fund_price), 6),
        "cov_narrative_price":    round(float(cov_narr_price), 6),
        "var_price":              round(float(var_price),      6),
        "sample_size":            sample_size,
    }
