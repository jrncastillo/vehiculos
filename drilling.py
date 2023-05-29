class Vehiculo():
    def __init__(self):
        self.marca = input("Ingrese marca del automovil: ")
        self.modelo = input("Ingrese modelo del automovil: ")
        self.nruedas = int(input("Ingrese cantidad de ruedas: "))

    def __str__(self):
        return (f"**********\nDatos automóvil 1\nMarca: {self.marca}\nModelo: {self.modelo}\nNúmero de ruedas: {self.nruedas}")
    

class Automovil(Vehiculo):
    def __init__(self):
        super().__init__()
        self.velocidad = int(input("Ingrese velocidad en km/hr: "))
        self.cilindrada = float(input("Ingrese cilindraje en cc: "))   

    def __str__(self):
        return (f"*Velocidad en km/h: {self.velocidad}\nCilindraje en cc: {self.cilindrada}\n**********")
    

    


