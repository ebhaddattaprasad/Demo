import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


options = Options()
options.set_preference("permissions.default.desktop-notification", 2)  # 2 means block

driver=webdriver.Firefox(options=options)
driver.implicitly_wait(5)
driver.get("https://www.spicejet.com/profile/sign-up")
driver.find_element(By.XPATH,"//div[@class='css-1dbjc4n r-1awozwy r-18u37iz r-1wtj0ep']/div[text()='Mr']").click()
driver.find_element(By.XPATH,"//div[@class='css-1dbjc4n']/div[text()='Mrs']").click()
driver.find_element(By.XPATH,"//input[@placeholder='e.g. John']").send_keys("dattaprasad")
driver.find_element(By.XPATH,"//input[@placeholder='Doe']").send_keys("ebhad")
driver.find_element(By.XPATH,"//div[contains(@class,'css-76zvg2 css-bfa6kz r-ubezar')and contains(text(),'India')]").click()
driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("british")
driver.find_element(By.XPATH,"//div[text()='British Indian Ocean Territory']").click()
driver.find_element(By.XPATH,"//input[@placeholder='DD/MM/YYYY']").click()
driver.find_element(By.XPATH,"//div[text()='1993']").click()
driver.find_element(By.XPATH,"//div[text()='1993']").click()
driver.find_element(By.XPATH,"//div[text()='Mar']").click()
driver.find_element(By.XPATH,"//div[text()='13']").click()
driver.find_element(By.XPATH,"//input[@placeholder='e.g. 9876-453-010']").send_keys("9898989898")

driver.quit()