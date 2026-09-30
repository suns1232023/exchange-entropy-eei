import numpy as np
import pandas as pd
from typing import Dict, Union, Tuple


class EEICalculator:
    """
    Realized Exchange Entropy and Exchange Entropy Index (EEI) Calculator.
    
    Mathematical Formulation:
        EEI(j,t) = [ Cov(ΔF_jt, ΔP_jt) - Cov(ΔN_jt, ΔP_jt) ] / Var(ΔP_jt)
    """

    def __init__(self, c1_threshold: float = 0.7, c2_threshold: float = 0.3):
        """
        :param c1_threshold: Upper threshold boundary between Phase I (EMH) and Phase II (Transitional)
        :param c2_threshold: Lower threshold boundary between Phase II (Transitional) and Phase III (Bubble/Crash)
        """
        self.c1_threshold = c1_threshold
        self.c2_threshold = c2_threshold

    def compute_eei(
        self,
        delta_F: np.ndarray,
        delta_N: np.ndarray,
        delta_P: np.ndarray
    ) -> Dict[str, float]:
        """
        Compute the EEI and its underlying covariance components.
        
        :param delta_F: Standardized fundamental surprises (ΔF)
        :param delta_N: Standardized narrative intensity / noise scores (ΔN)
        :param delta_P: Normalized price changes (ΔP)
        :return: Dictionary containing EEI metric, covariance components, and price variance
        """
        delta_F = np.asarray(delta_F, dtype=float)
        delta_N = np.asarray(delta_N, dtype=float)
        delta_P = np.asarray(delta_P, dtype=float)

        # Remove potential NaN or infinite values synchronously
        valid_mask = np.isfinite(delta_F) & np.isfinite(delta_N) & np.isfinite(delta_P)
        if np.sum(valid_mask) < 3:
            raise ValueError("Insufficient valid samples to compute EEI covariance decomposition.")

        f_valid = delta_F[valid_mask]
        n_valid = delta_N[valid_mask]
        p_valid = delta_P[valid_mask]

        var_P = float(np.var(p_valid, ddof=1))
        if var_P == 0 or np.isnan(var_P):
            raise ValueError("Price variance Var(ΔP) is zero or invalid.")

        cov_FP = float(np.cov(f_valid, p_valid)[0, 1])
        cov_NP = float(np.cov(n_valid, p_valid)[0, 1])

        eei_value = (cov_FP - cov_NP) / var_P

        return {
            "eei": float(eei_value),
            "cov_fundamental_price": cov_FP,
            "cov_narrative_price": cov_NP,
            "var_price": var_P,
            "sample_size": int(np.sum(valid_mask))
        }

    def classify_regime(self, eei_value: float) -> Tuple[str, str]:
        """
        Classify market state based on interpretation thresholds.
        
        :param eei_value: Computed EEI score
        :return: Tuple of (Regime Name, Description)
        """
        if eei_value >= self.c1_threshold:
            return (
                "Phase I: High-EEI",
                "Fundamental-driven price formation; fully aligned with Efficient Market Hypothesis (EMH)."
            )
        elif self.c2_threshold <= eei_value < self.c1_threshold:
            return (
                "Phase II: Transitional",
                "Mixed regime with heightened volatility; aligns with Adaptive Markets Hypothesis (AMH)."
            )
        elif 0.0 <= eei_value < self.c2_threshold:
            return (
                "Boundary State",
                "Neutral equilibrium; fundamental signals and narrative noise contribute equally."
            )
        else:
            return (
                "Phase III: Low-EEI",
                "Narrative dominance and echo chamber isolation; speculative bubbles and crash risks."
            )
