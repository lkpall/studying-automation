from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse, parse_qsl
from json import loads

browser = Firefox()

url = 'http://selenium.dunossauro.live/exercicio_04.html'

browser.get(url)

sleep(3)

# nome, email, senha, telefone, btn

def preenche_form(browser, nome, email, senha, telefone):
    browser.find_element_by_name('nome').send_keys(nome)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(senha)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('btn').click()

dados = {
    'nome':'Matheus',
    'email':'mfp186@hotmail.com',
    'senha':'batatinha',
    'telefone':'991356547'
}

preenche_form(browser, **dados)

sleep(1)

url_parseada = urlparse(browser.current_url).query
dic = dict(parse_qsl(url_parseada))

dic.pop('btn')

assert dic == dados

browser.quit()
