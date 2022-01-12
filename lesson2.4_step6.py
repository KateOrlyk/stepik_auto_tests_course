from selenium import webdriver
import time

try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/cats.html")
	browser.implicitly_wait(5)

	button = browser.find_element_by_id("button")
	buttun.click()

finally:
	time.sleep(10)
	browser.quit()