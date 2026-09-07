from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import os


def create_driver():
    browser = os.getenv("BROWSER", "chrome").lower()

    if browser == "chrome":
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        return webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        return webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")