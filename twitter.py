import json
import os
import StringIO
from twython import Twython

from flask import Flask, request


app = Flask(__name__)

with open('config.json') as data:
    config = json.load(data)

@app.route('/takeimage', methods=['GET'])
def take_image():
    os.system('imagesnap /Users/david/twitter.png')
    return json.dumps({'status': 'image taken'}), 200

@app.route('/deleteimage', methods=['GET'])
def delete_image():
    os.system('rm /Users/david/twitter.png')
    return json.dumps({'status': 'image deleted'}), 200

@app.route('/sendtotwitter', methods=['GET'])
def send_to_twitter():
    twitter = Twython(
        config['app_key'],
        config['app_secret'],
        config['oauth_token'],
        config['oauth_token_secret'])
    image = open('/Users/david/twitter.png', 'rb')
    tweet = twitter.update_status_with_media(
        status='Someone just came in.. #IntelmakerON #Scarecrow',
        media=image)
    return json.dumps({'status': 'sent to twitter'}), 200

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)
