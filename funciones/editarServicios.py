import json

def editarServicios():
    ruta = "archivos/Servicios.json"
    try:
        with open(ruta, "r") as archivo:
            lista_servicios = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No hay servicios registrados para editar.")
        return
    try:
        id_buscar = int(input("Ingrese el ID del servicio que desea editar: "))
    except ValueError:
        print("ID no válido.")
        return

    servicio_encontrado = None
    for servicio in lista_servicios:
        if servicio['id'] == id_buscar:
            servicio_encontrado = servicio
            break
    if not servicio_encontrado:
        print("Servicio no encontrado.")
        return
    print(f"Editando: {servicio_encontrado['nombre_paquete']}")
    print("1. Nombre del paquete")
    print("2. Precio")
    print("3. Tipo de evento")
    print("4. Horas de duracion")    
    opcion = input("Elija el número del campo que desea editar: ")

    if opcion == "1":
        servicio_encontrado['nombre_paquete'] = input("Nuevo nombre: ")
    elif opcion == "2":
        try:
            servicio_encontrado['precio'] = int(input("Nuevo precio: "))
        except ValueError:
            print("Precio inválido, no se realizaron cambios.")
            return
    elif opcion == "3":
        servicio_encontrado['tipo_evento'] = input("Nuevo tipo de evento: ")
    elif opcion == "4":
        servicio_encontrado['horas_duracion'] = input("Nueva duración: ")
    else:
        print("Opción no válida.")
        return
    
    with open(ruta, "w") as archivo:
        json.dump(lista_servicios, archivo, indent=4)
    
    print("Servicio actualizado exitosamente")