from time import sleep
def numeros_possiveis_aposta(jogador):
    while True:
        try:
            jogador = int(input("Digite um número inteiro de 1 a 10: "))
            if 1 <= jogador <= 10:
                print("Sorteando...")
                sleep(1)
                for i in range(1, 4):
                    print(f"{i}...")
                    sleep(1)
                return jogador
            else:
                print("Tem quer ser de 1 a 10")
                sleep(1)
        except ValueError:
            print("Apenas NÚMEROS de 1 a 10")
            sleep(1)

numeros_possiveis_aposta()