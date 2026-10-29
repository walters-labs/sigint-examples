"""Multi emitter noisy jitter: simulation, analysis, and optional plots."""

import numpy as np
from sigint_examples.simulation import generate_multi_emitter_jittered_pulses
from sigint_examples.processing import autocorrelation, detect_fundamental_PRIs
from sigint_examples.plotting import plot_time_domain

def run(show_plots=False):
    """Run the simulation and return analysis results; optionally display plots."""
    emitters = [{'PRI': 0.0001, 'pulse_width': 5e-06, 'jitter': 5e-06, 'amplitude': 1.0}, {'PRI': 0.000159, 'pulse_width': 8e-06, 'jitter': 8e-06, 'amplitude': 0.7}]
    t, rx, pulse_times_list = generate_multi_emitter_jittered_pulses(duration=0.01, emitters=emitters)
    if show_plots:
        plot_time_domain(t, rx, title='Multi-Emitter Jittered Pulses')
    auto, lags = autocorrelation(rx)
    lags = lags / 1_000_000  # Convert sample lags to seconds
    mid = len(auto) // 2
    auto_pos = auto[mid + 1:]
    lags_pos = lags[mid + 1:]
    min_PRI = min([e['PRI'] for e in emitters])
    fundamentals, peak_lags_us, peaks = detect_fundamental_PRIs(auto_pos, lags_pos, N_emitters=2, min_PRI=min_PRI, smooth_signal=None)
    return {
        'fundamentals': fundamentals,
        'peak_lags_us': peak_lags_us,
        'pulse_times_list': pulse_times_list,
        'rx': rx,
        't': t,
    }
