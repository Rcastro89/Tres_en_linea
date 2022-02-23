#!/usr/bin/python3


from tkinter import *
from turne import validar_ganador
from tkinter import ttk
import time

turno = __import__('turne').selec_turne
jugada = __import__('turne').jugada


class my_window_game():

    x_v = 500
    y_v = 300
    turno_actual = turno("O")
    cant_jug = 0
    jugador_x = ""
    jugador_o = ""
    dificultad = ""
    ganador = False
    puntos = {'Empate': 0}

    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry()
        self.raiz.title("Triky 2022")
        x = ((self.raiz.winfo_screenwidth() // 2) - (self.x_v // 2))
        y = ((self.raiz.winfo_screenheight() // 2) - (self.y_v // 2))
        self.raiz.geometry(str(self.x_v) + "x" +
                           str(self.y_v) + "+" + str(x) + "+" + str(y))
        self.raiz.update()

    def but_1(self):
        if self.btn_usado[1] == False and self.ganador == False:
            self.btn_usado[1] = self.turno_actual
            self.button_1['text'] = self.turno_actual
            jugada(1, self.turno_actual)
            self.validaciones()

    def but_2(self):
        if self.btn_usado[2] == False and self.ganador == False:
            self.btn_usado[2] = self.turno_actual
            self.button_2['text'] = self.turno_actual
            jugada(2, self.turno_actual)
            self.validaciones()

    def but_3(self):
        if self.btn_usado[3] == False and self.ganador == False:
            self.btn_usado[3] = self.turno_actual
            self.button_3['text'] = self.turno_actual
            jugada(3, self.turno_actual)
            self.validaciones()

    def but_4(self):
        if self.btn_usado[4] == False and self.ganador == False:
            self.btn_usado[4] = self.turno_actual
            self.button_4['text'] = self.turno_actual
            jugada(4, self.turno_actual)
            self.validaciones()

    def but_5(self):
        if self.btn_usado[5] == False and self.ganador == False:
            self.btn_usado[5] = self.turno_actual
            self.button_5['text'] = self.turno_actual
            jugada(5, self.turno_actual)
            self.validaciones()

    def but_6(self):
        if self.btn_usado[6] == False and self.ganador == False:
            self.btn_usado[6] = self.turno_actual
            self.button_6['text'] = self.turno_actual
            jugada(6, self.turno_actual)
            self.validaciones()

    def but_7(self):
        if self.btn_usado[7] == False and self.ganador == False:
            self.btn_usado[7] = self.turno_actual
            self.button_7['text'] = self.turno_actual
            jugada(7, self.turno_actual)
            self.validaciones()

    def but_8(self):
        if self.btn_usado[8] == False and self.ganador == False:
            self.btn_usado[8] = self.turno_actual
            self.button_8['text'] = self.turno_actual
            jugada(8, self.turno_actual)
            self.validaciones()

    def but_9(self):
        if self.btn_usado[9] == False and self.ganador == False:
            self.btn_usado[9] = self.turno_actual
            self.button_9['text'] = self.turno_actual
            jugada(9, self.turno_actual)
            self.validaciones()

    def canvas_game(self):
        self.ganador = False
        self.canvas.pack(expand=YES, fill=BOTH)
        self.canvas.create_line(self.x_v // 3, self.y_v //
                                6, self.x_v // 3, self.y_v // 1.10, width=5)
        self.canvas.create_line(self.x_v // 1.5, self.y_v // 6,
                                self.x_v // 1.5, self.y_v // 1.10, width=5)
        self.canvas.create_line(self.x_v // 10, self.y_v // 2.5,
                                self.x_v // 1.11, self.y_v // 2.5, width=5)
        self.canvas.create_line(self.x_v // 10, self.y_v // 1.50,
                                self.x_v // 1.11, self.y_v // 1.50, width=5)
        self.widget_5 = Label(self.canvas, text='TRIKY 2022',
                              fg='black', bg='white')
        self.widget_5.pack()
        self.widget_5.place(x=(self.x_v // 2 - 80), y=8)
        self.widget_5.config(font=('Arial', 20))
        self.button_1 = Button(self.canvas, text="",
                               width=3, height=2, bd="5", command=self.but_1)
        self.button_1.place(x=self.x_v // 7.14, y=self.y_v // 6)
        self.button_2 = Button(self.canvas, text="",
                               width=3, height=2, bd="5", command=self.but_2)
        self.button_2.place(x=self.x_v // 2.32, y=self.y_v // 6)
        self.button_3 = Button(self.canvas, text="",
                               width=3, height=2, bd="5", command=self.but_3)
        self.button_3.place(x=self.x_v // 1.38, y=self.y_v // 6)
        self.button_4 = Button(self.canvas, text="",
                               width=3, height=2, bd="5", command=self.but_4)
        self.button_4.place(x=self.x_v // 7.14, y=self.y_v // 2.3)
        self.button_5 = Button(self.canvas, text="",
                               width=3, height=2, bd="5", command=self.but_5)
        self.button_5.place(x=self.x_v // 2.32, y=self.y_v // 2.3)
        self.button_6 = Button(self.canvas, text="",
                               width=3, height=2, bd="5", command=self.but_6)
        self.button_6.place(x=self.x_v // 1.38, y=self.y_v // 2.3)
        self.button_7 = Button(self.canvas, text="",
                               width=3, height=2, bd="5", command=self.but_7)
        self.button_7.place(x=self.x_v // 7.14, y=self.y_v // 1.42)
        self.button_8 = Button(self.canvas, text="",
                               width=3, height=2, bd="5", command=self.but_8)
        self.button_8.place(x=self.x_v // 2.32, y=self.y_v // 1.42)
        self.button_9 = Button(self.canvas, text="",
                               width=3, height=2, bd="5", command=self.but_9)
        self.button_9.place(x=self.x_v // 1.38, y=self.y_v // 1.42)
        self.btn_usado = {1: False, 2: False, 3: False, 4: False, 5: False,
                          6: False, 7: False, 8: False, 9: False}
        self.etiqueta_turno()
        if self.cant_jug == 0:
            if self.turno_actual == "O":
                self.myIA(self.btn_usado, self.dificultad)
        self.raiz.mainloop()

    def canvas_main(self):
        self.canvas = Canvas(self.raiz, width=self.x_v,
                             height=self.y_v, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)
        self.widget_1 = Label(self.canvas, text='TRIKY 2022',
                              fg='black', bg='white')
        self.widget_1.pack()
        self.widget_1.place(x=(self.x_v // 2 - 80), y=self.y_v // 37.5)
        self.widget_1.config(font=('Arial', 20))
        self.widget_2 = Label(self.canvas, text='Selecciona:',
                              fg='black', bg='white')
        self.widget_2.pack()
        self.widget_2.place(x=self.x_v // 15, y=self.y_v // 6)
        self.widget_3 = Label(self.canvas, text='Nombre del Jugador X:',
                              fg='black', bg='white')
        self.widget_3.pack()
        self.widget_3.place(x=self.x_v // 1.8, y=self.y_v // 6)
        self.caja_texto_1 = Entry(self.canvas, width=15)
        self.caja_texto_1.place(x=self.x_v // 1.75, y=self.y_v // 4)
        self.widget_4 = Label(self.canvas, text='Nombre del Jugador O:',
                              fg='black', bg='white')
        self.widget_4.pack()
        self.widget_4.place(x=self.x_v // 1.8, y=self.y_v // 3)
        self.caja_texto_2 = Entry(self.canvas, width=15)
        self.caja_texto_2.place(x=self.x_v // 1.75, y=self.y_v // 2.4)
        self.caja_texto_2.config(state=DISABLED)
        self.button_10 = Button(
            self.canvas,
            text="Empezar", bd="5", command=self.siguiente_ventana)
        self.button_10.place(x=(self.x_v // 2) - 50, y=self.y_v // 1.8)
        self.v = IntVar()
        self.radio_but_1 = Radiobutton(self.canvas, text='1 Jugador',
                                       value=0,
                                       bg='white',
                                       command=self.seleccion_jugadores,
                                       variable=self.v)
        self.radio_but_1.pack(anchor=W)
        self.radio_but_1.place(x=self.x_v // 2 - 130,
                               y=(self.y_v // 7.5))
        self.radio_but_2 = Radiobutton(self.canvas, text='2 Jugadores',
                                       value=1,
                                       bg='white',
                                       command=self.seleccion_jugadores,
                                       variable=self.v)
        self.radio_but_2.pack(anchor=W)
        self.radio_but_2.place(x=self.x_v // 2 - 130,
                               y=(self.y_v // 7.5) + 22)
        self.widget_7 = Label(self.canvas, text='Dificultad:',
                              fg='black', bg='white')
        self.widget_7.pack()
        self.widget_7.place(x=self.x_v // 15, y=self.y_v // 3)
        self.combobox_1 = ttk.Combobox(self.canvas,
                                       values=[
                                           "Facil",
                                           "Intermedio",
                                           "Dificil",
                                           "Legendario"], state='readonly')
        self.combobox_1.place(x=self.x_v // 7, y=self.y_v // 2.40)
        self.combobox_1.current(0)
        self.raiz.mainloop()

    def seleccion_jugadores(self):
        for i in range(2):
            if (self.v.get() == i):
                if i == 0:
                    self.caja_texto_2.delete("0", "end")
                    self.caja_texto_2.config(state=DISABLED)
                    self.cant_jug = 0
                elif i == 1:
                    self.caja_texto_2.config(state=NORMAL)
                    self.cant_jug = 1

    def siguiente_ventana(self):
        self.dificultad = self.combobox_1.get()
        self.jugador_x = self.caja_texto_1.get()
        if self.cant_jug == 1:
            self.jugador_o = self.caja_texto_2.get()
        else:
            self.jugador_o = "PC Dificultad: " + self.dificultad
        self.puntos[self.jugador_x] = 0
        self.puntos[self.jugador_o] = 0
        self.widget_1.destroy()
        self.widget_2.destroy()
        self.widget_3.destroy()
        self.widget_4.destroy()
        self.widget_7.destroy()
        self.caja_texto_1.destroy()
        self.caja_texto_2.destroy()
        self.radio_but_1.destroy()
        self.radio_but_2.destroy()
        self.button_10.destroy()
        self.combobox_1.destroy()
        self.canvas_game()

    def etiqueta_turno(self):
        texto = ""
        self.widget_6 = Label(self.canvas, text=texto,
                              fg='black', bg='white')
        self.widget_6.pack()
        if self.turno_actual == 'X':
            texto = 'Jugador X: ' + self.jugador_x
            self.widget_6['text'] = ""
            self.widget_6['text'] = texto
            self.widget_6.place(x=20, y=20)

        else:
            texto = 'Jugador O: ' + self.jugador_o
            self.widget_6['text'] = ""
            self.widget_6['text'] = texto
            self.widget_6.place(x=350, y=20)

    def victoria(self):
        hay_ganador = False
        if self.validar == 'X':
            puntos_actuales = self.puntos[self.jugador_x] + 1
            self.puntos.update({self.jugador_x: puntos_actuales})
            hay_ganador = True
        elif self.validar == 'O':
            puntos_actuales = self.puntos[self.jugador_o] + 1
            self.puntos.update({self.jugador_o: puntos_actuales})
            hay_ganador = True
        elif self.validar == 'E':
            puntos_actuales = self.puntos['Empate'] + 1
            self.puntos.update({'Empate': puntos_actuales})
            hay_ganador = True
        if hay_ganador:
            print(self.puntos)
            self.button_10 = Button(self.canvas, text="Y", font=10,
                               width=3, height=2, bd="5", command=self.otra_partida)
            self.button_10.place(x=5, y=self.y_v - 70)
            self.button_11 = Button(self.canvas, text="N", font=10,
                               width=3, height=2, bd="5", command=self.fin)
            self.button_11.place(x=420, y=self.y_v - 70)
            self.ganador = True
            
    def otra_partida(self):
        self.widget_6.destroy()
        self.button_10.destroy()
        self.button_11.destroy()
        self.canvas.delete('all')
        for i in range(1, 10):
            jugada(i, 'E')
        self.canvas_game()
    
    def fin(self):
        self.turno_actual = turno("O")
        self.cant_jug = 0
        self.jugador_x = ""
        self.jugador_o = ""
        self.dificultad = ""
        self.ganador = False
        self.puntos = {'Empate': 0}
        self.widget_6.destroy()
        self.button_10.destroy()
        self.button_11.destroy()
        self.canvas.destroy()
        for i in range(1, 10):
            jugada(i, 'E')
        self.canvas_main()

    def validaciones(self):
        self.widget_6.destroy()
        self.turno_actual = turno(self.turno_actual)
        self.etiqueta_turno()
        self.validar = validar_ganador()
        self.victoria()
        if self.cant_jug == 0 and self.ganador == False:
            if self.turno_actual == "O":
                self.myIA(self.btn_usado, self.dificultad)

    def myIA(self, dic, dif):
        from IA import Jug_IA
        x = Jug_IA(dic, dif)
        seleccion_jugada_IA = x.jugadaIA()
        if seleccion_jugada_IA == 1:
            self.but_1()
        elif seleccion_jugada_IA == 2:
            self.but_2()
        elif seleccion_jugada_IA == 3:
            self.but_3()
        elif seleccion_jugada_IA == 4:
            self.but_4()
        elif seleccion_jugada_IA == 5:
            self.but_5()
        elif seleccion_jugada_IA == 6:
            self.but_6()
        elif seleccion_jugada_IA == 7:
            self.but_7()
        elif seleccion_jugada_IA == 8:
            self.but_8()
        elif seleccion_jugada_IA == 9:
            self.but_9()
