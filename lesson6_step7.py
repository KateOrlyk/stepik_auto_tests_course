from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")

    #Заполняем автоматически все поля текстом "Test"
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
        element.send_keys("Test")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()