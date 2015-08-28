import argparse
import os
import simplejson
import sys
import re
import requests
from selenium import webdriver
from selenium.webdriver.common import desired_capabilities
import time

pause = 2

def get_config():
    p = argparse.ArgumentParser()
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

    '''
    The code below is used for a headless browser. I can't get it to work at
    scraping usernames from OKC; it doesn't return any results. I'm guessing it
    has to do with OKC loading content on-the-fly instead of as a single page.
    On the other hand, it DOES seem to work at scraping profiles, which was one of
    the major motivations for using a headless browser.

    path_to_phantomjs = 'C:/Selenium/phantomjs-2.0.0-windows/bin/phantomjs.exe' # change path as needed
    capabilities = webdriver.DesiredCapabilities.PHANTOMJS.copy()
    capabilities["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (X11; Linux x86_64) "
                                                         "AppleWebKit/53 (KHTML, like Gecko) "
                                                         "Chrome/15.0.87")
    browser = webdriver.PhantomJS(executable_path = path_to_phantomjs, desired_capabilities = capabilities)
    '''
    browser = webdriver.Chrome() # use this when you want to _see_ the program working

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

def scroll_to_bottom_of_page(browser):
    last_height = browser.execute_script("return document.body.scrollHeight")
    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause)
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def scroll_to_top_of_page(browser):
    browser.execute_script("window.scrollTo(0, 0)") # scroll to top of page