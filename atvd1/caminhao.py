class Veiculo():
    def __init__ (self, placa, modelo, km_atual, motorista = ""):
        self.placa = placa
        self.modelo = modelo
        self.km_atual = km_atual
        self.motorista = motorista

    def atualizar(self, km_novo):
        self.km_atual += km_novo
