from clases import Automovil

def ingreso_automovil():
    lista = []
    cantidad = int(input("\nIngrese cantidad de Vehiculos a ingresar: "))
    for item in range(cantidad):
        print(f"\nIngrese datos del automovil {item+1}")
        print("")
        marca = input("Ingrese MARCA del automovil: ")
        modelo = input("Ingrese MODELO del automovil: ")
        nruedas = int(input("Ingrese NUMERO DE RUEDAS: "))
        velocidad = int(input("Ingrese VELOCIDAD en km/hr: "))
        cilindrada = int(input("Ingrese CILINDRAJE en cc: "))
        auto = Automovil(marca, modelo, nruedas, velocidad, cilindrada)
        lista.append(auto)
        print("")
    return lista

def imprimir_automovil(lista):

    for index,item in enumerate(lista):
        print(f"***********************\nDatos automóvil -{index+1}-\n-----------------------\nMarca: {item.marca}\nModelo: {item.modelo}\nN° Ruedas: {item.nruedas}\nVelocidad (km/h): {item.velocidad}\nCilindraje (cc): {item.cilindrada}\n***********************\n")

###########################################################################

autos = ingreso_automovil()

imprimir_automovil(autos)