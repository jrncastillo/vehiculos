import csv

class Vehiculo():
    def __init__(self, marca, modelo, nruedas):
        self.marca = marca
        self.modelo = modelo
        self.nruedas = nruedas

    def __str__(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nN° Ruedas: {self.nruedas}"
        

    def guardar_csv(self):
        try:
            with open("vehiculos.csv", "a",newline="") as archivo:
                datos = [(self.__class__, self.__dict__)]
                archivo_csv = csv.writer(archivo)
                archivo_csv.writerows(datos)

        except Exception as error:
            print(f"Error capturado {error}")
            
    @staticmethod        
    def leer_csv():
        try:
            with open("vehiculos.csv", "a",newline="") as archivo:
                vehiculos = csv.reader(archivo)
                for item in vehiculos:
                    print(item)
        except:
            pass

    def recuperar(self,nombre_archivo):
        vehiculos = []
        archivo = open(nombre_archivo, "r")
        archivo_csv = csv.reader(archivo)
        for vehiculo in archivo_csv:
            vehiculos.append(vehiculo)
        archivo.close()
        return vehiculos

class Automovil(Vehiculo):

    def __init__(self, marca, modelo, nruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, nruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + f"\nVelocidad en km/h: {self.velocidad}\nCilindraje en cc: {self.cilindrada}"

    def imprimir_automovil(self):

        return print(f"***********************\nMarca: {self.marca}\nModelo: {self.modelo}\nN° Ruedas: {self.nruedas}\nVelocidad (km/h): {self.velocidad}\nCilindraje (cc): {self.cilindrada}\n***********************\n")

##########################################################
class Bicicletas(Vehiculo):
    def __init__(self, marca, modelo, nruedas, tipo):
        super().__init__(marca, modelo, nruedas)
        self.tipo = tipo

    def __str__(self):
        return Vehiculo.__str__(self) + (f"\nTipo : {self.tipo}")

class Motocicletas(Bicicletas):
    def __init__(self, marca, modelo, nruedas, tipo, nradios, cuadro, motor):
        super().__init__(marca, modelo, nruedas, tipo)
        self.nradios = nradios
        self.cuadro = cuadro
        self.motor = motor

    def __str__(self):
        return Bicicletas.__str__(self) + (f"\nN° de Radios: {self.nradios}\nCuadro : {self.cuadro}\nMotor : {self.motor}")
###########################################################

###########################################################
class Carga(Automovil):
    def __init__(self, marca, modelo, nruedas, velocidad, cilindrada, pesocarga):
        super().__init__(marca, modelo, nruedas, velocidad, cilindrada)
        self.pesocarga = pesocarga

class Particular(Automovil):
    def __init__(self, marca, modelo, nruedas, velocidad, cilindrada, npuestos):
        super().__init__(marca, modelo, nruedas, velocidad, cilindrada)
        self.npuestos = npuestos

    def get_npuestos(self):
        return self.npuestos

    def set_npuesto(self, nuevo):
        self.npuestos = nuevo
        pass
###########################################################

