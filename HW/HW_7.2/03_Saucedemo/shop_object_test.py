from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

from pages.login_page import LoginPage
from pages.product_page import ProductPage

def test_cart_counter():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    login_page = LoginPage(browser)
    login_page.user_name("standard_user")
    login_page.password("secret_sauce")
    login_page.login()
    
    product_page = ProductPage(browser)
    product_page.go_to_prod_page()
    
    sleep(2)
    
    
    
