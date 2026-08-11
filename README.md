# exchange-entropy-eei
# Exchange Entropy (EEI)
### An Operational Metric for Information Processing Fidelity in Financial Markets

This repository provides the official implementation of **Exchange Entropy (H_ex)** and the **Exchange Entropy Index (EEI)** introduced in:

- *Information Silos and Market Efficiency Decay* (Sun, 2026)  
- *Exchange Entropy in Financial Information Processing* (Sun, 2026)  
- *Market Phase Transitions and the Information Physics of Financial Systems* (Sun, 2026)

EEI is a covariance-based estimator that measures how faithfully a market processes **fundamental information** relative to **narrative amplification** within information silos.

---

## 📌 What is EEI?

EEI is defined as:



\[
EEI = \frac{Cov(AF, AP) - Cov(AN, AP)}{Var(AP)}
\]



Where:

- **AF** = standardized fundamental surprise  
- **AN** = standardized narrative intensity  
- **AP** = price change  

Interpretation:

| EEI Value | Meaning |
|----------|---------|
| **1.0** | Pure fundamental processing |
| **0.3–0.7** | Mixed regime (Adaptive Markets) |
| **0.0** | Equal narrative & fundamental influence |
| **< 0** | Narrative dominance (bubble conditions) |

---

## 📁 Repository Contents

### `/eei/`
Core implementation of EEI:
- `eei_calculator.py` — main EEI computation module  
- `fundamental_signals.py` — earnings surprise & news-based signals  
- `narrative_extraction.py` — topic modeling & sentiment extraction  
- `network_metrics.py` — cross-silo network fragmentation metrics  
- `utils.py` — shared helpers  

### `/examples/`
Ready-to-run Jupyter notebooks:
- `example_eei_calculation.ipynb`  
- Sample datasets for price, fundamentals, and social media text  

### `/docs/`
- Full theoretical documentation  
- Phase transition diagrams  
- API reference  

### `/tests/`
Unit tests for reproducibility.

---

## 🚀 Quick Start

### Install
