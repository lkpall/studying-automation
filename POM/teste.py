from selenium.webdriver import Firefox
from pages.pages import PageTodo

browser = Firefox()

pagina = PageTodo(browser, 'http://selenium.dunossauro.live/todo_list.html')
pagina.open()
pagina.todo.create_todo('POM', 'POM POM POM POM')
