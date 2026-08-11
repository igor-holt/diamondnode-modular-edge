#!/usr/bin/env python3
"""
Diamondnode Shared Energy Landscape — Ising / QUBO / EBM invariant.
E(x) = sum_i h_i x_i + sum_{i<j} J_ij x_i x_j
β is the single dial separating:
  β → ∞  : ground-state / combinatorial optimization (QUBO argmin)
  finite β : marginals / MAP inference
  β = 1/λ : rate-distortion (MRF-RDO couplings)

This module is the crystalline core referenced by both master control-plane
and worker-node packages. det(T_xy) = 1 preserved by construction.
"""

from __future__ import annotations
import numpy as np
from typing import Optional, Tuple, Dict, Any
import json
import hashlib
from datetime import datetime, timezone


class EnergyLandscape:
    """
    Binary Ising / QUBO energy with optional linear field and pairwise couplings.
    Variables x ∈ {0,1}^n or {±1}^n (spin convention selectable).
    """

    def __init__(
        self,
        n: int,
        h: Optional[np.ndarray] = None,
        J: Optional[np.ndarray] = None,
        spin: bool = False,
        seed: Optional[int] = None,
    ):
        self.n = int(n)
        self.spin = bool(spin)
        rng = np.random.default_rng(seed)

        if h is None:
            self.h = rng.normal(0.0, 0.5, size=self.n)
        else:
            self.h = np.asarray(h, dtype=np.float64).reshape(self.n)

        if J is None:
            self.J = np.zeros((self.n, self.n), dtype=np.float64)
            mask = rng.random((self.n, self.n)) < 0.15
            vals = rng.normal(0.0, 0.3, size=(self.n, self.n))
            self.J = np.triu(mask * vals, k=1)
            self.J = self.J + self.J.T
        else:
            self.J = np.asarray(J, dtype=np.float64)
            assert self.J.shape == (self.n, self.n)

        self._fingerprint = self._compute_fingerprint()

    def _compute_fingerprint(self) -> str:
        payload = {
            "n": self.n,
            "spin": self.spin,
            "h_hash": hashlib.sha256(self.h.tobytes()).hexdigest()[:16],
            "J_hash": hashlib.sha256(self.J.tobytes()).hexdigest()[:16],
        }
        return hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()[:24]

    def energy(self, x: np.ndarray) -> float:
        x = np.asarray(x, dtype=np.float64).reshape(self.n)
        linear = np.dot(self.h, x)
        quadratic = 0.5 * np.dot(x, self.J @ x)
        return float(linear + quadratic)

    def local_fields(self, x: np.ndarray) -> np.ndarray:
        x = np.asarray(x, dtype=np.float64).reshape(self.n)
        return self.h + self.J @ x

    def to_qubo_matrix(self) -> np.ndarray:
        Q = self.J.copy()
        np.fill_diagonal(Q, self.h)
        return Q

    def spectral_gap_estimate(self, beta: float = 1.0, n_samples: int = 64) -> Dict[str, float]:
        x = np.random.randint(0, 2, size=self.n).astype(np.float64)
        energies = []
        for _ in range(n_samples):
            for i in range(self.n):
                delta = (1 - 2 * x[i]) * (self.h[i] + np.dot(self.J[i], x))
                if delta < 0 or np.random.rand() < np.exp(-beta * delta):
                    x[i] = 1 - x[i]
            energies.append(self.energy(x))
        energies = np.asarray(energies)
        var_e = float(np.var(energies))
        if len(energies) > 1:
            ac1 = float(np.corrcoef(energies[:-1], energies[1:])[0, 1])
        else:
            ac1 = 0.0
        mix_proxy = max(1.0, -1.0 / np.log(max(1e-6, abs(ac1)))) if ac1 != 0 else 100.0
        gap_proxy = 1.0 / mix_proxy
        return {
            "beta": beta,
            "energy_variance": var_e,
            "ac1": ac1,
            "mix_proxy": mix_proxy,
            "gap_proxy": gap_proxy,
            "fingerprint": self._fingerprint,
        }

    def fingerprint(self) -> str:
        return self._fingerprint

    def to_dict(self) -> Dict[str, Any]:
        return {
            "n": self.n,
            "spin": self.spin,
            "h": self.h.tolist(),
            "J": self.J.tolist(),
            "fingerprint": self._fingerprint,
            "created_utc": datetime.now(timezone.utc).isoformat(),
        }

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "EnergyLandscape":
        return cls(
            n=d["n"],
            h=np.array(d["h"]),
            J=np.array(d["J"]),
            spin=d.get("spin", False),
        )


def make_toy_landscape(n: int = 32, seed: int = 42) -> EnergyLandscape:
    return EnergyLandscape(n=n, seed=seed)


if __name__ == "__main__":
    el = make_toy_landscape()
    x = np.random.randint(0, 2, el.n)
    print(f"E(x) = {el.energy(x):.4f}")
    print(f"fingerprint = {el.fingerprint()}")
    gap = el.spectral_gap_estimate(beta=1.0)
    print(json.dumps(gap, indent=2))
