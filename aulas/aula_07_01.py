from selenium.webdriver import Firefox
from time import sleep

"""
1. Checar se a mudança ocorre no span (focus, blur)
2. Checar se a mudança ocorre no p (change)
"""

browser = Firefox()

browser.get('https://selenium.dunossauro.live/aula_07_d')

input_de_texto = browser.find_element_by_tag_name('input')
span = browser.find_element_by_tag_name('span')
p = browser.find_element_by_tag_name('p')

input_de_texto.click()
assert 'está com foco' == span.text, 'está com foco não está em span'
span.click()
assert 'está sem foco' == span.text, 'está sem foco não está em span'

"""
enviar "batata" no elemento input
então o texto em foco deverá ser o content de span
quando clickar no span
"""

assert p.text == "0", 'p não é zero'
input_de_texto.send_keys('batata')
span.click()
assert 'está com foco' == span.text, 'está com foco não está em span'
span.click()
assert 'está sem foco' == span.text, 'está sem foco não está em span'
assert p.text == '1', 'p não é um'

browser.quit()
