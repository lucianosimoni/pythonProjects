from operator import attrgetter
import qrcode

#Gerador de QR Code, salva as imagens localmente.
#Importando a biblioteca qrcode
#   Instalação da biblioteca:
#   pip install qrcode[pil] #Ja inclui a biblioteca pillow para gerar imgs.

stop = False

def cls(): print("\n" * 100)

def menuOpcoes():
    textoInput = """
    --------< QR Code Generator >--------
    --  [1] Simples                    --
    --  [2] Avançado                   --
    -------------------------------------
    Escolha o tipo de criação: """

    resposta = input(textoInput)
    if len(resposta) == 1 and resposta.isnumeric(): #Input 1 char apenas e é numerico
        if int(resposta) == 1:
            cls()
            qrCodeSimples()
            return
        else:
            cls()
            qrCodeAvancado()
    else: print("\n---!!!--- Opção invalida. ---!!!---")


def qrCodeSimples():
    dataInput = input("""--------< Simples >--------
    --  Valor do QR Code: """)
    
    nomeQrCode = input("""-- Nome do arquivo: """) + ".png"

    img = qrcode.make(dataInput)
    type(img) #qrcode.image.pil.PilImage   #Apenas mostra o tipo de arq.
    img.save(nomeQrCode)
    print("---------------------------")

def qrCodeAvancado():
    dataInput = input("--------< Avançado >---------------\n--  Valor do QR Code: ")
    versionInput = input("""--  Versão do QR (1-40): """)
    if versionInput.isnumeric() and int(versionInput) >= 1 and int(versionInput) <= 40: #É numerico e ta dentro da range
        versionInput = int(versionInput)
    else: 
        print("\n---!!!--- Valor não é numerico ou não é uma opção. ---!!!---")
        return
        
    errorInput = input("""--< Proteção >---------------------
    --  [1] 7% de correção de erros
    --  [2] 15% de correção de erros
    --  [3] 25% de correção de erros
    --  [4] 30% de correção de erros
    --  Escolha a proteção: """)
    if errorInput.isnumeric() and int(errorInput) >= 1 and int(errorInput) <= 4: #É numerico e ta dentro da range
        if int(errorInput) == 1: errorInput = "qrcode.constants.ERROR_CORRECT_L"
        elif int(errorInput) == 2: errorInput = "qrcode.constants.ERROR_CORRECT_M"
        elif int(errorInput) == 3: errorInput = "qrcode.constants.ERROR_CORRECT_Q"
        else: errorInput = "qrcode.constants.ERROR_CORRECT_H"
    else: 
        print("\n---!!!--- Valor não é numerico ou não é uma opção. ---!!!---")
        return
    
    boxInput = input("""--  Tamanho em px dos quadrados: """)
    if boxInput.isnumeric() and int(boxInput) >= 1: #É numerico e não é negativo
        boxInput = int(boxInput)
    else: 
        print("\n---!!!--- Valor não é numerico ou está negativo ---!!!---")
        return
    
    borderInput = input("""--  Tamanho em quadrados da 
    --  borda (Min 4): """)
    if borderInput.isnumeric() and int(borderInput) >= 4: #É numerico e maior ou igual a 4
        borderInput = int(borderInput)
    else: 
        print("\n---!!!--- Valor não é numerico ou é menor que 4 ---!!!---")
        return

    fillColorInput = input("""--< Cor de Preenchimento >---------
    --  [1] Preto
    --  [2] Branco
    --  [3] Azul
    --  [4] Laranja
    --  Escolha a cor: """)
    if fillColorInput.isnumeric() and int(fillColorInput) >= 1 and int(fillColorInput) <= 4: #É numerico e ta dentro da range
        if int(fillColorInput) == 1: fillColorInput = "black"
        elif int(fillColorInput) == 2: fillColorInput = "white"
        elif int(fillColorInput) == 3: fillColorInput = "blue"
        else: fillColorInput = "orange"
    else: 
        print("\n---!!!--- Valor não é numerico ou não é uma opção. ---!!!---")
        return

    backColorInput = input("""--< Cor de Fundo >-----------------
    --  [1] Preto
    --  [2] Branco
    --  [3] Azul
    --  [4] Laranja
    --  Escolha a cor: """)
    if backColorInput.isnumeric() and int(backColorInput) >= 1 and int(backColorInput) <= 4: #É numerico e ta dentro da range
        if int(backColorInput) == 1: backColorInput = "black"
        elif int(backColorInput) == 2: backColorInput = "white"
        elif int(backColorInput) == 3: backColorInput = "blue"
        else: backColorInput = "orange"
    else: 
        print("\n---!!!--- Valor não é numerico ou não é uma opção. ---!!!---")
        return

    nameQrCode = input("""--  Nome do arquivo: """) + ".png"

    qr = qrcode.QRCode(
        version=versionInput,
        error_correction= eval(errorInput),
        box_size=boxInput,
        border=borderInput
    )
    qr.add_data(dataInput)
    img = qr.make_image(fill_color=fillColorInput, back_color=backColorInput)
    img.save(nameQrCode)
    print("-----------------------------------")

while stop == False:
    menuOpcoes()