import time
from utils import get_config, load_browser

pause = 2

def main():
    cfg = get_config()
    browser = load_browser(cfg)
    browser.maximize_window()
    browser.get('https://www.okcupid.com/match')

    usernames = set()
    for age in range(19, 30):
        update_age(browser, age)
        time.sleep(pause)

        scroll_to_bottom_of_page(browser)

        new_usernames = get_all_usernames(browser)
        usernames = usernames | new_usernames

        scroll_to_top_of_page(browser)

    print("Done!")

def update_age(browser, age):
    age_selection_link = browser.find_element_by_xpath('//*[@id="match-status"]/span[5]/a')
    age_selection_link.click()

    time.sleep(pause)
    min_age_input_box = browser.find_element_by_css_selector('#match-status > span.filter-wrapper.filter-age > div > div.contents > input[type="text"]:nth-child(2)')
    min_age_input_box.clear()
    min_age_input_box.send_keys(str(age))

    max_age_input_box = browser.find_element_by_xpath('//*[@id="match-status"]/span[5]/div/div[1]/input[2]')
    max_age_input_box.clear()
    max_age_input_box.send_keys(str(age))

    age_selection_link.click()

def scroll_to_bottom_of_page(browser):
    last_height = browser.execute_script("return document.body.scrollHeight")
    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause)
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def get_all_usernames(browser):
    usernames = set()
    username_elements = browser.find_elements_by_class_name("name")
    for username_element in username_elements:
        username = username_element.text
        print(username)

    return usernames

def scroll_to_top_of_page(browser):
    browser.execute_script("window.scrollTo(0, 0)") # scroll to top of page

if __name__ == '__main__':
    main()