#while
contador = 0
while contador<=5:
    contador+=1
    print(contador, end =' ')
print('\n')
#For

cadena='Hola que hace'

for letra in cadena:
    print(letra, end = ' ')
print('\n')
frutas = ['banana','manzana','naranja']
for fruta in frutas:
    print(fruta)

acumulador = 0
ciclos = 0
while ciclos < 5:
     ciclos+=1
     print(f'ciclo {ciclos}')
     acumulador+=ciclos
     print(acumulador)