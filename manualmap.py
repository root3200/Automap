#!/usr/bin/python3
import os

def manual_map():
    print("Manual Nmap: ")
    ip = str(input("Escribe IP: "))
    os.system("nmap -p- -sS --min-rate 5000 --open -vvv -Pn " + ip)