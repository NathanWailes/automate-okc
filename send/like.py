import time
from utils import get_config, load_browser

def main(username):
    cfg = get_config()
    browser = load_browser(cfg)

    browser.get('https://www.okcupid.com/profile/' + username)
    elements = browser.find_elements_by_xpath('//*[@id="rate_user_profile"]')
    print(elements)
    like_button = elements[0]
    time.sleep(1)
    like_button.click()

    print("Done!")

if __name__ == '__main__':
    test_username = 'okcupid1865'
    main(test_username)