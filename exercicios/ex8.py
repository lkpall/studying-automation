from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def caixinha_colorida(key, ac, caixa, span):
    ac.key_down(key)
    ac.move_to_element(caixa)
    ac.pause(1)
    ac.click()
    ac.pause(1)
    ac.double_click()
    ac.pause(1)
    ac.move_to_element(span)
    ac.key_up(key)

url = 'https://selenium.dunossauro.live/caixinha'

browser = Firefox()

browser.get(url)

caixa = browser.find_element_by_id('caixa')
span = browser.find_element_by_tag_name('span')
ac = ActionChains(browser)

caixinha_colorida(Keys.SHIFT, ac, caixa, span)
caixinha_colorida(Keys.CONTROL, ac, caixa, span)
ac.context_click()
ac.pause(1)
ac.perform()

