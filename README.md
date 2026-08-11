# Exchange Entropy (EEI)

[![OSF Project](https://img.shields.io/badge/OSF-10.17605%2FOSF.IO%2F6NJE9-blue)](https://osf.io/6nje9/)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

### An Operational Metric for Information Processing Fidelity in Financial Markets

This repository contains the official implementation of **Exchange Entropy ($H_{ex}$)** and the **Exchange Entropy Index (EEI)**, developed under the **INFO-PHYS-SILO** research framework led by Scott Sun.

---

## 💡 Core Innovation: Unifying EMH and Behavioral Finance

> **"This framework shifts the paradigm from choosing 'who is right' (EMH vs. Behavioral Finance) to quantifying 'which state the market is in' on a continuous spectrum."**

Financial economics has long suffered from a structural conflict between the **Efficient Market Hypothesis (EMH)** (Fama, 1970) and **Behavioral Finance** (Shiller, Thaler, et al.). While EMH assumes rational agents and complete arbitrage, Behavioral Finance highlights cognitive biases (e.g., herd behavior, overconfidence) leading to systematic price distortions. 

Traditional literature treats these as mutually exclusive causal mechanisms: either information is perfectly processed, or it is systematically warped.

### ✂️ An Occam's Razor Perspective
Applying **Occam’s Razor** (*"Entities should not be multiplied without necessity"*), this framework introduces an **Information-Physics paradigm** that unifies both schools of thought under a single continuous state variable—**Exchange Entropy Index ($EEI$)**:

* **Traditional Dual-System Path (High Complexity)**: Requires two distinct, conflicting theoretical models (EMH + Behavioral Finance) plus external friction mechanisms (limits to arbitrage, sentiment cycles, behavioral biases) to explain market state shifts.
* **Unified Information-Physics Path (Minimal Assumptions)**: Unified within a single metric $EEI$. EMH ($EEI \to 1.0$) and behavioral anomalies ($EEI < 0$) are demonstrated to be different thermodynamic phases of the same information-processing system. Transition occurs naturally as the information isolation intensity ($\sigma$) crosses critical thresholds.

---

## 🏗️ The Tri-Paper Unification Architecture

The theoretical foundation is laid out sequentially across three core papers:

| Paper & Reference | Core Question Solved | Theoretical Contribution & Mechanism |
| :--- | :--- | :--- |
| **Paper A: Degradation Mechanism**<br>*(Sun, 2026; DOI: 10.5281/zenodo.20607052)* | *How does an efficient market degrade into an inefficient state?* | Introduces network topology and spatial isolation intensity ($\sigma$) to demonstrate how structural information silos cause continuous degradation of market pricing quality. |
| **Paper B: Operational Measurement**<br>*(Sun, 2026; DOI: 10.5281/zenodo.20695859)* | *How do we quantify the boundary between efficiency and noise?* | Formulates realized Exchange Entropy $$H_{ex} = I(\mathcal{I}; P) - \kappa \cdot D(\sigma)$$ and operationalizes $EEI$ through covariance decomposition of fundamental signals vs. narrative noise. |
| **Paper C: Phase Transitions & Unification**<br>*(Sun, 2026; DOI: 10.5281/zenodo.20789616)* | *Why do market regime switches occur abruptly?* | Applies physics phase transition theory to model how markets abruptly shift from rational pricing to "irrational exuberance" at critical thresholds of information fragmentation. |

### 📌 Academic Positioning: "Maxwell's Equations" for Asset Pricing
Just as **Maxwell’s equations unified electricity and magnetism** into two manifestations of a single electromagnetic field, the $EEI$ framework unifies market efficiency and behavioral inefficiency as distinct physical phases within a unified information-processing architecture.

---

## 🔬 Mathematical Definition

The realized Exchange Entropy accounts for semantic distortion $D(\sigma)$ driven by silo intensity $\sigma$:

$$H_{ex} = I(\mathcal{I}; P) - \kappa \cdot D(\sigma)$$

For empirical estimation, $EEI$ is operationalized via a covariance decomposition of normalized market price changes:

$$EEI(j,t) = \frac{\text{Cov}(\Delta F_{jt}, \Delta P_{jt}) - \text{Cov}(\Delta N_{jt}, \Delta P_{jt})}{\text{Var}(\Delta P_{jt})}$$

Where:
* $\Delta F_{jt}$ = Standardized fundamental surprise (e.g., standardized earnings surprise)
* $\Delta N_{jt}$ = Standardized narrative intensity (e.g., frequency-weighted sentiment of thematic keywords across social echo chambers)
* $\Delta P_{jt}$ = Normalized price change over the estimation window

### Interpretation Thresholds & Phase Regimes

| EEI Value | Regime / Phase | Market Interpretation |
| :--- | :--- | :--- |
| **1.0** | **Phase I: High-EEI** ($\sigma < \sigma_{c1}$) | Fundamental-driven price formation; fully aligned with the **Efficient Market Hypothesis (EMH)**. |
| **0.3 – 0.7** | **Phase II: Transitional** ($\sigma_{c1} < \sigma < \sigma_{c2}$) | Mixed regime with heightened volatility; aligns with the **Adaptive Markets Hypothesis (AMH)**. |
| **0.0** | **Boundary State** | Neutral equilibrium; fundamental signals and narrative noise contribute equally to price dynamics. |
| **< 0.0** | **Phase III: Low-EEI** ($\sigma > \sigma_{c2}$) | Narrative dominance and echo chamber isolation; indicative of speculative bubbles and crash risks. |

---

## 📁 Repository Structure

```text
├── eei/                        # Core Python Implementation Package
│   ├── eei_calculator.py       # Main EEI & covariance decomposition algorithms
│   ├── fundamental_signals.py  # Earnings surprise and fundamental signal extraction
│   ├── narrative_extraction.py # NLP pipeline (BERTopic/LDA) & social sentiment scoring
│   ├── network_metrics.py      # Cross-silo path length & network fragmentation analysis
│   └── utils.py                # Preprocessing and standardizers
├── examples/                   # Executable Tutorials & Notebooks
│   ├── example_eei_calculation.ipynb
│   └── sample_data/            # Mock dataset (Prices, Fundamentals, Social Text)
├── docs/                       # Extended Theoretical Documentation
│   ├── theoretical_framework.md
│   ├── phase_transition_diagrams/
│   └── api_reference.md
├── tests/                      # Unit & Integration Testing Suite
│   └── test_eei_calculator.py
├── LICENSE                     # Software under MIT, Content under CC-BY 4.0
└── README.md
