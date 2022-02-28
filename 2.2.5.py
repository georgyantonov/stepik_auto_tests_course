from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math

link = "http://suninjuly.github.io/execute_script.html"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(link)

btn = driver.find_element(By.CSS_SELECTOR, "body > div > form > button")
driver.execute_script("window.scrollBy(0, 150);")

x = (driver.find_element(By.CSS_SELECTOR, "#input_value")).text
res = math.log(abs(12*math.sin(int(x))))



inputf = driver.find_element(By.CSS_SELECTOR, "#answer")
inputf.send_keys(res)

chb = driver.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
rdbtn = driver.find_element(By.CSS_SELECTOR, "#robotsRule").click()
btn.click()

time.sleep(5)
driver.quit()