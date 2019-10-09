from tkinter import *
import tkinter as tk

def main():

    marco = tk.Tk()
    marco.title("Diagrama de Clases")
    marco.geometry("500x300")
    marco.title("´UML´")
    marco.configure(bg="black")

#   Métodos
    class AnadirClase():
        __fila,__columna = 3,0
        clases=[]

        def crearClase(self):

            self.__columna = self.__columna + 1
            print(str(self.__columna))

            self.__fila = self.__fila + 1
            print(str(self.__fila))
            self.__atri = []

            auxNN=StringVar()

            self.__nombre = Entry(marco, textvariable = auxNN, bg="black" , fg="white").grid(padx=5, pady=5, row=1,column=0)

            self.__atributos = Text(marco, width = 20, height=10, bg="black" , fg="white").grid(row=2,column=0)
            #matrizatr = [range(self.__columna) for i in range()]

            self.__metodos = Text(marco, width = 20, height=10, bg="black" , fg="white").grid(row=2,column=1)
            #matrizmet = [range(self.__columna) for i in range()]

        #def guardarDatos(self):
            def guardarDatos():
                most =auxNN.get()

                print(most)
                mest = self.__atributos[self.__fila].get('1.0', END)

                print(mest)


            self.__btnEnviar = Button(marco, text = "Enviar Clase", bg="black", fg="white", command=guardarDatos).grid( row=2,
                                                                                                  column=2,
                                                                                                  padx=5)

    btnCrear = Button(marco, text = "Crear Nueva Clase", bg="black", fg="white", command = AnadirClase().crearClase)
    btnCrear.grid(row=0,column=0)

    marco.mainloop()

main()
