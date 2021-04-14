from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    title_is,
    title_contains
)

url = 'https://selenium.dunossauro.live/aula_10_c.html'

browser = Firefox()

browser.get(url)

wdw = WebDriverWait(browser, 10)

links = browser.find_elements_by_css_selector('.body_b a')
links[1].click()

wdw.until(
    title_is('selenium') # verifica se o titulo da página é
)

wdw.until(
    title_contains('Aula 10b') # verifica se o titulo da página contem o elemento
)
