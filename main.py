import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
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


class mainWindow(QWidget):
	
        def __init__(self):
            super(mainWindow, self).__init__()
            self.setStyleSheet("background: #FDFD96")
            self.setWindowTitle("Residential Hall Event Bulletin")
            #self.layout = QtWidgets.QGridLayout(mainWindow)
            
            
            self.groupBox = QGroupBox ("Events")
            self.gridLayout = QtWidgets.QGridLayout(self)

            self.button = QPushButton("Mocktails! 3/21/23 @ 7pm", self)
            self.button.setMinimumHeight(400)
            self.button.setMinimumWidth(100)
            self.button.setStyleSheet("background: #FFFFFF; border-style: solid; border-width: 4px; border-color: #FFB346")
            self.gridLayout.addWidget(self.button, 0,0)

            self.button1 = QPushButton("Free Pizza! 1/12/23 @ 5pm", self)
            self.button1.setStyleSheet("background: #FFFFFF; border-style: solid; border-width: 4px; border-color: #FFB346")
            self.button1.setMinimumHeight(400)
            self.button1.setMinimumWidth(100)
            self.gridLayout.addWidget(self.button1, 0,1)

            self.button2 = QPushButton("Destress Fest! 4/11/23 @ 3pm", self)
            self.button2.setStyleSheet("background: #FFFFFF; border-style: solid; border-width: 4px; border-color: #FFB346")
            self.button2.setMinimumHeight(400)
            self.button2.setMinimumWidth(100)
            self.gridLayout.addWidget(self.button2, 0,2)

            self.button3 = QPushButton("Herb Plant Night! 4/5/23 @ 6pm", self)
            self.button3.setStyleSheet("background: #FFFFFF; border-style: solid; border-width: 4px; border-color: #FFB346")
            self.button3.setMinimumHeight(400)
            self.button3.setMinimumWidth(100)
            self.gridLayout.addWidget(self.button3, 0,3)

            #self.groupBox.setLayout(gridLayout)

            #events = ['Mocktails! 3/21/23 @ 7pm', 'Free Pizza! 1/12/23 @ 5pm', 'Destress Fest! 4/11/23 @ 3pm', 'Herb Plant Night! 4/5/23 @ 6pm']
            
            #positions = [(i, j) for i in range(3) for j in range(3)]

            #for i in range(1,3):
                #for j in range(1,3):
                    #self.layout.addWidget(QPushButton(events[i]),i,j)
                    
            #for position, event in zip(positions, events):
                #if event == '':
                    #continue
                #button = QPushButton(event)
                #self.layout.addWidget(button, *position)
            
            #self.setLayout(self.layout)
            self.createButton = QtWidgets.QPushButton(self)
            self.createButton.setText('Create')
            #self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            self.createButton.setStyleSheet("background: #FFFFFF; border-style: solid; border-width: 4px; border-color: #FF6962")
            self.createButton.clicked.connect(self.createNewEvent)
            self.createButton.move(1200,25)
            self.createButton.resize(150,50)
            self.createButton.setFont(QFont('Tahoma', 25))

            self.logo = QLabel(self)
            pixmap = QPixmap('Res_Logo.jpg')
            self.logo.resize(100,100)
            self.logo.setPixmap(pixmap.scaled(100,100))

            self.appName = QLabel('Residential Hall Event Bulletin', self)
            self.appName.resize(1000,100)
            self.appName.move(150, 0)
            self.appName.setFont(QFont('Abril Fatface', 75))

            self.welcome = QLabel(self)
            message = "Welcome {name}".format(name = row[0])
            self.welcome.setText(message)
            self.welcome.resize(900,100)
            self.welcome.move(1450,5)
            self.welcome.setFont(QFont('Tahoma', 30))

            self.dropdown1 = QComboBox(self)
            menuPix = QPixmap('menuIcon.png')
            self.dropdown1.addItem(QIcon(menuPix.scaled(100,100)), 'Menu')
            self.dropdown1.addItem('Switch User')
            self.dropdown1.addItem('Account Settings')
            self.dropdown1.addItem('Logout')
            self.dropdown1.move(1800, 25)
            self.dropdown1.resize(150,50)
            self.dropdown1.setStyleSheet("background: #FFFFFF")

            self.showMaximized()

        def createNewEvent(self):
            self.newEvent = createForm.caCard()
                
def main():
        app = QApplication(sys.argv)
        win = mainWindow()
        grid = QGridLayout(win)
    
        win.show()
        sys.exit(app.exec_())
main()
		


    

