from pull_links import pull_links
from scrape_lyrics import scrape_lyrics
from vader_sentiment import getSentimentScores
import sys
import os
import shutil

# Get user input for artist -> capitalize it
artist = sys.argv[1].title()

pull_links(artist)
# Dictionary w/ song name as key and lyrics as value
lyrics = scrape_lyrics('links.json')
os.remove('./links.json')
shutil.rmtree('./songs')
# Dictionary w/ song name as key and sentiment data as value
sentimentScores = getSentimentScores(lyrics)
# Print out sentimentScores
for song in sentimentScores:
    print(song + ': ')
    print(sentimentScores[song])
