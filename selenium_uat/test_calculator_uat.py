import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

BASE_URL = os.environ.get("BASE_URL", "http://localhost:1234")

def test_addition_flow():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(BASE_URL)

        driver.find_element(By.NAME, "first").send_keys("26")
        driver.find_element(By.NAME, "second").send_keys("24")
        driver.find_element(By.TAG_NAME, "button").click()

        time.sleep(1)

        result_text = driver.find_element(By.ID, "result").text
        assert "50" in result_text
    finally:
        driver.quit()