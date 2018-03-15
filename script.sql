PRAGMA foreign_keys=on

CREATE TABLE IF NOT EXISTS Country 
(

CodeCountry INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 

NameCountry TEXT NOT NULL

)


CREATE TABLE IF NOT EXISTS Resort 
(

IDResort INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 

NameResort TEXT NOT NULL, 

DescriptionResort TEXT NOT NULL, 

CodeOfTheCountry INTEGER NOT NULL, 

FOREIGN KEY (CodeOfTheCountry) REFERENCES Country(CodeCountry)

)


CREATE TABLE IF NOT EXISTS Hotel 

(

IDHotel INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 

HotelCategory INTEGER NOT NULL, 

Name TEXT NOT NULL, 

HotelDescription TEXT NOT NULL, 

id_Resort INTEGER NOT NULL, 

FOREIGN KEY (id_Resort) REFERENCES Resort(IDResort)
)


CREATE TABLE IF NOT EXISTS Flight 

(

FlightNumber INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 

Destination TEXT NOT NULL, 

DepartureDate NUMERIC NOT NULL, 

Price REAL NOT NULL, 

TravelTime TEXT NOT NULL, 

id_Resort INTEGER NOT NULL, 

FOREIGN KEY (id_Resort) REFERENCES Resort(IDResort)

)


CREATE TABLE IF NOT EXISTS Client 

(

IdClient INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 

FIOName TEXT NOT NULL, 

address TEXT NOT NULL, 

DateOfBirth NUMERIC NOT NULL, 

telephone INTEGER NOT NULL

)


CREATE TABLE IF NOT EXISTS Tour 

(

IDTour INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 

Descripte TEXT NOT NULL, 

ID_Client INTEGER NOT NULL, 

ID_Hotel INTEGER NOT NULL, 

Flight_Number INTEGER NOT NULL, 

FOREIGN KEY (ID_Client) REFERENCES Client(IdClient), 

FOREIGN KEY (ID_Hotel) REFERENCES Hotel(IDHotel), 

FOREIGN KEY (Flight_Number) REFERENCES Flight(FlightNumber)

)

 c.execute("DELETE FROM SHPKD WHERE decimal='%s' AND recordnumber='%s'" % (self.decimal_to_edit,
                                                                                      self.selected_key))