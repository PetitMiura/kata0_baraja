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

def barajar_for(baraja):
    for i in range(len(baraja)):
        j = random.randrange(0, len(baraja)-1)
        baraja[i], baraja[j] = baraja[j], baraja[i] 
    
    return baraja

