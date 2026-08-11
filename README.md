# Exchange Entropy (EEI)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![OSF DOI](https://img.shields.io/badge/OSF-10.17605%2FOSF.IO%2F6NJE9-blue)](https://osf.io/6nje9/)

### An Operational Metric for Information Processing Fidelity in Financial Markets

This repository provides the official implementation of **Exchange Entropy ($H_{ex}$)** and the **Exchange Entropy Index (EEI)**, developed under the **INFO-PHYS-SILO** research framework led by Scott Sun.

---

## 📌 Theoretical Framework & Citation

EEI integrates information theory, network science, and statistical physics to quantify how effectively financial markets incorporate fundamental information versus narrative noise within information silos (echo chambers).

If you utilize this repository, theoretical formulations, or code, please cite the following papers:

1. **Paper A (Network Model & Mechanism):**  
   Sun, S. (2026). *Information Silos and Market Efficiency Decay: A Network-Mediated Model of Pricing Degradation in Fragmented Information Environments*. Working Paper. DOI: [10.5281/zenodo.20607052](https://doi.org/10.5281/zenodo.20607052)
2. **Paper B (Mutual Information & Estimator):**  
   Sun, S. (2026). *Exchange Entropy in Financial Information Processing: An Operational Metric for Information Processing Fidelity in Asset Markets*. Working Paper. DOI: [10.5281/zenodo.20695859](https://doi.org/10.5281/zenodo.20695859)
3. **Paper C (Phase Transitions & IP-EMH):**  
   Sun, S. (2026). *Market Phase Transitions and the Information Physics of Financial Systems: Toward a Unified Framework Integrating Exchange Entropy, Network Topology, and Collective Information Processing*. Working Paper. DOI: [10.5281/zenodo.20789616](https://doi.org/10.5281/zenodo.20789616)

* **Author:** Scott Sun (Independent Researcher) | **ORCID:** [0009-0002-1095-6228](https://orcid.org/0009-0002-1095-6228)
* **OSF Project:** [OSF.IO/6NJE9](https://osf.io/6nje9/)

---

## 🔬 Mathematical Definition

The realized Exchange Entropy accounts for semantic distortion $D(\sigma)$ driven by silo intensity $\sigma$:

$$H_{ex} = I(\mathcal{I}; P) - \kappa \cdot D(\sigma)$$

For empirical estimation, EEI is operationalized using a covariance decomposition of normalized market price changes:

$$EEI(j,t) = \frac{\text{Cov}(\Delta F_{jt}, \Delta P_{jt}) - \text{Cov}(\Delta N_{jt}, \Delta P_{jt})}{\text{Var}(\Delta P_{jt})}$$

Where:
* $\Delta F_{jt}$ = Standardized fundamental surprise (e.g., earnings surprise scaled by price)
* $\Delta N_{jt}$ = Standardized narrative intensity (e.g., frequency-weighted sentiment of thematic keywords across social communities)
* $\Delta P_{jt}$ = Normalized price change over the estimation window

### Interpretation Thresholds & Phase Regimes

| EEI Value | Regime / Phase | Market Interpretation |
| :--- | :--- | :--- |
| **1.0** | **Phase I: High-EEI** ($\sigma < \sigma_{c1}$) | Pure fundamental processing; aligned with the Efficient Market Hypothesis (EMH). |
| **0.3 – 0.7** | **Phase II: Transitional** ($\sigma_{c1} < \sigma < \sigma_{c2}$) | Mixed regime; high volatility in EEI, aligned with Adaptive Markets Hypothesis (AMH). |
| **0.0** | **Boundary State** | Equal contribution of fundamental signals and narrative noise. |
| **< 0.0** | **Phase III: Low-EEI** ($\sigma > \sigma_{c2}$) | Narrative dominance & silo isolation; bubble conditions and critical risk. |

---

## 📁 Repository Structure

```text
├── eei/                        # Core Implementation Package
│   ├── eei_calculator.py       # Main EEI & covariance computation routines
│   ├── fundamental_signals.py  # Earnings surprise & news analytics extractions
│   ├── narrative_extraction.py # NLP topic modeling (BERTopic/LDA) & sentiment pipeline
│   ├── network_metrics.py      # Cross-silo path length & network fragmentation metrics
│   └── utils.py                # Preprocessing and standardizers
├── examples/                   # Executable Tutorials
│   ├── example_eei_calculation.ipynb
│   └── sample_data/            # Mock dataset for prices, fundamentals, and social text
├── docs/                       # Extended Documentation
│   ├── theoretical_framework.md
│   ├── phase_transition_diagrams/
│   └── api_reference.md
├── tests/                      # Unit & Integration Tests
│   └── test_eei_calculator.py
├── LICENSE                     # Code under MIT, Content under CC-BY 4.0
└── README.md
