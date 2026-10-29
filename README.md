# SIGINT
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
![basic-tests](https://github.com/jacksonwalters/SIGINT/actions/workflows/python-tests.yml/badge.svg)
![PyPI version](https://img.shields.io/pypi/v/sigint-examples?logo=pypi)

Explore signal intelligence techniques with runnable Python simulations. Each example generates a signal, analyzes it, and prints estimates. Add `--show-plots` to inspect the signals visually. No test runner is needed.

## Get started

Install this checkout in a virtual environment (includes NumPy, SciPy, and Matplotlib):

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
sigint list
sigint run basic --show-plots
```

On Windows, activate with `.venv\Scripts\activate` instead.

## Run examples

```bash
sigint run tdoa
sigint run gaussian-jitter --show-plots
sigint run two-pulse-trains --show-plots
```

Without `--show-plots`, examples print results and finish without opening windows. Interactive plots require a graphical desktop and a Matplotlib GUI backend; close each plot window to continue through the example.

| Example | What it demonstrates |
| --- | --- |
| `basic` | Carrier-modulated pulse train, matched filter, and pulse repetition interval (PRI) estimation |
| `amplitude-modulation` | Pulses with varying amplitudes and autocorrelation analysis |
| `chirped-pulses` | Matched filtering of linear chirps |
| `irregular-pulses` | Pulse timing with uniform jitter |
| `gaussian-jitter` | Gaussian timing jitter and PRI statistics with outlier removal |
| `multi-emitter-jitter` | Two emitters with noise and timing jitter |
| `noisy-multi-emitter` | Two fixed-PRI emitters in noise |
| `tdoa` | Time difference of arrival between two receivers |
| `two-pulse-trains` | Fundamental PRIs of two overlapping pulse trains |

You can also use `python -m sigint_examples` in place of `sigint`:

```bash
python -m sigint_examples list
python -m sigint_examples run chirped-pulses --show-plots
```

The original `sigint-workflow --show-plots` and `python -m sigint_examples.basic_workflow --show-plots` commands still work.

## Use from Python

The workflows live in `sigint_examples/examples/`, separate from their tests. For example:

```python
from sigint_examples.examples.gaussian_jittered import run

results = run(show_plots=False)
print(results["mean_PRI_clean"])  # seconds
```

Simulation parameters are defined near the start of each workflow. These are introductory estimators; noise, jitter, harmonics, and sample resolution can affect the estimates. Time estimates use seconds internally, except the multi-emitter `fundamentals` arrays, which use microseconds. CLI output labels its units.

## Development

Tests check the same workflows that the CLI runs:

```bash
python -m pip install -e '.[dev]'
python -m pytest
```

For optional visual debugging, use `python -m pytest --show-plots`. To exercise plotting on a headless machine, use `MPLBACKEND=Agg python -m pytest --show-plots`.
