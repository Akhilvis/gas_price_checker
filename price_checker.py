import time
from math import floor
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

gas_price_cutff = 140

driver = webdriver.Edge()
driver.get("https://www.gasbuddy.com/station/21424")
time.sleep(10)
gas_regular_ele = driver.find_element(
    By.XPATH,
    '//*[@id="root"]/div/div[3]/div/div/div[2]/div[1]/div[1]/div[1]/div[3]/div/div[2]/div[2]/div[1]/span',
)

regular_price = gas_regular_ele.text
regular_price = regular_price.replace("¢", "")
regular_price = int(eval(regular_price))

if regular_price < gas_price_cutff:
    pass
else:
    print("Price is high!!!")

time.sleep(10)


driver.close()
