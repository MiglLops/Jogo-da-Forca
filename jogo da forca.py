#jogo da forca 1.0 - 22/01/2025 // jogo da forca 2.0 - 01/02/2025
import random

def sorteio_palavra():
    global valor, palavra_oculta, letras_tentadas, palavra, numero
    forca = input("ESCOLHA UMA ALTERNATIVA: 1 - Frutas, 2 - Paises, 3 - animais, 4 - palavras")

    if forca == "1":
        frutas = ["pera", "maca", "banana", "abacaxi", "uva", "pessego", "morango", "limao", "laranja", "mexerica", "kiwi", "carambola"]
        fruta_aleatoria = random.choice(frutas)
        palavra = fruta_aleatoria
        numero = len(fruta_aleatoria)

    elif forca == "2":
        paises = ["brasil", "argentina", "nauru", "italia", "peru", "bolivia", "venezuela", "monaco", "canada", "estadosunidos", "africadosul", "china", "finlandia", "portugal", "espanha", "taiwan", "angola", "butao", "mexico", "abudhabi", "franca", "alemanha", "belgica", "russia", "panama", "groelandia"]
        pais_aleatorio = random.choice(paises)
        palavra = pais_aleatorio
        numero = len(pais_aleatorio)
    elif forca == "3":
        animais = ["formiga", "jacare", "anta", "capivara", "tamandua", "lesma", "leao", "dinossauro", "pato", "cachorro", "gato", "peixe", "passaro", "macaco", "aguaviva", "caranguejo", "cobra", "esponjadomar", "girafa", "castor", "escorpiao"]
        animal_aleatorio = random.choice(animais)
        palavra = animal_aleatorio
        numero = len(animal_aleatorio)
    elif forca == "4":
        palavras = ["amor", "termo", "abrir", "raios", "clube", "janta", "metal", "antes", "odiar", "lugar"]
        palavras_aleatorio = random.choice(palavras)
        palavra = palavras_aleatorio
        numero = len(palavras_aleatorio)
    palavra_oculta = numero * "_"
    print(f"{palavra_oculta}- {numero} Letras")
    valor = 6
    letras_tentadas = []

def rodar_jogo():
    global continuar, palavra_oculta, numero, valor
    continuar = True
    while continuar:
        letra = input("Digite uma palavra ou letra:").lower()

        if letra in letras_tentadas:
            print(f"Voce ja tentou essa a letra '{letra}'. Tente outra.")
            continue
        letras_tentadas.append(letra)

        if letra in palavra:
            palavra_oculta = "".join([letra if palavra[i] == letra else palavra_oculta[i] for i in range(len(palavra))])
            numero = numero - 1
            print(f"{palavra_oculta} - {numero} Letras")
        else:
            print("errado")
            print(f"{palavra_oculta} - {numero} Letras")
            valor = valor - 1

        if "_" not in palavra_oculta or letra == palavra:
            print(f"Voce acertou a palavra! - {palavra}")
            novamente = input("Deseja jogar novamente? s/n")
            if novamente == "s":
                sorteio_palavra()
            else:
                print("Jogo finalizado")
                continuar = False
        else:
            if valor <= 0:
                print(f"Voce perdeu! A palavra era '{palavra}'")
                novamente = input("Deseja jogar novamente? s/n")
                if novamente == "s":
                    sorteio_palavra()
                else:
                    print("Jogo finalizado")
                    continuar = False
            else:
                print(f"Restam {valor} tentativas")

sorteio_palavra()
rodar_jogo()