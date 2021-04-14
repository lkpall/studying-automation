from selenium.webdriver import Firefox

browser = Firefox()

url = 'https://selenium.dunossauro.live/aula_09_a.html'

browser.get(url)
browser.implicitly_wait(30)

btn = browser.find_element_by_css_selector('button')
btn.click()

sucess = browser.find_element_by_css_selector('#finisehd')
assert sucess.text == 'Carregamento concluído'
