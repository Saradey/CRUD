#страна
class Country :
    def __init__(self, ArrClient):
        self.__CodeCountry = ArrClient[0]    #айди страны
        self.__NameCountry = ArrClient[1]    #название страны
        self.__ArrGetEntity = []  # переменных сущности в список
        self.InitList()
        pass

####################################Иницилизация переменных сущности в список, функция 2 уровня
    def InitList(self):
        self.__ArrGetEntity = [self.__CodeCountry, self.__NameCountry]

################################гетеры
    def GetID(self):
        return self.__CodeCountry

    def GetNameCountry(self):
        return self.__NameCountry

    def GetInitList(self):
        return self.__ArrGetEntity

################################сетеры
    def SetCodeCountry(self, CodeCountry):
        self.__CodeCountry = CodeCountry
        pass

    def SetNameCountry(self, NameCountry):
        self.__NameCountry = NameCountry
        pass