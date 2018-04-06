from pull_links import pull_links
from scrape_lyrics import scrape_lyrics
from vader_sentiment import getSentimentScores
import sys
import os
import shutil

# Get user input for artist -> capitalize it
artist = sys.argv[1].title()

pull_links(artist)
lyrics = scrape_lyrics('links.json')
os.remove('./links.json')
getSentimentScores(lyrics)
shutil.rmtree('./songs')
