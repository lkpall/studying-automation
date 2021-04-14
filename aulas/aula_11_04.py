from selenium.webdriver import Firefox
from time import sleep
from selenium.webdriver.common.alert import Alert

browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_11_a')

sleep(2)

alerta = Alert(browser)

browser.find_element_by_id('all').click()

alerta.accept() # alerta
alerta.send_keys('Matheus') # prompt
alerta.accept() # prompt
alerta.accept() # confirm
