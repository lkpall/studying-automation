from abc import ABC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Quando uma classe recebe esse abc, ela se torna uma
#classe abstrata, ou seja, ela não pode ser chamada. Nesse caso, usado apenas
#para iniciar o webdriver

# Class PageElement é usada para inicializar/instanciar o webdriver, sendo aplicada
#em parametros de outras  classes. Assim evitando ter que instanciar o webdriver 
#toda vida nas outras classes. Além disso, tb procurar os web elements e pega a url
class PageElement(ABC):
    def __init__(self, webdriver, url=''):
        self.webdriver = webdriver
        self.url = url

    def find_element(self, locator):
        return self.webdriver.find_element(*locator)
    
    def find_elements(self, locator):
        return self.webdriver.find_elements(*locator)

    def open(self):
        self.webdriver.get(self.url) # substitui o browser.get() lá no codigo

# Essa classe representa a parte de criação do todo, 'objetificando-a'
class Todo(PageElement):
    # atributo = locator
    name = (By.ID, 'todo-name')
    description = (By.ID, 'todo-desc')
    urgent = (By.ID, 'todo-next')
    submit = (By.ID, 'todo-submit')
    
    def create_todo(self, name, description, urgent=False):
        self.webdriver.find_element(*self.name).send_keys(name)
        self.webdriver.find_element(*self.description).send_keys(description)
        if urgent:
            self.webdriver.find_element(*self.urgent).click()
        self.webdriver.find_element(*self.submit).click()

# Aqui é outra classe abstrata criada para pegar todos os cards dos containers 
#existente (A fazer, Fazendo, Pronto)
class CardContainer(PageElement, ABC):
    def todos(self):
        cards = self.find_elements(self.card)
        po_cards = []
        for card in cards:
            po_cards.append(Card(card))
        return po_cards

# Essas próximas 3 classes são os 3 containers existentes.
class AFazer(CardContainer):
    fieldset = (By.CSS_SELECTOR, 'div.body_a fieldset')
    card = (By.CLASS_NAME, 'terminal-card')

class Fazendo(CardContainer):
    fieldset = (By.CSS_SELECTOR, 'div.body_b fieldset')
    card = (By.CLASS_NAME, 'terminal-card')

class Pronto(CardContainer):
    fieldset = (By.CSS_SELECTOR, 'div.body_c fieldset')
    card = (By.CLASS_NAME, 'terminal-card')

# Por fim, a classe do card em si, onde possui os seus atributos e funções
class Card:
    # atributos do card
    def __init__(self, selenium_object):
        self.selenium_object = selenium_object
        self.name = By.CSS_SELECTOR, 'header.name'
        self.description = By.CSS_SELECTOR, 'div.description'
        self._do = By.CSS_SELECTOR, 'button.do'
        self._cancel = By.CSS_SELECTOR, 'button.cancel'
        self._load() # coloca o underline nele pq é "private"

    # button de fazer
    def do(self):
        self.selenium_object.find_element(*self._do).click()

    # button de cancelar, está nesse Try:Except pq quando o carda passa para o
    #container de Fazendo, não existe o button "cancelar", existe a de voltar
    #e nessa parte não implementamos isso
    def cancel(self):
        try:
            self.selenium_object.find_element(*self._cancel).click()
        except NoSuchElementException:
            print('Elemento não tem cancelar')

    # Nesse metodo ele busca os atributos.text do card
    def _load(self):
        self.name = self.selenium_object.find_element(*self.name).text
        self.description = self.selenium_object.find_element(*self.description).text

    # E nesse ele faz o print deles, retorna formatado
    def __repr__(self):
        return f'Card(name="{self.name}", description="{self.description}")'

# ----------------------------------------------------------
from selenium.webdriver import Firefox

webdriver = Firefox()
url = 'https://selenium.dunossauro.live/todo_list.html'

# Aqui ele instancia a classe Todo no todo_element e passa a ele como params
#o  browser e a url que ele tem que acessar
todo_element = Todo(webdriver, url)
todo_element.open() # Aqui ele inicia(da o .get) na url passada com o metodo open

# Aqui utiliza o metodo create_todo  e é passado como params o nome e a descrição
#nesse metodo tb já é apertando o button de confirmação e o card é enviado para o
#container de AFazer
todo_element.create_todo(
    'Dormir',
    'Dormir é muito bom'
)

a_fazer = AFazer(webdriver) # Instanciando o container AFazer na variavel

todos = a_fazer.todos() # Pegando a lista de todos os todos no container AFazer
todos[0].do() # apertnado o botão fazer no primeiro card da lista

fazendo = Fazendo(webdriver)
todos[0].cancel() # apertnado o botão cancelar no primeiro card da lista

# pronto = Pronto(webdriver)
# print(pronto.todos())

"""
O importante do conceito de PageObject é você saber identificar quais são os
objetos da página e saber  objetifica-los com coerência.
"""