#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
# mainwindow.py

import sys
from PyQt4 import QtGui,QtCore

class MainWindow(QtGui.QMainWindow):

	def __init__(self):
		super(MainWindow,self).__init__()

		self.initUI()

	def initUI(self):
		self.resize(800,600)
		self.setWindowTitle('EverLinux -- Evernote client for linux')

		icon = QtGui.QIcon('../icons/enlogo.png')
		self.setWindowIcon(icon)
		print 'aaa'

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	main = MainWindow()
	main.show()
	sys.exit(app.exec_())