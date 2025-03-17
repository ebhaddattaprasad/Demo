import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


driver=webdriver.Firefox()
driver.get("https://www.letskodeit.com/practice")
"""----------frame-----"""
#driver.switch_to.frame("courses-iframe")
# ew =WebDriverWait(driver ,10).until(EC.presence_of_element_located((By.XPATH ,"//div/a[text()='Sign In']")))
# ew.click()
"""--------Java Alert-----"""
driver.implicitly_wait(5)
# driver.find_element(By.ID,'name').send_keys("dattaprasad")
# driver.find_element(By.ID,'confirmbtn').click()
# d=driver.switch_to.alert
# time.sleep(2)
# d.dismiss()

"""-------"""

# driver.find_element(By.ID,'opentab').click()
# d=driver.window_handles
# driver.switch_to.window(d[1])
# time.sleep(3)
# driver.find_element(By.XPATH,"//a[text()='Sign In']").click()

driver.find_element(By.ID,'openwindow').click()
d=driver.window_handles
driver.switch_to.window(d[1])
time.sleep(3)
driver.find_element(By.XPATH,"//a[text()='Sign In']").click()