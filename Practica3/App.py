#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 22:01:15 2021

@author: Martinez Mendoza Cesar Ivan
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

#creacion de la clase del juego
class Gato():

    def __init__(self, player_symbol):
      
        self.symbol_list = []

        # Se especifican los 9 expacios disponibleas al inicio del juego
        for i in range(9):
            self.symbol_list.append(" ") 

        # inicializacion de variable 
        self.player_symbol = player_symbol


    def restart(self):
        
        for i in range(9):
            self.symbol_list[i] = " "


    def tablero(self):
        # Construccion del tablero mediante renglones y lienas a imprimir
        #en donde se realiza con la intenciaon de realizar un tiro
        #mediante las coordenadas del tablero un ejemplo para la casilla 0 seria 
        #la coordenada A1
        print("\n       A   B   C\n")
        
        
        row_one = "   1   " + self.symbol_list[0]
        row_one += " ║ " + self.symbol_list[1]
        row_one += " ║ " + self.symbol_list[2]
        print(row_one)

        
        print("      ═══╬═══╬═══")

   
        row_two = "   2   " + self.symbol_list[3]
        row_two += " ║ " + self.symbol_list[4]
        row_two += " ║ " + self.symbol_list[5]
        print(row_two)

      
        print("      ═══╬═══╬═══")

       
        row_three = "   3   " + self.symbol_list[6]
        row_three += " ║ " + self.symbol_list[7]
        row_three += " ║ " + self.symbol_list[8]
        print(row_three, "\n")



    def sharp(self, grid_coord):
    
        if grid_coord[0].isdigit():
            grid_coord = grid_coord[1] + grid_coord[0]

        
        col = grid_coord[0].capitalize()
        row = grid_coord[1]

        # conversion de coordenadas
        grid_index = 0

        if row == "1":
            if col == "A":
                grid_index = 0
            elif col == "B":
                grid_index = 1
            elif col == "C":
                grid_index = 2
        elif row == "2":
            if col == "A":
                grid_index = 3
            elif col == "B":
                grid_index = 4
            elif col == "C":
                grid_index = 5
        elif row == "3":
            if col == "A":
                grid_index = 6
            elif col == "B":
                grid_index = 7
            elif col == "C":
                grid_index = 8

        if self.symbol_list[grid_index] == " ":
            self.symbol_list[grid_index] = self.player_symbol

#actualizacion del tablero conforme los tiros de los jugadores
    def actualizacion(self, new_symbol_list):
        for i in range(9):
            self.symbol_list[i] = new_symbol_list[i]
#condiciones para ganar

    def ganar(self, player_symbol):
     
        g = []
        for i in range(9):
            g.append(self.symbol_list[i])


        sym = player_symbol

        # Configuarain de coordenadas las cuales hacer que un agente gane
        if g[0] == sym and g[1] == sym and g[2] == sym:
            return True

       
        elif g[3] == sym and g[4] == sym and g[5] == sym:
            return True
        
        
        elif g[6] == sym and g[7] == sym and g[8] == sym:
            return True 

       
        elif g[0] == sym and g[3] == sym and g[6] == sym:
            return True 

        elif g[1] == sym and g[4] == sym and g[7] == sym:
            return True 

      
        elif g[2] == sym and g[5] == sym and g[8] == sym:
            return True

      
        elif g[2] == sym and g[4] == sym and g[6] == sym:
            return True 

       
        elif g[0] == sym and g[4] == sym and g[8] == sym:
            return True 

        return False


    def empate(self):
#busqueda de localizacon de espacios ya ocupoados
        num_blanks = 0
        for i in range(9):
                if self.symbol_list[i] == " ":
                    num_blanks += 1
#de no ser asi se tiene que se ha conseguido empate entre los agentes
        if self.ganar(self.player_symbol) == False and num_blanks == 0:
            return True
        else:
            return False