"""Exercise the real public CLI, including packaged example discovery."""

import os
import subprocess
import sys

import pytest

from sigint_examples.cli import EXAMPLES


def invoke(*args):
    return subprocess.run(
        [sys.executable, "-m", "sigint_examples", *args],
        capture_output=True,
        text=True,
        env={**os.environ, "MPLBACKEND": "Agg"},
        timeout=30,
    )


def test_list():
    result = invoke("list")
    assert result.returncode == 0, result.stderr
    for name in EXAMPLES:
        assert name in result.stdout


@pytest.mark.parametrize("name", EXAMPLES)
def test_run_example(name):
    result = invoke("run", name)
    assert result.returncode == 0, result.stderr
    assert "µs" in result.stdout


def test_unknown_example():
    result = invoke("run", "does-not-exist")
    assert result.returncode == 2
    assert "invalid choice" in result.stderr


def test_help():
    result = invoke()
    assert result.returncode == 0
    assert "usage:" in result.stdout
