from PyQt5.QtCore import QFile, QIODevice, Qt, QTextStream
from PyQt5.QtWidgets import (QDialog, QFileDialog, QGridLayout, QHBoxLayout,
        QLabel, QLineEdit, QMessageBox, QPushButton, QTextEdit, QVBoxLayout,
        QWidget, QComboBox)

#виджет добавление сущностей, он принимает флаг switcher в качестве параметра и определяет
#какую сущность необходимо добавить в базу данных

class AddEntityWidget (QWidget):
    def __init__(self, switcher, resourceManager):
        super().__init__()
        self.__switcher = switcher  # для переключения между сущностями
        self.__resourceManager = resourceManager #наша база данных

        self.initUI()
        pass

####################################функции 1 уровня
    def initUI(self):
        self.setGeometry(500, 500, 400, 250)
        self.setWindowTitle("Add Entity")
        self.show()
        self.mainLayout = QGridLayout()  # иницилизируем сетку
        self.InitButtonWidget()
        self.setLayout(self.mainLayout)  # добавляем нашу сетку
        self.AddEntityWidgetInit()
        pass

####################################функции 2 уровня
        # что бы сто раз не писать иницилизацию кнопок
    def InitButtonWidget(self):
        self.addSave = QPushButton("&Сохранить")
        self.addSave.setToolTip("Сохранить результат в базу данных")
        self.addSave.clicked.connect(self.SAVE_ALL)

        self.addExit = QPushButton("&Отмена")
        self.addExit.setToolTip("Выйти")
        self.addExit.clicked.connect(self.close)

        self.mainLayout.addWidget(self.addSave, 7, 0)
        self.mainLayout.addWidget(self.addExit, 7, 2)
        pass

        #############создаем нужные нам лейблы и поля для заполнения
    def AddEntityWidgetInit(self):
        if self.__switcher == 0:
            self.AddClient()
            pass
        if self.__switcher == 1:
            self.AddTour()
            pass
        if self.__switcher == 2:
            self.AddHotel()
            pass
        if self.__switcher == 3:
            self.AddFlight()
            pass
        if self.__switcher == 4:
            self.AddResort()
            pass
        if self.__switcher == 5:
            self.AddCountry()
            pass
        if self.__switcher > 5 or self.__switcher < -1:
            self.AddClient()
            pass
        pass

