import sqlite3 as lite
#класс работы с файлом базы данных
class ResourceManager :

    def __init__(self):
        self.__con = lite.connect('DATA.db3')
        self.__cur = self.__con.cursor()
        #self.InitDataBase()
        pass

    #что бы заполнить базу данных начальными данными
    def InitDataBase(self):
        with self.__con:
            self.__cur.execute("PRAGMA foreign_keys=on;")
            self.__cur.execute("CREATE TABLE IF NOT EXISTS Country (CodeCountry INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NameCountry TEXT NOT NULL);")
            self.__cur.execute("CREATE TABLE IF NOT EXISTS Resort (IDResort INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NameResort TEXT NOT NULL, DescriptionResort TEXT NOT NULL, CodeOfTheCountry INTEGER NOT NULL, FOREIGN KEY (CodeOfTheCountry) REFERENCES Country(CodeCountry));")
            self.__cur.execute("CREATE TABLE IF NOT EXISTS Hotel (IDHotel INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, HotelCategory INTEGER NOT NULL, Name TEXT NOT NULL, HotelDescription TEXT NOT NULL, id_Resort INTEGER NOT NULL, FOREIGN KEY (id_Resort) REFERENCES Resort(IDResort));")
            self.__cur.execute("CREATE TABLE IF NOT EXISTS Flight (FlightNumber INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Destination TEXT NOT NULL, DepartureDate NUMERIC NOT NULL, Price REAL NOT NULL, TravelTime TEXT NOT NULL, id_Resort INTEGER NOT NULL, FOREIGN KEY (id_Resort) REFERENCES Resort(IDResort));")
            self.__cur.execute("CREATE TABLE IF NOT EXISTS Client (IdClient INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FIOName TEXT NOT NULL, address TEXT NOT NULL, DateOfBirth NUMERIC NOT NULL, telephone INTEGER NOT NULL);")
            self.__cur.execute("CREATE TABLE IF NOT EXISTS Tour (IDTour INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Descripte TEXT NOT NULL, ID_Client INTEGER NOT NULL, ID_Hotel INTEGER NOT NULL, Flight_Number INTEGER NOT NULL, FOREIGN KEY (ID_Client) REFERENCES Client(IdClient), FOREIGN KEY (ID_Hotel) REFERENCES Hotel(IDHotel), FOREIGN KEY (Flight_Number) REFERENCES Flight(FlightNumber));")

            self.__cur.execute("CREATE TABLE IF NOT EXISTS Country (CodeCountry INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NameCountry TEXT NOT NULL);")
            self.__cur.execute("INSERT OR REPLACE INTO Country VALUES(643, 'РОССИЯ')")
            self.__cur.execute("INSERT OR REPLACE INTO Country VALUES(440, 'ЛИТВА')")
            self.__cur.execute("INSERT OR REPLACE INTO Country VALUES(276, 'ГЕРМАНИЯ')")
            self.__cur.execute("INSERT OR REPLACE INTO Country VALUES(112, 'КАНАДА')")
            self.__cur.execute("INSERT OR REPLACE INTO Country VALUES(124, 'БЕЛАРУСЬ')")

            self.__cur.execute("CREATE TABLE IF NOT EXISTS Resort (IDResort INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NameResort TEXT NOT NULL, DescriptionResort TEXT NOT NULL, CodeOfTheCountry INTEGER NOT NULL, FOREIGN KEY (CodeOfTheCountry) REFERENCES Country(CodeCountry));")
            self.__cur.execute("INSERT OR REPLACE INTO Resort VALUES(1, 'Адлер', 'Один из городских районов города Сочи, административный центр Адлерского района.', 643)")
            self.__cur.execute("INSERT OR REPLACE INTO Resort VALUES(2, 'Гай - город', 'Город в России, административный центр Гайского городского округа Оренбургской области.', 643)")
            self.__cur.execute("INSERT OR REPLACE INTO Resort VALUES(3, 'Приморско-Ахтарск', 'Город в Краснодарском крае. Административный центр Приморско-Ахтарского района, а также Приморско-Ахтарского городского поселения.', 643)")
            self.__cur.execute("INSERT OR REPLACE INTO Resort VALUES(4, 'Каунас', 'Каунас (Kaunas) — второй по величине и значению город Литвы был основан в 1280 году на месте слияния двух самых больших литовских рек', 440)")
            self.__cur.execute("INSERT OR REPLACE INTO Resort VALUES(5, 'Ванкувер ', 'Один из пяти красивейших океанских городов мира, наряду с Сиднеем, Кейптауном, Сан-Франциско и Рио-де-Жанейро.', 112)")

            self.__cur.execute("CREATE TABLE IF NOT EXISTS Hotel (IDHotel INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, HotelCategory INTEGER NOT NULL, Name TEXT NOT NULL, HotelDescription TEXT NOT NULL, id_Resort INTEGER NOT NULL, FOREIGN KEY (id_Resort) REFERENCES Resort(IDResort));")
            self.__cur.execute("INSERT OR REPLACE INTO Hotel VALUES(1, 3, 'Гранд Отель Жемчужина', '1-я пляжная линиягалечный пляжбесплатный wi-fi в номере', 1)")
            self.__cur.execute("INSERT OR REPLACE INTO Hotel VALUES(2, 5, 'Marriott Красная Поляна Отель', 'бесплатный wi-fi в номереплатный wi-fi в номерепостроен в 2013 году', 1)")
            self.__cur.execute("INSERT OR REPLACE INTO Hotel VALUES(3, 1, 'Горняк', 'Гостиница Горняк расположена в центре города на первых двух этажах жилого дома.', 2)")
            self.__cur.execute("INSERT OR REPLACE INTO Hotel VALUES(4, 2, 'Отель Марисоль', '21 номерресторанбарпрокат велосипедов', 3)")
            self.__cur.execute("INSERT OR REPLACE INTO Hotel VALUES(5, 2, 'Tropicana Suite Hotel', 'бесплатный wi-fi в номере74 номералифтресторанбар', 5)")
            self.__cur.execute("INSERT OR REPLACE INTO Hotel VALUES(6, 4, 'Auberge Vancouver Hotel', ' бесплатный wi-fi в номереплатный wi-fi в номере58 номеровлифтресторан', 5)")

            self.__cur.execute("CREATE TABLE IF NOT EXISTS Flight (FlightNumber INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Destination TEXT NOT NULL, DepartureDate NUMERIC NOT NULL, Price REAL NOT NULL, TravelTime TEXT NOT NULL, id_Resort INTEGER NOT NULL, FOREIGN KEY (id_Resort) REFERENCES Resort(IDResort));")
            self.__cur.execute("INSERT OR REPLACE INTO Flight VALUES(111777, 'Адлер', date('NOW'), 850.70, '02:34:56', 1)")
            self.__cur.execute("INSERT OR REPLACE INTO Flight VALUES(223133, 'Адлер', date('2018-01-06'), 950.20, '02:40:00', 1)")
            self.__cur.execute("INSERT OR REPLACE INTO Flight VALUES(478383, 'Гай - город', date('2018-02-09'), 500.30, '01:40:00', 2)")
            self.__cur.execute("INSERT OR REPLACE INTO Flight VALUES(231234, 'Ванкувер', date('2018-01-02'), 2500.20, '15:40:00', 5)")

            self.__cur.execute("CREATE TABLE IF NOT EXISTS Client (IdClient INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FIOName TEXT NOT NULL, address TEXT NOT NULL, DateOfBirth NUMERIC NOT NULL, telephone INTEGER NOT NULL);")
            self.__cur.execute("INSERT OR REPLACE INTO Client VALUES(1, 'Гончаров Евгений Андреевич', 'Москва Проспект Вернадского', date('1994-02-06'), 89253719296)")
            self.__cur.execute("INSERT OR REPLACE INTO Client VALUES(2, 'Брежнева Татьяна Леонидовна' , 'Москва Преображенская', date('1995-03-02'), 89163752229)")
            self.__cur.execute("INSERT OR REPLACE INTO Client VALUES(3, 'Драгонову Дарья Андреевна' , 'Москва Авиамоторная', date('1997-06-06'), 89772283322)")

            self.__cur.execute("CREATE TABLE IF NOT EXISTS Tour (IDTour INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Descripte TEXT NOT NULL, ID_Client INTEGER NOT NULL, ID_Hotel INTEGER NOT NULL, Flight_Number INTEGER NOT NULL, FOREIGN KEY (ID_Client) REFERENCES Client(IdClient), FOREIGN KEY (ID_Hotel) REFERENCES Hotel(IDHotel), FOREIGN KEY (Flight_Number) REFERENCES Flight(FlightNumber));")
            self.__cur.execute("INSERT OR REPLACE INTO Tour VALUES(1, 'Отпуск, как отпуск', 1, 2, 111777)")
            self.__cur.execute("INSERT OR REPLACE INTO Tour VALUES(2, 'Путешествует', 3, 6, 231234)")
        pass
