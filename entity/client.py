#клиент
class Client :
    def __init__(self, ArrClient) :
        self.__IdClient = ArrClient[0]
        self.__FIOName = ArrClient[1]  #имя
        self.__address = ArrClient[2]
        self.__DateOfBirth = ArrClient[3]    #дата рождения
        self.__telephone = ArrClient[4]
        self.__ArrGetEntity = []        #переменных сущности в список
        self.InitList()
        pass

####################################Иницилизация переменных сущности в список, функция 2 уровня
    def InitList(self):
        self.__ArrGetEntity = [self.__FIOName, self.__address, self.__DateOfBirth, self.__telephone]

    ################################гетеры
    def GetID(self):
        return self.__IdClient

    def GetFIO(self):
        return self.__FIOName

    def GetAdress(self):
        return self.__address

    def GetDateOfBirth(self):
        return self.__DateOfBirth

    def GetTelephone(self):
        return self.__telephone

    def GetInitList(self):
        return self.__ArrGetEntity

    ################################сетеры
    def SetId(self, Id):
        self.__IdClient = Id
        pass

    def SetFIO(self, FIO):
        self.__FIOName = FIO
        pass

    def SetAdress(self, Adress):
        self.__address = Adress
        pass

    def SetDateOfBirth(self, DateOfBirth):
        self.__DateOfBirth = DateOfBirth
        pass

    def SetTelephone(self, telephone):
        self.__telephone = telephone
        pass
