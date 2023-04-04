import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import Qt
from PyQt5.QtCore import Qt
import cardClass

global test

class caCard(QtWidgets.QWidget):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.layout = QtWidgets.QFormLayout()
		self.setLayout(self.layout)
		self.setFixedSize(500,500)
		#eventDetails = []
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
		self.buttonsLayout = QHBoxLayout()

		self.saveBtn = QtWidgets.QPushButton(self)
		self.saveBtn.move(150,200)
		self.cancelBtn = QtWidgets.QPushButton(self)
		self.cancelBtn.move(250,200)
		self.saveBtn.setText('Save')
		self.cancelBtn.setText('Cancel')
		self.cancelBtn.clicked.connect(self.cancel)

	
	def save(self):
		eName = self.eventName.text()
		eDate = self.date.text()
		eTime = self.time.text()
		eLocation = self.location.text()
		eCA = self.caName.text()

		event = "{eventName} {eventDate} @ {eventTime}".format(eventName = eName, eventDate = eDate, eventTime = eTime)

		self.newButton = QPushButton(event, self)
		self.newButton.setStyleSheet("background: #FFFFFF; border-style: solid; border-width: 4px; border-color: #FFB346")
		self.newButton.setMinimumHeight(400)
		self.newButton.setMinimumWidth(100)

		eventCreated = cardClass.Card() #backend save

		return self.newButton


		

	def cancel(self):
		self.close()


		