from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

url = 'https://selenium.dunossauro.live/caixinha'

browser = Firefox()

browser.get(url)

caixa = browser.find_element_by_id('caixa')
span = browser.find_element_by_tag_name('span')

ac = ActionChains(browser)

def caixinha_colorida(key):
    ac.key_down(key)
    ac.move_to_element(caixa)
    ac.pause(1)
    ac.click()
    ac.pause(1)
    ac.double_click()
    ac.pause(1)
    ac.move_to_element(span)
    ac.key_up(key)

caixinha_colorida(Keys.SHIFT)
caixinha_colorida(Keys.CONTROL)
ac.context_click()
ac.pause(1)
ac.perform()

# Exercício 8 exibir e printar todas as cores possíveis da caixinha (17)
