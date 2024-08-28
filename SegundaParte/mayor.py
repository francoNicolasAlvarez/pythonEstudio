numero1,numero2= input('ingrese 2 números').split()
mayor = 'ninguno'
if numero1>numero2:
    mayor = numero1
elif numero2>numero1:
    mayor = numero2

print(f'El mayor es : {mayor}')