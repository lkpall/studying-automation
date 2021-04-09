from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()
dicMaster = {}
dic = {}

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'

browser.get(url)

sleep(1)

h1 = browser.find_element_by_tag_name('h1')

ps = browser.find_elements_by_tag_name('p')

# Pegando o atributo e o texto das tags P
dic.update({ps[0].get_attribute('atributo'): ps[0].text})
dic.update({ps[1].get_attribute('atributo'): ps[1].text})
dic.update({ps[2].get_attribute('atributo'): ps[2].text})

dicMaster.update({h1.text: dic})

print(dicMaster)

browser.quit()