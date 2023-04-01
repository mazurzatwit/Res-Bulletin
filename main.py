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
            self.setWindowTitle("Residential Hall Event Bulletin")
            #self.layout = QtWidgets.QGridLayout()
            label = QLabel()
            label.setText("PPPPLLLLLEEEAAAASSSSSEEEEEE")
            
            self.groupBox = QGroupBox ("Events")
            gridLayout = QGridLayout()

            self.button = QPushButton("Mocktails! 3/21/23 @ 7pm", self)
            self.button.setMinimumHeight(30)
            gridLayout.addWidget(self.button, 0,0)

            self.button1 = QPushButton("Mocktails! 3/21/23 @ 7pm", self)
            self.button1.setMinimumHeight(30)
            gridLayout.addWidget(self.button1, 0,1)

            self.button2 = QPushButton("Mocktails! 3/21/23 @ 7pm", self)
            self.button2.setMinimumHeight(30)
            gridLayout.addWidget(self.button2, 1,0)

            self.button3 = QPushButton("Mocktails! 3/21/23 @ 7pm", self)
            self.button3.setMinimumHeight(30)
            gridLayout.addWidget(self.button3, 1,1)

            self.groupBox.setLayout(gridLayout)

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
            self.createButton.setStyleSheet("background: #FF6962")
            self.createButton.clicked.connect(self.createNewEvent)

            self.Button4 = QtWidgets.QPushButton(self)
            self.Button4.setText('Hello???????')
            self.Button4.setStyleSheet("background: #FF6962")
            self.Button4.move(150,200)

            self.showMaximized()

        def createNewEvent(self):
            self.newEvent = createForm.caCard()
                
def main():
        app = QApplication(sys.argv)
        win = mainWindow()
        vbox = QVBoxLayout()
        vbox.addWidget(win.groupBox)
        win.setLayout(vbox)    
        win.show()
        sys.exit(app.exec_())
main()
		


    

