#! /usr/bin/env python

import os
import sys
import flask
from flask import render_template
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json


app = flask.Flask(__name__)


@app.route('/')
def index():
  credentials = json.load(open('../credentials.json'))
  chrome_options = Options()
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  d = webdriver.Chrome(chrome_options=chrome_options)
  d.get("https://www.instagram.com/accounts/login/")
  assert "Login" in d.title

  wait = WebDriverWait(d, 100)

  username = d.find_element_by_name('username').send_keys(credentials['username'])
  password = d.find_element_by_name('password').send_keys(credentials['password'])
  login_button = d.find_element_by_css_selector("._0mzm-.sqdOP.L3NKy")

  login_button.click()

  try:
    element = WebDriverWait(d, 7).until(
      EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'jaysonkadlecek')]"))
    )
  finally: 
    d.quit()

  return str(element.text)

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
