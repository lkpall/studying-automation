from selenium.webdriver import Firefox
from time import sleep

def find_by_text(browser, tag, text):
    elementos = browser.find_elements_by_tag_name(tag) # lista

    for elemento in elementos:
        if elemento.text == text:
            return elemento
        

browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_04_b.html')

nome_das_caixas = ['um', 'dois', 'tres', 'quatro']


for nome in nome_das_caixas:
    find_by_text(browser, 'div', nome).click()
for nome in nome_das_caixas:
    sleep(0.3)
    browser.back()
for nome in nome_das_caixas:
    sleep(0.3)
    browser.forward()
