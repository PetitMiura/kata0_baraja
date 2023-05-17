import barajas
'''
baraja_espanyola = crear_baraja(["A ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "S ", "C ", "R "], ("Bastos", "Copas", "Espadas", "Oros"))
baraja_espanyola_barajada = barajar(baraja_espanyola)

baraja_francesa = crear_baraja(["A ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "10 ", "J ", "Q ", "K "], ("Picas", "Corazones", "Diamantes", "Tréboles"))
baraja_francesa_barajada = barajar(baraja_francesa) 

print()
print(baraja_espanyola)
print()
print()
print(baraja_francesa)
print()
print()
print(baraja_espanyola_barajada)
print()
print()
print(baraja_francesa_barajada)
'''

b = barajas.crear_baraja("A234567SCR", "oceb")
print(b)
barajas.barajar_for(b)

mi_baraja = barajas.Baraja("A234567SCR", "BCEO")
print(mi_baraja.naipes)