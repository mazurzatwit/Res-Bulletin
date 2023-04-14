import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtGui import *
import createForm
import cardClass
import mysql.connector

#mySQL connection starts

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

    user_permissions = "SELECT User_Name_ID FROM `users` where Permissions = 'No';"
    cursor = connection.cursor()
    cursor.execute(user_permissions)
    # get all records
    records = cursor.fetchall()

    for rows in records:
        print("Student Name = ", rows[0])



class eventWindow(QWidget):
     
        def __init__(self):
            super().__init__()
            self.newEvent = createForm.studentCard()

class mainWindow(QWidget):
	
        def __init__(self):
            super(mainWindow, self).__init__()
            self.setStyleSheet("background: #FDFD96")
            self.setWindowTitle("Residential Hall Event Bulletin - Student View")
            #self.layout = QtWidgets.QGridLayout(mainWindow)
            #setGeometry(left,top,width,height)
            self.setGeometry(500,1000,1100,1000)
            
            #SCROLL
            #self.scroll = QScrollBar(self)
            #self.scroll
            #self.scroll.setMaximum(1000)
        

            self.groupBox = QGroupBox ("Events")
            self.gridLayout = QtWidgets.QGridLayout(self)

            event1 = "SELECT Event_Name, Event_Date, Event_Time FROM `ca_event` WHERE Event_Name = 'Grocery Bingo';"
            cursor = connection.cursor()
            cursor.execute(event1)
            # get all records
            records = cursor.fetchall()

            for row in records:
                  eName = row[0]
                  eDate = row[1]
                  eTime = row[2]

            event = "{eventName} {eventDate} @ {eventTime}".format(eventName = eName, eventDate = eDate, eventTime = eTime)

            self.button = QPushButton(event, self)
            self.button.setMinimumHeight(300)
            self.button.setMinimumWidth(100)
            self.button.setStyleSheet("background: #FFFFFF; border-style: solid; border-width: 4px; border-color: #FFB346")
            self.button.clicked.connect(self.showEventWindow)
            self.gridLayout.addWidget(self.button, 0,0)

            self.button1 = QPushButton("Free Pizza! 1/12/23 @ 5pm", self)
            self.button1.setStyleSheet("background: #FFFFFF; border-style: solid; border-width: 4px; border-color: #FFB346")
            self.button1.setMinimumHeight(300)
            self.button1.setMinimumWidth(100)
            self.gridLayout.addWidget(self.button1, 0,1)

            self.button2 = QPushButton("Destress Fest! 4/11/23 @ 3pm", self)
            self.button2.setStyleSheet("background: #FFFFFF; border-style: solid; border-width: 4px; border-color: #FFB346")
            self.button2.setMinimumHeight(300)
            self.button2.setMinimumWidth(100)
            self.gridLayout.addWidget(self.button2, 0,2)

            self.button3 = QPushButton("Herb Plant Night! 4/5/23 @ 6pm", self)
            self.button3.setStyleSheet("background: #FFFFFF; border-style: solid; border-width: 4px; border-color: #FFB346")
            self.button3.setMinimumHeight(300)
            self.button3.setMinimumWidth(100)
            self.gridLayout.addWidget(self.button3, 0,3)

            self.button4 = QPushButton("Stuffed Animals! 4/13/23 @ 5pm", self)
            self.button4.setStyleSheet("background: #FFFFFF; border-style: solid; border-width: 4px; border-color: #FFB346")
            self.button4.setMinimumHeight(300)
            self.button4.setMinimumWidth(100)
            self.gridLayout.addWidget(self.button4, 2,0)

            #HEADER
            self.logo = QLabel(self)
            pixmap = QPixmap('Res_Logo.jpg')
            self.logo.resize(100,100)
            self.logo.setPixmap(pixmap.scaled(100,100))

            self.appName = QLabel('Residential Hall Event Bulletin', self)
            self.appName.resize(1000,100)
            self.appName.move(150, 0)
            self.appName.setFont(QFont('Tahoma', 75))

            self.welcome = QLabel(self)
            message = "Welcome {name}".format(name = rows[0])
            self.welcome.setText(message)
            self.welcome.resize(900,100)
            self.welcome.move(1300,5)
            self.welcome.setFont(QFont('Tahoma', 30))

            self.dropdown1 = QComboBox(self)
            menuPix = QPixmap('menuIcon.png')
            self.dropdown1.addItem(QIcon(menuPix.scaled(100,100)), 'Menu')
            self.dropdown1.addItem('Switch User')
            self.dropdown1.addItem('Account Settings')
            self.dropdown1.addItem('Logout')
            self.dropdown1.move(1750, 25)
            self.dropdown1.resize(150,50)
            self.dropdown1.setStyleSheet("background: #FFFFFF")


            self.showMaximized()
        
        def showEventWindow(self):
             self.newWindow = eventWindow()
   
def main():
        app = QApplication(sys.argv)
        win = mainWindow()
    
        win.show()
        sys.exit(app.exec_())
main()

cursor.close()
connection.close()


    

