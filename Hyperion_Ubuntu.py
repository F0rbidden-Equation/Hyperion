# -*- coding: utf-8 -*-
import socket
import sys
import subprocess
from urllib.request import urlopen
from googlesearch import search
from colorama import init
from termcolor import colored

import errno
import os
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from colorama import init
from termcolor import colored
import socket
import geoip2.database
import subprocess

menu_1 = ("1")
menu_2 = ("2")
menu_3 = ("3")
menu_4 = ("4")
menu_5 = ("5")
menu_6 = ("6")
menu_7 = ("7")
menu_8 = ("8")
menu_9 = ("9")
menu_10 = ("10")
menu_11 = ("11")
menu_12 = ("12")
menu_13 = ("13")
menu_14 = ("14")
menu_15 = ("15")
menu_16 = ("16")

c1 = (colored("[1] ", 'blue'))
c1_a = (colored(" Scan Infos Network", 'green'))
c2 = (colored("[2] ", 'blue'))
c2_a = (colored(" Scan Anonymat Servers ", 'green'))
c3 = (colored("[3] ", 'blue'))
c3_a = (colored(" Test Version  Servers", 'green'))
c4 = (colored("[4]", 'blue'))
c4_a = (colored("  Scan Security Servers", 'green'))
c5 = (colored("[5]", 'blue'))
c5_a = (colored("  Scan Admin Panel Servers", 'green'))
c6 = (colored("[6]", 'blue'))
c6_a = (colored("  Scan CVE Servers", 'green'))
c7 = (colored("[7]", 'blue'))
c7_a = (colored("  Scan Advanced network", 'green'))
c8 = (colored("[8]", 'blue'))
c8_a = (colored("  Scan Default Xss,sql,...", 'green'))
c9 = (colored("[9]", 'blue'))
c9_a = (colored("  Scan Pages Defaults(php) ", 'green'))
c10 = (colored("[10]", 'blue'))
c10_a = (colored(" Recoon BruteForce", 'green'))
c11 = (colored("[11]", 'blue'))
c11_a = (colored(" Attack BruteForce", 'green'))
c12 = (colored("[12]", 'blue'))
c12_a = (colored(" Research Google Dork", 'green'))
c13 = (colored("[13]", 'blue'))
c13_a = (colored(" Research Email by theHarvester", 'green'))
c14 = (colored("[14]", 'blue'))
c14_a = (colored(" Detected Type DB mssql/Mysql/...", 'green'))
c15 = (colored("[15]", 'blue'))
c15_a = (colored(" DNS brute Force ", 'green'))
c16 = (colored("[16] ", 'blue'))
c16_a = (colored("Profiler Password", 'green'))


###########################################
c_Valide = (colored("[*]", 'green'))
c_Error = (colored("[*]", 'red'))


###########################################

