from selenium.webdriver import Firefox

browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_04_a.html')

lista_n_ordenada = browser.find_element_by_tag_name('ul')

lis = lista_n_ordenada.find_elements_by_tag_name('li')

a = lis[0].find_element_by_tag_name('a').text

print(a)

# Buscas aninhadas