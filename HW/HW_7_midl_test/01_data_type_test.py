from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
driver.set_window_size(1280, 850)

f_name = driver.find_element(By.CSS_SELECTOR, "[name='first-name']")
f_name.clear()
f_name.send_keys("Иван")

l_name = driver.find_element(By.CSS_SELECTOR, "[name='last-name']")
l_name.clear()
l_name.send_keys("Петров")

address = driver.find_element(By.CSS_SELECTOR, "[name='address']")
address.clear()
address.send_keys("Ленина, 55-3")

city = driver.find_element(By.CSS_SELECTOR, "[name='city']")
city.clear()
city.send_keys("Москва")

country = driver.find_element(By.CSS_SELECTOR, "[name='country']")
country.clear()
country.send_keys("Россия")

email = driver.find_element(By.CSS_SELECTOR, "[name='e-mail']")
email.clear()
email.send_keys("test@skypro.com")

phone = driver.find_element(By.CSS_SELECTOR, "[name='phone']")
phone.clear()
phone.send_keys("+7985899998787")	

job_pos = driver.find_element(By.CSS_SELECTOR, "[name='job-position']")
job_pos.clear()
job_pos.send_keys("QA")

company = driver.find_element(By.CSS_SELECTOR, "[name='company']")
company.clear()
company.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

zip_code_field_color = driver.find_element(By.CSS_SELECTOR, "#zip-code")
print(f" цвет не заполненного поля - {zip_code_field_color.value_of_css_property('background-color')}") # цвет НЕ заполенного поля после нажатия на кнопку "Submit"

company_field_color = driver.find_element(By.CSS_SELECTOR, "#company")
print(f" цвет заполненного поля - {company_field_color.value_of_css_property('background-color')}") # цвет заполенного поля после нажатия на кнопку "Submit"


fields = {
    "f_name": "#first-name",
    "l_name": "#last-name",
    "address": "#address",
    "city": "#city",
    "zip_code": "#zip-code",
    "country": "#country",
    "email": "#e-mail",
    "phone": "#phone",
    "job_pos": "#job-position",
    "company": "#company"
}

def assert_field_color(field_name, expected_color):
    field = driver.find_element(By.CSS_SELECTOR, fields[field_name])
    actual_color = field.value_of_css_property("background-color")
    try:
        assert actual_color == expected_color, f"Поле '{field_name}' не подсвечено правильным цветом"
    except AssertionError as e:
        print(e)
    

assert_field_color("f_name", "rgba(209, 231, 221, 1)")
assert_field_color("l_name", "rgba(209, 231, 221, 1)")
assert_field_color("address", "rgba(209, 231, 221, 1)")
assert_field_color("zip_code", "rgba(248, 215, 218, 1)")
assert_field_color("city", "rgba(209, 231, 221, 1)")
assert_field_color("country", "rgba(209, 231, 221, 1)")
assert_field_color("email", "rgba(209, 231, 221, 1)")
assert_field_color("phone", "rgba(209, 231, 221, 1)")
assert_field_color("job_pos", "rgba(209, 231, 221, 1)")
assert_field_color("company", "rgba(209, 231, 221, 1)")


driver.quit()