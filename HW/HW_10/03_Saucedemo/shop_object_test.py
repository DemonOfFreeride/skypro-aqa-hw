import allure
import pytest
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

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@allure.id("ST-1")
@allure.feature("AUTH")
@allure.title("Страница логинации")
@allure.description("Пользователь на страцине вводит логин и пароль после нажимает на кнопку 'Login'")
@allure.severity("Critical")
def test_login(browser):
    with allure.step("Логиннация пользователя"):
        login_page = LoginPage(browser)
        login_page.user_name("standard_user")
        login_page.password("secret_sauce")
        login_page.login()

@allure.id("ST-2")
@allure.feature("ADD")
@allure.title("Добавление продуктов в корзину")
@allure.description("Пользователь добавляет нескольких продуктов в корзину")
@allure.severity("Major")
def test_add_products_to_cart(browser):
    with allure.step("Добавление продуктов в корзину"):
        product_page = ProductPage(browser)
        product_page.go_to_prod_page()
        product_page.add_to_cart_backpack()
        product_page.add_to_t_shirt()
        product_page.add_to_cart_onesie()

@allure.id("ST-3")
@allure.feature("NAVIGATION")
@allure.title("Переход на страницу корзины")
@allure.description("Переход на страницу корзины для проверки добавленных продуктов")
@allure.severity("minor")
def test_go_to_cart(browser):
    with allure.step("Переход на страницу корзины"):
        cart_page = CartPage(browser)
        cart_page.go_to_cart_page()

@allure.id("ST-4")
@allure.story("Заполнение данных на странице оформления заказа")
@allure.feature("ADD")
@allure.title("Заполнение данных на странице оформления заказа")
@allure.description("Пользователь заполняет персональные данные на странице оформления заказа")
@allure.severity("critical")
def test_checkout(browser):
    with allure.step("Заполнение данных на странице оформления заказа"):
        checkout_page = CheckoutPage(browser)
        checkout_page.go_to_checkout_page()
        checkout_page.first_name("Luke")
        checkout_page.last_name("Skywalker")
        checkout_page.zip("431356")

@allure.id("ST-5")
@allure.story("Проверка общей суммы и завершение покупки")
@allure.feature("CHECKOUT")
@allure.title("Проверка общей суммы и завершение покупки")
@allure.description("Пользователь проверяет что зиказал и общую сумму далее завершает покупку")
@allure.severity("critical")
def test_verify_total_and_finish(browser):
    with allure.step("Проверка общей суммы и завершение покупки"):
        over_page = OverviewPage(browser)
        over_page.go_to_over_page()
        with allure.step("Получение общей суммы заказа"):
            tot = over_page.get_total()
            allure.attach(tot, name="Общая сумма заказа", attachment_type=allure.attachment_type.TEXT)
        with allure.step(f"Проверка суммы заказа: {tot}"):
            assert tot == "Total: $58.29", "Неправильная общая сумма заказа"
            allure.attach("Проверка суммы успешна", name="Результат проверки", attachment_type=allure.attachment_type.TEXT)
        
        over_page.finish_shoping()