def Menu_Infos_Network():
    print('----------  Menu Infos Network ------------')
    dns = input(colored("Enter your DNS target :", "green"))

    reader = geoip2.database.Reader('GeoLite2-City.mmdb')
    # print(socket.gethostbyname(dns))
    ip = (socket.gethostbyname(dns))
    response = reader.city(ip)
    country = (response.country.name)
    ifdns = (colored("|------> Dns : ", 'red'))
    print(ifdns + dns)
    ifip = (colored("|------> AdressIP: ", 'red'))
    print(ifip + ip)
    ifgeo = (colored("|------> Geolocation:", 'red'))
    # print(ifgeo + country)
    ifgeocity = (colored(" | City:", 'green'))
    city = (response.city.name)
    print(ifgeo, country, ifgeocity, city)
    print(colored("------------------[Scanning Informations on Admin / Servers] -------------------------", 'blue'))
    import whois

    w = whois.whois(ip)
    # print(w)
    emails = (w.emails)
    emcolor = (colored("|-----> Emails :", 'red'))
    print(emcolor, emails)
    dnsseccolor = (colored("|-----> Dns Secondary :", 'red'))
    dnssec = (w.dnssec)
    print(dnssec)
    namecolor = (colored("|-----> Name :", 'red'))
    name = (w.name)
    print(namecolor, name)
    orgcolor = (colored("|-----> Corporations :", 'red'))
    org = (w.org)
    print(orgcolor, org)
    adresscolor = (colored("|-----> Adress :", 'red'))
    adress = (w.adress)
    print(adresscolor, adress)
    citycolor = (colored("|-----> City :", 'red'))
    city = (w.city)
    print(citycolor, city)
    statecolor = (colored("|-----> State :", 'red'))
    state = (w.state)
    print(statecolor, state)
    zipcolor = (colored("|-----> Zip :", 'red'))
    zipcode = (w.zipcode)
    print(zipcolor, zipcode)
    colorcount = (colored("|-----> Country :", 'red'))
    country2 = (w.country)
    print(colorcount, country)
    servcolor = (colored("|-----> Names Servers :", 'red'))
    names_servers = (w.name_servers)
    print(servcolor, names_servers)
    creatio_datecolor = (colored("|-----> Creation Date Servers :", 'red'))
    creation_date = (w.creation_date)
    print(creatio_datecolor, creation_date)
    updated_datecolor = (colored("|-----> Last Update Date Servers :", 'red'))
    updated_date = (w.updated_date)
    print(updated_datecolor, updated_date)
    expiration_color = (colored("|-----> Expirations Date Servers :", 'red'))
    expiration_date = (w.expiration_date)
    print(expiration_color, expiration_date)

    print(colored("--------------------- > Enumetaration subdomains [accounts admin ads]     " + ip, 'blue'))
    subprocess.call("fierce --domain " + dns + " --subdomains accounts admin ads", shell=True)
    print(colored("--------------------------------------------------------------------------------------------", 'blue'))
    print(colored("----------------------> Enumeration subdomains    [admin]       -->       " + ip, 'blue'))
    subprocess.call("fierce --domain " + dns + " --subdomains admin --traverse 10", shell=True)
    print(colored("--------------------------------------------------------------------------------------------", 'blue'))
    print(colored("-----------------------> Enumeration subdomains    [mail]       -->        " + ip, 'blue'))
    subprocess.call("fierce --domain " + dns + " --subdomains mail --connect", shell=True)
    print(colored("--------------------------------------------------------------------------------------------", 'blue'))
    print(colored("--------------------------------------------------------------------------------------------", 'blue'))
    end = input(colored("Press *Enter* for return [Selection Menu Modules Multiple]", 'red'))
    Presentation()
    Select_Mod()


