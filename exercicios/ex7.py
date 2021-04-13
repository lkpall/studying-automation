from selenium.webdriver import Firefox
from selenium.webdriver.support.events import (AbstractEventListener, EventFiringWebDriver)
from time import sleep

class Escuta(AbstractEventListener):
    def before_click(self, elemento, webdriver):
        if elemento.tag_name == 'label':
            print(webdriver.find_element_by_tag_name('label').text)
        print(f'antes do click no {elemento.tag_name}')
    def after_click(self, elemento, webdriver):
        if elemento.tag_name == 'label':
            print(webdriver.find_element_by_tag_name('label').text)
        print(f'depois do click no {elemento.tag_name}')

def preencher_form(browser, id, valor, id_label):
    this_id = f'input[id="{id}"'
    this_id_label = f'label[id="{id_label}"'
    input_nome = browser.find_element_by_css_selector(this_id)
    input_nome.send_keys(valor)
    sleep(1)
    label = browser.find_element_by_css_selector(this_id_label)
    label.click()

browser = Firefox()

rapi_browser = EventFiringWebDriver(browser, Escuta())

rapi_browser.get('https://selenium.dunossauro.live/exercicio_07')

sleep(1)
preencher_form(rapi_browser, 'nome', 'Matheus', 'lnome')
preencher_form(rapi_browser, 'email', 'mfp186@hotmail.com', 'lemail')
preencher_form(rapi_browser, 'senha', '23456', 'lsenha')

button = browser.find_element_by_css_selector('input[id="btn"]')
button.click()

#browser.quit()
