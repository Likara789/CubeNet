"""3D cube reactor for CubeNet, implemented with pure Python lists."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
import math
from typing import Iterable, List

Grid = List[List[List[float]]]


def zero_grid(size: int) -> Grid:
    return [[[0.0 for _ in range(size)] for _ in range(size)] for _ in range(size)]


def grid_shape(grid: Grid) -> tuple[int, int, int]:
    return len(grid), len(grid[0]), len(grid[0][0])


@dataclass
class Cube:
    """Simple 3D cube reservoir with additive neighbor mixing."""

    size: int = 9
    decay: float = 0.92
    spread: float = 0.05

    def __post_init__(self) -> None:
        if self.size < 3:
            raise ValueError("Cube size must be at least 3 to support neighbors")
        self._neighbor_offsets = self._build_neighbor_offsets()

    def zero_state(self) -> Grid:
        return zero_grid(self.size)

    def step(self, state: Grid, injection: Grid | float | None = None) -> Grid:
        expected_shape = (self.size, self.size, self.size)
        if grid_shape(state) != expected_shape:
            raise ValueError("state shape does not match cube dimensions")

        if injection is None:
            injection_grid = 0.0
        elif isinstance(injection, (int, float)):
            injection_grid = float(injection)
        else:
            if grid_shape(injection) != expected_shape:
                raise ValueError("injection shape does not match cube dimensions")
            injection_grid = injection

        neighbor_sum = self._neighbor_sum(state)
        return self._mix(state, neighbor_sum, injection_grid)

    def _mix(self, state: Grid, neighbor_sum: Grid, injection: Grid | float) -> Grid:
        result = zero_grid(self.size)
        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    inj_val = injection if isinstance(injection, float) else injection[x][y][z]
                    mixed = self.decay * state[x][y][z] + self.spread * neighbor_sum[x][y][z] + inj_val
                    result[x][y][z] = math.tanh(mixed)
        return result

    def _neighbor_sum(self, state: Grid) -> Grid:
        padded = zero_grid(self.size + 2)
        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    padded[x + 1][y + 1][z + 1] = state[x][y][z]

        total = zero_grid(self.size)
        for dx, dy, dz in self._neighbor_offsets:
            for x in range(self.size):
                for y in range(self.size):
                    for z in range(self.size):
                        total[x][y][z] += padded[x + 1 + dx][y + 1 + dy][z + 1 + dz]
        return total

    @staticmethod
    def _build_neighbor_offsets() -> list[tuple[int, int, int]]:
        offsets = []
        for dx, dy, dz in product((-1, 0, 1), repeat=3):
            if dx == dy == dz == 0:
                continue
            offsets.append((dx, dy, dz))
        return offsets
