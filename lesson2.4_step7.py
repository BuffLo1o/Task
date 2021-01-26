from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
  return math.log(math.fabs(12 * math.sin(x)))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    # price = browser.find_element_by_id('price')
    # p = price.text
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "$100")
    )
    button1 = browser.find_element_by_id("book")
    button1.click()

    x_element = browser.find_element_by_id('input_value')
    x = int(x_element.text)
    print(x)
    y = str(calc(x))
    print(y)
    input1 = browser.find_element_by_id("answer")
    input1.click()
    input1.send_keys(y)

    button = browser.find_element_by_id("solve")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()