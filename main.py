opcion = 1
while (opcion != 5):
    print("BIENVENIDO A PhotoCampus")
    print("1. Registrar Servicios")
    print("2. Editar Servicios")
    print("3. Eliminar Servicios")
    print("4. Ver todos los servicios")
    print("5. Salir")
    opcion = int(input("Ingrese una opcion : "))
    
    match opcion:
        case 1:
            registrarServicios()
        case 2:
            editarServicios()
        case 3:
            eliminarServicios()
        case 4:
            verServicios()
        case 5:
            print("Hasta luego, que vuelvas pronto")
            print("Saliendo......")
            break
        case _:
            print("Opcion invalida, por favor comience de nuevo")