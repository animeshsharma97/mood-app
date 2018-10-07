import json
import requests
import sys
import tweepy, time
import watson_developer_cloud

from base64 import b64encode
from datetime import datetime

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic, QtCore

from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EmotionOptions

from app_ui import Ui_MainWindow

# Enter all the API credentials here
spotify_client_id = ''
spotify_client_secret = ''

twitter_ckey = ''
twitter_csecret = ''
twitter_atoken = ''
twitter_asecret = ''

ibm_username = ''
ibm_password = ''

# base64 encoding the 'client_id:client_secret' of Spotify Public API for generating the access token
s = str.encode('{}:{}'.format(spotify_client_id, spotify_client_secret))
encoded = b64encode(s).decode("utf-8")

# authentication for using Twitter API
auth = tweepy.OAuthHandler(twitter_ckey, twitter_csecret)
auth.set_access_token(twitter_atoken, twitter_asecret)
api = tweepy.API(auth)

# IBM Watson Natural Language Understanding Service module
natural_language_understanding = NaturalLanguageUnderstandingV1(
    username=ibm_username,
    password=ibm_password,
    version='2018-03-16')

# A curated list of messages and playlists for each emotion.
music_dict = {
    'sadness' : {'message': "It seems you are feeling down. Here's something to help cheer you up.",
            'emotion': 'happy',
            'link': "https://www.youtube.com/watch?v=MoHnffhBwqs&list=RDMoHnffhBwqs&start_radio=1"},

    'anger': {'message': "You seem to be in a bit of a temper. Here's something to calm you down.",
            'emotion': 'relaxing',
            'link': "https://www.youtube.com/watch?v=3AtDnEC4zak&list=PL4QNnZJr8sRNzSeygGocsBK9rVXhwy9W4"},

    'fear': {'message': "Oh no! It seems you're feeling a little insecure. Keep your chin up and listen to these!",
            'emotion': 'motivational',
            'link': "https://www.youtube.com/watch?v=hT_nvWreIhg&list=PLhGO2bt0EkwvRUioaJMLxrMNhU44lRWg8"},

    'joy': {'message': "We sense great vibes from you! Keep rocking!",
            'emotion': 'pop',
            'link': "https://www.youtube.com/watch?v=aJOTlE1K90k&list=PLMC9KNkIncKtGvr2kFRuXBVmBev6cAJ2u"},

    'disgust': {'message': "Let those bad feelings out with these awesome songs.",
            'emotion': 'positive',
            'link': "https://www.youtube.com/watch?v=xo1VInw-SKc&list=PLQWho9PxKfJR7MJeW0maer5eg7BczFVBU"}
}


