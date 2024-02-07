año= int (input ("selecciona un año entre 1990 y 2199 para saber si es bisiesto"))
if (año % 4 == 0 and año %100 != 0)or año % 400 == 0 :
    print ("El año", año,  "es Bisiesto")
else:
    print ("El año", año,  "no es Bisiesto")