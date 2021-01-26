from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath('//label/span[@id="input_value"]')
    x = x_element.text
    y = str(calc(x))
    print(x, y)
#    input1 = browser.find_element_by_xpath('//label/span[@type="text"]')
    input1 = browser.find_element_by_class_name("form-control")
    input1.click()
    input1.send_keys(y)
    time.sleep(2)

 # Отправляем заполненную форму
    option1 = browser.find_element_by_css_selector("[id='robotCheckbox'")
    option1.click()
    time.sleep(1)

    option2 = browser.find_element_by_css_selector("[id='robotsRule'")
    option2.click()
    time.sleep(1)

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