import os

import pytest

from utils.driver_factory import create_driver


@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = os.path.join(
                "screenshots",
                f"{item.name}.png"
            )

            driver.save_screenshot(screenshot_path)