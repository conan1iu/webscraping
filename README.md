## 🔭 Yahoo Finance Webscraping Project Documentation




Emojis

- 🔭 I’m currently working on ...

- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ 

'''python
options = Options()
options.headless = True
driver = webdriver.Chrome(options = options)
driver.get(f'https://www.cnbc.com/quotes/{actual_ticker}')
            
time.sleep(15)
            
per_cnbc = driver.find_element(By.XPATH, '//*[@class="Summary-container"]/div[3]/ul/li[2]/span[2]').text
per_cnbc = float(per_cnbc)
            
per = per_cnbc
            
flag1 = 'PE Ratio obtained from alt. source CNBC (N/A in Yahoo).'
'''



## Final proposals

- Move data source to CNBC 
- Change inital data source to a more accurate list of the S&P 500 which updates daily


## What I would work on if I had more time... 🌱

- Okay
  - test

