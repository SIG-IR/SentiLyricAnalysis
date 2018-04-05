from bs4 import BeautifulSoup
from bs4.element import Tag
import requests
import json
import sys
import time
import os
import re

file_name = 'links.json'
song_urls = json.loads(open(file_name).read())

# Creates a 'websites' folder if it doesn't already exist.
if not os.path.exists('songs'):
    os.makedirs('songs')

# Dictionary stores song name as key and lyrics as value
lyrics = {}

requestCount = 0
for url in song_urls:
    page = ''
    while page == '':
        try:
            page = requests.get(url)
        except:
            time.sleep(5)
            continue
    # file_name is artist + song name
    file_name = 'songs/' + url[19:] + '.txt'
    # get html from URL
    html = page.text
    soup = BeautifulSoup(html, 'html5lib')
    # extract text from lyrics paragraph
    lyrics_div = soup.find_all('div', class_="lyrics")
    lyrics_p = lyrics_div[0].find('p')
    lyrics_text = lyrics_p.text
    # Remove [Verse], etc. labels
    lyrics_text = re.sub(r'(?is)\[.*?\]\n', '', lyrics_text)

    # Writes the lyrics to a '.txt' file.
    with open(file_name, 'w') as outfile:
        outfile.write(lyrics_text)

    # Extract song_name from url
    song_name = url[19:]
    # Create new dictionary entry for song lyrics
    lyrics[song_name] = lyrics_text
