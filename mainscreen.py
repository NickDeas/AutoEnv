# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainscreen.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from envManager import EnvManager
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore

QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
envManager = EnvManager()

def getEnvList():
    return envManager.listEnvs()

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        self.app_lbls = []
        self.url_lbls = []
        self.view_env = []

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(637, 480)
        MainWindow.setStyleSheet("background-color:rgb(55, 55, 55);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 0, 641, 61))
        self.title.setStyleSheet("color: red;\n"
"font: 36pt \"Lucida Sans\";\n"
"qproperty-alignment: AlignCenter;\n"
"background: None;")
        self.title.setObjectName("title")
        self.title_line = QtWidgets.QFrame(self.centralwidget)
        self.title_line.setGeometry(QtCore.QRect(0, 50, 641, 20))
        self.title_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.title_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.title_line.setObjectName("title_line")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 90, 581, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.left_pane = QtWidgets.QVBoxLayout()
        self.left_pane.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.left_pane.setObjectName("left_pane")
        self.env_list = QtWidgets.QVBoxLayout()
        self.env_list.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.env_list.setObjectName("env_list")
        self.env_names = getEnvList()
        self.env_buttons = []
        for i, env in enumerate(self.env_names):
            temp_button = QtWidgets.QPushButton(self.gridLayoutWidget)
            temp_button.setObjectName(env)
            temp_button.clicked.connect(self.make_display(env))
            temp_button.setStyleSheet('color:white;\nbackground-color: grey;')
            self.env_buttons.append(temp_button)
            self.env_list.addWidget(temp_button)

        self.left_pane.addLayout(self.env_list)
        self.left_pane.setStretch(0, 4)
        self.gridLayout.addLayout(self.left_pane, 2, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 1, 1, 1)
        self.right_pane = QtWidgets.QVBoxLayout()
        self.right_pane.setObjectName("right_pane")
        self.apps_title = QtWidgets.QLabel(self.gridLayoutWidget)
        self.apps_title.setStyleSheet("color: white;\n"
"font: 14pt \"Lucida Sans\";")
        self.apps_title.setObjectName("apps_title")
        self.apps_title.setVisible(False)
        self.right_pane.addWidget(self.apps_title)
        self.app_list = QtWidgets.QVBoxLayout()
        self.app_list.setObjectName("app_list")
        self.right_pane.addLayout(self.app_list)
        self.add_app = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.add_app.setStyleSheet("color: black;\n"
"background-color: rgb(201, 201, 201);\n"
"font: 12pt \"Lucida Sans\";")
        self.add_app.setObjectName("add_app")
        self.add_app.setVisible(False)
        self.right_pane.addWidget(self.add_app, 0, QtCore.Qt.AlignRight)
        self.urls_title = QtWidgets.QLabel(self.gridLayoutWidget)
        self.urls_title.setStyleSheet("color: white;\n"
"font: 14pt \"Lucida Sans\";")
        self.urls_title.setObjectName("urls_title")
        self.urls_title.setVisible(False)
        self.right_pane.addWidget(self.urls_title)
        self.url_list = QtWidgets.QVBoxLayout()
        self.url_list.setObjectName("url_list")
        self.right_pane.addLayout(self.url_list)
        self.add_url = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.add_url.setStyleSheet("color: black;\n"
"background-color: rgb(201, 201, 201);\n"
"font: 12pt \"Lucida Sans\";")
        self.add_url.setObjectName("add_url")
        self.add_url.setVisible(False)
        self.right_pane.addWidget(self.add_url, 0, QtCore.Qt.AlignRight)
        self.right_pane.setStretch(0, 1)
        self.right_pane.setStretch(1, 3)
        self.right_pane.setStretch(3, 1)
        self.right_pane.setStretch(4, 3)
        self.gridLayout.addLayout(self.right_pane, 2, 2, 1, 1)
        self.my_envs_title = QtWidgets.QLabel(self.gridLayoutWidget)
        self.my_envs_title.setStyleSheet("color: white;\n"
"font: 20pt \"Lucida Sans\";\n"
"qproperty-alignment: AlignCenter;")
        self.my_envs_title.setAlignment(QtCore.Qt.AlignCenter)
        self.my_envs_title.setObjectName("my_envs_title")
        self.gridLayout.addWidget(self.my_envs_title, 0, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 1, 2, 1, 1)
        self.qv_title = QtWidgets.QLabel(self.gridLayoutWidget)
        self.qv_title.setStyleSheet("color: white;\n"
"font: 20pt \"Lucida Sans\";\n"
"qproperty-alignment: AlignCenter;")
        self.qv_title.setObjectName("qv_title")
        self.gridLayout.addWidget(self.qv_title, 0, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 4)
        self.gridLayout.setColumnStretch(2, 3)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(2, 6)
        self.new_env = QtWidgets.QPushButton(self.centralwidget)
        self.new_env.setGeometry(QtCore.QRect(230, 400, 75, 20))
        self.new_env.setStyleSheet("color: black;\n"
"background-color: rgb(201, 201, 201);\n"
"font: 12pt \"Lucida Sans\";")
        self.new_env.setObjectName("new_env")
        self.del_env = QtWidgets.QPushButton(self.centralwidget)
        self.del_env.setGeometry(QtCore.QRect(70, 400, 75, 20))
        self.del_env.setStyleSheet("color: black;\n"
"background-color: rgb(201, 201, 201);\n"
"font: 12pt \"Lucida Sans\";")
        self.del_env.setObjectName("del_env")
        self.open_env = QtWidgets.QPushButton(self.centralwidget)
        self.open_env.setGeometry(QtCore.QRect(150, 400, 75, 20))
        self.open_env.setStyleSheet("color: black;\n"
"background-color: rgb(201, 201, 201);\n"
"font: 12pt \"Lucida Sans\";")
        self.open_env.setObjectName("open_env")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 637, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AutoEnv"))
        self.title.setText(_translate("MainWindow", "AutoEnv"))
        self.apps_title.setText(_translate("MainWindow", "Apps"))
        for i, env_button in enumerate(self.env_buttons):
            env_button.setText(_translate("MainWindow", self.env_names[i]))
        self.add_app.setText(_translate("MainWindow", "Add App"))
        self.urls_title.setText(_translate("MainWindow", "Urls"))
        self.add_url.setText(_translate("MainWindow", "Add Url"))
        self.my_envs_title.setText(_translate("MainWindow", "My Environments"))
        self.qv_title.setText(_translate("MainWindow", "Quick View"))
        self.new_env.setText(_translate("MainWindow", "New Env"))
        self.del_env.setText(_translate("MainWindow", "Delete Env"))
        self.open_env.setText(_translate("MainWindow", "Open Env"))

    def showQV(self):
        self.add_app.setVisible(True)
        self.add_url.setVisible(True)
        self.apps_title.setVisible(True)
        self.urls_title.setVisible(True)

    def make_display(self, env_name):
        def display():
            self.showQV()
            self.view_env = env_name

            envManager.loadEnv(env_name)
            apps = envManager.curEnv.apps
            urls = envManager.curEnv.urls

            for i in reversed(range(self.app_list.count())): 
                self.app_list.itemAt(i).widget().setParent(None)

            for i in reversed(range(self.url_list.count())): 
                self.url_list.itemAt(i).widget().setParent(None)
                

            self.app_lbls = []
            self.url_lbls = []

            for app in apps:
                temp_app_lbl = QtWidgets.QLabel()
                self.app_list.addWidget(temp_app_lbl)
                temp_app_lbl.setText(app[app.rfind('/')+1:])
                self.app_lbls.append(temp_app_lbl)

            for url in urls:
                temp_url_lbl = QtWidgets.QLabel()
                self.url_list.addWidget(temp_url_lbl)
                temp_url_lbl.setText(url)
                temp_url_lbl.setWordWrap(True)
                self.url_lbls.append(temp_url_lbl)
        return display

    def del_env():
        envManager.remEnv(self.view_env)

        for env in self.env_buttons:
            if self.view_env == env.


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
