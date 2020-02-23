# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fenetre_B.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import subprocess
import sys
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(602, 320)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 681, 351))
        self.label.setStyleSheet("background-image: url(:/newPrefix/page_install-bar.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(180, 160, 271, 23))
        self.progressBar.setProperty("value", 10)
        subprocess.call("apt-get install git python3 python3-pip nmap wapiti", shell=True)
        subprocess.call("pip3 install python-whois google colorama urllib3 termcolor geoip2"
                        "colorama tldextract fierce wafw00f", shell=True)
        self.progressBar.setProperty("value", 30)
        subprocess.call("pip install BeautifulSoup termcolor",shell=True)
        self.progressBar.setProperty("value", 40)
        subprocess.call("cd /bin && git clone https://github.com/the-robot/sqliv.git", shell=True)
        subprocess.call("cd sqliv", shell=True)
        subprocess.call("sudo python2 setup.py -i", shell=True)
        self.progressBar.setProperty("value", 60)
        subprocess.call("cd /bin && git clone https://github.com/laramies/theHarvester", shell=True)
        subprocess.call("cd theHarvester")
        subprocess.call("python3.7 -m pip install -r requirements.txt", shell=True)
        self.progressBar.setProperty("value", 70)
        subprocess.call("cd /bin && git clone https://github.com/Mebus/cupp", shell=True)
        subprocess.call("")
        subprocess.call("")
        self.progressBar.setProperty("value", 80)
        subprocess.call("cd /bin && git clone https://github.com/s0md3v/Breacher", shell=True)
        self.progressBar.setProperty("value", 90)
        subprocess.call("cd /usr/share/nmap/scripts/ && git clone https://github.com/vulnersCom/nmap-vulners.git", shell=True)
        self.progressBar.setProperty("value", 100)

        self.progressBar.setObjectName("progressBar")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Hyperion", "Hyperion"))


import format_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
