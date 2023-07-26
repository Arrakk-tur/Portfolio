import logging
import sys

from pytest import fixture
from reportportal_client import RPLogger
from playwright.sync_api import sync_playwright

from utilities.application import App


# Report Portal
@fixture(scope="session")
def rp_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logging.setLoggerClass(RPLogger)
    return logger


@fixture(scope='session')
def rp_launch_id(request):
    if hasattr(request.config, "py_test_service"):
        return request.config.py_test_service.rp.launch_id


# Playwright
@fixture(scope="session")
def get_playwright():
    with sync_playwright() as p:
        yield p


# Driver
@fixture
def driver(get_playwright, request):
    base_url = request.config.getini("base_url")    # Setup in pytest.ini
    app = App(get_playwright, base_url=base_url)
    app.goto("")
    yield app
    app.close()

