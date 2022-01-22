fraseIni = input("Entre sua frase: ").split() #Recebe um Input e transforma em LISTA

def joinStr(lista): #Funcao semelhante ao JOIN, recebe uma LISTA
    stringFin = ""
    for valor in lista: #Passa por todo Item dentro da Lista
        if valor != " ": #Se nao for igual a ESPACO:
            stringFin += valor #Adiciona o Item á variavel local "stringFin"
    print(stringFin)

joinStr(fraseIni) #Chama a def joinStr alimentando com a fraseIni