"""Minimal example of the CubeNet retry loop."""

from cubenet import BackGate, Cube, FrontGate, RetryConfig, run_retry


def main() -> None:
    cube = Cube()
    front = FrontGate()
    back = BackGate()
    cfg = RetryConfig(max_retries=3, cube_ticks=3, confidence_threshold=0.65)

    signal = 0.8
    result = run_retry(signal, cube, front, back, cfg)

    print(f"attempts: {result.attempts}")
    print(f"compressed: {result.compressed}")
    print(f"confidence: {result.confidence:.3f}")


if __name__ == "__main__":
    main()
