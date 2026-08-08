---
title: "Recovered Clock Phase Uncertainty"
summary: "An experimental study framework for phase uncertainty mechanisms in FPGA high-speed transceiver recovered clocks."
status: "Ongoing"
topics: ["Clock Recovery", "CDR", "FPGA Transceiver", "Precision Timing"]
featured: true
---

## Research Question

Which mechanisms determine the phase state of a recovered clock after a defined intervention, and which parts of that behavior are repeatable under controlled conditions?

## Background

Clock recovery reconstructs timing from serial data. For precision-timing applications, correct data decoding is necessary but not sufficient: the recovered clock's phase relative to a reference may also matter.

## Physical Mechanisms

Candidate mechanisms include divider state, clock-distribution state, reset scope, loop acquisition, and measurement reference behavior. This list is a hypothesis space, not a result.

## Hypothesis

Different interventions may expose different phase-state sets. A valid test must keep acquisition and reference conditions fixed while changing only the intervention under study.

## Experimental Method

Each run should record configuration, firmware provenance, intervention sequence, environmental context, sample count, and instrument settings.

## Measurement Definition

For phases $\phi_1$ and $\phi_2$, the wrapped difference is

$$
\Delta\phi = \operatorname{atan2}(\sin(\phi_1-\phi_2),\cos(\phi_1-\phi_2)).
$$

The sign convention and reference edge must be stated before analysis.

## Statistical Method

Circular summaries, distribution comparison, and sensitivity to clustering assumptions are considered. Failure to reject a difference is not treated as proof of equivalence.

## Results

No unpublished numerical result is included in this public placeholder.

## Interpretation

Interpretation will distinguish observed distributions from claims about physical cause.

## Limitations

Instrument resolution, trigger behavior, finite samples, environmental drift, and hidden state can limit inference.

## Future Work

Future public work may add approved measurements, preregistered comparisons, and reproducible analysis definitions.

## Related Projects / Publications

See [High-Speed Link Phase Characterization](/projects/high-speed-link-phase/). Publication links remain pending confirmation.
