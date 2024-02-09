print (" Hoy vamos a realizar una receta de arepas")
print (" para ello me vas a indicar la cantidad de ingredientes a implementar y te dire cuantas arepas saldrán")
print ( "los ingredientes son: Agua, Harina PAN, cdt de sal" )

harina=int (input("indica la cantidad de harina a utilizar en gramos:"))
agua= int (input("indica la cantidad de agua a utilizar en ml:"))
sal= int (input("indica la cantidad de sal a utilizar en gramos:"))
#1 ml de agua = 1g de agua
# 1 cucharada = 12g 
 
gramos= harina + agua+ sal 
arepa= gramos / 65 
 
print ("vas a obtener", arepa, "arepas")
