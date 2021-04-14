from functools import partial
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def esperar_elemento(by, elemento, webdriver):
    print(f'Tentando encontrar o {elemento} by {by}')
    if webdriver.find_elements(by, elemento):
        return True
    return False

esperar_botao = partial(esperar_elemento, By.CSS_SELECTOR,'button')

browser = Firefox()

url = 'https://selenium.dunossauro.live/aula_09_a.html'
wdw = WebDriverWait(browser, 20, poll_frequency=0.1)

browser.get(url)

wdw.until(esperar_botao, 'deu ruim')

btn = browser.find_element_by_css_selector('button')
btn.click()

wdw.until(partial(esperar_elemento, By.ID, 'finished'), 'A mensagem de sucesso não apareceu')

sucess = browser.find_element_by_css_selector('#finished') 
assert sucess.text == 'Carregamento concluído'
