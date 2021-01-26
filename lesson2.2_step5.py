from selenium import webdriver
import time
import math

def calc(x):
  return math.log(math.fabs(12*math.sin(x)))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = int(x_element.text)
    y = str(calc(x))
    input1 = browser.find_element_by_id("answer")
    input1.click()
    input1.send_keys(y)
    time.sleep(0)

    browser.execute_script("window.scrollBy(0, 100);")

 # Отправляем заполненную форму
    option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
    option1.click()
    time.sleep(0)

    option2 = browser.find_element_by_css_selector("[id='robotsRule']")
    option2.click()
    time.sleep(0)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()