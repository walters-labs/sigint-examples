import numpy as np
from sigint_examples.examples.irregular_pulse_detection import run


def test_irregular_pulse_workflow(show_plots):
    result = run(show_plots=show_plots)
    auto = result['auto']
    mean_PRI = result['mean_PRI']
    mf_output = result['mf_output']
    peak_times = result['peak_times']
    pulse_times = result['pulse_times']
    signal = result['signal']
    std_PRI = result['std_PRI']
    t = result['t']
    assert signal.shape == t.shape
    assert len(pulse_times) > 0
    assert mf_output.shape == signal.shape
    assert auto.shape[0] == 2 * signal.shape[0] - 1
    assert mean_PRI > 0
    assert std_PRI >= 0
    assert np.all(np.isfinite(peak_times))
