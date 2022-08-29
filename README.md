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

This section doubles up as a walk through of why I made certain decisions in my code as well as an explanation of my error treatments.  

Firstly, I did not encounter any errors when scraping the first website for the S&P 500 list (`component A` in the code).

<br>

1. The first error I encountered was in `component B`, where some tickers would not load into the Yahoo Finance URL, either due to the ticker from the first website not matching what is in Yahoo Finance or something going wrong in the back end (404 error). For example, the first website had Berkshire Hathaway Class B's ticker as `BRK.B` when it was actually `BRK-B` on Yahoo Finance. 

    - In this case, I introduced the first layer of error treatment in `component C_1`; if the ticker did not load I instructed the code to search up the first two words of the respective company's name in Yahoo Finance's search box, click on the first result (since search results are returned in order of weight) then scrape the data from there, as well as the actual ticker of the stock. 
    
    - Sometimes there was a mismatch between the stock name and company name, so I added another step to this layer called `component C_2`; if searching up the first two words of the company name did not work, the code searches up only the first word.

    - If there are cases which still bypass both these error treatments, they enter `component E`. It is likely data entering this error treatment is an outlier, so I simply flag such observations as needing further investigation. 

<br>

2. The next error I encountered was the fact that Yahoo Finance doesn't report negative earnings, instead reporting an `N/A`. This meant the PE ratio for companies with negative earnings were unreported in the excel file. 

    - To resolve this issue I added `component D` in the code; if an originally scraped PE ratio was `N/A`, I redirected the scraper to CNBC. I then scraped the PE ratio from CNBC directly[^bignote] 
      
<br>

For these error treatments, if the error did occur and my solution was implemented, I added a comment to the spreadsheet. This way I can easily manually check off potentially incorrect observations.

NB: There are two .csv files in the GitHub repo; one is the original scraped output and the other 'cleaned' version contains manually checked data ready for analysis, i.e., comments/tickers were checked, outliers removed, amended tickers used.

<br>

Some other notable (but smaller) errors:
<br>

- Selenium would sometimes return a `'NoneType' object has no attribute 'text'`, which I resolved by adding a bunch of time.sleep() commands

- Another error I got was `unknown error: cannot determine loading status`, which I fixed by installing the latest version of Chrome and the Chrome driver (I even got Chrome Beta for this)  
- At times there are repeated spans or lists with no real differentiating classes or ID's. In this case, I found learning Xpaths handy, e.g., appending `\ul\span[2]` to reach the second span of an unordered list in a `div` that does have a class or ID 
- The .csv output initially stored numbers as a string, so I used `int()` or `float()` to convert all numbers stored as strings to actual integers or real numbers, respectively. 
- Both Beautiful Soup and Selenium have their strengths and weaknesses. Notably Beautiful Soup cannot use Xpaths. I found learning both to be helpful in adaptability. 


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

  - Create some sort of macro which asks the user for all necessary information such as user agents, then runs by itself (so any analyst can run this code quickly from their computer)

  - Moving code to cloud computing so it can run remotely as running the program takes a while (moving to cloud would help with parallel processing as well)
  - Starting projects from GitHub so full commit histories are visible (I only moved this project onto GitHub after a substantial period of time) 
  - Improve script to generate new Excel output files when it is run again rather than overwriting the previous output file, or store new outputs in a new sheet in the same Excel file, e.g. adding date suffix to file names or something

<br>

## Final recommendations

<br>

1. Change initial data source to a more reliable list of the S&P 500 which contains the correct tickers 

2. Switch second data source to CNBC/NASDAQ given Yahoo Finance issues[^bignote]  
3. Create even more robust error handling and monitor program performance over several days to gain more insight into further issues which can arise 

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
     

