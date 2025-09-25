import time

class Fuel_pump:
    def __init__(self):
        self.ligado = False
        self.valor = 0
        self.quantidade = 0
        self.combustivel = ""
        self.precoPorLitro = 0
        self.tanqueDoCliente = 0
        self.capacidade = 100

    def showSluppy(self):
        litros = 0
        valor_total = 0
        incremento = 0.1
        while litros < self.quantidade:
            litros += incremento
            if litros > self.quantidade:
                litros = self.quantidade
            valor_total = litros * self.precoPorLitro
            print(f"\rAbastecendo... {litros:.2f}L - R${valor_total:.2f}", end="")
            time.sleep(0.1)
        print()

    def informationFullTank(self):
        print(f"Tanque do cliente está cheio: {self.capacidade}L")

    def fuel(self, quantidade):
        self.tanqueDoCliente += quantidade

    def fuelForValue(self, valor):
        if self.ligado:
            self.valor = valor
            self.quantidade = self.valor / self.precoPorLitro
            if self.quantidade + self.tanqueDoCliente > self.capacidade:
                self.informationFullTank()
            else:
                self.fuel(self.quantidade)
                self.showSluppy()

    def fuelForLiters(self, litros):
        if self.ligado:
            self.quantidade = litros
            self.valor = self.quantidade * self.precoPorLitro
            if self.quantidade + self.tanqueDoCliente > self.capacidade:
                self.informationFullTank()
            else:
                self.fuel(self.quantidade)
                self.showSluppy()

    def selectFuel(self, tipo):
        
        match tipo:
            case 1:
                self.combustivel = "Gasolina"
                self.precoPorLitro = 5.30
            case 2:
                self.combustivel = "Etanol"
                self.precoPorLitro = 4.90
            case 3:
                self.combustivel = "Diesel"
                self.precoPorLitro = 3.90
            case _:
                pass


    def printMenu(self):
        print("Selecione o tipo de combustível:")
        print("1 - Gasolina - R$5.30/L")
        print("2 - Etanol - R$4.90/L")
        print("3 - Diesel - R$3.90/L")
        print("0 - Sair")

abastecer = Fuel_pump()

while True:
    try:
        opção = int(input("Abastecer por valor (1) ou por litros (2)? "))

        match opção:
            
            case 1:
                while True:
                    abastecer.printMenu()
                    try:
                        tipo = int(input("Digite o número correspondente ao combustível desejado: "))
                        if tipo == 0:
                            print("Encerrando o atendimento.")
                            break
                        abastecer.selectFuel(tipo)
                        if abastecer.combustivel == "":
                            print("Opção inválida. Tente novamente.")
                            continue
                        abastecer.ligado = True
                        valor = float(input(f"Digite o valor em reais para abastecer com {abastecer.combustivel}: R$"))
                        abastecer.fuelForValue(valor)
                        abastecer.ligado = False
                        print(f"Abastecido {abastecer.quantidade:.2f}L de {abastecer.combustivel}.")
                        print(f"Total no tanque do cliente: {abastecer.tanqueDoCliente:.2f}L")
                        break
                    except KeyboardInterrupt:
                        print("\nAtendimento interrompido pelo usuário.")
                        break


                    except ValueError:
                        print("Valor inválido. Tente novamente.")
            case 2:
                while True:
                    abastecer.printMenu()
                    try:
                        tipo = int(input("Digite o número correspondente ao combustível desejado: "))
                        if tipo == 0:
                            print("Encerrando o atendimento.")
                            break
                        abastecer.selectFuel(tipo)
                        if abastecer.combustivel == "":
                            print("Opção inválida. Tente novamente.")
                            continue
                        abastecer.ligado = True
                        litros = float(input(f"Digite a quantidade de litros para abastecer com {abastecer.combustivel}: L"))
                        abastecer.fuelForLiters(litros)
                        abastecer.ligado = False
                        print(f"Abastecido {abastecer.quantidade:.2f}L de {abastecer.combustivel}.")
                        print(f"Total no tanque do cliente: {abastecer.tanqueDoCliente:.2f}L")
                        break
                    except KeyboardInterrupt:
                        print("\nAtendimento interrompido pelo usuário.")
                        break
                    except ValueError:
                        print("Valor inválido. Tente novamente.")
            case _:
                print("Opção inválida. tente novamente.")
    except ValueError:
        print("Valor inválido. Tente novamente.")