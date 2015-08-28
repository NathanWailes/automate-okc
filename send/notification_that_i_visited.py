import time
from utils import get_config, load_browser

def main():
    cfg = get_config()
    browser = load_browser(cfg)
    #browser.maximize_window()

    browser.get('https://www.okcupid.com/profile/okcupid1865')


    ''' Need to update the stuff below
    elements = browser.find_elements_by_partial_link_text('Message')

    element = elements[1]
    element.click()

    message_box = browser.find_element_by_xpath("//textarea[starts-with(@id, 'message_')]")
    message_box.send_keys("Test message")

    send_button = browser.find_element_by_xpath("//*[@id='global_messaging_container']/div/form/button")
    '''

    send_button.click()
    print("Done!")

if __name__ == '__main__':
    main()