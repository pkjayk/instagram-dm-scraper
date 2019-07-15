#! /usr/bin/env python

import os
import flask
from flask import render_template
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


app = flask.Flask(__name__)


@app.route('/')
def index():
  print('test 1234')
  chrome_options = Options()
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  d = webdriver.Chrome(chrome_options=chrome_options)
  d.get("https://instagram.com")
  assert "Instagram" in d.title
  textblock = d.find_element_by_class_name('vvzhL').text

  return str(textblock)

''' 
    TODO: Put in separate class
    1: Allow user to select a thread
    2: Track thread
    3: Use long-polling feature Google provides to track new thread message
    4: Send push notification when thread has update or create a task? (Will need a DB)
'''

if __name__ == '__main__':
  # When running locally, disable OAuthlib's HTTPs verification.
  # ACTION ITEM for developers:
  #     When running in production *do not* leave this option enabled.
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

  # Specify a hostname and port that are set as a valid redirect URI
  # for your API project in the Google API Console.
  app.run(debug = True, host='0.0.0.0', port=80)
