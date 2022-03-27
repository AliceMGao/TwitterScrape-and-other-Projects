import json
import pandas as pd
import matplotlib.pyplot as plt
import os
import re
# path for windows
tweets_data_path = os.getcwd()+'\\twitter_data.txt'

# path for os
# tweets_data_path = os.getcwd()+'/twitter_data.txt'
# print (tweets_data_path)

# grab search terms
search_terms_file_name = 'Search-terms.txt'
search_terms_file = open(search_terms_file_name, 'r')
search_terms = [line.lower().strip() for line in search_terms_file.readlines()]
# print(search_terms)

# fn for word in text
def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

# twitter array
tweets_array = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_array.append(tweet)
    except:
        continue

print(len(tweets_array))

tweets = pd.DataFrame()

# # The OLD way, that produces an error because map now returns an itertor, not a list:
# # tweets['text'] = map(lambda tweet: tweet['text'], tweets_array)

# The NEW way that fixes it by converting it to a list:
tweets['text'] = list(map(lambda tweet: tweet['text'], tweets_array))

# assigning  tweets based on search match, printing out crude tweet counts, and appending values to
# list of tweets by cancer type
tweets_by_cancer_type = []
for i in range(len(search_terms)):
    tweets[search_terms[i]] = tweets['text'].apply(lambda tweet: word_in_text(search_terms[i], tweet))
    print(tweets[search_terms[i]].value_counts()[True])
    tweets_by_cancer_type.append(tweets[search_terms[i]].value_counts()[True])
# print(tweets_by_cancer_type)

# establishing categories
cancer_type = search_terms

# plotting details
x_pos = list(range(len(cancer_type)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_cancer_type, width, alpha=1, color='g')

# Setting axis labels and ticks
ax.set_ylabel('Number of tweets', fontsize=8)
ax.set_title('Ranking of cancer types (Raw data)', fontsize=10, fontweight='bold')
ax.set_xticks([p-0.1 for p in x_pos])
ax.set_xticklabels(cancer_type, fontsize=6)
plt.grid(linestyle=':')

# Saving the graph
plt.savefig('alice-barchart.png​',
            pad_inches=0.5,
            format='png',
            orientation = 'landscape')
