from selenium.webdriver import Firefox

def find_by_text(browser, tag, text):
    elementos = browser.find_elements_by_tag_name(tag) # lista

    for elemento in elementos:
        if elemento.text == text:
            return elemento
        

def find_by_href(browser, link):
    elementos = browser.find_elements_by_tag_name('a')
    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento

browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_04_a.html')

elemento_ddg = find_by_text(browser, 'a', 'DuckDuckGo')

elemento_ddg = find_by_href(browser, 'ddg')
