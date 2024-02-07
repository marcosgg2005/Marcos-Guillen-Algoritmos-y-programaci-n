import random #para RandRange 

ps_jugador = 100
ps_oponente = 100
defensa_oponente = 100
defensa_jugador = 100
while ps_jugador > 0 and ps_oponente > 0:
    ataque_jugador = input ("ataque (opciones disponibles malicioso, placaje, ascuas.): ")
    ataque_jugador = ataque_jugador.lower()
    if ataque_jugador == "malicioso":
        defensa_oponente = defensa_oponente -10 
        if defensa_oponente <= 0:
            defensa_oponente = 1
    elif ataque_jugador == "placaje":
        ps_oponente -= 35 / (defensa_oponente/100)
    elif ataque_jugador == "ascuas":
        ps_oponente -= 20
    else:
         print ("Que estas haciendo?! Tus ataques son malicioso, placaje y ascuas!")
            
    #Turno Oponente 
    #El turno del oponente se define con un random 
    ataque_oponente = random.randrange (1, 3+1)
    if ataque_oponente == 1 : #latigo 
        print("El oponente uso Latigo")
        defensa_jugador = -10 
        if defensa_jugador <= 0 :
            defensa_jugador = 1
    elif ataque_oponente ==2 : 
        print("El oponente uso placaje")
        ps_jugador -= 35 * (100/defensa_jugador)
    elif ataque_oponente == 3 : #pistola de agua
        print("El oponente uso pistolas de agua")
        ps_jugador -= 40 
#randrange esta garantizado a ser 1,2, ó 3 

#Si termina el ciclo alguien ha ganado 
if ps_oponente <= 0 and ps_jugador <= 0 :
    print ("Empate")
elif ps_oponente <= 0: 
    print ("Felicidades, has ganado")
else:
    print ("Lo siento has perdido")
    