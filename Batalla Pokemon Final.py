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
    InfoOponente [0] -= DeltaAD [0] * (100 / InfoOponente [1]) 
    if InfoOponente [0] >= 0:
        print ("el PS del oponente es de " + str (InfoOponente[0]))
    else:
        print ("el oponente fue debilitado")
    return InfoOponente
