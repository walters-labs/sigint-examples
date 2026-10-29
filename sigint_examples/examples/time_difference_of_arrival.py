"""Time difference of arrival: simulation, analysis, and optional plots."""

import numpy as np
from sigint_examples.simulation import generate_time_delay_pulses
from sigint_examples.processing import estimate_delay
import matplotlib.pyplot as plt

def run(show_plots=False):
    """Run the simulation and return analysis results; optionally display plots."""
    fs = 1_000_000  # Sampling rate (Hz)
    duration = 0.002
    pulse_width = 5e-06
    PRI = 100e-6
    true_delay = 1.5e-05
    SNR_dB = 0
    t, rx1, rx2 = generate_time_delay_pulses(fs, duration, pulse_width, PRI, delay=true_delay, SNR_dB=SNR_dB, seed=42)
    estimated_delay, lags, cross_corr = estimate_delay(rx1, rx2, fs)
    error = abs(estimated_delay - true_delay)
    print(f'True delay: {true_delay * 1000000.0:.2f} µs, Estimated delay: {estimated_delay * 1000000.0:.2f} µs, Error: {error * 1000000.0:.2f} µs')
    if show_plots:
        plt.figure()
        plt.subplot(2, 1, 1)
        plt.plot(t * 1000.0, rx1, label='Receiver 1')
        plt.plot(t * 1000.0, rx2, label='Receiver 2')
        plt.title('TDOA Signals')
        plt.xlabel('Time (ms)')
        plt.ylabel('Amplitude')
        plt.legend()
        plt.grid(True)
        plt.subplot(2, 1, 2)
        plt.plot(lags * 1000000.0, cross_corr)
        plt.axvline(estimated_delay * 1000000.0, color='r', linestyle='--', label='Estimated delay')
        plt.title('Cross-Correlation')
        plt.xlabel('Lag (µs)')
        plt.ylabel('Amplitude')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    return {
        'cross_corr': cross_corr,
        'duration': duration,
        'error': error,
        'fs': fs,
        'lags': lags,
        'rx1': rx1,
        'rx2': rx2,
        't': t,
    }
