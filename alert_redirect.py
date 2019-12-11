from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
             
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

button = browser.find_element_by_class_name("trollface.btn.btn-primary")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

num = browser.find_element_by_xpath("//span[@id ='input_value']")
x = num.text
y = calc(x)

answer = browser.find_element_by_class_name("form-control")
answer.send_keys(y)

button = browser.find_element_by_class_name("btn.btn-primary")
button.click()



