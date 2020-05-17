# -*- coding: utf-8 -*-
"""
Created on Wed May 13 14:48:57 2020

@author: dtha
"""

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
        
if __name__ == '__main__' :    
    url = 'https://s5.sir.sportradar.com/pinnaclevirtuals/en/1/season/1829728/h2h/276502/276513' # London Kiev
    driver = webdriver.Chrome()
    driver.execute_script("document.body.style.zoom='69%'")
    driver.get(url)    
    driver.maximize_window() # https://pythonbasics.org/selenium-maximize/

    home_team = driver.find_element_by_xpath('//*[@id="teambox"]/div[2]/div/div[1]/div[2]/div/div[1]/div[2]').text
    way_team = driver.find_element_by_xpath('//*[@id="teambox"]/div[1]/div/div[1]/div[2]/div/div[2]/div[2]').text
    
    print 'Team: ',home_team
    
    showmore_home = driver.find_element_by_xpath('//*[@id="sr-container"]/div/div/div[3]/div/div/div/div[4]/div[2]/div/div/div/div/div/div/div[2]/button')
    showmore_home.click()
    
    shownext = driver.find_element_by_xpath('//*[@id="sr-container"]/div/div/div[3]/div/div/div/div[5]/div[2]/div/div/div/div/div/div/div[2]/button')
    shownext.click()
    
    
    rounds_list = []
    nexts_list = []
    
    rounds = driver.find_elements_by_xpath('//*[@id="sr-container"]/div/div/div[3]/div/div/div/div[4]/div[2]/div/div/div/div/div/div/div[1]/table/tbody/tr')   
    for i in reversed(range(len(rounds))):
        round = rounds[i].text
        round2 = round.replace('\n', ' ')
        round3 = round2.replace('VFLM','')
        round4 = round3.replace('VL','')
        round5 = round4.replace('(FT)','')
        id = round5.find(':')
        t = round5[id-2:id+3]
        round6 = round5.replace(t,'')
        rounds_list.append(round6)
        print idenUO(round6), round6
    
    nexts = driver.find_elements_by_xpath('//*[@id="sr-container"]/div/div/div[3]/div/div/div/div[5]/div[2]/div/div/div/div/div/div/div[1]/table/tbody/tr')
    for i in range(len(nexts)):
        round = nexts[i].text
        round2 = round.replace('\n', ' ')
        round3 = round2.replace('VFLM','')
        round4 = round3.replace('VL','')
        round5 = round4.replace('(FT)','')
        id = round5.find(':')
        t = round5[id-2:id+3]
        nexts_list.append(round5.replace(t,''))
    
    while(1):
        driver.get(driver.current_url)
        last_round = driver.find_element_by_xpath('//*[@id="sr-container"]/div/div/div[3]/div/div/div/div[4]/div[2]/div/div/div/div/div/div/div[1]/table/tbody/tr[1]')
        round = last_round.text
        temp = re.findall(r'\d+', round) 
        num = list(map(int, temp))          # nb_round - hour - min - home_score - way_score
        temp_last = re.findall(r'\d+', rounds_list[-1]) 
        num_last = list(map(int, temp_last))
        print num
        print num_last
        if (num[0]!=num_last[0]):
            round2 = round.replace('\n', ' ')
            round3 = round2.replace('VFLM','')
            round4 = round3.replace('VL','')
            round5 = round4.replace('(FT)','')
            id = round5.find(':')
            t = round5[id-2:id+3]
            round6 = round5.replace(t,'')  
            print idenUO(round6), round6
                
        time.sleep(20)
        
        next_round = driver.find_element_by_xpath('//*[@id="sr-container"]/div/div/div[3]/div/div/div/div[5]/div[2]/div/div/div/div/div/div/div[1]/table/tbody/tr[1]')
        
    
    driver.close()