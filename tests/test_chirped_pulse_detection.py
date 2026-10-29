import numpy as np
from sigint_examples.examples.chirped_pulse_detection import run


def test_chirped_pulse_detection_workflow(show_plots):
    result = run(show_plots=show_plots)
    PRI = result['PRI']
    PRI_estimate = result['PRI_estimate']
    duration = result['duration']
    fs = result['fs']
    mf_output = result['mf_output']
    peak_indices = result['peak_indices']
    peak_times = result['peak_times']
    pulse_width = result['pulse_width']
    pulse_width_estimate = result['pulse_width_estimate']
    rx_signal = result['rx_signal']
    rx_signal_noisy = result['rx_signal_noisy']
    t = result['t']
    assert len(t) == int(duration * fs) + 1
    assert len(rx_signal) == len(t)
    assert len(peak_indices) > 0
    assert np.all(peak_times > 0)
    assert pulse_width_estimate is not None
    assert abs(pulse_width_estimate - pulse_width) < 5e-06
    assert len(mf_output) == len(rx_signal_noisy)
    assert PRI_estimate is not None
    assert abs(PRI_estimate - PRI) < 2e-05
