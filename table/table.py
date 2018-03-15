from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QMessageBox

#adapter
class Table :

    def __init__(self, resourceManager):
        self.__QTableWidget = QTableWidget()    #таблица
        self.__resourceManager = resourceManager
        self.___EntityListTeamp = []            #список сущностей
        self.__RowCout = 0                      #количество сущностей
        pass

#############################помещаем список сущностей в список таблицы
    def SetListEntityTable(self, _entityList):
        self.___EntityListTeamp = _entityList.GetArrEntity()
        self.__RowCout = _entityList.GetSizeRow()
        self.__SizeColumn = _entityList.GetSizeColumn()

        self.__DB = _entityList.GetNameTable()      #флаг имени таблицы для удаления записи
        self.__ID = _entityList.GetID()         #флаг имени записи для удаления
        self.__id =_entityList.GetIdArr()

        self.__QTableWidget.clear()

        self.__QTableWidget.setColumnCount(_entityList.GetSizeColumn())
        self.__QTableWidget.setRowCount(self.__RowCout)
        self.__QTableWidget.setHorizontalHeaderLabels(_entityList.GetArrColumn())
        pass

    def DeleteRow(self):

        row = 0
        for it in self.__QTableWidget.selectedItems():
            row = it.row()

        teamp = "DELETE FROM "+ self.__DB +" WHERE "+ self.__ID +" ="+ str(self.__id[row]) +";"
        if(self.__resourceManager.Execute(teamp)) :
            print("Done")

        self.__QTableWidget.removeRow(row)

        pass

    def Save(self):
        if self.__DB == 'Client' :
            self.SaveClient()
        if self.__DB == 'Tour' :
            self.SaveTour()
        if self.__DB == 'Country' :
            self.SaveCountry()
        if self.__DB == 'Flight' :
            self.SaveFlight()
        if self.__DB == 'Hotel' :
            self.SaveHotel()
        if self.__DB == 'Resort' :
            self.SaveHResort()
        pass

        pass

#############################создаем нашу таблицу и выгружаем туда весь список
    #загружаем таблицу, функция 2 уровня
    def GreatTable(self):
        i = -1
        j = 0
        for column in self.___EntityListTeamp :
            TeamInitList = column.GetInitList()
            i += 1
            j = 0
            for row in TeamInitList :
                self.__QTableWidget.setItem(i, j, QTableWidgetItem(str(row)))
                j += 1

        self.__QTableWidget.resizeColumnsToContents()
        pass

    def SaveClient(self):
        rows = []

        it = 0
        jt = 0
        while(it < self.__RowCout):
            while(jt < 4):
                rows.append(self.__QTableWidget.item(it, jt).text())
                jt += 1
            pass
            print(rows)
            if self.__resourceManager.Execute("UPDATE Client SET FIOName = '"+rows[0]+"', address = '"+rows[1]+"', DateOfBirth = '"+rows[2]+"', telephone ='"+rows[3]+"'  WHERE IdClient =" + str(it + 1) + ";"):
                print("Done")
            it += 1
            jt = 0
            rows.clear()
        pass



        pass

#############################гетеры
    def GreatGetTable(self):
        self.GreatTable()
        return self.__QTableWidget