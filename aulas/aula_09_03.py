from functools import partial
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait

def esperar_elemento(elemento, webdriver):
    print(f'Tentando encontrar o {elemento}')
    if webdriver.find_elements_by_css_selector(elemento):
        return True
    return False

esperar_botao = partial(esperar_elemento, 'button')
esperar_sucesso = partial(esperar_elemento, '#finished')

browser = Firefox()

url = 'https://selenium.dunossauro.live/aula_09_a.html'
wdw = WebDriverWait(browser, 10, poll_frequency=0.1)

browser.get(url)

wdw.until(esperar_botao)

btn = browser.find_element_by_css_selector('button')
btn.click()

wdw.until(esperar_sucesso, 'A mensagem de sucesso não apareceu')

sucess = browser.find_element_by_css_selector('#finished') 
assert sucess.text == 'Carregamento concluído'
