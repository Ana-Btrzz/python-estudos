class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):  # self ou this
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    # Métodos:
    def buzinar(self):
        print("plim plim")

    def parar(self):
        print("parando bicicleta")
        print("parou!")

    def correr(self):
        print("Vruummm")

    def __str__(self):
        return f"bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"


# criar a instancia para a classe:
b1 = Bicicleta("vermelha", "caloi", 2022, 600)
print(b1)

b1.buzinar()
b1.correr()
b1.parar()

# Bicicleta.parar(b1)
# Bicicleta.correr(b1)
# Bicicleta.buzinar(b1)