####################################функции 3 уровня
    def AddClient(self):
        nameLabel = QLabel("Имя Фамилие Отчество:")
        addressLabel = QLabel("Адрес:")
        dateOfBirthLabel = QLabel("Дата рождения YYYY-MM-DD:")  #ISO 8601
        TelephoneLabel = QLabel("Телефон:")


        self.mainLayout.addWidget(nameLabel, 0, 0)
        self.mainLayout.addWidget(addressLabel, 1, 0)
        self.mainLayout.addWidget(dateOfBirthLabel, 2, 0)
        self.mainLayout.addWidget(TelephoneLabel, 3, 0)

        self.nameLine = QLineEdit()
        self.addressText = QLineEdit()
        self.addDateOfBirthLabel = QLineEdit()
        self.addTelephone = QLineEdit()

        self.mainLayout.addWidget(self.nameLine, 0, 2)
        self.mainLayout.addWidget(self.addressText, 1, 2)
        self.mainLayout.addWidget(self.addDateOfBirthLabel, 2, 2)
        self.mainLayout.addWidget(self.addTelephone, 3, 2)
        pass

    def AddCountry(self):
        nameLabel = QLabel("Название страны:")
        StarLabel = QLabel("Код страны:")

        self.mainLayout.addWidget(nameLabel, 0, 0)
        self.mainLayout.addWidget(StarLabel, 1, 0)


        self.nameLine = QLineEdit()
        self.CodText = QLineEdit()

        self.mainLayout.addWidget(self.nameLine, 0, 2)
        self.mainLayout.addWidget(self.CodText, 1, 2)
        pass


    def AddHotel(self):
        nameLabel = QLabel("Название:")
        CategoryLabel = QLabel("Категория:")
        DescriptLabel = QLabel("Описание:")
        ResorLabel = QLabel("Курорт:")

        self.mainLayout.addWidget(nameLabel, 0, 0)
        self.mainLayout.addWidget(CategoryLabel, 1, 0)
        self.mainLayout.addWidget(DescriptLabel, 2, 0)
        self.mainLayout.addWidget(ResorLabel, 3, 0)

        self.CategoryText = QLineEdit()
        self.nameLine = QLineEdit()
        self.addDescript = QLineEdit()

        self.mainLayout.addWidget(self.nameLine, 0, 2)
        self.mainLayout.addWidget(self.CategoryText, 1, 2)
        self.mainLayout.addWidget(self.addDescript, 2, 2)


        self.comboResort = QComboBox(self)
        self.__arrH = self.__resourceManager.GetListResortSQL()
        self.__primaryKeyRe= None
        for it in self.__arrH :
            self.comboResort.addItem(it[1])
            pass
            self.comboResort.activated[str].connect(self.ClickOnComboHotelAddHotel)
        self.mainLayout.addWidget(self.comboResort, 3, 2)

        pass


    def AddTour(self):
        ClientLabel = QLabel("Клиент:")
        Country = QLabel("Страна:")
        Resort = QLabel("Курорт:")
        HotelLabel = QLabel("Отель:")
        FligthLabel = QLabel("Дата отправления рейса YYYY-MM-DD:")
        DescriptLabel = QLabel("Описание:")

        self.mainLayout.addWidget(ClientLabel, 0, 0)
        self.mainLayout.addWidget(Country, 1, 0)
        self.mainLayout.addWidget(Resort, 2, 0)
        self.mainLayout.addWidget(HotelLabel, 3, 0)
        self.mainLayout.addWidget(FligthLabel, 4, 0)
        self.mainLayout.addWidget(DescriptLabel, 5, 0)

        self.Descript = QLineEdit()
        self.mainLayout.addWidget(self.Descript, 5, 2)

        self.__comboClient = QComboBox(self)
        self.__arrClient = self.__resourceManager.GetListClientSQL()
        self.__primaryKeyClient = None
        for it in self.__arrClient:
            self.__comboClient.addItem(it[1])
            pass
        self.__comboClient.activated[str].connect(self.ClickOnComboClient)


        self.comboCountry = QComboBox(self)
        self.__arrCountry = self.__resourceManager.GetListCountrySQL()
        self.__primaryKeyCountre = None
        for it in self.__arrCountry:
            self.comboCountry.addItem(it[1])
            pass
        self.comboCountry.activated[str].connect(self.ClickOnComboCountry)


        self.comboResort = QComboBox(self)
        self.__primaryKeyResort = None
        self.comboResort.activated[str].connect(self.ClickOnComboResort)


        self.__primaryKeyHotel = None
        self.__comboHotel = QComboBox(self)
        self.__comboHotel.activated[str].connect(self.ClickOnComboHotel)


        self.__primaryKeyFligth = None
        self.__comboFligth = QComboBox(self)
        self.__comboFligth.activated[str].connect(self.ClickOnComboFligth)



        self.mainLayout.addWidget(self.comboCountry, 1, 2)
        self.mainLayout.addWidget(self.comboResort, 2, 2)
        self.mainLayout.addWidget(self.__comboHotel, 3, 2)
        self.mainLayout.addWidget(self.__comboFligth, 4, 2)
        self.mainLayout.addWidget(self.__comboClient, 0, 2)
        pass

    def AddFlight(self):

        iD = QLabel("Номер рейса:")
        FlightNumber =  QLabel("Пункт Назначения:")
        DepartureDate = QLabel("Дата отправления YYYY-MM-DD:")
        Price = QLabel("Цена:")
        TravelTime = QLabel("Время в пути HH-MM-SS:")
        Resort = QLabel("Курорт:")

        self.mainLayout.addWidget(iD, 0, 0)
        self.mainLayout.addWidget(FlightNumber, 1, 0)
        self.mainLayout.addWidget(DepartureDate, 2, 0)
        self.mainLayout.addWidget(Price, 3, 0)
        self.mainLayout.addWidget(TravelTime, 4, 0)
        self.mainLayout.addWidget(Resort, 5, 0)

        self.iD = QLineEdit()
        self.Destination = QLineEdit()
        self.DepartureDate = QLineEdit()
        self.TravelTime = QLineEdit()
        self.Price = QLineEdit()

        self.comboRes = QComboBox(self)
        self.__arrReso = self.__resourceManager.GetListResortSQL()
        self.__primaryKeyReso = None
        for it in self.__arrReso:
            self.comboRes.addItem(it[1])
            pass
        self.comboRes.activated[str].connect(self.ClickOnFligthToFly)


        self.mainLayout.addWidget(self.iD, 0, 2)
        self.mainLayout.addWidget(self.Destination, 1, 2)
        self.mainLayout.addWidget(self.DepartureDate, 2, 2)
        self.mainLayout.addWidget(self.Price, 3, 2)
        self.mainLayout.addWidget(self.TravelTime, 4, 2)

        self.mainLayout.addWidget(self.comboRes, 5, 2)
        pass

    def AddResort(self):

        NameResort = QLabel("Название Курорта:")
        DescriptionResort = QLabel("Описание курорта Курорта:")
        Country = QLabel("Страна:")

        self.mainLayout.addWidget(NameResort, 0, 0)
        self.mainLayout.addWidget(DescriptionResort, 1, 0)
        self.mainLayout.addWidget(Country, 2, 0)

        self.comboCount = QComboBox(self)
        self.__arrCount = self.__resourceManager.GetListCountrySQL()
        self.__primaryKeyCount = None
        for it in self.__arrCount:
            self.comboCount.addItem(it[1])
            pass
        self.comboCount.activated[str].connect(self.ClickOnResortAddToAdd)


        self.NameResort = QLineEdit()
        self.DescriptionResort = QLineEdit()

        self.mainLayout.addWidget(self.NameResort, 0, 2)
        self.mainLayout.addWidget(self.DescriptionResort, 1, 2)
        self.mainLayout.addWidget(self.comboCount, 2, 2)
        pass

    def SAVE_ALL(self):
        if self.__switcher == 0:
            if self.SaveClient() == False :
                ret = QMessageBox.warning(self, "Application", "Ошибка ввода")
            else:
                self.close()
            pass

        if self.__switcher == 1:
            if self.SaveTour() == False:
                ret = QMessageBox.warning(self, "Application", "Ошибка ввода")
            else:
                self.close()
            pass

        if self.__switcher == 2:
            if self.SaveHotel() == False:
                ret = QMessageBox.warning(self, "Application", "Ошибка ввода")
            else:
                self.close()
            pass

        if self.__switcher == 3:
            if self.SaveFlight() == False:
                ret = QMessageBox.warning(self, "Application", "Ошибка ввода")
            else:
                self.close()
            pass

        if self.__switcher == 4:
            if self.SaveResort() == False:
                ret = QMessageBox.warning(self, "Application", "Ошибка ввода")
            else:
                self.close()
            pass

        if self.__switcher == 5:
            if self.SaveCountry() == False:
                ret = QMessageBox.warning(self, "Application", "Ошибка ввода")
            else:
                self.close()
            pass

        if self.__switcher > 5 or self.__switcher < -1:
            if self.SaveTour() == False:
                ret = QMessageBox.warning(self, "Application", "Ошибка ввода")
            else:
                self.close()
            pass

        pass



