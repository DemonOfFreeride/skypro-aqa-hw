import allure
from selenium.webdriver.common.by import By

class ProductPage:
    """
        Класс Страница с продукцией, пользователь выбирает товар нажимая на кнопку 'Add to cart' 
    """ 
    
    def __init__(self, driver): # Инициализация браузера
        self._driver = driver
    
    @allure.step("Открывается старница с переченью товара")       
    def go_to_prod_page(self) -> None:
        """
            Функция открытия страници с переченью товара
        """  
        self._driver.get("https://www.saucedemo.com/inventory.html")
    
    @allure.step("Выбрать товар 'Sauce Labs Backpack'")    
    def add_to_cart_backpack(self) -> None:
        """
            Функция выбора для покунки товара 'Sauce Labs Backpack'
        """         
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()

    @allure.step("Выбрать товар 'Bike Light'")
    def add_to_cart_bike_light(self) -> None:
        """
            Функция выбора для покунки товара 'Bike Light'
        """ 
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light").click()       
    
    @allure.step("Выбрать товар 'T-shirt'") 
    def add_to_t_shirt(self) -> None:
        """
            Функция выбора для покунки товара 'T-shirt'
        """ 
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    
    @allure.step("Выбрать товар 'Fleece jacket'")     
    def add_to_cart_fleece_jacket(self) -> None:
        """
            Функция выбора для покунки товара 'Fleece jacket'
        """ 
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-fleece-jacket").click()
    
    @allure.step("Выбрать товар 'Labs Onesie'")     
    def add_to_cart_onesie(self) -> None:
        """
            Функция выбора для покунки товара 'Labs Onesie'
        """ 
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    
    @allure.step("Выбрать товар 'T-shirt (Red)'")     
    def add_to_cart_t_shirt_red(self) -> None:
        """
            Функция выбора для покунки товара 'T-shirt (Red)'
        """ 
        self._driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-test.allthethings()-t-shirt-(red)']").click()