#bs4 libraries 
from urllib import response
from bs4 import BeautifulSoup
import requests, openpyxl 

#due diligence library
import urllib.request

#excel library
from lxml import html

#selenium libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
import webbrowser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import re as re
import time
from selenium.webdriver.chrome.options import Options

#creation of excel spreadsheet
excel=openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active
sheet.title = 'Stocks'
print(excel.sheetnames)

sheet.append
sheet.append(['Rank by Weight', 'Code', 'Amended Code', 'Name', 'Market Cap', 'PE Ratio', 'Sector', 'Comments'])

#replace this with your user agent
my_user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36' 

#navigating the S&P 500 list website
url = 'https://topforeignstocks.com/indices/components-of-the-sp-500-index/'
source = requests.get(url)
soup = BeautifulSoup(source.text, 'html.parser') 
stocks = soup.find('tbody', class_='row-hover').find_all('tr')

stocks = stocks[88:89] #you can use this to filter a specific stock you know is giving you issues (to test your error handling)

for stock in stocks: 
    
    rank = int(stock.find('td', class_ = 'column-1').text)
    code = stock.find('td', class_ = 'column-3').a.text
    name = stock.find('td', class_ = 'column-2').text
    sector = stock.find('td', class_= 'column-4').text
    
    try:
        def extract(ticker):
            headers = {'User-Agent': my_user_agent}
            source = requests.get(f'https://finance.yahoo.com/quote/{ticker}?ltr=1')
            source.raise_for_status()
            url = f'https://finance.yahoo.com/quote/{ticker}?ltr=1'
            response = requests.get(url, headers)
            baguette = BeautifulSoup(response.text, 'html.parser')
            return baguette
        
        def transform1(baguette):
            mkt_capp = baguette.find('td', {'data-test':"MARKET_CAP-value"}).text.strip()
            return mkt_capp
        
        def transform2(baguette):
            perr = baguette.find('td', {'data-test':"PE_RATIO-value"}).text.strip()
            return perr

        c = extract(code) 
        mkt_cap = transform1(c) 
        per = transform2(c)
        
        actual_ticker = code 
        
        if (per == 'N/A'):
            
            options = Options()
            options.headless = True
            driver = webdriver.Chrome(options = options)
            driver.get(f'https://www.cnbc.com/quotes/{actual_ticker}')
            
            time.sleep(15)
            
            per_cnbc = driver.find_element(By.XPATH, '//*[@class="Summary-container"]/div[3]/ul/li[2]/span[2]').text
            per_cnbc = float(per_cnbc)
            
            per = per_cnbc
            
            flag1 = 'PE Ratio obtained from alt. source CNBC (N/A in Yahoo).'
            
            print(rank, code, actual_ticker, name, mkt_cap, per, sector, flag1)
        
            sheet.append([rank, code, actual_ticker, name, mkt_cap, per, sector, flag1]) 
            
        else:
            per = float(per)
            
            print(rank, code, actual_ticker, name, mkt_cap, per, sector)
        
            sheet.append([rank, code, actual_ticker, name, mkt_cap, per, sector])   
    except:
        try:
            options = Options()
            options.headless = True
            driver = webdriver.Chrome(options = options)
            driver.get('https://finance.yahoo.com/')
            errorstock = ' '.join(name.split()[:2])
            driver.find_element('id','yfin-usr-qry').send_keys(errorstock)
            time.sleep(5)
            driver.find_element('id', 'result-quotes-0').click()
            time.sleep(8)
            
            mkt_cap = driver.find_element(By.XPATH, "//td[@data-test='MARKET_CAP-value']").text
            per = driver.find_element(By.XPATH, "//td[@data-test='PE_RATIO-value']").text
                        
            actual_ticker_text = driver.find_element(By.XPATH, "//*[@id='similar-by-symbol']/h2/span").text
            actual_ticker = actual_ticker_text.split()[-1]
            
            flag2 = 'Original URL did not load for ticker. Stock was searched up by name, possibly amended ticker obtained instead.'
            
            if (per == 'N/A'):
            
                options = Options()
                options.headless = True
                driver = webdriver.Chrome(options = options)
                driver.get(f'https://www.cnbc.com/quotes/{actual_ticker}')
                
                time.sleep(15)
                
                per_cnbc = driver.find_element(By.XPATH, '//*[@class="Summary-container"]/div[3]/ul/li[2]/span[2]').text
                per_cnbc = float(per_cnbc)
                
                per = per_cnbc
                
                flag1 = 'PE Ratio obtained from alt. source CNBC (N/A in Yahoo).'
                
                comment = flag1 + " " + flag2
                
                print(rank, code, actual_ticker, name, mkt_cap, per, sector, comment)
            
                sheet.append([rank, code, actual_ticker, name, mkt_cap, per, sector, comment]) 
            
            else:
                
                per = float(per)
                
                print(rank, code, actual_ticker, name, mkt_cap, per, sector, flag2)
            
                sheet.append([rank, code, actual_ticker, name, mkt_cap, per, sector, flag2])
           
        except:
            try:
                options = Options()
                options.headless = True
                driver = webdriver.Chrome(options = options)
                driver.get('https://finance.yahoo.com/')
                errorstock = ' '.join(name.split()[:1])
                driver.find_element('id','yfin-usr-qry').send_keys(errorstock)
                time.sleep(5)
                driver.find_element('id', 'result-quotes-0').click()
                time.sleep(8)
                
                mkt_cap = driver.find_element(By.XPATH, "//td[@data-test='MARKET_CAP-value']").text
                per = driver.find_element(By.XPATH, "//td[@data-test='PE_RATIO-value']").text
                
                actual_ticker_text = driver.find_element(By.XPATH, "//*[@id='similar-by-symbol']/h2/span").text
                actual_ticker = actual_ticker_text.split()[-1]
            
                flag2 = 'Original URL did not load for ticker. Stock was searched up by name, possibly amended ticker obtained instead.'

                if (per == 'N/A'):
            
                    options = Options()
                    options.headless = True
                    driver = webdriver.Chrome(options = options)
                    driver.get(f'https://www.cnbc.com/quotes/{actual_ticker}')
                    
                    time.sleep(15)
                    
                    per_cnbc = driver.find_element(By.XPATH, '//*[@class="Summary-container"]/div[3]/ul/li[2]/span[2]').text
                    per_cnbc = float(per_cnbc)
                    
                    per = per_cnbc
                    
                    flag1 = 'PE Ratio obtained from alt. source CNBC (N/A in Yahoo).'
                    
                    comment = flag1 + " " + flag2
                    
                    print(rank, code, actual_ticker, name, mkt_cap, per, sector, comment)
                
                    sheet.append([rank, code, actual_ticker, name, mkt_cap, per, sector, comment]) 
            
                else:
                    
                    per = float(per)
                    
                    print(rank, code, actual_ticker, name, mkt_cap, per, sector, flag2)
                
                    sheet.append([rank, code, actual_ticker, name, mkt_cap, per, sector, flag2])
               
            except:
                flag = f'Investigate the stock with name {name} further within source data.'
                
                actual_ticker = 'See comment.'
                mkt_cap = 'See comment.'
                per = 'See comment.'
                
                print(rank, code, actual_ticker, name, mkt_cap, per, sector, flag)
        
                sheet.append([rank, code, actual_ticker, name, mkt_cap, per, sector, flag])    

#save the excel spreadsheet
excel.save('S&P 500 Stock Information.csv')

