def malicioso(InfoOponente,Mjugador):
    if InfoOponente[1]>10:
        DeltaAD = Mjugador ["malicioso"]
        InfoOponente [1] -= DeltaAD [1]
        print ("la defensa del oponente ahora es de " + str(InfoOponente[1]))
    else:
        print ("el oponente tiene la defensa al minimo")
    return InfoOponente

def placajeJ(Mjugador,InfoOponente):
    DeltaAD = Mjugador["placaje"]
    InfoOponente [0] -= DeltaAD[0] * (100/ InfoOponente[1])
    if InfoOponente [0] >= 0:
        print ("el PS del oponente es de" + str(InfoOponente[0]))
    else:
        print ("el oponente fue debilitado")
    return InfoOponente

def ascuas (Mjugador, InfoOponente):
    DeltaAD = Mjugador ["ascuas"]
    InfoOponente [0] -= DeltaAD [0] * (100 / InfoOponente[1]) 
    if InfoOponente [0] >= 0:
        print ("el PS del oponente es de " + str (InfoOponente[0]))
    else:
        print ("el oponente fue debilitado")
    return InfoOponente

def latigo (MOponente, infoJUgador):
    print ("el oponente utilizó latigo") 
    if infoJUgador[1] > 10:
        DeltaAD = MOponente["latigo"]
        infoJUgador[1] -= DeltaAD [1]
        infoJUgador [0] -= DeltaAD [0]
        print ("la defensa del jugador ahora es de" + str (infoJUgador[1]))
        print ("sus PS ahora son " + str(infoJUgador[0]))
    else:
        print("el jugador tiene la defensa al mínimo")
    return infoJUgador

def placajeO (MOponente, infoJUgador):
    print ("el oponente utilizó placaje")
    DeltaAD = MOponente ["placaje"]
    infoJUgador[0] -= DeltaAD[0] * (100 / infoJUgador[1])
    if infoJUgador [0] >= 0: 
        print ("el PS del jugador es de " + str (infoJUgador[0]))
    else: 
        print ("el jugador ha sido debilitado")
    return infoJUgador

def PAgua(MOponente, infoJUgador):
    print ("el oponente utilizó pistola de agua")
    DeltaAD = MOponente ["pistola de agua"]
    infoJUgador[0] -= DeltaAD[0] * (100 / infoJUgador[1])
    if infoJUgador [0] >= 0:
        print ("el PS del jugador es de " + str (infoJUgador[0]))
    else: 
        print ("el jugador ha sido debilitado")
    return infoJUgador
    
import math
import random
     
#El primer número de cada uno es la vida y el segundo la defensa
infoJUgador = [100 , 100]
InfoOponente = [100, 100]
    
Mjugador = { "malicioso" : ( 0,10), "placaje" : (35, 0), "ascuas" : (20, 0)}
MOponente = { "latigo" : ( 10,10), "placaje" : (35, 0), "pistola de agua" : (20, 0)}

               
# Pide a los jugadores que ingresen sus nombres al principio del juego
nombreJugador = input("Por favor, introduce el nombre del jugador: ")
nombreOponente = input("Por favor, introduce el nombre del oponente: ")

print (" Inicio de la batalla") 
print ("PS jugador " + str (infoJUgador[0]) + " y def jugador" + str(infoJUgador[1])) 
print ("PS oponente" + str (InfoOponente[0]) + " y def oponente" + str(InfoOponente [1]))

while True:
    # Desición de movimiento por parte del jugador 
    print ("¿Cuál será su movimiento?")
    print ("malicioso, ascuas, placaje")
    atJugador = input().lower()
    if atJugador == "malicioso" or atJugador == "ascuas" or atJugador == "placaje":
        if atJugador == "malicioso":
            malicioso(InfoOponente,Mjugador)
        elif atJugador == "ascuas":
            ascuas(Mjugador,InfoOponente)
        elif atJugador == "placaje":
            placajeJ(Mjugador, InfoOponente)
    else: 
        print("No posees el ataque " + str (atJugador))

    # Desición del movimiento por parte del oponente 
    atOponente= random.randrange(1,4)
    if atOponente == 1:
        latigo(MOponente, infoJUgador)
    elif atOponente == 2:
        placajeO (MOponente, InfoOponente)
    elif atOponente == 3:
        PAgua (MOponente, InfoOponente )

    # Verificar las condiciones de victoria
    if InfoOponente [0] <= 0 and infoJUgador[0] <= 0:
        print ("¡Es un empate!")
        break
    elif InfoOponente [0] <= 0:
        print ("¡" + nombreJugador + " ha ganado!")
        break
    elif infoJUgador[0] <= 0:
        print ("¡" + nombreOponente + " ha ganado!")
        break