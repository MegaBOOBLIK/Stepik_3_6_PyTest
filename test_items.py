import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_butt_Add_In_Yor_Cart(browser):
    browser.get(link)
    browser.find_element(By.XPATH, "//button[contains(@class,'btn-add-to-basket')]")
    # browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    # time.sleep(30)
    
    button_name = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket').text
    assert button_name == f'Añadir al carrito', f'Vérifiez la langue ou corrigez la saisie :)'
    if __name__ == "__main__"
        pytest.main()    
