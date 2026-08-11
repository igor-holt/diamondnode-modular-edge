# Diamondnode Modular Edge

**Genesis Conductor** dual-GTX-1650 edge stack for modular differentiation and thermodynamic sampling on consumer Turing GPUs.

## Packages

| Directory | Purpose |
|-----------|---------|
| `dual-1650/` | EnergyLandscape (Ising/QUBO/EBM) + Gibbs sampler + master control-plane watcher + worker node |
| `podman-turing-hyperneat/` | Podman Containerfile + Equinox CPPN-LEO + modular HyperNEAT evolution for modular differentiation |
| `openclaw-leo/` | OpenClaw Hermitian Thermo skill + Equinox CPPN-LEO geometric substrates |
| `needle-adapter/` | Needle-compatible tool schemas, generate() stub, finetune JSONL, Podman coexistence docs |

## Core invariants

- Single energy landscape \( E(x) = h \cdot x + x^T J x \); \(\beta\) is the only dial.
- LEO (Link Expression Output) separates topology from weights → modular differentiation.
- Hermitian symmetry option for self-adjoint energy/attention operators.
- Content fingerprints on every substrate and landscape.
- 14 MB Needle (or stub) as the tool-calling decision layer; JAX kernels stay heavy.
- Maru `# !nox` on R > 0.4; trace-consent / ORCID 0009-0008-8389-1297.

## Quick start (CPU validation)

```bash
# dual-1650 local test
cd dual-1650
export PYTHONPATH=shared
bash bootstrap_local_test.sh

# Needle stub
cd ../needle-adapter
export PYTHONPATH=stub:../podman-turing-hyperneat/shared:../dual-1650/shared
python3 stub/needle_diamondnode_stub.py "Differentiate a modular substrate then check the spectral gap"
```

## Operator path (second GTX 1650)

See `podman-turing-hyperneat/docs/MODULAR_DIFFERENTIATION.md` and `needle-adapter/docs/PODMAN_NEEDLE_INTEGRATION.md`.

## License & attribution

Genesis Conductor Protocol / MIT-compatible components.  
ORCID: 0009-0008-8389-1297  
Principal Investigator: Igor Holt, Kovach Enterprises / Genesis Conductor

---

*Truth is Structural.*
