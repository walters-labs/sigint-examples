import numpy as np
from sigint_examples.examples.two_pulse_trains import run


def test_two_pulse_trains_basic(show_plots):
    result = run(show_plots=show_plots)
    PRI1 = result['PRI1']
    PRI2 = result['PRI2']
    PRI_est_us = result['PRI_est_us']
    auto_positive = result['auto_positive']
    duration = result['duration']
    fs = result['fs']
    positive_lags = result['positive_lags']
    t = result['t']
    assert len(t) == int(duration * fs)
    assert len(positive_lags) == len(auto_positive)
    assert np.any(np.isclose(PRI_est_us, PRI1 * 1000000.0, atol=5.0))
    assert np.any(np.isclose(PRI_est_us, PRI2 * 1000000.0, atol=5.0))
    assert np.all(auto_positive > -1e-12)
