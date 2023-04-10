import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
import cardClass


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
		#QtCore.QObject.connect(self.saveBtn, QtCore.SIGNAL('clicked()'), self.showSavePopUp)
		#QtCore.QObject.connect(self.saveBtn, QtCore.SIGNAL('clicked()'), self.save)

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

	


		