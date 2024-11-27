import os
from webbrowser import Chrome

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()

chrome_user_data_dir= os.getenv("CHROME_DATA_DIRECTORY")

options = webdriver.ChromeOptions()

options.add_argument("--no-sandbox")
options.add_argument(f"--user-data-dir={chrome_user_data_dir}")
options.add_argument("--profile-directory=Default")

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)


try:
    # Открытие сайта
    driver.get("https://rivalz.ai/fragmentz?r=it_is_based")
    print(driver.title)

    # Ищем кнопку
    button = driver.find_element(By.XPATH, '//button[text()="MINE"]')
    print(button.text)

    # Жмём
    button.click()


except Exception as e:
    print(f"Наебнулось: {e}")

# finally:
#     # Закрытие браузера
#     driver.quit()