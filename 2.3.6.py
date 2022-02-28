from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(link)

fckn_btn = driver.find_element(By.CSS_SELECTOR, "body > form > div > div > button").click()

new_window = driver.window_handles[1]
driver.switch_to.window(new_window)

x = (driver.find_element(By.CSS_SELECTOR, "#input_value")).text
res = math.log(abs(12*math.sin(int(x))))

inpf = driver.find_element(By.CSS_SELECTOR,"#answer")
inpf.send_keys(str(res))

btn = driver.find_element(By.CSS_SELECTOR, "body > form > div > div > button").click()
time.sleep(5)
driver.quit()