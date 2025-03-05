from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# for headless mode stuff
options = Options()
options.add_argument("--headless")  # Enable headless mode
options.add_argument("--disable-gpu")  # Recommended for headless mode
options.add_argument("--window-size=1920,1080")  # Optional: Set window size
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()

def main():
    # get webpage
    driver.get("https://www.korail.com/global/eng/intro")
    time.sleep(1)
    print("1")

    # search button from main page
    button = driver.find_element(By.XPATH, "//*[@id='introDiv']/main/article/section[2]/button")
    button.click()
    time.sleep(1)
    print("2")

    # date select
    button = driver.find_element(By.XPATH, "//*[@id='dateinput__input-wrapper']")
    button.click()
    time.sleep(1)
    print("3")

    # date 25 select
    button = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/div/div/table/tbody/tr[5]/td[3]/a/span")
    button.click()
    time.sleep(1)
    print("4")
    # time.sleep(25)
    # right
    # right /html/body/div[5]/div/div/div/div[2]/div/div[2]/div/div/button[2]
    button = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[2]/div/div[2]/div/div/button[2]")
    button.click()
    time.sleep(1)
    button.click()
    time.sleep(1)
    print("5")

    # 11 select for 12pm
    button = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[2]/div/div[2]/div/div/div/div/div[12]/div/li/a")
    button.click()
    time.sleep(1)
    print("6")

    # apply button
    button = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[2]/div/div[3]/button[2]")
    button.click()
    time.sleep(1)

    # swap busan <> seoul : /html/body/div[1]/div[3]/div/div/section/div/div[2]/div/div/div/div/div[1]/div/div[2]/button
    button = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/section/div/div[2]/div/div/div/div/div[1]/div/div[2]/button")
    button.click()
    time.sleep(1)  

    # KTX /html/body/div[1]/div[3]/div[1]/div/div[2]/div/div/ul/li[3]/div/div[2]/div/a
    button = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div/ul/li[3]/div/div[2]/div/a")
    button.click()
    time.sleep(1)

    # seat selection /html/body/div[1]/div[3]/div[2]/div/div[2]/ul[2]/li[3]/a
    button = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div[2]/ul[2]/li[3]/a")
    button.click()
    time.sleep(1)

    # car selection
    button = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[2]/div/div/div[1]/div/div[1]/a")
    button.click()
    time.sleep(1)

    # get the list
    seat_list = driver.find_elements(By.XPATH, "//*[@id='srcar_select_options_ul']")
    
    for ul in seat_list:
        # Find all <li> elements within the current <ul>
        li_elems = ul.find_elements(By.TAG_NAME, "li")
        # Loop through the <li> elements and print their text
        for li in li_elems:
            print(li.text)
            print()

    time.sleep(1)
    driver.quit()

if __name__ == "__main__":
    main()