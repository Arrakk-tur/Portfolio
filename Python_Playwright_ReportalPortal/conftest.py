import logging
from typing import Generator

from pytest import fixture
from reportportal_client import RPLogger
from playwright.sync_api import sync_playwright, Playwright, APIRequestContext

from Python_Playwright_ReportalPortal.utilities.application import App
from Python_Playwright_ReportalPortal.api.api import ApiAuth


base_url_api = "https://restful-booker.herokuapp.com/"


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
        request,
        playwright: Playwright
) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(base_url=base_url_api)
    yield request_context
    request_context.dispose()


@fixture(scope="session")
def api_auth(
        playwright: Playwright, request, api_request_context
) -> Generator[APIRequestContext, None, None]:
    auth_token = ApiAuth().create_auth_token(api_request_context)
    headers = {"Cookie": auth_token}

    request_context = playwright.request.new_context(base_url=base_url_api, extra_http_headers=headers)
    yield request_context
    request_context.dispose()
