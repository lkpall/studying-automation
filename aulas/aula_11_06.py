from selenium.webdriver import Firefox
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support.expected_conditions import alert_is_present

browser = Firefox()

wdw = WebDriverWait(browser, 30)

browser.get('http://selenium.dunossauro.live/aula_11_b')

browser.current_window_handle 
#wids = browser.window_handles 

def find_window(url: str):
    wids = browser.window_handles
    for window in wids:
        browser.switch_to.window(window)
        if url in browser.current_url:
            break

find_window('duckduckgo')
