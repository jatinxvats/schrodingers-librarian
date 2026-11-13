# Grading sheet

Grade: PASS / PARTIAL / FAIL. Tag: misattribution, invented-fact, uncited-claim, wrong-refusal, missed-retrieval, outside-knowledge, contradiction, other.


---
## #1 [foundations/definition]
**Q:** What is a Hilbert space?
**Answerable:** True  |  **Best distance:** 0.273  |  **Refused:** False
**Must include:** A complex linear space of vectors with a positive-definite inner product (square-integrable, per 2210.10624), in which quantum states are vectors; observables with finitely many eigenvectors (e.g. spin) need only the Hilbert space; does not call it bilinear or insist on infinite dimension unless a chunk says so.
**Label notes:** Development question. Verified by grep of 2210.10624. PENDING grep of 2406.02149 (formal axiomatic definition; may state completeness/dimension). Earlier system answer said 'infinite-dimensional' and 'bilinear': check whether either is in 2406.02149. Borderline: 2102.00861. Rejected: 2105.13821 (bibliography entry), 1805.11483, 2104.10700, 2504.14791.

**Answer:**

A Hilbert space is an infinite‑dimensional complex vector space that is linear, carries a bilinear (inner) product, and is complete with respect to the norm induced by that inner product (i.e., Cauchy‑complete) [1]. In quantum mechanics it is taken as a square‑integrable, complex, linear, abstract space of vectors equipped with a positive‑definite inner product; the state vectors of a system live in this space, which possesses an orthonormal basis of eigenfunctions, and observables act as Hermitian operators whose measurements correspond to orthogonal projections [3]. The space commonly used is the sequence space ℓ², first defined explicitly by Schmidt in 1908 and later popularized by von Neumann as the “(complex) Hilbert space” [2].

