from time import process_time_ns

nombre = input('ingrese su nombre')
dias = int(input('¿Reserva para cuantos días?'))
vista_mar = input('¿Desea reservar una habitación con vista al mar?si/no')

costo_habitacion = 150.5 if vista_mar.strip() == 'no' else 190.5
costo = dias * costo_habitacion
vista_mar_txt = 'con' if vista_mar == 'si' else 'sin'
print(f'''
{nombre}
habitación {vista_mar_txt} vista al mar
precio de habitacion: ${costo_habitacion}
tiempo de estadía: {dias} días
Costo total: ${costo}''')