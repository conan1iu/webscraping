# 🔭 Yahoo Finance Webscraping Project Documentation

<br>

## 💡 Purpose of this documentation

<br>

This documentation is written in place to:

- Guide anyone who needs to take over this project or reuse the code elsewhere 
- Help others understand key problems encountered and solutions engineered (to inspire problem solving for any future problems)
- Detail my reflections on:
  - Possible improvements for next time
  - Recommendations for future work 
  - Notable findings and final remarks

<br>

## 🤔 Key errors encountered and engineered solutions (in chronological order)

<br>

N/A's were popping up in Excel for the PE Ratios, as Yahoo Finance doesn't report negative earnings. So if a PE Ratio was N/A, it was calculated by dividing Market Share Price by Earnings Per Share.[^bignote] 

<br>

## 🌱 What I would work on if I had more time... 

<br>

- Some areas of code can be refined even further - I look forward to improving my best practices further as I gain more experience. If I had more time here I would:

  - Implement Python classes
  - Add even more comments
  - Make code more readable 
  - Segregate different parts of the functions to improve code reuseability 
  - Try to create even more robust error handling (monitor program over several days to gain more insight into further issues which can arise).
  - Implement better edge cases in error treatment for compatability, simplicity and further error risk management 

<br>

- Given more time to work on this project I would also continue future proofing by:
  - Moving code to cloud so it can run remotely as running the program takes a while
  - 
 

<br>

## Final recommendations and comments

<br>

- Change inital data source to a more reliable list of the S&P 500 which updates daily and contains the correct tickers
- Switch data source to CNBC or NASDAQ given reliability issues as seen with Yahoo Finance
- The Excel spreadsheet contains both the original scraped output plus a sheet containing manually cleaned data, i.e., checking comments and removing outliers)


<br>

## Footnotes

[^bignote]: Initially, I calculated the PE ratio by scraping the market share price and earnings per share for the companies (then calculating their ratio to find the PE ratio) with negative earnings. However, Yahoo Finance actually reports a different EPS to CNBC, NASDAQ, WSJ, etc. for some reason (see image below code). I've included the code I used originally however it will provide the incorrect PE ratio, which is why I scrape it from CNBC. 

        def transform3(baguette):
            price = baguette.find('fin-streamer', {'class':"Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
            return price
        
        def transform4(baguette):
            eps = baguette.find('td', {'data-test':"EPS_RATIO-value"}).text.strip()
            return eps #this obtains some incorrect value which disagrees with multiple other sources

        c = extract(code) 
        share_price = float(transform3(c))
        eps = float(transform4(c))
        
        per = share_price/eps
        
        print(per)
      
      Yahoo Finance:
      
      <img width="468" alt="image" src="https://user-images.githubusercontent.com/87015101/187060046-6812ac11-ce1c-4146-afd9-73c5f1ac47ab.png">
      
      CNBC: 
      
      <img width="333" alt="image" src="https://user-images.githubusercontent.com/87015101/187059943-58b90d92-d2af-435c-9174-f04f3a3c594c.png">

      NASDAQ:
      
      <img width="910" alt="image" src="https://user-images.githubusercontent.com/87015101/187059969-5d6b78ff-17eb-4e8f-98f9-2017b00d2b18.png">
      
      I chose to scrape the PE ratio from CNBC directly as i) NASDAQ did not have the value and ii) even when using the formula to calculate the PE ratio, there are sometimes minute rounding errors.
     

