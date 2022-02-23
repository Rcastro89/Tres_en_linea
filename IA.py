#!/usr/bin/python3

import random


class Jug_IA():

    def __init__(self, dic, dif):
        self.mydict = dic
        self.mydific = dif

    def jugadaIA(self):
        self.jugadas_disponibles = []
        self.jugadas_oponente = []
        self.mis_jugadas = []
        for k, v in self.mydict.items():
            if v == False:
                self.jugadas_disponibles.append(k)
            elif v == "X":
                self.jugadas_oponente.append(k)
            elif v == "O":
                self.mis_jugadas.append(k)
        if self.mydific == "Facil":
            seleccion_jugada_IA = random.choice(self.jugadas_disponibles)
            return seleccion_jugada_IA
        elif self.mydific == "Intermedio":
            return self.intermedio()
        elif self.mydific == "Dificil":
            return self.dificil()
        else:
            return self.legendario()

    def intermedio(self):
        tipo_de_jugada = ["inteligente", "aleatoria"]
        jugada = random.choice(tipo_de_jugada)
        if jugada == "inteligente":
            seleccion_jugada_IA = self.dificil()
        else:
            seleccion_jugada_IA = random.choice(self.jugadas_disponibles)
        return seleccion_jugada_IA

    def dificil(self):
        if 1 in self.jugadas_oponente and 2 in self.jugadas_oponente:
            if 3 in self.jugadas_disponibles:
                seleccion_jugada_IA = 3
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = random.choice(self.jugadas_disponibles)
        if 1 in self.jugadas_oponente and 3 in self.jugadas_oponente:
            if 2 in self.jugadas_disponibles:
                seleccion_jugada_IA = 2
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = random.choice(self.jugadas_disponibles)
        if 1 in self.jugadas_oponente and 4 in self.jugadas_oponente:
            if 7 in self.jugadas_disponibles:
                seleccion_jugada_IA = 7
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = random.choice(self.jugadas_disponibles)
        if 1 in self.jugadas_oponente and 7 in self.jugadas_oponente:
            if 4 in self.jugadas_disponibles:
                seleccion_jugada_IA = 4
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = random.choice(self.jugadas_disponibles)
        if 1 in self.jugadas_oponente and 5 in self.jugadas_oponente:
            if 9 in self.jugadas_disponibles:
                seleccion_jugada_IA = 9
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = random.choice(self.jugadas_disponibles)
        if 1 in self.jugadas_oponente and 9 in self.jugadas_oponente:
            if 5 in self.jugadas_disponibles:
                seleccion_jugada_IA = 5
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = random.choice(self.jugadas_disponibles)
        if 2 in self.jugadas_oponente and 3 in self.jugadas_oponente:
            if 1 in self.jugadas_disponibles:
                seleccion_jugada_IA = 1
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = random.choice(self.jugadas_disponibles)
        if 2 in self.jugadas_oponente and 5 in self.jugadas_oponente:
            if 8 in self.jugadas_disponibles:
                seleccion_jugada_IA = 8
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = random.choice(self.jugadas_disponibles)
        if 2 in self.jugadas_oponente and 8 in self.jugadas_oponente:
            if 5 in self.jugadas_disponibles:
                seleccion_jugada_IA = 5
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = random.choice(self.jugadas_disponibles)
        if 3 in self.jugadas_oponente and 6 in self.jugadas_oponente:
            if 9 in self.jugadas_disponibles:
                seleccion_jugada_IA = 9
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = random.choice(self.jugadas_disponibles)
        if 3 in self.jugadas_oponente and 9 in self.jugadas_oponente:
            if 6 in self.jugadas_disponibles:
                seleccion_jugada_IA = 6
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = random.choice(self.jugadas_disponibles)
        if 3 in self.jugadas_oponente and 5 in self.jugadas_oponente:
            if 7 in self.jugadas_disponibles:
                seleccion_jugada_IA = 7
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = random.choice(self.jugadas_disponibles)
        if 3 in self.jugadas_oponente and 7 in self.jugadas_oponente:
            if 5 in self.jugadas_disponibles:
                seleccion_jugada_IA = 5
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = random.choice(self.jugadas_disponibles)
        if 4 in self.jugadas_oponente and 7 in self.jugadas_oponente:
            if 1 in self.jugadas_disponibles:
                seleccion_jugada_IA = 1
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = random.choice(self.jugadas_disponibles)
        if 4 in self.jugadas_oponente and 5 in self.jugadas_oponente:
            if 6 in self.jugadas_disponibles:
                seleccion_jugada_IA = 6
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = random.choice(self.jugadas_disponibles)
        if 4 in self.jugadas_oponente and 6 in self.jugadas_oponente:
            if 5 in self.jugadas_disponibles:
                seleccion_jugada_IA = 5
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = random.choice(self.jugadas_disponibles)
        if 5 in self.jugadas_oponente and 6 in self.jugadas_oponente:
            if 4 in self.jugadas_disponibles:
                seleccion_jugada_IA = 4
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = random.choice(self.jugadas_disponibles)
        if 5 in self.jugadas_oponente and 7 in self.jugadas_oponente:
            if 3 in self.jugadas_disponibles:
                seleccion_jugada_IA = 3
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = random.choice(self.jugadas_disponibles)
        if 5 in self.jugadas_oponente and 8 in self.jugadas_oponente:
            if 2 in self.jugadas_disponibles:
                seleccion_jugada_IA = 2
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = random.choice(self.jugadas_disponibles)
        if 5 in self.jugadas_oponente and 9 in self.jugadas_oponente:
            if 1 in self.jugadas_disponibles:
                seleccion_jugada_IA = 1
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = random.choice(self.jugadas_disponibles)
        if 6 in self.jugadas_oponente and 9 in self.jugadas_oponente:
            if 3 in self.jugadas_disponibles:
                seleccion_jugada_IA = 3
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = random.choice(self.jugadas_disponibles)
        if 7 in self.jugadas_oponente and 8 in self.jugadas_oponente:
            if 9 in self.jugadas_disponibles:
                seleccion_jugada_IA = 9
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = random.choice(self.jugadas_disponibles)
        if 7 in self.jugadas_oponente and 9 in self.jugadas_oponente:
            if 8 in self.jugadas_disponibles:
                seleccion_jugada_IA = 8
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = random.choice(self.jugadas_disponibles)
        if 8 in self.jugadas_oponente and 9 in self.jugadas_oponente:
            if 7 in self.jugadas_disponibles:
                seleccion_jugada_IA = 7
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = random.choice(self.jugadas_disponibles)
        if 5 in self.jugadas_disponibles:
            seleccion_jugada_IA = 5
        else:
            seleccion_jugada_IA = random.choice(self.jugadas_disponibles)
        return seleccion_jugada_IA
    
    def legendario(self):
        esquinas = [1, 3, 7, 9]
        if 1 in self.mis_jugadas and 2 in self.mis_jugadas:
            if 3 in self.jugadas_disponibles:
                seleccion_jugada_IA = 3
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = self.dificil()
                return seleccion_jugada_IA
        if 1 in self.mis_jugadas and 3 in self.mis_jugadas:
            if 2 in self.jugadas_disponibles:
                seleccion_jugada_IA = 2
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = self.dificil()
                return seleccion_jugada_IA
        if 1 in self.mis_jugadas and 4 in self.mis_jugadas:
            if 7 in self.jugadas_disponibles:
                seleccion_jugada_IA = 7
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = self.dificil()
                return seleccion_jugada_IA
        if 1 in self.mis_jugadas and 7 in self.mis_jugadas:
            if 4 in self.jugadas_disponibles:
                seleccion_jugada_IA = 4
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = self.dificil()
                return seleccion_jugada_IA
        if 1 in self.mis_jugadas and 5 in self.mis_jugadas:
            if 9 in self.jugadas_disponibles:
                seleccion_jugada_IA = 9
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = self.dificil()
                return seleccion_jugada_IA
        if 1 in self.mis_jugadas and 9 in self.mis_jugadas:
            if 5 in self.jugadas_disponibles:
                seleccion_jugada_IA = 5
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = self.dificil()
                return seleccion_jugada_IA
        if 2 in self.mis_jugadas and 3 in self.mis_jugadas:
            if 1 in self.jugadas_disponibles:
                seleccion_jugada_IA = 1
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = self.dificil()
                return seleccion_jugada_IA
        if 2 in self.mis_jugadas and 5 in self.mis_jugadas:
            if 8 in self.jugadas_disponibles:
                seleccion_jugada_IA = 8
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = self.dificil()
                return seleccion_jugada_IA
        if 2 in self.mis_jugadas and 8 in self.mis_jugadas:
            if 5 in self.jugadas_disponibles:
                seleccion_jugada_IA = 5
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = self.dificil()
                return seleccion_jugada_IA
        if 3 in self.mis_jugadas and 6 in self.mis_jugadas:
            if 9 in self.jugadas_disponibles:
                seleccion_jugada_IA = 9
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = self.dificil()
                return seleccion_jugada_IA
        if 3 in self.mis_jugadas and 9 in self.mis_jugadas:
            if 6 in self.jugadas_disponibles:
                seleccion_jugada_IA = 6
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = self.dificil()
                return seleccion_jugada_IA
        if 3 in self.mis_jugadas and 5 in self.mis_jugadas:
            if 7 in self.jugadas_disponibles:
                seleccion_jugada_IA = 7
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = self.dificil()
                return seleccion_jugada_IA
        if 3 in self.mis_jugadas and 7 in self.mis_jugadas:
            if 5 in self.jugadas_disponibles:
                seleccion_jugada_IA = 5
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = self.dificil()
                return seleccion_jugada_IA
        if 4 in self.mis_jugadas and 7 in self.mis_jugadas:
            if 1 in self.jugadas_disponibles:
                seleccion_jugada_IA = 1
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = self.dificil()
                return seleccion_jugada_IA
        if 4 in self.mis_jugadas and 5 in self.mis_jugadas:
            if 6 in self.jugadas_disponibles:
                seleccion_jugada_IA = 6
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = self.dificil()
                return seleccion_jugada_IA
        if 4 in self.mis_jugadas and 6 in self.mis_jugadas:
            if 5 in self.jugadas_disponibles:
                seleccion_jugada_IA = 5
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = self.dificil()
                return seleccion_jugada_IA
        if 5 in self.mis_jugadas and 6 in self.mis_jugadas:
            if 4 in self.jugadas_disponibles:
                seleccion_jugada_IA = 4
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = self.dificil()
                return seleccion_jugada_IA
        if 5 in self.mis_jugadas and 7 in self.mis_jugadas:
            if 3 in self.jugadas_disponibles:
                seleccion_jugada_IA = 3
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = self.dificil()
                return seleccion_jugada_IA
        if 5 in self.mis_jugadas and 8 in self.mis_jugadas:
            if 2 in self.jugadas_disponibles:
                seleccion_jugada_IA = 2
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = self.dificil()
                return seleccion_jugada_IA
        if 5 in self.mis_jugadas and 9 in self.mis_jugadas:
            if 1 in self.jugadas_disponibles:
                seleccion_jugada_IA = 1
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = self.dificil()
                return seleccion_jugada_IA
        if 6 in self.mis_jugadas and 9 in self.mis_jugadas:
            if 3 in self.jugadas_disponibles:
                seleccion_jugada_IA = 3
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = self.dificil()
                return seleccion_jugada_IA
        if 7 in self.mis_jugadas and 8 in self.mis_jugadas:
            if 9 in self.jugadas_disponibles:
                seleccion_jugada_IA = 9
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = self.dificil()
                return seleccion_jugada_IA
        if 7 in self.mis_jugadas and 9 in self.mis_jugadas:
            if 8 in self.jugadas_disponibles:
                seleccion_jugada_IA = 8
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = self.dificil()
                return seleccion_jugada_IA
        if 8 in self.mis_jugadas and 9 in self.mis_jugadas:
            if 7 in self.jugadas_disponibles:
                seleccion_jugada_IA = 7
                return seleccion_jugada_IA
            else:
                seleccion_jugada_IA = self.dificil()
                return seleccion_jugada_IA
        if 5 in self.jugadas_disponibles:
            seleccion_jugada_IA = 5
        elif len(self.jugadas_disponibles) == 8:
            seleccion_jugada_IA = random.choice(esquinas)
        else:
            seleccion_jugada_IA = self.dificil()
        return seleccion_jugada_IA
