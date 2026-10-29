"""Amplitude modulation: simulation, analysis, and optional plots."""

import numpy as np
from sigint_examples.simulation import generate_amplitude_modulated_pulses
from sigint_examples.processing import matched_filter, autocorrelation, estimate_PRI_from_autocorr, estimate_pulse_width_from_autocorr
from sigint_examples.plotting import plot_time_domain, plot_autocorr, plot_histogram

def run(show_plots=False):
    """Run the simulation and return analysis results; optionally display plots."""
    t, signal, pulse_times = generate_amplitude_modulated_pulses()
    if show_plots:
        plot_time_domain(t, signal, title='Amplitude-Modulated Pulse Train')
    mf_output = matched_filter(signal, pulse_width=5e-06, fs=1000000.0)
    if show_plots:
        plot_time_domain(t, mf_output, title='Matched Filter Output')
    auto, lags = autocorrelation(signal)
    lags = lags / 1_000_000  # Convert sample lags to seconds
    if show_plots:
        plot_autocorr(lags, auto, title='Autocorrelation')
    PRI_estimate, peak_lags, auto_pos, lags_pos = estimate_PRI_from_autocorr(auto, lags)
    pulse_width_estimate, zoom_lags, zoom_auto, left_idx, right_idx = estimate_pulse_width_from_autocorr(auto, lags)
    if show_plots:
        plot_autocorr(zoom_lags, zoom_auto, title='Zoomed Autocorrelation for Pulse Width Estimation')
        plot_histogram(np.diff(peak_lags), title='Histogram of Estimated PRIs')
    return {
        'PRI_estimate': PRI_estimate,
        'auto': auto,
        'left_idx': left_idx,
        'mf_output': mf_output,
        'peak_lags': peak_lags,
        'pulse_times': pulse_times,
        'pulse_width_estimate': pulse_width_estimate,
        'right_idx': right_idx,
        'signal': signal,
        't': t,
        'zoom_auto': zoom_auto,
    }
