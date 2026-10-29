import numpy as np
from sigint_examples.examples.amplitude_modulation import run


def test_amplitude_modulation_workflow(show_plots):
    result = run(show_plots=show_plots)
    PRI_estimate = result['PRI_estimate']
    auto = result['auto']
    left_idx = result['left_idx']
    mf_output = result['mf_output']
    peak_lags = result['peak_lags']
    pulse_times = result['pulse_times']
    pulse_width_estimate = result['pulse_width_estimate']
    right_idx = result['right_idx']
    signal = result['signal']
    t = result['t']
    zoom_auto = result['zoom_auto']
    assert signal.shape == t.shape
    assert len(pulse_times) > 0
    assert mf_output.shape == signal.shape
    assert auto.shape[0] == 2 * signal.shape[0] - 1
    assert PRI_estimate > 0
    assert np.all(np.isfinite(peak_lags))
    assert pulse_width_estimate > 0
    assert left_idx < right_idx < len(zoom_auto)
