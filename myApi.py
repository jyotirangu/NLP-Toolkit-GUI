# import paralleldots

# class API:
    
#     def __init__(self):
#         paralleldots.set_api_key('dd7e0218333da03d74f52e25af94f1f93d5a5885')

#     def sentimental_analysis(self,text):
#         response = paralleldots.sentiment(text)
#         return response



# myApi.py

from pysentimiento import create_analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import spacy

nlp = spacy.load("en_core_web_md")
sentiment_analyzer = create_analyzer(task="sentiment", lang="en")
emotion_analyzer = create_analyzer(task="emotion", lang="en")
vader = SentimentIntensityAnalyzer()

class API:
    def sentiment(self, text):
        return sentiment_analyzer.predict(text)

    def emotion(self, text):
        return emotion_analyzer.predict(text)

    def vader_sentiment(self, text):
        return vader.polarity_scores(text)

    def ner(self, text):
        doc = nlp(text)
        return [(ent.text, ent.label_) for ent in doc.ents]
