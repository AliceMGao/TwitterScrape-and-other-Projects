# TwitterScrape-and-other-Projects

This project included 2 major deliverables I created from python in conjunction with Twitter API and Html:
* Python program working with Twitter API designed to web scrape mentions of different types of cancer, process the raw data generated at the time of running the application, then analyze, and graph the frequency of each term used. Files essential to it include:
  * <a href= "https://github.com/AliceMGao/TwitterScrape-and-other-Projects/blob/28b02e15b083b2f585e97664c359f35573f65bf8/twitter-miner.py">twitter-miner.py</a>
  * <a href= "https://github.com/AliceMGao/TwitterScrape-and-other-Projects/blob/28b02e15b083b2f585e97664c359f35573f65bf8/analyze-tweets.py">analyze-tweets.py</a>
  * <a href= "https://github.com/AliceMGao/TwitterScrape-and-other-Projects/blob/28b02e15b083b2f585e97664c359f35573f65bf8/Search-terms.txt">Search-terms.txt</a>
* Python program that works to extract data from encounters from a CSV file, parse them into JSON, analyze, and aggregate total counts of clinical encounters in a monthly and yearly summary, rendering results in Html and emailing to a designated account. Files essential to it include:
  * <a href= "https://github.com/AliceMGao/TwitterScrape-and-other-Projects/blob/28b02e15b083b2f585e97664c359f35573f65bf8/IMS-testing.py">IMS-testing.py</a>
  * <a href= "https://github.com/AliceMGao/TwitterScrape-and-other-Projects/blob/28b02e15b083b2f585e97664c359f35573f65bf8/ims-report-creator.py">ims-report-creator.py</a>
  * <a href= "https://github.com/AliceMGao/TwitterScrape-and-other-Projects/blob/28b02e15b083b2f585e97664c359f35573f65bf8/ims-report-creator_self_email.py">ims-report-creator_self_email.py</a>

All relevant data collected from previously running the Twitter miner application and the CSV for the project are included in the zip file: <a href="https://github.com/AliceMGao/TwitterScrape-and-other-Projects/blob/504df220da402d86b446a82de514a6d837cd492a/TwitterScrape_andCancerFrequencyVisualization.zip">TwitterScrape_andCancerFrequencyVisualization.zip.</a> Below is a gif preview of what it looks like in the browser after extracting all files and opening the Html page to navigate API results.
<img src='TwitterScrape_Cancer.gif' width='1220'>

This project was interesting in that it connected different programming, data analysis, and web API training I completed during coursework, fully bringing together programming tools in python like matplotlib, pandas, and coding for HTML, JSON, and 3rd party API providers (Twitter, Gmail) to create an interesting data visualization API that’s customizable to a specific use case for reporting and analysis. 

Frequent testing, iterative development scaling up on small segments of performing code was important in the success of the applications in collecting information and parsing it into usable data, practices I learned core in any research or web API project based on a large volume of raw data.

# Disclaimer
All clinical encounter data used for this project is fictional, and data scraped from Twitter is within stipulations of Twitter’s API policy. Raw data is not human readable, and only aggregated results are shown in the generated bar chart which does not present any identifying information.
