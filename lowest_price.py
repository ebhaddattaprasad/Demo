from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
all_name=all_price=driver.find_elements(By.XPATH,"//div[@class='tableFixHead']//tbody/tr/td[1]")
all_price=driver.find_elements(By.XPATH,"//div[@class='tableFixHead']//tbody/tr/td[4]")
dict1={}
namelist=[]
pricelist=[]
higher= {}
count=0

for name in all_name:
    n1=name.text
    namelist.append(n1)
for price in all_price:
        p1=int(price.text)
        pricelist.append(p1)
print(namelist,pricelist,len(all_name))
for item in range(0,len(all_name)):
    dict1[namelist[item]]=pricelist[item]

for nam1,price1 in dict1.items():
    if price1>count:
        count=price1
        higher[nam1]=price1

print(higher)
