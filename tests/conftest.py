import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--show-plots",
        action="store_true",
        default=False,
        help="Show plots during tests"
    )

@pytest.fixture
def show_plots(request):
    yield request.config.getoption("--show-plots")
    # Headless backends retain figures after show(); release them between tests.
    import matplotlib.pyplot as plt
    plt.close("all")
