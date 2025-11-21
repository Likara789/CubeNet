# CubeNet

This repository documents and experiments with CubeNet, a 3D neural reactor
architecture built around chaotic signal propagation and gate-mediated retries.
See [Plan.md](Plan.md) for the conceptual outline and roadmap.

## Quick start

The minimal prototype is implemented with pure Python lists (no third-party
numerical dependencies). Run the sample pipeline:

```bash
python examples/simple_run.py
```

This constructs a cube, front/back gates, and runs the retry loop until the back
gate reports sufficient confidence.

## Tests

```bash
python -m pytest
```