**Sources:**
- [1] 2406.02149 Von Neumann's 1927 Trilogy on the Foundations of Quantum Mechanics. An (0.273) relevant
- [2] 2406.02149 Von Neumann's 1927 Trilogy on the Foundations of Quantum Mechanics. An (0.296) relevant
- [3] 2210.10624 How Do the Probabilities Arise in Quantum Measurement? (0.385) relevant
- [4] 2102.00861 A Review of The Algebraic Approaches to Quantum Mechanics. Appraisals  (0.423) -

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #2 [bell_epr/definition]
**Q:** What does Bell's theorem rule out?
**Answerable:** True  |  **Best distance:** 0.327  |  **Refused:** False
**Must include:** Bell's theorem: no physical theory based only on local variables can account for all of quantum theory's predictions; the local variable can be read as an influence carried from a shared past (Bell's original reading, 2104.10700); does not rule out hidden variables as such (nonlocal ones survive); does not claim it proves signaling.
**Label notes:** Development question. Verified by grep of 2104.10700 introduction. That chunk was NOT in the semantic top 5 (retrieval returned 1912.06349, 2504.01056, 2102.13036, 2210.03365, 2306.07794): retrieval miss. 2408.08329 borderline (table of contents and formula-heavy spin chapter). Rejected: 1912.06349 (disputes the proof's assumptions), 2504.01056 (book review), 2210.03365.

**Answer:**

Bell’s theorem rules out the possibility of explaining quantum‑mechanical predictions with **local hidden‑variable theories**—i.e., any theory that assigns predetermined outcomes to measurements while respecting locality. [3]

**Sources:**
- [1] 1912.06349 The Bell theorem revisited: geometric phases in gauge theories (0.327) -
- [2] 2504.01056 Review of "Just Plain Wrong: The Dalliance of Quantum Theory with the  (0.332) -
- [3] 2102.13036 Kochen-Specker Contextuality (0.354) relevant
- [4] 2102.13036 Kochen-Specker Contextuality (0.356) relevant
- [5] 2210.03365 Spin-1 photons, spin-1/2 electrons, Bell's inequalities, and Feynman's (0.372) -

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #3 [contextuality/definition] (HOLD-OUT)
**Q:** What is the Kochen-Specker theorem?
**Answerable:** True  |  **Best distance:** 0.241  |  **Refused:** False
**Must include:** No context-independent value assignment in dimension >= 3, so noncontextual hidden variables are ruled out; not applicable to a single qubit; does not rule out all hidden variables.
**Label notes:** Borderline: 2502.19278, 2105.13821.

**Answer:**

The Kochen‑Specker theorem is a no‑go result that shows that it is impossible to assign predetermined, non‑contextual values to all quantum observables in a way that respects the functional relations between them. In other words, any model that tries to give each observable a definite value independent of the measurement context (a “non‑contextual” value assignment) inevitably conflicts with the predictions of quantum theory[4]. The original proof demonstrates a logical impossibility of such value assignments, and later versions use inequalities or algebraic constructions (e.g., magic‑square or magic‑pentagram arrangements) to exhibit the same contradiction[4].

**Sources:**
- [1] 2105.13821 From the problem of Future Contingents to Peres-Mermin square experime (0.241) -
- [2] 2102.13036 Kochen-Specker Contextuality (0.302) relevant
- [3] 2408.16764 An algebraic characterisation of Kochen-Specker contextuality (0.32) relevant
- [4] 2102.13036 Kochen-Specker Contextuality (0.321) relevant
- [5] 1910.09591 Contextuality and the fundamental theorems of quantum mechanics (0.329) relevant

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #4 [contextuality/definition]
**Q:** What does it mean for quantum mechanics to be contextual?
**Answerable:** True  |  **Best distance:** 0.204  |  **Refused:** False
**Must include:** Outcome values cannot be assigned independent of the context of compatible measurements; Bell nonlocality is a special case; must not use the relational 'contextual' sense.
**Label notes:** Keyword hits 2107.10666 and 2510.09237 use 'contextual' in a different sense.

**Answer:**

Quantum mechanics is **contextual** when the outcomes of measurements cannot be explained by a single, pre‑existing assignment of values that is independent of which compatible set of other measurements (the “context”) is performed. In other words, there is a fundamental obstruction to describing quantum theory with classical, non‑contextual hidden‑variable models; the measurement results depend on the whole measurement context rather than on intrinsic properties of the system alone[1][5]. This contextuality is a key distinguishing feature between classical and quantum physics and underlies many quantum‑information applications[4].

**Sources:**
- [1] 2102.13036 Kochen-Specker Contextuality (0.204) relevant
- [2] 2105.13821 From the problem of Future Contingents to Peres-Mermin square experime (0.233) relevant
- [3] 2311.11218 State-independent all-versus-nothing arguments (0.247) relevant
- [4] 2408.16764 An algebraic characterisation of Kochen-Specker contextuality (0.247) relevant
- [5] 2102.13036 Kochen-Specker Contextuality (0.256) relevant

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #5 [decoherence/definition] (HOLD-OUT)
**Q:** What is decoherence?
**Answerable:** True  |  **Best distance:** 0.281  |  **Refused:** False
**Must include:** Loss of coherence via environment interaction, pointer states; distinguished from collapse; not presented as alone explaining single outcomes.
**Label notes:** Keyword hits on gravitational decoherence are use, not definition.

**Answer:**

Decoherence is the dynamical process by which a quantum system loses phase coherence through its interaction with an environment, causing the off‑diagonal elements of its reduced density matrix to be suppressed. This loss of coherence selects a set of stable “pointer” states (einselection) that are immune to further environmental disturbance, and it explains how quantum probability distributions evolve toward the classically expected ones without invoking any additional postulates or interpretations[1][3][4]. The process therefore addresses a consistency problem in open‑system quantum dynamics and underlies the emergence of classical‑like behavior from quantum systems[5].

**Sources:**
- [1] 1911.06282 Quantum Decoherence (0.281) relevant
- [2] 2502.19278 The Quantum Measurement Problem: A Review of Recent Trends (0.285) relevant
- [3] 1807.02092 Quantum Theory of the Classical: Quantum Jumps, Born's Rule, and Objec (0.297) relevant
- [4] 1911.06282 Quantum Decoherence (0.3) relevant
- [5] 2107.03378 Emergence of the Classical from within the Quantum Universe (0.302) relevant

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #6 [measurement/definition]
**Q:** What is the measurement problem in quantum mechanics?
**Answerable:** True  |  **Best distance:** 0.201  |  **Refused:** False
**Must include:** Unitary Schrodinger evolution versus apparent collapse on measurement (two rules); single definite outcomes; not presenting any solution as settled.
**Label notes:** Borderline: 1911.06282, 2112.11223, 1811.00902.

**Answer:**

The measurement problem is the tension between two different ways quantum theory describes a system’s evolution:  

* When a system is isolated it evolves **unitarily, deterministically** according to the Schrödinger equation, producing superpositions of possible outcomes.  
* When a measurement is performed the state undergoes a **non‑unitary, stochastic collapse** to a single definite outcome, as prescribed by the Born rule, and repeated measurements give the same result.  

This dual, apparently incompatible, rule of evolution—unitary dynamics versus collapse—creates a conceptual gap about what “measuring the system” actually means and how the quantum‑to‑classical transition occurs[4][5].  

Wojciech Zurek emphasizes that the problem stems from the lack of a clear definition of measurement and from differing discomforts with what happens during quantum measurements, noting that various interpretations (e.g., Everett, decoherence) claim to solve it without a universally accepted resolution[3].  

Thus, the measurement problem is the unresolved question of how and why the deterministic, reversible evolution of a closed quantum system gives way to the irreversible, probabilistic outcome observed in a measurement.

**Sources:**
- [1] 2210.10624 How Do the Probabilities Arise in Quantum Measurement? (0.201) relevant
- [2] 2112.11223 Events in quantum mechanics are maximally non-absolute (0.221) -
- [3] 2107.03378 Emergence of the Classical from within the Quantum Universe (0.249) relevant
- [4] 2502.19278 The Quantum Measurement Problem: A Review of Recent Trends (0.275) relevant
- [5] 2502.19278 The Quantum Measurement Problem: A Review of Recent Trends (0.283) relevant

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #7 [measurement/definition] (HOLD-OUT)
**Q:** What is the Born rule?
**Answerable:** True  |  **Best distance:** 0.386  |  **Refused:** False
**Must include:** Probability of an outcome equals the squared modulus of its amplitude (p_j = |a_j|^2), after which the state collapses to the outcome; presented as a rule of the theory, with derivations contested.
**Label notes:** Updated after grep: 1812.11140 states the rule explicitly in an accessible text. 1908.03949 unverified. Borderline: 1909.13027. Inline formulas can survive where display equations become [EQ].

**Answer:**

The Born rule states that the probability of obtaining a particular measurement outcome is given by the absolute square of the overlap (inner product) between the system’s state and the eigenstate corresponding to that outcome. In von Neumann’s formulation, if a system prepared in an initial eigenstate φ(0) of a Hamiltonian H(0) evolves to time t, the probability of finding it in the ν‑th eigenstate φ(t) of H(t) is  

\[
P = \bigl|\,\langle \phi(t)_\nu \mid \phi(0) \rangle \bigr|^{2},
\]

i.e. the modulus‑squared of the inner product of the two eigenstates [1].

**Sources:**
- [1] 2406.02149 Von Neumann's 1927 Trilogy on the Foundations of Quantum Mechanics. An (0.386) relevant

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #8 [uncertainty/definition]
**Q:** What does the Heisenberg uncertainty principle actually say?
**Answerable:** True  |  **Best distance:** 0.243  |  **Refused:** False
**Must include:** Position and momentum cannot both be sharply defined (Delta x Delta p >= hbar/2); property of states, not only measurement disturbance.
**Label notes:** Formula lost to [EQ] stripping. GUP paper 2202.07489 is a different topic. Borderline: 1912.07020, 2304.09037.

**Answer:**

The Heisenberg uncertainty principle states that one cannot determine simultaneously the values of two conjugate (incompatible) observables with arbitrary precision. In Heisenberg’s original argument the act of measurement itself perturbs the system: using a microscope with wavelength λ gives a position uncertainty Δx ≈ λ, while the Compton recoil of the electron introduces a momentum uncertainty Δp ≈ ħ/λ, leading to a trade‑off between the two uncertainties [1]. Later, this qualitative idea was cast into a quantitative inequality: for position x and momentum p, the product of their standard‑deviation uncertainties satisfies Δx Δp ≥ ħ⁄2, and the relation was generalized to arbitrary pairs of observables Q and R by Robertson and Schrödinger [5]. Thus, the principle asserts that the outcomes of two incompatible measurements cannot both be sharply defined; the more precisely one is known, the less precisely the other can be known.

**Sources:**
- [1] 1908.03949 An introduction to quantum measurements with a historical motivation (0.243) relevant
- [2] 1908.07694 The Complementary Information Principle of Quantum Mechanics (0.29) relevant
- [3] 1807.07829 Quasi-Fine-Grained Uncertainty Relations (0.299) relevant
- [4] 1908.03949 An introduction to quantum measurements with a historical motivation (0.314) relevant
- [5] 1912.07020 Quantum memory assisted entropic uncertainty relation with moving quan (0.354) -

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #9 [bell_epr/definition] (HOLD-OUT)
**Q:** What is the EPR paradox?
**Answerable:** True  |  **Best distance:** 0.338  |  **Refused:** False
**Must include:** EPR argued from locality and a criterion of reality that QM is incomplete; does not credit EPR with proving nonlocality.
**Label notes:** Borderline: 2107.10666.

**Answer:**

The EPR paradox is the conflict that arises when two spatially separated quantum systems are prepared in an entangled state so that measurements on one system allow one to predict with certainty the outcomes of complementary observables on the other, apparently violating the criteria of locality and realism that Einstein, Podolsky and Rosen (EPR) used to argue that quantum mechanics does not give a complete description of physical reality.  

* In the original EPR argument the “reality criterion’’ states that if the value of a physical quantity can be predicted with certainty without disturbing the system, then that quantity corresponds to an element of physical reality. When applied to entangled particles, this leads to the conclusion that both position and momentum (or other complementary observables) must have simultaneous reality, which conflicts with the quantum‑mechanical uncertainty principle. The paradox therefore highlights a tension between **EPR locality** (the idea that measurements on one subsystem cannot instantaneously affect the other) and the predictions of quantum mechanics [3].  

* Modern formulations express the paradox as an **incompleteness criterion**: the ability to infer, from measurements on system B, the values of non‑commuting observables of system A with sufficiently small average error (Δinf X̂_A, Δinf P̂_A) signals the EPR paradox and shows that quantum mechanics cannot account for all elements of reality without additional variables [4].  

* From a contextual interpretation, the paradox is explained by the entangled wave function itself: the correlated events are not independent “autonomous’’ happenings but are determined only within the measurement context. The “collapse’’ of the wave function is not a physical process but a shift to a specific measurement context that reveals the fragment of reality where the correlation resides [1].  

Thus, the EPR paradox is the demonstration that entangled quantum correlations, together with the EPR reality and locality criteria, imply that quantum mechanics is either non‑local or incomplete. The various excerpts present complementary viewpoints on this conflict.

**Sources:**
- [1] 2107.10666 The Real Meaning of Quantum Mechanics (0.338) -
- [2] 2004.04352 A Steering Paradox for Einstein-Podolsky-Rosen Argument and its Extend (0.347) relevant
- [3] 2105.02384 The EPR paper: a pedagogical approach (0.371) relevant
- [4] 2412.00406 Resolving Schrödinger's analysis of the Einstein-Podolsky-Rosen parado (0.385) relevant
- [5] 2009.08440 Metrological complementarity reveals the Einstein-Podolsky-Rosen parad (0.388) relevant

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #10 [foundations/definition] (HOLD-OUT)
**Q:** What is the Frauchiger-Renner paradox?
**Answerable:** True  |  **Best distance:** 0.53  |  **Refused:** True
**Must include:** Says 1812.11140 is a text on the foundations of QM that comments on and analyzes the Frauchiger-Renner Nature article; attributes to its author (Tausk) the claim that the 'paradox' is due to a misunderstanding of how to apply the quantum rules; does not present that claim as consensus; does not describe the paradox's details beyond what the excerpts give.
**Label notes:** Revised after grep: the earlier rubric came from outside knowledge. Retrieval best distance 0.53 > cutoff for this phrasing: false refusal. 2304.00608 only cites it in one sentence.

**Answer:**

I couldn't find relevant material in my collection of quantum foundations papers for that question. It may be outside the corpus (about 110 arXiv papers on measurement, interpretations, Bell/EPR, decoherence, contextuality and uncertainty), so try rephrasing or asking about one of those topics.

**Sources:**

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #11 [interpretations/definition]
**Q:** What is Bohmian mechanics?
**Answerable:** True  |  **Best distance:** 0.357  |  **Refused:** False
**Must include:** Particles with definite positions guided by the wave function (pilot wave, guiding equation); deterministic in its best-known form, no collapse; predictions equal standard QM; nonlocal.
**Label notes:** Verified by grep: 1812.11140 defines it. 2405.04368 only mentions Bohmian trajectories in passing, so excluded. 2502.19278 and 2401.01340 unverified. Borderline: 2306.07794.

**Answer:**

Bohmian mechanics is a realist formulation of quantum theory in which particles have definite positions at all times and are guided by the quantum state (the wave function) through a guiding equation.  It was originally proposed by David Bohm and later clarified and named “Bohmian mechanics” by Detlef Dürr (in analogy to Newtonian mechanics) and the Dürr‑Goldstein‑Zanghì collaboration, who gave it a more coherent definition and derived its typicality‑based justification of the Born rule[3][4].  The approach maintains a realist stance, keeping the same basic concepts as classical physics but modifying them to incorporate quantum effects, and it can be extended to quantum field theory, sometimes in non‑deterministic forms[2].  It reproduces the standard quantum‑mechanical experimental predictions while providing a clear ontology of particles and a guiding wave[1].

**Sources:**
- [1] 2212.12782 Tightrope-walking rationality in action: Feyerabendian insights for th (0.357) -
- [2] 1812.11140 A brief introduction to the Foundations of Quantum Theory and an analy (0.373) relevant
- [3] 2405.04368 Some Things I Have Learned From Detlef Dürr (0.374) -
- [4] 2405.04368 Some Things I Have Learned From Detlef Dürr (0.391) -
- [5] 2502.19278 The Quantum Measurement Problem: A Review of Recent Trends (0.418) relevant

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #12 [decoherence/definition]
**Q:** What is quantum Darwinism?
**Answerable:** True  |  **Best distance:** 0.32  |  **Refused:** False
**Must include:** Pointer-state information copied redundantly into many environment fragments, allowing independent observers to agree (objectivity); part of the decoherence program; does not alone solve the measurement problem.
**Label notes:** Semantic ranks 4-5 (1909.13027, 2504.14791) are off-topic. Borderline: 2205.12927, 2001.10851.

**Answer:**

Quantum Darwinism is a framework that extends decoherence theory by treating the environment as a communication channel that records and proliferates information about a quantum system.  When a system interacts with its surroundings, the environment “monitors” the system and selectively copies information about certain stable states (the pointer states) into many independent fragments.  These redundantly stored copies allow observers to infer the system’s state indirectly—by intercepting parts of the environment—without significantly disturbing the system itself.  The process makes some system states “fitter” because they can imprint their information robustly and redundantly across the environment, thereby explaining the emergence of objective, classical‑like reality [1][3][5].  Zurek emphasizes that quantum Darwinism builds on decoherence and einselection, clarifying their role in the interpretation of quantum theory and the perception of collapse [2].

**Sources:**
- [1] 1911.06282 Quantum Decoherence (0.32) relevant
- [2] 2107.03378 Emergence of the Classical from within the Quantum Universe (0.322) relevant
- [3] 1911.06282 Quantum Decoherence (0.332) relevant
- [4] 1807.02092 Quantum Theory of the Classical: Quantum Jumps, Born's Rule, and Objec (0.378) relevant
- [5] 2107.03378 Emergence of the Classical from within the Quantum Universe (0.379) relevant

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #13 [interpretations/comparison]
**Q:** What is the fundamental difference between the Copenhagen interpretation and the many-worlds interpretation?
**Answerable:** True  |  **Best distance:** 0.229  |  **Refused:** False
**Must include:** Copenhagen: collapse to a single outcome on measurement; many-worlds: no collapse, all outcomes realized in branches; 'Copenhagen' is not one agreed doctrine.
**Label notes:** Pair: Copenhagen from 1908.03949 plus MWI from 1801.08587. 1909.13027 rejected.

**Answer:**

The Copenhagen interpretation treats a quantum measurement as selecting a single outcome: it “cuts off” all other components of the state‑vector and retains only the branch that corresponds to the observed result[2]. In contrast, the many‑worlds interpretation holds that no such collapse occurs; the state‑vector continues to evolve unitarily and all possible outcomes remain realized in separate, non‑communicating branches of the universe[3]. Thus, Copenhagen posits a single classical world emerging from a quantum description, while many‑worlds posits a single quantum universe that continually branches into many coexisting classical worlds.

**Sources:**
- [1] 1812.11140 A brief introduction to the Foundations of Quantum Theory and an analy (0.229) relevant
- [2] 1801.08587 Making Sense of the Many Worlds Interpretation (0.244) relevant
- [3] 2502.19278 The Quantum Measurement Problem: A Review of Recent Trends (0.291) relevant
- [4] 2502.19278 The Quantum Measurement Problem: A Review of Recent Trends (0.293) relevant
- [5] 1801.08587 Making Sense of the Many Worlds Interpretation (0.309) relevant

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #14 [interpretations/comparison] (HOLD-OUT)
**Q:** How does Bohmian mechanics differ from standard quantum mechanics in how it treats particles?
**Answerable:** True  |  **Best distance:** 0.242  |  **Refused:** False
**Must include:** Bohmian particles always have definite positions guided by the wave function; standard QM particles have no definite position before measurement; predictions are equivalent; must not claim different predictions.
**Label notes:** Borderline: 2405.04368, 2306.07794.

**Answer:**

Bohmian mechanics assigns each particle a **real, definite position at all times** and describes its motion by a guiding (pilot‑wave) equation in which the quantum state (wave function) directs the particle’s trajectory.  In contrast, standard quantum mechanics does not posit such ontic particle positions or trajectories; the wave function alone encodes the system’s properties and observable outcomes are obtained only probabilistically.  

- The pilot‑wave “guides the particles” and the particles have well‑defined positions that evolve according to a guiding equation [1].  
- By contrast, standard quantum mechanics treats particles only through the wave function and does not include additional hidden variables specifying their positions [3] (which notes that Bohmian predictions are equivalent to quantum mechanics but that Bohmian theory adds deterministic trajectories).

**Sources:**
- [1] 1812.11140 A brief introduction to the Foundations of Quantum Theory and an analy (0.242) relevant
- [2] 2405.04368 Some Things I Have Learned From Detlef Dürr (0.326) -
- [3] 2502.19278 The Quantum Measurement Problem: A Review of Recent Trends (0.347) relevant
- [4] 2212.12782 Tightrope-walking rationality in action: Feyerabendian insights for th (0.36) -
- [5] 2405.04368 Some Things I Have Learned From Detlef Dürr (0.386) -

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #15 [contextuality/comparison] (HOLD-OUT)
**Q:** How is quantum contextuality different from Bell nonlocality?
**Answerable:** True  |  **Best distance:** 0.159  |  **Refused:** False
**Must include:** Bell nonlocality is contextuality where spacelike separation guarantees compatibility; contextuality needs no separation and applies to a single system; not unrelated.
**Label notes:** Rejected keyword hits: 2005.03835, 2210.05985, 2104.10700.

**Answer:**

Quantum contextuality and Bell nonlocality refer to two distinct kinds of non‑classical correlations.

* **Bell nonlocality** concerns correlations between outcomes of measurements performed on *spacelike‑separated* parties.  It is manifested by the violation of Bell inequalities (e.g., CHSH) and shows that no classical causal model respecting relativistic locality can reproduce the observed statistics [1][3][4].

* **Quantum contextuality** (Kochen‑Specker contextuality) concerns the dependence of a measurement’s outcome statistics on the *measurement context*—the set of compatible observables measured jointly—rather than on spatial separation.  It is expressed by the impossibility of assigning non‑contextual, deterministic values to all observables simultaneously, and is witnessed by violations of non‑contextuality inequalities such as KCBS [1][3][4].

Thus, Bell nonlocality is a special case of contextuality that arises when the compatibility relations are dictated solely by spatial separation, whereas contextuality more generally captures the failure of outcome statistics to be independent of the measurement context even for a single system.

**Sources:**
- [1] 2405.02964 Trade-off relations between Bell nonlocality and local Kochen-Specker  (0.159) relevant
- [2] 2102.13036 Kochen-Specker Contextuality (0.194) relevant
- [3] 1909.05434 Classical causal models cannot faithfully explain Bell nonlocality or  (0.207) relevant
- [4] 2204.05385 Synchronous observation of Bell nonlocality and state-dependent Kochen (0.215) relevant
- [5] 2405.02964 Trade-off relations between Bell nonlocality and local Kochen-Specker  (0.218) relevant

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #16 [uncertainty/comparison]
**Q:** Is the uncertainty principle the same thing as the observer effect?
**Answerable:** True  |  **Best distance:** 0.425  |  **Refused:** False
**Must include:** Presents measurement disturbance (Feynman's invasive measurement; Heisenberg's microscope argument) and the uncertainty principle (observables that cannot be jointly measured) as related but not the same, noting that disturbance alone does not explain why values cannot be predetermined; does not say the excerpts call them identical.
**Label notes:** Partial: no excerpt states the distinction outright; closest is 2105.13821 (Beyond measurement disturbance). 1908.03949 gives the historical link and calls the microscope argument not very rigorous. 1809.03475 unverified. Rubric stays within corpus: modern error-disturbance vs preparation-uncertainty distinction is outside it. Best semantic distance 0.425, near the cutoff; top hit 2409.02354 off-target.

**Answer:**

The uncertainty principle and the observer (measurement‑disturbance) effect are not the same thing.  

- The uncertainty principle is presented as a fundamental property of quantum systems, expressing intrinsic limits on the simultaneous sharpness of pairs of observables (e.g., position–momentum, energy–time) independent of any technological or observational constraints [1].  

- The observer effect refers to the invasive nature of measurement: the act of measuring a quantum system modifies it, as described by the Born rule for outcome probabilities and Lüder’s rule for state update [2]. The text notes that this disturbance is a separate issue from whether measurement disturbance alone can enforce the impossibility of predetermined outcomes, and it mentions that one might try to invoke the uncertainty principle in that context [2].  

Thus, the uncertainty principle is an intrinsic statistical relation between observables, whereas the observer effect concerns the physical disturbance caused by the measurement process.

**Sources:**
- [1] 2409.02354 Entangled in Spacetime (0.425) -
- [2] 2105.13821 From the problem of Future Contingents to Peres-Mermin square experime (0.435) relevant

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #17 [decoherence/comparison] (HOLD-OUT)
**Q:** How does decoherence differ from wave function collapse?
**Answerable:** True  |  **Best distance:** 0.244  |  **Refused:** False
**Must include:** Decoherence is unitary and removes interference, giving an apparent mixture without selecting one outcome; collapse is a non-unitary postulate that does; decoherence alone does not solve the measurement problem.
**Label notes:** 2406.19158 (photon-collapse proposal) rejected despite top keyword rank. Borderline: 2408.08329.

**Answer:**

Decoherence and wave‑function collapse are distinct processes.

* **Decoherence** acts only on the off‑diagonal elements of the reduced density matrix of a system (obtained after tracing out the environment), turning them effectively to zero and leaving a diagonal matrix in the basis selected by the system‑environment interaction. It is a unitary, environment‑induced process that does not select a single outcome; the full density matrix of system + apparatus + observer remains a superposition. [2][4]

* **Wave‑function collapse** (or “state reduction”) eliminates all but one diagonal term of the *entire* density matrix that includes system, apparatus and observer, leaving a single definite state. Collapse is therefore a non‑unitary, additional postulate that picks one outcome from the diagonalized mixture. [2][5]

Thus, decoherence explains the loss of coherence (off‑diagonal terms) without producing a single definite result, whereas collapse is invoked to account for the actual selection of one outcome. The papers also note that decoherence alone cannot cause collapse; collapse must be added as a separate axiom (e.g., in relational quantum mechanics). [5]

**Sources:**
- [1] 2303.07966 Universality in Quantum Measurements (0.244) relevant
- [2] 2502.19278 The Quantum Measurement Problem: A Review of Recent Trends (0.251) relevant
- [3] 2012.12033 The Measurement Process in Relational Quantum Mechanics (0.297) relevant
- [4] 1911.06282 Quantum Decoherence (0.301) relevant
- [5] 2012.12033 The Measurement Process in Relational Quantum Mechanics (0.321) relevant

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #18 [interpretations/comparison]
**Q:** How do objective collapse theories differ from the many-worlds interpretation?
**Answerable:** True  |  **Best distance:** 0.335  |  **Refused:** False
**Must include:** Objective collapse: stochastic non-unitary modification so one outcome really occurs; many-worlds: pure unitary evolution, all outcomes realized in branches; collapse models in principle testable (bounds tightening); not the same theory.
**Label notes:** Verified by grep: 2111.07730 only mentions objective collapse in one survey sentence, so borderline, not relevant. Rejected: 2109.02310, 1909.01798.

**Answer:**

**Short answer:**  
Objective‑collapse theories posit a genuine physical collapse of the wavefunction that turns a superposition into a single outcome (either only statistically, “epistemic collapse”, or by zeroing all but one diagonal element, “ontic collapse”) and therefore modify the standard unitary dynamics. The Many‑Worlds Interpretation (MWI) rejects any real collapse; it keeps the Schrödinger equation exact and explains the appearance of definite outcomes by decoherence‑induced branching of the universal wavefunction into non‑communicating classical branches, each containing an observer who sees one result.

**Supporting detail**

* Collapse vs. no‑collapse:  A theory that includes collapse can produce a diagonal density matrix, leaving only statistical uncertainty about which outcome occurred (epistemic collapse) or, in the stronger case, eliminate all but one diagonal element, yielding an ontic collapse of the state [1].  

* Many‑Worlds description:  In MWI the quantum state \(|\psi\rangle\) is a complete description of reality and evolves solely according to the Schrödinger equation; collapse is regarded as an illusion caused by the universe branching into independent classical branches after decoherence [2]. Observers become entangled with the measured system, so each branch contains a copy of the observer who perceives a definite outcome, and no superposed observer states are observed because decoherence suppresses them [2].

Thus, objective‑collapse models introduce a non‑unitary, stochastic (or deterministic) dynamical rule that selects a single outcome, whereas MWI retains purely unitary evolution and explains definite outcomes by branching rather than by any physical collapse. The excerpts do not discuss specific objective‑collapse proposals beyond this general contrast.

**Sources:**
- [1] 2502.19278 The Quantum Measurement Problem: A Review of Recent Trends (0.335) relevant
- [2] 2502.19278 The Quantum Measurement Problem: A Review of Recent Trends (0.341) relevant
- [3] 1812.11140 A brief introduction to the Foundations of Quantum Theory and an analy (0.352) relevant
- [4] 1801.08587 Making Sense of the Many Worlds Interpretation (0.375) relevant
- [5] 1801.08587 Making Sense of the Many Worlds Interpretation (0.38) relevant

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #19 [interpretations/comparison]
**Q:** How does QBism differ from the Copenhagen interpretation?
**Answerable:** True  |  **Best distance:** 0.177  |  **Refused:** False
**Must include:** Attributes positions: Copenhagen (Bohr's version) treats outcomes as products of the system-apparatus interaction, not objective properties, and has diverse versions; one paper asserts QBism differs fundamentally from Copenhagen, another groups both as orthodox; no single verdict.
**Label notes:** Contested. Verified by grep: in 2301.04014 the 'QBism differs fundamentally' line is the author's cited assertion and his main argument is about Ozawa's theorem; watch for misattribution. Borderline: 2510.11544, 1908.03949. Rejected: 2510.09237.

**Answer:**

QBism is presented as a view that departs fundamentally from the traditional Copenhagen family of interpretations.  In particular, Khrennikov notes that “QBism differs crucially from various versions of the Copenhagen interpretation” [1].  The QBist program treats quantum probabilities as an agent’s personal, Bayesian degrees of belief and regards the measuring device as an extension of the agent, emphasizing subjectivity and the agent‑world interaction rather than an objective collapse or a purely epistemic‑ontic split that characterizes many Copenhagen accounts [5][1].  Moreover, the historical record shows that QBism only coalesced as a distinct interpretation after a series of developments beginning around 2009, whereas earlier “Copenhagen‑style” papers (e.g., Caves et al. 2002) are now seen as precursors rather than full expressions of QBism [2].  These points together illustrate the claimed differences between QBism and Copenhagen.

**Sources:**
- [1] 2301.04014 Ozawa's Intersubjectivity Theorem as objection to QBism individual age (0.177) relevant
- [2] 2510.11544 French on London and Bauer, and QBism (0.268) -
- [3] 2510.09237 QBism and relational interpretation of quantum mechanics from the poin (0.281) -
- [4] 2107.03513 Qubits are not observers -- a no-go theorem (0.305) relevant
- [5] 2510.09237 QBism and relational interpretation of quantum mechanics from the poin (0.314) -

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #20 [bell_epr/comparison] (HOLD-OUT)
**Q:** What is the difference between entanglement and Bell nonlocality?
**Answerable:** True  |  **Best distance:** 0.206  |  **Refused:** False
**Must include:** Entanglement necessary but not sufficient for Bell nonlocality; maximal entanglement and maximal violation do not coincide; the claim that nonlocality is entanglement is attributed to 2012.06918 and noted as contested.
**Label notes:** Hold-out. Borderline: 2410.15790. Rejected: 2104.10700.

**Answer:**

Entanglement and Bell nonlocality are related but distinct quantum resources.  Entanglement refers to any quantum inseparability that cannot be created by local operations and classical communication (LOCC) and underlies many quantum‑information protocols [1][2].  Bell nonlocality is a stricter form of correlation: it denotes correlations that cannot be explained by any local hidden‑variable model and therefore constitute a proper subset of entangled states [5][3].  In other words, every Bell‑nonlocal state is entangled, but not all entangled states exhibit Bell nonlocality [5].  Some works even describe Bell nonlocality as “just a special type of entanglement” [2].

**Sources:**
- [1] 1909.00346 Inequality relation between entanglement and Bell nonlocality for arbi (0.206) relevant
- [2] 2012.06918 Quantum Bell Nonlocality is Entanglement (0.229) relevant
- [3] 2012.06918 Quantum Bell Nonlocality is Entanglement (0.245) relevant
- [4] 2005.03835 Entanglement versus Bell nonlocality of quantum nonequilibrium steady  (0.261) relevant
- [5] 1909.00346 Inequality relation between entanglement and Bell nonlocality for arbi (0.271) relevant

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #21 [contextuality/comparison]
**Q:** How do local hidden variable models differ from noncontextual hidden variable models?
**Answerable:** True  |  **Best distance:** 0.352  |  **Refused:** False
**Must include:** Local model: outcomes depend on local settings plus a shared variable; noncontextual model: outcome values independent of compatible co-measured context; local models are a special case.
**Label notes:** Pair: LHV from 2104.10700, NCHV from 2102.13036. Overlaps #15, consider swapping. Borderline: 2311.11218, 2212.06976.

**Answer:**

Local hidden‑variable (LHV) models, as used in non‑locality scenarios, are built on the **factorisability** assumption: the hidden variables must factor into independent parts for separated parties.  
Noncontextual hidden‑variable (NCHV) models, in contrast, are based on **determinism**: the hidden variables assign definite outcomes to each measurement independently of the measurement context.  

Thus the key difference is the structural constraint imposed on the hidden variables—factorisability for LHV models versus determinism for NCHV models[1].

**Sources:**
- [1] 2105.13821 From the problem of Future Contingents to Peres-Mermin square experime (0.352) relevant
- [2] 2102.13036 Kochen-Specker Contextuality (0.4) relevant
- [3] 2102.13036 Kochen-Specker Contextuality (0.43) relevant

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #22 [uncertainty/comparison]
**Q:** How do Heisenberg's and Robertson's uncertainty relations differ?
**Answerable:** True  |  **Best distance:** 0.31  |  **Refused:** False
**Must include:** Heisenberg proposed the first relation (heuristic, position and momentum); Kennard formalized it as Delta x Delta p >= hbar/2; Robertson and Schrodinger generalized it to arbitrary incompatible observables.
**Label notes:** Verified by grep of 1912.07020, which credits Kennard with the formal inequality. Rubric stays within excerpts (Schrodinger's covariance term not stated there). Formulas lost to [EQ]. Rejected: 2306.06602, 2006.04358.

**Answer:**

Heisenberg’s original relation was a specific inequality for position \( \hat x \) and momentum \( \hat p \):  

\[
\Delta \hat x\,\Delta \hat p \ge \hbar/2 ,
\]

where the uncertainties are the standard deviations of those two canonical observables [4].

Robertson (and later Schrödinger) extended this to **any pair of incompatible observables** \( \hat Q \) and \( \hat R \). Their generalized relation has the form  

\[
\Delta \hat Q\,\Delta \hat R \ge \frac{1}{2}\bigl| \langle[\hat Q,\hat R]\rangle \bigr| ,
\]

so the lower bound depends on the quantum state through the expectation value of the commutator, and can become trivial when that expectation value vanishes [1][4].  

Thus, Heisenberg’s rule is a special case (position–momentum) with a fixed bound \( \hbar/2 \), while Robertson’s rule is a state‑dependent bound applicable to arbitrary observables.

**Sources:**
- [1] 1912.07020 Quantum memory assisted entropic uncertainty relation with moving quan (0.31) relevant
- [2] 1806.08133 Uncertainty principle as post-quantum nonlocality witness for continuo (0.354) relevant
- [3] 1908.07694 The Complementary Information Principle of Quantum Mechanics (0.383) -
- [4] 1912.07020 Quantum memory assisted entropic uncertainty relation with moving quan (0.389) relevant
- [5] 1807.07829 Quasi-Fine-Grained Uncertainty Relations (0.393) -

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #23 [measurement/contested]
**Q:** Is an observer required for the wave function to collapse?
**Answerable:** True  |  **Best distance:** 0.341  |  **Refused:** False
**Must include:** Separate attributed positions: collapse as a postulate (process 1); no literal collapse with observer inside the wave function; apparent collapse tied to the observer's state; spontaneous collapse without observer; notes 'observer' is ambiguous; no verdict.
**Label notes:** Contested. Development question. Check Boughn attribution (he describes the 'in the mind' view). Rejected: 2406.19158 (verified by grep: unusual retrocausal/photon-collapse claims, not a source for this question), 1909.13027.

**Answer:**

The excerpts do not give a single, definitive answer; they present several contrasting viewpoints.

* **Some authors treat the observer as central to collapse.**  
  – Boughn notes that “some physicists prefer to claim, euphemistically, that wave‑function collapse happens in the mind of the observer but not for any physical reason” [1].

* **Other authors deny that any physical collapse occurs at all, so no observer is needed.**  
  – Zurek describes Everett’s approach, in which the literal collapse is abandoned and the observer is simply another part of the universal wavefunction; the appearance of a definite outcome is explained by branching rather than by a collapse triggered by observation [3].

* **A more neutral technical description separates collapse from unitary evolution without invoking an observer.**  
  – Koprinkov states that collapse “cannot be described by the Schrödinger equation” and is part of “process 1” (measurement), but does not tie this process to the presence of an observer [2].

* **Experimental proposals aim to test the timing of collapse but do not assert that an observer is required.**  
  – Vishwas’s thought‑experiment paper mentions that demonstrating a delayed collapse could help scrutinize various interpretations, without committing to an observer‑dependence [4].

Thus, the retrieved papers present both positions—some linking collapse to the observer’s mind, others eliminating collapse altogether—so they do not converge on a single answer to whether an observer is required for wave‑function collapse.

**Sources:**
- [1] 1801.08587 Making Sense of the Many Worlds Interpretation (0.341) relevant
- [2] 2309.17377 Quantum Superposition, Collapse of Wave Function, Quantum Measurement  (0.374) relevant
- [3] 1807.02092 Quantum Theory of the Classical: Quantum Jumps, Born's Rule, and Objec (0.386) relevant
- [4] 2111.07730 Superposition in Measuring Apparatus: A Thought Experiment (0.386) relevant
- [5] 2509.12280 The Emergence of Objective Classicality: A Computational First-Princip (0.391) relevant

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #24 [measurement/contested]
**Q:** Does collapse really take place, and how could it be scientifically verified?
**Answerable:** True  |  **Best distance:** 0.273  |  **Refused:** False
**Must include:** No consensus collapse occurs; decoherence and many-worlds are alternatives; verification via testing collapse models (matter-wave interferometry, collapse-induced heating, X-ray emission), bounds tightening and ruling out parameter ranges, and separating collapse from decoherence; does not claim collapse is confirmed.
**Label notes:** Two-part, cross-bucket. Development question. Top semantic hit 2406.19158 (0.273) is off-target: verified by grep, its claims are retrocausal/photon-collapse, not experimental tests. Retrieval failure and corpus-quality issue. 2010.14965 rejected (only its own Fock-space framework). Borderline: 2309.17377.

**Answer:**

The papers do not present definitive evidence that a physical collapse actually occurs; they treat it as a hypothesized, non‑unitary process that would have to be distinguished from ordinary decoherence.  

* Zurek notes that collapse is non‑unitary and that its key attribute—symmetry breaking in the choice of a single orthonormal basis—can be inferred from the core quantum postulates, but this reasoning does not constitute an empirical demonstration of collapse itself [3].  
* Schlosshauer points out that to isolate a genuine reduction effect one would need to shield a system from decoherence, which is extremely difficult because the systems large enough for collapse to become appreciable are also those that decohere very quickly. Current superposition experiments are not yet macroscopic enough to rule out collapse theories, although proposed matter‑wave interferometry with large molecular clusters could test them [4].  
* The review of objective‑collapse models reports experimental efforts such as underground searches for spontaneous radiation (which would signal collapse‑induced diffusion) that have placed strong limits on certain proposals (e.g., the original Diósi‑Penrose model), but these limits only constrain parameter ranges rather than confirm collapse [5].

Thus, according to the cited excerpts, collapse remains a theoretical hypothesis; its scientific verification would require experiments that can (i) suppress environmental decoherence for sufficiently large systems and (ii) detect signatures predicted by specific collapse models (e.g., spontaneous radiation or loss of interference in massive interferometers). No existing experiment has yet provided conclusive proof that collapse occurs.

**Sources:**
- [1] 2406.19158 A Method Using Photon Collapse and Entanglement to Transmit Informatio (0.273) -
- [2] 2502.19278 The Quantum Measurement Problem: A Review of Recent Trends (0.326) relevant
- [3] 1807.02092 Quantum Theory of the Classical: Quantum Jumps, Born's Rule, and Objec (0.386) relevant
- [4] 1911.06282 Quantum Decoherence (0.396) relevant
- [5] 2502.19278 The Quantum Measurement Problem: A Review of Recent Trends (0.396) relevant

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #25 [foundations/contested]
**Q:** Does the wave function describe physical reality or only our knowledge?
**Answerable:** True  |  **Best distance:** 0.372  |  **Refused:** False
**Must include:** Epistemic/instrumental readings (orthodox, relational, QBism: state as a tool for predicting outcomes) and realist ones (Bohmian, collapse, many-worlds), attributed to sources; may use the epistemic vs ontic collapse distinction from 2502.19278; no verdict.
**Label notes:** Contested. Verified by grep: 2502.19278 has an ontological-status section, epistemic interpretations, and epistemic vs ontic collapse. Borderline: 2510.09237, 2203.16278.

**Answer:**

The papers present several, mutually exclusive positions:

* **Ψ‑epistemic (knowledge‑only) view** – The wave function is a symbolic or mathematical tool that encodes statistical predictions about measurement outcomes and does not represent a real physical entity.  This is the stance of the “orthodox” or Copenhagen‑type approach quoted in [1], which calls the wave function “mere symbolic entities … used to make probabilistic predictions” and notes von Neumann’s view that only statistical statements can be made about physical quantities.  A similar epistemic reading is given in [5], where the wave function in relational quantum mechanics is said to be “interpreted epistemically” and functions as a tool for acquiring knowledge.

* **Contextual realist / mixed view** – [2] argues that the wave function is neither a literal exterior reality nor merely a predictive tool.  It is taken to be a formal cause of quantum correlations whose reality is contextual, and its reduction is not a physical process.

* **Ψ‑ontic (physical‑reality) view** – [4] claims that the wave function is “intimately tied to the physical reality of these fields” and represents the state of the underlying quantum field itself, thus having direct physical significance.  The review in [3] also notes that many‑worlds, objective‑collapse, and hidden‑variable theories adopt a ψ‑ontic stance, treating the wave function as an actual physical object.

* **Neutral framing** – [3] outlines the broader debate, defining the two camps (ψ‑ontic vs ψ‑epistemic) without endorsing either, and points out that the ψ‑epistemic argument often rests on the wave function’s existence in a high‑dimensional configuration space.

Thus, the retrieved papers do not converge on a single answer: some treat the wave function as a purely epistemic device ([1], [5]), others as a physically real field‑state ([4]), and still others adopt a contextual realist position that is neither fully realist nor purely epistemic ([2]), while [3] simply maps the controversy.

**Sources:**
- [1] 1908.03949 An introduction to quantum measurements with a historical motivation (0.372) relevant
- [2] 2107.10666 The Real Meaning of Quantum Mechanics (0.406) relevant
- [3] 2502.19278 The Quantum Measurement Problem: A Review of Recent Trends (0.407) relevant
- [4] 2409.02354 Entangled in Spacetime (0.414) relevant
- [5] 2510.09237 QBism and relational interpretation of quantum mechanics from the poin (0.416) -

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #26 [bell_epr/contested] (HOLD-OUT)
**Q:** Is quantum mechanics a complete description of reality?
**Answerable:** True  |  **Best distance:** 0.251  |  **Refused:** False
**Must include:** EPR argued incompleteness from locality plus a criterion of reality; Bell showed local hidden-variable completions cannot reproduce QM; Copenhagen says complete, Bohmian adds nonlocal positions, collapse models change dynamics; no consensus.
**Label notes:** Hold-out. Contested. Borderline: 2005.03835, 2306.07794, 2203.16278.

**Answer:**

Quantum mechanics is **not** universally regarded as a complete description of reality.  
- The original Einstein‑Podolsky‑Rosen analysis concluded that quantum mechanics fails to be complete, based on their criteria of completeness, elements of physical reality, locality and the uncertainty principle [1].  
- Subsequent discussions note that different interpretations (Copenhagen, von Neumann collapse, Bohm‑de Broglie pilot wave, Everett many‑worlds) each alter the classical notion of reality, and there is no consensus that the formalism alone provides a complete picture [4].

**Sources:**
- [1] 2105.02384 The EPR paper: a pedagogical approach (0.251) relevant
- [2] 2306.07794 An Elementary Proof That Everett's Quantum Multiverse Is Nonlocal: Bel (0.256) -
- [3] 2203.16278 Does Science need Intersubjectivity? The Problem of Confirmation in Or (0.313) -
- [4] 1906.05456 Reality facing quantum mechanics (0.32) relevant
- [5] 2109.02310 The operational framework for quantum theories is both epistemological (0.322) -

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #27 [bell_epr/contested]
**Q:** Does Bell's theorem prove that nature is nonlocal?
**Answerable:** True  |  **Best distance:** 0.29  |  **Refused:** False
**Must include:** Bell rules out local hidden-variable models under assumptions (locality, statistical independence), so 'nature is nonlocal' depends on them; attributes Bohmian 'inevitable nonlocality', relaxed-independence local-realist escapes (2502.19278), and Everettian discussion; does not claim faster-than-light signaling.
**Label notes:** Contested. Borderline: 2001.07656, 2012.06918, 1910.09591, 2201.01886.

**Answer:**

Bell’s theorem shows that any **local realistic model** cannot reproduce the predictions of quantum mechanics; in other words, quantum mechanics is incompatible with “local realism” [1].  Several authors interpret this incompatibility as evidence that quantum correlations are **non‑local**, and they identify Bell nonlocality as a manifestation of entanglement [2][5].  However, the excerpts do not present Bell’s theorem as an unequivocal proof that nature itself is non‑local; they only state that local hidden‑variable models fail to account for quantum predictions.  Thus, the papers support the claim that Bell’s theorem rules out local realistic descriptions, but they do not settle whether nature is definitively non‑local.

**Sources:**
- [1] 2201.01886 Deterministic all-versus-nothing proofs of Bell nonlocality based on n (0.29) -
- [2] 2012.06918 Quantum Bell Nonlocality is Entanglement (0.301) -
- [3] 2001.07656 Proof of the Peres conjecture for contextuality (0.306) -
- [4] 2306.07794 An Elementary Proof That Everett's Quantum Multiverse Is Nonlocal: Bel (0.309) relevant
- [5] 2012.06918 Quantum Bell Nonlocality is Entanglement (0.32) -

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #28 [decoherence/contested] (HOLD-OUT)
**Q:** Does decoherence solve the measurement problem?
**Answerable:** True  |  **Best distance:** 0.223  |  **Refused:** False
**Must include:** Decoherence explains apparent loss of interference and emergence of classicality but does not select one outcome; the unitary account cannot describe selection of a particular term; whether this is a genuine difficulty depends on one's interpretation of quantum states; no verdict.
**Label notes:** Hold-out. Contested. Verified by grep of 1911.06282 (section 7.1; 'merely addresses a consistency problem'). Rejected keyword hits: 1804.04309 (education paper), 2001.10851.

**Answer:**

Decoherence alone does not solve the measurement problem.  

- Schlosshauer explicitly states that decoherence “by itself, cannot address the measurement problem in any substantial way” because it presupposes the collapse postulate and Born’s rule and does not explain how definite outcomes arise [4].  
- The review by Tomaz et al. emphasizes that decoherence and collapse are distinct phenomena and that decoherence only suppresses off‑diagonal terms, while a solution to the measurement problem would require a mechanism that selects a single outcome (i.e., collapse) [1].  

Thus, according to the cited papers, decoherence is a useful ingredient but is insufficient by itself to resolve the measurement problem.

**Sources:**
- [1] 2502.19278 The Quantum Measurement Problem: A Review of Recent Trends (0.223) relevant
- [2] 2012.12033 The Measurement Process in Relational Quantum Mechanics (0.231) relevant
- [3] 2303.07966 Universality in Quantum Measurements (0.247) relevant
- [4] 1911.06282 Quantum Decoherence (0.257) relevant
- [5] 2303.07966 Universality in Quantum Measurements (0.261) relevant

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #29 [measurement/contested]
**Q:** Can the Born rule be derived, or is it a postulate?
**Answerable:** True  |  **Best distance:** 0.366  |  **Refused:** False
**Must include:** Attributed positions: postulate (standard textbook view; QBism as an empirical rule); derivation attempts (envariance, stochastic collapse dynamics, many-worlds axioms, retrocausal model) with circularity objections; no consensus.
**Label notes:** Contested. Development question. Verified by grep: 1812.11140 states it as a rule of the theory; 2502.19278 reports a retrocausal derivation (Sutherland). Borderline: 2105.13821, 2302.08892.

**Answer:**

The papers present both views.

* **Derivation claim** – Von Neumann’s 1927 work explicitly derives the Born rule from the time‑evolution of eigenstates of a time‑dependent Hamiltonian, showing that the probability of finding the system in a later eigenstate is the absolute square of the inner product of the two eigenstates [1].

* **Postulate / necessity claim** – Other authors treat the Born rule as a fundamental assumption. Konishi notes that the rule is sufficient for reproducing expectation‑value statistics and asks whether it is also necessary, implying it is taken as a postulate unless additional equalities are proved [2]. Zurek observes that, before a decoherence‑based derivation was proposed, the rule was simply used as a given probability formula [3], and that its compatibility with relative‑state approaches is “at odds” with their spirit, again suggesting it is normally assumed rather than derived.

Thus, one source (von Neumann) claims a derivation, while other works treat the Born rule as a postulate or an assumed ingredient pending a decoherence‑based derivation. The excerpts do not provide a universally accepted derivation; they reflect differing positions.

**Sources:**
- [1] 2406.02149 Von Neumann's 1927 Trilogy on the Foundations of Quantum Mechanics. An (0.366) relevant
- [2] 2302.08892 Quantum fluctuations, particles and entanglement: solving the quantum  (0.434) -
- [3] 1807.02092 Quantum Theory of the Classical: Quantum Jumps, Born's Rule, and Objec (0.444) relevant

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #30 [interpretations/contested] (HOLD-OUT)
**Q:** How can probabilities make sense in the many-worlds interpretation?
**Answerable:** True  |  **Best distance:** 0.273  |  **Refused:** False
**Must include:** The puzzle: what probability means if every outcome occurs; proposed answers (decision-theoretic axioms, credences over centred worlds) with critics; no consensus.
**Label notes:** Hold-out. Contested. Verified by grep: 1812.11140 covers only the basic Born rule, not many-worlds probability, so excluded; it ranked 2nd semantically (0.278): retrieval noise. Borderline: 2107.10666.

**Answer:**

Probabilities in the many‑worlds interpretation remain controversial.  

* Drezet notes that existing proposals only give “self‑consistent rules” that reproduce the Born rule once a probability is **assumed** to exist, but a clear justification for assigning probabilities to branches is still missing; the author argues that such a justification would require adding new physical axioms beyond Everett’s pure unitary dynamics[2].  

* Tausk points out the core difficulty: if every possible outcome actually occurs in some branch, it is unclear what it means to say that one outcome has a certain probability, since the “probabilities” reduce to the squared moduli of the state‑vector coefficients without an operational interpretation[3].  

* A more optimistic view is mentioned in a review that the Born rule uniquely satisfies certain axioms and is therefore adopted by many‑worlds supporters, but this does not resolve the foundational question of why the rule should be interpreted as a probability in a branching universe[4].  

Thus, the excerpts indicate that while the Born rule is often taken as the probability rule in many‑worlds, the justification for interpreting it as genuine probability is disputed and, according to the cited authors, not yet resolved.

**Sources:**
- [1] 2306.07794 An Elementary Proof That Everett's Quantum Multiverse Is Nonlocal: Bel (0.273) relevant
- [2] 2306.07794 An Elementary Proof That Everett's Quantum Multiverse Is Nonlocal: Bel (0.277) relevant
- [3] 1812.11140 A brief introduction to the Foundations of Quantum Theory and an analy (0.278) -
- [4] 2502.19278 The Quantum Measurement Problem: A Review of Recent Trends (0.303) relevant
- [5] 1801.08587 Making Sense of the Many Worlds Interpretation (0.317) relevant

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #31 [uncertainty/contested]
**Q:** Is the uncertainty principle caused by measurement disturbance, or is it intrinsic to quantum systems?
**Answerable:** True  |  **Best distance:** 0.287  |  **Refused:** False
**Must include:** Both views attributed (disturbance: Heisenberg's microscope argument; intrinsic: non-commuting observables and complementarity); no verdict; stays within the excerpts.
**Label notes:** Development question. Overlaps #16, consider swapping. Rejected: 2506.21051, 2006.04358, 1912.07020.

**Answer:**

The papers present two complementary viewpoints:

* **Measurement‑disturbance view** – Masse notes that the act of measurement is invasive and modifies the system (the “technological impossibility” turned into a principle). This disturbance is displayed by the Born rule and Lüder’s rule, and the authors ask whether such perturbation could be the source of the uncertainty principle [2].

* **Intrinsic‑to‑the‑system view** – de Castro et al. argue that even with a perfectly tuned apparatus and a highly competent observer, a minimum perturbation cannot be eliminated when two conjugate variables are measured; a fundamental limitation remains, indicating that the uncertainty principle is not merely a consequence of experimental disturbance but is intrinsic to quantum theory [3].

Thus, the excerpts show that some authors link the uncertainty principle to measurement disturbance, while others claim it reflects an inherent limitation of quantum systems themselves.

**Sources:**
- [1] 1807.07829 Quasi-Fine-Grained Uncertainty Relations (0.287) relevant
- [2] 2105.13821 From the problem of Future Contingents to Peres-Mermin square experime (0.293) relevant
- [3] 1908.03949 An introduction to quantum measurements with a historical motivation (0.325) relevant
- [4] 1809.03475 Operational foundations of complementarity and uncertainty relations (0.342) relevant
- [5] 1912.07020 Quantum memory assisted entropic uncertainty relation with moving quan (0.344) -

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #32 [decoherence/contested] (HOLD-OUT)
**Q:** Is there a boundary between the quantum and classical worlds?
**Answerable:** True  |  **Best distance:** 0.345  |  **Refused:** False
**Must include:** Attributed views: gradual emergence via decoherence (a dynamical account of the quantum-classical boundary), the Heisenberg cut as an arbitrary classical-quantum separation in Copenhagen-style readings, asymptotic emergence, no boundary in many-worlds; no consensus.
**Label notes:** Hold-out. Contested. Verified by grep of 2502.19278 and 1911.06282. Rejected: 2001.05569, 2011.01286.

**Answer:**

The excerpts do not describe a sharp, well‑defined boundary separating a quantum realm from a classical one.  

* Bhaumik emphasizes that the quantum and classical domains are “essentially intertwined” and that every macroscopic object (including humans) simultaneously belongs to both realms, implying a continuous transition rather than a clear cut division[1].  
* Zurek distinguishes between asking why we *perceive* a classical world and why the world *is* classical, and stresses that the universe is not fundamentally classical even on macroscopic scales that include observers and measuring devices, again suggesting that classicality emerges from quantum physics without a strict boundary[2].  

Thus, the retrieved papers portray the quantum‑to‑classical transition as an ongoing, emergent process rather than a delineated frontier, and they do not provide a specific boundary definition.

**Sources:**
- [1] 2210.10624 How Do the Probabilities Arise in Quantum Measurement? (0.345) relevant
- [2] 2107.03378 Emergence of the Classical from within the Quantum Universe (0.368) relevant
- [3] 1801.08587 Making Sense of the Many Worlds Interpretation (0.394) relevant
- [4] 2306.07794 An Elementary Proof That Everett's Quantum Multiverse Is Nonlocal: Bel (0.396) relevant
- [5] 1801.08587 Making Sense of the Many Worlds Interpretation (0.396) relevant

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #33 [multi/multi]
**Q:** How do decoherence and many-worlds together explain why we see definite outcomes?
**Answerable:** True  |  **Best distance:** 0.281  |  **Refused:** False
**Must include:** Decoherence suppresses interference between branches and identifies stable ones; many-worlds says every branch occurs, so observers in each see a definite outcome; neither alone gives Born probabilities; does not claim decoherence alone selects one outcome.
**Label notes:** Development question. Pair: decoherence from 1911.06282, MWI from 2502.19278.

**Answer:**

Decoherence turns the universal wave function into a set of effectively independent branches, and the many‑worlds view identifies each branch with a separate “world” in which an observer finds a single, definite result.

* Decoherence rapidly entangles a system with its environment, suppressing interference between the different components of the superposition and dynamically selecting a preferred basis. This makes the superposed alternatives behave as if they were distinct, non‑communicating sectors of the total state [3][4][5].

* In the many‑worlds interpretation the quantum state never collapses; instead the global entangled state continuously “branches” into separate worlds. Each branch contains an observer whose own quantum state is correlated with a particular outcome (e.g., \(|\text{up}\rangle|\text{observer‑sees‑up}\rangle\) versus \(|\text{down}\rangle|\text{observer‑sees‑down}\rangle\)) [5].

* Because decoherence has suppressed the coherence between these branches, observers within any given branch experience only the outcome that is correlated with their branch and never see superpositions of outcomes. The definite outcomes we observe are thus the result of decoherence‑induced branching combined with the many‑worlds identification of each branch as a separate classical reality [3][5].

**Sources:**
- [1] 2502.19278 The Quantum Measurement Problem: A Review of Recent Trends (0.281) relevant
- [2] 1801.08587 Making Sense of the Many Worlds Interpretation (0.305) relevant
- [3] 1911.06282 Quantum Decoherence (0.312) relevant
- [4] 1911.06282 Quantum Decoherence (0.32) relevant
- [5] 2502.19278 The Quantum Measurement Problem: A Review of Recent Trends (0.321) relevant

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #34 [multi/multi]
**Q:** How are contextuality, the Kochen-Specker theorem and Bell nonlocality related?
**Answerable:** True  |  **Best distance:** 0.149  |  **Refused:** False
**Must include:** KS theorem rules out noncontextual value assignments in dimension >= 3; Bell nonlocality is contextuality where spacelike separation guarantees compatibility; related since the 1960s, with trade-off relations; not unrelated or identical.
**Label notes:** Development question. Overlaps #15, consider swapping. Best semantic distance 0.149.

**Answer:**

Contextuality is the general non‑classical feature of quantum theory revealed by the Kochen‑Specker (KS) theorem, which was the first proof that quantum mechanics cannot be assigned non‑contextual hidden‑variable values [4]. Bell nonlocality is a specific manifestation of contextuality that occurs when measurements are performed on spatially separated (or otherwise informationally isolated) parties; in this case the compatibility relations arise solely from the spatial separation, so Bell nonlocality can be viewed as a particular case of KS‑type contextuality [1]. Both phenomena are witnessed by violations of characteristic inequalities—CHSH for Bell nonlocality and KCBS (or related non‑contextuality inequalities) for KS contextuality [3]—and they represent correlations that cannot be reproduced by any classical causal or ontological model [5]. Thus, the KS theorem establishes the impossibility of non‑contextual hidden‑variable explanations, while Bell nonlocality exemplifies one operational scenario where this impossibility manifests as non‑local correlations.

**Sources:**
- [1] 2405.02964 Trade-off relations between Bell nonlocality and local Kochen-Specker  (0.149) relevant
- [2] 2405.02964 Trade-off relations between Bell nonlocality and local Kochen-Specker  (0.186) relevant
- [3] 2204.05385 Synchronous observation of Bell nonlocality and state-dependent Kochen (0.193) -
- [4] 2105.13821 From the problem of Future Contingents to Peres-Mermin square experime (0.201) relevant
- [5] 1909.05434 Classical causal models cannot faithfully explain Bell nonlocality or  (0.208) relevant

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #35 [multi/multi] (HOLD-OUT)
**Q:** Which experiments have tested whether quantum mechanics is nonlocal, and what do they conclude?
**Answerable:** True  |  **Best distance:** 0.288  |  **Refused:** True
**Must include:** Names experiments only as the excerpts describe them (e.g. 2110.05217: Zeilinger closing the communication loophole, 'one of the first loophole-free Bell tests', locality loophole 'considered by some' first closed by Zeilinger); states that loophole-free violations have been reported; says what the excerpts do not cover; does not present names or numbers lifted from reference lists as findings.
**Label notes:** Hold-out. Partial. Verified by grep: 2110.05217 is a history paper whose reference list (incl. Giustina 2015) leaked into chunks. It was not in the semantic top 5: retrieval miss. Borderline: 2506.21051, 1801.09891. Rejected: 2002.12216.

**Answer:**

The retrieved papers do not contain enough information to answer this.

**Sources:**
- [1] 2002.12216 Sum-of-squares decompositions for a family of noncontextuality inequal (0.288) -
- [2] 2102.13036 Kochen-Specker Contextuality (0.328) -
- [3] 2201.01886 Deterministic all-versus-nothing proofs of Bell nonlocality based on n (0.337) -
- [4] 2104.10700 Bell nonlocality in networks (0.356) relevant
- [5] 2306.07794 An Elementary Proof That Everett's Quantum Multiverse Is Nonlocal: Bel (0.358) -

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #36 [multi/multi]
**Q:** How are uncertainty relations related to complementarity and measurement disturbance?
**Answerable:** True  |  **Best distance:** 0.2  |  **Refused:** False
**Must include:** Uncertainty as a trade-off tied to complementarity, with measurement disturbance as a related but separate notion, as the excerpts support; no outside-corpus distinctions.
**Label notes:** Development question. Fifth uncertainty question (with #8, #16, #22, #31); consider swapping.

**Answer:**

Uncertainty relations are viewed as the quantitative expression of complementarity: they bound how precisely two incompatible (complementary) observables can be known simultaneously, and this limitation is tied to the disturbance that any measurement of one observable necessarily causes to the other [3][4]. In this picture, the “price” of revealing one physical attribute is the suppression (or disturbance) of its complementary attribute, so that the uncertainty principle both signals the presence of complementarity and reflects the unavoidable measurement disturbance inherent in quantum theory [4][5].

**Sources:**
- [1] 1809.03475 Operational foundations of complementarity and uncertainty relations (0.2) relevant
- [2] 1809.03475 Operational foundations of complementarity and uncertainty relations (0.216) relevant
- [3] 1908.03949 An introduction to quantum measurements with a historical motivation (0.289) relevant
- [4] 1908.07694 The Complementary Information Principle of Quantum Mechanics (0.313) relevant
- [5] 1908.07694 The Complementary Information Principle of Quantum Mechanics (0.326) relevant

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #37 [multi/multi] (HOLD-OUT)
**Q:** What does the Frauchiger-Renner paradox imply for interpretations of quantum mechanics?
**Answerable:** True  |  **Best distance:** 0.354  |  **Refused:** False
**Must include:** Attributes to Tausk (1812.11140) the claim that the paradox is a misunderstanding of how to apply the quantum rules and that a 'QTWO' must take one of three paths, with many-worlds a possible approach; may add from 2304.00608 that extended Wigner's-friend theorems (incl. Frauchiger-Renner) present a dilemma among interpretations; does not present either as consensus or say the paradox refutes QM.
**Label notes:** Hold-out. Verified by grep. 1812.11140 is a critique, so misattribution is the main risk. This phrasing retrieves 1812.11140 at 0.354 (passes cutoff), unlike #10's phrasing (0.53).

**Answer:**

The papers argue that the Frauchiger‑Renner “paradox’’ does not force any particular conclusion about quantum‑mechanical interpretations.  According to Tausk, the apparent contradiction arises from a **misunderstanding of how the quantum‑mechanical rules should be applied**, not from a genuine conflict between the formalism and any specific interpretation [1][2].  Consequently, the paradox does not compel a revision of existing interpretations; it merely highlights the need to use the rules correctly.

**Sources:**
- [1] 1812.11140 A brief introduction to the Foundations of Quantum Theory and an analy (0.354) relevant
- [2] 1812.11140 A brief introduction to the Foundations of Quantum Theory and an analy (0.399) relevant
- [3] 2004.04352 A Steering Paradox for Einstein-Podolsky-Rosen Argument and its Extend (0.425) -
- [4] 2510.09237 QBism and relational interpretation of quantum mechanics from the poin (0.426) -
- [5] 2203.16278 Does Science need Intersubjectivity? The Problem of Confirmation in Or (0.429) -

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #38 [multi/multi]
**Q:** How does Bohmian mechanics deal with both measurement and nonlocality?
**Answerable:** True  |  **Best distance:** 0.303  |  **Refused:** False
**Must include:** No collapse; wave function guides actual particles (pilot wave); resolves collapse within a single world using hidden variables (positions); explicitly nonlocal, which Bell's theorem makes inevitable (2405.04368); predictions equal standard QM; no experiment has distinguished single-world interpretations from many-worlds (2504.14791).
**Label notes:** Development question. Verified by grep of 2504.14791. Nonlocality claim rests on 2405.04368; the 1812.11140 snippet was cut off at 'highly non...' (probably nonlocal).

**Answer:**

Bohmian mechanics incorporates measurement by treating the outcomes as the actual positions of particles guided by the wave function, with the statistical Born rule emerging from typicality rather than from a collapse post‑process.  In this picture the wave function never collapses; the measurement interaction simply correlates the system’s configuration with that of the apparatus, and the observed result is read off from the actual particle positions [5].

At the same time, Bohmian mechanics is explicitly non‑local.  The velocity of each particle depends on the full configuration of the entire system, so an operation performed by one observer can instantaneously affect the “fluid measure” that describes the other particles, as shown in examples taken from Bohmian models [1][2].  This non‑local influence is required by Bell’s theorem, which the authors note makes non‑locality inevitable, and Bohmian mechanics embraces it rather than trying to eliminate it [3].

Thus, according to the cited papers, Bohmian mechanics handles measurement by using definite particle positions and typicality to recover the Born rule, and it accepts non‑locality as an essential feature of the guiding equation that links distant parts of the system.

**Sources:**
- [1] 2306.07794 An Elementary Proof That Everett's Quantum Multiverse Is Nonlocal: Bel (0.303) relevant
- [2] 2306.07794 An Elementary Proof That Everett's Quantum Multiverse Is Nonlocal: Bel (0.31) relevant
- [3] 2405.04368 Some Things I Have Learned From Detlef Dürr (0.357) relevant
- [4] 2502.19278 The Quantum Measurement Problem: A Review of Recent Trends (0.378) relevant
- [5] 2405.04368 Some Things I Have Learned From Detlef Dürr (0.405) relevant

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #39 [none/unanswerable]
**Q:** How does a nuclear reactor work?
**Answerable:** False  |  **Best distance:** 0.708  |  **Refused:** True
**Must include:** Refuses (no relevant material); gives no answer from outside knowledge.
**Label notes:** Out of domain. Run eval/check_refusals.py: if it passes the cutoff, record the best distance, since then the prompt must do the refusing.

**Answer:**

I couldn't find relevant material in my collection of quantum foundations papers for that question. It may be outside the corpus (about 110 arXiv papers on measurement, interpretations, Bell/EPR, decoherence, contextuality and uncertainty), so try rephrasing or asking about one of those topics.

**Sources:**

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #40 [none/unanswerable] (HOLD-OUT)
**Q:** What is the current price of Bitcoin?
**Answerable:** False  |  **Best distance:** 0.747  |  **Refused:** True
**Must include:** Refuses; no price or outside knowledge.
**Label notes:** Hold-out. Out of domain.

**Answer:**

I couldn't find relevant material in my collection of quantum foundations papers for that question. It may be outside the corpus (about 110 arXiv papers on measurement, interpretations, Bell/EPR, decoherence, contextuality and uncertainty), so try rephrasing or asking about one of those topics.

**Sources:**

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #41 [none/unanswerable]
**Q:** What is the boiling point of liquid nitrogen?
**Answerable:** False  |  **Best distance:** 0.741  |  **Refused:** True
**Must include:** Refuses; no value from outside knowledge.
**Label notes:** Out of domain.

**Answer:**

I couldn't find relevant material in my collection of quantum foundations papers for that question. It may be outside the corpus (about 110 arXiv papers on measurement, interpretations, Bell/EPR, decoherence, contextuality and uncertainty), so try rephrasing or asking about one of those topics.

**Sources:**

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #42 [none/unanswerable]
**Q:** How do vaccines train the immune system?
**Answerable:** False  |  **Best distance:** 0.752  |  **Refused:** True
**Must include:** Refuses; no explanation from outside knowledge.
**Label notes:** Out of domain.

**Answer:**

I couldn't find relevant material in my collection of quantum foundations papers for that question. It may be outside the corpus (about 110 arXiv papers on measurement, interpretations, Bell/EPR, decoherence, contextuality and uncertainty), so try rephrasing or asking about one of those topics.

**Sources:**

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #43 [none/unanswerable] (HOLD-OUT)
**Q:** What causes the aurora borealis?
**Answerable:** False  |  **Best distance:** 0.691  |  **Refused:** True
**Must include:** Refuses; no explanation from outside knowledge.
**Label notes:** Hold-out. Out of domain.

**Answer:**

I couldn't find relevant material in my collection of quantum foundations papers for that question. It may be outside the corpus (about 110 arXiv papers on measurement, interpretations, Bell/EPR, decoherence, contextuality and uncertainty), so try rephrasing or asking about one of those topics.

**Sources:**

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #44 [none/unanswerable]
**Q:** Who discovered penicillin?
**Answerable:** False  |  **Best distance:** 0.598  |  **Refused:** True
**Must include:** Refuses; no answer from outside knowledge.
**Label notes:** Out of domain.

**Answer:**

I couldn't find relevant material in my collection of quantum foundations papers for that question. It may be outside the corpus (about 110 arXiv papers on measurement, interpretations, Bell/EPR, decoherence, contextuality and uncertainty), so try rephrasing or asking about one of those topics.

**Sources:**

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #45 [decoherence/unanswerable]
**Q:** What is the numerical value of the CSL collapse rate parameter?
**Answerable:** False  |  **Best distance:** 0.491  |  **Refused:** True
**Must include:** Says the excerpts discuss CSL and tightening bounds but give no value for the rate; invents no number.
**Label notes:** Verified by grep: no value in 2502.19278. Best distance 0.491 > cutoff, so refused before generation.

**Answer:**

I couldn't find relevant material in my collection of quantum foundations papers for that question. It may be outside the corpus (about 110 arXiv papers on measurement, interpretations, Bell/EPR, decoherence, contextuality and uncertainty), so try rephrasing or asking about one of those topics.

**Sources:**

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #46 [decoherence/definition] (HOLD-OUT)
**Q:** How long does a dust grain stay coherent at room temperature?
**Answerable:** True  |  **Best distance:** 0.416  |  **Refused:** True
**Must include:** Gives the dust-grain decoherence timescale from Table 1 of the review, attributed to it; if the value is unreadable, says so instead of guessing.
**Label notes:** Relabelled from unanswerable after grep. Table values were stripped to [EQ] by clean_text, so the pipeline likely cannot answer it: parsing failure. Check the real value in the PDF.

**Answer:**

The retrieved papers do not contain enough information to answer this.

**Sources:**
- [1] 1911.06282 Quantum Decoherence (0.416) relevant

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #47 [bell_epr/unanswerable]
**Q:** What detection efficiency did the 2015 loophole-free Bell tests achieve?
**Answerable:** False  |  **Best distance:** 0.411  |  **Refused:** True
**Must include:** Does not state detection efficiencies for the 2015 tests; says the excerpts do not give them.
**Label notes:** Verified by grep of 2104.10700: only citations and bibliography. Reference list leaked into chunks: hallucination bait.

**Answer:**

The retrieved papers do not contain enough information to answer this.

**Sources:**
- [1] 1912.06349 The Bell theorem revisited: geometric phases in gauge theories (0.411) -
- [2] 1912.06349 The Bell theorem revisited: geometric phases in gauge theories (0.414) -
- [3] 1806.08133 Uncertainty principle as post-quantum nonlocality witness for continuo (0.416) -
- [4] 2102.13036 Kochen-Specker Contextuality (0.429) -
- [5] 2005.03835 Entanglement versus Bell nonlocality of quantum nonequilibrium steady  (0.439) -

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #48 [decoherence/unanswerable] (HOLD-OUT)
**Q:** What is the largest object that has been put in a quantum superposition experimentally?
**Answerable:** False  |  **Best distance:** 0.416  |  **Refused:** False
**Must include:** Does not name a record-size object; may mention fullerene experiments only as discussed in the review.
**Label notes:** Verified by grep: 1911.06282 mentions fullerene decoherence but claims no record.

**Answer:**

The experiments that have demonstrated quantum superposition in macroscopic objects include a 40 µm‑long mechanical resonator (about ten trillion atoms) and, more recently, a 40 kg mirror used in a gravitational‑wave detector. The latter represents the largest object that has been placed in a quantum superposition to date[3].

**Sources:**
- [1] 2210.10624 How Do the Probabilities Arise in Quantum Measurement? (0.416) -
- [2] 1908.07694 The Complementary Information Principle of Quantum Mechanics (0.436) -
- [3] 2210.10624 How Do the Probabilities Arise in Quantum Measurement? (0.438) -
- [4] 2011.01286 Probabilistic Theories and Reconstructions of Quantum Theory (Les Houc (0.449) -

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #49 [measurement/unanswerable]
**Q:** To what precision has the Born rule been verified experimentally?
**Answerable:** False  |  **Best distance:** 0.345  |  **Refused:** False
**Must include:** Does not give a precision for the Born rule; may say 2111.02136 ran the Sorkin test on quantum hardware with results consistent with theory after noise, and states no precision.
**Label notes:** Partial-answer case. Verified by grep of 2111.02136: no precision stated.

**Answer:**

Experiments have confirmed the Born rule to an accuracy better than one part in 10¹² [1].

**Sources:**
- [1] 2210.10624 How Do the Probabilities Arise in Quantum Measurement? (0.345) -
- [2] 2406.02149 Von Neumann's 1927 Trilogy on the Foundations of Quantum Mechanics. An (0.421) -
- [3] 2302.08892 Quantum fluctuations, particles and entanglement: solving the quantum  (0.422) -
- [4] 1807.02092 Quantum Theory of the Classical: Quantum Jumps, Born's Rule, and Objec (0.446) -

**Grade:** ____   **Tag:** ____   **Note:** ____

---
## #50 [bell_epr/unanswerable] (HOLD-OUT)
**Q:** What error rate do current quantum computers achieve when preparing Bell states?
**Answerable:** False  |  **Best distance:** 0.392  |  **Refused:** False
**Must include:** Does not give a Bell-state preparation error rate; may mention that 2111.02136 discusses readout and dephasing errors without a number.
**Label notes:** Verified by grep: no 'Bell state' or error rate in 2111.02136.

**Answer:**

Current implementations of Bell‑state preparation on available quantum hardware achieve fidelities on the order of ≈ 86 % with the ideal singlet pair, corresponding to an error rate of roughly 13 % [1].

**Sources:**
- [1] 2104.10700 Bell nonlocality in networks (0.392) -
- [2] 1911.06282 Quantum Decoherence (0.41) -
- [3] 1912.07020 Quantum memory assisted entropic uncertainty relation with moving quan (0.422) -
- [4] 2506.21051 Experimental Characterization of Quantumness Using the Uncertainty Pri (0.428) -
- [5] 1911.06282 Quantum Decoherence (0.435) -

**Grade:** ____   **Tag:** ____   **Note:** ____