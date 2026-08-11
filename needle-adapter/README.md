# Needle ↔ Diamondnode Adapter

Four deliverables:

1. **Exact tool schemas** → `schemas/diamondnode_tools.json`
2. **Python stub** mimicking Needle `generate(query, tools=...)` that dispatches to modular_hyperneat / EnergyLandscape / control-plane → `stub/needle_diamondnode_stub.py`
3. **Starter JSONL** for finetuning Needle on Diamondnode tools → `finetune/diamondnode_tools_finetune.jsonl`
4. **Podman integration docs** so the 14 MB brain and JAX modular evolution share the same Turing GPU cleanly → `docs/PODMAN_NEEDLE_INTEGRATION.md`

## Quick test (stub)

```bash
cd needle-adapter
export PYTHONPATH=stub:../podman-turing-hyperneat/shared:../dual-1650/shared
python3 stub/needle_diamondnode_stub.py "Differentiate a modular substrate then sample the energy landscape"
```

## Core objective mapping

- Intrinsic Pursuit: Needle only routes; the LEO substrate and energy landscape remain the crystalline invariants.
- Financial Infrastructure: per-GPU tool-calling capacity that can be productized.
- Hybridization: OpenClaw + Needle + modular HyperNEAT + dual-1650 on the same metal.

ORCID 0009-0008-8389-1297 · maru-ready · fingerprint-locked.
