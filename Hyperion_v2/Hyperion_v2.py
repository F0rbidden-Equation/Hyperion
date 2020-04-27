# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from colorama import init
from termcolor import colored
import subprocess
import backG1
import Red_Dns
import red_final2
import whitehat
import os
import whois
import socket

class Ui_Report(object):
    def setupUi_report(self, report):
        report.setObjectName("Form")
        report.resize(724, 599)
        self.label = QtWidgets.QLabel(report)
        self.label.setGeometry(QtCore.QRect(-20, -30, 971, 661))
        self.label.setStyleSheet("image: url(:/newPrefix/red_final2.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(report)
        self.textBrowser.setGeometry(QtCore.QRect(110, 50, 511, 541))
        self.textBrowser.setObjectName("textBrowser")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(report)
        self.commandLinkButton.setGeometry(QtCore.QRect(630, 550, 81, 41))
        self.commandLinkButton.setStyleSheet("color: rgb(252, 233, 79);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 14pt \"Ubuntu\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/exit-xxl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.label_2 = QtWidgets.QLabel(report)
        self.label_2.setGeometry(QtCore.QRect(150, 20, 521, 31))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(report)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 81, 81))
        self.label_3.setStyleSheet("image: url(:/newPrefix/img_whitehat.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(report)
        QtCore.QMetaObject.connectSlotsByName(report)

    def retranslateUi(self, report):
        _translate = QtCore.QCoreApplication.translate
        report.setWindowTitle(_translate("report", "Report Analysis"))
        self.commandLinkButton.setText(_translate("report", "Exit"))
        self.label_2.setText(_translate("report", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Report Analysis : Hyperion v2.0</span></p></body></html>"))








class Ui_Dns(object):
    def setupUi_Dns(self, Dns):
        Dns.setObjectName("Network")
        Dns.resize(434, 146)
        self.lineEdit = QtWidgets.QLineEdit(Dns)
        self.lineEdit.setGeometry(QtCore.QRect(190, 70, 231, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dns)
        self.label.setGeometry(QtCore.QRect(-30, -30, 511, 301))
        self.label.setStyleSheet("image: url(:/newPrefix/red_DNS.jpg);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dns)
        self.pushButton.setGeometry(QtCore.QRect(350, 110, 71, 25))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Dns)
        self.label_2.setGeometry(QtCore.QRect(0, 70, 191, 17))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dns)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 61, 51))
        self.label_3.setStyleSheet("image: url(:/newPrefix/img_whitehat.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dns)
        self.label_4.setGeometry(QtCore.QRect(100, 0, 271, 20))
        self.label_4.setObjectName("label_4")
        self.label.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()

        self.retranslateUi(Dns)
        QtCore.QMetaObject.connectSlotsByName(Dns)

    def retranslateUi(self, Dns):
        _translate = QtCore.QCoreApplication.translate
        Dns.setWindowTitle(_translate("Dialog", "DNS Research"))
        self.label.setText(_translate("Dialog", ""))
        self.pushButton.setText(_translate("Dialog", "Starting"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#eeeeec;\">Domain Name System :</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#eeeeec;\">Hyperion Open-Source Intelligence</span></p></body></html>"))






class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(621, 369)
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(Dialog)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(0, 230, 151, 41))
        self.commandLinkButton_3.setStyleSheet("background-color: rgb(204, 0, 0);\n"
"color: rgb(238, 238, 236);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/database2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_3.setIcon(icon)
        self.commandLinkButton_3.setIconSize(QtCore.QSize(30, 30))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.commandLinkButton_5 = QtWidgets.QCommandLinkButton(Dialog)
        self.commandLinkButton_5.setGeometry(QtCore.QRect(550, 330, 81, 31))
        self.commandLinkButton_5.setStyleSheet("background-color: rgb(204, 0, 0);\n"
"color: rgb(238, 238, 236);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icons/exit-xxl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_5.setIcon(icon1)
        self.commandLinkButton_5.setObjectName("commandLinkButton_5")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(0, 80, 141, 41))
        self.commandLinkButton.setStyleSheet("background-color: rgb(204, 0, 0);\n"
"color: rgb(238, 238, 236);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./icons/earth-red.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon2)
        self.commandLinkButton.setIconSize(QtCore.QSize(30, 30))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(Dialog)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(0, 180, 141, 41))
        self.commandLinkButton_2.setStyleSheet("background-color: rgb(204, 0, 0);\n"
"color: rgb(238, 238, 236);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./icons/security3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_2.setIcon(icon3)
        self.commandLinkButton_2.setIconSize(QtCore.QSize(30, 30))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(Dialog)
        self.commandLinkButton_4.setGeometry(QtCore.QRect(0, 130, 141, 41))
        self.commandLinkButton_4.setStyleSheet("background-color: rgb(204, 0, 0);\n"
"color: rgb(238, 238, 236);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./icons/server-xl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_4.setIcon(icon4)
        self.commandLinkButton_4.setIconSize(QtCore.QSize(30, 30))
        self.commandLinkButton_4.setObjectName("commandLinkButton_4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 61))
        self.label.setStyleSheet("image: url(:/newPrefix/img_whitehat.jpg);")
        self.label.setObjectName("label")
        self.commandLinkButton_6 = QtWidgets.QCommandLinkButton(Dialog)
        self.commandLinkButton_6.setGeometry(QtCore.QRect(0, 280, 141, 41))
        self.commandLinkButton_6.setStyleSheet("background-color: rgb(204, 0, 0);\n"
"color: rgb(238, 238, 236);")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./icons/network-map4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_6.setIcon(icon5)
        self.commandLinkButton_6.setIconSize(QtCore.QSize(30, 30))
        self.commandLinkButton_6.setObjectName("commandLinkButton_6")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 70, 381, 241))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(140, 0, 451, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(610, 400, 191, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(270, 340, 171, 20))
        self.label_5.setObjectName("label_5")
        self.commandLinkButton_3.raise_()
        self.commandLinkButton_5.raise_()
        self.commandLinkButton_2.raise_()
        self.commandLinkButton_4.raise_()
        self.label.raise_()
        self.commandLinkButton_6.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.commandLinkButton.raise_()
        self.label_5.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Hyperion V2"))
        self.commandLinkButton_3.setText(_translate("Dialog", "Infos Datas-Base"))
        self.commandLinkButton_5.setText(_translate("Dialog", "Quit"))
        self.commandLinkButton.setText(_translate("Dialog", "Infos Network"))
        self.commandLinkButton_2.setText(_translate("Dialog", "Infos Security"))
        self.commandLinkButton_4.setText(_translate("Dialog", "Infos Servers"))
        self.label.setText(_translate("Dialog", "Gif1"))
        self.commandLinkButton_6.setText(_translate("Dialog", "Map Network"))
        self.label_2.setText(_translate("Dialog", "Gif2"))
        self.gif = QMovie('network.gif')
        self.label_2.setMovie(self.gif)
        self.gif.start()
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; color:#ef2929;\">Hyperion Automate Open-Source Intelligence           V2.0</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "by lzarus"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ef2929;\">OSINT CyberSecurity</span></p></body></html>"))




class Controller:
    def __init__(self):
        pass

    def voir_Menu_general(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.ui.commandLinkButton.clicked.connect(self.voir_Menu_Network)
        self.ui.commandLinkButton_4.clicked.connect(self.voir_Menu_Servers)
        self.ui.commandLinkButton_2.clicked.connect(self.voir_Menu_Security)
        self.ui.commandLinkButton_3.clicked.connect(self.voir_Menu_DataBase)
        self.ui.commandLinkButton_6.clicked.connect(self.voir_Menu_Map_Network)
        self.ui.commandLinkButton_5.clicked.connect(self.close_Menu_General)
        self.Dialog.show()




    def voir_Menu_Network(self, Dns):
        self.Dns = QtWidgets.QDialog()
        self.ui = Ui_Dns()
        self.ui.setupUi_Dns(self.Dns)
        self.Dns.show()
        self.ui.pushButton.clicked.connect(self.voir_report_network)

    def voir_Menu_Servers(self):
        self.Dns = QtWidgets.QDialog()
        self.ui = Ui_Dns()
        self.ui.setupUi_Dns(self.Dns)
        self.Dns.show()
        self.ui.pushButton.clicked.connect(self.voir_report_servers)

    def voir_Menu_Security(self):
        self.Dns = QtWidgets.QDialog()
        self.ui = Ui_Dns()
        self.ui.setupUi_Dns(self.Dns)
        self.Dns.show()
        self.ui.pushButton.clicked.connect(self.voir_report_security)

    def voir_Menu_DataBase(self):
        self.Dns = QtWidgets.QDialog()
        self.ui = Ui_Dns()
        self.ui.setupUi_Dns(self.Dns)
        self.Dns.show()
        self.ui.pushButton.clicked.connect(self.voir_report_DataBase)

    def voir_Menu_Map_Network(self):
        self.Dns = QtWidgets.QDialog()
        self.ui = Ui_Dns()
        self.ui.setupUi_Dns(self.Dns)
        self.Dns.show()
        self.ui.pushButton.clicked.connect(self.voir_report_Map_Network)

    def voir_report_network(self):
        self.Dns.close()

        dns = self.ui.lineEdit.text()

        print(colored("[*] ---> patient please ... 15 secondes scanning building report[Network]", 'blue'))
        print(dns)
        verifdns = os.system("ping -c 1 " + dns)
        if verifdns == 0:
            ip = (socket.gethostbyname(dns))
            import subprocess

            f = open(r'Fonctions_Network.txt', 'w')

            subprocess.call(["nmap --script dns-brute " + dns], shell=True, stdout=f)
            import subprocess



            ############### dnsenum ########################
            subprocess.call(["dnsrecon -d "+ dns], shell=True, stdout=f)


            #subprocess.call("[nmap -sn --script hostmap-* " + dns], shell=True, stdout=f)


            f.close()

            self.report = QtWidgets.QWidget()
            self.ui = Ui_Report()
            self.ui.setupUi_report(self.report)
            text = open('Fonctions_Network.txt').read()
            self.ui.textBrowser.setPlainText(text)
            self.report.show()
            self.ui.commandLinkButton.clicked.connect(self.close_Report_Analyse)
            print(colored("[*] ---> Scanning Network termined ! building report[Network]: ok !", 'green'))
        else:
            print(colored("[*] !!!! *Errors Dns* !!!!", 'red'))

    def voir_report_servers(self):
        self.Dns.close()
        dns = self.ui.lineEdit.text()  ## ok !!!!!
        print(colored("[*] ---> patient please ... 15 secondes scanning building report[Servers] !!", 'blue'))
        print(dns)
        verifdns = os.system("ping -c 1 " + dns)
        if verifdns == 0:
            ip = (socket.gethostbyname(dns))
            import subprocess

            f = open('Fonctions_Servers.txt', 'w')
            subprocess.call(["fierce --domain " + dns + " --subdomains accounts admin ads"], shell=True, stdout=f)
            subprocess.call(["nmap --script=dns-service-discovery "+ dns], shell=True, stdout=f)
            f.write("\n")
            f.write("#### Scanners Informations Principal ##################### \n")

            w = whois.whois(dns)

            # print(w)
            emails = (w.emails)
            emcolor = ("|-----> Emails :")
            print(emcolor, emails, file=f)
            dnsseccolor = ("|-----> Dns Secondary :")
            dnssec = (w.dnssec)
            print(dnsseccolor, dnssec, file=f)
            namecolor = ("|-----> Name :")
            name = (w.name)
            print(namecolor, name, file=f)
            orgcolor = ("|-----> Corporations :")
            org = (w.org)
            print(orgcolor, org, file=f)
            adresscolor = ("|-----> Adress :")
            adress = (w.adress)
            print(adresscolor, adress, file=f)
            citycolor = ("|-----> City :")
            city = (w.city)
            print(citycolor, city, file=f)
            statecolor = ("|-----> State :")
            state = (w.state)
            print(statecolor, state, file=f)
            zipcolor = ("|-----> Zip :")
            zipcode = (w.zipcode)
            print(zipcolor, zipcode, file=f)
            colorcount = ("|-----> Country :")
            country2 = (w.country)
            print(colorcount, country2, file=f)
            servcolor = ("|-----> Names Servers :")
            names_servers = (w.name_servers)
            print(servcolor, names_servers, file=f)
            creatio_datecolor = ("|-----> Creation Date Servers :")
            creation_date = (w.creation_date)
            print(creatio_datecolor, creation_date, file=f)
            updated_datecolor = ("|-----> Last Update Date Servers :")
            updated_date = (w.updated_date)
            print(updated_datecolor, updated_date, file=f)
            expiration_color = ("|-----> Expirations Date Servers :")
            expiration_date = (w.expiration_date)
            print(expiration_color, expiration_date, file=f)
            f.close()

            self.report = QtWidgets.QWidget()
            self.ui = Ui_Report()
            self.ui.setupUi_report(self.report)
            text = open('Fonctions_Servers.txt').read()
            self.ui.textBrowser.setPlainText(text)
            self.report.show()
            self.ui.commandLinkButton.clicked.connect(self.close_Report_Analyse)
        else:
            print(colored("[*] !!!! *Errors Dns* !!!!", 'red'))

        f.close()
        print(colored("[*] ---> Scanning Servers termined ! building report[Server]: ok !", 'green'))

    def voir_report_security(self):
        import subprocess
        self.Dns.close()

        f = open(r'Fonctions_security.txt', 'w')
        print(colored("[*] ---> patient please ... 15 secondes scanning building report[Security] !!", 'blue'))
        dns = self.ui.lineEdit.text()



        verifdns = os.system("ping -c 1 " + dns)
        if verifdns == 0:
            ip = (socket.gethostbyname(dns))


            subprocess.call(["nmap --script=http-waf-fingerprint "+ dns], shell=True, stdout=f)
            subprocess.call(["nmap -sV --script nmap-vulners "+ dns], shell=True, stdout=f)
            subprocess.call(["wafw00f http://www."+dns], shell=True)

        else:
            print(colored("[*] !!!! *Errors Dns* !!!!", 'red'))

        f.close()


        self.report = QtWidgets.QWidget()
        self.ui = Ui_Report()
        self.ui.setupUi_report(self.report)
        text = open('Fonctions_security.txt').read()
        self.ui.textBrowser.setPlainText(text)
        self.report.show()
        self.ui.commandLinkButton.clicked.connect(self.close_Report_Analyse)
        print(colored("[*] ---> Scanning Security  termined building report[Security]: ok !", 'green'))
    def voir_report_DataBase(self):
        self.Dns.close()

        dns = self.ui.lineEdit.text()


        import subprocess
        f = open('Fonctions_DB.txt', 'w')

        print("")
        print(colored("[*] ---> patient please ... 15 secondes scanning building report[DataBase] !!", 'blue'))
        print("")

        verifdns = os.system("ping -c 1 " + dns)
        if verifdns == 0:
            ip = (socket.gethostbyname(dns))
            hosts = [ip]
            ports = [1433, 1434, 3306, 1583, 3050, 3351, 5432]
            color1 = ("|---> [+] Connecting to [")
            colorP = ("] | port: ")
            print("--" * 60)
            serv = ("Microsoft SQL Server ,Pervasive SQL, Firebird & Interbase ,MySQL ,MariaDB ,PostgreSQL ")
            print("Report Detections Protocoles Network 'open' on the DNS Target : " + serv, file=f)
            print("--" * 60, file=f)
            for host in hosts:
                for port in ports:
                    try:
                        print(color1 + host + colorP + str(port), file=f)
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.settimeout(5)
                        result = s.connect_ex((host, port))
                        if result == 0:
                            print(
                                " [-!*!-] Detection [sucessfull] DataBase " + str(port) + " services / port open  !!!",
                                file=f)
                            ##### Analyse #####

                            if port == 1433:
                                print("[*] Analyse... TCP Microsoft SQL port [1433] ", file=f)
                                subprocess.call(["nmap - p 1433 --script ms-sql-info "] + ip, shell=True, stdout=f)
                            if port == 1434:
                                print("[*] Analyse... UDP Microsoft SQL port [1434]", file=f)
                            if port == 1583:
                                print("[*] Analyse... TCP [Pervasive SQL] port [1583]  ", file=f)

                            if port == 3306:
                                print("[*] Analyse...  TCP  [MySQL / MariaDB] [3306]  ", file=f)
                                subprocess.call("nmap -p 3306 --script=mysql-info  " + ip, shell=True, stdout=f)
                                subprocess.call("nmap -p 3306  --script=mysql-enum  " + ip, shell=True, stdout=f)

                            if port == 3050:
                                print("[*] Analyse... TCP [Firebird & Interbase] port [3050] ", file=f)

                            if port == 3351:
                                print("[*] Analyse... TCP [Pervasive SQL] port [3351]  ", file=f)

                            if port == 5432:
                                print("[*] Analyse TCP [PostgreSQL] port [5432]  ", file=f)

                        if port == 1433:
                            print("[>> Test ... TCP Microsoft SQL Server port [1433]  ", file=f)

                        ##### detection si c'est ouvert ##########
                        if port == 1434:
                            print(">> Test .. UDP Microsoft SQL port [1434]", file=f)
                        if port == 1583:
                            print(">> Test .. TCP [Pervasive SQL] port [1583]  ", file=f)

                        if port == 3306:
                            print(">> Test .. TCP  [MySQL / MariaDB] port [3306]  ", file=f)

                        if port == 3050:
                            print(">> Test .. TCP [Firebird & Interbase] port [3050] ", file=f)

                        if port == 3351:
                            print(">> Test .. TCP [Pervasive SQL] port [3351]  ", file=f)

                        if port == 5432:
                            print(">> Test .. TCP [PostgreSQL] port [5432]  ", file=f)
                            print("--------------------Scanning Termined !! -------------------------------")

                    except:
                        pass

        f.close()
        self.report = QtWidgets.QWidget()
        self.ui = Ui_Report()
        self.ui.setupUi_report(self.report)
        text = open('Fonctions_DB.txt').read()
        self.ui.textBrowser.setPlainText(text)
        self.report.show()
        self.ui.commandLinkButton.clicked.connect(self.close_Report_Analyse)
        print(colored("[*] ---> Scanning DatBase termined ! building report[DataBase]: ok !", 'green'))



    def voir_report_Map_Network(self):
        self.Dns.close()

        dns = self.ui.lineEdit.text()  ## ok !!!!!
        print(dns)
        print(colored("[*] ---> patient please !! ...  1/2 minutes scanning building Map from DNS target [Mapping Network] !!", 'blue'))
        verifdns = os.system("ping -c 1 " + dns)
        if verifdns == 0:
            ip = (socket.gethostbyname(dns))
            import subprocess

            subprocess.call(["cd Photon &&  python3 photon.py -u " + dns," --dns"], shell=True)
            print(colored("[*] ---> Mapping Networking from DNS target: ok !", 'green'))
            print(colored("[*] -------------> Map Network DNS/Infos : Hyperionv2/Photon/", 'magenta'), dns)
        else:
            print(colored("[*] !!!! *Errors Dns* !!!!", 'red'))


    def close_Menu_General(self):
        self.Dialog.close()
    def close_Report_Analyse(self):
        self.report.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Controller = Controller()
    Controller.voir_Menu_general()
    sys.exit(app.exec_())
