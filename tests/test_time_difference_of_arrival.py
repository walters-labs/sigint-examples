import numpy as np
from sigint_examples.examples.time_difference_of_arrival import run


def test_tdoa_basic(show_plots):
    result = run(show_plots=show_plots)
    cross_corr = result['cross_corr']
    duration = result['duration']
    error = result['error']
    fs = result['fs']
    lags = result['lags']
    rx1 = result['rx1']
    rx2 = result['rx2']
    t = result['t']
    assert len(t) == int(duration * fs) + 1
    assert np.mean(rx1 ** 2) > 0
    assert np.mean(rx2 ** 2) > 0
    assert error < 2e-06
    assert len(lags) == len(cross_corr)
    assert np.max(cross_corr) > 0
