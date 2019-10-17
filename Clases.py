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
            #print(str(self.__columna))

            self.__fila = self.__fila + 1
            #print(str(self.__fila))
            self.__atri = []

            auxNN=StringVar()

            self.__nombre = Entry(marco, textvariable = auxNN, bg="black" , fg="white").grid(padx=5, pady=5, row=1,column=0)

            self.__atributos = Text(marco, width = 20, height=10, bg="black" , fg="white")
            self.__atributos.grid(row=2,column=0)

            self.__metodos = Text(marco, width = 20, height=10, bg="black" , fg="white")
            self.__metodos.grid(row=2,column=1)

            def crear():
                ventana = Tk()
                lienzo = Canvas(ventana,
                width=300, height=300,bg="#9AE5D3")
                ventana.title("Clase")
                lienzo.grid(row=0,column=100)
                lienzo.create_rectangle(
                5,5,295,295, fill="#2D6457", outline="RED",width=1)
                lienzo.create_line(5, 50, 295, 50, width=1, fill='RED')
                lienzo.create_line(5, 180, 295, 180, width=1, fill='RED')

                most =auxNN.get()
                lienzo.create_text(50,30, text=str(most))

                x=self.__atributos.get(1.0, END)
                r = re.split("/n", x)
                for i in r:
                    print(i)
                lienzo.create_text(50,70, text=str(x))

                ventana.mainloop()
            #crear()

            boton = tk.Button(marco, text="Mostrar clase", bg="black", fg="white", command=crear)
            boton.grid(row=3, column=2, padx=5)
            #boton.pack()

            def guardarDatos():

                
                #print(most)



                a=self.__metodos.get(1.0, END)
                b = re.split("/n", a)
                for i in b:
                    print(i)

            self.__btnEnviar = Button(marco, text = "Enviar Clase", bg="black", fg="white", command=guardarDatos).grid( row=2,
                                                                                                  column=2,
                                                                                                  padx=5)

    btnCrear = Button(marco, text = "Crear Nueva Clase", bg="black", fg="white", command = AnadirClase().crearClase)
    btnCrear.grid(row=0,column=0)

    marco.mainloop()

main()
