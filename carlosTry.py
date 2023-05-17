''' 
import random

for i in range(len(baraja)):
    j = random.randint(0, len(baraja)-1)
    baraja[i], baraja[j] = baraja[j], baraja[i] 
'''