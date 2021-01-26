from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('num1')
    x = int(x_element.text)
    z_element = browser.find_element_by_id('num2')
    z = int(z_element.text)
    print(x, z)
    y = str(x + z)
    print(y)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y)
    time.sleep(2)

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()