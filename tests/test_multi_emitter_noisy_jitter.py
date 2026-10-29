import numpy as np
from sigint_examples.examples.multi_emitter_noisy_jitter import run


def test_multi_emitter_jitter_workflow(show_plots):
    result = run(show_plots=show_plots)
    fundamentals = result['fundamentals']
    peak_lags_us = result['peak_lags_us']
    pulse_times_list = result['pulse_times_list']
    rx = result['rx']
    t = result['t']
    assert rx.shape == t.shape
    assert len(pulse_times_list) == 2
    assert len(fundamentals) <= 2
    assert all((f > 0 for f in fundamentals))
    assert np.all(np.isfinite(peak_lags_us))
