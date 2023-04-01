import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import createForm
import mysql.connector
from mysql.connector import Error

#mySQL connection starts
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Res Bulletin',
                                         user='root')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

        user_permissions = "SELECT User_Name_ID FROM `users` where Permissions = 'Yes';"
        cursor = connection.cursor()
        cursor.execute(user_permissions)
        # get all records
        records = cursor.fetchall()

        for row in records:
            print("CA Name = ", row[0], )

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


class mainWindow(QMainWindow):
	
        def __init__(self):
            super(mainWindow, self).__init__()
            self.setStyleSheet("background: #FDFD96")
            self.setFixedSize(400, 400)
            self.setWindowTitle("Residential Hall Event Bulletin")
            self.layout = QtWidgets.QGridLayout()
            self.setLayout(self.layout)
            
            self.createButton = QtWidgets.QPushButton(self)
            self.createButton.setText('Create')
            self.createButton.setStyleSheet("background: #FF6962")
            self.createButton.clicked.connect(self.createNewEvent)

            #self.layout.addWidget(self.createButton.clicked.connect(self.createNewEvent), 0, 0)

            self.show()

        def createNewEvent(self):
            #self.newEvent = createForm.caCard()
            print('test please work!')
                
def main():
	app = QApplication(sys.argv)
	win = mainWindow()
	win.show()
	sys.exit(app.exec_())
main()
		


    

