"""Gaussian jittered: simulation, analysis, and optional plots."""

import numpy as np
from sigint_examples.simulation import generate_gaussian_jittered_pulses
from sigint_examples.processing import add_awgn, matched_filter_detect, estimate_PRI_statistics
from sigint_examples.plotting import plot_time_domain, plot_matched_filter, plot_PRI_histogram, plot_PRI_vs_time

def run(show_plots=False):
    """Run the simulation and return analysis results; optionally display plots."""
    fs = 1_000_000  # Sampling rate (Hz)
    duration = 0.01
    base_PRI = 100e-6
    pulse_width = 5e-06
    jitter_std = 5e-06
    SNR_dB = 0
    t, rx, pulse_times = generate_gaussian_jittered_pulses(fs, duration, base_PRI, pulse_width, jitter_std, seed=42)
    rx_noisy = add_awgn(rx, SNR_dB, seed=42)
    mf_output, t_valid, peaks, pulse_times_detected, threshold = matched_filter_detect(rx_noisy, pulse_width, fs, base_PRI, jitter_std)
    estimated_PRIs_clean, mean_PRI_clean, std_PRI_clean = estimate_PRI_statistics(pulse_times_detected)
    if show_plots:
        plot_time_domain(t, rx_noisy, detected_peaks=pulse_times_detected, zoom=(0, 0.005))
        plot_matched_filter(t_valid, mf_output, peaks, threshold, zoom_start=0, zoom_end=0.005)
        plot_PRI_histogram(estimated_PRIs_clean, base_PRI, mean_PRI_clean)
        plot_PRI_vs_time(pulse_times_detected, np.diff(pulse_times_detected), base_PRI, mean_PRI_clean, jitter_std, duration)
    return {
        'base_PRI': base_PRI,
        'estimated_PRIs_clean': estimated_PRIs_clean,
        'mean_PRI_clean': mean_PRI_clean,
        'pulse_times_detected': pulse_times_detected,
        'std_PRI_clean': std_PRI_clean,
    }
