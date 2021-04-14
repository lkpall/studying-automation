from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_11_a')

sleep(1)

browser.find_element_by_id('alert').click()

alerta = browser.switch_to.alert

alerta.accept() # confirma, clicka no ok