def Menu_Anonymat_Servers():
    print(colored("-------------------[Scanning System Anonymisation use by Network Targets]------------", 'green'))
    print("")
    dns = input(colored("Enter your DNS target :", "green"))
    ip = (socket.gethostbyname(dns))
    reader = geoip2.database.Reader('GeoIP2-Anonymous-IP-Test.mmdb')
    response = reader.anonymous_ip(ip)

    def AnonymousIP():
        print(colored("[*] Analyse... [Anonymous IP] on servers Targets ", 'blue'))
        Anonymous = (response.is_anonymous)

        if Anonymous == 0:  # False = 0  / True = 1
            print(colored("Security [IP Anonymous] = No Actived", 'green'))
        elif Anonymous == 1:
            print(colored("Security [IP Anonymous] = Actived", 'red'))
        else:
            print(colored("IP adress No Valide", 'red'))

    def vpnIP():
        print(colored("[*] Analyse ... [Vpn] use by AdressIP", 'blue'))
        vpn = (response.is_anonymous_vpn)

        if vpn == 0:  # False = 0  / True = 1
            print(colored("Security [vpn] = No Actived", 'green'))
        elif vpn == 1:
            print(colored("Security [vpn] = Actived", 'red'))
        else:
            print(colored("IP adress No Valide", 'red'))

    def proxyIP():
        print(colored("[*] Analyse ... [public_proxy] use by Network Targets", 'blue'))
        proxy = (response.is_public_proxy)

        if proxy == 0:  # False = 0  / True = 1
            print(colored("Security [public_proxy] = No Actived", 'green'))
        elif proxy == 1:
            print(colored("Security [public_proxy] = Actived", 'red'))
        else:
            print(colored("IP Adress No Valide", 'red'))



    def hostingIP():
        print(colored("[*] Analyse ... [hosting_provider] use by Network Targets", 'blue'))
        hosting = (response.is_hosting_provider)

        if hosting == 0:  # False = 0  / True = 1
            print(colored("Security [hosting_provider] = No Actived", 'green'))
        elif hosting == 1:
            print(colored("Security [hosting_provider] = No Actived", 'red'))
        else:
            print(colored("IP Adress No Valide", 'red'))

    def TorIP():
        print(colored("[*] Analyse ... [tor_exit_node] use by Network Targets", 'blue'))
        Tor = (response.is_anonymous_vpn)

        if Tor == 0:  # False = 0  / True = 1
            print(colored("Security [tor_exit_node] = No Actived", 'green'))
        elif Tor == 1:
            print(colored("Security [tor_exit_node] = Actived", 'red'))
        else:
            print(colored("IP Adress No Valide", 'red'))


    AnonymousIP()
    vpnIP()
    proxyIP()
    hostingIP()
    TorIP()
    input(colored("Press *Enter* for return [Selection Menu Modules Multiple]", 'red'))
    Presentation()
    Select_Mod()

def Menu_Version_Servers():
    dns = input(colored("Enter your DNS target :", "green"))
    ip = (socket.gethostbyname(dns))
    # subprocess.call("nickto -h ")
    hosts = [ip]
    ports = [80, 443]
    color1 = (colored("|---> [+] Connecting to [", 'green'))
    colorP = (colored("] | port: ", 'green'))
    print(colored("--" * 60, 'green'))

    print(colored("--" * 60, 'green'))
    for host in hosts:
        for port in ports:
            try:

                print(color1 + host + colorP + str(port))
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(5)
                result = s.connect_ex((host, port))


                if port == 80:
                    ipport = (ip + " 80")
                    print(colored(">> Services [HTTP] 80  > open ", 'blue'))
                    subprocess.call("printf 'GET / HEAD HTTP/1.0\n' | nc " + ipport, shell=True)
                elif port == 443:
                    ipport2 = (ip + " 443")
                    print(colored(">> Services [HTTP] 443  > open ", 'blue'))
                    subprocess.call("printf 'GET / HEAD HTTP/1.0\n' | nc " + ipport2, shell=True)
                    print("")
                    input(colored("Press *Enter* for return [Selection Menu Modules Multiple]", 'red'))
                    Presentation()
                    Select_Mod()


                else:
                    print("port no detected")

            except:
                input(colored("Press *Enter* for return [Selection Menu Modules Multiple]", 'red'))
                Presentation()
                Select_Mod()


def Menu_Admin_Panel_Servers():
    dns = input(colored("Enter your DNS target :", "green"))
    ip = (socket.gethostbyname(dns))
    print(colored("----------------------System Automate AdminFinder ---------------------------------------:", 'blue'))
    subprocess.call("cd ./Breacher/ && python breacher.py -u " + ip , shell=True)
    input(colored("Press *Enter* for return [Selection Menu Modules Multiple]", 'red'))
    Presentation()
    Select_Mod()


def Menu_CVE_Servers():
    dns = input(colored("Enter your *DNS* / [no ip]! target :", "green"))
    ip = (socket.gethostbyname(dns))
    print(colored("----------------------System Automate nmap Module CVE    *!Please Patient 1 Minute!*  :", 'blue'))
    subprocess.call("sudo nmap --script nmap-vulners -sV -Pn " + dns, shell=True)
    input(colored("Press *Enter* for return [Selection Menu Modules Multiple]", 'red'))
    Presentation()
    Select_Mod()


