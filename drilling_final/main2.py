from clases import Vehiculo,Automovil, Bicicletas, Carga, Particular, Motocicletas

particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicletas("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicletas("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

print("")
print(particular)
print("")
print(carga)
print("")
print(bicicleta)
print("")
print(motocicleta)
print("")

print(f"Motocicleta es instancia con relación a Vehículo: {isinstance(motocicleta,Vehiculo)}")
print(f"Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta,Automovil)}")
print(f"Motocicleta es instancia con relación a Particular: {isinstance(motocicleta,Particular)}")
print(f"Motocicleta es instancia con relación a Carga: {isinstance(motocicleta,Carga)}")
print(f"Motocicleta es instancia con relación a Bicicletas: {isinstance(motocicleta,Bicicletas)}")
print(f"Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta,Motocicletas)}")