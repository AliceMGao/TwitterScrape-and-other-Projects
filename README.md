# TwitterScrape-and-other-Projects

This project included 2 major deliverables I created from python in conjunction with Twitter API and Html:
* Python program working with Twitter API designed to web scrape mentions of different types of cancer, process the raw data generated at the time of running the application, then analyze, and graph the frequency of each term used. Files essential to it include:
  *twitter-miner.py
  *analyze-tweets.py
  *Search-terms.txt
* Python program that works to extract data from encounters from a CSV file, parse them into JSON, analyze, and aggregate total counts of clinical encounters in a monthly and yearly summary, rendering results in Html and emailing to a designated account. Files essential to it include:
  * IMS-testing.py
  * ims-report-creator_self_email.py

All relevant data collected from previously running the Twitter miner application and the CSV for the project are included in the zip file: TwitterScrape_andCancerFrequencyVisualization.zip. Below is a gif preview of what it looks like in the browser after extracting all files and opening the Html page to navigate API results.
<img src='TwitterScrape_Cancer.gif' width='1220'>

This project was interesting in that it connected different programming, data analysis, and web API training I completed during coursework, fully bringing together programming tools in python like matplotlib, pandas, and coding for HTML, JSON, and 3rd party API providers (Twitter, Gmail) to create an interesting data visualization API that’s customizable to a specific use case for reporting and analysis. 
Frequent testing, iterative development scaling up on small segments of performing code was important in the success of the applications in collecting information and parsing it into usable data, practices I learned core in any research or web API project based on a large volume of raw data.

# Disclaimer
All clinical encounter data used for this project is fictional, and data scraped from Twitter is within stipulations of Twitter’s API policy. Raw data is not human readable, and only aggregated results are shown in the generated bar chart which does not present any identifying information.
