"""Two pulse trains: simulation, analysis, and optional plots."""

import numpy as np
from sigint_examples.simulation import generate_two_pulse_train
from sigint_examples.processing import autocorr_two_pulses, estimate_fundamentals
from sigint_examples.plotting import plot_two_pulse_autocorr

def run(show_plots=False):
    """Run the simulation and return analysis results; optionally display plots."""
    fs = 1_000_000  # Sampling rate (Hz)
    duration = 0.005
    PRI1, pulse_width1 = (100e-6, 5e-6)
    PRI2, pulse_width2 = (150e-6, 8e-6)
    t, rx, rx1, rx2 = generate_two_pulse_train(fs, duration, PRI1, pulse_width1, PRI2, pulse_width2)
    positive_lags, auto_positive = autocorr_two_pulses(rx, fs)
    fundamentals = estimate_fundamentals(positive_lags, auto_positive)
    PRI_est_us = fundamentals
    if show_plots:
        plot_two_pulse_autocorr(positive_lags, auto_positive, fundamentals)
    return {
        'PRI1': PRI1,
        'PRI2': PRI2,
        'PRI_est_us': PRI_est_us,
        'auto_positive': auto_positive,
        'duration': duration,
        'fs': fs,
        'fundamentals': fundamentals,
        'positive_lags': positive_lags,
        't': t,
    }
