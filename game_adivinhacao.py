from random import randint
from time import sleep

print(" === BEM VINDO AO TIGRINHO LITE === ")

saldo = 0

codigo = ["jaca", "xwp", "jamelao"]
codigo_jogador = str(input("Digite seu codigo promocial, ou (NÃO) para continuar: ")).strip().lower()
negação = ["n", "não", "nao", "no"]

if codigo_jogador in codigo:
    saldo += 50
    print("Codigo promocional aceito, adicionado R$:50,00 ao seu saldo")
elif codigo_jogador in negação:
    print("Vamos continuar")
else:
    print("Não entendi o que quis dizer, vamos continuar")
    
def aposta(jogador, bot, saldo, ganho):
    if ganho == 1:
        if jogador == bot:
            saldo += saldo * 9 / 100
            print(f"PARABENS!! O número escolhido foi {bot} Você aumento seu saldo em 9%, seu novo saldo R$:{saldo}")
        else:
            saldo -= 9
            print(f"Que pena, o número escolhido era {bot}, foi debitado R$:9 de seu saldo ficando {saldo}")
            sleep(1)
            print("Vamos girar novamente")
    elif ganho == 2:
        if jogador == bot:
            saldo += saldo * 15 / 100
            print(f"PARABENS!! O número escolhido foi {bot} Você aumento seu saldo em 15%, seu novo saldo R$:{saldo}")
        else:
            saldo -= 15
            print(f"Que pena, o número escolhido era {bot}, foi debitado R$:15 de seu saldo ficando {saldo}")
            sleep(1)
            print("Vamos girar novamente")
    else:        
        if jogador == bot:
            saldo += saldo * 20 / 100
            print(f"PARABENS!! O número escolhido foi {bot} Você aumento seu saldo em 20%, seu novo saldo R$:{saldo}")
        else:
            saldo -= 20
            print(f"Que pena, o número escolhido era {bot}, foi debitado R$:20 de seu saldo ficando {saldo}")
            sleep(1)
            print("Vamos girar novamente")
    return saldo

while True:
    try:
        numero_bot = randint(1, 10)
        if saldo < 50:
            diferença = 50 - saldo
            deposito = int(input(f"Seu saldo está R$:{saldo}, precisa de {diferença} para iniciar o game: "))
            saldo += deposito
        else:
            dificuldade = int(input("Escolha seu grau de dificuldade:\n[1] A rodada Custa 9, Lucro = 9% do saldo \n[2] A rodada Custa 15, Lucro = 15% do saldo \n[3] A rodada Custa 20, Lucro = 20% do saldo "))
            print(f"Você tem {saldo} de saldo, vamos jogar")
            usuario = int(input("Escolha um número de 1 a 10: "))
            print("Sorteando...")
            sleep(1)
            for i in range(1, 10):
                if i <= 3:
                    print(f"{i}...")
                    sleep(1)
                else:
                    break
            saldo = aposta(usuario, numero_bot, saldo, dificuldade)
            sleep(1.5)
            
    except ValueError:
        continuar = input("Não consegui compreender o que disse, deseja continuar? (s/n)")
        if continuar != "s":
            print("Encerrando...")
            break
        else:
            print("Vamos lá")
            continue