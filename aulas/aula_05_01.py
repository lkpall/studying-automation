from selenium.webdriver import Firefox

firefox = Firefox()

firefox.get('http://selenium.dunossauro.live/aula_05_a.html')

div_py = firefox.find_element_by_id('python')
div_hk = firefox.find_element_by_id('haskell')

print(div_py.text)
print(div_hk.text)

firefox.quit()
