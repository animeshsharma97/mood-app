# mood-app

A Desktop app to suggest a playlist of songs based on user's mood derived from their tweets.

In this project, we have created a Desktop app where a user enters their twitter handle, then we extract their tweets for the last 24 hours and pass each tweet to the IBM Watson Natural Language Understanding Service to extract the emotion of those tweets, i.e. joy, sadness, anger, fear, disgust. Then we extract the dominant emotion of all the tweets. After that, we suggest a curated playlist of songs to the user based on their dominant mood.

To run this app, first of all you must install all the dependencies in your virtual environment. For that, run the following commands:

```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

Then you can make a standalone app using the command:

```
pyinstaller --onefile '/path/to/MyApp.py'
```

This creates some folders in the folder that you have run the previous command. The app is stored in the dist folder by the name of the original .py file of the app.
Run that file to see some awesome results.

![shade_app](https://user-images.githubusercontent.com/32910261/46581923-b14a3580-ca5d-11e8-8a57-e1864ecfd844.png)

![playlist1](https://user-images.githubusercontent.com/32910261/46581938-d474e500-ca5d-11e8-9360-7b6c3486b989.png)

# A preview of our UI:

<a href="http://www.youtube.com/watch?feature=player_embedded&v=klpPTeLnX60
" target="_blank"><img src="http://img.youtube.com/vi/klpPTeLnX60/0.jpg" 
alt="The video could not be loaded." width="500" height="300" border="10" /></a>

# Undertaking
We undertake that all our work is original and has not been copied or plagiarised from anywhere.
