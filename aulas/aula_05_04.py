from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse
from json import loads

firefox = Firefox()

firefox.get('http://selenium.dunossauro.live/aula_05.html')

sleep(2)

# nome, email, senha, telefone, btn

def preenche_form(browser, nome, email, senha, telefone):
    browser.find_element_by_name('nome').send_keys(nome)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(senha)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('btn').click()

estrutura = {
    'nome':'Matheus',
    'email':'mfp186@hotmail.com',
    'senha':'batatinha',
    'telefone':'998765432'
}

preenche_form(firefox, **estrutura)

sleep(2)

url_parseada = urlparse(firefox.current_url)

texto_resultado = firefox.find_element_by_id('result').text
resultado_arrumado = texto_resultado.replace('\'', "\"")

dic_result = loads(resultado_arrumado)

assert dic_result == estrutura

firefox.quit()
