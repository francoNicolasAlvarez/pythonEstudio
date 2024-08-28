salida_sistema_txt= input('¿Salir del sistema?si/no')
salir_sistema = salida_sistema_txt.strip().lower() == 'si'


if not salir_sistema:
    print('Dentro del sistema')
else:
    print('saliendo del sistema')