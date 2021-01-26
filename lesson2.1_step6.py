from selenium import webdriver
import time
import math

def calc(x):
  return math.log(math.fabs(12 * math.sin(x)))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_tag_name('img')
    x_element1 = int(x_element.get_attribute('valuex'))
    print(x_element1)
    y = str(calc(x_element1))
    input1 = browser.find_element_by_id("answer")
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