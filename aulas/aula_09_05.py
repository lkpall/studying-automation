from functools import partial
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class EsperarElemento:
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, webdriver):
        if webdriver.find_elements(*self.locator):
            return True
        return False

locator = (By.CSS_SELECTOR,'button')
esperar_botao = EsperarElemento(locator)

browser = Firefox()

url = 'https://selenium.dunossauro.live/aula_09_a.html'
wdw = WebDriverWait(browser, 20, poll_frequency=0.1)

browser.get(url)

wdw.until(esperar_botao, 'deu ruim')

btn = browser.find_element_by_css_selector('button')
btn.click()

wdw.until(EsperarElemento(locator=(id, 'finished')),
    'A mensagem de sucesso não apareceu'
    )

sucess = browser.find_element_by_css_selector('#finished') 
assert sucess.text == 'Carregamento concluído'
