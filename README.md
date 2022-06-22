# Automap
### Herramienta para hacer escaneo manual o automático con nmap

![screenshot](https://user-images.githubusercontent.com/58263431/175098458-28a2276b-d8d9-46a7-b93e-e942d0b55d9d.png)

## Esta herramienta te permite ver en tiempo real tu *gateway* y tu *ip local*.
## Puedes usarla para hacer escaneo automatico o manual.
Ejemplos.

    AUTOMAP= Hace un scaner automatico con la ip 192.168.1.0/24 y los paremtros nmap -p- -sS --min-rate 5000 --open -vvv -Pn
    MANUALMAP= Escribes tu ip objetivo y aplica un escaner con los parametros nmap -p- -sS --min-rate 5000 --open -vvv -Pn

## Ejecutar como root :-> sudo ./main
