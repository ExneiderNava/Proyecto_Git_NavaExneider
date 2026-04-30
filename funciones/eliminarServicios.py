import json

def eliminarServicios():
    ruta = "archivos/Servicios.json"
    
    try:
        with open(ruta, "r") as archivo:
            lista_servicios = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No hay servicios registrados.")
        return
    try:
        id_eliminar = int(input("Ingrese el ID del servicio que desea eliminar: "))
    except ValueError:
        print("El ID debe ser un número.")
        return
    encontrado = False
    
    for i in range(len(lista_servicios)):
        if lista_servicios[i]['id'] == id_eliminar:
            print(f"Servicio encontrado: {lista_servicios[i]['nombre_paquete']}")
            print("¿Seguro que deseas eliminarlo?")
            print("1. SI")
            print("2. NO")
            confirmar = int(input("Ingrese una opcion : "))
            if confirmar == 1:
                lista_servicios.pop(i)
                encontrado = True
                break
            else:
                print("Eliminación cancelada.")
                return

    if not encontrado:
        print(f"No se encontró ningún servicio con el ID {id_eliminar}")
        return
    
    with open(ruta, "w") as archivo:
        json.dump(lista_servicios, archivo, indent=4)
    
    print("¡Servicio eliminado con éxito!")