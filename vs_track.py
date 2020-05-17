# -*- coding: utf-8 -*-
"""
Created on Mon May 11 13:07:10 2020

@author: dtha
"""
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time
import re

# driver = webdriver.Chrome(ChromeDriverManager().install())

from collections import namedtuple
from namedlist import namedlist

def idenUO(full_score_string):
    id = full_score_string.find(':')
#    print id
    home_score = int(full_score_string[id-1])
    way_score = int(full_score_string[id+1])
#    print home_score, way_score
    total_goal = home_score + way_score
#    print total_goal
    uo = 'U 2.5'
    if total_goal > 2.5:
        uo = 'O 2.5'
    if total_goal > 3.5:
        uo = 'O 3.5'
    return uo    

def print_schedule(url):
    driver = webdriver.Chrome()
    driver.get(url)    
    driver.maximize_window() # https://pythonbasics.org/selenium-maximize/

    home_team = driver.find_element_by_xpath('//*[@id="teambox"]/div[2]/div/div[1]/div[2]/div/div[1]/div[2]').text
    way_team = driver.find_element_by_xpath('//*[@id="teambox"]/div[1]/div/div[1]/div[2]/div/div[2]/div[2]').text
    
    print home_team
    
    showmore_home = driver.find_element_by_xpath('//*[@id="sr-container"]/div/div/div[3]/div/div/div/div[4]/div[2]/div/div/div/div/div/div/div[2]/button')
    showmore_home.click()
    
    showmore_way = driver.find_element_by_xpath('//*[@id="sr-container"]/div/div/div[3]/div/div/div/div[4]/div[3]/div/div/div/div/div/div/div[2]/button')
    showmore_way.click()
    
    shownext = driver.find_element_by_xpath('//*[@id="sr-container"]/div/div/div[3]/div/div/div/div[5]/div[2]/div/div/div/div/div/div/div[2]/button')
    shownext.click()
    
    shownext_way = driver.find_element_by_xpath('//*[@id="sr-container"]/div/div/div[3]/div/div/div/div[5]/div[3]/div/div/div/div/div/div/div[2]/button')
    shownext_way.click()
    
    home_matches = driver.find_element_by_xpath('//*[@id="sr-container"]/div/div/div[3]/div/div/div/div[4]/div[2]/div/div/div/div/div/div/div[1]/table')
#    print home_matches
#    print home_matches.text    
    
    way_matches = driver.find_element_by_xpath('//*[@id="sr-container"]/div/div/div[3]/div/div/div/div[4]/div[3]/div/div/div/div/div/div/div[1]/table')
#    print way_matches
    way_matches_text = way_matches.text.split('\n')    
#    print way_matches_text
    
    rounds = driver.find_elements_by_xpath('//*[@id="sr-container"]/div/div/div[3]/div/div/div/div[4]/div[2]/div/div/div/div/div/div/div[1]/table/tbody/tr')   
    for i in reversed(range(len(rounds))):
        round = rounds[i].text
        round2 = round.replace('\n', ' ')
        round3 = round2.replace('VFLM','')
        round4 = round3.replace('VL','')
        round5 = round4.replace('(FT)','')
#        times = re.findall(r'^(?:(?:(\d+):)?(\d+):)$',round5)
#        print times
#        round6 = round5.replace(times[0],'')
        id = round5.find(':')
        t = round5[id-2:id+3]
        round6 = round5.replace(t,'')
        print idenUO(round6), round6
    
    
    nexts = driver.find_elements_by_xpath('//*[@id="sr-container"]/div/div/div[3]/div/div/div/div[5]/div[2]/div/div/div/div/div/div/div[1]/table/tbody/tr')
    for i in range(len(nexts)):
        round = nexts[i].text
        round2 = round.replace('\n', ' ')
        round3 = round2.replace('VFLM','')
        round4 = round3.replace('VL','')
        round5 = round4.replace('(FT)','')
#        times = re.findall(r'^(?:(?:(\d+):)?(\d+):)$',round5)
#        print times
#        round6 = round5.replace(times[0],'')
        id = round5.find(':')
        t = round5[id-2:id+3]
        print round5.replace(t,'')    
    print ('---------------------------------------------\n')
    print way_team
    rounds_way = driver.find_elements_by_xpath('//*[@id="sr-container"]/div/div/div[3]/div/div/div/div[4]/div[3]/div/div/div/div/div/div/div[1]/table/tbody/tr')
    for i in reversed(range(len(rounds_way))):
        round = rounds_way[i].text
        round2 = round.replace('\n', ' ')
        round3 = round2.replace('VFLM','')
        round4 = round3.replace('VL','')
        round5 = round4.replace('(FT)','')
#        times = re.findall(r'^(?:(?:(\d+):)?(\d+):)$',round5)
#        print times
#        round6 = round5.replace(times[0],'')
        id = round5.find(':')
        t = round5[id-2:id+3]
        round6 = round5.replace(t,'')
        print idenUO(round6), round6
    
    nexts_way = driver.find_elements_by_xpath('//*[@id="sr-container"]/div/div/div[3]/div/div/div/div[5]/div[3]/div/div/div/div/div/div/div[1]/table/tbody/tr')
    for i in range(len(nexts_way)):
        round = nexts_way[i].text
        round2 = round.replace('\n', ' ')
        round3 = round2.replace('VFLM','')
        round4 = round3.replace('VL','')
        round5 = round4.replace('(FT)','')
#        times = re.findall(r'^(?:(?:(\d+):)?(\d+):)$',round5)
#        print times
#        round6 = round5.replace(times[0],'')
        id = round5.find(':')
        t = round5[id-2:id+3]
        print round5.replace(t,'')    
    print ('---------------------------------------------\n')    
    driver.close()
        
if __name__ == '__main__' :    
#    print_schedule('https://s5.sir.sportradar.com/pinnaclevirtuals/en/1/season/1831606/h2h/276505/276508') #  mos ber
    print_schedule('https://s5.sir.sportradar.com/pinnaclevirtuals/en/1/season/1831548/h2h/276512/276502') # par lon
    print_schedule('https://s5.sir.sportradar.com/pinnaclevirtuals/en/1/season/1831548/h2h/276513/276514') #kiev rom