import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
import cardClass
import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                         database='Res Bulletin',
                                         user='root')
cursor = connection.cursor()


class caCard(QtWidgets.QWidget):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.layout = QtWidgets.QFormLayout()
		self.setLayout(self.layout)
		self.setFixedSize(500,500)
		self.eventName = QLineEdit()
		self.date = QLineEdit()
		self.time = QLineEdit()
		self.location = QLineEdit()
		self.caName = QLineEdit()
		

		self.layout.addRow("Event Name:", self.eventName)
		self.layout.addRow("Date:", self.date)
		self.layout.addRow("Time:", self.time)
		self.layout.addRow("Location:", self.location)
		self.layout.addRow("CA Name:", self.caName)

		self.createButtons()

		self.show()

	def createButtons(self):
		self.saveBtn = QtWidgets.QPushButton(self)
		self.saveBtn.move(150,200)
		self.cancelBtn = QtWidgets.QPushButton(self)
		self.cancelBtn.move(250,200)
		self.saveBtn.setText('Save')
		self.cancelBtn.setText('Cancel')
		self.cancelBtn.clicked.connect(self.cancel)
		self.saveBtn.clicked.connect(self.showSavePopUp)
		self.saveBtn.clicked.connect(self.save)
	

	def save(self):
		eName = self.eventName.text()
		eDate = self.date.text()
		eTime = self.time.text()
		eLocation = self.location.text()
		eCA = self.caName.text()

		eventInfo = [eName, eDate, eTime, eLocation, eCA]
		print(eventInfo)

		self.eventCreated = cardClass.Card() #backend save
		self.eventCreated.create(eName,eDate,eTime,eLocation,eCA)

	def showSavePopUp(self):
		msg=QMessageBox()
		msg.setWindowTitle("Save")
		msg.setText("Confirm save of event information?")
		msg.setIcon(QMessageBox.Information)
		msg.setStandardButtons(QMessageBox.Save|QMessageBox.Cancel)

		msg.buttonClicked.connect(self.savePopUp)
		
		msg.exec()		

	def savePopUp(self, i):
		self.close()


	def cancel(self):
		self.close()

		
class studentCard(QtWidgets.QWidget):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.layout = QtWidgets.QFormLayout()
		self.setLayout(self.layout)
		self.setFixedSize(500,500)
		self.attendance = QWidget()
		self.layout_h = QHBoxLayout(self.attendance)


		studentInfo = "SELECT * From Student_Card WHERE Event_Name = 'Grocery Bingo'"
		cursor = connection.cursor()
		cursor.execute(studentInfo)
        # get all records
		records = cursor.fetchall()

		for row in records:
			ename = row[0]
			edate = row[1]
			etime = row[2]
			elocation = row[3]
			eCA = row[4]
			eYes = row[5]
			eMaybe = row[6]
			eNo = row[7]
			eForum = row[8]
		
		self.eventName = QLabel(ename)
		self.date = QLabel(edate)
		self.time = QLabel(etime)
		self.location = QLabel(elocation)
		self.caName = QLabel(eCA)
		self.yes = QLabel(eYes)
		self.no = QLabel(eNo)
		self.maybe = QLabel(eMaybe)

		self.layout_h.addWidget(self.yes)
		self.layout_h.addWidget(self.no)
		self.layout_h.addWidget(self.maybe)

		self.layout.addRow("Event Name:", self.eventName)
		self.layout.addRow("Date:", self.date)
		self.layout.addRow("Time:", self.time)
		self.layout.addRow("Location:", self.location)
		self.layout.addRow("CA Name:", self.caName)

		self.rating = QLineEdit()
		self.rating.setPlaceholderText("Enter a number:")
		self.comment = QLineEdit()
		self.comment.setPlaceholderText("Enter a comment:")
		self.layout.addRow("Rating (Scale: 1-5): ", self.rating)
		self.layout.addRow("Comment: ", self.comment)
	
		self.closeBtn = QtWidgets.QPushButton(self)
		self.closeBtn.move(200,250)
		self.closeBtn.setText('Close')
		self.closeBtn.clicked.connect(self.closed)
		
		
		self.show()

	def closed(self):
		self.close()


		

