from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))

	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/explicit_wait2.html")

	browser.implicitly_wait(5)

	price = WebDriverWait(browser, 12).until(
		EC.text_to_be_present_in_element((By.ID, "price"), "100")
		)
	button1 = browser.find_element_by_id("book")
	button1.click()

	element = browser.find_element_by_id("answer");
	browser.execute_script("arguments[0].scrollIntoView(true);", element);

	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	y = calc(int(x))

	input = browser.find_element_by_id("answer")
	input.send_keys(y)

	button2 = browser.find_element_by_id("solve")
	button2.click()

finally:
	time.sleep(12)