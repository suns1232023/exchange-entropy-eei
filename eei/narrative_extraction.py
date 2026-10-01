
import pandas as pd
import numpy as np
from typing import Union, List, Optional
from .utils import normalize_series


class NarrativeExtractor:
    """
    NLP and Sentiment Pipeline Wrapper to compute narrative intensity
    and noise scores (ΔN).
    """

    def __init__(self, sentiment_decay: float = 0.95):
        self.sentiment_decay = sentiment_decay

    def compute_narrative_intensity(
        self,
        text_volume: pd.Series,
        sentiment_scores: pd.Series,
        echo_chamber_weight: Optional[pd.Series] = None,
    ) -> pd.Series:
        """
        Compute frequency-weighted sentiment across social echo chambers.

        :param text_volume: Normalized count/frequency of thematic keywords
        :param sentiment_scores: Polarity score (-1.0 to 1.0)
        :param echo_chamber_weight: Weight corresponding to silo concentration (optional)
        :return: Standardized Narrative Surprise ΔN
        """
        raw_intensity = text_volume * sentiment_scores

        if echo_chamber_weight is not None:
            raw_intensity = raw_intensity * (1.0 + echo_chamber_weight)

        # Apply exponential smoothing for narrative persistence
        smoothed_intensity = raw_intensity.ewm(
            alpha=1.0 - self.sentiment_decay
        ).mean()

        return normalize_series(smoothed_intensity)

    @staticmethod
    def aggregate_multi_channel_narratives(
        channel_series_list: List[pd.Series],
    ) -> pd.Series:
        """
        Aggregate multiple narrative streams
        (e.g., Twitter/X, Reddit, Financial Media).
        """
        combined = pd.concat(channel_series_list, axis=1).mean(axis=1)
        return normalize_series(combined)

