#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
# login.py

import sys
from PyQt4 import QtCore,QtGui

class LoginWindow(QtGui.QWidget):
	def __init__(self):
		super(LoginWindow, self).__init__()
		
		self.initUI()

	def initUI(self):

		self.resize(350,200)
		self.setWindowTitle('please login your account')

		icon = QtGui.QIcon('../icons/enlogo.png')
		self.setWindowIcon(icon)

		username = QtGui.QLabel('account:')
		password = QtGui.QLabel('password:')

		unInput = QtGui.QLineEdit()
		pwInput = QtGui.QLineEdit()

		cbNotAgain = QtGui.QCheckBox('alway sign in')


		btnReg = QtGui.QCommandLinkButton('create account', 'create account for free')
		btnSubmit = QtGui.QCommandLinkButton('Sign In', 'sign in your account')

		grid = QtGui.QGridLayout()
		grid.setSpacing(10)

		grid.addWidget(username, 1, 0)
		grid.addWidget(unInput, 1, 1)

		grid.addWidget(password, 2, 0)
		grid.addWidget(pwInput, 2, 1)

		grid.addWidget(cbNotAgain, 3, 0, 1, 2)

		hbox = QtGui.QHBoxLayout()
		hbox.addWidget(btnReg)
		hbox.addWidget(btnSubmit)

		vbox = QtGui.QVBoxLayout()
		vbox.addLayout(grid)
		vbox.addLayout(hbox)

		self.setLayout(vbox)
		self.center()

	#center windows
	def center(self):
		screen = QtGui.QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	login = LoginWindow()
	login.show()
	sys.exit(app.exec_())

