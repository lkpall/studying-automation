from selenium.webdriver import Firefox

b = Firefox()

url = 'http://selenium.dunossauro.live/aula_06_a.html'

b.get(url)

# Usando a tag type como atributo [attr=valor]
# nome = b.find_element_by_css_selector('[type="text"]')
# senha = b.find_element_by_css_selector('[type="password"]')
# btn = b.find_element_by_css_selector('[type="submit"]')

# Usando o "name" como atributo [attr="valor"] pega exatamente o valor que é 
# passado depois do =
# nome = b.find_element_by_css_selector('[name="nome"]')
# senha = b.find_element_by_css_selector('[name="senha"]')
# btn = b.find_element_by_css_selector('[name="l0c0"]')

# Usando o atributo * [attr*="valor"] pega qualquer elemento que tenha o 
# conjunto especificado
# nome = b.find_element_by_css_selector('[name*="ome"]')
# senha = b.find_element_by_css_selector('[name*="nha"]')
# btn = b.find_element_by_css_selector('[name*="l0"]')

# Usando o atributo | [attr|="valor"] pega exatamente mesmo o elemento que tenha
# o valor depois do =
# nome = b.find_element_by_css_selector('[name|="nome"]')
# senha = b.find_element_by_css_selector('[name|="senha"]')
# btn = b.find_element_by_css_selector('[name|="l0c0"]')

# Usando o atributo ^ [attr^="valor"] pega o elemento que comece com tal valor
# nome = b.find_element_by_css_selector('[name^="n"]')
# senha = b.find_element_by_css_selector('[name^="s"]')
# btn = b.find_element_by_css_selector('[name^="l"]')

# Usando o atributo $ [attr$="valor"] pega o elemento que termina com tal valor
# nome = b.find_element_by_css_selector('input[name$="e"]')
# senha = b.find_element_by_css_selector('input[name$="a"]')
# btn = b.find_element_by_css_selector('input[name$="0"]')

nome.send_keys('Matheus')
senha.send_keys('batatinha123')
btn.click()
