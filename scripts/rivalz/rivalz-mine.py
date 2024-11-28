import os
from webbrowser import Chrome
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

load_dotenv()

chrome_user_data_dir= os.getenv("CHROME_DATA_DIRECTORY")
password = os.getenv("PASSWORD")
rabby_extension_id=os.getenv("RABBY_EXTENSION_ID")

options = webdriver.ChromeOptions()

options.add_argument("--no-sandbox")
options.add_argument("--start-maximized")
options.add_argument("--disable-popup-blocking")
options.add_argument(f"--user-data-dir={chrome_user_data_dir}")
options.add_argument("--profile-directory=Default")

options.add_experimental_option("detach", True)


tabs = {}

driver = webdriver.Chrome(options=options)
print(driver.title)

def rivalz_mine():
    driver.switch_to.new_window('rivalz')
    driver.get("https://rivalz.ai/fragmentz?r=it_is_based")
    tabs['rivalz'] = driver.current_window_handle
    button = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="MINE"]')))
    button.click()
    for window in driver.window_handles:
        if window != driver.current_window_handle:
            driver.switch_to.window(window)
            break



def login_into_rabby():

    driver.get(f"chrome-extension://{rabby_extension_id}/index.html")
    tabs['rabby'] = driver.current_window_handle
    rabby_input = (WebDriverWait(driver,5)
                   .until(EC.presence_of_element_located((By.TAG_NAME, 'input'))))

    if rabby_input:
        rabby_input.send_keys( password)
        rabby_input.send_keys(Keys.RETURN)

try:
    login_into_rabby()
    # Чтобы расширения успели проснуться
    time.sleep(2)
    rivalz_mine()

    print(driver.window_handles)
    for window_handle in driver.window_handles:
        # print(driver.title, driver)
        print(tabs)
        if window_handle == tabs['rivalz'] or window_handle == tabs['rabby']:
            print(window_handle)
        else:
            driver.switch_to.window(window_handle)
    driver.execute_script("return document.documentElement.outerHTML")
    # rabby_sign_button = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.TAG_NAME,  'button')))
    # print(rabby_sign_button)

except Exception as e:
    print(driver.title)
    print(f"Наебнулось: {e}")

# finally:
#     # Закрытие браузера
#     driver.quit()