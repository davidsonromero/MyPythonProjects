alphabetWithAccents = ['a', 'á', 'à', 'ã', 'â', 'ä', 'b', 'c', 'ç', 'd', 'e', 'é', 'è', 'ê', 'ë', 'f', 'g', 'h', 'i', 'í', 'ì', 'î', 'ï', 'j', 'k', 'l', 'm', 'n', 'o', 'ó', 'ò', 'õ', 'ô', 'ö', 'p', 'q', 'r', 's', 't', 'u', 'ú', 'ù', 'û', 'ü', 'v', 'w', 'x', 'y', 'z', 'ç', 'ñ']
upperAlphabetWithAccents = ['A', 'Á', 'À', 'Ã', 'Â', 'Ä', 'B', 'C', 'Ç', 'D', 'E', 'É', 'È', 'Ê', 'Ë', 'F', 'G', 'H', 'I', 'Í', 'Ì', 'Î', 'Ï', 'J', 'K', 'L', 'M', 'N', 'O', 'Ó', 'Ò', 'Õ', 'Ô', 'Ö', 'P', 'Q', 'R', 'S', 'T', 'U', 'Ú', 'Ù', 'Û', 'Ü', 'V', 'W', 'X', 'Y', 'Z', 'Ç', 'Ñ']

def checkIndex(a, b):
    count = 0
    for x in b:
        if(x == a):
            return count
        else:
            count += 1

def encripta(letter, transform): 

    transformedText = ""
    #verifica se é espaço ou número
    if(letter.isalpha() == False):
        transformedText += letter
    #se for letra maiúscula:
    elif(letter.isupper()):
        index = checkIndex(letter, upperAlphabetWithAccents)
        if(transform + index > 50):
            rotate = transform + index - 51
        else:
            rotate = index + transform
        transformedText += upperAlphabetWithAccents[rotate]
    #se for letra minúscula:
    elif(letter.islower()):
        index = checkIndex(letter, alphabetWithAccents)
        if(transform + index > 50):
            rotate = transform + index - 51
        else:
            rotate = index + transform
        transformedText += alphabetWithAccents[rotate]
    return transformedText

def descripta(letter, transform): 
  
    transformedText = ""
    if(letter.isalpha() == False):
        transformedText += letter
    elif(letter.isupper()):
        index = checkIndex(letter, upperAlphabetWithAccents)
        if(index - transform < 0):
            rotate = index - transform + 51
        else:
            rotate = index - transform
        transformedText += upperAlphabetWithAccents[rotate]

    elif(letter.islower()):
        index = checkIndex(letter, alphabetWithAccents)
        if(index - transform < 0):
            rotate = index - transform + 51
        else:
            rotate = index - transform
        transformedText += alphabetWithAccents[rotate]

    return transformedText

def getRotationNumbers(password, text):
    length = len(text)
    password = password.lower()
    rotationNumbers = []
    for x in range(len(password)):
        rotationNumbers.append(alphabetWithAccents.index(password[x]) + 1)
    repeat = length // len(password)
    for x in range(repeat):
        for y in range(len(password)):
            rotationNumbers.append(rotationNumbers[y])
    return rotationNumbers

def readOption():
    try:
        option = int(input("Escolha uma opção:\n\n1-Encriptar o texto\n\n2-Descriptar o texto\n> "))
    except:
        print("Opção inválida!")
        return readOption()
    if(option == 1):
        return 1
    elif(option == 2):
        return 2
    else:
        print("Opção inválida!")
        readOption()

def checkPassword(password):
    if(len(password) < 1):
        print("Senha inválida!")
        return False
    else:
        for x in password:
            if(x.isalpha() == False):
                print("Senha inválida!")
                return False
            else:
                return True

def endOrRestart():
    reiniciar = input("\n\nDeseja reiniciar o programa (S/N)?\n")
    if(reiniciar.lower() == 's'):
        return True
    else:
        return False

while True:
    print("""
_____   ____  _____   ______  ________  ____  _____  ________  ______      ________
|_  _| |_  _||_   _|.' ___  ||_   __  ||_   \|_   _||_   __  ||_   __ \   |_   __  | 
  \ \   / /    | | / .'   \_|  | |_ \_|  |   \ | |    | |_ \_|  | |__) |    | |_ \_| 
   \ \ / /     | | | |   ____  |  _| _   | |\ \| |    |  _| _   |  __ /     |  _| _  
    \ ' /     _| |_\ `.___]  |_| |__/ | _| |_\   |_  _| |__/ | _| |  \ \_  _| |__/ | 
     \_/     |_____|`._____.'|________||_____|\____||________||____| |___||________| 
   ______  ____  ____  _______  ____  ____  ________  _______                        
 .' ___  ||_  _||_  _||_   __ \|_   ||   _||_   __  ||_   __ \                       
/ .'   \_|  \ \  / /    | |__) | | |__| |    | |_ \_|  | |__) |                      
| |          \ \/ /     |  ___/  |  __  |    |  _| _   |  __ /                       
\ `.___.'\   _|  |_    _| |_    _| |  | |_  _| |__/ | _| |  \ \_                     
 `.____ .'  |______|  |_____|  |____||____||________||____| |___|  
 
 """)
 
    text = input("\n\nDigite o texto a ser processado: ")
    option = readOption()
    password = input("Digite a senha (apenas letras): ")
    control = 0
    transformedText = ""
    if(not checkPassword(password)):
        if(endOrRestart()):
            continue
        else:
            break
    else:
        rotation = getRotationNumbers(password, text)
        if(option == 1):
            for x in text:
                transformedText += encripta(x, rotation[control])
                control += 1
        elif(option == 2):
            for x in text:
                transformedText += descripta(x, rotation[control])
                control += 1

        print("\n\nTexto criptografado: \n" + transformedText)
        if(endOrRestart()):
            continue
        else:
            break