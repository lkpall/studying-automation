from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'

browser.get(url)

sleep(1)

a = browser.find_element_by_tag_name('a')

while True:
    a.click()
    test = browser.find_elements_by_tag_name('p')
    recv = test[-1].text
    if len(recv) > 3:
        print(recv[0:11])
        break
sleep(5)
browser.quit()