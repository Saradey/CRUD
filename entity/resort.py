#курорты
class Resort :
    def __init__(self, ArrClient) :
        self.__IDResort = ArrClient[0]  #айди курорта
        self.__NameResort = ArrClient[1]    #название курорта
        self.__DescriptionResort = ArrClient[2]    #дата отправления
        self.__ArrGetEntity = []  # переменных сущности в список
        self.InitList()
        pass

####################################Иницилизация переменных сущности в список, функция 2 уровня
    def InitList(self):
        self.__ArrGetEntity = [self.__NameResort, self.__DescriptionResort]

################################гетеры
    def GetID(self):
        return self.__IDResort

    def GetNameResort(self):
        return self.__NameResort

    def GetDescriptionResort(self):
        return self.__DescriptionResort

    def GetInitList(self):
        return self.__ArrGetEntity

################################сетеры
    def SetIDResort(self, IDResort):
        self.__IDResort = IDResort
        pass

    def SetNameResort(self, NameResort):
        self.__NameResort = NameResort
        pass

    def SetDescriptionResort(self, DescriptionResort):
        self.__DescriptionResort = DescriptionResort
        pass