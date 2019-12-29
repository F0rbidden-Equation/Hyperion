# Project Hyperion

# Presentations :

   The program hyperion is a program called "Automate", playing the role of Swiss Knife in step of recognition, pentesting .
   This one, gathers several programs in 1 only, to facilitate the so-called "passive" Pentesting step. The objective is to facilitate
   the testing of networks, machines, services, as well as the detection of potential security flaws constituting the audited network.

## The program consists of 15 modules (functions) which are as follows :


```bash
     1) Scan infos Server       : DNS* scan scanner as well as DNS* information (Ip address, locations, date...)
     2) Scan Analysis Anonymat  : Scan by scanner, allows to determine if the target server uses Tor networks
     3) Test Version Servers    : Send request http, on port 80/443 to determine the version of the audited server
     4) Scan Security Servers   : Scanner security detections type: Waff firewall, information on security/security used
     5) Scan Admin Panel        : Scanner, Page Analysis, to determine the administration portal, web server
     6) Scan CVE Servers        : CVE scanner, detects all CVE* vulnerabilities by Database CVE online in real time
     7) Scan Advanced Network   : Scanner of advanced type allows to analyze ports, services, version of active services
     8) Scan Default Xss,sql,.. : Scanner Multiple detects flaws such as: Xss, Sql, Crlf, backup, blindsql, module nikto ...
     9) Scan Pages Default php  : Scanner of default pages on Php site, allows detection for SQL injection
    10) Recoon Bruteforce       : Analysis of communication services,  recognition by "open" ports, such as: SSH,FTP,Telnet,...
    11) Google Dork Research    : Vulnerable servers search via google using the "Dork" search method.
    12) Research Emails         : Search potentially active emails from a name, nickname, ...
    13) Detected Type DB/...    : Version Identification
    14) DNS Brute Force         : Secondary Adress DNS search assigned to the audited DNS* by forced raw method
    15) Profilers Password      : allows you to create a password list, using "Profilers" methods, personal info




```

## Installation

```python
Linux Platform Installation Guide :
   
     > Install
     # Ubuntu 18
     cd Hyperion
     sudo chmod + hyperion_Ubuntu_install.py
     sudo python3 hyperion_project.py
 
     > Install
     # Kali Linux 2019
     cd Hyperion
     sudo chmod + hyperion_kali_install.py
     sudo python3 hyperion_project.py

```

## # Graphical presentations, modules in the Hyperion program :
![Salam1-articleLarge](https://user-images.githubusercontent.com/59021489/71563083-3e761180-2a8a-11ea-8c07-fa4e30a73b7e.jpg)