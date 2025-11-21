"""Retry loop orchestration for CubeNet."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .cube import Cube, Grid
from .gates import BackGate, FrontGate


@dataclass
class RetryConfig:
    max_retries: int = 3
    cube_ticks: int = 3
    confidence_threshold: float = 0.7


@dataclass
class RetryResult:
    attempts: int
    final_state: Grid
    compressed: tuple[float, float]
    confidence: float


def run_retry(
    input_signal: float,
    cube: Cube,
    front_gate: FrontGate,
    back_gate: BackGate,
    config: Optional[RetryConfig] = None,
) -> RetryResult:
    """Run the CubeNet retry loop for a single signal."""

    cfg = config or RetryConfig()
    state = cube.zero_state()
    compressed = (0.0, 0.0)
    confidence = cfg.confidence_threshold

    for attempt in range(cfg.max_retries + 1):
        injection = front_gate.prime(input_signal)
        for _ in range(cfg.cube_ticks):
            state = cube.step(state, injection)
            injection = 0.0

        compressed = back_gate.compress(state)
        confidence = back_gate.confidence(compressed)

        if confidence >= cfg.confidence_threshold:
            return RetryResult(attempts=attempt + 1, final_state=state, compressed=compressed, confidence=confidence)

        feedback = back_gate.feedback(compressed, cfg.confidence_threshold)
        front_gate.apply_feedback(feedback)

    return RetryResult(attempts=cfg.max_retries + 1, final_state=state, compressed=compressed, confidence=confidence)
