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

- Some areas of code can be refined to follow best practices - I look forward to improving my practices further as I gain more experience. If I had more time here I would:
  - Implement Python classes
  - Add even more comments
  - Make code more readable 
  - Figure out a way to segregate different parts of the functions to improve code reuseability 
  - Try to create even more robust error handling and implement better edge cases for compatability and simplicity 
            


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
     

