from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse

def start_game(browser):
    main = browser.find_element_by_tag_name('main')
    element = main.find_element_by_tag_name('li')
    anchor = element.find_element_by_tag_name('a')
    anchor.click()

def select_anchor(browser, atributo):
    main = browser.find_element_by_tag_name('main')
    elements = main.find_elements_by_tag_name('li')
    anchor_1 = elements[0].find_element_by_tag_name('a')
    anchor_2 = elements[1].find_element_by_tag_name('a')
    if atributo == anchor_1.get_attribute('attr'):
        anchor_1.click()
    else:
        anchor_2.click()

def select_path(browser):
    main = browser.find_element_by_tag_name('main')
    elements = main.find_elements_by_tag_name('li')
    anchor_1 = elements[0].find_element_by_tag_name('a')
    anchor_2 = elements[1].find_element_by_tag_name('a')
    url = urlparse(browser.current_url)
    url = url.path
    if url[1:] == anchor_1.text:
        anchor_1.click()
    else:
        anchor_2.click()

"""
Descrição do exercício
1. acessar a página https://selenium.dunossauro.live/exercicio_03.html
    e clickar no botão de iniciar
2. começar o jogo
3. responder errado
4. pegar o título da página e comparar com uma das respostas
5. pegar o path nos parametros e comparar com a resposta
6. dar um refresh na página
7. curtir a vitória ^^
"""

browser = Firefox()

# parte 1

browser.get('https://selenium.dunossauro.live/exercicio_03.html')

sleep(1)

# parte 2

start_game(browser)

# parte 3

sleep(1)

select_anchor(browser, 'errado')

# parte 4

sleep(40)

select_anchor(browser, 'certo')

# parte 5

sleep(1)

select_path(browser)

# parte 6

sleep(1)

browser.refresh()

# parte 7 ihuuuuuuuuuuuuuuuuuuuuuuuu

sleep(5)
browser.quit()