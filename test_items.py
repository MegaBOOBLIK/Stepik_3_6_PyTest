import time
import pytest
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_butt_Add_In_Yor_Cart(browser):
    browser.implicitly_wait(10)
    browser.get(link)
    
    assert browser.find_element(By.XPATH, "//button[contains(@class,'btn-add-to-basket')]")
    # browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    # time.sleep(30)
    
   
