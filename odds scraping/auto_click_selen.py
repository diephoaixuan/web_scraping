from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

from collections import namedtuple
from namedlist import namedlist

recent_form = namedlist('recent_form', [
    'total',
    'overall',
    'record'
])

h2h_data = namedlist('h2h_data', [
    'league',
    'home',
    'away',
    'scoreFT',
    'scoreHT',
    'HW',
    'D',
    'AW',
    'WDL',
    'OU'], default=None)

def get_table(table_id):
    table = driver.find_element(By.ID,table_id)
    rows = table.find_elements(By.TAG_NAME,"tr")
    row_texts=[]
    for row in rows:
        row_texts.append(row.text)
    return row_texts

def getH2H(h2h_table):
    rows = h2h_table.find_elements(By.TAG_NAME, "tr")
    total_game = len(rows)-4
    latest_game = rows[3].find_elements(By.TAG_NAME, "td")
    h2h_full = [] 
    overall_form = [int(i) for i in rows[-1].text.split() if i.isdigit()]
    for row in rows[3:-1]:
        line = row.find_elements(By.TAG_NAME, "td")
        h2h = h2h_data(
            league = line[0].text,
            home = line[2].text,
            away = line[6].text ,
            scoreFT = line[3].text,
            scoreHT = line[4].text,
            HW = line[7].text,
            D = line[8].text,
            AW = line[9].text,
            WDL = line[13].text,
            OU = line[15].text
        )
        h2h_full.append(h2h)
    h2h_full.append(overall_form)
    return h2h_full 

def getForm(form_table):
    overall_form = [int(i) for i in form_table[-1].split() if i.isdigit()]
    record = []
    if len(overall_form)==0:
        total = 0
        overall = [0,0,0]
    else:
        total = overall_form[0]
        overall = overall_form[1:]
        record = [game[-1] for game in form_table[3:-1]]
    form = recent_form(
        total = total, 
        overall = overall,
        record = record
    )
    return form 

def homeFavorite(h2h_full):
    overallFavorite = h2h_full[-1][1]>h2h_full[-1][-1]
    return overallFavorite 

url = "http://www.nowgoal.com/2in1.htm?infoid="
driver = webdriver.Chrome()
driver.get(url)
click_actions = driver.find_elements_by_xpath("//a[@title='Match analyze']")

for action in click_actions:
    action.click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    # teams = driver.find_elements_by_xpath("//*[@id='headVs']/table/tbody/tr/td/span/a")
    # home = teams[0].text
    # away = teams[1].text 
    # print (home, 'vs', away)

    home_table = get_table('table_v1')
    away_table = get_table('table_v2')
#     h2h = get_table('table_v3')

    h2h_full = getH2H(driver.find_element(By.ID,'table_v3'))
    homeform = getForm(home_table)
    awayform = getForm(away_table)
    if len(h2h_full)==1:
        driver.close()
        driver.switch_to.window(driver.window_handles[0]) #back to the 1st loaded tab (all matches)
        continue
    if homeFavorite(h2h_full):
        print (h2h_full[0].home, ' vs ', h2h_full[0].away)
    driver.close()
    driver.switch_to.window(driver.window_handles[0]) #back to the 1st loaded tab (all matches)
driver.quit()
print('home favorite h2h scanner done !')