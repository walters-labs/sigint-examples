"""Chirped pulse detection: simulation, analysis, and optional plots."""

import numpy as np
from sigint_examples.simulation import generate_chirped_train
from sigint_examples.processing import matched_filter_chirp, detect_peaks, estimate_pulse_widths, add_awgn, autocorrelation
from sigint_examples.plotting import plot_time_domain, plot_autocorr

def run(show_plots=False):
    """Run the simulation and return analysis results; optionally display plots."""
    fs = 1_000_000  # Sampling rate (Hz)
    duration = 0.002
    PRI = 100e-6
    pulse_width = 5e-06
    fc = 100000
    bandwidth = 50000
    SNR_dB = 0
    t, rx_signal, pulse_times = generate_chirped_train(fs, duration, PRI, pulse_width, fc, bandwidth)
    rx_signal_noisy = add_awgn(rx_signal, SNR_dB, seed=42)
    mf_output = matched_filter_chirp(rx_signal_noisy, pulse_width, fs, fc, bandwidth)
    peak_indices, peak_times, estimated_PRIs, PRI_estimate = detect_peaks(mf_output, t)
    pulse_width_estimate = estimate_pulse_widths(mf_output, t, peak_indices)
    if show_plots:
        plot_time_domain(t, rx_signal_noisy, title='Chirped Pulse Train in Noise', detected_peaks=peak_times, zoom=(0, 0.002))
        plot_time_domain(t, mf_output, title='Matched Filter Output', detected_peaks=peak_times, zoom=(0, 0.002))
        auto, lags = autocorrelation(rx_signal_noisy)
        lags = lags / fs
        plot_autocorr(lags, auto, title='Autocorrelation of Chirped Pulse Train')
    return {
        'PRI': PRI,
        'PRI_estimate': PRI_estimate,
        'duration': duration,
        'fs': fs,
        'mf_output': mf_output,
        'peak_indices': peak_indices,
        'peak_times': peak_times,
        'pulse_width': pulse_width,
        'pulse_width_estimate': pulse_width_estimate,
        'rx_signal': rx_signal,
        'rx_signal_noisy': rx_signal_noisy,
        't': t,
    }
