import json
import time
from utils import get_config, load_browser

pause = 2

def main():
    cfg = get_config()
    browser = load_browser(cfg)
    #browser.maximize_window()

    with open('users_data.json', 'r') as f:
         users_data = json.load(f)
    usernames = users_data.keys()

    for username in usernames:
        if ('scraped' in users_data[username]) and users_data[username]['scraped'] == True:
            continue
        else:
            print(users_data[username])
            browser.get('https://www.okcupid.com/profile/' + username)
            time.sleep(pause)
            #last_online = browser.find_elements_by_xpath('//span[starts-with(@id, "fancydate_")]')
            #print(last_online)

            current_user_data = get_user_data(browser)
            users_data[username] = current_user_data
            print(current_user_data)
            with open('users_data.json', 'w') as outfile:
                json.dump(users_data, outfile)
    print("Done!")

def get_user_data(browser):
    user_data = {}
    attributes = ['orientation', 'height', 'bodytype', 'smoking', 'drinking', \
                  'drugs', 'religion', 'sign', 'education', 'job', 'income', \
                  'status', 'pets', 'language']
    for attribute in attributes:
        try:
            css_selector = '#ajax_' + attribute
            user_data[attribute] = browser.find_element_by_css_selector(css_selector).text
        except:
            continue
    user_data["scraped"] = True
    return user_data

if __name__ == '__main__':
    main()