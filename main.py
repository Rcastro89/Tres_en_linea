#!/usr/bin/python3
import os
import numpy
import turne as turne
import windows as window


ventanita = window.my_window_game()
ventanita.canvas_main()



"""selection = " "
error = 0
turno = "X"
chances = 0
os.system("clear")
while ord(selection) != 113 and ord(selection) != 81:
    if error == 0:
        turne.print_table()
    if turno == "X":
        selection = (input("Marca el numero de la "
                           "posicion que deseas jugar o 'q' para salir "))
        large = len(selection)
        print(selection)
    else:
        selection = numpy.random.choice(turne.positions)
        chances = 0
        while selection == "X" or selection == "O":
            selection = numpy.random.choice(turne.positions)
            chances += 1
            if chances > 9:
                break
    if chances >= 9:
        print("No hay mas jugadas posibles")
        exit(1)
    else:
        if large == 1:
            if ((ord(selection) < 49 or ord(selection) > 57)
                    and ord(selection) != 113 and ord(selection) != 81):
                error = 1
                print(("SELECCION INCORRECTA! debe ingresar "
                       "un numero del 1 al 9 o 'q' para salir"))
            else:
                error = 0
                os.system("clear")
                if (selection == "1" and turne.positions[0] != "X"
                        and turne.positions[0] != "O"):
                    turne.positions[0] = turne
                    turne.p_print[0] = turne
                    turno = turne.selec_turne(turne)
                elif (selection == "2" and turne.positions[1] != "X"
                        and turne.positions[1] != "O"):
                    turne.positions[1] = turne
                    turne.p_print[1] = turne
                    turno = turne.selec_turne(turne)
                elif (selection == "3" and turne.positions[2] != "X"
                        and turne.positions[2] != "O"):
                    turne.positions[2] = turne
                    turne.p_print[2] = turne
                    turno = turne.selec_turne(turne)
                elif (selection == "4" and turne.positions[3] != "X"
                        and turne.positions[3] != "O"):
                    turne.positions[3] = turne
                    turne.p_print[3] = turne
                    turno = turne.selec_turne(turne)
                elif (selection == "5" and turne.positions[4] != "X"
                        and turne.positions[4] != "O"):
                    turne.positions[4] = turne
                    turne.p_print[4] = turne
                    turno = turne.selec_turne(turne)
                elif (selection == "6" and turne.positions[5] != "X"
                        and turne.positions[5] != "O"):
                    turne.positions[5] = turne
                    turne.p_print[5] = turne
                    turno = turne.selec_turne(turne)
                elif (selection == "7" and turne.positions[6] != "X"
                        and turne.positions[6] != "O"):
                    turne.positions[6] = turne
                    turne.p_print[6] = turne
                    turno = turne.selec_turne(turne)
                elif (selection == "8" and turne.positions[7] != "X"
                        and turne.positions[7] != "O"):
                    turne.positions[7] = turne
                    turne.p_print[7] = turne
                    turno = turne.selec_turne(turne)
                elif (selection == "9" and turne.positions[8] != "X"
                        and turne.positions[8] != "O"):
                    turne.positions[8] = turne
                    turne.p_print[8] = turne
                    turno = turne.selec_turne(turne)
                elif selection != "q" and selection != "Q":
                    print("Juagada no permitida\n")
        else:
            error = 1
            selection = " "
            print(("SELECCION INCORRECTA! debe ingresar"
                   "un numero del 1 al 9 o 'q' para salir"))"""
