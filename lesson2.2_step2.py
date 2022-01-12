
import time
from selenium import webdriver 
from selenium.webdriver.support.ui import Select

try:

    #link = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def sum(x1,x2):
     return str(int(x1)+int(x2))

    num1 = browser.find_elements_by_id("num1")[0].text
    num2 = browser.find_elements_by_id("num2")[0].text
    y=sum(num1, num2)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y)

    btnSubmit = browser.find_element_by_css_selector(".btn") 
    btnSubmit.click()
 
finally:

    time.sleep(10)
    browser.quit()