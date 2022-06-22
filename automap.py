#!/usr/bin/python3
import os

def auto_map():
    print("Auto nmap para: 191.168.1.0/24")
    a = str("192.168.1.0/24")
    os.system("nmap -p- -sS --min-rate 5000 --open -vvv -Pn -oG test " + a)