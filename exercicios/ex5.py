from selenium.webdriver import Firefox

def preencher_forms(browser):
    forms = ['.form-l0c0', '.form-l0c1', '.form-l1c0', '.form-l1c1']

    for form in forms:
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

url = 'http://selenium.dunossauro.live/exercicio_05.html'

b.get(url)

preencher_forms(b)

b.quit()
