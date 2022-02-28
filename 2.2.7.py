from selenium.webdriver.common.by import By
from selenium import webdriver
import time



link = "http://suninjuly.github.io/file_input.html"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(link)

inpf1 = driver.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(2)")
inpf1.send_keys("Name")

inpf2 = driver.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(4)")
inpf2.send_keys("Surname")

inpf3 = driver.find_element(By.CSS_SELECTOR,"body > div > form > div > input:nth-child(6)")
inpf3.send_keys("mail@mail.com")

inpfile = driver.find_element(By.CSS_SELECTOR, "#file")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'text.txt')
inpfile.send_keys(file_path)


btn = driver.find_element(By.CSS_SELECTOR, "body > div > form > button").click()

time.sleep(5)
driver.quit()