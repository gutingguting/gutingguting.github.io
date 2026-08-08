---
title: "CDC for Detector Readout"
summary: "Choosing synchronization structures by signal meaning rather than by signal width alone."
category: "FPGA"
tags: ["CDC", "FIFO", "Reset"]
published: 2026-01-07
readingTime: "5 min read"
featured: false
placeholder: true
---

## The question is semantic

A single-bit level, a pulse, a counter, and a packet stream carry different meaning. They therefore need different clock-domain crossing structures.

## Common structures

- Synchronizer chains for stable single-bit levels.
- Toggle or handshake schemes for events.
- Gray-coded pointers for asynchronous FIFOs.
- Explicit protocols for multi-bit control snapshots.

## Reset is part of CDC

Reset assertion and release can create cross-domain behavior of their own. Verification should include startup, independent reset, backpressure, and recovery cases.
