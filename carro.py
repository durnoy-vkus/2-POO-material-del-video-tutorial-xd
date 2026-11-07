class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidad=0
        self.encendido=False
        self.historial_Velocidad=[0]


    def mostrarEstado(self):
        print ("================================")
        print (f"Marca:", self.marca)
        print (f"Modelo:", self.modelo)
        print (f"Ano:", self.ano)
        print (f"Velocidad:", self.velocidad, "km/h")
        print (f"Encendido:", self.encendido)
        print (f"Historial de velocidad:", self.historial_Velocidad)
        print ("================================")
        print ("")

    def encenderCarro(self):
        print ("Modelo: ", self.modelo)
        print("Variable encendido:", self.encendido)
        if self.encendido:
            print ("El carro ya esta encendido ya puedes trabajar en el")
        else:
            self.encendido=True
            print ("El carro ha sido encendido")
            print ("================================")

    def acelerar(self, cantidad):
        #If de vanguardia
        if not self.encendido or cantidad <= 0:
            print ("El carro esta apagado, no puedes acelerar, o la cantidad debe ser mayor a 0")
            return

        #Aqui
        for alias in range(cantidad):
            self.velocidad += 10
            self.historial_Velocidad.append(self.velocidad)
            print("Acelerando... Velocidad actual:", self.velocidad)

    def frenar(self):
        #if de vanguardia
        if not self.encendido or self.velocidad <= 0:
            print ("El carro esta apagado, no puedes frenar, o la cantidad debe ser mayor a 0")
            return

        while self.velocidad > 0:
            self.velocidad -= 10
            self.historial_Velocidad.append(self.velocidad)
            print ("Frenando... Velocidad actual:", self.velocidad)
        