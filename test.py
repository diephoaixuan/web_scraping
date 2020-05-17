# -*- coding: utf-8 -*-
"""
Created on Sun May 17 12:48:40 2020

@author: dtha
"""

from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time
import re

url = 'https://s5.sir.sportradar.com/pinnaclevirtuals/en/1/season/1829728/h2h/276502/276513' # London Kiev
driver = webdriver.Chrome()
driver.execute_script("document.body.style.zoom='69%'")
driver.get(url)    
driver.maximize_window() # https://pythonbasics.org/selenium-maximize/

dropdown = driver.find_element_by_xpath('//*[@id="teambox"]/div[1]/div/div[1]/div[2]/div/div[1]')
dropdown.click()