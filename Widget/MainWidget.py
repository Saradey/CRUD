from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget

from DATA.ResourceManager import ResourceManager
from entity.entityList import EntityList
from functional.functionalMainWidget import FunctionalMain
from table.table import Table

class MainWidget(QMainWindow) :

    def __init__(self):
        super().__init__()
        self.__resourceManager = ResourceManager()
        self.__table_widget = QWidget()   #ВИДЖЕТ ТАБЛИЦЫ
        self.__addEntityWbdget = None     #ВИДЖЕТ для добавления сущностей
        self.__entityList = EntityList(self.__resourceManager)      #класс список сущностей для таблицы
        self.__grid_layout = QGridLayout()     # сетка
        self.__table = Table(self.__resourceManager)                #таблица
        self.__switcher = 0                   #для переключения таблиц
        self.__functionalMain = FunctionalMain(self, self.__table)    #класс функционал, получает ссылку на главный виджет и работает с ним

        self.initUI()   #иницилизируем интерфейс
        pass

####################################функции 1 уровня
    def initUI(self):
        self.initTableWidget()

        self.setGeometry(400, 400, 1200, 500)
        self.setWindowTitle("Tour Operator : Airlands")
        pass



####################################функции 2 уровня
   #создаем таблицу, к функции initUI
    def initTableWidget(self):
        self.__table_widget.setLayout(self.__grid_layout)  # добавляем в наш виджет таблицы сетку
        self.setCentralWidget(self.__table_widget)  # Устанавливаем центральный виджет таблицу
        self.GreatTable()               #3 уровень, функция создания таблицы данных
        pass

####################################функции 3 уровня
    #функция создания таблицы данных, к функции initTableWidget
    def GreatTable(self) :
        self.__entityList.GreatTable(self.__switcher)    #создаем список и загружаем из sql сущности
        self.__table.SetListEntityTable(self.__entityList)  #загружаем в табилицу все сущности
        self.__grid_layout.addWidget(self.__table.GreatGetTable(), 0, 0)  # Добавляем таблицу в сетку
        pass

####################################сетеры
    def SetSwitcher(self, switcher):
        self.__switcher = switcher
        pass

    def SetAddEntityWidget(self, EntityWidget):
        self.__addEntityWbdget = EntityWidget
        pass

####################################гетеры
    def GetSwitcher(self):
        return self.__switcher

    def GetResourceManager(self):
        return self.__resourceManager