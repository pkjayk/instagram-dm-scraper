#! /usr/bin/env python

import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json

with open('../credentials.json') as json_file:
    credentials = json.load(json_file)

chrome_options = Options()
#chrome_options.add_argument('--headless')
mobile_emulation = { "deviceName": "iPhone X" }
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
d = webdriver.Chrome('/Users/jaysonkadlecek/desktop/chromedriver 2', chrome_options=chrome_options)
d.get("https://www.instagram.com/accounts/login/")
assert "Login" in d.title

wait = WebDriverWait(d, 100)

username = d.find_element_by_name('username').send_keys(credentials['username'])
password = d.find_element_by_name('password').send_keys(credentials['password'])
login_button = d.find_element_by_xpath("//button[@type='submit']")

login_button.click()

try:
  element = WebDriverWait(d, 10).until(
    EC.presence_of_element_located((By.cssSelector(".mt3GC > button:nth-child(1)")))
  )
finally: 
  d.find_element_by_css_selector(".mt3GC > button:nth-child(1)").click()
  d.find_element_by_css_selector(".xWeGp").click()



print str(element.text)
