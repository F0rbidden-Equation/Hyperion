#!/bin/bash
 
apt-get install git python3  python3-pip  nmap wapiti
pip3 install python-whois google colorama urllib3 termcolor geoip2 colorama tldextract fierce
pip install BeautifulSoup termcolor
 
 
cd /usr/share/nmap/scripts/ && git clone https://github.com/vulnersCom/nmap-vulners.git
 
git clone https://github.com/EnableSecurity/wafw00f
cd  wafw00f
python setup.py install
wafw00f https://example.org
 
git clone https://github.com/the-robot/sqliv.git
cd sqliv
sudo python2 setup.py -i
python sqliv.py -t www.example.com/index.php?id=1
 
 
 
git clone https://github.com/laramies/theHarvester
cd theHarvester
python3.7 -m pip install -r requirements.txt
python3.7 theHarvester.py -h
 
 
git clone https://github.com/Mebus/cupp
cd cupp
python3 cupp.py -h
 
git clone https://github.com/s0md3v/Breacher
cd Breacher
python breacher.py
