from selenium.webdriver import Firefox
from time import sleep
from selenium.webdriver.common.alert import Alert

browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_11_a')

sleep(1)

browser.find_element_by_id('prompt').click()

alerta = Alert(browser)

alerta.send_keys('Matheus')
#alerta.accept() # confirma, clicka no ok
