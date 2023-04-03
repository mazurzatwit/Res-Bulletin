import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import Qt
from PyQt5.QtCore import Qt

class caCard(QtWidgets.QWidget):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.layout = QtWidgets.QFormLayout()
		self.setLayout(self.layout)
		self.setFixedSize(500,500)
		#eventDetails = []
		eventName = QLineEdit()

		self.layout.addRow("Event Name:", eventName)
		self.layout.addRow("Date:", QLineEdit())
		self.layout.addRow("Time:", QLineEdit())
		self.layout.addRow("Location:", QLineEdit())
		self.layout.addRow("CA Name:", QLineEdit())

		#eventDetails = [eventName.text()]
		#self.keyPressEvent() 

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


	def keyPressEvent(self, event):
		eventName = QLineEdit()
		if (event.key() == Qt.Key.Key_Return) or (event.key() == Qt.Key.Key_Enter):
			return eventName.text()
	
	#def save():
		

	def cancel(self):
		self.close()


		