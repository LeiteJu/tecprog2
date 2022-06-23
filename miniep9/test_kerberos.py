from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options

import pytest


if __name__ == "__main__":

    driver = webdriver.Chrome(ChromeDriverManager().install())


    driver.get("https://letmegooglethat.com/")

    assert "Let Me Google That" in driver.title
    print("Acessamos o: " + driver.title + "\n")

    elem = driver.find_elements(By.ID, "search-input")
    text_box = elem[0] 
    text_box.send_keys("O que e Kerberos?")
    
    # generate the link
    but = driver.find_elements(By.ID, "search")[0].click()

    url = driver.find_elements(By.ID, "url-result")

    assert url != []

    print(url[0].get_attribute('value'))

    driver.quit()