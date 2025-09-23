from time import sleep
from colorama import Fore

class Semafaro:
    def __init__(self):
        self.situação = "vermelho"
        self.time = 10

    def vermelho(self):
        while True:
            if self.time == 0:
                self.time += 15
                self.situação = "verde"
                break
            else:
                self.time -= 1
                sleep(1.5)
                print(self.time)
        return self.time

    def verde(self):
        while True:
            if self.time == 0:
                self.time += 5
                self.situação = "amarelo"
                break
            else:
                self.time -= 1
                sleep(1.5)
                print(self.time)
        return self.situação

    def amarelo(self):
        while True:
            if self.time == 0:
                self.time += 10
                self.situação = "vermelho"
                break
            else:
                self.time -= 1
                sleep(1.5)
                print(self.time)

bora = Semafaro()

while True:
    if bora.situação == "vermelho":
        print(Fore.RED + f"{bora.situação}")
        bora.vermelho()
    elif bora.situação == "verde":
        print(Fore.GREEN + f"{bora.situação}")
        bora.verde()
    elif bora.situação == "amarelo":
        print(Fore.YELLOW + f"{bora.situação}")
        bora.amarelo()