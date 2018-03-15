#отели
class Hotel :
    def __init__(self, ArrClient) :
        self.__IDHotel = ArrClient[0]  #айди отеHC
        self.__HotelCategory = ArrClient[1]     #категория отел
        self.__Name = ArrClient[2]       #имя отеля
        self.__HotelDescription = ArrClient[3]  #описание отеля
        self.__ArrGetEntity = []  # переменных сущности в список
        self.InitList()
        pass

####################################Иницилизация переменных сущности в список, функция 2 уровня
    def InitList(self):
        self.__ArrGetEntity = [self.__Name, self.__HotelCategory, self.__HotelDescription]

################################гетеры
    def GetID(self):
        return self.__IDHotel

    def GetHotelCategory(self):
        return self.__HotelCategory

    def GetName(self):
        return self.__Name

    def GetHotelDescription(self):
        return self.__HotelDescription

    def GetInitList(self):
        return self.__ArrGetEntity

################################сетеры
    def SetIDHotel(self, IDHotel):
        self.__IDHotel = IDHotel
        pass

    def SetHotelCategory(self, HotelCategory):
        self.__HotelCategory = HotelCategory
        pass

    def SetName(self, Name):
        self.__Name = Name
        pass

    def SetHotelDescription(self, HotelDescription):
        self.__HotelDescription = HotelDescription
        pass