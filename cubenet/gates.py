"""Front and back gates for CubeNet."""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Tuple

from .cube import Grid, zero_grid


@dataclass
class FrontGate:
    """Front gates GateA and GateB with a small internal slap dynamic."""

    micro_iters: int = 4
    leak: float = 0.05
    feedback_gain: float = 0.3
    cube_size: int = 9

    def __post_init__(self) -> None:
        self.state = [0.0, 0.0]

    def prime(self, signal: float) -> Grid:
        """Run A↔B micro-updates to shape the injection packet."""

        self.state[0] = (1.0 - self.leak) * self.state[0] + signal
        self.state[1] = (1.0 - self.leak) * self.state[1] - signal * 0.1

        for _ in range(self.micro_iters):
            delta = 0.5 * (self.state[1] - self.state[0])
            self.state[0] += delta
            self.state[1] -= delta
            self.state[0] *= 1.0 - self.leak
            self.state[1] *= 1.0 - self.leak

        injection = zero_grid(self.cube_size)
        center = self.cube_size // 2
        injection[0][center][center] = self.state[0]
        for y in range(center - 1, center + 2):
            for z in range(center - 1, center + 2):
                injection[0][y][z] += 0.25 * self.state[1]
        return injection

    def apply_feedback(self, feedback: Tuple[float, float]) -> None:
        fb_a, fb_b = feedback
        self.state[0] += self.feedback_gain * fb_a
        self.state[1] += self.feedback_gain * fb_b


@dataclass
class BackGate:
    """Back gates GateC and GateD for compression and confidence."""

    confidence_floor: float = 0.1

    def compress(self, state: Grid) -> tuple[float, float]:
        mean_activation = _mean(state)
        edge_activation = _mean(_edges(state))
        return (mean_activation, edge_activation)

    def confidence(self, compressed: tuple[float, float]) -> float:
        energy = math.sqrt(compressed[0] ** 2 + compressed[1] ** 2)
        margin = compressed[1] - compressed[0]
        return max(self.confidence_floor, math.tanh(energy + 0.5 * margin))

    def feedback(self, compressed: tuple[float, float], target_confidence: float) -> Tuple[float, float]:
        current_conf = self.confidence(compressed)
        error = target_confidence - current_conf
        return error * 0.6, error * -0.4


def _mean(values: list[float] | list[list[float]] | Grid) -> float:
    if not values:
        return 0.0
    if isinstance(values[0], list):
        flat = []
        for item in values:  # type: ignore[arg-type]
            flat.append(_mean(item))
        return sum(flat) / len(flat)
    return float(sum(values) / len(values))  # type: ignore[arg-type]


def _edges(state: Grid) -> list[float]:
    size = len(state)
    result: list[float] = []
    for x in range(size):
        for y in range(size):
            for z in range(size):
                if x in (0, size - 1) or y in (0, size - 1) or z in (0, size - 1):
                    result.append(state[x][y][z])
    return result
