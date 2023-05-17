import random 

def crear_baraja(n, p):
    numeros = n
    palos = p

    baraja = []

    for palo in palos:
        for numero in numeros:
            naipe = numero + palo
            baraja.append(naipe)

    return baraja

def barajar(baraja):
    nueva_baraja = []
    if baraja:
        nueva_baraja = random.sample(baraja, len(baraja))

    return nueva_baraja

