# A Lista de cada valor é organizada desta forma:
# 0:["Titulo", "Artista", "Genero", "Duração"]
musicas = {
    0:["Infinita Highway", "Engenheiros do Hawaii", "Rock Nacional", "4:18"],
    1:["O papa é pop", "Engenheiros do Hawaii", "Rock Nacional", "3:55"],
    2:["sou dela", "nando reis", "pop", "4:34"],
    3:["por onde andei", "nando reis", "pop", "3:59"],
    4:["tempos modernos", "lulu santos", "pop", "3:45"],
    5:["toda forma de amor", "lulu santos", "pop", "3:48"]
}

def corpoprincipal(): #função da nossa interfarsse grafica
    print('''Escolha uma opção:
******playlist spotify************
 *  1. Cadastrar musica                                              *
 *  2. exibir musicas                                                *
 *  3. filtrar          
 *  0. Sair                                                          *
************************
    ''')

def cadastroDemusic():
    titulo = input('Digite o titulo da musica: ')
    artista = input('Digite o nome do Artista: ')
    genero = input('Digite o genero: ')
    duracao = input('Digite quanto tempo tem a musica: ')
    listinha = [titulo, artista, genero, duracao]
    if len(musicas) == 0:
        musicas[0] = listinha
    else:
        ultiMusicID = list(musicas)[-1]
        proxMusicID = ultiMusicID + 1
        musicas[proxMusicID] = listinha

def calcularTempo(listaDeIDS):
    horasTotais = 0
    minutosTotais = 0
    segundosTotais = 0

    for id in listaDeIDS:
        horaSplit = musicas[id][3].split(":")
        minInt = int(horaSplit[0])
        segInt = int(horaSplit[1])
        minutosTotais += minInt
        segundosTotais += segInt

    if segundosTotais >= 60:
        segundosTotais = segundosTotais%60
        minutosTotais += 1
    elif minutosTotais >= 60:
        minutosTotais = minutosTotais%60
        horasTotais += 1
    print("Tempo da playlist: ", horasTotais,":",minutosTotais,":",segundosTotais," ==/==/==/==/==/== \n ")

def filtrarMusicas():
  #Artista é o IDX 1
  #Genero é o IDX 2
  oQueFiltrar = input("[1]Artista\n[2]Genero\n")
  if oQueFiltrar == "1": #Artista
    artista = input("Digite o nome do seu Artista: ") #ACHO QUE EH PQ EH STRING
    idsDasMusicas = []
    print(" \nExibindo filtro de artista.")
    for i in musicas:
      if musicas[i][1] == artista: #Se o artista do item i do dicionario musicas for o mesmo que o input
        idsDasMusicas.append(i) 
        print(" - ".join(musicas[i])) #Mostra a musica filtrada!!
    #Adicionar uma condição pra se o idsDasMusicas estiver vazio, printar que nao encontrou musicas.
    if len(idsDasMusicas) <= 0:
      print("Nenhuma musica encontrada.\n ")
    else:
      calcularTempo(idsDasMusicas)
  
  elif oQueFiltrar == "2": #Genero
    genero = input("Digite o genero desejado: ")
    idsDasMusicas = []
    print(" ")
    print(" \nExibindo filtro de genero")
    for i in musicas:
      if musicas[i][2] == genero:
        idsDasMusicas.append(i)
        print(" - ".join(musicas[i])) #Mostrar a musica filtrada!!
    #Adicionar uma condição pra se o idsDasMusicas estiver vazio, printar que nao encontrou musicas.
    if len(idsDasMusicas) <= 0:
      print("Nenhuma musica encontrada.")
      print(" ")
    else:
      calcularTempo(idsDasMusicas)
  
  else: #Se o user ter digitado outro valor
    print("Opção inexistente. Tente novamente")

def exibirMusica():
    idsDasMusicas = []
    print(" \nExibindo playlist Spotify.")
    
    for i in musicas:
        idsDasMusicas.append(i)
        print(" - ".join(musicas[i]))

    calcularTempo(idsDasMusicas)
    
while True:
    corpoprincipal()
    opcao= int(input('Digite a opção que você deseja acessar:'))
    if opcao == 1:
        cadastroDemusic()
    elif opcao == 2:
        exibirMusica()
    elif opcao == 3:
        filtrarMusicas()
    elif opcao == 0:
        break