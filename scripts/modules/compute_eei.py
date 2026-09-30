import numpy as np
import pandas as pd
from eei.eei_calculator import EEICalculator

def execute_eei_pipeline(market_df: pd.DataFrame, narrative_df: pd.DataFrame) -> dict:
    """
    根据每日更新的数据运行 EEI 协方差分解计算并识别相态
    """
    # 假设两张表包含 \Delta F, \Delta N, \Delta P
    df = pd.merge(market_df, narrative_df, on=["asset_id", "timestamp"])
    
    delta_F = df["delta_fundamental"].values
    delta_N = df["delta_narrative"].values
    delta_P = df["delta_price"].values
    
    calculator = EEICalculator()
    eei_val = calculator.compute_eei(delta_F, delta_N, delta_P)
    
    # 判断相态 (Phase Regime)
    if eei_val >= 0.8:
        regime = "Phase I: High-EEI (EMH Market Efficiency)"
    elif 0.3 <= eei_val < 0.8:
        regime = "Phase II: Transitional (AMH Mixed Regime)"
    elif 0.0 <= eei_val < 0.3:
        regime = "Boundary State (Neutral Equilibrium)"
    else:
        regime = "Phase III: Low-EEI (Narrative Bubble / Crash Risk)"
        
    return {
        "timestamp": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
        "eei_value": round(float(eei_val), 4),
        "regime": regime,
        "cov_fund_price": round(float(np.cov(delta_F, delta_P)[0, 1]), 4),
        "cov_narr_price": round(float(np.cov(delta_N, delta_P)[0, 1]), 4),
        "var_price": round(float(np.var(delta_P)), 4)
    }