class MyApp(QMainWindow):
    '''
    Class which returns the UI alongwith the logic implemented for the same.
    '''

    def __init__(self):
        super(MyApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.name = ''
        self.username = ''
        self.result_yes = ''
        self.result_no = ''
        self.ui.Button.clicked.connect(self.detect_emotion)
        self.ui.YesButton.clicked.connect(self.spotify_yes)
        self.ui.NoButton.clicked.connect(self.spotify_no)

    def get_tweets(self, api):
        '''
        Get the tweets for a particular Twitter handle.
        '''

        self.ui.resultWindow.setText('')
        self.ui.resultWindow2.setText('')
        page = 1
        tweet_list = []
        while True:
            try:
                tweets = api.user_timeline(self.username, page=page)
                if not tweets:
                    return tweet_list
                for tweet in tweets:
                    if (datetime.now() - tweet.created_at).days < 1:
                        tweet_list.append(tweet.text)
                        self.name = tweet.user.name
                    else:
                        return tweet_list
                page += 1
                time.sleep(5)
            except tweepy.error.TweepError as e:
                return "{}".format(e)

    def spotify_yes(self):
        '''
        Get the results when the user has a Spotify account.
        '''

        if self.result_yes == '' or self.username == '':
            result = '**Please enter a valid Twitter Handle first!'
            self.ui.resultWindow.setText(result)

        else:
            self.ui.resultWindow2.setText(self.result_yes)
            self.ui.resultWindow2.setOpenExternalLinks(True)

    def spotify_no(self):
        '''
        Get the results when the user doesn't have a Spotify account.
        '''

        if self.result_no == '' or self.username == '':
            result = '**Please enter a valid Twitter Handle first!'
            self.ui.resultWindow.setText(result)
        else:
            self.ui.resultWindow2.setText(self.result_no)
            self.ui.resultWindow2.setOpenExternalLinks(True)

    def get_urls(self, emotion):
        '''
        Get the urls of playlists for an emotion.
        '''

        auth_url = 'https://accounts.spotify.com/api/token'
        headers = {
            'Content-type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic {}'.format(encoded)
        }
        data = {'grant_type': 'client_credentials'}

        r = requests.post(auth_url, data=data, headers=headers)
        access_token = r.json().get('access_token', None)

        spotify_url = 'https://api.spotify.com/v1/search'
        params = {
            'q': '{}'.format(emotion),
            'type': 'playlist',
            'limit': '5'
        }
        headers = {
            'Content-type': 'application/json',
            'Authorization': 'Bearer {}'.format(access_token)
        }

        r = requests.get(spotify_url, params=params, headers=headers)
        items = r.json().get('playlists').get('items', None)
        if items:
            url_list = [item['external_urls']['spotify'] for item in items]
        return url_list

    def detect_emotion(self):
        '''
        Function which is called after clicking the 'Know your mood' button on UI which then displays some appropriate message
        '''
        
        self.username = self.ui.twitter_name.text()
        if self.username == '':
            self.ui.resultWindow.setText('')
            self.ui.resultWindow2.setText('')
            result = """<html><body>
                        <p>**Please enter a valid Twitter Handle first!</p> 
                        </body></html>"""
            self.ui.resultWindow.setText(result)

        else:
            tweet_list = self.get_tweets(api)
            if isinstance(tweet_list, str):
                self.result_no, self.result_yes = '', ''
                result = """<html><body>
                            <p>**Error while extracting tweets from this Twitter handle!</p> 
                            <p>Please try another Twitter handle or check your Internet connection.</p>
                            </body></html>"""
                result = result.format(error=tweet_list)
                self.ui.resultWindow.setText(result)

            elif tweet_list:
                result_dict = {}
                try:
                    for tweet in tweet_list:
                        response = natural_language_understanding.analyze(
                        text=tweet,
                        features=Features(
                        emotion=EmotionOptions())).get_result()
                        
                        emotion_dict = response['emotion']['document']['emotion']
                        emotion = max(emotion_dict.keys(), key=(lambda key: emotion_dict[key]))

                        if result_dict.get(emotion, None):
                            result_dict[emotion] += 1
                        else:
                            result_dict[emotion] = 1

                    dominant_emotion = max(result_dict.keys(), key=(lambda key: result_dict[key])) if result_dict else None
                    
                    result = """<html><head></head><body>
                            <p>Hi <strong>{name}!</strong> Your dominant emotion is : {emotion}</p>
                            <p>We would like to suggest some music for you...</p>
                            </body></html>
                            """
                    result = result.format(name=self.name, emotion=dominant_emotion)
                    self.ui.resultWindow.setText(result)

                    playlist = music_dict[dominant_emotion]
                    url_list = self.get_urls(playlist['emotion'])
                    links = []
                    for i in range(len(url_list)):
                        links.append("<p><a href='{}'> Playlist {}</a></p>".format(url_list[i], i+1))
        
                    links = "".join(links)
                    self.result_yes = """<html><head></head><body>
                                <p>{msg}</p>
                                {links}
                                </body></html>"""
                    self.result_yes = self.result_yes.format(msg=playlist['message'], links=links)
                
                    self.result_no = """<html><head></head><body>
                                    <p> No worries! We have a playlist on YouTube waiting for you! </p>
                                    <p> <a href="{link}"> Your Playlist </a></body></html>"""
                    self.result_no = self.result_no.format(link=playlist['link'])
            
                except (watson_developer_cloud.watson_service.WatsonApiException, requests.exceptions.ConnectionError) as e:
                    self.ui.resultWindow.setText('')
                    self.ui.resultWindow2.setText('')
                    self.result_no, self.result_yes = '', ''
                    if str(e).startswith("('Connection aborted"):
                        result = """<html><body>
                                <p>**Please check your Internet connection!</p>
                                </body></html>"""
                    else:
                        result = """<html><body>
                                <p>Unsupported text language in one of the tweets of <strong>{name}</strong></p>
                                </body></html>"""
                    result = result.format(name=self.name)
                    self.ui.resultWindow.setText(result)
            else:
                self.ui.resultWindow.setText('')
                self.ui.resultWindow2.setText('')
                self.result_no, self.result_yes = '', ''
                result = """<html><body>
                            <p>No tweets found for Twitter handle <strong>{name}</strong> in the last 24 hours.</p>
                            </body></html>"""
                result = result.format(name=self.username)
                self.ui.resultWindow.setText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
