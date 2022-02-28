import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
driver = webdriver.Chrome()
driver.get(link)

booking = WebDriverWait(driver, 12).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "100")
)

driver.find_element(By.CSS_SELECTOR, "#book").click()

x = (driver.find_element(By.CSS_SELECTOR, "#input_value")).text
res = math.log(abs(12*math.sin(int(x))))

inpf = driver.find_element(By.CSS_SELECTOR,"#answer")
inpf.send_keys(str(res))

btn = driver.find_element(By.CSS_SELECTOR, "#solve").click()

time.sleep(5)
driver.quit()