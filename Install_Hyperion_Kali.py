import os
import subprocess as sb

# Executed in mod root (sudo**) Important (Permission)
print("[System Auto_Installation : Programme Hyperion]")
print("Starting .. Auto-Install ...   librairy Python3/Python2/Externals Code ")

sb.call("apt-get install python3 theharvester python3-pip hydra nmap", shell=True)

sb.call("pip3 install python-whois google colorama urllib3 termcolor geoip2 colorama tldextract fierce ", shell=True)
sb.call("pip install BeautifulSoup termcolor ", shell=True) 
print("")





print(" [*] Install librairy Python3/2 : Termined !")
print("")
print("[*] starting ... Programs external : AutoConfig - Auto_Install - ...")
print("---------------------------------------------------------------------")

print("Install [Wafw00f] .... please patient !!!")
sb.call("git clone https://github.com/EnableSecurity/wafw00f", shell=True)
sb.Popen("cd  ./wafw00f", shell=True)
sb.Popen("chmod +x ./wafw00f/setup.py", shell=True)
sb.call("cd ./wafw00f/ && python3 setup.py install", shell=True)
print("------------> Test ... ")
sb.call("wafw00f https://example.org", shell=True)
print(">>> Install Wafw00f* : Termined !")
print("")

print(" [*] Install [Sqliv] : .... ! please patient !!!")
sb.call("git clone https://github.com/the-robot/sqliv.git", shell=True)
sb.Popen("cd  ./sqliv", shell=True)
sb.Popen("chmod +x ./sqliv/requirements.txt", shell=True)
sb.call("pip  install -r ./sqliv/requirements.txt", shell=True)
sb.Popen("chmod +x ./sqliv/setup.py", shell=True)
sb.call("python2 ./sqliv/setup.py -i", shell=True)
print("------------> Test ... ")

print(" >>> Install Sqliv* : Termined !")
print("")

print(" [*] Install [Wapiti] : ..... ! please patient !!!")
sb.call("git clone https://github.com/mbarbon/wapiti", shell=True)
sb.call("cd  ./wapiti", shell=True)
sb.Popen("chmod +x ./wapiti/setup.py", shell=True)
sb.run("cd ./wapiti/ && python setup.py install", shell=True)
print("------------> Test ... ")
print(" >>> Install Wapiti* : Termined !")
print("")

print(" [*] Install [cupp] : .... ! please patient !!!")
sb.call("git clone https://github.com/Mebus/cupp", shell=True)
sb.call("cd  ./cupp", shell=True)
sb.Popen("chmod +x ./cupp/cupp.py", shell=True)
print("------------> Test ... ")
sb.run("cd ./cupp/ && python3 cupp.py", shell=True)
print(" >>> Install CUPP* : Termined !")

print("Install [breacher] .... please patient !!!")
sb.call("git clone https://github.com/s0md3v/Breacher", shell=True)
sb.Popen("cd  ./Breacher && ", shell=True)
sb.Popen("chmod +x ./Breacher/Breacher.py", shell=True)
print("------------> Test ... ")
sb.call("cd ./Breacher/ && python breacher.py ", shell=True)
print(">>> Install Breacher* : Termined !")
print("")

print(" [*] Module --script CVE install >>> usr/share/nmap/script ")
sb.call("cd /usr/share/nmap/scripts/ && git clone https://github.com/vulnersCom/nmap-vulners.git", shell=True)
print("---------AutoTest on scanme.nmap.org  -- patient please 1 minute -")

print("-----------------------------------------------------------------------------------------------------------")
print("----------------------------[*Install Termined* !!!]--------------------------------------")
