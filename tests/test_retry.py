from cubenet import BackGate, Cube, FrontGate, RetryConfig, run_retry


def test_retry_completes_and_shapes():
    cube = Cube()
    front = FrontGate()
    back = BackGate()
    cfg = RetryConfig(max_retries=2, cube_ticks=2, confidence_threshold=0.5)

    result = run_retry(1.2, cube, front, back, cfg)

    assert len(result.final_state) == cube.size
    assert len(result.final_state[0]) == cube.size
    assert len(result.final_state[0][0]) == cube.size
    assert len(result.compressed) == 2
    assert 0.0 <= result.confidence <= 1.0
    assert 1 <= result.attempts <= cfg.max_retries + 1


def test_feedback_changes_gate_state():
    front = FrontGate()
    before = list(front.state)
    front.apply_feedback((0.5, -0.25))
    assert before != front.state
