def numeros_possiveis_aposta(jogador):
    try:
        if jogador >= 1 and jogador <= 10:
            return True
        else:
            return False
    except ValueError:
        return False
    
champs = int(input("Digite"))

if numeros_possiveis_aposta(champs):
    print("ok")
else:
    print("no")