from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint # printa bonitinho

"""
1. Pegar todos os links de aulas
    {'nome da aula': 'link da aula'}
2. Navegar até o exercício 3 
    achar a url do exercício 3 e ir até lá
"""

def get_links(browser, elemento):
    """
    Pega todos os links dentro de um elemento

    - browser = a instância do navegador
    - elemento = webelement [aside, main, body, ul, ol]
    """
    resultado = {}
    element = browser.find_element_by_tag_name(elemento)
    ancoras = element.find_elements_by_tag_name('a')
    for ancora in ancoras:
        resultado[ancora.text] = ancora.get_attribute('href')
    return resultado

browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_04.html')

sleep(1)

# Parte 1

aulas = get_links(browser, 'aside')

pprint(aulas)

# Parte 2

exercicios = get_links(browser, 'main')

pprint(exercicios)

browser.get(exercicios['Exercício 3'])
