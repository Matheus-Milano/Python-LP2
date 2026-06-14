class OrdemServico():
    def __init__(self, caminhao, num_protocolo, desc_problema, motorista, status = "Aberta"):
        self.caminhao = caminhao
        self.num_protocolo = num_protocolo
        self.desc_problema = desc_problema
        self.motorista = motorista
        self.status = status

    def atualizarStatus(self, status_atual):
        self.status = status_atual
        print(f"Status: {self.status}, Motorista: {self.motorista.nome}")