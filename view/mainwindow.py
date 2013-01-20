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
		