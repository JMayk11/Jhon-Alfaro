class Asistente:
    def __init__(self, run):
        self.run = run

asistentes = []
asientos_vendidos = []

def comprar_entradas():
    precios = {'Platinum': 120000, 'Gold': 80000, 'Silver': 50000}
    ubicaciones = [' ' for _ in range(100)]
    print('Ubicaciones disponibles:')
    for asiento, estado in enumerate(ubicaciones, start=1):
        if asiento <= 20:
            tipo = 'Platinum'
        elif asiento <= 50:
            tipo = 'Gold'
        else:
            tipo = 'Silver'
        print(f'{asiento}: {tipo} - {precios[tipo]}')
    cantidad = int(input('Ingrese la cantidad de entradas a comprar (entre 1 y 3): '))
    if cantidad < 1 or cantidad > 3:
        print('Cantidad inválida.')
        return
    for _ in range(cantidad):
        asiento = int(input('Ingrese el número de asiento que desea comprar: '))
        if asiento < 1 or asiento > 100:
            print('Asiento inválido.')
            continue
        if asiento in [a for a, _ in asientos_vendidos]:
            print('Ubicación no disponible.')
            continue
        run = input('Ingrese el RUN de la persona que ocupará el asiento (sin guión. Ej: 20978130): ')
        if len(run) != 8 or not run.isdigit():
            print('RUN inválido.')
            continue
        asistentes.append(Asistente(run))
        if asiento <= 20:
            tipo = 'Platinum'
        elif asiento <= 50:
            tipo = 'Gold'
        else:
            tipo = 'Silver'
        asientos_vendidos.append((asiento, tipo))
        print('Operación realizada correctamente.')

def mostrar_ubicaciones_disponibles():
    ubicaciones = [' ' for _ in range(100)]
    for asiento in range(1, 21):
        ubicaciones[asiento-1] = 'Platinum'
    for asiento in range(21, 51):
        ubicaciones[asiento-1] = 'Gold'
    for asiento in range(51, 101):
        ubicaciones[asiento-1] = 'Silver'
    for asiento, tipo in enumerate(ubicaciones, start=1):
        estado = 'X' if (asiento, tipo) in asientos_vendidos else ' '
        tipo_real = 'Platinum' if asiento <= 20 else ('Gold' if asiento <= 50 else 'Silver')
        print(f'{asiento}: {tipo_real} - {estado}')

def ver_listado_asistentes():
    print('Listado de asistentes:')
    asistentes_ordenados = sorted(asistentes, key=lambda x: x.run)
    for asistente in asistentes_ordenados:
        print(asistente.run)

def mostrar_ganancias_totales():
    precios = {'Platinum': 120000, 'Gold': 80000, 'Silver': 50000}
    total = sum(precios[tipo] for _, tipo in asientos_vendidos)
    print(f'Ganancias totales: ${total}')

while True:
    print('--- Menú ---')
    print('1. Comprar entradas')
    print('2. Mostrar ubicaciones disponibles')
    print('3. Ver listado de asistentes')
    print('4. Mostrar ganancias totales')
    print('5. Salir')

    opcion = input('Ingrese una opción: ')
    if opcion == '1':
        comprar_entradas()
    elif opcion == '2':
        mostrar_ubicaciones_disponibles()
    elif opcion == '3':
        ver_listado_asistentes()
    elif opcion == '4':
        mostrar_ganancias_totales()
    elif opcion == '5':
        print('Saliendo del sistema. ¡Gracias!')
        break
    else:
        print('Opción inválida.')
