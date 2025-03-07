import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    service_obj = Service("/Users/nomiklee/Downloads/chromedriver-mac-arm64/chromedriver")
    driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()