#!/usr/bin/python3
#######ESTETICA########
import pyfiglet
from termcolor import colored
#######SISTEMA#########
import netifaces
import os 
import socket
from automap import auto_map
from manualmap import manual_map
#from lookscan import look_test
#######Funcion menu########
def menu():

    while True:
        ###########VARIABLES#########################
        host_ip = socket.gethostbyname(socket.gethostname())
        gate_way = netifaces.gateways()
        only_gateway = gate_way['default'][netifaces.AF_INET][0]
        ###############Titulos-Red####################
        titulo = pyfiglet.figlet_format("Auto.Nmap", font="speed")
        print(colored(titulo, 'red'),colored("=====By-R4m3200=====", 'yellow'))

        print(colored("Gateway=>", 'red'),colored(only_gateway, 'green'),colored("Address=>", 'red'),colored(host_ip, 'green'))
        print(colored("1-Automap: \n2-Manualmap: \n3-Lookscan:", 'blue'))

        a = 1
        b = 2
        c = 3
        opcion = int(input(colored("==> ", 'red')))
        if opcion == 1:
            auto_map()
        elif opcion == 2:
            manual_map()
        elif opcion == 3:
            look_test()

        repetir = input("Realizar otro escaneo: Y/N ")
        
        if repetir == str('n'):
            print(colored("[!]Saliendo....", 'green'))
            break

menu()