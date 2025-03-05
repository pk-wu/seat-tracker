from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")  # Enable headless mode
options.add_argument("--disable-gpu")  # Recommended for headless mode
options.add_argument("--window-size=1920,1080")  # Optional: Set window size

driver = webdriver.Chrome(options=options)
# driver.get("https://www.google.com")
driver.get("https://www.korail.com/global/eng/intro")

print(driver.title)  # Just to confirm it's working

driver.quit()
print("its done")