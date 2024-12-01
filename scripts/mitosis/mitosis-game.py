import os
from webbrowser import Chrome
import time

from pywinauto.findwindows import find_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

load_dotenv()

def execute_js(code):
    return driver.execute_script(code)


cell_ids = [
    '2-8', '2-7', '2-6', '2-5', '2-4',
    '3-5', '4-6', '5-5', '6-4', '6-5', '6-6', '6-7', '6-8',
    '9-8', '9-7', '9-6', '9-5', '9-4',
    '12-4', '13-4', '14-4', '13-5', '13-6', '13-7', '13-8',
    '17-8', '18-8', '19-8', '20-8', '20-7', '20-6', '20-5', '20-4', '19-4', '18-4', '17-4', '17-5', '17-6', '17-7'
]


def get_element_by_id(data_cell_id):
    return WebDriverWait(driver, 100000).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'[data-cell-id="{data_cell_id}"]')))


def go_through_elements(array):
    for id in array:
        element = get_element_by_id(id)
        if element:
            webdriver.ActionChains(driver).move_to_element(element).click().perform()

def process_cell_ids():
    go_through_elements(cell_ids)
    go_through_elements(reversed(cell_ids))
    process_cell_ids()


chrome_user_data_dir= os.getenv("CHROME_DATA_DIRECTORY")

options = webdriver.ChromeOptions()

options.add_argument("--no-sandbox")
# options.add_argument("--start-maximized")
options.add_argument("--disable-popup-blocking")
options.add_argument(f"--user-data-dir={chrome_user_data_dir}")
options.add_argument("--profile-directory=Default")

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

try:
    time.sleep(2)

    driver.get("https://testnet.mitosis.org/")

    time.sleep(2)

    button_play = WebDriverWait(driver, 1000).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Mini Game')]"))
    )

    button_play.click()

    time.sleep(2)

    process_cell_ids()

except Exception as e:
    print(f"Наебнулось: {e}")


finally:
    process_cell_ids()