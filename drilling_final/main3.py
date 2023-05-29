from clases import Automovil, Particular, Carga, Bicicletas, Motocicletas, Vehiculo


particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
particular.guardar_csv()

automovil = Automovil("Ford", "Fiesta", "4", "180", "500")
automovil.guardar_csv()

carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
carga.guardar_csv()
bicicleta = Bicicletas("Shimano", "MT Ranger", 2, "Carrera")
bicicleta.guardar_csv()
motocicleta = Motocicletas("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)
motocicleta.guardar_csv()


Vehiculo.leer_csv()