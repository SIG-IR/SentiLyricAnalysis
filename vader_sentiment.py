"""
VADER sentiment analysis tools:
    Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
    Sentiment Analysis of Social Media Text. Eighth International Conference on
    Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.

"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

# Assuming we have a list of lyrics sorted chronologically
# Returns a dictionary of Lyrics and their sentiment weights
def getSentimentScores(lyrics):
    sentimentScores = {}
    for song in lyrics:
        # Puts the song as key and the sentiment score as value
        sentimentScores[song] = analyzer.polarity_scores(lyrics[song])
    return sentimentScores
