from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options

import pytest


def test_kerberos ():

    # options = Options()

    # options.add_experimental_option('excludeSwitches', ['enable-logging'])


    driver = webdriver.Chrome(ChromeDriverManager().install())


    driver.get("https://letmegooglethat.com/")

    assert "Let Me Google That" in driver.title
    print("Acessamos o: " + driver.title + "\n")

    # assert "Python" in driver.title
    elem = driver.find_elements(By.ID, "search-input")
    # print(elem)
    # elem.clear()
    text_box = elem[0] 
    text_box.send_keys("O que é Kerberos?")
    
    # generate the link
    but = driver.find_elements(By.ID, "search")[0].click()

    # sleep(15)

    url = driver.find_elements(By.ID, "url-result")

    assert url != []

    print(url[0].get_attribute('value'))

    # sleep(15)
    # elem.send_keys(Keys.RETURN)
    # assert "No results found." not in driver.page_source
    # print(x)

    driver.quit()