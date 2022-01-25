# A Lista de cada valor é organizada desta forma:
# 0:["ID", "Titulo", "Artista", "Duração"]
musicas = {

}

#A lista de cada valor é organizada desta forma:
#'Nome da playlist':[id da musica, id da musica]
playlists = {

}

def corpoprincipal(): #função da nossa interfarsse grafica
    print('\n1. Cadastrar musica\n2. Exibir musicas\n3. Criar playlist\n4. Exibir playlist\n0. Sair\n')

def cadastrarMusica():
    titulo = input('Digite o titulo da musica: ')
    artista = input('Digite o nome do Artista: ')
    duracao = input('Digite quanto tempo tem a musica: ')
    listinha = [titulo, artista, duracao]
    if len(musicas) == 0: #Se o dict MUSICAS estiver vazio, definir a ID para 0
        listinha.insert(0, str(0)) #Adiciona o ID à LISTA
        musicas[0] = listinha
    else: #Se não estiver vazio, pegar o ultimo ID e adicionar +1
        ultiMusicID = list(musicas)[-1]
        proxMusicID = ultiMusicID + 1
        listinha.insert(0, str(proxMusicID))
        musicas[proxMusicID] = listinha

def exibirMusicas(): #EXIBE TODAS AS MUSICAS
    print(' \n-- Exibindo musicas.')
    for i in musicas:
        print(' - '.join(musicas[i]))

def exibirMusica(idDaMusica): #EXIBE APENAS A MUSICA DO ID
    if musicas[idDaMusica]:
        print(' - '.join(musicas[idDaMusica]))

def criarPlaylist():
    nomePlaylist = input('Digite o nome da sua playlist: ')
    idMusicas = input('Digite separado por virgulas os IDs das musicas que quer adicionar: ')
    idMusicasSplited = idMusicas.split(',')
    playlists[nomePlaylist] = idMusicasSplited #Cria um novo dicionario

def exibirPlaylist():
    nomePlaylist = input('Nome da playlist: ')
    if playlists[nomePlaylist]: #Se existe a playlist do usuario
        for i in playlists[nomePlaylist]:
            exibirMusica(int(i))

while True:
    corpoprincipal()
    opcao= int(input('Digite a opção que você deseja acessar: '))
    if opcao == 1: #Cadastro musica
        cadastrarMusica()
    elif opcao == 2: #Exibir musicas
        exibirMusicas()
    elif opcao == 3: #Cadastrar playlist
        criarPlaylist()
    elif opcao == 4: #Exibir playlists
        exibirPlaylist()
    elif opcao == 0:
        break