def Menu_Security_Servers():
    dns = input(colored("Enter your DNS target :", "green"))
    ip = (socket.gethostbyname(dns))

    print(colored("--------------------------------------------------------------------------------------------", 'blue'))
    print(colored("------------------------ [Identify : Type WaF Secure] -----------------------------------------",'blue'))
    subprocess.call("wafw00f " + ip, shell=True) #problem ide but its ok
    print(colored("------------------------ [Identify : Security Firewall] -------------------------------------------------",'blue'))
    subprocess.call("nmap -p80,443 --script http-waf-fingerprint --script-args http-waf-fingerprint.intensive=1 " + ip , shell=True)
    print(colored("--------------------------------------------------------------------------------------------", 'blue'))
    print(colored("------------------------ [Identify : Pages Errors] -----------", 'blue'))
    subprocess.call("nmap -p80,443 --script http-errors " + ip, shell=True)
    print("")
    input(colored("Press *Enter* for return [Selection Menu Modules Multiple]", 'red'))
    Presentation()
    Select_Mod()


def Menu_Advanced_network():
    dns = input(colored("Enter your DNS target :", "green"))
    ip = (socket.gethostbyname(dns))
    print(colored("----------------------Scan Advanced Network ---------------------------------- :", 'blue'))
    subprocess.call("sudo nmap -O -A -sV -Pn " + dns, shell=True)
    input(colored("Press *Enter* for return [Selection Menu Modules Multiple]", 'red'))
    Presentation()
    Select_Mod()


def Menu_Pages_php():
    print("sqliv")
    print("--------------------------------Research defaults PHP for Injection-----------------------------------")
    print("")
    url = input(colored("Enter your Url website (http://... php): ", 'red' ))
    print("")
    subprocess.call("cd ./sqliv/ && python sqliv.py -t " + url, shell=True)
    input(colored("Press *Enter* for return [Selection Menu Modules Multiple]", 'red'))
    Presentation()
    Select_Mod()


def Menu_bruteforce_R():
    dns = input(colored("Enter your DNS target :", "green"))
    ip = (socket.gethostbyname(dns))
    hosts = [ip]
    ports = [21, 22, 23, 80, 110, 119, 143, 445, 465, 512, 513, 514, 563, 993, 1433, 2525, 3306, 5432]
    color1 = (colored("|---> [+] Connecting to [", 'green'))
    colorP = (colored("] | port: ", 'green'))
    print(colored("--" * 60, 'green'))
    serv = (colored("ssh ftp telnet vnc mysql mssql postgresql rsh ....", 'red'))
    print("... Starting Detections Protocoles 'open' on the network Targets > " + serv)
    print(colored("--" * 60, 'green'))
    for host in hosts:
        for port in ports:
            try:

                print(color1 + host + colorP + str(port))
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(5)
                result = s.connect_ex((host, port))
                if result == 0:
                    print("  [*] Port " + str(port) + " Service found !")

                elif port == 21:
                    print(colored(">> Analyse Services [FTP] [21]   ", 'blue'))

                elif port == 22:
                    print(colored(">> Analyse Services [SSH] [22]  ", 'blue'))

                elif port == 23:
                    print(colored(">> Analyse Services [Telnet] [23] ", 'blue'))

                elif port == 25:
                    print(colored(">> *Analyse Services [Smtp]  [25] ", 'blue'))

                elif port == 80:
                    print(colored(">> Analyse Services on port [80]", 'blue'))


                elif port == 110:
                    print(colored(">> Analyse Services [Pop3] [110] ", 'blue'))

                elif port == 119:
                    print(colored(">> Analyse Services [Nmtp] [119]", 'blue'))

                elif port == 143:
                    print(colored(">> Analyse Services [Imap] [143]", 'blue'))

                elif port == 465:
                    print(colored(">> Analyse Services [Smtp_ExtraSecure]  [465]", 'blue'))

                elif port == 512:
                    print(colored(">> Analyse Services [R_exe] [512] ", 'blue'))


                elif port == 513:
                    print(colored(">> Analyse Services [R_login] [513]", 'blue'))

                elif port == 514:
                    print(colored(">> Analyse Services [RSH] on port [514]", 'blue'))

                elif port == 563:
                    print(colored(">> Analyse Services [Nmtp_Secure] [563]", 'blue'))

                elif port == 993:
                    print(colored(">> Analyse Services [Imap_Secure] [993] ", 'blue'))

                elif port == 1433:
                    print(colored(">> Analyse Services [MSSQL] [1433] ", 'blue'))

                elif port == 2525:
                    print(colored(">> Analyse Services [Smtp_Secure] [2525] ", 'blue'))

                elif port == 3306:
                    print(colored(">> Analyse Services [MySQL] [3306]", 'blue'))

                elif port == 5432:
                    print(colored(">> Analyse Services [Posgresql] [5432]", 'blue'))
                    print("")
                    input(colored("Press *Enter* for return [Selection Menu Modules Multiple]", 'red'))
                    Presentation()
                    Select_Mod()





            except:
                pass
                input(colored("Press *Enter* for return [Selection Menu Modules Multiple]", 'red'))
                Presentation()
                Select_Mod()


