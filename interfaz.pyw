import sys
from archivocopia import *
from clasedisco import *
from claseposte import *
from PyQt5.QtWidgets import QMessageBox
from Resultados import *
#instanciando las clases poste, disco y Reporte
disco1 = disco(diametro = 1)
disco2 = disco(diametro = 2)
disco3 = disco(diametro = 3)
disco4 = disco(diametro = 4)
disco5 = disco(diametro = 5)
disco6 = disco(diametro = 6)
disco7 = disco(diametro = 7)
disco8 = disco(diametro = 8)
poste1 = poste()
poste2 = poste()
poste3 = poste()
Resultadospdf = Reporte("resultadospdf")
n = -1
n_disco = 0
class formulario(QtWidgets.QWidget):


    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.poste1 = poste1
        self.poste2 = poste2
        self.poste3 = poste3
        self.inicio()
        self.ui.combo.activated.connect(self.postes_disponibles)
        self.ui.mover.clicked.connect(self.contar_movimientos)
        self.ui.mover.clicked.connect(self.desplazar)    
        self.ui.combo2.activated.connect(self.desbloquear)
        self.Resultadospdf = Resultadospdf

    def inicio(self):
        self.poste1.recibir([self.ui.Disco8, disco8])
        self.poste1.recibir([self.ui.Disco7, disco7])
        self.poste1.recibir([self.ui.Disco6, disco6])
        self.poste1.recibir([self.ui.Disco5, disco5]) 
        self.poste1.recibir([self.ui.Disco4, disco4])
        self.poste1.recibir([self.ui.Disco3, disco3])
        self.poste1.recibir([self.ui.Disco2, disco2])
        self.poste1.recibir([self.ui.Disco1, disco1])
        self.ui.combo.view().setRowHidden(1, True)
        self.ui.combo.view().setRowHidden(2, True)
        self.ui.combo2.view().setRowHidden(0, True)
        self.ui.combo2.setEnabled(False)
        self.ui.mover.setEnabled(False)

    def postes_disponibles(self):            

        self.ui.combo2.setEnabled(True)

        if self.ui.combo.currentText() == "Poste 1":
            if self.poste2.condicion_poste() == True:
                self.ui.combo2.view().setRowHidden(1, False)
                self.ui.combo.view().setRowHidden(1, True)
            else:
                if self.poste1.condicion_poste() == True:
                    self.ui.combo2.view().setRowHidden(0, False)
                    self.ui.combo.view().setRowHidden(0, True)
                    self.ui.combo.view().setRowHidden(1, False) 
                    self.ui.combo.view().setRowHidden(2, False)
                else:
                    if self.poste1.e_superior()[1].con_diametro() < self.poste2.e_superior()[1].con_diametro():
                        self.ui.combo2.view().setRowHidden(1, False)
                        self.poste1.e_superior()[0].setStyleSheet("background-color: yellow")
                        self.poste2.e_superior()[0].setStyleSheet("background-color: orange")
                    else:
                        self.ui.combo2.view().setRowHidden(1, True)
                        self.ui.combo.view().setRowHidden(1, False)
                        self.poste1.e_superior()[0].setStyleSheet("background-color: yellow")
                        self.poste2.e_superior()[0].setStyleSheet("background-color: orange")

            if self.poste3.condicion_poste() == True:
                self.ui.combo2.view().setRowHidden(2, False)
                self.ui.combo.view().setRowHidden(2, True)
            else: 
                if self.poste1.condicion_poste() == True:   
                    self.ui.combo2.view().setRowHidden(0, False)
                    self.ui.combo.view().setRowHidden(0, True)
                    self.ui.combo.view().setRowHidden(1, False) 
                    self.ui.combo.view().setRowHidden(2, False)
                else:
                    if self.poste1.e_superior()[1].con_diametro() < self.poste3.e_superior()[1].con_diametro():
                        self.ui.combo2.view().setRowHidden(2, False)   
                        self.poste1.e_superior()[0].setStyleSheet("background-color: yellow")
                        self.poste3.e_superior()[0].setStyleSheet("background-color: orange")
                    else:
                        self.ui.combo2.view().setRowHidden(2, True)
                        self.ui.combo.view().setRowHidden(2, False)
                        self.poste1.e_superior()[0].setStyleSheet("background-color: yellow")
                        self.poste3.e_superior()[0].setStyleSheet("background-color: orange")
            
            if self.poste1.condicion_poste() == False and self.poste2.condicion_poste() == False and self.poste3.condicion_poste() == False:
                if self.poste1.e_superior()[1].con_diametro() > self.poste2.e_superior()[1].con_diametro() and self.poste1.e_superior()[1].con_diametro() > self.poste3.e_superior()[1].con_diametro():
                    self.poste1.e_superior()[0].setStyleSheet("background-color: orange")
                    self.ui.combo.view().setRowHidden(0, True)

        if self.ui.combo.currentText() == "Poste 2":
            
            if poste1.condicion_poste() == True:
                self.ui.combo2.view().setRowHidden(0, False)
                self.ui.combo.view().setRowHidden(0, True)
            else:
                if self.poste2.condicion_poste() == True:   
                    self.ui.combo2.view().setRowHidden(1, False)                    
                    self.ui.combo.view().setRowHidden(1, True)
                    self.ui.combo.view().setRowHidden(0, False) 
                    self.ui.combo.view().setRowHidden(2, False)
                else:
                    self.poste1.e_superior()[0].setStyleSheet("background-color: orange")
                    self.poste2.e_superior()[0].setStyleSheet("background-color: yellow")
                    if self.poste2.e_superior()[1].con_diametro() < self.poste1.e_superior()[1].con_diametro():
                        self.ui.combo2.view().setRowHidden(0, False)                    
                    else:
                        self.ui.combo2.view().setRowHidden(0, True)
                        self.ui.combo.view().setRowHidden(0, False)
            
            if poste3.condicion_poste() == True:
                self.ui.combo2.view().setRowHidden(2, False)
                self.ui.combo.view().setRowHidden(2, True)
            else:
                if self.poste2.condicion_poste() == True:   
                    self.ui.combo2.view().setRowHidden(1, False)
                    self.ui.combo.view().setRowHidden(1, True)
                    self.ui.combo.view().setRowHidden(0, False) 
                    self.ui.combo.view().setRowHidden(2, False)
                else:
                    self.poste1.e_superior()[0].setStyleSheet("background-color: orange")
                    self.poste2.e_superior()[0].setStyleSheet("background-color: yellow")
                    if self.poste2.e_superior()[1].con_diametro() < self.poste3.e_superior()[1].con_diametro():
                        self.ui.combo2.view().setRowHidden(2, False)                        
                    else: 
                        self.ui.combo2.view().setRowHidden(2, True)
                        self.ui.combo.view().setRowHidden(2, False)
                
            if self.poste1.condicion_poste() == False and self.poste2.condicion_poste() == False and self.poste3.condicion_poste() == False:
                if self.poste2.e_superior()[1].con_diametro() > self.poste1.e_superior()[1].con_diametro() and self.poste2.e_superior()[1].con_diametro() > self.poste3.e_superior()[1].con_diametro():
                    self.poste2.e_superior()[0].setStyleSheet("background-color: orange")
                    self.ui.combo.view().setRowHidden(1, True)

        if self.ui.combo.currentText() == "Poste 3":
            
            if poste1.condicion_poste == True:
                self.ui.combo2.view().setRowHidden(0, False)
                self.ui.combo.view().setRowHidden(0, True)
            else:
                if self.poste3.condicion_poste() == True:   
                    self.ui.combo2.view().setRowHidden(2, False)
                    self.ui.combo.view().setRowHidden(2, True)
                    self.ui.combo.view().setRowHidden(0, False) 
                    self.ui.combo.view().setRowHidden(1, False)
                else:
                    self.poste3.e_superior()[0].setStyleSheet("background-color: yellow")
                    self.poste1.e_superior()[0].setStyleSheet("background-color: orange")
                    if self.poste3.e_superior()[1].con_diametro() < self.poste1.e_superior()[1].con_diametro():
                        self.ui.combo2.view().setRowHidden(0, False)                        
                    else:
                        self.ui.combo2.view().setRowHidden(0, True)
                        self.ui.combo.view().setRowHidden(0, False)


            if poste2.condicion_poste() == True:
                self.ui.combo2.view().setRowHidden(1, False)
                self.ui.combo.view().setRowHidden(1, True)
            else:
                if self.poste3.condicion_poste() == True:   
                    self.ui.combo2.view().setRowHidden(2, False)
                    self.ui.combo.view().setRowHidden(2, True)
                    self.ui.combo.view().setRowHidden(0, False) 
                    self.ui.combo.view().setRowHidden(1, False)
                else:
                    self.poste2.e_superior()[0].setStyleSheet("background-color: orange")
                    self.poste3.e_superior()[0].setStyleSheet("background-color: yellow")
                    if self.poste3.e_superior()[1].con_diametro() < self.poste2.e_superior()[1].con_diametro():
                        self.ui.combo2.view().setRowHidden(1, False)                        
                    else:
                        self.ui.combo2.view().setRowHidden(1, True)
                        self.ui.combo.view().setRowHidden(1, False)
            
            if self.poste1.condicion_poste() == False and self.poste2.condicion_poste() == False and self.poste3.condicion_poste() == False:
                if self.poste3.e_superior()[1].con_diametro() > self.poste1.e_superior()[1].con_diametro() and self.poste3.e_superior()[1].con_diametro() > self.poste2.e_superior()[1].con_diametro():
                    self.poste3.e_superior()[0].setStyleSheet("background-color: orange")
                    self.ui.combo.view().setRowHidden(2, True)
          

    def desplazar(self):
        
        if self.ui.combo.currentText() == self.ui.combo2.currentText():
            QMessageBox.about(self, "Movimiento Identidad", "El disco seleccionado se ha quedado en la misma posición")
        if self.ui.combo.currentText() == "Poste 1" and self.ui.combo2.currentText() == "Poste 2":
            self.poste1.e_superior()[0].move(360 + 23 - (self.poste1.e_superior()[0].size().width())/2 ,270 - 20*(int(self.poste2.longitud()) + 1))

            self.poste2.recibir(self.poste1.e_superior())
            self.poste1.entregar()            
            self.poste2.e_superior()[0].setStyleSheet("background-color: orange")

        if self.ui.combo.currentText() == "Poste 1" and self.ui.combo2.currentText() == "Poste 3":
            self.poste1.e_superior()[0].move(610 + 23 - (self.poste1.e_superior()[0].size().width())/2 ,270 - 20*(int(self.poste3.longitud()) + 1))                    

            self.poste3.recibir(self.poste1.e_superior())
            self.poste1.entregar()            
            self.poste3.e_superior()[0].setStyleSheet("background-color: orange")

        if self.ui.combo.currentText() == "Poste 2" and self.ui.combo2.currentText() == "Poste 1":
            self.poste2.e_superior()[0].move(110 + 23 - (self.poste2.e_superior()[0].size().width())/2 ,270 - 20*(int(self.poste1.longitud()) + 1))                    

            self.poste1.recibir(self.poste2.e_superior())
            self.poste2.entregar()    
            self.poste1.e_superior()[0].setStyleSheet("background-color: orange")    

        if self.ui.combo.currentText() == "Poste 2" and self.ui.combo2.currentText() == "Poste 3":

            self.poste2.e_superior()[0].move(610 + 23 - (self.poste2.e_superior()[0].size().width())/2 ,270 - 20*(int(self.poste3.longitud()) + 1))                    
    
            self.poste3.recibir(self.poste2.e_superior())
            self.poste2.entregar()   
            self.poste3.e_superior()[0].setStyleSheet("background-color: orange")         

        if self.ui.combo.currentText() == "Poste 3" and self.ui.combo2.currentText() == "Poste 1":
            self.poste3.e_superior()[0].move(110 + 23 - (self.poste3.e_superior()[0].size().width())/2 ,270 - 20*(int(self.poste1.longitud()) + 1))                    

            self.poste1.recibir(self.poste3.e_superior())
            self.poste3.entregar()
            self.poste1.e_superior()[0].setStyleSheet("background-color: orange")

        if self.ui.combo.currentText() == "Poste 3" and self.ui.combo2.currentText() == "Poste 2":
            self.poste3.e_superior()[0].move(360 + 23 - (self.poste3.e_superior()[0].size().width())/2 ,270 - 20*(int(self.poste2.longitud()) + 1))                    

            self.poste2.recibir(self.poste3.e_superior())  
            self.poste3.entregar()      
            self.poste2.e_superior()[0].setStyleSheet("background-color: orange")

        if self.poste1.longitud() == 8 or self.poste3.longitud() == 8:
            QMessageBox.about(self, "Juego Finalizado", "Felicidades has reordenado todos los discos en otro poste")
            self.close()

        self.postes_disponibles()    
        self.ui.mover.setEnabled(False)
        self.ui.combo2.setEnabled(False)
       
    def desbloquear(self):
        self.ui.mover.setEnabled(True)
    
    def showEvent(self, event):
        self.contar_movimientos()

    def contar_movimientos(self):
        global n
        n += 1  
        self.ui.label7.setText("Número de movimientos: " + str(n))
        return n
    
    def closeEvent(self, event):
        #n_jugadas
        global n_disco
        np_seleccionado = self.ui.combo.currentText()[-1]
        np_llegada = self.ui.combo2.currentText()[-1]
        if self.ui.combo2.currentText() == "Poste 1" and self.poste1.condicion_poste() == False:
            n_disco = self.poste1.e_superior()[1].con_diametro()
        else:
            n_disco = "El disco del poste seleccionado no fue desplazado al poste de llegada."
        if self.ui.combo2.currentText() == "Poste 2" and self.poste2.condicion_poste() == False:
            n_disco = self.poste2.e_superior()[1].con_diametro()
        else:
            n_disco = "El disco del poste seleccionado no fue desplazado al poste de llegada."
        if self.ui.combo2.currentText() == "Poste 3" and self.poste3.condicion_poste() == False:
            n_disco = self.poste3.e_superior()[1].con_diametro()
        else:
            n_disco = "El disco del poste seleccionado no fue desplazado al poste de llegada."

        self.Resultadospdf.crearPreambulo()
        self.Resultadospdf.iniciarReporte()
        self.Resultadospdf.iniciar_tabla(4)
        self.Resultadospdf.escribir_fila("Número de Jugadas", "Poste seleccionado", "Número de Disco", "Poste de llegada")
        self.Resultadospdf.escribir_fila("No pude contar las paratidas", str(np_seleccionado), str(n_disco), str(np_llegada))
        self.Resultadospdf.terminar_tabla()
        
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    miapp = formulario()
    miapp.show()
    sys.exit(app.exec_())