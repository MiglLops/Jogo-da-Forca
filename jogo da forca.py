#jogo da forca 1.0 - 22/01/2024
import random

forca = input("ESCOLHA UMA ALTERNATIVA: 1 - Frutas, 2 - Paises, 3 - animais")

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
else:
    animais = ["formiga", "jacare", "anta", "capivara", "tamandua", "lesma", "leao", "dinossauro", "pato", "cachorro", "gato", "peixe", "passaro", "macaco", "aguaviva", "caranguejo", "cobra", "esponjadomar", "girafa", "castor", "escorpiao"]
    animal_aleatorio = random.choice(animais)
    palavra = animal_aleatorio
    numero = len(animal_aleatorio)

palavra_oculta = numero * "_"
print(f"{palavra_oculta}- {numero} Letras")
valor = 6

letras_tentadas = []

while True:
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
        print("erro")
        print(f"{palavra_oculta} - {numero} Letras")
        valor = valor - 1

    if "_" not in palavra_oculta or letra == palavra:
        print(f"Voce acertou a palavra!")
        break
    else:
        if valor <= 0:
            print("Voce perdeu!")
            break
        else:
            print(f"Restam {valor} tentativas")
