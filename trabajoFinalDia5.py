from random import choice


def bienvenida():
    print("BIENVENIDOS al Ahorcador")
    print("Arrancas con 9 vidas para conseguir adivinar una palabra SECRETA")
    return


def ingresoletra():
    letraa = "1"
    while letraa not in "abcdefghijolmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        letraa = input('Ingresa una Letra:')
    return letraa.lower()


def generarpalabra():
    palabra = ('fuente','contar','estadio','musculo','sensacion','fuerza','casa')
    return choice(palabra)


def generarlineas(palabrasecreta):
    contador = len(palabrasecreta)
    adivinador = []
    for n in range(contador):
        adivinador.append('_')
    print(f'La palabra es {" ".join(adivinador)} y tiene {contador} letras')
    return adivinador


def controlvidas(vidaas):
    if vidaas > 0:
        print(f'Te quedan {vidaas}!')
        return vidaas - 1


def controlletra(letrar, palabra):
    palabra = list(palabra)
    encontradoss = []
    for n in range(len(palabra)):
        if letrar == palabra[n]:
            encontradoss.append(n+1)
    return encontradoss


def completarlineas(lista,letras,adivinador):
    for n in lista:
        adivinador[n-1] = letras
    print(" ".join(adivinador))
    return adivinador


bienvenida()
secreto = generarpalabra()
lineas = generarlineas(secreto)
vidas = 8
while vidas > 0:
    letra = ingresoletra()
    encontrados = controlletra(letra,secreto)
    if encontrados == []:
        vidas = controlvidas(vidas)
    lineas = completarlineas(encontrados,letra,lineas)
    if "_" not in lineas:
        print(f"FELICITACIONES adivinaste la palabra secreta!")
        break
    if vidas == 0:
        print('Game over')
        print(f'la palabra secreta era: {secreto}')
        break

