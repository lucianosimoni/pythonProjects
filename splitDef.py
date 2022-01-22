fraseIni = input("Texto inicial: ") #Pega o input do user

def splitChar(frase): #Funcao semelhante ao SPLIT
    arrayFin = [] #Nossa variavel de retorno (print)
    for i in frase:
        arrayFin.append(i)
    return(arrayFin)

print(splitChar(fraseIni))
