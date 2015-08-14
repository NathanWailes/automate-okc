import argparse
import simplejson
import sys
import time
import re
from selenium import webdriver

pause = 2

def main():
    cfg = get_cfg()

    browser = load_browser(cfg)

    browser.maximize_window()
    browser.get('https://www.okcupid.com/match')

    for age in range(19, 30):
        update_age(browser, age)
        time.sleep(pause)

        scroll_to_bottom_of_page(browser)
        scroll_to_top_of_page(browser)

    print("Done!")

def get_cfg():
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

def scroll_to_top_of_page(browser):
    browser.execute_script("window.scrollTo(0, 0)") # scroll to top of page



'''
elements = browser.find_elements_by_partial_link_text('Message')

element = elements[1]
element.click()

message_box = browser.find_element_by_xpath("//textarea[starts-with(@id, 'message_')]")
message_box.send_keys("Test message")

send_button = browser.find_element_by_xpath("//*[@id='global_messaging_container']/div/form/button")
send_button.click()










history_re = r'<td class="item"><a href="(.*)">'
history = set()
for match in re.findall(history_re, browser.page_source):
    history.add(match.strip('/'))

# Current menu
print("Retrieving menu...")
browser.get('https://myeatclub.com/menu/' + str(cfg.menu_number))
browser.implicitly_wait(1)
time.sleep(1)

# Parse menu
print("Processing menu...")
menu = []
elements = browser.find_elements_by_class_name('mi-infobox')
for element in elements:
    item = element.find_element_by_class_name('mi-item-name-link')
    link = item.get_attribute('href')
    link = link.replace('https://myeatclub.com', '', 1)
    link = link[:link.find('?')].strip('/')
    name = item.text
    rest = element.find_element_by_class_name('mi-restaurant-name')
    restaurant = rest.text
    ratings = element.find_elements_by_class_name('mi-i-stars-text')
    rating = ratings[-1].text
    tag_holder = element.find_element_by_class_name('mi-dish-tags')
    links = tag_holder.find_elements_by_css_selector('a')
    tags = map(lambda x: x.get_attribute('data-content'), links)
    add = element.find_element_by_class_name('mi-add-btn')
    if link not in history:
        menu.append((rating, name, restaurant, tags, add))

def filter_menu(menu, num_choices, cfg):
    menu = filter(lambda x: len(set(cfg.avoid_tag).intersection(set(x[3]))) == 0, menu)
    if cfg.require_tag:
        menu = filter(lambda x: all(t in x[3] for t in cfg.require_tag), menu)
    menu = filter(lambda x: x[2] not in cfg.avoid_restaurant, menu)
    return sorted(menu, key=lambda x: x[0], reverse=True)[:num_choices]

num_choices = 5
result = "Top %d choices:\n" % num_choices
new_menu = filter_menu(menu, num_choices, cfg)
for index, menu_item in enumerate(new_menu):
    if cfg.place_order and index == 0:
        print("Ordering " + menu_item[1])
        #menu_item[4].click()
        time.sleep(5)
        element = browser.find_element_by_class_name('checkout-btn')
        #element.click()
    result += str(index) + ". Rating: " + menu_item[0] + " " + menu_item[1] + " by " + menu_item[2] + " (" + ", ".join(menu_item[3]) + ")\n"
print(result)

if not cfg.preserve_browser:
    browser.quit()
'''


if __name__ == '__main__':
    main()