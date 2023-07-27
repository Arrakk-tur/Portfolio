import logging
import sys
from typing import Generator

from pytest import fixture
from reportportal_client import RPLogger
from playwright.sync_api import sync_playwright, Playwright, APIRequestContext

from utilities.application import App, Api


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


# API Playwright
@fixture(scope='session')
def api_request_context(
        playwright: Playwright, request
) -> Generator[APIRequestContext, None, None]:
    base_url_api = request.config.getini("base_url_api")    # Setup in pytest.ini
    request_context = playwright.request.new_context(base_url=base_url_api)
    yield request_context
    request_context.dispose()


@fixture(scope="session")
def api_auth(api_request_context) -> Generator[APIRequestContext, None, None]:
    request_context = Api().create_auth_token(api_request_context)
    yield request_context
    request_context.dispose()
