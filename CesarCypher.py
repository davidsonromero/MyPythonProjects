def checkIndex(a, b):
    count = 0
    for x in b:
        if(x == a):
            return count
        else:
            count += 1

def encripta(text, transform): 
    upperAlphabet = ['A', 'Á', 'Ã', 'À', 'Â', 'Ä', 'B', 'C', 'Ç', 'D', 'E', 'É', 'È', 'Ê', 'Ë', 'F', 'G', 'H', 'I', 'Í', 'Ì', 'Ï', 'Î', 'J', 'K', 'L', 'M', 'N', 'O', 'Õ', 'Ô', 'Ó', 'Ò', 'Ö', 'P', 'Q', 'R', 'S', 'T', 'U', 'Ú', 'Ù', 'Û', 'Ü', 'V', 'W', 'X', 'Y', 'Z']
    lowerAlphabet = ['a', 'á', 'ã', 'à', 'â', 'ä', 'b', 'c', 'ç', 'd', 'e', 'é', 'è', 'ê', 'ë', 'f', 'g', 'h', 'i', 'í', 'ì', 'ï', 'î', 'j', 'k', 'l', 'm', 'n', 'o', 'õ', 'ô', 'ó', 'ò', 'ö', 'p', 'q', 'r', 's', 't', 'u', 'ú', 'ù', 'û', 'ü', 'v', 'w', 'x', 'y', 'z']

    transformedText = ""

    for letter in text:
        #verifica se é espaço ou número
        if(letter.isalpha() == False):
            transformedText += letter

        #se for letra maiúscula:
        elif(letter.isupper()):
            index = checkIndex(letter, upperAlphabet)
            if(transform + index > 48):
                rotate = transform + index - 49
            else:
                rotate = index + transform
            transformedText += upperAlphabet[rotate]

        #se for letra minúscula:
        elif(letter.islower()):
            index = checkIndex(letter, lowerAlphabet)
            if(transform + index > 48):
                rotate = transform + index - 49
            else:
                rotate = index + transform
            transformedText += lowerAlphabet[rotate]

    return transformedText

def descripta(text, transform): 
    upperAlphabet = ['A', 'Á', 'Ã', 'À', 'Â', 'Ä', 'B', 'C', 'Ç', 'D', 'E', 'É', 'È', 'Ê', 'Ë', 'F', 'G', 'H', 'I', 'Í', 'Ì', 'Ï', 'Î', 'J', 'K', 'L', 'M', 'N', 'O', 'Õ', 'Ô', 'Ó', 'Ò', 'Ö', 'P', 'Q', 'R', 'S', 'T', 'U', 'Ú', 'Ù', 'Û', 'Ü', 'V', 'W', 'X', 'Y', 'Z']
    lowerAlphabet = ['a', 'á', 'ã', 'à', 'â', 'ä', 'b', 'c', 'ç', 'd', 'e', 'é', 'è', 'ê', 'ë', 'f', 'g', 'h', 'i', 'í', 'ì', 'ï', 'î', 'j', 'k', 'l', 'm', 'n', 'o', 'õ', 'ô', 'ó', 'ò', 'ö', 'p', 'q', 'r', 's', 't', 'u', 'ú', 'ù', 'û', 'ü', 'v', 'w', 'x', 'y', 'z']

    transformedText = ""

    for letter in text:
        if(letter.isalpha() == False):
            transformedText += letter

        elif(letter.isupper()):
            index = checkIndex(letter, upperAlphabet)
            if(index - transform < 0):
                rotate = index - transform + 49
            else:
                rotate = index - transform
            transformedText += upperAlphabet[rotate]

        elif(letter.islower()):
            index = checkIndex(letter, lowerAlphabet)
            if(index - transform < 0):
                rotate = index - transform + 49
            else:
                rotate = index - transform
            transformedText += lowerAlphabet[rotate]

    return transformedText

def convert(text, transform, option):
    if(option == 1):
        convertedText = encripta(text, transform)
    elif(option == 2):
        convertedText = descripta(text, transform)

    return("\n" + convertedText)

def ler_dados(mensagem, valores_validos, conversao=None):
    msg_erro = f'Valor inválido, deve ser um desses: {", ".join(map(str, valores_validos))}\n'
    while True:
        try:
            valor = input(mensagem)
            if conversao is not None:
                valor = conversao(valor)
            if valor in valores_validos:
                return valor
            else:
                print(msg_erro)
        except:
            print(msg_erro)

print ("Bem-vindo! Este programa serve para encriptar ou descriptar textos com a Cifra de César.\n\n")

while True:
    text = input("Escreva o texto para encriptar ou descriptar:\n")

    option = ler_dados("Escolha uma opção:\n\n1-Encriptar o texto\n\n2-Descriptar o texto\n> ", [1, 2], int)

    transform = ler_dados("Escolha o número de rotação (1-48): ", range(1, 49), int)

    print(f'\nResultado da conversão:\n\n {convert(text, transform, option)}')

    reiniciar = ler_dados('\n\nDeseja reiniciar o programa (S/N)?\n', ['s', 'n'], str.lower)
    if reiniciar == 'n':
        break

#Créditos pela ajuda: https://pt.stackoverflow.com/users/112052 Valeu, Mano!