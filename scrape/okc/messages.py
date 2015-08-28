import json
import time
from automate-okc.utils import get_config, load_browser, download_image, create_dir, \
                  scroll_to_bottom_of_page

pause = 2

def main():
    cfg = get_config()
    browser = load_browser(cfg)

    browser.get('https://www.okcupid.com/messages')
    time.sleep(pause)

    scroll_to_bottom_of_page(browser)
    usernames = get_all_usernames(browser)
    print(usernames)

    print("Done!")

def get_all_usernames(browser):
    '''Should probably combine this with the similar function in scrape_usernames
    and move it into utils.py'''
    usernames = set()
    username_elements = browser.find_elements_by_class_name("subject")
    for username_element in username_elements:
        username = username_element.text
    return usernames

if __name__ == '__main__':
    main()