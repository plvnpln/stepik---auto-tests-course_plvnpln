from selenium import webdriver

import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
             
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")


t_element = browser.find_element_by_id("treasure")
x = t_element.get_attribute("valuex")
y = calc(x)

print(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

option1 = browser.find_element_by_id("robotCheckbox")
option1.click()

option2 = browser.find_element_by_id("robotsRule")
option2.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()







