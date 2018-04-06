from bs4 import BeautifulSoup
from bs4.element import Tag
from bs4.element import NavigableString
import requests
import json
import sys

def pull_links(artist):
    # URL for search results for artist on AZLyrics
    search_url = 'https://genius.com/artists/' + artist
    # Get webpage (Response object) with URL
    search_results = requests.get(search_url)
    # Get text (HTML) from webpage, convert to BeautifulSoup object
    search_results_html = search_results.text
    soup = BeautifulSoup(search_results_html, 'html5lib')

    # Get all <a> tags with class mini_card
    song_listings = soup.find_all('a', class_="mini_card")
    links_file = open('links.json', 'w')
    links_file.write('[')
    first = True
    # Write URLs to links.json
    for x in song_listings:
        link = x['href']
        if first:
            links_file.write('\n\t\"' + link + '\"')
            first = False
            continue
        links_file.write(',\n\t\"' + link + '\"')
    links_file.write('\n]')