################################исполнение скрипта, внешнии функции

    def Execute(self, script):
        print(script)
        with self.__con:
            try:
                self.__cur.executescript(script)
            except lite.DatabaseError:
                print("False")
                return False
            else:
                return True


    def ExecuteReturn(self, script, scriptID):
        self.__cur.execute(script, scriptID)
        rows = self.__cur.fetchall()
        return rows

################################гетеры
    def GetListClientSQL(self):
        self.__cur.execute("SELECT * FROM Client")  # Этот SQL запрос выбирает все данные из таблицы Cars.
        rows = self.__cur.fetchall()
        return rows

    def GetListTourSQL(self):
        self.__cur.execute("SELECT * FROM Tour")  # Этот SQL запрос выбирает все данные из таблицы Cars.
        rows = self.__cur.fetchall()
        return rows

    def GetListCountrySQL(self):
        self.__cur.execute("SELECT * FROM Country")  # Этот SQL запрос выбирает все данные из таблицы Cars.
        rows = self.__cur.fetchall()
        return rows

    def GetListHotelSQL(self):
        self.__cur.execute("SELECT * FROM Hotel")  # Этот SQL запрос выбирает все данные из таблицы Cars.
        rows = self.__cur.fetchall()
        return rows

    def GetListResortSQL(self):
        self.__cur.execute("SELECT * FROM Resort")  # Этот SQL запрос выбирает все данные из таблицы Cars.
        rows = self.__cur.fetchall()
        return rows

    def GetListFlightSQL(self):
        self.__cur.execute("SELECT * FROM Flight")  # Этот SQL запрос выбирает все данные из таблицы Cars.
        rows = self.__cur.fetchall()
        return rows