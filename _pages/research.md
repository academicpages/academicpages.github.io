---
layout: archive
title: "Research"
permalink: /research/
excerpt: "Research"
author_profile: true
---

<h3> MOB-ML </h3>

The basic elements of chemistry are atoms and electrons, whose behavior is governed by quantum mechanics.
Based on the principles of the quantum mechanics, quantum chemistry methods offers a way to calculate the properties of molecules.
However, for large or medium sized molecules, it is not easy to reach the desired accuracy within an acceptable computational cost.
Thus, we developed _Molecular-Orbital-Based Machine Learning_ (MOB-ML) to obtain the molecular properties in the level of highly accurate but expensive wavefunction theory from the cheap Hartree-Fock method.

MOB-ML is carefully designed to satisfy all the physical requirements of a good quantum chemistry theory, including translation and rotational invariance, permutation symmetries of atoms and orbitals, and size consistency. 
By ensuring the equivairance relations, it is also generalized to learn tensorial and response properties with the same accuracy as the scalar properties.
These properties make MOB-ML a general and accurate method to be applied to organic molecules, intermolecular interactions, transition states, and open-shell systems.
We also developed novel machine learning algorithms includes alternative black-box matrix multiplication (AltBBMM) and kernel addition Gaussian process regression (KA-GPR), which greatly enhances the machine learning efficiency without loss of accuracy.
Due to these developments, MOB-ML has already shown great performance compared with other novel quantum machine learning methods in the world, and has already been used to generate highly accurate potential energy surface (PES) in real applications.

References:
TBA

<h3> RPMD </h3>

Classical molecular dynamics methods have already shown to be successful for modeling large chemical and biological systems.
However, for light atoms like hydrogen and its isotopes, nuclear quantum effect is non-negligible and cannot be captured by these classical methods.
Ring-polymer molcular dynamics is a semi-classical quantum dynamics method to approximately describe the nuclear quantum effect.

In a recent work, we introduced a generalized class of thermalized RPMD integrators and studied their equilibrium accuracy, convergence rate, stability and dimensionality-freedom from a theoreical aspect of view. We confirmed that the "BCOCB" type integrator over all other known integrators in this class.

References:
TBA

<h3> Electron-phonon interaction </h3>

High electric field electron transport is of fundamental interest and practical importance in semiconductors.
In fact, the theoretical description of electron transport requires accurate calculation of electron-phonon interaction.
However, due to the high computational cost, the multi-phonon processes are usually neglected in the elctron-phonon interaction calculation.

In a recent work, we studied high-field transport properties in GaAs by including on-shell two phonon scattering process.
Our finding reconciles a long-standing discrepancy regarding the strength of intervalley scattering in GaAs as inferred from transport and optical studies.

References:
TBA

