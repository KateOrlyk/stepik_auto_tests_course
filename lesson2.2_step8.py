from selenium import webdriver
import time
import os

try:
	link = 'http://suninjuly.github.io/file_input.html'
	browser = webdriver.Chrome()
	browser.get(link)

	input1 = browser.find_element_by_name("firstname")
	input1.send_keys("Kate")

	input2 = browser.find_element_by_name("lastname")
	input2.send_keys("Suprunenko")

	input3 = browser.find_element_by_name("email")
	input3.send_keys("kate.suprunenko24@gmail.com")

	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir, 'file.txt')
	element = browser.find_element_by_name("file") #browser.find_elements_by_name не подходит, так как нужно выбрать один елемент 
	element.send_keys(file_path)

	button = browser.find_element_by_css_selector("button.btn")
	button.click()

finally:
	time.sleep(30)
	browser.quit()