#scraping example
from selenium import webdriver
import pandas as pd
import time
#driver = webdriver.Chrome('D:\dha\trash script\chromedriver')
#driver.get('http://info.nowgoal.com/en/SubLeague/2010-2011/9/132.html')

# season = ['2010-2011', '2011-2012', '2012-2013', '2013-2014', '2014-2015', '2015-2016', '2016-2017', '2017-2018', '2018-2019']
season = ['2011-2012']
#Loop through seasons
for s in season:
    driver = webdriver.Chrome()
    driver.get('http://info.nowgoal.com/en/SubLeague/' + s + '/9/132.html')
    #driver.get('http://info.nowgoal.com/en/SubLeague/' + s + '/33.html')
    OddsRecord = pd.DataFrame(columns=['Round','Hometeam', 'Scorehome', 'Scoreaway','Awayteam','Home','Draw','Away','Date','Status'])

    round_no = driver.find_elements_by_xpath("//*[contains(@class,'lsm2')]")
    
    #Loop through rounds
    for i in round_no[:1]:
        print ('round_no 0',i)
        Round = i.text
        print ('Round', Round)
        i.click()
        match_no = driver.find_elements_by_xpath("//*[contains(@title,'Odds')]")
        print (match_no[0])
        for j in match_no[:1]:
            while (len(driver.window_handles) < 2):
                j.click()
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[1])

            print(driver.find_elements_by_xpath("//*[@id='headVs']/table/tbody/tr/td/span/a")[0])
            hometeam = driver.find_elements_by_xpath("//*[@id='headVs']/table/tbody/tr/td/span/a")[0].text
            homescore = driver.find_elements_by_xpath("//*[@id='headVs']/table/tbody/tr/td[2]/div/div/div")[0].text
            awayscore = driver.find_elements_by_xpath("//*[@id='headVs']/table/tbody/tr/td[2]/div/div/div[3]")[0].text
            awayteam = driver.find_elements_by_xpath("//*[@id='headVs']/table/tbody/tr/td[3]/span/a")[0].text
 
            #navigate to 365
            menu_no = driver.find_elements_by_xpath("//*[contains(@class,'mintopnav v2')]/li[4]")
            menu_no[0].click()
            menu_no = driver.find_elements_by_xpath("//*[contains(@id,'comBtn_8')]")
            menu_no[0].click()

            #get odd from table
            Home = driver.find_elements_by_xpath("//*[@id='div_h']/table/tbody/*/td[3]")
            Draw = driver.find_elements_by_xpath("//*[@id='div_h']/table/tbody/*/td[4]")
            Away = driver.find_elements_by_xpath("//*[@id='div_h']/table/tbody/*/td[5]")
            Date = driver.find_elements_by_xpath("//*[@id='div_h']/table/tbody/*/td[6]")
            Status = driver.find_elements_by_xpath("//*[@id='div_h']/table/tbody/*/td[7]")
            #table_no = driver.find_elements_by_xpath("//*[@id='div_h']/table/tbody/*")

            for k in range(1,len(Home)):
                OddsRecord.loc[len(OddsRecord)] = [Round, hometeam, homescore, awayscore, awayteam, Home[k].text, Draw[k].text, Away[k].text, Date[k].text, Status[k].text]

            # driver.close()
            driver.switch_to.window(driver.window_handles[0])
    # driver.quit()
    OddsRecord.to_csv('Bundesliga2_' + s + '.csv')
print("Done!")

