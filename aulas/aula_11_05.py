from selenium.webdriver import Firefox
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support.expected_conditions import alert_is_present

browser = Firefox()

wdw = WebDriverWait(browser, 30)

browser.get('http://selenium.dunossauro.live/aula_11_a')

sleep(2)

browser.find_element_by_id('alertd').click()

alerta = wdw.until(alert_is_present()) # esse metodo alem de verificar se o 
# alert existe, retorna ele, o que elimina fazer a declaração dele no inicio
# que nem tava fazendo antes, assim "alerta = Alert(browser)"

alerta.accept() 

