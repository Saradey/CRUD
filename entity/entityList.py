from entity.client import Client
from entity.country import Country
from entity.flight import Flight
from entity.hotel import Hotel
from entity.resort import Resort
from entity.tour import Tour

#Энтити лист хранит в себе список определенных сущностей
#и при открытии выбранной таблицы (Клиенты, Путевки, Рейсы и тд.
#будет загружаться из sql некоторое количество сущностей и необходимые данные)

class EntityList:
    def __init__(self, resourceManager):
        self.__resourceManager = resourceManager  #получаем ссылку на ресурс менеджер
        self.__arrEntity = []   #список сущностей для загрузки в таблицу
        self.__arrColumn = []   #список столбцов таблиц
        self.__id = []  # для ключей
        self.DB = None
        pass

#######################################################иницилизация списков
    #иницилизация списка клиентов
    def InitListClient(self):
        self.__arrEntity.clear()
        self.__arrColumn.clear()

        arrColumn = ["Фамилия Имя Отчество", "Адрес", "Дата рождения", "Контактный телефон"]
        self.__arrColumn = arrColumn

        self.__id.clear()
        AllEntityСortege = self.__resourceManager.GetListClientSQL()
        for it in AllEntityСortege :
            TeampArr = list(it)
            self.__id.append(TeampArr[0])
            self.__arrEntity.append(Client(TeampArr))

        self.DB = "Client"
        self.ID = "IdClient"

        pass


    #иницилизация списка путевок
    def InitListTour(self):
        self.__arrEntity.clear()
        self.__arrColumn.clear()

        arrColumn = ["Описание Путевки"]
        self.__arrColumn = arrColumn

        self.__id.clear()
        AllEntityСortege = self.__resourceManager.GetListTourSQL()
        for it in AllEntityСortege:
            TeampArr = list(it)
            self.__id.append(TeampArr[0])
            self.__arrEntity.append(Tour(TeampArr))

        self.DB = "Tour"
        self.ID = "IDTour"
        pass


    #иницилизация списка стран
    def InitListCountry(self):
        self.__arrEntity.clear()
        self.__arrColumn.clear()

        arrColumn = ["Код страны", "Название"]
        self.__arrColumn = arrColumn

        self.__id.clear()
        self.__id.clear()
        AllEntityСortege = self.__resourceManager.GetListCountrySQL()
        for it in AllEntityСortege:
            TeampArr = list(it)
            self.__id.append(TeampArr[0])
            self.__arrEntity.append(Country(TeampArr))

        self.DB = "Country"
        self.ID = "CodeCountry"
        pass


    # иницилизация списка рейсов
    def InitListFlight(self):
        self.__arrEntity.clear()
        self.__arrColumn.clear()

        arrColumn = ["№ Рейса", "Пункт назначения", "Дата отправления", "Цена", "Время в пути"]
        self.__arrColumn = arrColumn

        self.__id.clear()
        AllEntityСortege = self.__resourceManager.GetListFlightSQL()
        for it in AllEntityСortege:
            TeampArr = list(it)
            self.__id.append(TeampArr[0])
            self.__arrEntity.append(Flight(TeampArr))

        self.DB = "Flight"
        self.ID = "FlightNumber"
        pass


    # иницилизация списка отелей
    def InitListHotel(self):
        self.__arrEntity.clear()
        self.__arrColumn.clear()

        arrColumn = ["Названия отеля", "Категория отеля", "Описание отеля"]
        self.__arrColumn = arrColumn

        self.__id.clear()
        AllEntityСortege = self.__resourceManager.GetListHotelSQL()
        for it in AllEntityСortege:
            TeampArr = list(it)
            self.__id.append(TeampArr[0])
            self.__arrEntity.append(Hotel(TeampArr))

        self.DB = "Hotel"
        self.ID = "IDHotel"
        pass


    # иницилизация списка курортов
    def InitListResort(self):
        self.__arrEntity.clear()
        self.__arrColumn.clear()

        arrColumn = ["Название курорта", "Описание курорта"]
        self.__arrColumn = arrColumn

        self.__id.clear()
        AllEntityСortege = self.__resourceManager.GetListResortSQL()
        for it in AllEntityСortege:
            TeampArr = list(it)
            self.__id.append(TeampArr[0])
            self.__arrEntity.append(Resort(TeampArr))

        self.DB = "Resort"
        self.ID = "IDResort"
        pass

#######################################################иницилизация списков
    def GreatTable(self, switcher):
        if switcher == 0 :
            self.InitListClient()
        if switcher == 1 :
            self.InitListTour()
        if switcher == 2 :
            self.InitListHotel()
        if switcher == 3 :
            self.InitListFlight()
        if switcher == 4 :
            self.InitListResort()
        if switcher == 5 :
            self.InitListCountry()
        if switcher > 5 or switcher < -1:
            self.InitListClient()
        pass

################################гетеры
    def GetArrEntity(self):
        return self.__arrEntity

    def GetArrColumn(self):
        return self.__arrColumn

    def GetSizeColumn(self):
        return len(self.__arrColumn)

    def GetSizeRow(self):
        return len(self.__arrEntity)

    def GetNameTable(self):
        return self.DB

    def GetID(self):
        return self.ID

    def GetIdArr(self):
        return self.__id