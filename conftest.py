import pytest

from core.api_client import ApiClient
from core.driver_factory import get_driver

@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def api_client():
    return ApiClient()