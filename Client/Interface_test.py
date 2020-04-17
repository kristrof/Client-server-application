import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import login  # Это наш конвертированный файл дизайна
import main_window
import Connect
import hashlib
import threading
import asyncio
import pickle



class Log(QtWidgets.QMainWindow, login.Ui_Client_main):


    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле login.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password) # Чтобы пароль не было видно
        self.pushButton.clicked.connect(self.login_in)

    def login_in(self):
        # передаем логин и пароль пользователя на сервер
        login = ""
        pasw = ""
        login = self.lineEdit.text()
        pasw = self.lineEdit_2.text()
        pasw = hashlib.md5(pasw.encode())
        pasw = pasw.hexdigest()
        login_pas = login+' '+pasw
        msg = '1 '

        Connect.snd(login_pas, msg,sock)
        res = Connect.rec(sock)
        if res.decode('utf-8') == "true":
            self.window2 = main_win()
            self.window2.show()
            self.window().close()



class main_win(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.table)
        self.pushButton_2.clicked.connect(self.ins_row)
        self.pushButton_3.clicked.connect(self.ins_row_bd)




    def table(self):
        global count
        count = 0
        #Для вывода таблицы нужной пользователю
        name = ""
        msg = ""
        name = self.lineEdit.text()
        msg = "2 "
        Connect.snd(name, msg, sock)
        massiv = Connect.rec(sock)
        massiv = pickle.loads(massiv)
        # количество столбцов и строк в зависимости от полученных данных
        self.tableWidget.setRowCount(len(massiv))
        self.tableWidget.setColumnCount(len(massiv[0]))
        global rows
        rows = len(massiv)
        global column
        column = len(massiv[0])
        # очищаем таблицу
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(["Id","Data"])
        # заполняем таблицу
        row = 0
        for tup in massiv:
            col = 0
            for item in tup:
                cellinfo = QTableWidgetItem(str(item))
                self.tableWidget.setItem(row, col, cellinfo)
                col +=1
            row +=1
        #self.tableWidget.insertRow(4)



    def ins_row(self):
        # для вставки новой строки в таблицу
        test = self.tableWidget.rowCount()
        self.tableWidget.insertRow(test)
        global count
        count = count+1



    def ins_row_bd(self):
        # передаем данные для вставки в таблицу на сервере
        massiv1 = []
        i = 0
        for i in range(count):
            j = 0
            s = []
            for j in range(column):
                s.insert(j, self.tableWidget.item(i + rows, j ).text())
                j+=1
            massiv1.insert(i, tuple(s))
            i+=1
        # тут пока только так
        row_for_bd = ""
        for tup in massiv1:
            for item in tup:
                row_for_bd = row_for_bd  +"'"+item+"'"+ ","
            row_for_bd = row_for_bd+ ":"
        msg = "3 "
        Connect.snd(row_for_bd,msg ,sock)



    def closeEvent(self, event):
        data = ""
        msg = "0"
        Connect.snd(data, msg, sock)
        Connect.close_sock(sock)



def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Log()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    global sock
    sock = Connect.connect()
    sys.exit(app.exec_())  # и запускаем приложение



if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()