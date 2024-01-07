from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverviewPage

def test_cart_counter():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    login_page = LoginPage(browser)
    login_page.user_name("standard_user")
    login_page.password("secret_sauce")
    login_page.login()
    
    product_page = ProductPage(browser)
    product_page.go_to_prod_page()
    product_page.add_to_cart_backpack()
    product_page.add_to_t_shirt()
    product_page.add_to_cart_onesie()
    
    cart_page = CartPage(browser)
    cart_page.go_to_cart_page()
    
    checkout_page = CheckoutPage(browser)
    checkout_page.go_to_checkout_page()
    checkout_page.first_name("Luke")
    checkout_page.last_name("Skywalker")
    checkout_page.zip("431356")
    
    over_page = OverviewPage(browser)
    over_page.go_to_over_page()
    tot = over_page.get_total()
    over_page.finish_shoping()
    
    browser.quit()
    
    assert tot == "Total: $58.29" , "Не правильтаня общая сумма заказа"