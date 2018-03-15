from PyQt5.QtWidgets import QAction, qApp
from Widget.AddEntityWidget import AddEntityWidget
#класс работает с statusBar и с меню барами главного виджета
class FunctionalMain :

    def __init__(self, MainWidget, table):
        self.__MainWidget = MainWidget
        self.InitStatusBar()

        self.__menubar = self.__MainWidget.menuBar()   #создаем строки меню

        self.table = table

        self.__fileMenu = self.__menubar.addMenu('&Файл')   #создаем строку Файл
        self.__exitAction = QAction('&Выход', self.__MainWidget)
        self.__saveAction = QAction('&Сохранить', self.__MainWidget)

        self.__ListMenu = self.__menubar.addMenu('&Списки')  # создаем строку списков
        self.__client = QAction('&Клиенты', self.__MainWidget)
        self.__county = QAction('&Страны', self.__MainWidget)
        self.__fligth = QAction('&Рейсы', self.__MainWidget)
        self.__hotel = QAction('&Отели', self.__MainWidget)
        self.__resort = QAction('&Курорты', self.__MainWidget)
        self.__tour = QAction('&Путевки Клиентов', self.__MainWidget)


        self.__editingMenu = self.__menubar.addMenu('&Редактировать')  #создаем строку списков
        self.__add = QAction('&Добавить сущность', self.__MainWidget)
        self.__delete = QAction('&Удалить выбранное', self.__MainWidget)

        self.GreatProgramMenu() #создаем все бары
        pass

################################функции 1 уровня
    def InitStatusBar(self):
        self.__MainWidget.statusBar()
        pass

    #содержит в себе функции создания всех программных меню и баров
    def GreatProgramMenu(self):
        self.InitProgramMenu()
        pass


################################функции 2 уровня
    #создаем кнопки для программного меню
    def InitProgramMenu(self):

        self.__saveAction.setStatusTip('Сохранить изменения')
        self.__saveAction.triggered.connect(self.Save)
        self.__fileMenu.addAction(self.__saveAction)

        self.__exitAction.setStatusTip('Выйти из приложения')
        self.__exitAction.triggered.connect(qApp.quit)
        self.__fileMenu.addAction(self.__exitAction)
###############
        self.__client.setStatusTip('Открыть список клиентов')
        self.__client.triggered.connect(self.OpenClint)
        self.__ListMenu.addAction(self.__client)

        self.__county.setStatusTip('Открыть список стран')
        self.__county.triggered.connect(self.OpenCounty)
        self.__ListMenu.addAction(self.__county)

        self.__fligth.setStatusTip('Открыть список рейсов')
        self.__fligth.triggered.connect(self.OpenFligth)
        self.__ListMenu.addAction(self.__fligth)

        self.__hotel.setStatusTip('Открыть список отелей')
        self.__hotel.triggered.connect(self.OpenHotel)
        self.__ListMenu.addAction(self.__hotel)

        self.__resort.setStatusTip('Открыть список курортов')
        self.__resort.triggered.connect(self.OpenResort)
        self.__ListMenu.addAction(self.__resort)

        self.__tour.setStatusTip('Открыть список созданных путевок')
        self.__tour.triggered.connect(self.OpenTour)
        self.__ListMenu.addAction(self.__tour)
###############
        self.__add.setStatusTip('Добавить сущность')
        self.__add.triggered.connect(self.OpenWindiwWidgetGreat)
        self.__editingMenu.addAction(self.__add)

        self.__delete.setStatusTip('Удалить выбранную сущность')
        self.__delete.triggered.connect(self.DELETE_ENITY)
        self.__editingMenu.addAction(self.__delete)

###############
        pass

################################функция триггеры для кнопок программного меню
    #функции триггер для отрыктия списков
    def OpenClint(self):
        self.__MainWidget.SetSwitcher(0)
        self.__MainWidget.GreatTable()
        pass

    def OpenCounty(self):
        self.__MainWidget.SetSwitcher(5)
        self.__MainWidget.GreatTable()
        pass

    def OpenFligth(self):
        self.__MainWidget.SetSwitcher(3)
        self.__MainWidget.GreatTable()
        pass

    def OpenHotel(self):
        self.__MainWidget.SetSwitcher(2)
        self.__MainWidget.GreatTable()
        pass

    def OpenResort(self):
        self.__MainWidget.SetSwitcher(4)
        self.__MainWidget.GreatTable()
        pass

    def OpenTour(self):
        self.__MainWidget.SetSwitcher(1)
        self.__MainWidget.GreatTable()
        pass

    #функции триггер для Редактировать
    def OpenWindiwWidgetGreat(self):
        switcher = self.__MainWidget.GetSwitcher()
        resTeamp = self.__MainWidget.GetResourceManager()

        if switcher == 0 :
            self.__MainWidget.SetAddEntityWidget(AddEntityWidget(0, resTeamp))
        if switcher == 1 :
            self.__MainWidget.SetAddEntityWidget(AddEntityWidget(1, resTeamp))
        if switcher == 2 :
            self.__MainWidget.SetAddEntityWidget(AddEntityWidget(2, resTeamp))
        if switcher == 3 :
            self.__MainWidget.SetAddEntityWidget(AddEntityWidget(3, resTeamp))
        if switcher == 4 :
            self.__MainWidget.SetAddEntityWidget(AddEntityWidget(4, resTeamp))
        if switcher == 5 :
            self.__MainWidget.SetAddEntityWidget(AddEntityWidget(5, resTeamp))
        if switcher > 5 or switcher < -1:
            self.__MainWidget.SetAddEntityWidget(AddEntityWidget(0, resTeamp))
        pass

    def DELETE_ENITY(self):
        self.table.DeleteRow()
        pass

    # функции триггер для Редактировать
    def Save(self):
        self.table.Save()
        pass