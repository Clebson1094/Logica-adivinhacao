from random import randint
from time import sleep

print(" === BEM VINDO AO TIGRINHO LITE === ")
sleep(1.5)
saldo = 0

opcoes_dificuldade = [1, 2, 3]

def dificuldade(opcoes):
    while True:
        escolha = int(input("Escolha seu grau de dificuldade:\n[1] A rodada Custa 9, Lucro = 9% do saldo \n[2] A rodada Custa 15, Lucro = 15% do saldo \n[3] A rodada Custa 20, Lucro = 20% do saldo "))
        if escolha not in opcoes:
            print("Escolha somente algumas das opções citadas por gentileza")
            continue
        elif escolha == 1:
            return 1
        elif escolha == 2:
            return 2
        elif escolha == 3:
            return 3
        else:
            print("Não entendi o que quis dizer, tente novamente")
            continue
        
def aposta(jogador, bot, saldo, ganho):
    custos = {1: 9, 2: 15, 3: 20}
    lucros = {1: 0.09, 2: 0.15, 3: 0.20}
    custo = custos[ganho]
    lucro = lucros[ganho]

    if jogador == bot:
        saldo += saldo * lucro
        print(f"PARABENS!!! O número escolhido foi {bot}, já foi depositado em seu saldo seu lucro, ficando com R$:{saldo}")
    else:
        saldo -= custo
        print(f"Que pena o número escolhido foi {bot}, foi debitado {custo}")
        sleep(1)
        print("Vamos girar novamente")
    return saldo

def numeros_possiveis_aposta(jogador):
    return 1 <= jogador <= 10

while True:
    try:
        numero_bot = randint(1, 10)
        if saldo < 50:
            diferença = 50 - saldo
            try:
                deposito = float(input(f"Seu saldo está R$:{saldo}, precisa de {diferença} para iniciar o game: "))
                saldo += deposito
                sleep(1)
                print("Carregando déposito...")
                sleep(1.2)
                print("Verificando veracidade")
                sleep(1.9)
                print("Concluído")
            except ValueError:
                print("Tu quer depositar letras? digite número por gentileza...")
                sleep(1.5)
        else:
            try:
                nivel = dificuldade(opcoes_dificuldade)
                print(f"Você tem {saldo} de saldo, vamos jogar")
                usuario = int(input("Digite um número inteiro de 1 a 10: "))
                if numeros_possiveis_aposta(usuario):
                    print("Sorteando...")
                    sleep(1)
                    for i in range(1, 4):
                        print(f"{i}...")
                        sleep(1)
                    saldo = aposta(usuario, numero_bot, saldo, nivel)
                    sleep(1.5)
                else:
                    print("Apenas número de 1 a 10... recomeçando")
                    sleep(1.5)
            except ValueError:
                print("Tu não sabe ler não bixo?")
                sleep(1.5)
    except ValueError:
        continuar = input("Não consegui compreender o que disse, deseja continuar? (s/n) ")
        if continuar != "s":
            print("Encerrando...")
            break
        else:
            print("Vamos lá")
            continue