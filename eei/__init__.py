"""
Exchange Entropy Index (EEI) Core Package
An Operational Metric for Information Processing Fidelity in Financial Markets.
"""

from .eei_calculator import EEICalculator
from .fundamental_signals import FundamentalSignalExtractor
from .narrative_extraction import NarrativeExtractor
from .network_metrics import NetworkTopologyMetrics
from .utils import normalize_series, align_time_series

__version__ = "0.1.0"
__author__ = "Scott Sun"

__all__ = [
    "EEICalculator",
    "FundamentalSignalExtractor",
    "NarrativeExtractor",
    "NetworkTopologyMetrics",
    "normalize_series",
    "align_time_series",
]
