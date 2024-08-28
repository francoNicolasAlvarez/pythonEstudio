compra = int(input('Ingrese el valor de la compra\n'))
cliente = (input('Es socio de la tienda si/no\n')).strip()
descuento=0
if compra > 1000:
    if cliente == 'si':
        descuento = compra*0.1
    else:
        descuento = compra*0.05
print(F'''
{cliente.upper()} ES CLIENTE
LA COMPRA ES DE ${compra}
EL DESCUENTO ES DE ${descuento}
Y EL TOTAL ES DE {compra - descuento}''')