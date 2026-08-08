---
title: "Circular Statistics for Phase"
summary: "Why phase data needs wrapped differences and circular summaries near the boundary."
category: "Statistics"
tags: ["Phase", "Circular Statistics", "Measurement"]
published: 2026-01-06
readingTime: "6 min read"
featured: false
placeholder: true
---

## Linear averages can fail at the wrap

Angles just below and just above a wrap boundary are physically close but numerically far apart. An ordinary arithmetic mean can therefore be misleading.

## Mean direction

For phases $\phi_k$, define

$$
\bar{C}=\frac{1}{N}\sum_k\cos\phi_k,\qquad
\bar{S}=\frac{1}{N}\sum_k\sin\phi_k.
$$

The sample mean direction is $\operatorname{atan2}(\bar{S},\bar{C})$. The resultant length describes concentration but does not, by itself, establish a physical mechanism.

## Report the convention

Always state the phase unit, wrap interval, sign, reference, and preprocessing before comparing samples.
