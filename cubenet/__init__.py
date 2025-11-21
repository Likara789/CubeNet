"""Minimal CubeNet prototype components.

This package provides a small, pure-numpy implementation of the CubeNet
building blocks described in ``Plan.md``: a 3D cube reactor, front/back
control gates, and a retry loop that negotiates confidence.
"""

from .cube import Cube
from .gates import BackGate, FrontGate
from .retry import RetryConfig, RetryResult, run_retry

__all__ = [
    "BackGate",
    "Cube",
    "FrontGate",
    "RetryConfig",
    "RetryResult",
    "run_retry",
]
