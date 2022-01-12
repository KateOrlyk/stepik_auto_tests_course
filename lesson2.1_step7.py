from selenium import webdriver
import time
import math

try:

    def calc(x):
     return str(math.log(abs(12*math.sin(int(x)))))

    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(int(x))
 
    input = browser.find_element_by_css_selector("[id='answer']")
    input.send_keys(y)
 
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
 
    radioB = browser.find_element_by_id("robotsRule")
    radioB.click()
 
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()