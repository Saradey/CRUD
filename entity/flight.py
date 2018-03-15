#рейс
class Flight :
    def __init__(self, ArrClient) :
        self.__FlightNumber = ArrClient[0]  #айди рейса
        self.__Destination = ArrClient[1]    #пункт назначения
        self.__DepartureDate = ArrClient[2]    #дата отправления
        self.__Price = ArrClient[3]    #цена
        self.__TravelTime = ArrClient[4] #время в пути
        self.__ArrGetEntity = []  # переменных сущности в список
        self.InitList()
        pass

####################################Иницилизация переменных сущности в список, функция 2 уровня
    def InitList(self):
        self.__ArrGetEntity = [self.__FlightNumber, self.__Destination,
                               self.__DepartureDate, self.__Price, self.__TravelTime]

################################гетеры
    def GetID(self):
        return self.__FlightNumber

    def GetDestination(self):
        return self.__Destination

    def GetDepartureDate(self):
        return self.__DepartureDate

    def GetPrice(self):
        return self.__Price

    def GetTravelTime(self):
        return self.__TravelTime

    def GetInitList(self):
        return self.__ArrGetEntity

################################сетеры
    def SetFlightNumber(self, FlightNumber):
        self.__FlightNumber = FlightNumber
        pass

    def SetDestination(self, Destination):
        self.__Destination = Destination
        pass

    def SetDepartureDate(self, DepartureDate):
        self.__DepartureDate = DepartureDate
        pass

    def SetPrice(self, Price):
        self.__Price = Price
        pass

    def SetTravelTime(self, TravelTime):
        self.__TravelTime = TravelTime
        pass