import subprocess


class Reporte():


    def __init__(self, nombre):
        self.nombre = nombre + ".tex"
        self.archivo = open(nombre + ".tex", "w")


    def crearPreambulo(self):
        self.archivo.write("\\documentclass[12pt]{book} \n")


    def iniciarReporte(self):
        self.archivo.write("\\begin{document} \n")

    def terminarReporte(self):
        self.archivo.write("\\end{document} \n")
        self.archivo.close()

    def iniciar_tabla(self, noColumns, separador = True):
        self.numeroCol = noColumns
        self.archivo.write("\\begin{tabular}{"  +  "|c|" * noColumns +   "} \n ")


    def terminar_tabla(self):
        self.archivo.write("\\end{tabular} \n")

    def escribir_fila(self, *args):
        if len(args) != self.numeroCol:
            print("Tienes un número incorrecto de columnas")
        else:
            for i in range(0,len(args)):
                if( i == len(args) - 1 ):
                    self.archivo.write(args[i] + "\\\\ \n")
                else:
                    self.archivo.write(args[i] + "& ")

    def compilarReporte(self):
        subprocess.run(["pdflatex" , self.nombre])
        subprocess.run(["okular", "ejemplo.pdf"])
      