def Menu_scan_defaults():
    dns = input(colored("Enter your DNS target :", "green"))
    ip = (socket.gethostbyname(dns))

    subprocess.call("cd ./wapiti/src && python wapiti.py " + ip + " -u -n 5 -b domain -v 2 -o /tmp/outfile.html  ", shell=True)
    end = input(colored("Press *Enter* for return [Selection Menu Modules Multiple]", 'red'))
    Presentation()
    Select_Mod()


def Menu_G():
    dns = input(colored("Enter your DNS target :", "green"))
    ip = (socket.gethostbyname(dns))
    print('ok')
    end = input(colored("Press *Enter* for return [Selection Menu Modules Multiple]", 'red'))
    Presentation()
    Select_Mod()


def Menu_EmailR():
    mail_name = input(colored("Enter your name of research (example : steven.gmail) :", 'magenta'))
    subprocess.run("cd ./theHarvester/ && python3 theHarvester.py -d " + mail_name + " -l 500 -b google", shell=True)
    print("")
    end = input(colored("Press *Enter* for return [Selection Menu Modules Multiple]", 'red'))
    Presentation()
    Select_Mod()


def Dns_Force():
    dns = input(colored("Enter your DNS target :", "green"))
    ip = (socket.gethostbyname(dns))
    print(colored("-------please patient !-2 minute --------- [DNS Brute Force] ---------------------------------------",'blue'))
    subprocess.call("nmap -p80,443 --script dns-brute " + dns, shell=True)
    end = input(colored("Press *Enter* for return [Selection Menu Modules Multiple]", 'red'))
    Presentation()
    Select_Mod()


def Scan_Security():
    dns = input(colored("Enter your DNS target :", "green"))
    ip = (socket.gethostbyname(dns))
    print(colored("------------------------ [Identify : Type WaF Secure] -----------------------------------------",'blue'))
    subprocess.call("wafw00f " + ip, shell=True)
    print(colored("------------------------ [Identify : Security Firewall] -------------------------------------------------",'blue'))
    subprocess.call("nmap -p80,443 --script http-waf-fingerprint --script-args http-waf-fingerprint.intensive=1" + ip, shell=True)
    print(colored("--------------------------------------------------------------------------------------------", 'blue'))
    print(colored("------------------------ [Identify : Versions DataBase] -------------------------------------------------",'blue'))
    subprocess.call("wafw00f " + ip, shell=True)
    print(colored("-----------------------------------------------------------------------------------------------",'blue'))

    print(colored("-----------------------------------------------------------------------------------------------",'blue'))
    print(colored("------------------------ [Identify : Pages Errors] -----------", 'blue'))
    subprocess.call("--script http-errors targetWebsite.com" + ip, shell=True)
    input(colored("Press *Enter* for return [Selection Menu Modules Multiple]", 'red'))
    Presentation()
    Select_Mod()


