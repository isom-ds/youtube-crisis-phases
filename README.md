# youtube-crisis-phases
> Detecting and forecasting crisis phases in financial markets using YouTube social media signals.

## Abstract
Financial crises unfold in identifiable phases — pre-crisis, acute crisis, and recovery — yet real-time detection of phase transitions from noisy social media data remains an open problem. This repository implements a pipeline for detecting and forecasting crisis phases using YouTube-derived social media signals combined with financial price data, providing decision-support for anticipating market regime changes. The work contributes a social media-based phase detection methodology as a complementary layer to conventional technical analysis.

## Research Context
- **Thesis:** *Epidemiology of Online Emotions* (Kok-Shun, 2026)
- **Chapter:** Chapter 4 — Emotional Dynamics in Online Communities
- **Contribution type:** Artefact (crisis phase detection and forecasting system)
- **Associated paper:** "Can AI Learn to Surf the Wave of Emotions? Modelling Self-Organising Social Media Communities in Financial Crises," ACIS 2023

## Methods
- YouTube social media signal extraction
- Financial price data integration (yfinance)
- Crisis phase detection and classification
- Time-series forecasting of phase transitions

## Datasets
| Dataset | Description | Access |
|---------|-------------|--------|
| YouTube social media signals | YouTube-derived emotional/topical signals during crisis periods | Collected |
| Financial market data | Asset price time series | Via yfinance (open) |

## Repository Structure
```
youtube-crisis-phases/
├── src/
│   ├── models/
│   │   └── secrets.py               # API key and credential management
│   └── __pycache__/
└── README.md
```

## Requirements & Setup
Python 3.10+, Pandas, requests, yfinance; DevContainer for reproducibility.

```bash
# Using DevContainer (recommended)
# Open in VS Code → Reopen in Container

# Or install directly:
pip install -r requirements.txt
```

## Usage
Run the analysis notebooks for phase detection and forecasting. Social media signals feed into the phase classification model alongside financial price data.

## References

B. V. Kok-Shun, J. Chan, G. Peko, and D. Sundaram, "Can AI Learn to Surf the Wave of Emotions? Modelling Self-Organising Social Media Communities in Financial Crises," in *ACIS 2023 Proceedings*, vol. 79, 2023 [Online]. Available: https://aisel.aisnet.org/acis2023/79.

<details>
<summary>BibTeX</summary>

```bibtex
@inproceedings{P1_kok-shun_can_2023,
  title     = {Can {AI} {Learn} to {Surf} the {Wave} of {Emotions}? {Modelling} {Self}-{Organising} {Social} {Media} {Communities} in {Financial} {Crises}},
  volume    = {79},
  booktitle = {{ACIS} 2023 {Proceedings}},
  author    = {Kok-Shun, Brice Valentin and Chan, Johnny and Peko, Gabrielle and Sundaram, David},
  year      = {2023},
  url      = {https://aisel.aisnet.org/acis2023/79},
}
```

</details>
