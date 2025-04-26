import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QSize
from PyQt5.QtCore import QTimer
import time

# LATEST

# jlkjlkjlkjk

#ldkfjjalsdjfl;ak

#adfja;sldjfl;kasdf
# kjhkljhklhklhjk


#adjfalkdsjflasdjf;lkasdjf

# 45454545454545

#NEW THUNG

# adjfalkdjfal;kjdfasdf


# NEWERWER 1049


# NEW branch, 10:28

# LATEST 10:26



# HelloWorld.py


# asdklfjalkdsfjalkdsfj

#2322322323323232


# eeeeeeeeerrrrrrrrreeeeeee

#akdjfa;lkdsfj  M<XZCN>XMZcnc mxcn.MNXc.M
# VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
# NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN

#nnvmzxcnv  nzxcnvz.,mcnvz  nzxc,vnz,mcv


# bbbbbbbbbbbbbbBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB

# 7777777777777777777777777777777777777777777777


# 555555555555555555555 55555555555555 55555555555 555555555 

# vvvvvvvvvvvvvvv Larest 

# HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH MM

class HelloWindow ( QMainWindow ) :

    def handleTimer(self) :
        lTime = time.localtime ( time.time () )
        localtime = time.asctime ( lTime )
        self.timeLab.setText ( localtime )
        self.SetSize ( lTime )

    def __init__(self) :
        self.SetMainStyle()

        self.setWindowTitle ( "CSU" )

        central_widget = QWidget ( self )
        self.setCentralWidget ( central_widget )

        grid_layout = QGridLayout ( self )
        central_widget.setLayout ( grid_layout )

        self.CreateTimeDisplay ( grid_layout )
        self.SetDateDisplayStyles ()
        self.SetSize ( time.localtime ( time.time () ) )
        self.StartTimeUpdates ()

    def SetMainStyle(self):
        QMainWindow.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)

    def CreateTimeDisplay(self, grid_layout) :
        self.timeLab = QLabel ( 'Pending Time', self )
        self.timeLab.setFont ( QtGui.QFont ( 'SansSerif', 18 ) )
        self.timeLab.setAlignment ( QtCore.Qt.AlignCenter )
        grid_layout.addWidget ( self.timeLab, 0, 0 )

    def SetDateDisplayStyles(self) :
        #self.timeLab.setStyleSheet ( "background-color: yellow;border: 1px solid" )
        self.timeLab.setStyleSheet("color: black;  background-color: yellow")

    def SetSize(self, tTime) :
        marg = 0.25
        localtime = time.asctime ( tTime )
        metrics = QtGui.QFontMetrics ( self.timeLab.font () )
        w = metrics.boundingRect ( localtime ).width ()
        twidth = w + (w * marg)
        theight = metrics.boundingRect ( localtime ).height ()

        self.setMinimumWidth ( twidth )
        self.setMaximumHeight ( theight )

    def StartTimeUpdates(self) :
        self.timer = QTimer ()
        self.timer.timeout.connect ( self.handleTimer )
        self.timer.start ( 1000 )

    def StopTimeUpdates(self) :
        self.timer.stop ()

if __name__ == "__main__" :
    app = QtWidgets.QApplication ( sys.argv )
    mainWin = HelloWindow ()

    mainWin.show ()

    sys.exit ( app.exec_ () )
