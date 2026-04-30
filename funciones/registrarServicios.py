import json
def registrarServicios():
    print("Modulo para registrar servicios")
    numero_paquete = int(input("Ingrese el id unico del paquete : "))
    nombre_paquete = input("Ingrese el nombre del paquete fotografico : ")
    try:
        precio = int(input("Ingrese el precio de paque : "))
    except ValueError:
        print("El precio debe ser un numero")
        return
    tipo_evento = input("Para que tipo de evento es el paquete : ")
    duracion = input("ingrese la duración estimada para este paquete en horas: ")
    
    servicio = {
        "id" : numero_paquete,
        "nombre_paquete" : nombre_paquete,
        "precio" : precio,
        "tipo_evento" : tipo_evento,
        "horas_duracion" : duracion
    }
    
    ruta = "archivos/Servicios.json"
    
    try:
        with open(ruta, "r") as servicios:
            try:
                lista_servicios = json.load(servicios)
            except json.JSONDecodeError:
                lista_servicios = []
    except FileNotFoundError:
        lista_servicios = []            
    lista_servicios.append(servicio)
    
    with open(ruta, "w") as archivo:
        json.dump(lista_servicios, archivo, indent=4)
        
    print("Servicio registrado exitosamente")
        