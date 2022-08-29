# 🔭 Yahoo Finance Webscraping Project Documentation

<br>

## 💡 Purpose of this documentation

<br>

This documentation is written in place to:

- Guide anyone who needs to take over this project or reuse the code elsewhere 
- Help others understand key problems encountered and solutions engineered (to inspire problem solving for any future problems)
- Detail my reflections on possible improvements for next time and recommendations for future work 

<br>

## 🤔 Key errors encountered and engineered solutions (in chronological order)

<br>

N/A's were popping up in Excel for the PE Ratios, as Yahoo Finance doesn't report negative earnings. So if a PE Ratio was N/A, it was calculated by dividing Market Share Price by Earnings Per Share.[^bignote] 







NB: The Excel spreadsheet contains both the original scraped output in a sheet called 'Stocks' + a sheet containing manually checked data ready for analysis, i.e., comments/tickers were checked, outliers removed, amended tickers used.

<br>

## 🌱 What I would work on if I had more time... 

<br>

- Some code can be optimised further - I look forward to improving my best practices as I gain more professional experience. If I had more time here, I would:

  - Implement parallel processes to improve efficiency and scalability, i.e., open up 5 browsers at once to scrape 5 stocks at a time rather than one at a time

  - Figure out a way to store all the headless browsers used in the error handling by Selenium, so once the Excel file comes out I can resolve all comments one by one without having to search for all the stocks again   
  - Implement Python classes to improve functionality
  - Segregate different parts of the big loop to improve code reuseability 
  - Create initiator functions to reduce repeated lines of code
  - Implement better treatment of edge cases in error handling for compatability, simplicity and further error risk management (e.g. replace "." with "-" in tickers throwing up an error)
  - Make code more readable 

<br>

- I would future proof this project and upcoming projects by:

  - Moving code to cloud computing so it can run remotely as running the program takes a while (moving to cloud would help with parallel processing as well)

  - Starting projects from Github so full commit histories are visible 

<br>

## Final recommendations

<br>

- Recommendation 1: Change initial data source to a more reliable list of the S&P 500 which contains the correct tickers 

- Recommendation 2: Switch second data source to CNBC/NASDAQ given Yahoo Finance issues[^bignote]  
- Recommendation 3: Create even more robust error handling and monitor program performance over several days to gain more insight into further issues which can arise 

<br>

## Footnotes


[^bignote]: Initially, I calculated the PE ratio by scraping the market share price and earnings per share for the companies (then calculating their ratio to find the PE ratio) with negative earnings. However, Yahoo Finance actually reports a different EPS to CNBC, NASDAQ, WSJ, etc. for some reason (see images below). I ultimately decided if the PE ratio was "N/A" the first time around from Yahoo, then the program would scrape the PE ratio from CNBC directly as i) NASDAQ did not have the value and ii) even when using the formula to calculate the PE ratio using the official numbers, there are sometimes minute rounding errors.

      Yahoo Finance: stock data for NASDAQ:PEG as at 26 August. 
      
      <img width="468" alt="image" src="https://user-images.githubusercontent.com/87015101/187060046-6812ac11-ce1c-4146-afd9-73c5f1ac47ab.png">
      
      CNBC: different EPS to Yahoo.
      
      <img width="333" alt="image" src="https://user-images.githubusercontent.com/87015101/187059943-58b90d92-d2af-435c-9174-f04f3a3c594c.png">

      NASDAQ: same EPS as CNBC.
      
      <img width="910" alt="image" src="https://user-images.githubusercontent.com/87015101/187059969-5d6b78ff-17eb-4e8f-98f9-2017b00d2b18.png">

      I've included the code I originally used to complete this calculation, but it yields a PE ratio which obviously differs to all other sources:

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
     

