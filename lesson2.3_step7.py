from selenium import webdriver
import time
import math

def calc(x):
  return math.log(math.fabs(12 * math.sin(x)))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    new_window = browser.window_handles[1]

    x_element = browser.find_element_by_id('input_value')
    x = int(x_element.text)
    print(x)
    y = str(calc(x))
    print(y)
    input1 = browser.find_element_by_id("answer")
    input1.click()
    input1.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()