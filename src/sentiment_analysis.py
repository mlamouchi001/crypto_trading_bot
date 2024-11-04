# src/sentiment_analysis.py
import tweepy
from transformers import pipeline
from config.config import TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET, PAIR

# Initialisation de l'analyseur de sentiment
sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# Authentification Twitter
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

def fetch_social_data(pair):
    """
    Récupère les tweets récents pour la cryptomonnaie spécifiée.

    Parameters:
        pair (str): La paire de trading, par exemple 'BTC/USDT'.

    Returns:
        list: Une liste de tweets en texte brut.
    """
    # Utilisez le nom de la crypto pour rechercher des tweets
    query = pair.split('/')[0]  # Extrait le nom de la crypto (ex: 'BTC' de 'BTC/USDT')
    tweets = []
    
    try:
        for tweet in tweepy.Cursor(api.search_tweets, q=query, lang="en", tweet_mode="extended").items(10):  # Récupère les 10 derniers tweets
            tweets.append(tweet.full_text)
    except tweepy.TweepError as e:
        print(f"Erreur lors de la récupération des tweets: {e}")
    
    return tweets

def analyze_advanced_sentiment(tweets):
    """
    Analyse le sentiment d'une liste de tweets.

    Parameters:
        tweets (list): Liste de textes de tweets.

    Returns:
        float: Score moyen de sentiment.
    """
    results = sentiment_analyzer(tweets)
    sentiment_scores = []
    
    for result in results:
        label = result['label']
        score = result['score']
        
        # Conversion des labels de sentiment en scores
        if label == '1 star':
            sentiment_scores.append(-2 * score)
        elif label == '2 stars':
            sentiment_scores.append(-1 * score)
        elif label == '3 stars':
            sentiment_scores.append(0)
        elif label == '4 stars':
            sentiment_scores.append(1 * score)
        elif label == '5 stars':
            sentiment_scores.append(2 * score)
    
    # Calcul du score moyen
    return sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0
