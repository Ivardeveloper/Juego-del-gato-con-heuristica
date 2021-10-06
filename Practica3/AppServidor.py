
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


#importacion de librerias de red
import socket 
import pickle 

# import the game
from App import Gato

#Tomando en cuenta que la direccion 127.0.0.1 es igual ala palbra localhost
HOST = '127.0.0.1' 
PORT = 10000

# set up the server 

#Levantando el servidor
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

# se aceptan todas las peticiones por parte del cliente
client_socket, client_address = s.accept()
print(f"\n                  Agentes inteligentes expertos  ")
print(f"                 Alumno: Martinez Mendoza Cesar Ivan  ")
print(f"               Practica3: Juego del gato con heuristica ")
print(f"        Direccion IP y numero de puerto ulizados: {client_address} ")
print(f"                       Applicacion Servidor ")
print(f"\n")


# iniciando el juego
player_x = Gato("X")

rematch = True

while rematch == True:
    print(f"\n El agente Servidor utiliza la heuristica para tomar una decicion a tirar")

  # draw the grid
    player_x.tablero()
    print(f"\n\n Turno contrario")
    x_symbol_list = client_socket.recv(1024)
    x_symbol_list = pickle.loads(x_symbol_list)
    player_x.actualizacion(x_symbol_list)
    

    # clico de repeticion, con las condiciones en las cuales codeja continuar el juego
    while player_x.ganar("O") == False and player_x.ganar("X") == False and player_x.empate() == False:
        
    
         
        print(f"\n          Tu turno")
        player_x.tablero()
        player_coord = input(f"Ingresa la cordenada: ")
        player_x.sharp(player_coord)

        #tablaero
        player_x.tablero()

        
        o_symbol_list = pickle.dumps(player_x.symbol_list)
        client_socket.send(o_symbol_list)

        #condiciones de gane y empate
        if player_x.ganar("O") == True or player_x.empate() == True:
            break

        # actualizacion de tablero
        print(f"\n\n Turno contrario")
        x_symbol_list = client_socket.recv(1024)
        x_symbol_list = pickle.loads(x_symbol_list)
        player_x.actualizacion(x_symbol_list)
        
        


    # menjase 
    if player_x.ganar("X") == True:
        print(f"            Has ganado!")
    elif player_x.empate() == True:
        print(f"            ha sido empate")
    else:
        print(f"        El cliente ha ganado")

   

client_socket.close()