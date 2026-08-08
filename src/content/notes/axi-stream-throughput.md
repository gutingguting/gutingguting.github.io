---
title: "Reasoning About AXI-Stream Throughput"
summary: "A compact way to relate bus width, clock rate, valid-ready occupancy, and packet overhead."
category: "DAQ"
tags: ["AXI-Stream", "Throughput", "Backpressure"]
published: 2026-01-08
readingTime: "6 min read"
featured: true
placeholder: true
---

## Start with accepted transfers

An AXI-Stream beat transfers only when both `TVALID` and `TREADY` are asserted. Peak payload rate therefore does not describe a stream that experiences bubbles or backpressure.

## A simple model

For bus width $W$, clock frequency $f$, and accepted-beat fraction $\eta$, an idealized transfer rate is

$$R = W f \eta.$$

Packet headers, trailers, partial final beats, and protocol gaps reduce payload efficiency further.

## Measure the contract

Count offered beats, accepted beats, packet boundaries, and stall duration in the clock domain where the handshake occurs.