####################################функции 4 уровня

    def ClickOnComboCountry(self, text):
        self.comboResort.clear()
        self.__comboHotel.clear()
        self.__comboFligth.clear()

        for it in self.__arrCountry :
            if(text == it[1]) :
                self.__primaryKeyCountre = it[0]

        self.__arrResort = self.__resourceManager.ExecuteReturn("SELECT * FROM Resort WHERE CodeOfTheCountry=:Id",
                                                                {"Id": self.__primaryKeyCountre})

        for it in self.__arrResort:
            self.comboResort.addItem(it[1])
            pass
        pass






####################################################Для добавления Курорта
####################################################

    def ClickOnResortAddToAdd(self, text):
        for it in self.__arrCount:
            if(text == it[1]) :
                self.__primaryKeyCount = it[0]
        pass


####################################################Для добавления Курорта
####################################################





####################################################Для добавления Рейсов
####################################################

    def ClickOnFligthToFly(self, text):
        for it in self.__arrReso:
            if(text == it[1]) :
                self.__primaryKeyReso = it[0]
        pass

####################################################Для добавления Рейсов
####################################################






####################################################Для добавления отеля
####################################################

    def ClickOnComboHotelAddHotel(self, text):
        for it in self.__arrH:
            if(text == it[1]) :
                self.__primaryKeyRe = it[0]
        pass

