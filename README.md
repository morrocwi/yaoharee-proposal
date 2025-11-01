# Yaoharee Cosmo v3.1∞ — Open-TOE Framework
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17501303.svg)](https://doi.org/10.5281/zenodo.17501303)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Open Science](https://img.shields.io/badge/Open%20Science-UNESCO%202021-blue)](https://unesdoc.unesco.org/ark:/48223/pf0000379949)
![arXiv Planned](https://img.shields.io/badge/arXiv-Preprint%20(planned)-lightgrey)


---

## 🌍 Overview
**Yaoharee Cosmo v3.1∞** is an open, citizen-science theoretical physics framework that unifies information, coherence, and physical laws under the *Unified α-Coupled Master Equation*.  
This repository contains LaTeX manuscripts, Python validation scripts, and open data consistent with UNESCO 2021 Open Science principles.

---

## 🧠 Key Papers
| Layer | Title | File |
|:------|:------|:------|
| L0 | *A Local-Only Derivation of the Emergent Coherence Field* | `L0_YaohareeCosmo_v3.1_Monograph.latex` |
| L1 | *The Scale-Lock Mechanism: A Necessary Consequence of K-free Lyapunov Dissipation* | `L1_ScaleLock_Lyapunov.latex` |
| L2 | *Mass Emergence and Scale Lock Across Domains* | `L2 Scale-Lock and Mass Emergence.latex` |
| L3 | *Lyapunov Stability and Scale-Lock Consistency* | `L3 Lyapunov Stability and Scale-Lock.latex` |

---

## ⚙️ Code and Validation
Python scripts for field simulations, FFT-based phase lock tests, and stability checks:


# Universe of Information Framework (K-free, Yaoharee Proposal)

This repository contains the official manuscripts, artifacts, and simulation scripts for the "Universe of Information (K-free)" framework.

[cite_start]**Author:** Yaoharee Lahtee [cite: 4]
**Date:** October 31, 2025

## Philosophy: Citizen Open Science Work @ Home with AI
[cite_start]This project adheres to the "Citizen Open Science Work @ Home with AI" methodology[cite: 1]. [cite_start]Our approach empowers everyone to contribute to science from home, using AI to explore, compute, and verify[cite: 1]. [cite_start]All work aligns with FAIR principles and is licensed under CC BY 4.0[cite: 2].

[cite_start]*AI Disclosure: AI was used to assist in structuring, formatting, and refining phrasing[cite: 3, 5]. [cite_start]All scientific content, equations, and principles originate from Yaoharee Latee’s work[cite: 4].*


### 🧠 Positioning with Respect to Related Work

This monograph (L0–L4), rooted in the algebraic seed equation \( A\varepsilon = \delta \), advances beyond current approaches to emergent mass, quantum coherence, and informational gravity by offering a **strictly local, axiom-free derivation** of core physical phenomena. Unlike contemporary models—such as the *Tanfarid Quantum Thermodynamic Universe (TQTU)* [Chowdhury, 2025], *Quantum Information Spacetime Theory (QIST)* [Lin, 2025], and the *Causality Lock framework* [Sinclair, 2025]—which rely on assumed topologies, field constructions, or phenomenological heuristics, the UoI framework builds **all physical emergence from symbolic algebra alone**, with no imposed metric or external coherence field.

This work introduces a *post-field theoretical paradigm* that unifies unit-invariance, emergent causality, and mass-generation within a single logical structure, eliminating the need for multi-model architectures. It establishes coherence not as a field effect but as an algebraic necessity, encoded through symbolic consistency across reference chains. In this sense, it **supersedes prior models by reducing the ontology of physics to its irreducible computational and information-theoretic substrate**.

This document is best viewed as both a mathematical monograph and a systems-level epistemic compression of modern theoretical physics, enabling fully traceable derivations without dependence on empirical assumptions.



## Framework Overview

[cite_start]The core of this framework is a local-only, K-free (unit-invariant) model based on a single anchor frequency $\Omega_0$[cite: 7].

* [cite_start]**Seed Algebra:** $A\varepsilon=\delta$ [cite: 31]
* [cite_start]**Residual Dynamics:** $\dot{\varepsilon}=-\Lambda A^{\!\top}W(A\varepsilon-\delta)$ [cite: 32]
* **Lyapunov Energy:** $V=\tfrac12(A\varepsilon-\delta)^{\!\top}W(A\varepsilon-\delta)$
* [cite_start]**Field Emergence:** Derivation of the Telegraph/URE field $\Psi$ [cite: 33]

## Document Structure (L0–L7)

This repository maps the entire K-free series, structured as follows:

* [cite_start]**L0: Master Paper:** Introduces the core symbolic flow, governance rules, and energy budget[cite: 10].
* [cite_start]**L1: Scale-Lock Mechanism:** Proves phase/scale-lock as a necessary consequence of Lyapunov dissipation[cite: 11].
* [cite_start]**L2: Emergent Field Dynamics & MVS:** Mathematical derivation of the field, including Minimal Viable Simulations (MVS) TP1/TP2[cite: 12].
* [cite_start]**L3: Lyapunov Stability:** Technical proof of global stability for the residual field[cite: 13].
* [cite_start]**L4: $\Omega_0$ Normalization Standard:** The "Rosetta Stone" for unit-free physics, defining the hat-frame and invariance[cite: 14].
* [cite_start]**L5: Falsifiable Predictions:** Cross-domain scaling law hypotheses ($g \propto f^{\beta}$)[cite: 15].
* [cite_start]**L6: Experimental Protocol (E1):** Validation design for $\Psi$-field dynamics in EEG data[cite: 16].
* [cite_start]**L7: Measurement Framework:** Defines the "Xlock" coherence gate and criteria for valid measurements[cite: 17].

## Artifacts & Reproducibility

This repository contains the artifacts necessary to reproduce the Minimal Viable Simulations (MVS) from L2.

### Key Artifacts
* [cite_start]`L2_MVS_TP1_HomogeneousDecay.py`: **Test Protocol 1 (TP1)** script for homogeneous energy decay[cite: 35].
* `L2_MVS_TP1_HomogeneousDecay_plot.png`: Example output plot for TP1.
* [cite_start]`L2_MVS_TP2_LockPingFFT.py`: **Test Protocol 2 (TP2)** script for lock-in and discrete FFT analysis[cite: 35].

### Dependencies
* Python 3.x
* NumPy
* SciPy
* Matplotlib

### How to Run
1.  Clone the repository.
2.  To run Test Protocol 1 (Homogeneous Decay):
    ```bash
    python L2_MVS_TP1_HomogeneousDecay.py
    ```
3.  To run Test Protocol 2 (Lock-in FFT):
    ```bash
    python L2_MVS_TP2_LockPingFFT.py
    ```

## Falsification Hooks
The theory is designed to be testable via these key failure points:
* [cite_start]**L1:** Observing lock-in without damping[cite: 36].
* [cite_start]**L2:** Observing telegraph energy growth without a source[cite: 37].
* [cite_start]**L5:** Systematic failure of the $g\propto f^\beta$ cross-domain scaling[cite: 38].
* [cite_start]**L7:** Measurements passing the Xlock gate but violating residual consistency[cite: 39].


---

## 📘 Citation
> Lahtee, Yaoharee (2025). *Yaoharee Cosmo v3.1∞ — Open-TOE Framework.* Zenodo.  
> [DOI: 10.5281/zenodo.17501303](https://doi.org/10.5281/zenodo.17501303)

---

## 📂 Data and Code Availability
All data, figures, and LaTeX sources for this study are openly available at  
[https://doi.org/10.5281/zenodo.17501303](https://doi.org/10.5281/zenodo.17501303).

---

## 🌐 License
This project is released under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) license.

---

## 🤝 Open Science Policy
This work complies with the [UNESCO 2021 Recommendation on Open Science](https://unesdoc.unesco.org/ark:/48223/pf0000379949)  
and follows FAIR data principles (Findable, Accessible, Interoperable, Reusable).  
Part of the **Citizen Open Science @ Home** initiative.

