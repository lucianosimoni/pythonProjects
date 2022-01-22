msgIni = input("Msg: ").lower() #transformar em minusculas ".lower()"
msgFinNum = []

alfLet = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
"n","o","p","q","r","s","t","u","v","w","x","y","z","space"]
alfNum = [-26,-25,-24,-23,-22,-21,-20,-19,-18,-17,-16,-15,-14,-13,-12,
-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,666]

for i in msgIni:
    idx:int
    if i in alfLet: #verificar se a letra tem na array alfLet
        idx = alfLet.index(i) #pega o index da letra na array letras
        msgFinNum.insert(0, alfNum[idx]) #add na array final o valor da idx numeros
    elif i == " ":
        msgFinNum.insert(0, alfNum[26]) #0 pois é um espaço
    else: 
        msgFinNum.insert(0, alfNum[27]) #666 pois não existe
        
print(msgFinNum)

#Questão do brainly: https://brainly.com.br/tarefa/51172945?answeringSource=feedPublic%2FhomePage%2F12
#O .insert(0, idx) vai inserir o valor do respectivo index na posição 0 (primeira casa) da array, fazendo com que a Array seja "lida" de traz pra frente como pedido na questão.