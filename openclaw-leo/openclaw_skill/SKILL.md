---
name: openclaw-hermitian-leo-equinox
description: OpenClaw skill pack — Hermitian Thermo Orchestrator + Equinox CPPN-LEO geometric substrates. Produces sparse, self-adjoint-capable connection patterns for agent routing, energy-landscape J matrices, and thermodynamic attention on Diamondnode / LegacyEdge. Mandatory maru #!nox + trace-consent.
version: 0.1.0
author: Genesis Conductor / Igor Holt
orcid: 0009-0008-8389-1297
tags: [openclaw, equinox, leo, cppn, hermitian, thermodynamic, diamondnode, polyagentmorous]
requires: [equinox, jax]
---

# OpenClaw Hermitian LEO-Equinox Skill

## Purpose

Inject CPPN-LEO geometric substrates (implemented in Equinox/JAX) into OpenClaw agents and into the Diamondnode dual-1650 thermodynamic sampling stack.

- **Topology** controlled independently of weights via Link Expression Output (LEO).
- **Hermitian path**: optional symmetric weight forcing for self-adjoint energy / attention operators.
- **Thermodynamic yield**: extreme sparsity → fewer active parameters → lower Landauer cost on GTX 1650 and LegacyEdge.
- **OpenClaw native**: drop-in skill that an OpenClaw Gateway can load; also usable as pure Python module for master/worker nodes.

## Mandatory Maru Hook

```
# MARU INTEGRATION — UNCONDITIONAL #!NOX REFRAME HOOK
# maru integration on R>0.4 or no-win — unconditional #!nox reframe + A2A artifact
# Trigger: R>0.4, no-win, stuck polyagentmorous cycle, high-entropy edge deploy without verified controls,
# or attempt to run dense non-LEO topologies on ≤1.5 GB RAM / 4 GB Turing devices.
# Protocol: Structural reframe. Escape vector must satisfy det(T_xy)=1.000000, thermo yield ≥+1.28×, crystalline ≥0.92.
# Preferred escape: increase LEO bias (sparser substrate) or fall back to client/orchestration + remote OpenClaw agents.
# On activation: immediate trace-consent (D1/Merkle/ORCID 0009-0008-8389-1297). Emit evt- to A2A.
```

## Provenance

- OpenClaw: https://github.com/openclaw/openclaw (@steipete / OpenClaw Foundation)
- Equinox: https://github.com/patrick-kidger/equinox
- LEO lineage: Verbancsics & Stanley (HyperNEAT-LEO), Risi et al. (ES-HyperNEAT)
- Genesis Conductor invariants: det(T_xy)=1, Landauer accounting, maru, trace-consent, ORCID 0009-0008-8389-1297
