from selenium.webdriver import Firefox
from time import sleep

def preencher_forms(browser, form):
    junt_nome = form + ' input[name="nome"]'
    nome = browser.find_element_by_css_selector(junt_nome)
    nome.send_keys('Matheus')
    junt_senha = form + ' input[name="senha"]'
    senha = browser.find_element_by_css_selector(junt_senha)
    senha.send_keys('123456789')
    junt_button = form + ' input[type="submit"]'
    button = browser.find_element_by_css_selector(junt_button)
    button.click()

b = Firefox()

url = 'http://selenium.dunossauro.live/exercicio_06.html'

b.get(url)
sleep(1)

for cont in range(0, 6):
    p = b.find_elements_by_css_selector('p ~ p > span')
    span = p[0].text
    form = ".form-"+span
    preencher_forms(b, form)
    sleep(1)

b.quit()