def Menu_Research_dork():
    dork = input(colored("Enter your Dork : ", 'magenta'))  # part research
    tld1 = input(colored("Enter your specifications (com ,org,... ):", 'magenta'))
    lang1 = input(colored("Enter your Specifications 'lang' (ex : en ,fr,...) :", 'magenta'))
    for url in search(dork, tld=tld1, lang=lang1, num=10, start=0, stop=None, pause=2.0):
        print(colored("[*]", 'green') + url)
        # print(colored("[*] Save page..... txt : ", 'magenta') + url)
        import tldextract
        dns = tldextract.extract(url)
        (dns.subdomain, dns.domain, dns.suffix)
        dns2 = (dns.registered_domain)

        from urllib.request import Request, urlopen
        from socket import error as SocketError  # part web research
        import errno
        try:

            html = urlopen(url)

        except SocketError as e:
            print(colored("[*] Erno_error Bypass Actived", 'green'))
        except HTTPError as e:
            print(colored("[*] HTTP error Bypass Actived", 'green'))
        except URLError as e:
            print(colored("[*] Server not found !!! Bypass Actived!", 'green'))
        except ValueError as e:
            print(colored("[*] Valors error", 'green'))
        except socket.gaierror as e:
            print(colored("[*] Errors gaierror", 'green'))


        else:
            print("[*] " + url)

    input(colored("Press *Enter* for return [Selection Menu Modules Multiple]", 'red'))
    Presentation()
    Select_Mod()
    # print(html.read().decode('utf-8', 'ignore'))


def Menu_profiler_passwords():
    print("Profilers Passwords")
    subprocess.run("cd ./cupp/ && python3 cupp.py -i ", shell=True)
    input(colored("Press *Enter* for return [Selection Menu Modules Multiple]", 'red'))
    Presentation()
    Select_Mod()


def Menu_attack_bruteF():
    dns = input(colored("Enter your DNS target :", "green"))
    ip = (socket.gethostbyname(dns))
    services = ("Enter your service example : mysql >>> ")
    subprocess.call("hydra -L /root/Desktop/user.txt –P /root/Desktop/pass.txt" + ip + services, shell=True)
    input(colored("Press *Enter* for return [Selection Menu Modules Multiple]", 'red'))
    Presentation()
    Select_Mod()


def Detected_typeDB():
    dns = input(colored("Enter your DNS target :", "green"))
    ip = (socket.gethostbyname(dns))
    hosts = [ip]
    ports = [1433, 1434, 3306, 1583,3050, 3306, 3351, 5432]
    color1 = (colored("|---> [+] Connecting to [", 'green'))
    colorP = (colored("] | port: ", 'green'))
    print(colored("--" * 60, 'green'))
    serv = (colored("Microsoft SQL Server ,Pervasive SQL, Firebird & Interbase ,MySQL / MariaDB ,PostgreSQL ", 'red'))
    print("... Starting Detections Protocoles 'open' on the network Targets > " + serv)
    print(colored("--" * 60, 'green'))
    for host in hosts:
        for port in ports:
            try:

                print(color1 + host + colorP + str(port))
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(5)
                result = s.connect_ex((host, port))
                if result == 0:
                    print(" [*] Services DataBase Found !!!! " + str(port) + " open!")

                if port == 1433:
                    print(colored(">> Test .. TCP Microsoft SQL Server port [1433]  ", 'blue'))

                if port == 1434:
                    print(colored(">> Test .. UDP Microsoft SQL Server port [1434]", 'blue'))
                if port == 1583:
                    print(colored(">> Test .. TCP [Pervasive SQL] port [1583]  ", 'blue'))
                if port == 3050:
                    print(colored(">> Test .. TCP [Firebird & Interbase] port [3050] ", 'blue'))

                if port == 3306:
                    print(colored(">> Test .. TCP  [MySQL / MariaDB] port [3306]  ", 'blue'))


                if port == 3351:
                    print(colored(">> Test .. TCP [Pervasive SQL] port [3351]  ", 'blue'))
                if port == 5432:
                    print(colored(">> Test .. TCP [PostgreSQL] port [5432]  ", 'blue'))
            except:
                pass
    print("")
    input(colored("Press *Enter* for return [Selection Menu Modules Multiple]", 'red'))
    Presentation()
    Select_Mod()



