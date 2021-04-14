from abc import ABC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from biblioteca import Page, PageElement

# ----------------------------------------------------------
from selenium.webdriver import Firefox

browser = Firefox()

page = PageTodo(browser, 'http://selenium.dunossauro.live/todo_list.html')

page.open()

page.todo.create_todo('Fazer aaula', 'Selenium aula POM')

print(page.a_fazer.todos())
