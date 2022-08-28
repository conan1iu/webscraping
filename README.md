# 🔭 Yahoo Finance Webscraping Project Documentation

- 🤔 Purpose of this documentation

This documentation is written in place to:

- Guide anyone who needs to take over this project or reuse the code 
- Help others understand key problems encountered and solutions engineered to inspire problem solving for any future problems
- 






Emojis

- 🔭 I’m currently working on ...

- 👯 I’m looking to collaborate on ...

- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ 


### Key errors encountered, solutions


N/A's were popping up in Excel for the PE Ratios, as Yahoo Finance doesn't report negative earnings. So if a PE Ratio was N/A, it was calculated by dividing Market Share Price by Earnings Per Share.[^bignote] 



### Final proposals

- Move data source to CNBC 
- Change inital data source to a more accurate list of the S&P 500 which updates daily


### What I would work on if I had more time... 🌱

- Some areas of code can be refined to follow best practices - I look forward to learning this as I gain more experience. If I had more time here I would:
            - Implement Python classes
            - Add even more comments
            - Make code more readable 
            - Figure out a way to segregate different parts of the functions to improve code reuseability 
            - Try to create even more robust error handling and implement better edge cases for compatability 
            
- 


[^bignote]: Here's one with multiple paragraphs and code.

        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options = options)
        driver.get(f'https://www.cnbc.com/quotes/{actual_ticker}')

        time.sleep(15)

        per_cnbc = driver.find_element(By.XPATH, '//*[@class="Summary-container"]/div[3]/ul/li[2]/span[2]').text
        per_cnbc = float(per_cnbc)

        per = per_cnbc

        flag1 = 'PE Ratio obtained from alt. source CNBC (N/A in Yahoo).'
      
      ![image](https://user-images.githubusercontent.com/87015101/187057110-40d69327-a32d-46c9-83a8-24f37f41651b.png)

      However, as I mentioned, simplify where possible to avoid introducing new errors. I ended up recalling my commerce course and instead sraped               the market share price and EPS Ratio from Yahoo Finance to calculate the negative PE Ratio (reducing the sources I was scraping from). 

