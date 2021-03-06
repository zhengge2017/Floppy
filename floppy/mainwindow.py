# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jens/Floppy/floppy/ressources/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from floppy.nodeLib import NodeList, NodeFilter
from floppy.reportWidget import ReportWidget
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet('''MainWindow { background-color: rgb(95,95,95); border-color: black }''')
        MainWindow.resize(1250, 629)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.HorizontalSplitter = QtWidgets.QSplitter(self.centralWidget)
        self.HorizontalSplitter.setStyleSheet("QSplitter::handle{background: rgb(85,85,85);}")
        self.HorizontalSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.HorizontalSplitter.setObjectName("HorizontalSplitter")
        self.DrawArea = QtWidgets.QTabWidget(self.HorizontalSplitter)
        self.DrawArea.setObjectName("DrawArea")
        self.DrawArea.setTabsClosable(True)
        self.RightContainer = QtWidgets.QWidget(self.HorizontalSplitter)
        self.RightContainer.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RightContainer.sizePolicy().hasHeightForWidth())
        self.RightContainer.setSizePolicy(sizePolicy)
        self.RightContainer.setMaximumSize(QtCore.QSize(450, 16777215))
        self.RightContainer.setBaseSize(QtCore.QSize(0, 0))
        self.RightContainer.setObjectName("RightContainer")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.RightContainer)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.VerticalSplitter = QtWidgets.QSplitter(self.RightContainer)
        self.VerticalSplitter.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.VerticalSplitter.setOrientation(QtCore.Qt.Vertical)
        self.VerticalSplitter.setObjectName("VerticalSplitter")
        self.TopContainer = QtWidgets.QWidget(self.VerticalSplitter)
        self.TopContainer.setObjectName("TopContainer")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.TopContainer)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.TopLayout = QtWidgets.QVBoxLayout()
        self.TopLayout.setObjectName("TopLayout")
        # self.FilterEdit = QtWidgets.QLineEdit(self.TopContainer)
        self.FilterEdit = NodeFilter(self.TopContainer)
        self.FilterEdit.setObjectName("FilterEdit")
        self.TopLayout.addWidget(self.FilterEdit)
        # self.NodeListView = QtWidgets.QListView(self.TopContainer)
        self.NodeListView = NodeList(self.TopContainer)
        self.NodeListView.setObjectName("NodeListView")
        self.TopLayout.addWidget(self.NodeListView)
        self.gridLayout_3.addLayout(self.TopLayout, 0, 0, 1, 1)
        # self.BottomWidget = QtWidgets.QWidget(self.VerticalSplitter)
        self.BottomWidget = ReportWidget(self.VerticalSplitter)
        self.BottomWidget.setObjectName("BottomWidget")
        self.gridLayout_2.addWidget(self.VerticalSplitter, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.HorizontalSplitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setStyleSheet('''QMenuBar{background: rgb(75,75,75); border-color: black}

        QMenuBar::item {spacing: 3px; padding: 1px 4px;background: transparent; border-radius: 4px; color: white}
        QMenuBar::item:selected { /* when selected using mouse or keyboard */
        background: #a8a8a8;}

        QMenu {
        background-color: rgb(95,95,95); /* sets background of the menu */
        border: 1px solid black;
        }

        QMenu::item {
        /* sets background of menu item. set this to something non-transparent
        if you want menu color and menu item color to be different */
        background-color: transparent;
        color: white;
        }

        QMenu::item:selected { /* when user selects item using mouse or keyboard */
        background-color: rgb(0,85,100);
        }
        ''')
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1250, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setStyleSheet('''
        QToolBar {background: rgb(75,75,75); border:1px solid rgb(55,55,55)}
        QToolButton { color: white }
        ''')
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        iconRoot = os.path.realpath(__file__)
        iconRoot = os.path.join(os.path.dirname(os.path.dirname(iconRoot)), 'floppy')
        iconRoot = os.path.join(iconRoot, 'ressources').replace('\\','/')
        killIconhovered = iconRoot+'/kill.png'
        killIcon = iconRoot+'/closeTab.png'
        self.DrawArea.setStyleSheet('''
        QTabWidget::pane {{ /* The tab widget frame */
    border-top: 6px solid #414141;

}}
QTabWidget::tab-bar {{
    left: 0px; /* move to the right by 5px */
}}

QTabBar::tab {{
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #626262, stop: 0.4 #626262,
                                stop: 0.5 #626262, stop: 1.0 #626262);
    border: 2px solid #414141;
    border-bottom-color: #414141; /* same as the pane color */
    border-top-left-radius: 16px;
    border-top-right-radius: 4px;
    min-width: 15ex;
    padding: 3px;
    padding-right: 8px;
    color: white;
}}

QTabBar::tab:selected, QTabBar::tab:hover {{
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #414141, stop: 0.4 #414141,
                                stop: 0.5 #414141, stop: 1.0 #414141);
}}

QTabBar::tab:selected {{
    border-color: #414141;
    border-bottom-color: #414141; /* same as pane color */
    margin-top: 0px;
}}

QTabBar::tab:!selected {{
    margin-top: 2px; /* make non-selected tabs look smaller */
}}

QTabBar::close-button {{
    image: url({close})
}}
QTabBar::close-button:hover {{
    image: url({close2})
}}
        '''.format(close=killIcon, close2=killIconhovered))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

