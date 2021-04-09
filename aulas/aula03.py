from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()
browser.get('https://curso-python-selenium.netlify.app/aula_03.html')
sleep(2)

a = browser.find_element_by_tag_name('a')

for click in range(1, 11):
    p = browser.find_elements_by_tag_name('p')
    a.click()
    print(f'Valor do ultimo p {p[-1].text} valor do click: {click}') 


print(f'texto de a: {a.text}')

# browser.quit()
