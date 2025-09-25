class Eloisa:
    def __init__(self):
        self.name = "Eloisa"
        self.peso = "Magrela"
        self.força = "Inexistente"

    def atacar(self):
        print(f"{self.name} tentou atacar, mas não conseguiu.")

eloisa = Eloisa()

while True:
    escolha = int(input("Digite o que você quer fazer:\n[1] Atacar\n[2] Exibir força\n[3] Exibir tipo de corpo\n"))
    match escolha:
        case 1:
            eloisa.atacar()
        case 2:
            print(f"A força de {eloisa.name} é: {eloisa.força}")
        case 3:
            print(f"O tipo de corpo de {eloisa.name} é: {eloisa.peso}")