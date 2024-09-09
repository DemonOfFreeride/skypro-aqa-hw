import allure
from selenium.webdriver.common.by import By

class CartPage:
    """
        Класс Страница корзина, на странице можно увидеть добавленый для покупки товар и его стоимость
    """ 
    
    def __init__(self, driver): # Инициализация браузера
        self._driver = driver
    
    @allure.step("Открывается старница карзины")      
    def go_to_cart_page(self) -> None:
        """
            Функция открытия страницы Корзина
        """  
        self._driver.get("https://www.saucedemo.com/cart.html")
     
    @allure.step("Перейти на страницу с перечнем товара")         
    def back_to_shoping(self) -> None:
        """
            Функция перехода из корзины на страницу с перечнем товара
        """ 
        self._driver.get("https://www.saucedemo.com/inventory.html")
    
    @allure.step("Удалить из корзины 'Sauce Labs Backpack'")    
    def del_from_cart_backpack(self) -> None:
        """
            Функция удаления из корзины 'Sauce Labs Backpack'
        """ 
        self._driver.find_element(By.CSS_SELECTOR, "#remove-sauce-labs-backpack").click()
    
    @allure.step("Удалить из корзины 'Bike Light'")         
    def del_from_cart_bike_light(self) -> None:
        """
            Функция удаления из корзины 'Bike Light'
        """ 
        self._driver.find_element(By.CSS_SELECTOR, "#remove-sauce-labs-bike-light").click()

    @allure.step("Удалить из корзины 'T-shirt'")
    def del_from_cart_t_shirt(self) -> None:
        """
            Функция удаления из корзины 'T-shirt'
        """ 
        self._driver.find_element(By.CSS_SELECTOR, "#remove-sauce-labs-bolt-t-shirt").click()

    @allure.step("Удалить из корзины 'Fleece jacket'") 
    def del_from_cart_fleece_jacket(self) -> None:
        """
            Функция удаления из корзины 'Fleece jacket'
        """ 
        self._driver.find_element(By.CSS_SELECTOR, "#remove-sauce-labs-fleece-jacket").click()

    @allure.step("Удалить из корзины 'Labs Onesie'") 
    def del_from_onesie(self) -> None:
        """
            Функция удаления из корзины 'Labs Onesie'
        """ 
        self._driver.find_element(By.CSS_SELECTOR, "#remove-sauce-labs-onesie").click()

    @allure.step("Удалить из корзины 'T-shirt (Red)'") 
    def del_from_cart_t_shirt_red(self) -> None:
        """
            Функция удаления из корзины 'T-shirt (Red)'
        """ 
        self._driver.find_element(By.CSS_SELECTOR, "[data-test='remove-test.allthethings()-t-shirt-(red)']").click()