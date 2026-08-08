---
title: "Understanding FPGA Recovered Clocks"
summary: "A short conceptual map from serial transitions to a recovered parallel-domain clock."
category: "High-Speed Links"
tags: ["CDR", "Transceiver", "Clocking"]
published: 2026-01-10
readingTime: "4 min read"
featured: true
placeholder: true
---

## What is recovered?

A clock-data recovery loop estimates sampling timing from transitions in a serial stream. The recovered timing then feeds device-specific divider and distribution stages before it becomes visible in the FPGA fabric.

## Why phase deserves its own definition

Link correctness describes decoded data. Phase characterization asks a different question: where does an observable recovered clock sit relative to a stated reference and edge convention?

## A useful checklist

- Name the observation point.
- State the reference edge and wrap interval.
- Separate CDR acquisition from downstream divider behavior.
- Record reset scope and configuration provenance.

This note is a placeholder and contains no device-specific result.