####################################################Для добавления отеля
####################################################






####################################################Для добавления путевки
####################################################
    def ClickOnComboResort(self, text):
        self.__comboHotel.clear()
        self.__comboFligth.clear()

        for it in self.__arrResort:
            if(text == it[1]) :
                self.__primaryKeyResort= it[0]

        self.__arrHotel = self.__resourceManager.ExecuteReturn("SELECT * FROM Hotel WHERE id_Resort=:Id",
                                                                {"Id": self.__primaryKeyResort})

        self.__arrFlight = self.__resourceManager.ExecuteReturn("SELECT * FROM Flight WHERE id_Resort=:Id",
                                                                {"Id": self.__primaryKeyResort})

        for it in self.__arrHotel:
            self.__comboHotel.addItem(it[2])
            pass


        for it in self.__arrFlight:
            self.__comboFligth.addItem(it[2])
            pass

        pass


    def ClickOnComboHotel(self, text):
        for it in self.__arrHotel:
            if(text == it[2]) :
                self.__primaryKeyHotel = it[0]
        pass


    def ClickOnComboFligth(self, text):
        for it in self.__arrFlight:
            if(text == it[2]) :
                self.__primaryKeyFligth= it[0]
        pass


    def ClickOnComboClient(self, text):
        for it in self.__arrClient:
            if (text == it[1]):
                self.__primaryKeyClient = it[0]
        pass

####################################################Для добавления путевки
####################################################







####################################################Сохраянем
####################################################
    def SaveTour(self):
        if self.Descript.text().strip() :
            return self.__resourceManager.Execute("INSERT INTO Tour (Descripte, ID_Client, ID_Hotel, Flight_Number) VALUES ('"+self.Descript.text()+"',"+str(self.__primaryKeyClient)+","+str(self.__primaryKeyHotel)+","+str(self.__primaryKeyFligth)+");")
        else:
            return False

    def SaveClient(self):
        if self.nameLine.text().strip() and self.addressText.text().strip() and	self.addDateOfBirthLabel.text().strip() and self.addTelephone.text().strip():
            return self.__resourceManager.Execute("INSERT INTO Client (FIOName, address, DateOfBirth, telephone) VALUES('"+self.nameLine.text()+"','"+ self.addressText.text() +"','"+ self.addDateOfBirthLabel.text() +"','"+ self.addTelephone.text()+"')")
        else:
            return False

    def SaveHotel(self):
        if self.CategoryText.text().strip() and self.nameLine.text().strip() and self.addDescript.text().strip():
            return self.__resourceManager.Execute("INSERT INTO Hotel (HotelCategory, Name, HotelDescription, id_Resort) VALUES('" + self.CategoryText.text() + "','" + self.nameLine.text() + "','" + self.addDescript.text() +"',"+str(self.__primaryKeyRe)+")")
        else:
            return False

    def SaveFlight(self):
        if self.iD.text().strip() and self.Destination.text().strip() and self.DepartureDate.text().strip() and self.Price.text().strip() and self.TravelTime.text().strip():
            return self.__resourceManager.Execute("INSERT INTO Flight (FlightNumber, Destination, DepartureDate, Price, TravelTime, id_Resort) VALUES("+ self.iD.text() +",'"+self.Destination.text()+"','"+self.DepartureDate.text()+"'," + self.Price.text() +",'"+self.TravelTime.text()+"',"+ str(self.__primaryKeyReso)+")")
        else:
            return False

    def SaveResort(self):
        if self.NameResort.text().strip() and self.DescriptionResort.text().strip():
            return self.__resourceManager.Execute("INSERT INTO Resort (NameResort, DescriptionResort, CodeOfTheCountry) VALUES('"+self.NameResort.text()+"','"+self.DescriptionResort.text()+"',"+str(self.__primaryKeyCount)+")")
        else:
            return False

    def SaveCountry(self):
        if self.nameLine.text().strip() and self.CodText.text().strip():
            return self.__resourceManager.Execute("INSERT INTO Country (CodeCountry, NameCountry) VALUES("+self.CodText.text()+",'"+self.nameLine.text()+"')")
        else:
            return False
####################################################Сохраянем
####################################################