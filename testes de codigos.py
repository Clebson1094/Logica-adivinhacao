vitorias = 0
derrotas = 0

bot = 2

while True:
    humano = int(input("Digite"))
    if humano == bot:
        vitorias += 1
    else:
        derrotas += 1
        humano = False

    print(vitorias, derrotas)
    print(bool(humano))