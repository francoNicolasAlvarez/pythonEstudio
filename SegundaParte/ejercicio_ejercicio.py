nombre = input('Ingrese su nombre')
pasos = int(input('¿Cuanto caminó hoy?'))

META_PASOS_DIARIOS= 10000
calorias_por_paso=0.04
calorias_quemadas= pasos*calorias_por_paso
meta_alcanzada = 'si' if META_PASOS_DIARIOS<=pasos else 'no'

print(f'''
{nombre}
caminaste {pasos}
{meta_alcanzada} alcanzaste la meta
quemaste {calorias_quemadas} calorias''')

