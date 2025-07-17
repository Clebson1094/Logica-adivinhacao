from random import randint
from time import sleep

print(" === BEM VINDO AO TIGRINHO LITE === ")
sleep(1)
saldo = 0

def codigos_promocionais(carteira):
    while True:
        codigo = str(input("Digite o seu codigo promocional, caso não tenha digite (JOGAR): ")).lower()
        match codigo:
            case "html css kkk" | "se a classe operária tudo produz, a ela tudo pertence" | "virginia" | "jailson utinguense":
                return 50 + carteira
            case "jogar":
                return carteira + 0
            case _:
                print("Codigo inexistente, caso não tenha digite (jogar)")

saldo = codigos_promocionais(saldo)

def niveis_de_apostas():
    while True:
        try:
            dificuldade = int(input((("Escolha seu grau de dificuldade:"
            "\n[1] A rodada Custa 9, Lucro = 9% do saldo"
            "\n[2] A rodada Custa 15, Lucro = 15% do saldo "
            "\n[3] A rodada Custa 20, Lucro = 20% do saldo"
            "\nDIGITE:   "))))
            match dificuldade:
                case 1 | 2 | 3:
                    return dificuldade
                case _:
                    print("Escolha um número válido")
        except ValueError:
            print("Tente novamente com números de 1 a 3")

def deposito(carteira, restante):
    while True:
        try:
            deposito = float(input(f"Seu saldo está R$:{carteira}, precisa de {restante} para iniciar o game: "))
            if deposito <= 0:
                print("Não é aceito deposito zerado ou negativo")
                continue
            else:
                mensagens = ["Carregando deposito...", "Verificando autenticidade...", "Deposito concluído..."]
                tempo = [1, 1.2, 1.8]
                for i, texto in enumerate(mensagens):
                    print(texto)
                    sleep(tempo[i])
                carteira += deposito
                return carteira
        except ValueError:
            print("Coloque o valor em números por favor!")
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

def numeros_possiveis_aposta():
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
        except ValueError:
            print("Apenas NÚMEROS de 1 a 10")

while True:
    try:
        numero_bot = randint(1, 10)
        if saldo < 50:
            diferença = 50 - saldo
            saldo = deposito(saldo, diferença)
        else:
            try:
                nivel = niveis_de_apostas()
                print(f"Você tem {saldo} de saldo, vamos jogar")
                usuario = numeros_possiveis_aposta()
                saldo = aposta(usuario, numero_bot, saldo, nivel)
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