def Presentation():
    print(colored("             [Hyperion OSINT Automate Research] ", 'blue'))
    print(colored("""
    ██╗  ██╗██╗   ██╗██████╗ ███████╗██████╗ ██╗ ██████╗ ███╗   ██╗
    ██║  ██║╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██║██╔═══██╗████╗  ██║
    ███████║ ╚████╔╝ ██████╔╝█████╗  ██████╔╝██║██║   ██║██╔██╗ ██║
    ██╔══██║  ╚██╔╝  ██╔═══╝ ██╔══╝  ██╔══██╗██║██║   ██║██║╚██╗██║
    ██║  ██║   ██║   ██║     ███████╗██║  ██║██║╚██████╔╝██║ ╚████║
    ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝ """, 'blue'))
    print(colored("                   [Coded by Lazarus®]", 'green'))
    print("")
    print("")
    print(colored("[Selection Menu Modules Multiple]", 'blue'))
    print(colored("--" * 70, 'green'))
    print(c1 + c1_a, "    |", c5 + c5_a, " | ", c9 + c9_a, " |", c13 + c13_a)
    print(c2 + c2_a, "|", c6 + c6_a, "         | ", c10 + c10_a, "         |", c14 + c14_a)
    print(c3 + c3_a, " |", c7 + c7_a, "    | ", c11 + c11_a, "         |", c15 + c15_a)
    print(c4 + c4_a, " |", c8 + c8_a, " | ", c12 + c12_a, "      |", c16 + c16_a)
    print(colored("--" * 70, 'green'))

def Select_Mod():
    Selection = input(colored('|----> Selection Modules >>> :', 'blue'))

    if str(Selection) == menu_1:
        Menu_Infos_Network()

    elif str(Selection) == menu_2:
        Menu_Anonymat_Servers()

    elif str(Selection) == menu_3:
        Menu_Version_Servers()

    elif str(Selection) == menu_4:
        Menu_Security_Servers()

    elif str(Selection) == menu_5:
        Menu_Admin_Panel_Servers()


    elif str(Selection) == menu_6:
        Menu_CVE_Servers()

    elif str(Selection) == menu_7:
        Menu_Advanced_network()



    elif str(Selection) == menu_8:
        Menu_scan_defaults()

    elif str(Selection) == menu_9:
        Menu_Pages_php()

    elif str(Selection) == menu_10:
        Menu_bruteforce_R()

    elif str(Selection) == menu_11:
        Menu_attack_bruteF()

    elif str(Selection) == menu_12:
         Menu_Research_dork()


    elif str(Selection) == menu_13:
         Menu_EmailR()

    elif str(Selection) == menu_14:
         Detected_typeDB()


    elif str(Selection) == menu_15:
         Dns_Force()

    elif str(Selection) == menu_16:
         Menu_profiler_passwords()



    else:
        print(c_Error,"Error Selection\n ")
        Select_Mod()


Presentation()
Select_Mod()