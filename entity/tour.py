#путевка
class Tour:
    def __init__(self, ArrClient):
        self.__IDTour = ArrClient[0]        #айди путевки
        self.__Descripte = ArrClient[1]     #описание путевки
        self.__ArrGetEntity = []        #переменных сущности в список
        self.InitList()
        pass

####################################Иницилизация переменных сущности в список, функция 2 уровня
    def InitList(self):
        self.__ArrGetEntity = [self.__Descripte]

################################гетеры
    def GetID(self):
        return self.__IDTour

    def GetInitList(self):
        return self.__ArrGetEntity

    def GetDescripte(self):
        return self.__Descripte

################################сетеры
    def SetIDTour(self, IDTour):
        self.__IDTour = IDTour
        pass

    def SetDescripte(self, Descripte):
        self.__Descripte = Descripte
        pass