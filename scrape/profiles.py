import json
import time
from utils import get_config, load_browser, download_image, create_dir

pause = 2

def main():
    cfg = get_config()
    browser = load_browser(cfg)

    with open('users_data.json', 'r') as f:
         users_data = json.load(f)
    usernames = users_data.keys()

    for username in usernames:
        if profile_has_been_scraped(users_data, username):
            continue
        else:
            update_users_data(browser, users_data, username)
    print("Done!")

def profile_has_been_scraped(users_data, username):
    if 'scraped' in users_data[username]:
        if users_data[username]['scraped'] == True:
            return True
    return False

def update_users_data(browser, users_data, username):
    browser.get('https://www.okcupid.com/profile/' + username)
    time.sleep(pause)
    if profile_doesnt_exist(browser):
        return
    current_user_data = get_user_data(browser, username)
    users_data[username] = current_user_data
    with open('users_data.json', 'w') as outfile:
        json.dump(users_data, outfile)

def profile_doesnt_exist(browser):
    try:
        find_elements_by_xpath('//*[@id="profile_bs"]/div/h2')
        return True
    except:
        return False

def get_user_data(browser, username):
    user_data = {}
    get_profile_photos(browser, username)
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

def get_profile_photos(browser, username):
    save_dir = 'profiles/' + username + '/'
    create_dir(save_dir) # need to fix these names
    i = 0
    for image in browser.find_elements_by_xpath('//div[@id="profile_thumbs"]//img[@src]'):
        image_url = image.get_attribute('src')
        save_path = save_dir + str(i) + '.webp' # probably a bad idea to assume the img format
        download_image(image_url, save_path)
        i += 1 # using 'i' is probably not the clean way to name these images

if __name__ == '__main__':
    main()