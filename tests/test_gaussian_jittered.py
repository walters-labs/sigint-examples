import numpy as np
from sigint_examples.examples.gaussian_jittered import run


def test_gaussian_jittered_workflow(show_plots):
    result = run(show_plots=show_plots)
    base_PRI = result['base_PRI']
    estimated_PRIs_clean = result['estimated_PRIs_clean']
    mean_PRI_clean = result['mean_PRI_clean']
    pulse_times_detected = result['pulse_times_detected']
    std_PRI_clean = result['std_PRI_clean']
    assert len(pulse_times_detected) > 5
    assert np.all(pulse_times_detected > 0)
    assert estimated_PRIs_clean is not None
    assert abs(mean_PRI_clean - base_PRI) < 2e-05
    assert std_PRI_clean > 0
