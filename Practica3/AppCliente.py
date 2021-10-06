#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 19:39:10 2021

@author: ivan
"""
#INSTITUTO POLITÉCNICO NACIONAL
#ESCUELA SUPERIOR DE INGENIERÍA MECÁNICA ELÉCTRICA
#DEPARTAMENTO ACADÉMICO DE INGENIERÍA EN COMUNICACIONES Y ELECTRÓNICA
#ACADEMIA DE COMPUTACIÓN
#AGENTES INTELIGENTES EXPERTOS
#PROFESOR: POSADAS DURAN JUAN PABLO FRANCISCO
#ALUMNO: MARTÍNEZ MENDOZA CESAR IVÁN
#GRUPO: 9CV12
#TRABAJO: PRACTICA 3 JUEGO DEL GATO CON HEURISTICA


import socket # for networking
import pickle # for sending/receiving objects 

# import the game
from App import Gato

HOST = '127.0.0.1'  # the server's IP address 
PORT = 10000
      # the port we're connecting to 

# connect to the host
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print(f"\n                  Agentes inteligentes expertos  ")
print(f"                 Alumno: Martinez Mendoza Cesar Ivan  ")
print(f"               Practica3: Juego del gato con heuristica ")
print(f"        Direccion IP y numero de puerto ulizados: {s.getsockname()} ")
print(f"                       Applicacion Cliente ")

print(f"\n")

# set up the game
player_o = Gato("O")

# allow the player to suggest playing again
rematch = True

while rematch == True:
    # a header for an intense tic-tac-toe match! 
    print(f"\n   El agente cliente hace tiros al azar ")
 
    
    

    # the rest is in a loop; if either player has won, it exits 
    while player_o.ganar("O") == False and player_o.ganar("X") == False and player_o.empate() == False:
#El cliente es el primero en realizar un tiro
        print(f"\n       Tu turno!")
        player_o.tablero()
        player_coord = input(f"Ingresa coordenada: ")
        player_o.sharp(player_coord)

        # actualizacion del tablero
        player_o.tablero()

       
        x_symbol_list = pickle.dumps(player_o.symbol_list)
        s.send(x_symbol_list)

        # condicion de gane o de empate 
        if player_o.ganar("X") == True or player_o.empate() == True:
            break

        # actualizacion del tablero
        print(f"\n Turno contrario")
        o_symbol_list = s.recv(1024)
        o_symbol_list = pickle.loads(o_symbol_list)
        player_o.actualizacion(o_symbol_list)

    # mensajes
    if player_o.ganar("O") == True:
        print(f"Haz ganado!")
    elif player_o.empate() == True:
        print(f" Empate")
    else:
        print(f"Has perdido.")

  
 

s.close()