import json

def verServicios():
    ruta = "archivos/Servicios.json"
    try:
        with open(ruta, "r") as archivo:
            lista_servicios = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No hay servicios registrados aún.")
        return

    if not lista_servicios:
        print("La lista de servicios está vacía.")
        return

    for servicio in lista_servicios:
        id_servicio = servicio.get('id', 'N/A')
        nombre = servicio.get('nombre_paquete', 'Sin nombre')
        precio = servicio.get('precio', 0)
        duracion = servicio.get('horas_duracion', '0')
        
        print(f"{id_servicio} | {nombre[:20]} | ${precio} | {duracion} H")