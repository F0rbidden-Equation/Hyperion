from PyQt5 import QtCore, QtGui, QtWidgets
import background_install




class Ui_fenetre1(object):
    def setupUi_fenetre1(self, fenetre1):
        fenetre1.setObjectName("Dialog")
        fenetre1.resize(736, 447)
        self.buttonBox = QtWidgets.QDialogButtonBox(fenetre1)
        self.buttonBox.setGeometry(QtCore.QRect(550, 400, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(fenetre1)
        self.label.setGeometry(QtCore.QRect(-10, -60, 291, 621))
        self.label.setStyleSheet("image: url(:/newPrefix/Red_img_install.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(fenetre1)
        self.label_2.setGeometry(QtCore.QRect(280, -60, 461, 511))
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.buttonBox.raise_()
        self.label.raise_()

        self.retranslateUi(fenetre1)
        self.buttonBox.accepted.connect(fenetre1.accept)
        self.buttonBox.rejected.connect(fenetre1.reject)
        QtCore.QMetaObject.connectSlotsByName(fenetre1)

    def retranslateUi(self, fenetre1):
        _translate = QtCore.QCoreApplication.translate
        fenetre1.setWindowTitle(_translate("Dialog", "Hyperion Install"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; font-style:italic; color:#ef2929;\">Hyperion Installation v2.0</span></p><p><br/></p><p><span style=\" font-size:18pt; font-style:italic; color:#ffffff;\">Installation Informations Hyperion  :</span></p><p><span style=\" font-size:16pt; text-decoration: underline; color:#ef2929;\">Paquets required</span></p><p><span style=\" color:#ffffff;\">--&gt; Librairy PyQt5 python3</span></p><p><span style=\" color:#ffffff;\">--&gt; Librairy socket python3 </span></p><p><span style=\" color:#ffffff;\">--&gt; Librairy Whois python3</span></p><p><span style=\" color:#ffffff;\">--&gt; Librairy Wafw00f python3 </span></p><p><span style=\" color:#ffffff;\">--&gt; Program Nmap / script Vulners.nse</span></p><p><span style=\" color:#ffffff;\">--&gt; Program Photon Mapping Network</span></p></body></html>"))



class Ui_fenetre2(object):
    def setupUi_fenetre2(self, fenetre2):
        fenetre2.setObjectName("Dialog")
        fenetre2.resize(759, 391)
        self.buttonBox = QtWidgets.QDialogButtonBox(fenetre2)
        self.buttonBox.setGeometry(QtCore.QRect(570, 350, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(fenetre2)
        self.label.setGeometry(QtCore.QRect(0, -20, 261, 481))
        self.label.setStyleSheet("image: url(:/newPrefix/Red_img_install.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(fenetre2)
        self.label_2.setGeometry(QtCore.QRect(260, 0, 501, 471))
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.scrollArea = QtWidgets.QScrollArea(fenetre2)
        self.scrollArea.setGeometry(QtCore.QRect(280, 50, 461, 211))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 523, 301))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.checkBox = QtWidgets.QCheckBox(fenetre2)
        self.checkBox.setGeometry(QtCore.QRect(280, 310, 331, 23))
        self.checkBox.setStyleSheet("color: rgb(252, 233, 79);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/warning.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkBox.setIcon(icon)
        self.checkBox.setObjectName("checkBox")
        self.label_4 = QtWidgets.QLabel(fenetre2)
        self.label_4.setGeometry(QtCore.QRect(280, 280, 321, 20))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(252, 233, 79);")
        self.label_4.setObjectName("label_4")
        self.label_2.raise_()
        self.buttonBox.raise_()
        self.label.raise_()
        self.scrollArea.raise_()
        self.checkBox.raise_()
        self.label_4.raise_()

        self.retranslateUi(fenetre2)
        self.buttonBox.accepted.connect(fenetre2.accept)
        self.buttonBox.rejected.connect(fenetre2.reject)
        self.buttonBox.hide()
        QtCore.QMetaObject.connectSlotsByName(fenetre2)

    def retranslateUi(self, fenetre2):
        _translate = QtCore.QCoreApplication.translate
        fenetre2.setWindowTitle(_translate("Dialog", "Hyperion Install"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#ef2929;\">Hyperion License Open-Source </span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#ef2929;\">Software Hyperion License Open-Source</span></p><p><span style=\" font-style:italic; color:#ffffff;\">the followings packages required for the Hyperion Program must be installed</span></p><p><span style=\" font-weight:600; color:#ef2929;\">Confirmed installations packages required :</span></p><p><span style=\" color:#8ae234;\">--&gt; </span><span style=\" color:#ffffff;\">Librairy PyQt5 python3 : </span><span style=\" color:#8ae234;\">ok !</span></p><p><span style=\" color:#ef2929;\">--&gt; </span><span style=\" color:#ffffff;\">Librairy socket python3: ??</span></p><p><span style=\" color:#ef2929;\">--&gt; </span><span style=\" color:#ffffff;\">Librairy Whois python3: ??</span></p><p><span style=\" color:#ef2929;\">--&gt; </span><span style=\" color:#ffffff;\">Librairy Wafw00f python3 : ?? </span></p><p><span style=\" color:#ef2929;\">--&gt; </span><span style=\" color:#ffffff;\">Program Nmap / script Vulners.nse : ??</span></p><p><span style=\" color:#ef2929;\">--&gt; </span><span style=\" color:#ffffff;\">Program Photon Mapping Network :??</span></p><p><span style=\" color:#ffffff;\">created by Lazarus</span></p></body></html>"))
        self.checkBox.setText(_translate("Dialog", "Confirmed Installations ?? !"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline; color:#ffffff;\">Checked the box for confirmed Installations</span><span style=\" font-weight:600; color:#ffffff;\"> :</span></p></body></html>"))
        self.checkBox.stateChanged.connect(self.clickBox)
    def clickBox(self, state):

        if state == QtCore.Qt.Checked:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("Icons/stamp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.checkBox.setIcon(icon)
            self.checkBox.setObjectName("checkBox")
            self.checkBox.setText("Installation Confirmed !!")
            self.buttonBox.show()  # passé en clair
            # self.buttonBox.accepted.connect(self.accept)



        else:

            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("./warning.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.checkBox.setIcon(icon)
            self.checkBox.setObjectName("checkBox")
            self.checkBox.setText("Confirmed Installation ?? !!")
            self.buttonBox.hide()  ### passé en secret
            # print('Unchecked')

class Ui_fenetre3(object):
    def setupUi_fenetre3(self, fenetre3):
        fenetre3.setObjectName("Dialog")
        fenetre3.resize(542, 234)
        self.label_2 = QtWidgets.QLabel(fenetre3)
        self.label_2.setGeometry(QtCore.QRect(0, 60, 461, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(fenetre3)
        self.label_3.setGeometry(QtCore.QRect(220, 110, 171, 31))
        self.label_3.setObjectName("label_3")
        self.progressBar = QtWidgets.QProgressBar(fenetre3)
        self.progressBar.setGeometry(QtCore.QRect(50, 150, 471, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(fenetre3)
        self.pushButton.setGeometry(QtCore.QRect(410, 200, 111, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(fenetre3)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 200, 161, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(fenetre3)
        self.label.setGeometry(QtCore.QRect(0, -1, 631, 51))
        self.label.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.label.setObjectName("label")

        self.retranslateUi(fenetre3)
        QtCore.QMetaObject.connectSlotsByName(fenetre3)

    def retranslateUi(self, fenetre3):
        _translate = QtCore.QCoreApplication.translate
        fenetre3.setWindowTitle(_translate("Dialog", "Hyperion Install"))
        self.label_2.setText(_translate("Dialog","<html><head/><body><p><span style=\" font-size:14pt; text-decoration: underline;\">Installations of packages for the Hyperion program :</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog","<html><head/><body><p><span style=\" font-size:18pt;\">Installations ...</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "start"))
        self.pushButton_2.setText(_translate("Dialog", "Termined"))
        self.label.setText(_translate("Dialog","<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">Hyperion Program Auto-Installation v2.0 </span></p></body></html>"))
        self.pushButton_2.hide()
        self.pushButton.clicked.connect(self.start_install)




    def start_install(self):
        import sys
        import subprocess

        self.progressBar.setProperty("value", 15)
        subprocess.call("sudo apt-get install git python3 python-pip python3-pip ",shell=True)
        self.progressBar.setProperty("value", 30)
        self.progressBar.setProperty("value", 40)
        subprocess.call("pip install tld requests", shell=True)
        self.progressBar.setProperty("value", 50)
        subprocess.call("pip install wafw00f ", shell=True)
        subprocess.call("pip3 install python-whois tld requests", shell=True)
        self.progressBar.setProperty("value", 70)
        subprocess.call("pip3 install colorama termcolor", shell=True)
        self.progressBar.setProperty("value", 80)
        subprocess.call("cd /usr/share/nmap/scripts/ && sudo git clone https://github.com/vulnersCom/nmap-vulners.git ", shell=True)
        subprocess.call("cd /usr/share/nmap/scripts/ && sudo git clone https://github.com/scipag/vulscan.git ", shell=True)
        self.progressBar.setProperty("value", 100)
        print("[*] Installation Termined !!!")
        self.pushButton.hide()
        self.pushButton_2.show()






class Ui_fenetre4(object):
    def setupUi_fenetre4(self, fenetre4):
        fenetre4.setObjectName("Dialog")
        fenetre4.resize(717, 441)
        self.label = QtWidgets.QLabel(fenetre4)
        self.label.setGeometry(QtCore.QRect(-20, -20, 251, 481))
        self.label.setStyleSheet("image: url(:/newPrefix/Red_img_install.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(fenetre4)
        self.label_2.setGeometry(QtCore.QRect(230, -10, 491, 451))
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(fenetre4)
        self.pushButton.setGeometry(QtCore.QRect(600, 400, 89, 25))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(fenetre4)
        QtCore.QMetaObject.connectSlotsByName(fenetre4)

    def retranslateUi(self, fenetre4):
        _translate = QtCore.QCoreApplication.translate
        fenetre4.setWindowTitle(_translate("Dialog", "Hyperion Install"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><br/></p><p><span style=\" font-size:28pt; font-weight:600; font-style:italic; color:#ef2929;\">Hyperion Installation v2.0</span></p><p><br/></p><p><span style=\" font-size:18pt; font-style:italic; color:#ffffff;\">Installation Informations Hyperion :</span></p><p><span style=\" font-size:16pt; text-decoration: underline; color:#8ae234;\">Paquets required installed </span></p><p><span style=\" color:#ffffff;\">--&gt; Librairy PyQt5 python3 </span><span style=\" color:#888a85;\">: </span><span style=\" color:#8ae234;\">ok </span></p><p><span style=\" color:#ffffff;\">--&gt; Librairy socket python3</span><span style=\" color:#888a85;\"> : </span><span style=\" color:#8ae234;\">ok </span></p><p><span style=\" color:#ffffff;\">--&gt; Librairy Whois python3</span><span style=\" color:#888a85;\">  : </span><span style=\" color:#8ae234;\">ok </span></p><p><span style=\" color:#ffffff;\">--&gt; Librairy Wafw00f python3</span><span style=\" color:#888a85;\"> : </span><span style=\" color:#8ae234;\">ok </span></p><p><span style=\" color:#ffffff;\">--&gt; Program Nmap / script Vulners.nse</span><span style=\" color:#888a85;\"> : </span><span style=\" color:#8ae234;\">ok </span></p><p><span style=\" color:#ffffff;\">--&gt; Program Photon Mapping Network</span><span style=\" color:#888a85;\"> : </span><span style=\" color:#8ae234;\">ok </span></p><p><span style=\" color:#8ae234;\">-----&gt; Installation Termined with sucess !</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Termined"))


class Controller:
    def __init__(self):
        pass
    def Menu_Install(self):
        self.fenetre1 = QtWidgets.QDialog()
        self.ui = Ui_fenetre1()
        self.ui.setupUi_fenetre1(self.fenetre1)
        self.fenetre1.show()
        self.ui.buttonBox.accepted.connect(self.Menu_Install2)

    def Menu_Install2(self):
        self.fenetre2 = QtWidgets.QDialog()
        self.ui = Ui_fenetre2()
        self.ui.setupUi_fenetre2(self.fenetre2)
        self.fenetre2.show()
        self.ui.buttonBox.accepted.connect(self.Menu_Install3)

    def Menu_Install3(self):
        self.fenetre3 = QtWidgets.QDialog()
        self.ui = Ui_fenetre3()
        self.ui.setupUi_fenetre3(self.fenetre3)
        self.fenetre3.show()
        self.ui.pushButton_2.clicked.connect(self.Menu_Install4)

    def Menu_Install4(self):
        self.fenetre3.close()
        self.fenetre4 = QtWidgets.QDialog()
        self.ui = Ui_fenetre4()
        self.ui.setupUi_fenetre4(self.fenetre4)
        self.fenetre4.show()
        self.ui.pushButton.clicked.connect(self.close_install)

    def close_install(self):
        self.fenetre4.close()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Controller = Controller()
    Controller.Menu_Install()
    sys.exit(app.exec_())
