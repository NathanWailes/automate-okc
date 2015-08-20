import argparse
import os
import simplejson
import sys
import re
import requests
from selenium import webdriver

def get_config():
    p = argparse.ArgumentParser()
    p.add_argument('--avoid-tag', default=[], action='append')
    p.add_argument('--require-tag', default=[], action='append')
    p.add_argument('--avoid-restaurant', default=[], action='append')
    p.add_argument('--place-order', action='store_true')
    p.add_argument('--preserve-browser', action='store_true')
    p.add_argument('--menu-number', default=1)
    p.add_argument('--cookies-path', default='okc_cookies')
    cfg = p.parse_args(sys.argv[1:])
    return cfg

def load_browser(cfg):
    # Load cookies
    print("Loading cookies...")
    with open(cfg.cookies_path) as c:
        cookies = simplejson.load(c)
        phantomjs_cookies = []
        for key, val in cookies.items():
            phantomjs_cookies.append({"name": key, "value": val, "domain": "okcupid.com"})

    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get('https://www.okcupid.com')
    for cookie in phantomjs_cookies:
        browser.add_cookie(cookie)
    return browser

def download_image(image_url, save_path):
    f = open(save_path,'wb')
    f.write(requests.get(image_url).content)
    f.close()

def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)