from selenium.common.exceptions import NoAlertPresentException # в начале файла
from selenium import webdriver
import time
import math
import pytest


link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(10)
address = browser.find_element_by_xpath("//button[@value='Добавить в корзину']")
address.click()
alert = browser.switch_to.alert
browser.implicitly_wait(5)
alert = browser.switch_to.alert
x = alert.text.split(" ")[2]
answer = str(math.log(abs((12 * math.sin(float(x))))))
alert.send_keys(answer)
alert.accept()
