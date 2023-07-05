import os


def pytest_addoption(parser):
    parser.addoption(
        "--lang",
        action="store",
        default="https://www.limango.pl/",
        help="Language for the test",
        choices=("pl", "de", "nl"),
    )


def pytest_configure(config):
    os.environ["lang"] = config.getoption('lang')
    os.environ["url"] = f"https://www.limango.{config.getoption('lang')}/"
