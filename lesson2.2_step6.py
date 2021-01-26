from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Gi")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Gi")
    input2 = browser.find_element_by_name("email")
    input2.send_keys("Gi")

    current_dir = os.path.abspath(os.path.dirname(""))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element_by_id('file')
    element.send_keys(file_path)

    # Отправляем заполненную форму
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