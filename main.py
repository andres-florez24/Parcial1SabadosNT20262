# Sistema de Monitoreo de Consumo Energético
# Función 1: Registrar Comercio
def registrar_Comercio():
    """
    Solicita datos del comercio y retorna un diccionario
    Entradas: nombre, meta de consumo
    Salida: diccionario con nombre, meta y lista vacía de consumos
    """
    nombre = input("Ingrese nombre del comercio: ")
    meta = float(input("Ingrese meta de consumo (kWh): "))
    
    comercio = {
        "nombre": nombre,
        "meta": meta,
        "consumos": []
    }
    
    return comercio
 
 
# Función 2: Registrar Consumo
def registrar_Consumo(comercio):
    """
    Registra 4 semanas de consumo para un comercio
    Entrada: diccionario comercio
    Salida: diccionario comercio actualizado con consumos
    """
    consumos = []
    
    for i in range(1, 5):
        consumo = float(input(f"Ingrese consumo semana {i} (kWh): "))
        consumos.append(consumo)
    
    comercio["consumos"] = consumos
    
    return comercio
 
 
# Función 3: Calcular Promedio
def calcular_Promedio(consumos):
    """
    Calcula el promedio de consumo SIN usar sum()
    Entrada: lista de consumos (4 valores)
    Salida: promedio en float
    """
    suma = 0
    cantidad = 0
    
    for valor in consumos:
        suma = suma + valor
        cantidad = cantidad + 1
    
    promedio = suma / cantidad
    
    return promedio
 
 
# Función 4: Calcular Variación
def calcular_variacion(consumos):
    """
    Calcula la variación porcentual entre semana 1 y semana 4
    Fórmula: ((semana4 - semana1) / semana1) * 100
    Entrada: lista de consumos [sem1, sem2, sem3, sem4]
    Salida: variación porcentual en float
    """
    semana1 = consumos[0]
    semana4 = consumos[3]
    
    variacion = ((semana4 - semana1) / semana1) * 100
    
    return variacion
 
 
# Función 5: Clasificar Consumo
def clasificar_consumo(promedio, meta, variacion):
    """
    Clasifica el consumo según promedio, meta y variación
    Criterios:
    - Eficiente: promedio <= meta AND variación <= 5%
    - Observación: promedio <= meta AND variación > 5%
    - Alto: promedio > meta hasta 20% (meta <= promedio <= meta*1.20)
    - Crítico: promedio > meta en más del 20% (promedio > meta*1.20)
    
    Entrada: promedio (float), meta (float), variacion (float porcentaje)
    Salida: clasificación (string)
    """
    clasificacion = ""
    
    if promedio <= meta:
        if variacion <= 5:
            clasificacion = "Eficiente"
        else:
            clasificacion = "En observación"
    else:
        limite_critico = meta * 1.20
        if promedio <= limite_critico:
            clasificacion = "Alto"
        else:
            clasificacion = "Crítico"
    
    return clasificacion
 
 
# Función 6: Generar Informe
def generar_informe(comercios):
    """
    Genera informe completo con:
    - Datos de cada comercio (nombre, promedio, variación, clasificación)
    - Conteo de comercios por clasificación
    - Comercio con mayor promedio
    
    Entrada: lista de diccionarios comercios
    Salida: imprime el informe en pantalla
    """
    
    # Variables para el conteo de clasificaciones
    eficientes = 0
    observacion = 0
    altos = 0
    criticos = 0
    
    # Variables para encontrar mayor promedio
    mayor_promedio = 0
    comercio_mayor_promedio = ""
    
    print("\n" + "="*80)
    print("INFORME DE CONSUMO ENERGÉTICO")
    print("="*80)
    
    # Procesar cada comercio
    for comercio in comercios:
        nombre = comercio["nombre"]
        meta = comercio["meta"]
        consumos = comercio["consumos"]
        
        # Calcular promedio y variación
        promedio = calcular_Promedio(consumos)
        variacion = calcular_variacion(consumos)
        
        # Clasificar
        clasificacion = clasificar_consumo(promedio, meta, variacion)
        
        # Mostrar datos del comercio
        print(f"\nComercio: {nombre}")
        print(f"  Promedio: {promedio:.2f} kWh")
        print(f"  Variación: {variacion:.2f}%")
        print(f"  Clasificación: {clasificacion}")
        
        # Contar clasificaciones
        if clasificacion == "Eficiente":
            eficientes = eficientes + 1
        elif clasificacion == "En observación":
            observacion = observacion + 1
        elif clasificacion == "Alto":
            altos = altos + 1
        elif clasificacion == "Crítico":
            criticos = criticos + 1
        
        # Buscar comercio con mayor promedio SIN usar max()
        if promedio > mayor_promedio:
            mayor_promedio = promedio
            comercio_mayor_promedio = nombre
    
    # Mostrar resumen
    print("\n" + "="*80)
    print("RESUMEN POR CLASIFICACIÓN")
    print("="*80)
    print(f"Eficiente: {eficientes} comercio(s)")
    print(f"En observación: {observacion} comercio(s)")
    print(f"Alto: {altos} comercio(s)")
    print(f"Crítico: {criticos} comercio(s)")
    
    print("\n" + "="*80)
    print(f"Comercio con mayor promedio: {comercio_mayor_promedio} ({mayor_promedio:.2f} kWh)")
    print("="*80 + "\n")
 
 
# EJECUCIÓN PRINCIPAL
if __name__ == "__main__":
    comercios = []
    
    print("SISTEMA DE MONITOREO DE CONSUMO ENERGÉTICO")
    print("=" * 50)
    
    # Preguntar cuántos comercios va a registrar
    cantidad_comercios = int(input("\n¿Cuántos comercios desea registrar? "))
    
    # Registrar comercios
    for i in range(cantidad_comercios):
        print(f"\n--- Comercio #{i + 1} ---")
        
        # Función 1: Registrar comercio
        comercio = registrar_Comercio()
        
        # Función 2: Registrar consumos
        comercio = registrar_Consumo(comercio)
        
        comercios.append(comercio)
    
    # Función 6: Generar informe (que usa internamente las funciones 3, 4 y 5)
    generar_informe(comercios)