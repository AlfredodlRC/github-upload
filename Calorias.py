print("¿Que dia es hoy?")
dia=input()
print("Carlorias del desayuno:")
caloriasDesayuno=int(input())
print("Carlorias de la comida:")
caloriasComida=int(input())
print("Carlorias de la merienda:")
caloriasMerienda=int(input())
print("Carlorias de la cena:")
caloriasCena=int(input())

caloriasDia=caloriasDesayuno+caloriasComida+caloriasMerienda+caloriasCena

print("Las calorias consumidas el dia "+dia+" son "+str(caloriasDia))

