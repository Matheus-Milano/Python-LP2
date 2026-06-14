class Animal:
    def __init__(self, nome, energia, fome, raca, tutor):
        self.fome = fome
        self.energia = energia
        self.nome = nome
        self.raca = raca
        self.tutor = tutor

    def alimentar(self):
        if self.fome >= 100:
            print(f"O {self.nome} está cheio")
        else:
            self.fome += 20
            self.energia += 30
            print(f"O {self.nome} se alimentou e está com {self.energia}% de energia, e {self.fome}% de fome")


    def brincar(self):
        if self.energia > 20:
            self.energia -= 20
            print(f"O {self.nome} brincou e ficou com {self.energia}% de energia")
        else:
            print(f"O {self.nome} não tem energia o suficiente para brincar")


    def informar_estado(self):
        print(f"O {self.nome} está com {self.fome}% sem fome, e com {self.energia}% de energia")

animal = Animal('Gersu', 60, 30, 'Gersu', 'Eu')

animal.brincar()
animal.brincar()
animal.alimentar()
animal.alimentar()
animal.informar_estado()