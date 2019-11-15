# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mywin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5.QtWidgets import QWidget,QApplication

app=QApplication(sys.argv)
win=QWidget()
win.resize(400,300)
win.move(300,300)
win.setWindowTitle('我的第一个pyqt5程序')
win.show()
sys.exit(app.exec_())

