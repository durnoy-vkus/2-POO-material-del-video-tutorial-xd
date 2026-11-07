from carro import Carro

def main():
    impala = Carro("Chevrolet", "Impala", 1967)

    while True:
        print("")
        print("\n")
        print("Seleccione una opción:")
        print("1. Encender carro")
        print("2. Acelerar carro")
        print("3. Frenar carro")
        print("4. Mostrar estado del carro")
        print("5. Salir")
        print("===============================")

        opcion = input("Ingrese el número de la opción deseada: ")

        match opcion:
            case "1":
                impala.encenderCarro()
            case "2":
                cantidad = int(input("Ingrese la cantidad de veces que desea acelerar (cada vez aumenta 10 km/h): "))
                impala.acelerar(cantidad)
            case "3":
                impala.frenar()
            case "4":
                impala.mostrarEstado()
            case "5":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()