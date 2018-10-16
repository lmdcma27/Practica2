  -Clase Disco: solamente contiene el atributo diametro que es un entrero y el método con_diametro que retorna el diametro del disco.

  -Clase Poste: no contiene atributos y sus metodos son los mismos que los de una pila; recibir() agrega un elemento al poste, entregar() retira el elemento superior del poste, e_superior() retorna el elemento superior del poste, longitud() retorna el número de elementos y con_poste() verifica si el poste no contiene elementos.
  
  -interfaz: luego de instanciar la clases poste y disco se definío el metodo inicio en donde se ingresar los discos a los postes. El método postes disponibles verifica el texto actual del ComboBox usado para seleccionar y determina si el poste seleccionado esta o no vacio, dentro de esta condicion vuelve a determinar si un segundo poste esta o no vacio para saber si debe comparar los diametros de los discos, entonces oculta o hace visible los postes y cambia el color del disco seleccionado segun este se pueda cambiar o no de poste, análogamente para el poste seleccionado y el tercer poste. Dado que el ComboBox tiene 3 elementos, repetimos las mismas condiciones permutando los postes. Despues de que cualquier poste sea seleccionado habilita el segundo CombBox.
  
   El método desplazar se activa al hacer click en el boton mover, toma el texto actual de ambos ComboBox y entonces calcula la altura del poste al cual se desplaza el disco para determinar las nuevas coordenadas del disco, luego agrega el disco superior del primer poste al segundo, después lo elimina del primero y le cambia el color y verifica si un poste(no el inicial) tiene longitud 8 para terminar el juego. Por último deshabilita el segundo ComboBox y el boton mover.
   
   El método desbloquear habilita el boton mover y se ejecuta al seleccionar cualquier poste del ComboBox.
   El método contar_movimiento cuenta el número de movimientos realizados en la partida y se ejecuta al hacer click en el boton mover.
   El último méetodo es el evento closeEvent() que guarda los textos actuales de los ComboBox, el último disco desplazado. Finalmente los muestra en un pdf compilado desde latex.
 
  
  
