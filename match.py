opcionSeleccionar = input("Seleccione una familia de la tabla periodica: ")

match opcionSeleccionar:
    case 1:
        print("Seleccionaste la familia de los metales alcalinos")
        print("Estos son los elementos de la familia de los metales alcalinos")
        print("1.- Litio (Li)")
    case 2:
        print("Seleccionaste la familia de los metales alcalinoterreos")
        print("Estos son los elementos de la familia de los metales alcalinoterreos")
        print("1.- Berilio (Be)")
    case 3:
        print("Seleccionaste la familia de los metales de transición")
        print("Estos son los elementos de la familia de los metales de trasnsición")
        print("1.- Hierro (Fe)")
    case 4:
        print("Seleccionaste la familia de los metales del bloque p")
        print("Estos son los elementos de la familia de los metales del bloque p")
        print("1.- Galio (Ga)")
    case 5:
        print("Seleccionaste la familia de los metales del bloque d")
        print("Estos son los elementos de la familia de los metales del bloque d")
        print("1.- Magnesio (Mg)")
    case _:
        print("Opcion no valida")