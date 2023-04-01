import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

class caCard(QtWidgets.QWidget):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.layout = QtWidgets.QFormLayout()
		self.setLayout(self.layout)

		self.layout.addRow("Event Name:", QLineEdit())
		self.layout.addRow("Date:", QLineEdit())
		self.layout.addRow("Time:", QLineEdit())
		self.layout.addRow("Location:", QLineEdit())
		self.layout.addRow("CA Name:", QLineEdit())

		self.createButtons()

		self.show()

	def createButtons(self):
		buttonsLayout = QHBoxLayout()

		buttonsLayout.addWidget(QPushButton("Save"))
		buttonsLayout.addWidget(QPushButton("Cancel"))

	
	#def save():
		

	#def cancel():


		