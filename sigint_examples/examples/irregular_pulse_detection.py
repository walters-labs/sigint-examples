"""Irregular pulse detection: simulation, analysis, and optional plots."""

import numpy as np
from sigint_examples.simulation import generate_irregular_pulses
from sigint_examples.processing import matched_filter, autocorrelation, estimate_PRI_from_mf
from sigint_examples.plotting import plot_time_domain, plot_autocorr, plot_histogram

def run(show_plots=False):
    """Run the simulation and return analysis results; optionally display plots."""
    t, signal, pulse_times = generate_irregular_pulses()
    if show_plots:
        plot_time_domain(t, signal, 'Irregular Pulse Train')
    mf_output = matched_filter(signal, pulse_width=5e-06, fs=1000000.0)
    if show_plots:
        plot_time_domain(t, mf_output, 'Matched Filter Output')
    auto, lags = autocorrelation(signal)
    lags = lags / 1_000_000  # Convert sample lags to seconds
    if show_plots:
        plot_autocorr(lags, auto, 'Autocorrelation')
    mean_PRI, std_PRI, peak_times, estimated_PRIs = estimate_PRI_from_mf(mf_output, t)
    if show_plots:
        plot_histogram(estimated_PRIs, title='Histogram of Estimated PRIs')
    return {
        'auto': auto,
        'mean_PRI': mean_PRI,
        'mf_output': mf_output,
        'peak_times': peak_times,
        'pulse_times': pulse_times,
        'signal': signal,
        'std_PRI': std_PRI,
        't': t,
    }
