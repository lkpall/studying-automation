from selenium.webdriver import Firefox

firefox = Firefox()

firefox.get('http://selenium.dunossauro.live/aula_05_b.html')

topico = firefox.find_element_by_class_name('topico')
linguagens = firefox.find_elements_by_class_name('linguagens')

for linguagem in linguagens:
    print(
        (linguagem.find_element_by_tag_name('h2').text,
        linguagem.find_element_by_tag_name('p').text)
        )