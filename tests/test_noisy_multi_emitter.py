import numpy as np
from sigint_examples.examples.noisy_multi_emitter import run


def test_noisy_multi_emitter_workflow(show_plots):
    result = run(show_plots=show_plots)
    fundamentals = result['fundamentals']
    assert len(fundamentals) <= 2
    assert all((f > 0 for f in fundamentals))
