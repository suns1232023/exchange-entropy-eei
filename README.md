# Exchange Entropy (EEI)

> **An Operational Metric for Information Processing Fidelity in Financial Markets**

[![Daily EEI Calculation Pipeline](https://github.com/suns1232023/exchange-entropy-eei/actions/workflows/daily_eei_pipeline.yml/badge.svg)](https://github.com/suns1232023/exchange-entropy-eei/actions/workflows/daily_eei_pipeline.yml)
[![OSF Project](https://img.shields.io/badge/OSF-10.17605%2FOSF.IO%2F6NJE9-blue)](https://osf.io/6nje9/)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains the official Python implementation and computational pipeline for **Exchange Entropy ($H_{ex}$)** and the **Exchange Entropy Index (EEI)**, developed under the **INFO-PHYS-SILO** research framework led by Scott Sun.

---

## 💡 Core Innovation: Unifying EMH and Behavioral Finance

Financial economics has long suffered from a structural conflict between the **Efficient Market Hypothesis (EMH)** (Fama, 1970) and **Behavioral Finance** (Shiller, Thaler, et al.). While EMH assumes rational agents and complete arbitrage, Behavioral Finance highlights cognitive biases (e.g., herd behavior, overconfidence) leading to systematic price distortions. Traditional literature often treats these as mutually exclusive causal mechanisms.

Applying an **Information-Physics paradigm**, this framework unifies both schools of thought under a single continuous state variable — the **Exchange Entropy Index ($EEI$)**:

- **Traditional Dual-System Path (High Complexity)**: Requires two distinct, conflicting theoretical models plus external friction mechanisms (limits to arbitrage, sentiment cycles) to explain market state shifts.
- **Unified Information-Physics Path (Minimal Assumptions)**: Models market efficiency ($EEI \to 1.0$) and behavioral anomalies ($EEI < 0$) as distinct emergent phases of a single information-processing architecture. Regime transitions occur as the spatial information isolation intensity ($\sigma$) crosses critical thresholds.

---

### 🛡️ Epistemic Scope & Academic Positioning

Within this repository and research framework:
- Terms such as **"Thermodynamic Phase"**, **"Phase Transition"**, and **"Phase Boundary"** refer to formal phenomenological analogies and statistical mechanics mappings *internal to the EEI framework*.
- The theoretical positioning as a *"Maxwellian Unification"* serves as a conceptual heuristic to highlight how two seemingly opposed regimes (EMH vs. Behavioral anomalies) can be derived from a single continuous parameter space ($\sigma$).

---

## 🏗️ The Tri-Paper Unification Architecture

The theoretical foundation is laid out sequentially across three core papers:

| Paper & Reference | Core Question Solved | Theoretical Contribution & Mechanism |
| :--- | :--- | :--- |
| **Paper A: Degradation Mechanism**<br>*(Sun, 2026; DOI: [10.5281/zenodo.20607052](https://doi.org/10.5281/zenodo.20607052))* | *How does an efficient market degrade into an inefficient state?* | Introduces network topology and spatial isolation intensity ($\sigma$) to demonstrate how structural information silos cause continuous degradation of market pricing quality. |
| **Paper B: Operational Measurement**<br>*(Sun, 2026; DOI: [10.5281/zenodo.20695859](https://doi.org/10.5281/zenodo.20695859))* | *How do we quantify the boundary between efficiency and noise?* | Formulates realized Exchange Entropy $H_{ex} = I(\mathcal{I}; P) - \kappa \cdot D(\sigma)$ and operationalizes $EEI$ through covariance decomposition of fundamental signals vs. narrative noise. |
| **Paper C: Phase Transitions & Unification**<br>*(Sun, 2026; DOI: [10.5281/zenodo.20789616](https://doi.org/10.5281/zenodo.20789616))* | *Why do market regime switches occur abruptly?* | Applies physics phase transition theory to model how markets abruptly shift from rational pricing to "irrational exuberance" at critical thresholds of information fragmentation. |

---

## 🔬 Mathematical Formulation

The realized Exchange Entropy accounts for semantic distortion $D(\sigma)$ driven by silo intensity $\sigma$:

$$H_{ex} = I(\mathcal{I}; P) - \kappa \cdot D(\sigma)$$

For empirical estimation, $EEI$ is operationalized via a covariance decomposition of normalized market price changes over an estimation window:

$$EEI(j,t) = \frac{\text{Cov}(\Delta F_{jt}, \Delta P_{jt}) - \text{Cov}(\Delta N_{jt}, \Delta P_{jt})}{\text{Var}(\Delta P_{jt})}$$

Where:
- $\Delta F_{jt}$ = Standardized fundamental surprise (e.g., standardized unexpected earnings)
- $\Delta N_{jt}$ = Standardized narrative intensity (e.g., frequency-weighted sentiment across social echo chambers)
- $\Delta P_{jt}$ = Normalized price change over the estimation window

### Interpretation Thresholds & Phase Regimes

| EEI Value | Regime / Phase | Market Interpretation |
| :--- | :--- | :--- |
| **$\ge 0.7$** | **Phase I: High-EEI** ($\sigma < \sigma_{c1}$) | Fundamental-driven price formation; fully aligned with the **Efficient Market Hypothesis (EMH)**. |
| **0.3 – 0.7** | **Phase II: Transitional** ($\sigma_{c1} < \sigma < \sigma_{c2}$) | Mixed regime with heightened volatility; aligns with the **Adaptive Markets Hypothesis (AMH)**. |
| **0.0 – 0.3** | **Boundary State** | Neutral equilibrium; fundamental signals and narrative noise contribute equally to price dynamics. |
| **$< 0.0$** | **Phase III: Low-EEI** ($\sigma > \sigma_{c2}$) | Narrative dominance and echo chamber isolation; indicative of speculative bubbles and crash risks. |

---

## 📁 Repository Structure & Automated Architecture

This repository operates as an automated computational research workflow backed by a **GitHub Actions Daily CI/CD Pipeline**:

```text
exchange-entropy-eei/
│
├── .github/
│   └── workflows/
│       └── daily_eei_pipeline.yml     # GitHub Actions Daily CI/CD Workflow
│
├── eei/                                # Core Python Package
│   ├── __init__.py
│   ├── eei_calculator.py              # EEI & covariance decomposition
│   ├── fundamental_signals.py         # Earnings surprise & fundamental signal extraction
│   ├── narrative_extraction.py        # NLP pipeline & social sentiment scoring
│   ├── network_metrics.py             # Cross-silo path length & network fragmentation
│   └── utils.py                       # Preprocessing and standardizers
│
├── scripts/                            # Pipeline Execution & Automation
│   ├── daily_runner.py                # Main Pipeline Orchestrator
│   └── modules/
│       ├── fetch_market_data.py       # Market price and fundamental data ingester
│       ├── process_narratives.py      # Social narrative intensity processor
│       ├── compute_eei.py             # EEI computation & regime classification
│       └── update_eei_reports.py      # JSON, CSV, and Markdown report generator
│
├── data/                               # Persistent Daily Execution Storage
│   ├── eei_latest_metrics.json        # Latest computed EEI scores and regime status
│   ├── eei_history_series.csv         # Historical cumulative EEI time-series
│   └── daily_log.md                   # Auto-appended daily execution log
│
├── tests/                              # Unit & Integration Testing Suite
│   └── test_eei_calculator.py
│
├── docs                                # GitHub Pages landing page (Jekyll)
├── requirements.txt                    # Project Dependencies
├── setup.py                            # Package Configuration
└── README.md                           # Master Repository Documentation
```

> **Note on `examples/` and `docs/` directory:** Extended tutorials (Jupyter notebooks, sample data) and detailed API documentation are planned for a future release. The current `docs` file serves as the GitHub Pages landing page.

---

## 🚀 Quick Start

```bash
# Clone and install
git clone https://github.com/suns1232023/exchange-entropy-eei.git
cd exchange-entropy-eei
pip install -r requirements.txt
pip install -e .

# Run the daily pipeline manually
python scripts/daily_runner.py

# Run unit tests
python -m pytest tests/
```

### Minimal Usage Example

```python
import numpy as np
from eei import EEICalculator

calculator = EEICalculator(c1_threshold=0.7, c2_threshold=0.3)

# Simulate 30-day window
np.random.seed(42)
delta_P = np.random.normal(0, 0.02, 30)
delta_F = 0.8 * delta_P + np.random.normal(0, 0.005, 30)
delta_N = 0.1 * delta_P + np.random.normal(0, 0.005, 30)

result = calculator.compute_eei(delta_F, delta_N, delta_P)
regime, description = calculator.classify_regime(result["eei"])

print(f"EEI: {result['eei']:.4f}")
print(f"Regime: {regime}")
print(f"Description: {description}")
```

---

## 📊 Latest EEI Output

The pipeline writes daily results to `data/eei_latest_metrics.json`:

```json
{
  "timestamp": "2026-09-29 00:00:00",
  "date": "2026-09-29",
  "eei_value": 0.8251,
  "regime": "Phase I: High-EEI",
  "regime_description": "Fundamental-driven price formation; fully aligned with Efficient Market Hypothesis (EMH).",
  "cov_fundamental_price": 0.000312,
  "cov_narrative_price": 0.000045,
  "var_price": 0.000324,
  "sample_size": 30
}
```

---

## 📚 References

1. Fama, E. F. (1970). Efficient capital markets: A review of theory and empirical work. *Journal of Finance*, 25(2), 383–417.
2. Shiller, R. J. (2000). *Irrational Exuberance*. Princeton University Press.
3. Lo, A. W. (2004). The Adaptive Markets Hypothesis. *Journal of Portfolio Management*, 30(5), 15–29.
4. Sun, S. (2026). *Information Silo Degradation and Exchange Entropy*. Zenodo. DOI: [10.5281/zenodo.20607052](https://doi.org/10.5281/zenodo.20607052)
5. Sun, S. (2026). *Exchange Entropy Index: Operational Measurement*. Zenodo. DOI: [10.5281/zenodo.20695859](https://doi.org/10.5281/zenodo.20695859)
6. Sun, S. (2026). *Phase Transitions and Unification*. Zenodo. DOI: [10.5281/zenodo.20789616](https://doi.org/10.5281/zenodo.20789616)
7. OSF Project Registration: [osf.io/6nje9](https://osf.io/6nje9/)

---

## 📄 License

- **Code:** [MIT License](https://opensource.org/licenses/MIT)
- **Documentation & Research Content:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
