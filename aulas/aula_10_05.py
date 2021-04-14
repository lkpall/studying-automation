from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    staleness_of
)

url = 'https://selenium.dunossauro.live/aula_10_b.html'

browser = Firefox()

browser.get(url)

wdw = WebDriverWait(browser, 60)

element = browser.find_element_by_tag_name('button')
print(element.is_displayed()) # diz se o botao está visivel

try:
    wdw.until(staleness_of(element))
except:
    print(element.is_enabled()) # diz se o botao está ativo

element.click()

p = browser.find_element_by_tag_name('p')

assert 'quei' in p.text
