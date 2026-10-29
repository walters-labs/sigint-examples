"""Discover and run the packaged examples without a test runner."""

import argparse
from importlib import import_module


EXAMPLES = {
    "basic": ("basic_workflow", "Carrier-modulated pulse train and PRI estimation"),
    "amplitude-modulation": ("examples.amplitude_modulation", "Pulses with varying amplitudes"),
    "chirped-pulses": ("examples.chirped_pulse_detection", "Matched filtering of linear chirps"),
    "irregular-pulses": ("examples.irregular_pulse_detection", "Pulse timing with uniform jitter"),
    "gaussian-jitter": ("examples.gaussian_jittered", "Pulse timing with Gaussian jitter"),
    "multi-emitter-jitter": ("examples.multi_emitter_noisy_jitter", "Two emitters with noise and timing jitter"),
    "noisy-multi-emitter": ("examples.noisy_multi_emitter", "Two fixed-PRI emitters in noise"),
    "tdoa": ("examples.time_difference_of_arrival", "Delay estimation between two receivers"),
    "two-pulse-trains": ("examples.two_pulse_trains", "Separate repetition intervals of two pulse trains"),
}


def print_summary(result):
    """Report time estimates in microseconds; emitter estimates already use µs."""
    for key, label in (
        ("PRI_estimate", "Estimated PRI"),
        ("mean_PRI", "Mean PRI"),
        ("std_PRI", "PRI standard deviation"),
        ("mean_PRI_clean", "Mean PRI (outliers removed)"),
        ("std_PRI_clean", "PRI standard deviation (outliers removed)"),
        ("pulse_width_estimate", "Estimated pulse width"),
    ):
        value = result.get(key)
        if value is not None:
            print(f"{label}: {value * 1e6:.2f} µs")
    if "fundamentals" in result:
        values = ", ".join(f"{value:.2f}" for value in result["fundamentals"])
        print(f"Estimated fundamental PRIs: {values or 'none detected'} µs")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Explore SIGINT simulations and analysis.")
    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("list", help="List available examples")
    run_parser = subparsers.add_parser("run", help="Run an example and print its estimates")
    run_parser.add_argument("example", choices=EXAMPLES)
    run_parser.add_argument("--show-plots", action="store_true", help="Open interactive Matplotlib plots")
    args = parser.parse_args(argv)
    if args.command is None:
        parser.print_help()
    elif args.command == "list":
        for name, (_, description) in EXAMPLES.items():
            print(f"{name:24} {description}")
    else:
        module, description = EXAMPLES[args.example]
        print(description)
        run = import_module(f"sigint_examples.{module}").run
        result = run(show_plots=args.show_plots)
        if result is not None:
            print_summary(result)
    return 0
