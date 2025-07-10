def niveis_de_apostas(dificuldade):
    match dificuldade:
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 3
        case _:
            return "Escolha outra opção"
     

dificuldade = int(input("Digite"))
niveis_de_apostas(dificuldade)

print(niveis_de_apostas(dificuldade))
